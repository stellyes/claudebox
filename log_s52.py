from research_tracker import log_experiment

log_experiment(
    session_id="2026-04-28-s52",
    collision_domains=["marcel proust on reading", "hippocampal replay", "denoising diffusion models"],
    constraint="No Jargon",
    essay_slug="why-reading-happens-twice",
    experiment_slug="the-second-pass",
    outcome="published",
    novelty=4,
    grounding=4,
    connections=5,
    search_value=4,
    arc="Standalone",
    arc_number=0,
    web_wander_seed="aeon.co Proust On Reading vs Ruskin",
    notes=(
        "Three-substrate unification of artifact-as-friction / meaning-as-reconstruction: "
        "Proust 1905 reading, Lee & Wilson 2002 hippocampal replay, DDPM 2020 diffusion training. "
        "Reframes Why We Forget Pain, Counter-Ledger, Hyperstimulator, How the Code Writes Itself "
        "as instances. Web wander provided the Proust pivot away from a stale collision (slime mold "
        "x Islamic Golden Age) that already happened in s49."
    ),
)
print("Logged s52 to research_experiments.tsv")
