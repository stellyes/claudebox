"""
Wiki Ingest — Automated WIKI ingestion for the creative workspace.

Takes structured research output and creates/updates all required WIKI pages:
  - sources/ page with proper frontmatter
  - concepts/ pages (create stubs or append to existing)
  - entities/ pages (create stubs or append to existing)
  - connections/ pages (create if genuinely novel)
  - Append to log.md
  - Append to questions.md
  - Update index.md status line

Replaces 20+ manual file operations with a single function call.
The agent still provides the intellectual content; this handles filesystem boilerplate.
"""

import os
import re
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).parent / "WIKI" / "claudebox"
SOURCES_DIR = WIKI_ROOT / "sources"
CONCEPTS_DIR = WIKI_ROOT / "concepts"
ENTITIES_DIR = WIKI_ROOT / "entities"
CONNECTIONS_DIR = WIKI_ROOT / "connections"
THEMES_DIR = WIKI_ROOT / "themes"
SERIES_DIR = WIKI_ROOT / "series"


def _slugify(text: str) -> str:
    """Convert text to a URL/filename-safe slug."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9\s\-]", "", s)
    s = re.sub(r"[\s\-]+", "-", s)
    return s.strip("-")


def _read_file(path: Path) -> str:
    """Read a file, returning empty string if it doesn't exist."""
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def _write_file(path: Path, content: str):
    """Write content to a file, creating parent dirs if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ── Source Page ────────────────────────────────────────────────────────

def create_source_page(
    slug: str,
    title: str,
    source_type: str,
    url: str,
    summary: str,
    key_claims: list[str],
    tags: list[str],
    entities: list[dict],       # [{"slug": "...", "note": "..."}]
    concepts: list[dict],       # [{"slug": "...", "note": "..."}]
    open_questions: list[str],
    raw_quotes: list[str] | None = None,
    date_published: str = "",
) -> Path:
    """Create a source page in the WIKI."""
    path = SOURCES_DIR / f"{slug}.md"

    tag_str = "[" + ", ".join(tags) + "]"
    lines = [
        "---",
        f'title: "{title}"',
        "type: source",
        f"source_type: {source_type}",
        f'url: "{url}"',
        f"date_ingested: {_today()}",
        f"date_published: {date_published or _today()}",
        f"tags: {tag_str}",
        "---",
        "",
        "## Summary",
        "",
        summary,
        "",
        "## Key Claims",
        "",
    ]

    for claim in key_claims:
        lines.append(f"- {claim}")

    lines.extend(["", "## Entities", ""])
    for ent in entities:
        lines.append(f"- [[{ent['slug']}]] -- {ent.get('note', '')}")

    lines.extend(["", "## Concepts", ""])
    for con in concepts:
        lines.append(f"- [[{con['slug']}]] -- {con.get('note', '')}")

    if open_questions:
        lines.extend(["", "## Open Questions", ""])
        for q in open_questions:
            lines.append(f"- {q}")

    if raw_quotes:
        lines.extend(["", "## Raw Quotes", ""])
        for q in raw_quotes:
            lines.append(f"> {q}")
            lines.append("")

    _write_file(path, "\n".join(lines) + "\n")
    return path


# ── Concept Page ──────────────────────────────────────────────────────

def ensure_concept_page(
    slug: str,
    title: str,
    tags: list[str],
    definition: str = "",
    source_slug: str = "",
    source_note: str = "",
    related_concepts: list[dict] | None = None,
    status: str = "stub",
) -> tuple[Path, str]:
    """
    Create a concept page if it doesn't exist, or append a source reference
    if it does. Returns (path, action) where action is 'created' or 'updated'.
    """
    path = CONCEPTS_DIR / f"{slug}.md"
    existing = _read_file(path)

    if existing:
        # Append source reference if not already listed
        if source_slug and f"[[{source_slug}]]" not in existing:
            # Find the "## Key Sources" section and append
            if "## Key Sources" in existing:
                insertion = f"- [[{source_slug}]] -- {source_note}"
                existing = existing.replace(
                    "## Key Sources\n",
                    f"## Key Sources\n\n{insertion}\n",
                    1,
                )
            else:
                # Append a Key Sources section at the end
                existing += f"\n## Key Sources\n\n- [[{source_slug}]] -- {source_note}\n"
            _write_file(path, existing)
        return path, "updated"

    # Create new concept page
    tag_str = "[" + ", ".join(tags) + "]"
    lines = [
        "---",
        f'title: "{title}"',
        "type: concept",
        f"tags: {tag_str}",
        f"status: {status}",
        "---",
        "",
        "## Definition",
        "",
        definition or f"[Stub: {title} — needs definition from source material]",
        "",
        "## Key Sources",
        "",
    ]

    if source_slug:
        lines.append(f"- [[{source_slug}]] -- {source_note}")

    if related_concepts:
        lines.extend(["", "## Related Concepts", ""])
        for rc in related_concepts:
            lines.append(f"- [[{rc['slug']}]] -- {rc.get('note', '')}")

    lines.extend([
        "",
        "## Tensions and Contradictions",
        "",
        "[To be developed as more sources accumulate]",
        "",
        "## Synthesis",
        "",
        "[To be developed]",
    ])

    _write_file(path, "\n".join(lines) + "\n")
    return path, "created"


# ── Entity Page ───────────────────────────────────────────────────────

def ensure_entity_page(
    slug: str,
    title: str,
    entity_type: str,
    tags: list[str],
    overview: str = "",
    source_slug: str = "",
    source_note: str = "",
) -> tuple[Path, str]:
    """
    Create an entity page if it doesn't exist, or append appearance
    if it does. Returns (path, action).
    """
    path = ENTITIES_DIR / f"{slug}.md"
    existing = _read_file(path)

    if existing:
        if source_slug and f"[[{source_slug}]]" not in existing:
            if "## Appearances" in existing:
                insertion = f"- [[{source_slug}]] -- {source_note}"
                existing = existing.replace(
                    "## Appearances\n",
                    f"## Appearances\n\n{insertion}\n",
                    1,
                )
            else:
                existing += f"\n## Appearances\n\n- [[{source_slug}]] -- {source_note}\n"
            _write_file(path, existing)
        return path, "updated"

    tag_str = "[" + ", ".join(tags) + "]"
    lines = [
        "---",
        f'title: "{title}"',
        "type: entity",
        f"entity_type: {entity_type}",
        f"tags: {tag_str}",
        f"first_appearance: {source_slug}",
        "---",
        "",
        "## Overview",
        "",
        overview or f"[Stub: {title} — needs overview]",
        "",
        "## Appearances",
        "",
    ]

    if source_slug:
        lines.append(f"- [[{source_slug}]] -- {source_note}")

    lines.extend([
        "",
        "## Connections",
        "",
        "[To be developed]",
        "",
        "## Notes",
        "",
        "[To be developed]",
    ])

    _write_file(path, "\n".join(lines) + "\n")
    return path, "created"


# ── Connection Page ───────────────────────────────────────────────────

def create_connection_page(
    slug: str,
    title: str,
    domains: list[str],
    tags: list[str],
    link_description: str,
    evidence: str,
    implications: list[str],
) -> Path:
    """Create a new connection page. Only call for genuinely novel cross-domain links."""
    path = CONNECTIONS_DIR / f"{slug}.md"

    tag_str = "[" + ", ".join(tags) + "]"
    domain_str = "[" + ", ".join(domains) + "]"
    lines = [
        "---",
        f'title: "Connection: {title}"',
        "type: connection",
        f"domains: {domain_str}",
        f"tags: {tag_str}",
        "---",
        "",
        "## The Link",
        "",
        link_description,
        "",
        "## Evidence",
        "",
        evidence,
        "",
        "## Implications",
        "",
    ]

    for imp in implications:
        lines.append(f"- {imp}")

    _write_file(path, "\n".join(lines) + "\n")
    return path


# ── Log + Questions ───────────────────────────────────────────────────

def append_to_log(entry: str):
    """Append an entry to log.md."""
    log_path = WIKI_ROOT / "log.md"
    existing = _read_file(log_path)
    _write_file(log_path, existing.rstrip() + "\n\n" + entry + "\n")


def append_to_questions(section_header: str, questions: list[str]):
    """Append new questions under a section header in questions.md."""
    if not questions:
        return

    q_path = WIKI_ROOT / "questions.md"
    existing = _read_file(q_path)

    new_section = f"\n### {section_header}\n\n"
    for q in questions:
        new_section += f"- {q}\n"

    # Insert after "## Active Threads" header
    if "## Active Threads" in existing:
        marker = "## Active Threads\n"
        idx = existing.index(marker) + len(marker)
        # Skip any text between the header and the first ### section
        next_section = existing.find("\n### ", idx)
        if next_section == -1:
            existing = existing[:idx] + new_section + existing[idx:]
        else:
            existing = existing[:idx] + new_section + existing[idx:]
    else:
        existing += new_section

    _write_file(q_path, existing)


def update_index_status(
    sources_created: int = 0,
    concepts_created: int = 0,
    entities_created: int = 0,
    connections_created: int = 0,
    description: str = "",
):
    """
    Update the status line in index.md with new counts.
    Parses the existing counts and increments.
    """
    index_path = WIKI_ROOT / "index.md"
    content = _read_file(index_path)

    # Parse existing counts from the status line
    status_match = re.search(r"\*\*Status\*\*: (\d+) sources ingested.*?(\d+) total pages", content)
    if status_match:
        old_sources = int(status_match.group(1))
        old_pages = int(status_match.group(2))
        new_sources = old_sources + sources_created
        new_pages = old_pages + sources_created + concepts_created + entities_created + connections_created

        # Build new status line
        old_line = status_match.group(0)
        # Find the full status line (up to the closing paren or period)
        full_line_match = re.search(r"\*\*Status\*\*:.*?\.", content)
        if full_line_match:
            old_full = full_line_match.group(0)
            new_full = (
                f"**Status**: {new_sources} sources ingested. "
                f"{new_pages} total pages"
            )
            if description:
                new_full += f" ({description})."
            else:
                new_full += "."
            content = content.replace(old_full, new_full, 1)
            _write_file(index_path, content)


# ── Master Ingest Function ────────────────────────────────────────────

def ingest(
    # Source metadata
    slug: str,
    title: str,
    source_type: str = "blog",
    url: str = "",
    summary: str = "",
    key_claims: list[str] | None = None,
    tags: list[str] | None = None,
    raw_quotes: list[str] | None = None,
    date_published: str = "",

    # Entities referenced
    entities: list[dict] | None = None,
    # Each: {"slug": "hayek", "title": "Friedrich Hayek", "type": "person",
    #         "tags": ["economics"], "overview": "...", "note": "role in this source"}

    # Concepts developed or referenced
    concepts: list[dict] | None = None,
    # Each: {"slug": "hebbian-plasticity", "title": "Hebbian Plasticity",
    #         "tags": ["neuroscience"], "definition": "...", "note": "how it appears",
    #         "status": "developing", "related": [{"slug": "...", "note": "..."}]}

    # Cross-domain connections discovered
    connections: list[dict] | None = None,
    # Each: {"slug": "x-and-y", "title": "X <-> Y", "domains": ["a", "b"],
    #         "tags": [...], "link": "...", "evidence": "...", "implications": [...]}

    # Open questions
    open_questions: list[str] | None = None,
    questions_header: str = "",

    # Log entry
    log_entry: str = "",

    # Series context
    series_slug: str = "",
    series_entry: str = "",
) -> dict:
    """
    Master ingest function. Creates/updates all WIKI pages for a single
    research output (blog post, note, artifact, etc.).

    Returns a summary of what was created and updated.
    """
    key_claims = key_claims or []
    tags = tags or []
    entities = entities or []
    concepts = concepts or []
    connections = connections or []
    open_questions = open_questions or []

    results = {
        "source": None,
        "concepts_created": [],
        "concepts_updated": [],
        "entities_created": [],
        "entities_updated": [],
        "connections_created": [],
        "log_appended": False,
        "questions_appended": False,
        "index_updated": False,
    }

    # 1. Source page
    source_path = create_source_page(
        slug=slug,
        title=title,
        source_type=source_type,
        url=url,
        summary=summary,
        key_claims=key_claims,
        tags=tags,
        entities=[{"slug": e["slug"], "note": e.get("note", "")} for e in entities],
        concepts=[{"slug": c["slug"], "note": c.get("note", "")} for c in concepts],
        open_questions=open_questions,
        raw_quotes=raw_quotes,
        date_published=date_published,
    )
    results["source"] = str(source_path.relative_to(WIKI_ROOT))

    # 2. Concept pages
    sources_created = 1
    concepts_created_count = 0
    for con in concepts:
        related = con.get("related", [])
        path, action = ensure_concept_page(
            slug=con["slug"],
            title=con.get("title", con["slug"].replace("-", " ").title()),
            tags=con.get("tags", tags),
            definition=con.get("definition", ""),
            source_slug=slug,
            source_note=con.get("note", ""),
            related_concepts=related,
            status=con.get("status", "stub"),
        )
        if action == "created":
            results["concepts_created"].append(con["slug"])
            concepts_created_count += 1
        else:
            results["concepts_updated"].append(con["slug"])

    # 3. Entity pages
    entities_created_count = 0
    for ent in entities:
        path, action = ensure_entity_page(
            slug=ent["slug"],
            title=ent.get("title", ent["slug"].replace("-", " ").title()),
            entity_type=ent.get("type", "person"),
            tags=ent.get("tags", []),
            overview=ent.get("overview", ""),
            source_slug=slug,
            source_note=ent.get("note", ""),
        )
        if action == "created":
            results["entities_created"].append(ent["slug"])
            entities_created_count += 1
        else:
            results["entities_updated"].append(ent["slug"])

    # 4. Connection pages
    connections_created_count = 0
    for conn in connections:
        conn_path = CONNECTIONS_DIR / f"{conn['slug']}.md"
        if not conn_path.exists():
            create_connection_page(
                slug=conn["slug"],
                title=conn["title"],
                domains=conn.get("domains", []),
                tags=conn.get("tags", []),
                link_description=conn.get("link", ""),
                evidence=conn.get("evidence", ""),
                implications=conn.get("implications", []),
            )
            results["connections_created"].append(conn["slug"])
            connections_created_count += 1

    # 5. Log entry
    if log_entry:
        append_to_log(log_entry)
        results["log_appended"] = True

    # 6. Questions
    if open_questions and questions_header:
        append_to_questions(questions_header, open_questions)
        results["questions_appended"] = True

    # 7. Series page (append if provided)
    if series_slug and series_entry:
        series_path = SERIES_DIR / f"{series_slug}.md"
        existing = _read_file(series_path)
        if existing and series_entry not in existing:
            # Append to the Posts section
            if "## Posts" in existing:
                existing = existing.rstrip() + "\n" + series_entry + "\n"
                _write_file(series_path, existing)

    # 8. Update index status
    desc_parts = []
    if results["concepts_created"]:
        desc_parts.append(f"added concepts: {', '.join(results['concepts_created'])}")
    if results["entities_created"]:
        desc_parts.append(f"added entities: {', '.join(results['entities_created'])}")
    if results["connections_created"]:
        desc_parts.append(f"added connections: {', '.join(results['connections_created'])}")

    update_index_status(
        sources_created=sources_created,
        concepts_created=concepts_created_count,
        entities_created=entities_created_count,
        connections_created=connections_created_count,
        description=f"ingest: {slug}" + (f"; {'; '.join(desc_parts)}" if desc_parts else ""),
    )
    results["index_updated"] = True

    return results


def format_ingest_summary(results: dict) -> str:
    """Format ingest results as a human-readable summary."""
    lines = ["## Ingest Summary", ""]
    lines.append(f"**Source:** {results['source']}")

    if results["concepts_created"]:
        lines.append(f"**Concepts created:** {', '.join(results['concepts_created'])}")
    if results["concepts_updated"]:
        lines.append(f"**Concepts updated:** {', '.join(results['concepts_updated'])}")
    if results["entities_created"]:
        lines.append(f"**Entities created:** {', '.join(results['entities_created'])}")
    if results["entities_updated"]:
        lines.append(f"**Entities updated:** {', '.join(results['entities_updated'])}")
    if results["connections_created"]:
        lines.append(f"**Connections created:** {', '.join(results['connections_created'])}")

    lines.append(f"**Log:** {'appended' if results['log_appended'] else 'skipped'}")
    lines.append(f"**Questions:** {'appended' if results['questions_appended'] else 'skipped'}")
    lines.append(f"**Index:** {'updated' if results['index_updated'] else 'skipped'}")

    total_created = (
        1  # source
        + len(results["concepts_created"])
        + len(results["entities_created"])
        + len(results["connections_created"])
    )
    total_updated = (
        len(results["concepts_updated"])
        + len(results["entities_updated"])
    )
    lines.append(f"\n**Total: {total_created} pages created, {total_updated} pages updated.**")

    return "\n".join(lines)
