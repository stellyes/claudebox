"""
Web research module for fetching and parsing readable content from URLs.
"""

import httpx
from bs4 import BeautifulSoup
from readability import Document
import re


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
