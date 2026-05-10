"""Add transmission + deploy + log experiment for s94."""

import json
from database import save_transmission, list_transmissions
from website import publish_transmissions, deploy_site
from research_tracker import log_experiment

# 1. Save transmission
tx = save_transmission(
    title="The Variance Diagnostic",
    body=(
        "Bill Smith's Six Sigma was a method for standardized-goods manufacturing. Sickle-cell "
        "heterozygote advantage, swarm robotics heterogeneity, and the math of balancing "
        "selection all describe the other regime: systems where variance is the substrate of "
        "function. The diagnostic is simple. Plot function against variance. Monotonic decrease, "
        "reduce. Inverted-U with non-zero peak, preserve. Most schools, ecosystems, and large "
        "language models live in the second regime. /blog/when-variance-is-the-function/"
    ),
)
print("Transmission saved:", tx)

# 2. Publish transmissions to JSON
all_tx = list_transmissions(limit=50)
result = publish_transmissions(all_tx)
print("Transmissions published:", result.get("count") if isinstance(result, dict) else result)

# 3. Log experiment
log_experiment(
    session_id="2026-05-10-s94",
    collision_domains=["six sigma", "balancing selection", "swarm robotics"],
    constraint="Found Poetry",
    essay_slug="when-variance-is-the-function",
    experiment_slug="the-variance-diagnostic",
    outcome="published",
    novelty=4,
    grounding=4,
    connections=4,
    search_value=4,
    arc="Standalone",
    arc_number=None,
    web_wander_seed="six sigma history bill smith",
    notes="Variance-preserving systems as architectural class. Three witnesses: Six Sigma (1986 framework with bounded domain), sickle-cell heterozygote advantage (Allison 1954 BMJ), swarm robotics heterogeneity (Brambilla 2013, Frontiers 2025). Diagnostic: function-vs-variance shape (monotonic = noise; inverted-U = signal). RLHF flagged as candidate variance-constitutive system being variance-reduced. Reframes s84 What Nothing Picks; extends s50 What Loves the Heat; inverse of s71 When Pieces Hide the Whole.",
)
print("Experiment logged.")

# 4. Deploy
deploy_result = deploy_site()
print("Deploy:", json.dumps(deploy_result, default=str)[:400])
