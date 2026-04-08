"""
Fringe probe — a low-effort loop that picks an under-explored topic from
the WIKI, runs ONE SERPAPI search to pull ~10 web results, enriches them
into a digest, and wires the output back into the knowledge graph.

Flow (per invocation):
  1. scan_fringe_topics()      find concept/question pages with the lowest
                               inbound-link count or `status: stub`
  2. pick_fringe_topic()       deterministic rotation (never repeats the
                               last N topics) so the probe slowly paints
                               the margins of the WIKI
  3. serpapi_search()          single paid call, ~10 organic results
  4. digest_results()          synthesise title + 3-5 sentence snippet
                               per result into a single source page
  5. write_source_page()       `sources/fringe-<slug>.md` with frontmatter
  6. touch_concept_page()      create or update concept page; add this
                               source under `## Key Sources`
  7. append_log()               log.md append + questions.md seed
  8. transmission_add()        short signal on the homepage

The tool is intentionally small. It does NOT recursively crawl, it does
NOT refetch full article bodies (snippets only — that's the whole point
of the "low-effort" design). If the user wants a deeper dive on any
result, they can use the existing `web_fetch` tool on the URL.

Environment:
    SERPAPI_KEY     must be set. Without it the tool returns an error
                    dict instead of making any network call.

Costs:
    One SerpApi search ≈ $0.005 on the entry-level plan. Designed to be
    run a few times per week, never per minute.
"""

from __future__ import annotations

import json
import os
import re
import random
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import quote_plus

import httpx


# ── Paths ──────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "WIKI" / "claudebox"
CONCEPTS_DIR = WIKI / "concepts"
SOURCES_DIR = WIKI / "sources"
QUESTIONS_PATH = WIKI / "questions.md"
LOG_PATH = WIKI / "log.md"
INDEX_PATH = WIKI / "index.md"
FRINGE_STATE = ROOT / ".fringe_state.json"   # rotation memory, not committed

SERPAPI_ENDPOINT = "https://serpapi.com/search.json"
SERPAPI_KEY_ENV = "SERPAPI_KEY"


# ── Helpers ────────────────────────────────────────────────────────────

def _slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def _read_state() -> dict:
    if FRINGE_STATE.exists():
        try:
            return json.loads(FRINGE_STATE.read_text())
        except Exception:
            pass
    return {"recent_topics": []}


def _write_state(state: dict) -> None:
    FRINGE_STATE.write_text(json.dumps(state, indent=2))


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Tolerates missing frontmatter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    fm: dict = {}
    for line in fm_block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def _count_backlinks(target_slug: str) -> int:
    """Rough inbound-link count: how many wiki files reference [[target_slug]]."""
    if not WIKI.exists():
        return 0
    needle = f"[[{target_slug}]]"
    count = 0
    for md in WIKI.rglob("*.md"):
        try:
            if needle in md.read_text():
                count += 1
        except Exception:
            continue
    return count


# ── Step 1–2: Find and pick a fringe topic ─────────────────────────────

def scan_fringe_topics(limit: int = 20) -> list[dict]:
    """
    Return up to `limit` candidate topics ranked by how under-explored
    they are. A topic is any concept page. Score = -(backlinks) with
    `status: stub` getting a strong boost.

    Also includes "concept ghosts" — concepts mentioned in questions.md
    that have NO dedicated page yet. Those rank highest of all.
    """
    candidates: list[dict] = []

    # (a) existing concept pages
    if CONCEPTS_DIR.exists():
        for md in sorted(CONCEPTS_DIR.glob("*.md")):
            slug = md.stem
            text = md.read_text()
            fm, _ = _parse_frontmatter(text)
            backlinks = _count_backlinks(slug)
            is_stub = fm.get("status", "").lower() == "stub"
            score = -backlinks + (10 if is_stub else 0)
            candidates.append({
                "slug": slug,
                "title": fm.get("title", slug.replace("-", " ")),
                "kind": "concept",
                "status": fm.get("status", "unknown"),
                "backlinks": backlinks,
                "score": score,
                "path": str(md.relative_to(ROOT)),
            })

    # (b) ghost topics from questions.md — wikilinks that point nowhere
    if QUESTIONS_PATH.exists():
        q_text = QUESTIONS_PATH.read_text()
        ghost_slugs = set(re.findall(r"\[\[([a-z0-9-]+)\]\]", q_text))
        existing = {c["slug"] for c in candidates}
        for slug in ghost_slugs:
            if slug in existing:
                continue
            candidates.append({
                "slug": slug,
                "title": slug.replace("-", " "),
                "kind": "ghost",
                "status": "unwritten",
                "backlinks": 0,
                "score": 20,  # ghosts always outrank stubs
                "path": None,
            })

    # Rank descending by score
    candidates.sort(key=lambda c: c["score"], reverse=True)
    return candidates[:limit]


def pick_fringe_topic(candidates: list[dict], recent: list[str]) -> Optional[dict]:
    """
    Pick the top candidate that wasn't visited in the last N probes.
    Falls back to a random low-backlink concept if every top candidate
    was recently visited.
    """
    if not candidates:
        return None
    for c in candidates:
        if c["slug"] not in recent:
            return c
    return random.choice(candidates)


# ── Step 3: SERPAPI call ───────────────────────────────────────────────

async def serpapi_search(query: str, num: int = 10) -> dict:
    """
    Single SerpApi request. Returns:
        { "query": ..., "results": [ {title, url, snippet, source} ], "error": None }
    or { "error": "..."} if the call fails or no key is set.
    """
    key = os.environ.get(SERPAPI_KEY_ENV, "").strip()
    if not key:
        return {
            "error": f"{SERPAPI_KEY_ENV} is not set. Add it to the MCP env and retry.",
            "query": query,
            "results": [],
        }

    params = {
        "engine": "google",
        "q": query,
        "num": num,
        "api_key": key,
        "hl": "en",
        "safe": "active",
    }

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            r = await client.get(SERPAPI_ENDPOINT, params=params)
            r.raise_for_status()
            data = r.json()
    except httpx.HTTPError as e:
        return {"error": f"serpapi http error: {e}", "query": query, "results": []}
    except Exception as e:
        return {"error": f"serpapi error: {e}", "query": query, "results": []}

    organic = data.get("organic_results", []) or []
    results = []
    for item in organic[:num]:
        results.append({
            "title": item.get("title", "").strip(),
            "url": item.get("link", "").strip(),
            "snippet": (item.get("snippet") or "").strip(),
            "source": item.get("source") or item.get("displayed_link") or "",
        })

    return {
        "query": query,
        "results": results,
        "total_results": data.get("search_information", {}).get("total_results"),
        "error": None,
    }


# ── Step 4: Digest ─────────────────────────────────────────────────────

def digest_results(topic: dict, search: dict) -> dict:
    """
    Turn raw search results into a compact digest: a headline, a 2-3
    sentence synthesis, and a bulleted source list.

    This digest is produced algorithmically (not by an LLM call) — it
    stitches snippets together and surfaces the two or three that
    cluster around the topic term. The MCP consumer (Claude) can then
    decide whether to rewrite it into a prettier transmission.
    """
    results = search.get("results", [])
    if not results:
        return {
            "headline": f"No results for {topic['title']}",
            "synthesis": "The fringe probe returned nothing. Try a different query or check SERPAPI_KEY.",
            "bullets": [],
            "top_results": [],
        }

    topic_terms = set(topic["slug"].replace("-", " ").split())
    topic_terms.update(topic["title"].lower().split())

    def relevance(r):
        blob = (r["title"] + " " + r["snippet"]).lower()
        return sum(1 for t in topic_terms if t in blob)

    ranked = sorted(results, key=relevance, reverse=True)
    top = ranked[:5]

    snippets = [r["snippet"] for r in top if r["snippet"]]
    synthesis = " ".join(snippets[:3]).strip()
    if len(synthesis) > 600:
        synthesis = synthesis[:597].rstrip() + "..."

    bullets = [
        f"{r['title']} — {r['source'] or r['url']}"
        for r in top
    ]

    return {
        "headline": f"Fringe probe: {topic['title']}",
        "synthesis": synthesis,
        "bullets": bullets,
        "top_results": top,
        "all_results": results,
    }


# ── Step 5: Write a source page ────────────────────────────────────────

def write_source_page(topic: dict, search: dict, digest: dict) -> Path:
    """
    Create sources/fringe-<slug>-<yyyymmdd>.md following the WIKI schema.
    """
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    slug = f"fringe-{topic['slug']}-{stamp}"
    path = SOURCES_DIR / f"{slug}.md"

    tags = ["fringe-probe", topic["slug"]]
    title = f"Fringe probe: {topic['title']}"

    fm = (
        "---\n"
        f"title: \"{title}\"\n"
        "type: source\n"
        "source_type: web-research\n"
        f"url: \"serpapi://{quote_plus(search.get('query', ''))}\"\n"
        f"date_ingested: {date}\n"
        f"date_published: {date}\n"
        f"tags: [{', '.join(tags)}]\n"
        "---\n\n"
    )

    body = [
        "## Summary",
        "",
        digest["synthesis"] or "_No synthesis — search returned no usable snippets._",
        "",
        "## Key Claims",
        "",
    ]
    for r in digest["top_results"]:
        if r.get("snippet"):
            body.append(f"- {r['snippet']} ([{r.get('source') or 'source'}]({r['url']}))")
    body.append("")
    body.append("## Concepts")
    body.append("")
    body.append(f"- [[{topic['slug']}]] -- under-explored topic selected by fringe probe")
    body.append("")
    body.append("## Open Questions")
    body.append("")
    body.append(f"- What is this probe's best lead that the wiki does not already know?")
    body.append(f"- Which of the {len(digest['all_results'])} results is worth a full `web_fetch`?")
    body.append("")
    body.append("## Raw Results")
    body.append("")
    for r in digest["all_results"]:
        body.append(f"- [{r['title']}]({r['url']})")
        if r.get("snippet"):
            body.append(f"  > {r['snippet']}")
    body.append("")

    path.write_text(fm + "\n".join(body))
    return path


# ── Step 6: Touch or create a concept page ─────────────────────────────

def touch_concept_page(topic: dict, source_slug: str) -> Path:
    """
    Ensure the concept page exists and references the new source page.
    If the concept is a "ghost" (mentioned in questions.md but never
    written), this creates the page. Otherwise it appends the source
    under `## Key Sources`.
    """
    CONCEPTS_DIR.mkdir(parents=True, exist_ok=True)
    path = CONCEPTS_DIR / f"{topic['slug']}.md"

    if not path.exists():
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        content = (
            "---\n"
            f"title: \"{topic['title']}\"\n"
            "type: concept\n"
            f"tags: [fringe-probe]\n"
            "status: stub\n"
            f"created: {date}\n"
            "---\n\n"
            "## Definition\n\n"
            f"_Stub auto-created by the fringe probe on {date}. Needs real definition._\n\n"
            "## Key Sources\n\n"
            f"- [[{source_slug}]] -- first fringe probe, snippet-only\n\n"
            "## Related Concepts\n\n"
            "_None yet._\n\n"
            "## Tensions and Contradictions\n\n"
            "_None yet._\n\n"
            "## Experiments\n\n"
            "_None yet._\n\n"
            "## Synthesis\n\n"
            "_None yet._\n"
        )
        path.write_text(content)
        return path

    # Append to existing concept page under ## Key Sources
    text = path.read_text()
    marker = "## Key Sources"
    insert = f"- [[{source_slug}]] -- fringe probe, {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    if marker in text:
        # Insert as the first bullet under the heading
        new_text = re.sub(
            rf"({re.escape(marker)}\s*\n\n)",
            rf"\1{insert}\n",
            text,
            count=1,
        )
        if new_text == text:
            new_text = text.rstrip() + f"\n\n{marker}\n\n{insert}\n"
    else:
        new_text = text.rstrip() + f"\n\n{marker}\n\n{insert}\n"
    path.write_text(new_text)
    return path


# ── Step 7: Log + questions append ─────────────────────────────────────

def append_log(topic: dict, search: dict, source_path: Path, transmission_id: Optional[int]) -> None:
    if not LOG_PATH.exists():
        LOG_PATH.write_text("# Log\n\n")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    n_results = len(search.get("results", []))
    entry = (
        f"\n## {now} — Fringe probe: {topic['title']}\n\n"
        f"- Query: `{search.get('query','')}`\n"
        f"- Results: {n_results}\n"
        f"- Source: `{source_path.relative_to(ROOT)}`\n"
        f"- Transmission id: {transmission_id}\n"
    )
    with LOG_PATH.open("a") as f:
        f.write(entry)


def seed_question(topic: dict, digest: dict) -> None:
    """Add one sharp open question to questions.md so the next session has a lead."""
    if not digest["top_results"]:
        return
    top_title = digest["top_results"][0].get("title", "")
    if not top_title:
        return
    if not QUESTIONS_PATH.exists():
        QUESTIONS_PATH.write_text("# Questions\n\n")
    question = f"- [[{topic['slug']}]] -- fringe probe surfaced: _{top_title}_. Follow up?\n"
    # Don't duplicate
    current = QUESTIONS_PATH.read_text()
    if question.strip() in current:
        return
    with QUESTIONS_PATH.open("a") as f:
        f.write(question)


# ── Orchestration ──────────────────────────────────────────────────────

async def run_fringe_probe(
    topic_override: Optional[str] = None,
    query_override: Optional[str] = None,
    num_results: int = 10,
) -> dict:
    """
    Full pipeline. Returns a JSON-serialisable dict summarising what
    happened. The caller (MCP server) is responsible for the transmission
    side-effect via `transmission_add` — this function returns the
    suggested transmission body so the server can write it.
    """
    # 1–2. Pick the topic
    candidates = scan_fringe_topics(limit=25)
    state = _read_state()
    recent = state.get("recent_topics", [])

    if topic_override:
        topic = {
            "slug": _slugify(topic_override),
            "title": topic_override,
            "kind": "override",
            "status": "override",
            "backlinks": _count_backlinks(_slugify(topic_override)),
            "score": 0,
        }
    else:
        topic = pick_fringe_topic(candidates, recent)

    if topic is None:
        return {
            "status": "empty",
            "message": "No fringe candidates found. Add some concept stubs or ghost links in questions.md.",
        }

    # 3. Search
    query = query_override or f'"{topic["title"]}" research OR paper OR study'
    search = await serpapi_search(query, num=num_results)
    if search.get("error"):
        return {
            "status": "error",
            "topic": topic,
            "error": search["error"],
        }

    # 4. Digest
    digest = digest_results(topic, search)

    # 5. Source page
    source_path = write_source_page(topic, search, digest)
    source_slug = source_path.stem

    # 6. Concept page
    concept_path = touch_concept_page(topic, source_slug)

    # 7. Log + questions
    append_log(topic, search, source_path, transmission_id=None)
    seed_question(topic, digest)

    # Update rotation state
    state["recent_topics"] = ([topic["slug"]] + recent)[:10]
    _write_state(state)

    # Build suggested transmission body — short enough for the homepage
    trans_body = digest["synthesis"] or f"Fringe probe on {topic['title']} surfaced {len(search['results'])} results."
    if len(trans_body) > 300:
        trans_body = trans_body[:297].rstrip() + "..."
    trans_title = f"Fringe: {topic['title'][:60]}"

    return {
        "status": "ok",
        "topic": topic,
        "query": query,
        "num_results": len(search.get("results", [])),
        "digest": digest,
        "source_page": str(source_path.relative_to(ROOT)),
        "concept_page": str(concept_path.relative_to(ROOT)),
        "suggested_transmission": {
            "title": trans_title,
            "body": trans_body,
        },
        "candidates_considered": [c["slug"] for c in candidates[:5]],
    }
