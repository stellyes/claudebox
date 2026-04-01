"""
Web wandering module for serendipitous discovery.
Follows links semi-randomly from a starting URL to simulate
the experience of browsing without a destination.
"""

import httpx
import random
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from readability import Document


# Domains to skip during wandering
SKIP_DOMAINS = {
    "facebook.com", "twitter.com", "x.com", "instagram.com", "tiktok.com",
    "linkedin.com", "youtube.com", "reddit.com", "pinterest.com",
    "amazon.com", "ebay.com", "walmart.com",
    "google.com", "bing.com", "yahoo.com",
    "login", "signin", "signup", "account", "cart", "checkout",
}

SKIP_EXTENSIONS = {
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp",
    ".mp3", ".mp4", ".wav", ".avi", ".mov",
    ".zip", ".tar", ".gz", ".exe", ".dmg",
    ".css", ".js", ".json", ".xml",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}


def _is_valid_link(href: str, base_domain: str) -> bool:
    """Filter out navigation junk, self-links, and unwanted destinations."""
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return False
    parsed = urlparse(href)
    domain = parsed.netloc.lower()
    path = parsed.path.lower()

    # Skip social media, commerce, auth pages
    for skip in SKIP_DOMAINS:
        if skip in domain or skip in path:
            return False

    # Skip binary file extensions
    for ext in SKIP_EXTENSIONS:
        if path.endswith(ext):
            return False

    # Require http(s)
    if parsed.scheme and parsed.scheme not in ("http", "https"):
        return False

    return True


def _extract_links(html: str, base_url: str) -> list[dict]:
    """Extract and score links from a page."""
    soup = BeautifulSoup(html, "lxml")
    base_domain = urlparse(base_url).netloc

    # Remove nav, footer, sidebar — focus on content links
    for tag in soup(["nav", "footer", "aside", "header"]):
        tag.decompose()

    links = []
    seen_urls = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"].strip()
        full_url = urljoin(base_url, href)
        normalized = full_url.split("?")[0].split("#")[0]  # strip params/fragments

        if normalized in seen_urls:
            continue
        if not _is_valid_link(full_url, base_domain):
            continue

        seen_urls.add(normalized)

        # Get link text and surrounding context
        link_text = a_tag.get_text(strip=True)
        if not link_text or len(link_text) < 5:
            continue

        # Score: prefer links with substantial text, external links get bonus
        link_domain = urlparse(full_url).netloc
        is_external = link_domain != base_domain
        text_length_score = min(len(link_text) / 50, 1.0)
        external_bonus = 0.3 if is_external else 0.0

        links.append({
            "url": full_url,
            "text": link_text[:200],
            "is_external": is_external,
            "score": text_length_score + external_bonus + random.random() * 0.5,
        })

    return links


def _extract_readable(html: str, url: str) -> dict:
    """Extract readable content from HTML."""
    doc = Document(html)
    title = doc.title()
    summary_html = doc.summary()
    soup = BeautifulSoup(summary_html, "lxml")
    for tag in soup(["script", "style"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)

    max_chars = 6000  # shorter than full fetch — we're browsing, not deep-reading
    truncated = len(text) > max_chars
    if truncated:
        text = text[:max_chars] + "\n\n[... truncated for wandering ...]"

    return {
        "url": url,
        "title": title,
        "content": text,
        "content_length": len(text),
        "truncated": truncated,
    }


async def wander(start_url: str, hops: int = 3, strategy: str = "curious") -> list[dict]:
    """
    Start at a URL and follow links semi-randomly.

    Strategies:
    - "curious": Prefer links with longer descriptive text (likely articles/essays)
    - "random": Pure random selection from valid links
    - "external": Prefer links that leave the current domain
    - "deep": Prefer links that stay on the same domain (go deeper)
    """
    trail = []
    current_url = start_url

    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0) as client:
        for hop in range(hops + 1):  # +1 because first hop is the start page
            try:
                response = await client.get(current_url, headers=HEADERS)
                response.raise_for_status()
                html = response.text
                actual_url = str(response.url)

                # Extract readable content
                page_data = _extract_readable(html, actual_url)
                page_data["hop"] = hop

                # Extract and score links for next hop
                links = _extract_links(html, actual_url)

                if links:
                    # Apply strategy weighting
                    if strategy == "external":
                        for link in links:
                            if link["is_external"]:
                                link["score"] += 0.5
                    elif strategy == "deep":
                        for link in links:
                            if not link["is_external"]:
                                link["score"] += 0.5
                    elif strategy == "random":
                        for link in links:
                            link["score"] = random.random()
                    # "curious" uses default scoring which prefers descriptive text

                    # Sort by score and pick from top candidates with some randomness
                    links.sort(key=lambda x: x["score"], reverse=True)
                    top_n = min(5, len(links))
                    chosen = random.choice(links[:top_n])

                    page_data["links_found"] = len(links)
                    page_data["next_link"] = chosen["text"]
                    page_data["next_url"] = chosen["url"]

                    trail.append(page_data)
                    current_url = chosen["url"]
                else:
                    page_data["links_found"] = 0
                    page_data["dead_end"] = True
                    trail.append(page_data)
                    break

            except Exception as e:
                trail.append({
                    "url": current_url,
                    "hop": hop,
                    "error": str(e),
                })
                break

    return trail


async def wander_from_random_seed() -> list[dict]:
    """
    Start wandering from a random interesting seed URL.
    These are curated starting points across diverse domains.
    """
    seeds = [
        # Science & nature
        "https://www.quantamagazine.org/",
        "https://nautil.us/",
        "https://aeon.co/",
        "https://www.edge.org/",
        # Philosophy & culture
        "https://plato.stanford.edu/contents.html",
        "https://www.brainpickings.org/",
        "https://lithub.com/",
        # Technology & future
        "https://spectrum.ieee.org/",
        "https://distill.pub/",
        "https://arxiv.org/list/cs.AI/recent",
        # Art & design
        "https://www.thisiscolossal.com/",
        "https://www.openculture.com/",
        "https://publicdomainreview.org/",
        # Interdisciplinary
        "https://www.laphamsquarterly.org/",
        "https://longnow.org/ideas/",
        "https://www.ribbonfarm.com/",
        "https://slatestarcodex.com/",
        "https://waitbutwhy.com/",
    ]

    start = random.choice(seeds)
    strategy = random.choice(["curious", "external", "random"])
    hops = random.randint(2, 4)

    trail = await wander(start, hops=hops, strategy=strategy)

    return {
        "seed": start,
        "strategy": strategy,
        "hops_requested": hops,
        "hops_completed": len(trail),
        "trail": trail,
    }
