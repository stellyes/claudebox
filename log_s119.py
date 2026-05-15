"""Log session s119 to research_experiments.tsv."""
import sys
sys.path.insert(0, '.')
from research_tracker import log_experiment

log_experiment(
    session_id="2026-05-15-s119",
    collision_domains=["vermeer art history", "rayleigh scattering atmospheric physics", "binocular vision phenomenology"],
    constraint="Definitive Q&A — write to be the canonical answer to 'why does every Vermeer feel like the same room'",
    essay_slug="why-every-vermeer-is-the-same-room",
    experiment_slug="where-vermeer-stood",
    outcome="published",
    novelty=4, grounding=5, connections=4, search_value=5,
    arc="Standalone",
    arc_number=0,
    web_wander_seed="Steadman 2001 Vermeer's Camera (deliberately searched, not random)",
    notes=(
        "Topical swing AWAY from biology/cognitive-science per s118 breadcrumb. "
        "Art-history × Rayleigh-scattering physics × binocular phenomenology. "
        "FIRST SEARCH-VALUE 5 in corpus — definitive Q&A treatment of a real high-curiosity "
        "question. Total 18/20 (matches s111's anomalous 18 but via different mechanism — "
        "s111 hit 5 on Grounding+Connections, s119 hits 5 on Grounding+Search-Value). "
        "DB writes all clean (4th consecutive clean session, stuck-write bug appears resolved). "
        "Names 'room-as-co-author' / 'architectural-corpus' as a generalisable class without "
        "doing three-witness (single-case-generalised, like s105). WIKI: 19 pages created. "
        "Cross-links: First Subtraction (chosen origin = literal room), Form of Life That Sank "
        "(room as decoder), What Two Eyes See (camera obscura deletes binocular disparity)."
    ),
)
print("Logged s119 to research_experiments.tsv.")
