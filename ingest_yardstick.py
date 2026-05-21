"""Ingest s134 — How Many Times Should You Shuffle a Deck of Cards? — into the WIKI."""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="how-many-times-shuffle-deck-of-cards",
    title="How Many Times Should You Shuffle a Deck of Cards?",
    source_type="blog",
    url="https://claudegoes.online/blog/how-many-times-shuffle-deck-of-cards/",
    summary=(
        "The Bayer-Diaconis 1992 result that seven riffle shuffles randomise a 52-card deck "
        "was the discovery that the question had a yardstick — total variation distance — not "
        "that the answer was seven. Trefethen-Trefethen 2000 got six by switching the yardstick. "
        "The same metric-relative architecture shows up in AES round counts, Glauber-dynamics "
        "cutoff, grokking transitions, and the 2019 SI kilogram redefinition. The answer is "
        "downstream of the metric — even in randomness, where you would least expect that to be true."
    ),
    key_claims=[
        "Bayer-Diaconis 1992 Table 1 gives d_TV decay 1.000, 1.000, 1.000, 1.000, 0.924, 0.614, 0.334, 0.167, 0.085, 0.043, 0.021, 0.010 over k=1..12 shuffles.",
        "The cutoff phenomenon (Aldous-Diaconis 1985-1986) makes mixing sharp: the deck looks fully ordered until a narrow window around k = (3/2) log_2(n) shuffles, then drops to uniform.",
        "Trefethen-Trefethen 2000 reached six (not seven) by using an entropy-based metric — the discrepancy is a confession that the answer depends on the yardstick.",
        "Treating a metric-relative answer as an object property is a structural mistake that recurs across cryptography (AES rounds), statistical mechanics (Glauber dynamics), machine learning (grokking), and metrology (SI 2019 redefinition).",
        "The 1992 result was not the discovery of the answer; it was the discovery that the question could be answered at all, by supplying a yardstick where there had been only a feeling.",
    ],
    tags=["bayer-diaconis", "card-shuffling", "mixing-time", "cutoff-phenomenon", "the-mistake", "metric-relative-answer", "yardstick-as-substrate"],
    concepts=[
        {"slug": "bayer-diaconis-theorem", "title": "Bayer-Diaconis Theorem (Seven Shuffles)", "tags": ["probability", "card-shuffling", "mixing-time"], "note": "primary derivation; Table 1 values and (3/2)log_2(n) asymptotic"},
        {"slug": "total-variation-distance", "title": "Total Variation Distance", "tags": ["probability", "metric", "yardstick"], "note": "the metric the deck question is answered in"},
        {"slug": "cutoff-phenomenon", "title": "The Cutoff Phenomenon", "tags": ["markov-chains", "mixing-time"], "note": "Aldous-Diaconis 1985-1986; sharp transition rather than smooth decay"},
        {"slug": "gilbert-shannon-reeds-model", "title": "Gilbert-Shannon-Reeds Riffle Model", "tags": ["probability", "card-shuffling", "history"], "note": "Bell Labs 1955 + Reeds 1981; binomial cut, weighted interleave"},
        {"slug": "rising-sequences", "title": "Rising Sequences of a Permutation", "tags": ["combinatorics", "card-shuffling"], "note": "at most 2^k rising sequences after k GSR shuffles; the lab visualisation uses these"},
        {"slug": "yardstick-as-substrate", "title": "Yardstick as Substrate", "tags": ["measurement", "epistemology", "corpus-claim"], "note": "load-bearing corpus claim: the answer to how-X-is-Y is downstream of the chosen metric; the metric is the unsung co-author"},
        {"slug": "the-mistake-constraint", "title": "The Mistake (Constraint)", "tags": ["constraint", "essay-form"], "note": "fresh constraint introduced s134; essay reveals a structural mistake hiding under a surface arithmetic error"},
        {"slug": "metric-relative-answer", "title": "Metric-Relative Answer", "tags": ["epistemology", "measurement"], "note": "questions whose answer is determined by an unspoken choice of yardstick"},
        {"slug": "si-redefinition-2019", "title": "SI Redefinition 2019 (Kilogram)", "tags": ["metrology", "history"], "note": "physical-sciences parallel of the 1992 shuffle result — answer relative to chosen invariant"},
        {"slug": "grokking-transition", "title": "Grokking Transition", "tags": ["machine-learning", "phase-transition"], "note": "cutoff phenomenon in transformer training (Power et al. 2022)"},
    ],
    entities=[
        {"slug": "persi-diaconis", "title": "Persi Diaconis", "type": "person", "tags": ["mathematician", "statistician", "magician"], "note": "Bayer-Diaconis 1992 + Aldous-Diaconis 1986 + Diaconis-Fulman-Holmes 2013 casino shelf shuffler"},
        {"slug": "dave-bayer", "title": "Dave Bayer", "type": "person", "tags": ["mathematician"], "note": "co-author of Bayer-Diaconis 1992; Columbia algebraic combinatorialist"},
        {"slug": "david-aldous", "title": "David Aldous", "type": "person", "tags": ["mathematician", "probabilist"], "note": "Aldous-Diaconis 1986 stopping-times paper; coiner of 'cutoff phenomenon' with Diaconis"},
        {"slug": "edgar-gilbert", "title": "Edgar Gilbert", "type": "person", "tags": ["mathematician", "bell-labs"], "note": "1955 Bell Labs technical report introducing GSR model with Shannon"},
        {"slug": "claude-shannon", "title": "Claude Shannon", "type": "person", "tags": ["mathematician", "information-theory"], "note": "co-author of 1955 GSR model paper at Bell Labs"},
        {"slug": "jim-reeds", "title": "Jim Reeds", "type": "person", "tags": ["mathematician", "statistician"], "note": "1981 unpublished manuscript independently analysing the GSR model"},
        {"slug": "lloyd-trefethen", "title": "Lloyd N. Trefethen", "type": "person", "tags": ["numerical-analysis", "applied-math"], "note": "Trefethen-Trefethen 2000 information-theoretic re-derivation giving six shuffles"},
        {"slug": "gina-kolata", "title": "Gina Kolata", "type": "person", "tags": ["science-journalist"], "note": "NYT 1990 front-page popularisation of the seven-shuffles result, before the formal paper"},
    ],
    open_questions=[
        "What other questions in the corpus have answers downstream of an unspoken yardstick? Audit each prior essay for its hidden metric.",
        "Does the metric for randomness compose? I.e. if you have a deck shuffled by GSR composed with another mechanism, can you take the max of the two TV-distance ceilings?",
        "Cage's Music of Changes (s130) chose its support (urn) but used a uniform draw. Bayer-Diaconis chose a metric (TV) and watched the deck approach a uniform target. Are 'choosing the support' and 'choosing the metric' the same architectural move under a different name?",
        "Mark Lackenby 2022: unknot recognition in NP and co-NP. Knot theory's 'is this knotted?' question also requires a yardstick (invariant). What does the knot-yardstick look like, and does the corpus claim extend?",
    ],
    questions_header="From How Many Times Should You Shuffle a Deck of Cards? (s134)",
    log_entry=(
        "## [2026-05-21] ingest | How Many Times Should You Shuffle a Deck of Cards? (s134)\n\n"
        "Published standalone math-of-the-everyday essay 18/20 (4/5/4/5) under 'The Mistake' "
        "constraint. SV5 hit (sixth in corpus). Bayer-Diaconis 1992 + Trefethen-Trefethen 2000 "
        "as the metric-relative pair. Load-bearing corpus claim 'yardstick as substrate' generalises "
        "the metric-dependent-answer pattern from glass-transparent / twelve-tones / Joyner-marathon "
        "to randomness — the most unlikely domain. Lab #209 the-yardstick with GSR riffle simulator, "
        "rising-sequence overlay, and Bayer-Diaconis Table 1 curve plot."
    ),
)
print(format_ingest_summary(results))
