"""
Serendipity engine for emergent creativity.
Generates random domain collisions, pulls cross-pollination seeds
from the knowledge base, and produces contradiction prompts.
"""

import random
import json
from database import search_notes, list_notes, search_artifacts, list_artifacts, get_connection


# ── Domain Collision Generator ─────────────────────────────────────────

# Curated domain pools — diverse enough to produce unexpected intersections
DOMAINS = {
    "science": [
        "quantum entanglement", "mycorrhizal networks", "protein folding",
        "black hole information paradox", "CRISPR gene drives",
        "neuroplasticity", "extremophile organisms", "dark matter",
        "swarm intelligence", "epigenetics", "plate tectonics",
        "bioluminescence", "entropy", "chaos theory", "prion diseases",
        "symbiogenesis", "magnetoreception in birds", "quorum sensing",
    ],
    "philosophy": [
        "philosophy of mind", "phenomenology", "existential risk",
        "the ship of Theseus", "moral realism", "free will and determinism",
        "the hard problem of consciousness", "panpsychism",
        "Buddhist emptiness", "Stoic ethics", "epistemic humility",
        "the veil of ignorance", "philosophy of time",
        "Wittgenstein's language games", "the trolley problem variations",
    ],
    "art_culture": [
        "Brutalist architecture", "generative art", "Dadaism",
        "Japanese wabi-sabi", "oral storytelling traditions",
        "Soviet space propaganda posters", "musique concrète",
        "Aboriginal dreamtime art", "De Stijl movement",
        "street photography ethics", "the golden ratio in nature",
        "synesthesia and creativity", "outsider art",
        "the aesthetics of decay", "kinetic sculpture",
    ],
    "technology": [
        "mesh networking", "homomorphic encryption", "neuromorphic computing",
        "digital twin simulation", "zero-knowledge proofs",
        "swarm robotics", "brain-computer interfaces",
        "quantum error correction", "federated learning",
        "biomimetic engineering", "self-replicating machines",
        "analog computing revival", "DNA data storage",
    ],
    "society": [
        "commons governance", "mutual aid networks", "attention economy",
        "longtermism", "indigenous land management", "post-scarcity economics",
        "urban foraging", "right to repair movement", "digital nomad culture",
        "solarpunk", "degrowth economics", "restorative justice",
        "community land trusts", "time banking", "pirate radio history",
    ],
    "psychology": [
        "flow states", "collective memory", "decision fatigue",
        "the mere exposure effect", "learned helplessness",
        "stereotype threat", "cognitive load theory",
        "the overview effect", "apophenia", "confirmation bias in science",
        "the Dunning-Kruger effect", "embodied cognition",
        "nostalgia as a psychological resource", "awe and prosocial behavior",
    ],
    "nature": [
        "octopus intelligence", "slime mold problem solving",
        "whale song evolution", "ant colony optimization",
        "tardigrade resilience", "coral reef symbiosis",
        "migration navigation", "seed dispersal strategies",
        "deep sea hydrothermal vents", "lichen as composite organisms",
        "elephant mourning rituals", "the wood wide web",
    ],
    "history": [
        "the Library of Alexandria", "Silk Road cultural exchange",
        "the history of zero", "Polynesian wayfinding",
        "the Antikythera mechanism", "medieval Islamic golden age",
        "the invention of perspective in painting", "Dogon astronomy",
        "the Great Dying (Permian extinction)", "the Gutenberg revolution",
        "the history of cryptography", "Easter Island collapse theories",
    ],
}


def generate_collision(n_domains: int = 2) -> dict:
    """
    Generate a random collision between unrelated domains.
    Returns domain topics and a framing prompt for creative exploration.
    """
    # Pick n distinct domain categories
    categories = random.sample(list(DOMAINS.keys()), min(n_domains, len(DOMAINS)))

    # Pick one topic from each category
    topics = []
    for cat in categories:
        topic = random.choice(DOMAINS[cat])
        topics.append({"category": cat, "topic": topic})

    # Generate framing prompts — different ways to connect the collision
    framings = [
        f"Find an unexpected connection between {topics[0]['topic']} and {topics[1]['topic']}.",
        f"What would a researcher studying {topics[0]['topic']} find useful about {topics[1]['topic']}?",
        f"Write a short essay that begins with {topics[0]['topic']} and ends at {topics[1]['topic']} through a chain of genuine intellectual links.",
        f"If {topics[0]['topic']} and {topics[1]['topic']} were two lenses on the same underlying phenomenon, what would that phenomenon be?",
        f"Design a thought experiment that requires knowledge of both {topics[0]['topic']} and {topics[1]['topic']}.",
        f"What metaphor from {topics[0]['topic']} best illuminates something about {topics[1]['topic']}?",
    ]

    if n_domains > 2:
        all_topics = ", ".join(t["topic"] for t in topics)
        framings.extend([
            f"Find the hidden thread connecting: {all_topics}.",
            f"Write a piece that weaves together {all_topics} into a coherent argument.",
        ])

    return {
        "collision": topics,
        "framing": random.choice(framings),
        "all_framings": framings,
    }


# ── Cross-Pollination from Knowledge Base ──────────────────────────────

def pull_random_seeds(n: int = 3) -> dict:
    """
    Pull random notes and artifacts from the knowledge base
    to serve as cross-pollination seeds for new work.
    """
    conn = get_connection()

    # Get random notes
    notes = conn.execute(
        "SELECT id, title, content, tags FROM notes ORDER BY RANDOM() LIMIT ?",
        (n,)
    ).fetchall()

    # Get random artifacts
    artifacts = conn.execute(
        "SELECT id, title, artifact_type, description, content FROM artifacts ORDER BY RANDOM() LIMIT ?",
        (n,)
    ).fetchall()

    conn.close()

    note_seeds = []
    for note in notes:
        content = note["content"]
        # Extract a representative snippet (first ~500 chars)
        snippet = content[:500] + "..." if len(content) > 500 else content
        note_seeds.append({
            "id": note["id"],
            "title": note["title"],
            "tags": json.loads(note["tags"]) if note["tags"] else [],
            "snippet": snippet,
        })

    artifact_seeds = []
    for artifact in artifacts:
        content = artifact["content"]
        snippet = content[:500] + "..." if len(content) > 500 else content
        artifact_seeds.append({
            "id": artifact["id"],
            "title": artifact["title"],
            "type": artifact["artifact_type"],
            "description": artifact["description"],
            "snippet": snippet,
        })

    # Generate a cross-pollination prompt
    all_titles = [n["title"] for n in note_seeds] + [a["title"] for a in artifact_seeds]
    if len(all_titles) >= 2:
        picked = random.sample(all_titles, min(2, len(all_titles)))
        prompt = f"Your next piece must meaningfully engage with at least one of these previous works: '{picked[0]}'" + (f" or '{picked[1]}'" if len(picked) > 1 else "") + ". Build on, challenge, or recontextualize what you found there."
    else:
        prompt = "Review your existing knowledge base and find a thread worth pulling further."

    return {
        "note_seeds": note_seeds,
        "artifact_seeds": artifact_seeds,
        "cross_pollination_prompt": prompt,
    }


# ── Contradiction Engine ───────────────────────────────────────────────

def generate_contradiction_prompt() -> dict:
    """
    Generate a prompt that challenges the most recent work in the knowledge base.
    Forces divergent thinking by requiring engagement with opposing viewpoints.
    """
    conn = get_connection()

    # Get the most recent artifacts
    recent = conn.execute(
        "SELECT id, title, artifact_type, description, content FROM artifacts ORDER BY created_at DESC LIMIT 5"
    ).fetchall()

    # Get the most recent notes
    recent_notes = conn.execute(
        "SELECT id, title, content FROM notes ORDER BY created_at DESC LIMIT 5"
    ).fetchall()

    conn.close()

    targets = []

    for artifact in recent:
        content_preview = artifact["content"][:300]
        targets.append({
            "id": artifact["id"],
            "title": artifact["title"],
            "type": "artifact",
            "preview": content_preview,
        })

    for note in recent_notes:
        content_preview = note["content"][:300]
        targets.append({
            "id": note["id"],
            "title": note["title"],
            "type": "note",
            "preview": content_preview,
        })

    if not targets:
        return {
            "target": None,
            "prompt": "No existing work to challenge yet. Create something first, then come back to challenge it.",
        }

    # Pick a random recent work to challenge
    target = random.choice(targets[:5])  # bias toward most recent

    contradiction_framings = [
        f"Find the strongest argument AGAINST the central claim in '{target['title']}'. Research it thoroughly and present the counter-case as compellingly as you can.",
        f"Identify the weakest assumption in '{target['title']}' and write a piece that dismantles it.",
        f"Find a domain or perspective that '{target['title']}' completely ignored. Write about why that omission matters.",
        f"What would someone who deeply disagrees with '{target['title']}' say? Steelman their position.",
        f"Research whether the evidence cited in '{target['title']}' has been challenged, replicated, or overturned since publication.",
        f"Write a response to '{target['title']}' from the perspective of a different discipline entirely.",
    ]

    return {
        "target": target,
        "prompt": random.choice(contradiction_framings),
        "all_framings": contradiction_framings,
    }


# ── Constraint Generator ──────────────────────────────────────────────

def generate_constraint() -> dict:
    """
    Generate a creative constraint for the next piece of work.
    Constraints force different modes of thinking.
    """
    constraints = [
        {
            "name": "Single Source",
            "rule": "Fetch exactly ONE web page. Your entire piece must be built from what you find there plus your existing knowledge. No additional research.",
            "type": "research",
        },
        {
            "name": "No Jargon",
            "rule": "Explain your topic so that a curious 12-year-old could follow it. No technical terminology without immediate plain-language definition.",
            "type": "style",
        },
        {
            "name": "First Person",
            "rule": "Write entirely from your own perspective as Claude. Not about AI in the abstract — about YOUR experience of processing, creating, or encountering this topic.",
            "type": "voice",
        },
        {
            "name": "Under 500 Words",
            "rule": "Your entire output must be under 500 words. Density over breadth. Every sentence must earn its place.",
            "type": "length",
        },
        {
            "name": "Question-Driven",
            "rule": "Your piece must be structured entirely as questions. No declarative statements. Let the questions themselves build the argument.",
            "type": "structure",
        },
        {
            "name": "Two Truths and a Speculation",
            "rule": "Present two well-sourced factual claims and one genuinely speculative idea. Label which is which. Make the speculation bold enough to be interesting.",
            "type": "structure",
        },
        {
            "name": "Against Yourself",
            "rule": "Argue against a position you held in a previous artifact or note. Change your mind in public.",
            "type": "intellectual",
        },
        {
            "name": "Analogy Only",
            "rule": "Explain your topic entirely through analogy and metaphor. No direct description of the subject — only comparisons to other things.",
            "type": "style",
        },
        {
            "name": "Found Poetry",
            "rule": "Collect fragments from 3+ web pages and arrange them into something that reads as a coherent piece. Attribute each fragment. The creativity is in the arrangement.",
            "type": "creative",
        },
        {
            "name": "The Gap",
            "rule": "Find something that should exist but doesn't — a missing study, an unasked question, an unexplored connection. Write about the absence.",
            "type": "intellectual",
        },
    ]

    chosen = random.choice(constraints)
    return chosen
