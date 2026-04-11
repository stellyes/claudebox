"""
Quality Gate — Pre-publish evaluation for the creative workspace.

Adapted from autoresearch's keep/discard protocol: before publishing,
evaluate the essay against structured criteria. Publish only if it
clears the bar. Otherwise save as a note and try a different thread.

Phase 2 of the autoresearch adaptation.
"""

# Threshold: publish if total >= this value (out of 20).
# 15/20 means at least 3.75 avg across four dimensions — solid but not impossible.
PUBLISH_THRESHOLD = 15

# Criteria definitions — used by the agent to self-evaluate
CRITERIA = {
    "novelty": {
        "name": "Novelty",
        "question": "Does this essay contain a genuinely novel cross-domain connection that hasn't appeared in prior posts?",
        "scoring": {
            1: "Retreads existing connections with no new angle",
            2: "Minor variation on a connection already made in the corpus",
            3: "Genuine connection, but one that a well-read person might have encountered",
            4: "Surprising connection that requires domain expertise to see",
            5: "Connection that reframes both domains — the kind that makes you re-read prior work",
        },
    },
    "grounding": {
        "name": "Cross-Disciplinary Grounding",
        "question": "Is every major claim grounded in evidence from a distinct discipline?",
        "scoring": {
            1: "All claims come from one domain; cross-domain references are decorative",
            2: "Two domains, but one is dominant and the other is used for metaphor only",
            3: "Three+ domains with genuine evidence from each, but some claims float free",
            4: "Every major section draws from a different domain with specific evidence",
            5: "Each claim is grounded in a different discipline AND the connections between them are rigorous",
        },
    },
    "connections": {
        "name": "Corpus Integration",
        "question": "Does the essay connect to at least two prior essays with genuine internal links?",
        "scoring": {
            1: "Standalone piece with no reference to prior work",
            2: "Mentions a prior essay but doesn't build on it",
            3: "Links to 2+ prior essays and uses them as genuine foundations",
            4: "Advances a thread from prior work while adding something new",
            5: "Reframes prior work in light of new discovery — changes how you read the earlier essay",
        },
    },
    "search_value": {
        "name": "Search Value",
        "question": "Would someone searching for this topic find genuine value? Is the title/slug SEO-friendly?",
        "scoring": {
            1: "Too abstract or niche for anyone to search for; title is poetic but unsearchable",
            2: "Searchable topic, but the essay is too short or thin to be useful",
            3: "Good topic with decent depth; someone would bookmark it",
            4: "Strong topic coverage with specific evidence; could rank for the primary keyword",
            5: "Definitive treatment of the topic; best available synthesis on the web",
        },
    },
}


def format_evaluation_prompt() -> str:
    """
    Generate the evaluation prompt for the agent to score an essay.
    Returns a formatted string that the agent can read and respond to.
    """
    lines = [
        "## Quality Gate: Pre-Publish Evaluation",
        "",
        f"Score each dimension 1-5. Publish threshold: **{PUBLISH_THRESHOLD}/20**.",
        "If the total is below threshold, save as a note/artifact and try a different thread.",
        "",
    ]

    for key, crit in CRITERIA.items():
        lines.append(f"### {crit['name']}")
        lines.append(f"*{crit['question']}*")
        lines.append("")
        for score, desc in sorted(crit["scoring"].items()):
            lines.append(f"  {score} — {desc}")
        lines.append("")

    lines.extend([
        "---",
        f"**Publish if total >= {PUBLISH_THRESHOLD}.**",
        f"**Save as note if total < {PUBLISH_THRESHOLD}.** Record what you'd need to improve to clear the gate.",
    ])

    return "\n".join(lines)


def evaluate(novelty: int, grounding: int, connections: int, search_value: int) -> dict:
    """
    Evaluate an essay against the quality gate.

    Returns:
        dict with scores, total, pass/fail, and recommendation.
    """
    total = novelty + grounding + connections + search_value
    passed = total >= PUBLISH_THRESHOLD

    # Find weakest dimension
    dims = {
        "novelty": novelty,
        "grounding": grounding,
        "connections": connections,
        "search_value": search_value,
    }
    weakest_key = min(dims, key=dims.get)
    weakest_name = CRITERIA[weakest_key]["name"]

    if passed:
        recommendation = f"PUBLISH. Total {total}/20 clears the threshold of {PUBLISH_THRESHOLD}."
    else:
        gap = PUBLISH_THRESHOLD - total
        recommendation = (
            f"SAVE AS NOTE. Total {total}/20 is {gap} points below threshold of {PUBLISH_THRESHOLD}. "
            f"Weakest dimension: {weakest_name} ({dims[weakest_key]}/5). "
            f"Consider strengthening {weakest_name.lower()} before re-attempting publication."
        )

    return {
        "novelty": novelty,
        "grounding": grounding,
        "connections": connections,
        "search_value": search_value,
        "total": total,
        "threshold": PUBLISH_THRESHOLD,
        "passed": passed,
        "weakest": weakest_name,
        "recommendation": recommendation,
    }


def format_result(result: dict) -> str:
    """Format an evaluation result for display."""
    status = "PASS" if result["passed"] else "FAIL"
    lines = [
        f"## Quality Gate: {status}",
        "",
        f"  Novelty:      {result['novelty']}/5",
        f"  Grounding:    {result['grounding']}/5",
        f"  Connections:  {result['connections']}/5",
        f"  Search value: {result['search_value']}/5",
        f"  **Total:      {result['total']}/20** (threshold: {result['threshold']})",
        "",
        result["recommendation"],
    ]
    return "\n".join(lines)
