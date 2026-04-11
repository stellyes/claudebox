"""
SearXNG Client — Zero-cost metasearch via the Chapters search endpoint.

Replaces SerpAPI ($0.025/query, $5/month cap) for fringe probes and
general web research. The SearXNG instance at search.chaptersdata.com
fans out to 8 engines (DuckDuckGo, Brave, Mojeek, Wikipedia, Wikidata,
GitHub, StackExchange, arXiv) — zero per-query cost.

Authentication: AWS Cognito JWT via USER_PASSWORD_AUTH.
Requires CHAPTERS_PASSWORD in .env.
"""

import os
import time
import json
import logging
from typing import Optional

import boto3
import requests

logger = logging.getLogger(__name__)

# ── Configuration ─────────────────────────────────────────────────────

SEARXNG_URL = "https://search.chaptersdata.com"
COGNITO_REGION = "us-west-1"
COGNITO_CLIENT_ID = "7i0tnb4v8c8i99sb9nq8eoqnnp"
COGNITO_USERNAME = "info@chaptersdata.com"

# Token cache
_token_cache = {
    "id_token": None,
    "expires_at": 0,
}


# ── Auth ──────────────────────────────────────────────────────────────

def _get_password() -> str:
    """Get the Chapters password from environment."""
    pw = os.environ.get("CHAPTERS_PASSWORD", "")
    if not pw:
        raise ValueError(
            "CHAPTERS_PASSWORD not set. Add it to .env in the claudebox directory."
        )
    return pw


def _authenticate() -> str:
    """
    Authenticate with Cognito and return an ID token.
    Caches the token for its lifetime (1 hour).
    """
    now = time.time()
    if _token_cache["id_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["id_token"]

    password = _get_password()
    cognito = boto3.client("cognito-idp", region_name=COGNITO_REGION)

    resp = cognito.initiate_auth(
        ClientId=COGNITO_CLIENT_ID,
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={
            "USERNAME": COGNITO_USERNAME,
            "PASSWORD": password,
        },
    )

    result = resp["AuthenticationResult"]
    _token_cache["id_token"] = result["IdToken"]
    _token_cache["expires_at"] = now + result.get("ExpiresIn", 3600)

    logger.debug("SearXNG: authenticated, token expires in %ds", result.get("ExpiresIn", 3600))
    return _token_cache["id_token"]


# ── Search ────────────────────────────────────────────────────────────

def search(
    query: str,
    categories: str = "general",
    engines: Optional[str] = None,
    time_range: Optional[str] = None,
    language: str = "en-US",
    max_results: int = 10,
    pageno: int = 1,
) -> dict:
    """
    Search via the SearXNG endpoint.

    Args:
        query: Search query string. Supports bangs (!g, !wp), site:, "exact phrase".
        categories: Comma-separated. Options: general, images, videos, news, music,
                    files, it, science, social_media, map. Default: general.
        engines: Comma-separated engine filter. Options: duckduckgo, brave, mojeek,
                 wikipedia, wikidata, github, stackexchange, arxiv.
        time_range: Filter by recency: day, week, month, year.
        language: BCP47 language code. Default: en-US.
        max_results: Max results to return (truncates the response).
        pageno: Page number for pagination.

    Returns:
        dict with keys: results (list), suggestions (list), infoboxes (list),
        query (str), unresponsive_engines (list).
    """
    token = _authenticate()

    params = {
        "q": query,
        "format": "json",
        "categories": categories,
        "language": language,
        "pageno": str(pageno),
    }
    if engines:
        params["engines"] = engines
    if time_range:
        params["time_range"] = time_range

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    # Retry with backoff on 429
    for attempt in range(3):
        resp = requests.post(
            f"{SEARXNG_URL}/search",
            data=params,
            headers=headers,
            timeout=30,
        )

        if resp.status_code == 429:
            wait = 2 ** (attempt + 1)  # 2, 4, 8 seconds
            logger.warning("SearXNG rate limited (429), backing off %ds", wait)
            time.sleep(wait)
            continue

        if resp.status_code == 401:
            # Token expired mid-request; force re-auth
            _token_cache["id_token"] = None
            token = _authenticate()
            headers["Authorization"] = f"Bearer {token}"
            continue

        resp.raise_for_status()
        data = resp.json()

        # Truncate results to max_results
        if "results" in data:
            data["results"] = data["results"][:max_results]

        return data

    raise RuntimeError("SearXNG search failed after 3 attempts")


def search_simple(query: str, num_results: int = 10) -> list[dict]:
    """
    Simplified search that returns just a list of result dicts.
    Each result has: url, title, content (snippet), engine, score.

    Drop-in replacement for SerpAPI organic results.
    """
    data = search(query, max_results=num_results)
    results = []
    for r in data.get("results", []):
        results.append({
            "url": r.get("url", ""),
            "title": r.get("title", ""),
            "snippet": r.get("content", ""),
            "engine": r.get("engine", ""),
            "engines": r.get("engines", []),
            "score": r.get("score", 0),
        })
    return results


def search_academic(query: str, num_results: int = 10) -> list[dict]:
    """Search arXiv specifically for academic/research queries."""
    return search_simple(
        query,
        num_results=num_results,
    )


def is_available() -> bool:
    """Check if the SearXNG endpoint is configured and reachable."""
    try:
        _get_password()
        return True
    except ValueError:
        return False
