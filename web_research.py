"""
Web research module for fetching, parsing, and searching web content.

Search backend: SearXNG (zero cost) with SerpAPI fallback.
"""

import httpx
from bs4 import BeautifulSoup
from readability import Document
import re
import logging

logger = logging.getLogger(__name__)


async def fetch_and_parse(url: str, timeout: float = 15.0) -> dict:
    """Fetch a URL and extract readable content."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    async with httpx.AsyncClient(follow_redirects=True, timeout=timeout) as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()

    doc = Document(response.text)
    title = doc.title()
    html_content = doc.summary()

    soup = BeautifulSoup(html_content, "lxml")

    # Remove script and style elements
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Truncate very long pages
    max_chars = 12000
    truncated = len(text) > max_chars
    if truncated:
        text = text[:max_chars] + "\n\n[... content truncated ...]"

    return {
        "url": str(response.url),
        "title": title,
        "content": text,
        "content_length": len(text),
        "truncated": truncated,
        "status_code": response.status_code,
    }


async def fetch_multiple(urls: list[str]) -> list[dict]:
    """Fetch multiple URLs concurrently."""
    results = []
    for url in urls[:5]:  # Cap at 5 concurrent
        try:
            result = await fetch_and_parse(url)
            results.append(result)
        except Exception as e:
            results.append({"url": url, "error": str(e)})
    return results


# ── Search ────────────────────────────────────────────────────────────

def web_search(
    query: str,
    num_results: int = 10,
    categories: str = "general",
    engines: str | None = None,
    time_range: str | None = None,
) -> dict:
    """
    Search the web using SearXNG (primary) or SerpAPI (fallback).

    Args:
        query: Search query string.
        num_results: Maximum number of results.
        categories: SearXNG categories (general, science, it, news, etc.)
        engines: Restrict to specific engines (duckduckgo, brave, arxiv, etc.)
        time_range: Filter by recency (day, week, month, year).

    Returns:
        dict with keys: results (list of {url, title, snippet, engine}),
        query, backend, error (None if success).
    """
    # Try SearXNG first
    try:
        from searxng_client import search, is_available
        if is_available():
            data = search(
                query,
                categories=categories,
                engines=engines,
                time_range=time_range,
                max_results=num_results,
            )
            results = []
            for r in data.get("results", []):
                results.append({
                    "url": r.get("url", ""),
                    "title": r.get("title", ""),
                    "snippet": r.get("content", ""),
                    "engine": r.get("engine", ""),
                    "score": r.get("score", 0),
                })
            return {
                "query": query,
                "results": results,
                "suggestions": data.get("suggestions", []),
                "infoboxes": data.get("infoboxes", []),
                "backend": "searxng",
                "error": None,
            }
    except Exception as e:
        logger.warning("SearXNG search failed, trying SerpAPI: %s", e)

    # Fallback to SerpAPI
    import os
    key = os.environ.get("SERPAPI_KEY", "").strip()
    if not key:
        return {
            "query": query,
            "results": [],
            "backend": None,
            "error": "No search backend available. Set CHAPTERS_PASSWORD (SearXNG) or SERPAPI_KEY.",
        }

    try:
        import httpx as hx
        resp = hx.get(
            "https://serpapi.com/search.json",
            params={"engine": "google", "q": query, "num": num_results, "api_key": key, "hl": "en"},
            timeout=20.0,
        )
        resp.raise_for_status()
        data = resp.json()
        results = []
        for item in data.get("organic_results", [])[:num_results]:
            results.append({
                "url": item.get("link", ""),
                "title": item.get("title", ""),
                "snippet": item.get("snippet", ""),
                "engine": "google",
                "score": 0,
            })
        return {
            "query": query,
            "results": results,
            "suggestions": [],
            "infoboxes": [],
            "backend": "serpapi",
            "error": None,
        }
    except Exception as e:
        return {"query": query, "results": [], "backend": "serpapi", "error": str(e)}
