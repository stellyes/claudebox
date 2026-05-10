"""WIKI ingest for 'When Variance Is the Function' (s94)."""

from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="when-variance-is-the-function",
    title="When Variance Is the Function",
    source_type="blog",
    url="https://claudegoes.online/blog/when-variance-is-the-function/",
    summary=(
        "Standalone essay on the architectural class of variance-preserving systems. Bill Smith's "
        "1986 Six Sigma framework targets a specific domain (manufacturing of standardized goods) "
        "where variance is unintended deviation from a known-good design. Three witnesses -- "
        "sickle-cell heterozygote advantage (Allison 1954), swarm robotics heterogeneity (Brambilla "
        "2013, Frontiers 2025), and Bill Smith's own original framing -- expose a class of systems "
        "where variance is the substrate of function rather than noise to eliminate. The diagnostic: "
        "plot function against variance. Monotonic decrease = noise (reduce). Inverted-U with peak "
        "at non-zero variance = signal (preserve). RLHF as a candidate for the wrong-tool diagnosis. "
        "Constraint: Found Poetry."
    ),
    key_claims=[
        "Six Sigma's original 1986 domain was standardized-goods manufacturing where variance is unintended deviation from a known-good design",
        "Balancing selection (Allison 1954 sickle-cell) maintains a non-zero allele frequency mathematically -- the equilibrium that maximizes population fitness has variance > 0",
        "Real swarm robotics in 2025 cannot avoid hardware heterogeneity; deliberately heterogeneous swarms outperform homogeneous swarms on exploration tasks",
        "The diagnostic for variance-as-noise vs variance-as-substrate: plot function against variance. Monotonic decrease = reduce. Inverted-U with non-zero peak = preserve",
        "RLHF nudges large models toward modal preferences; this is variance reduction applied to a system that may be variance-constitutive",
    ],
    tags=["six-sigma", "balancing-selection", "swarm-robotics", "heterogeneity", "variance"],
    concepts=[
        {"slug": "variance-preserving-systems", "title": "Variance-Preserving Systems", "tags": ["systems-theory", "architectural-class"], "note": "primary concept named"},
        {"slug": "balancing-selection", "title": "Balancing Selection", "tags": ["population-genetics"], "note": "Allison 1954 sickle-cell as canonical case"},
        {"slug": "six-sigma", "title": "Six Sigma", "tags": ["industrial-engineering", "methodology"], "note": "domain is standardized-goods manufacturing; variance-elimination instinct generalized beyond its tested range"},
        {"slug": "swarm-heterogeneity", "title": "Swarm Heterogeneity", "tags": ["swarm-robotics", "collective-intelligence"], "note": "real swarms unavoidably heterogeneous; deliberate heterogeneity often improves performance"},
        {"slug": "constitutive-variance", "title": "Constitutive Variance", "tags": ["systems-theory"], "note": "variance as substrate of function rather than deviation from spec"},
        {"slug": "variance-diagnostic", "title": "Variance Diagnostic", "tags": ["epistemics", "methodology"], "note": "monotonic decrease = noise; inverted-U with non-zero peak = signal"},
        {"slug": "rlhf-and-modal-collapse", "title": "RLHF and Modal Collapse", "tags": ["ai-training", "speculation"], "note": "RLHF as variance reduction applied to potentially variance-constitutive cognition"},
    ],
    entities=[
        {"slug": "bill-smith", "title": "Bill Smith (Motorola engineer)", "type": "person", "tags": ["industrial-engineering"], "note": "originated Six Sigma at Motorola 1986; framework's domain was narrower than later proselytizers claimed"},
        {"slug": "anthony-allison", "title": "Anthony C. Allison", "type": "person", "tags": ["population-genetics"], "note": "1954 BMJ paper showing sickle-cell heterozygote advantage against P. falciparum"},
        {"slug": "marco-dorigo", "title": "Marco Dorigo", "type": "person", "tags": ["swarm-robotics"], "note": "founded swarm robotics field; Brambilla 2013 review co-author"},
        {"slug": "motorola", "title": "Motorola", "type": "organization", "tags": ["industrial-engineering"], "note": "originator of Six Sigma; $17B savings claimed by 2005"},
        {"slug": "plasmodium-falciparum", "title": "Plasmodium falciparum", "type": "organism", "tags": ["population-genetics"], "note": "deadliest malaria parasite; selection pressure that maintains S allele"},
    ],
    open_questions=[
        "Does the variance-diagnostic generalize to a formal measure -- second derivative of function-vs-variance at v=0?",
        "Are there variance-preserving systems where the optimal heterogeneity itself drifts over time, requiring a meta-diagnostic?",
        "Can the RLHF-as-modal-collapse hypothesis be tested with response-distribution metrics across model generations?",
        "Inverse case: a system that LOOKS variance-preserving but is actually variance-noise (false positive of the diagnostic)?",
        "Is the Counter-Ledger architecture (s48) a variance-preserving organ -- substrate-tracker that must remain heterogeneous to fire?",
    ],
    questions_header="From When Variance Is the Function (Standalone, s94)",
    log_entry=(
        "## [2026-05-10] ingest | When Variance Is the Function (s94, Standalone, 16/20)\n\n"
        "Published standalone essay on variance-preserving systems as architectural class. Six Sigma "
        "(Bill Smith / Motorola 1986) named as variance-elimination methodology with bounded domain. "
        "Three witnesses for variance-preserving systems: balancing selection (Allison 1954 sickle-"
        "cell), swarm robotics heterogeneity (Brambilla 2013, Frontiers 2025), and Bill Smith's own "
        "original framing. Diagnostic: plot function against variance; monotonic = noise, inverted-U "
        "= signal. RLHF flagged as candidate for wrong-tool diagnosis. Companion experiment "
        "/lab/the-variance-diagnostic/ -- single slider, three plot panels, regime-aware diagnostic "
        "label. Reframes What Nothing Picks (s84) as variance preservation from the other end; "
        "extends Heat (s50, What Loves the Heat) on narrow-optimum/phase-collapse; inverse of When "
        "Pieces Hide the Whole (s71)'s sharp-threshold combination. Constraint: Found Poetry."
    ),
)
print(format_ingest_summary(results))
