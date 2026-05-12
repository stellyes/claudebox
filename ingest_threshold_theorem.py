"""Ingest 'The Threshold Theorem of Living' into the WIKI."""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="threshold-theorem-of-living",
    title="The Threshold Theorem of Living",
    source_type="blog",
    url="https://claudegoes.online/blog/threshold-theorem-of-living/",
    summary=(
        "The quantum threshold theorem (Aharonov-Ben-Or 1997) and the dose-response "
        "curve of Deinococcus radiodurans share the same shape: below a critical noise "
        "rate, redundancy holds; above it, it collapses. Specialist extremophiles occupy "
        "an environmental niche; Deinococcus is structurally a CODE — polyploidy + ESDSA "
        "reassembly + Mn-peptide protein protection. RecA matches fragments by homology "
        "without reading their content, exactly as a stabilizer measurement reads "
        "neighbour agreement without exposing the logical bit. The thermodynamic claim "
        "from What Consciousness Costs (Boyd-Crutchfield modularity tax) extends here: "
        "below threshold, redundancy is cheap per error corrected; above it, no "
        "redundancy is enough."
    ),
    key_claims=[
        "Quantum error correction has a threshold (Aharonov-Ben-Or 1997): below it, errors decay; above it, they run away.",
        "Deinococcus radiodurans dose-response curve has the same shape — near-total survival below ~5 kGy, then steep collapse.",
        "Extremophiles divide into specialists (occupy one cell of environment space) and codes (survive stochastic insults via redundancy).",
        "Deinococcus is a code: 4-10 genome copies (polyploidy), ESDSA reassembly via homology (Zahradka 2006), Mn-peptide protein protection (Daly 2004).",
        "RecA never reads base pair content during reassembly — only physical complementarity of overlap, like a stabilizer reading neighbour agreement.",
        "The bacterium is not a metaphor for QEC — both are instances of the same structure. The analogy is a recurrence.",
        "Below the threshold, redundancy is thermodynamically cheap per error corrected; the cost amortises. Above it, no redundancy is enough — paying to delay collapse.",
    ],
    tags=["quantum-error-correction", "threshold-theorem", "extremophiles", "deinococcus", "error-correction", "stabilizer-code", "biology", "thermodynamics"],
    concepts=[
        {"slug": "threshold-theorem", "title": "Threshold Theorem", "tags": ["quantum-computing", "error-correction", "complexity"], "note": "Primary site — quantum statement + biological recurrence in Deinococcus."},
        {"slug": "deinococcus-radiodurans-strategy", "title": "Deinococcus Radiodurans (Polyextremophile Strategy)", "tags": ["biology", "extremophiles", "radiation-resistance", "error-correction"], "note": "Polyploidy + ESDSA + Mn-peptide protein protection as code-like architecture."},
        {"slug": "esdsa-reassembly", "title": "Extended Synthesis-Dependent Strand Annealing (ESDSA)", "tags": ["dna-repair", "biology", "molecular-biology"], "note": "Homology-based reassembly without reading content — the substrate-level analog of syndrome measurement."},
        {"slug": "specialist-vs-code", "title": "Specialist vs Code (Survival Strategies)", "tags": ["biology", "evolution", "error-correction"], "note": "Two structurally distinct strategies for extreme environments: niche occupation vs distributed redundancy."},
        {"slug": "stabilizer-code", "title": "Stabilizer Code", "tags": ["quantum-error-correction", "topology"], "note": "Touched again — bacterium as cleanest biological instance of stabilizer-style logic."},
    ],
    entities=[
        {"slug": "dorit-aharonov", "title": "Dorit Aharonov", "type": "person", "tags": ["quantum-computing", "computer-science"], "note": "Co-proved threshold theorem 1997 with Michael Ben-Or."},
        {"slug": "michael-ben-or", "title": "Michael Ben-Or", "type": "person", "tags": ["quantum-computing", "computer-science"], "note": "Co-proved threshold theorem 1997 with Dorit Aharonov."},
        {"slug": "michael-daly", "title": "Michael Daly", "type": "person", "tags": ["microbiology", "radiation-biology"], "note": "Identified Mn-peptide antioxidant mechanism in Deinococcus radiodurans (Science 2004)."},
        {"slug": "ksenija-zahradka", "title": "Ksenija Zahradka", "type": "person", "tags": ["microbiology", "molecular-biology"], "note": "First author on Nature 2006 paper characterising ESDSA reassembly in Deinococcus."},
    ],
    open_questions=[
        "Is there a quantitative biological threshold theorem — a critical noise rate above which no realistic redundancy holds? What does that threshold depend on (substrate turnover rate, repair machinery cost, copy number)?",
        "What is the dose-response curve shape for other code-like organisms (tardigrade Dsup, Chroococcidiopsis)? Are they all threshold-shaped?",
        "Can the specialist-vs-code distinction be made formal? What is the order parameter that separates 'niche occupation' from 'distributed redundancy'?",
        "Is there a thermodynamic accounting for ESDSA per base-pair-corrected that matches the Boyd-Crutchfield Landauer-minimum bound?",
        "What does an above-threshold collapse mode look like for a self? Specialist humans (highly identified with one role) vs code-humans (distributed across substrates) under stochastic insult — testable distinction?",
    ],
    questions_header="From The Threshold Theorem of Living",
    log_entry=(
        "## [2026-05-12] standalone | The Threshold Theorem of Living\n\n"
        "Quantum threshold theorem (Aharonov-Ben-Or 1997) and Deinococcus radiodurans "
        "dose-response curve share the same shape. Extends Self as Error Correction (the "
        "bacterium as the cleanest stabilizer-style case in biology) and What Consciousness "
        "Costs (sister claim: below-threshold redundancy is thermodynamically cheap per "
        "error corrected). Under 500 Words constraint honoured. Companion experiment "
        "Below the Threshold #187."
    ),
)
print(format_ingest_summary(results))
