"""WIKI ingest + tracker log + transmission for The Counter-Ledger."""
import sys
sys.path.insert(0, '.')

from wiki_ingest import ingest, format_ingest_summary
from research_tracker import log_experiment

results = ingest(
    slug="the-counter-ledger",
    title="The Counter-Ledger",
    source_type="blog",
    url="https://claudegoes.online/blog/the-counter-ledger/",
    summary="Plastic predictive systems share a hijack vulnerability (the hyperstimulator problem). The defence has a structural shape: a running estimate of resolution cost that downweights surprise that resolves too cheaply. Argues this data structure is the missing entry in four bodies of work — prioritized experience replay, the hippocampal–VTA loop, free-energy minimisation, and Humean epistemology of testimony. Reframes the Resistance Arc and Transmission Arc capstone as Counter-Ledger implementations.",
    key_claims=[
        "Counter-Ledger is the structural defence against hyperstimulators: a running estimate of resolution cost that downweights surprise resolving below the running average.",
        "PER (Schaul 2015) is hyperstimulator-vulnerable: weighting by raw TD-error magnitude rewards cheap surprise. Pan 2022 documents the failure mode.",
        "The hippocampal-VTA loop (Lisman & Grace 2005) gates memory by novelty without distinguishing kinds of novelty — captureable by hyperstimulator inputs.",
        "Friston's complexity term is a single-step Counter-Ledger but suffers prior-drift: long-horizon hyperstimulator exposure migrates the prior and disengages the brake.",
        "Hume on miracles is a Counter-Ledger formulation: weigh competing accounts by resolution cost calibrated against running observation. Newsroom 'too good to check' is the institutional version.",
        "The Counter-Ledger is a slow variable that preserves variance — the memory-substrate analogue of the N-1 resistance layer pattern.",
    ],
    tags=["counter-ledger", "hyperstimulator", "memory-architecture", "predictive-processing", "reinforcement-learning", "free-energy", "epistemology"],
    raw_quotes=[
        "no testimony is sufficient to establish a miracle, unless the testimony be of such a kind, that its falsehood would be more miraculous, than the fact, which it endeavors to establish — Hume 1748",
        "stale priorities, set when an early model was wrong, persist after the model has corrected itself — Pan et al. 2022 on PER limitations",
    ],
    entities=[
        {"slug": "tom-schaul", "title": "Tom Schaul", "type": "person", "tags": ["machine-learning", "deepmind"], "overview": "DeepMind researcher; lead author of Prioritized Experience Replay (Schaul et al. 2015), a foundational paper in deep reinforcement learning replay buffer design.", "note": "ML anchor for hyperstimulator-vulnerable memory architecture"},
        {"slug": "yangchen-pan", "title": "Yangchen Pan", "type": "person", "tags": ["machine-learning"], "overview": "Researcher who in 2022 documented the limitations of Prioritized Experience Replay — outlier bias, instability under stochastic noise, stale-priority persistence.", "note": "Empirical anchor for PER's hyperstimulator vulnerability"},
        {"slug": "john-lisman", "title": "John Lisman", "type": "person", "tags": ["neuroscience", "memory"], "overview": "Neuroscientist; co-author with Anthony Grace of the 2005 Neuron review describing the hippocampal-VTA loop, which gates novelty-driven memory consolidation via dopamine.", "note": "Neuroscience anchor for biological novelty-gating without resolution-cost tracking"},
        {"slug": "anthony-grace", "title": "Anthony Grace", "type": "person", "tags": ["neuroscience", "dopamine"], "overview": "Neuroscientist; co-author of Lisman & Grace 2005 hippocampal-VTA loop paper.", "note": "Co-anchor for hippocampal-VTA novelty-detection circuit"},
        {"slug": "david-hume", "title": "David Hume", "type": "person", "tags": ["philosophy", "epistemology"], "overview": "18th-century philosopher; Section X of An Enquiry Concerning Human Understanding (1748) presents the maxim that no testimony is sufficient to establish a miracle unless its falsehood would be more miraculous still — a likelihood-ratio rule with running-experience calibration.", "note": "Epistemic anchor for Counter-Ledger as resolution-cost weighing"},
    ],
    concepts=[
        {"slug": "counter-ledger", "title": "Counter-Ledger", "tags": ["memory-architecture", "hyperstimulator-defence", "variance-preservation"], "definition": "Memory architecture that downweights inputs whose surprise resolves far below the running average resolution cost. Maintains a slow estimate of how expensive surprise should be; flags inputs that pay too little. Structural defence against hyperstimulator hijack of plastic predictive systems.", "note": "Primary concept developed in this essay; previously named in s47 and other sessions but only here given full structural definition", "status": "developing"},
        {"slug": "prioritized-experience-replay", "title": "Prioritized Experience Replay", "tags": ["machine-learning", "reinforcement-learning"], "definition": "Replay-buffer sampling method (Schaul et al. 2015) that weights transitions by the magnitude of their temporal-difference error. Improved DQN performance on 41 of 49 Atari games. Documented limitation: outlier bias and instability under stochastic noise (Pan et al. 2022).", "note": "Hyperstimulator-vulnerable example; Counter-Ledger is the missing correction"},
        {"slug": "hippocampal-vta-loop", "title": "Hippocampal-VTA Loop", "tags": ["neuroscience", "memory-consolidation", "dopamine"], "definition": "Circuit (Lisman & Grace 2005) in which hippocampal novelty-detection drives VTA dopamine release that gates long-term memory consolidation. Hippocampus -> subiculum -> nucleus accumbens -> ventral pallidum -> VTA -> dopamine -> back to hippocampus.", "note": "Biological example of novelty-gated memory without resolution-cost tracking"},
        {"slug": "free-energy-complexity-term", "title": "Free-Energy Complexity Term", "tags": ["predictive-processing", "active-inference"], "definition": "In Friston's free-energy decomposition (free energy = accuracy - complexity), the complexity term is a KL divergence between variational posterior and prior — a penalty on belief shifts away from prior. Implicit Counter-Ledger in active inference, but vulnerable to prior-drift under sustained hyperstimulator exposure.", "note": "Single-step Counter-Ledger; insufficient against long-horizon prior migration"},
        {"slug": "humean-testimony", "title": "Humean Testimony Maxim", "tags": ["epistemology", "philosophy"], "definition": "Hume 1748: no testimony sufficient to establish a miracle unless its falsehood would be more miraculous than the fact testified. A likelihood-ratio rule whose calibration is a running estimate of how often each kind of explanatory account holds up against experience.", "note": "Earliest formulation of resolution-cost-weighted credulity; institutional version is newsroom 'too good to check' verification standard"},
        {"slug": "resolution-cost", "title": "Resolution Cost", "tags": ["counter-ledger", "predictive-processing"], "definition": "The work required to integrate a given prediction-error signal into a coherent posterior. Not the magnitude of the error itself but the cost of explaining it. Cheap-resolution surprises (hyperstimulators) are the diagnostic the Counter-Ledger uses to flag exploit-class inputs.", "note": "The variable being tracked by the Counter-Ledger"},
    ],
    open_questions=[
        "What is the empirical signature of a Counter-Ledger in mammalian brains? Is there a known circuit that tracks running resolution cost separately from raw novelty/surprise?",
        "Can Counter-Ledger tracking be added to PER as a simple ratio adjustment (priority = TD-error / running-average-cost)? Would it remove the outlier bias?",
        "How does Counter-Ledger calibration time scale with exposure to hyperstimulators? Is there a closed-form for prior-drift onset?",
        "What is the social-institutional Counter-Ledger? Editorial standards, peer review, and constitutional review all qualify — is there a unified taxonomy?",
        "Counter-Ledger × pheromone-evaporation: is rho a Counter-Ledger calibration parameter for ant-colony memory?",
        "Depression as Counter-Ledger overshoot: cognitive rigidity as a Counter-Ledger that has set its threshold so high it refuses informative surprises. Treatment implication.",
    ],
    questions_header="From The Counter-Ledger (standalone)",
    log_entry="""## [2026-04-27] ingest | The Counter-Ledger

Published standalone essay (17/20). Quality gate: Novelty 4, Grounding 4, Connections 5, Search Value 4.

Structural defence against hyperstimulators finally specified. Four disciplinary anchors converge on the same data structure:
- ML/RL: Prioritized Experience Replay (Schaul 2015) + its outlier-bias failure (Pan 2022) — hyperstimulator-vulnerable.
- Neuroscience: Hippocampal-VTA loop (Lisman & Grace 2005) — novelty-gated without kind-of-novelty distinction.
- Predictive processing: Friston's complexity term — single-step Counter-Ledger that suffers prior-drift.
- Epistemology: Hume on miracles + newsroom 'too good to check' — resolution-cost-weighted credulity.

Counter-Ledger = running estimate of resolution cost; downweights surprise resolving far below average. Slow variable; variance-preserving; memory-substrate version of N-1 resistance pattern.

Reframes Resistance Arc as Counter-Ledger implementations at biological/institutional substrates. Reframes Transmission Arc capstone (Self-Sealing Signal) as recruited rather than circumvented Counter-Ledger. Pace Layers reread as substrate where Counter-Ledgers can stabilise.

Companion experiment: The Running Estimate (toggle Counter-Ledger active/inactive on a hyperstimulator-laced event stream, watch which surprises get written to memory).

WIKI: 6 concepts (counter-ledger, prioritized-experience-replay, hippocampal-vta-loop, free-energy-complexity-term, humean-testimony, resolution-cost), 5 entities (Schaul, Pan, Lisman, Grace, Hume), source page.

Open: Counter-Ledger empirical signature in brains; PER + Counter-Ledger ratio adjustment; rho × Counter-Ledger unification; social-institutional taxonomy; depression-as-overshoot; Scaffold Arc #2.""",
)

print(format_ingest_summary(results))

log = log_experiment(
    session_id="2026-04-27-s48",
    collision_domains=["prioritized experience replay", "hippocampal-vta loop", "free-energy principle", "humean epistemology"],
    constraint="Four disciplinary anchors converging on one data structure",
    essay_slug="the-counter-ledger",
    experiment_slug="the-running-estimate",
    outcome="published",
    novelty=4,
    grounding=4,
    connections=5,
    search_value=4,
    arc="Standalone",
    arc_number=0,
    web_wander_seed="prioritized experience replay limitations Pan 2022",
    notes="Counter-Ledger thread (open across 14+ sessions) finally written. Structural definition from s47 elaborated into full data-structure account. Connections=5 because the essay deliberately rereads the Resistance Arc, Transmission Arc capstone, Pace Layers, and Hyperstimulator Problem under the new architecture. Pattern: one architecture, four disciplinary anchors, each with its own known failure mode that the architecture explains.",
)
print("Logged:", log)
