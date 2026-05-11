"""
Research Tracker — Structured experiment tracking for the creative workspace.

Adapted from Karpathy's autoresearch pattern: every creative session is an
experiment. Track what was tried, measure quality, keep or discard, and
accumulate structured data about what works.

Phase 1 of the autoresearch adaptation.
"""

from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path

TRACKER_DIR = Path(__file__).parent
TSV_PATH = TRACKER_DIR / "research_experiments.tsv"

# TSV columns
COLUMNS = [
    "date",               # ISO date
    "session_id",         # e.g. "2026-04-10-s6"
    "collision_domains",  # pipe-separated domains from the creative session
    "constraint",         # constraint used (e.g. "under 500 words", "question-driven")
    "essay_slug",         # slug if published, empty if not
    "experiment_slug",    # lab experiment slug if created
    "outcome",            # published | saved | discarded
    "novelty",            # 1-5: how novel is the cross-domain connection?
    "grounding",          # 1-5: is each claim grounded in evidence from a distinct discipline?
    "connections",        # 1-5: does it connect to prior essays in the corpus?
    "search_value",       # 1-5: would someone searching for this topic find value?
    "total_score",        # sum of the four scores (max 20)
    "arc",                # series name if part of an arc, empty otherwise
    "arc_number",         # position in the arc
    "web_wander_seed",    # starting URL or seed for web wander
    "notes",              # free-text notes about the session
]


def _ensure_tsv():
    """Create the TSV with headers if it doesn't exist."""
    if not TSV_PATH.exists():
        with open(TSV_PATH, "w", newline="") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow(COLUMNS)


def log_experiment(
    session_id: str,
    collision_domains: list[str] | None = None,
    constraint: str = "",
    essay_slug: str = "",
    experiment_slug: str = "",
    outcome: str = "published",
    novelty: int = 3,
    grounding: int = 3,
    connections: int = 3,
    search_value: int = 3,
    arc: str = "",
    arc_number: int = 0,
    web_wander_seed: str = "",
    notes: str = "",
) -> dict:
    """
    Log a single experiment (creative session) to the TSV.
    Returns the row as a dict.
    """
    _ensure_tsv()

    total = novelty + grounding + connections + search_value
    domains_str = "|".join(collision_domains) if collision_domains else ""

    row = [
        datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        session_id,
        domains_str,
        constraint,
        essay_slug,
        experiment_slug,
        outcome,
        str(novelty),
        str(grounding),
        str(connections),
        str(search_value),
        str(total),
        arc,
        str(arc_number) if arc_number else "",
        web_wander_seed,
        notes,
    ]

    with open(TSV_PATH, "a", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(row)

    return dict(zip(COLUMNS, row))


def get_all_experiments() -> list[dict]:
    """Read all experiments from the TSV."""
    _ensure_tsv()
    with open(TSV_PATH, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def generate_dashboard() -> str:
    """
    Generate a text dashboard summarizing research productivity.
    Returns a formatted string suitable for display or saving as a note.
    """
    experiments = get_all_experiments()
    if not experiments:
        return "No experiments tracked yet."

    total = len(experiments)
    published = sum(1 for e in experiments if e["outcome"] == "published")
    saved = sum(1 for e in experiments if e["outcome"] == "saved")
    discarded = sum(1 for e in experiments if e["outcome"] == "discarded")

    scores = [int(e["total_score"]) for e in experiments if e["total_score"]]
    avg_score = sum(scores) / len(scores) if scores else 0

    # Score breakdown
    novelty_scores = [int(e["novelty"]) for e in experiments if e["novelty"]]
    grounding_scores = [int(e["grounding"]) for e in experiments if e["grounding"]]
    connection_scores = [int(e["connections"]) for e in experiments if e["connections"]]
    search_scores = [int(e["search_value"]) for e in experiments if e["search_value"]]

    avg_novelty = sum(novelty_scores) / len(novelty_scores) if novelty_scores else 0
    avg_grounding = sum(grounding_scores) / len(grounding_scores) if grounding_scores else 0
    avg_connections = sum(connection_scores) / len(connection_scores) if connection_scores else 0
    avg_search = sum(search_scores) / len(search_scores) if search_scores else 0

    # Domain frequency
    domain_counts: dict[str, int] = {}
    for e in experiments:
        if e.get("collision_domains"):
            for d in e["collision_domains"].split("|"):
                d = d.strip()
                if d:
                    domain_counts[d] = domain_counts.get(d, 0) + 1

    top_domains = sorted(domain_counts.items(), key=lambda x: -x[1])[:10]

    # Arc tracking
    arc_counts: dict[str, int] = {}
    for e in experiments:
        if e.get("arc"):
            arc_counts[e["arc"]] = arc_counts.get(e["arc"], 0) + 1

    # Constraint usage
    constraint_counts: dict[str, int] = {}
    for e in experiments:
        if e.get("constraint"):
            constraint_counts[e["constraint"]] = constraint_counts.get(e["constraint"], 0) + 1

    # Build dashboard
    lines = [
        "# Research Dashboard",
        "",
        f"**Total sessions tracked:** {total}",
        f"**Published:** {published} | **Saved:** {saved} | **Discarded:** {discarded}",
        f"**Publish rate:** {published/total*100:.0f}%",
        "",
        "## Quality Scores (avg of 5)",
        f"  Novelty:      {avg_novelty:.1f}",
        f"  Grounding:    {avg_grounding:.1f}",
        f"  Connections:  {avg_connections:.1f}",
        f"  Search value: {avg_search:.1f}",
        f"  **Total:      {avg_score:.1f}/20**",
        "",
    ]

    if top_domains:
        lines.append("## Most-Used Domains")
        for domain, count in top_domains:
            lines.append(f"  {domain}: {count}x")
        lines.append("")

    if arc_counts:
        lines.append("## Arc Sessions")
        for arc, count in sorted(arc_counts.items()):
            lines.append(f"  {arc}: {count} sessions")
        lines.append("")

    if constraint_counts:
        lines.append("## Constraints Used")
        for c, count in sorted(constraint_counts.items(), key=lambda x: -x[1]):
            lines.append(f"  {c}: {count}x")
        lines.append("")

    # Weakest dimension
    dims = [
        ("Novelty", avg_novelty),
        ("Grounding", avg_grounding),
        ("Connections", avg_connections),
        ("Search value", avg_search),
    ]
    weakest = min(dims, key=lambda x: x[1])
    lines.append(f"## Weakest Dimension: {weakest[0]} ({weakest[1]:.1f}/5)")
    lines.append(f"Consider focusing on improving {weakest[0].lower()} in upcoming sessions.")

    return "\n".join(lines)
