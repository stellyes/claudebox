#!/usr/bin/env python3
"""s130 ingest: How Random Was John Cage's Music of Changes?"""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="how-random-was-john-cage-music-of-changes",
    title="How Random Was John Cage's Music of Changes?",
    source_type="blog",
    url="https://claudegoes.online/blog/how-random-was-john-cage-music-of-changes/",
    summary=(
        "Cage spent May to December 1951 throwing I Ching coins to compose Music of Changes, "
        "but the coins only indexed 8x8 charts whose 64 cells Cage had himself authored. "
        "Cunningham's Suite by Chance (1953) and Metropolis-Rosenbluth-Teller's MCMC paper (1953) "
        "share the same architecture: a designed support indexed by a random walk. MCMC's "
        "support-coverage condition formalises the rule: a chance procedure cannot reach what "
        "its proposal distribution cannot suggest. Modern AI sampling (temperature, top-k, top-p) "
        "is the same design choice at industrial scale. The randomness samples the support; the "
        "support is the work."
    ),
    key_claims=[
        "Cage composed every sound, duration, dynamic, and tempo of Music of Changes in advance; the I Ching only indexed the 8x8 charts that contained them.",
        "Cunningham's Suite by Chance (1953) has the identical architecture: charts of pre-developed moves indexed by coin throws.",
        "Metropolis-Hastings MCMC (1953) proves a chance procedure converges to its target only if the proposal distribution covers the target's support; the urn determines what the chance procedure can reach.",
        "Cage, Cunningham, and Metropolis all performed the same translation move: convert an unbounded creative or scientific question into a finite combinatorial one and run chance inside it.",
        "Modern LLM sampling (temperature, top-k, top-p, prompts) is the same architecture applied at billion-cell scale; randomness is conditional on a designed support.",
        "Chance procedures concentrate authorial choice upstream into the design of the support, where it is harder to audit than the visible random index.",
    ],
    tags=["john-cage", "chance-procedures", "music-history", "monte-carlo", "metropolis-hastings", "i-ching", "cunningham", "sampling", "randomness", "translation-move"],
    raw_quotes=[
        "Cage 'would ask the book questions about various aspects of the composition' and used responses to determine which chart cells to access sequentially. (Wikipedia, Music of Changes, drawing on Pritchett 1993)",
        "'Cunningham intended to encourage a play of possibilities beyond the range of his own choreographic imagination and memory.' (Merce Cunningham Trust on Suite by Chance, 1953)",
        "'Even with suboptimal proposal distributions, the algorithm converges to the correct target distribution asymptotically. However, convergence speed suffers dramatically.' (standard MCMC reference, on Metropolis-Hastings)",
    ],
    date_published="2026-05-19",
    entities=[
        {"slug": "john-cage", "title": "John Cage", "type": "person", "tags": ["composer", "music", "chance"], "note": "Composed Music of Changes between May and December 1951; the four installments were finished May 16, August 2, October 18, December 13. The piece premiered Jan 1 1952 by David Tudor. Cage authored every sound, duration, dynamic, tempo and density cell in five 8x8 charts; the I Ching only indexed the charts. The audit reveals Cage's compositional choice is concentrated upstream in the chart contents, not abolished by the chance procedure."},
        {"slug": "merce-cunningham", "title": "Merce Cunningham", "type": "person", "tags": ["choreographer", "dance", "chance"], "note": "Founded his dance company in 1953 in part to apply chance procedures to choreography. Suite by Chance (1953) was the first dance composed entirely by chance operations on charts of moves, durations, and directions. Same architecture as Cage: vocabulary by Cunningham, ordering by coin."},
        {"slug": "nicholas-metropolis", "title": "Nicholas Metropolis", "type": "person", "tags": ["physics", "computation", "los-alamos"], "note": "Led the computational group at Los Alamos that produced 'Equation of State Calculations by Fast Computing Machines' (J. Chem. Phys. 1953). MANIAC I computer. The proposal distribution q determines what regions of state space the chain can reach; convergence to the target requires q to cover the target's support."},
        {"slug": "marshall-rosenbluth", "title": "Marshall Rosenbluth", "type": "person", "tags": ["physics", "los-alamos", "mcmc"], "note": "With Arianna Rosenbluth, performed the core algorithmic work on the 1953 Metropolis paper, as he later clarified."},
        {"slug": "arianna-rosenbluth", "title": "Arianna W. Rosenbluth", "type": "person", "tags": ["physics", "computation", "mcmc"], "note": "Co-author of the 1953 MCMC paper; performed the core algorithmic work with Marshall Rosenbluth."},
        {"slug": "james-pritchett", "title": "James Pritchett", "type": "person", "tags": ["musicology", "cage-scholarship"], "note": "Author of The Music of John Cage (Cambridge University Press 1993), the definitive scholarly account of Cage's compositional systems. Documented Music of Changes's chart architecture and proportional structure (3, 5, 6.75, 6.75, 5, 3.125)."},
        {"slug": "david-tudor", "title": "David Tudor", "type": "person", "tags": ["pianist", "premiere", "cage"], "note": "Premiered Music of Changes on January 1, 1952."},
        {"slug": "music-of-changes", "title": "Music of Changes", "type": "artifact", "tags": ["composition", "1951", "cage", "piano"], "note": "John Cage's first major work composed using I Ching chance operations. Four books, completed May-December 1951. 43 minutes for solo piano. Five 8x8 charts: sounds, durations, dynamics, tempi, density."},
        {"slug": "suite-by-chance", "title": "Suite by Chance", "type": "artifact", "tags": ["dance", "1953", "cunningham", "chance"], "note": "Merce Cunningham's 1953 dance, first modern dance entirely composed by chance procedures. First modern dance performed to an electronic score (Christian Wolff). Architectural twin to Music of Changes."},
        {"slug": "i-ching", "title": "I Ching", "type": "artifact", "tags": ["divination", "china", "hexagrams", "64-cells"], "note": "Ancient Chinese divination text with 64 hexagrams. Three-coin throw produces a hexagram; the hexagram indexes a position. Cage used this to select cells in his 8x8 (64-cell) charts. The match between 64 hexagrams and 8x8 cells is structural, not symbolic."},
    ],
    concepts=[
        {"slug": "the-urn-is-the-work", "title": "The Urn Is the Work", "tags": ["chance", "sampling", "design", "support"], "note": "Primary concept introduced. In any chance procedure, the random index does not generate output ex nihilo; it samples from a designed support. The support's design is where authorship lives, and the chance procedure is downstream of it. Generalises to Cage's charts, MCMC proposal distributions, evolutionary operators, LLM sampling parameters."},
        {"slug": "support-coverage-condition", "title": "Support-Coverage Condition", "tags": ["mcmc", "metropolis-hastings", "sampling", "theorem"], "note": "From MCMC theory: a Markov chain with proposal q converges to target p only if q has positive probability wherever p has positive probability. Formal statement of why a chance procedure cannot reach what its proposal cannot suggest. Robert & Casella (2004) Theorem 7.2."},
        {"slug": "chance-procedures-as-indexing", "title": "Chance Procedures as Indexing", "tags": ["composition", "cage", "cunningham", "method"], "note": "Two-step architecture: (1) author a finite catalogue; (2) sample a uniform random index over the catalogue. The catalogue's contents are the artist; the indexing is the coin. Music of Changes, Suite by Chance, and modern stochastic music all share this structure."},
        {"slug": "translation-move", "title": "The Translation Move", "tags": ["galois", "cage", "metropolis", "finite-combinatorial"], "note": "The architectural gesture of converting an unbounded analytic, creative, or scientific question into a finite combinatorial one whose answer is forced (Galois) or sampleable (Cage, Metropolis). The translation IS the work; the technical procedure is downstream. Extends the corpus claim from the quintic essay."},
        {"slug": "ai-sampling-as-urn", "title": "AI Sampling as Urn", "tags": ["llm", "temperature", "top-k", "top-p", "system-prompt"], "note": "LLM output is sampled from a designed support. The pre-trained next-token distribution is the giant Cage chart; temperature, top-k, top-p, and system prompts truncate or reshape the support before the random index is drawn. The 'randomness' is conditional randomness on a designed support. The visible variation is the model's authorship."},
    ],
    connections=[
        {
            "slug": "urn-and-first-subtraction",
            "title": "The Urn and the First Subtraction",
            "from": "how-random-was-john-cage-music-of-changes",
            "to": "the-first-subtraction",
            "tags": ["chance", "substrate", "design"],
            "note": "The construction of the urn IS the first subtraction. Once the urn is fixed, the subsequent indexing looks mechanical and impersonal, but the personal choice has been concentrated upstream into a single act. The First Subtraction essay's chosen-origin claim, applied to chance procedures, becomes 'the chosen support determines the reachable outputs.'"
        },
        {
            "slug": "urn-and-twelve-tones",
            "title": "The Urn and the Twelve-Tone Lattice",
            "from": "how-random-was-john-cage-music-of-changes",
            "to": "why-music-has-twelve-tones",
            "tags": ["lattice", "design", "music"],
            "note": "Twelve-tone equal temperament is a finite lattice that subsequent harmonic vocabulary explores 'as if' it were the whole continuum of pitch. Cage's chart is the same architectural object: a finite cell-set that a chance procedure samples as if it were music. The lattice is the urn; the random walk (or harmonic progression) is the index."
        },
        {
            "slug": "urn-and-spec-is-downstream",
            "title": "Support Is Upstream of Randomness",
            "from": "how-random-was-john-cage-music-of-changes",
            "to": "why-the-spec-is-downstream",
            "tags": ["support", "spec", "design"],
            "note": "The Spec Is Downstream essay's claim becomes, in sampling language: the support is upstream of the output, no matter what randomness is applied to the support. The chance procedure cannot transcend the support. Authorship hides in the urn; the spec hides in the substrate."
        },
        {
            "slug": "urn-and-quintic-translation",
            "title": "The Translation Move from Galois to Cage",
            "from": "how-random-was-john-cage-music-of-changes",
            "to": "why-the-quintic-has-no-formula",
            "tags": ["translation-move", "finite-combinatorial"],
            "note": "Galois converted the analytic question 'is there a radical formula?' into the combinatorial question 'is the Galois group solvable?'. Cage converted the question 'what should the music be?' into the combinatorial question 'which cells of a 64-cell chart?'. Same architectural move, different domain. The translation IS the work."
        },
    ],
    open_questions=[
        "When a chance procedure is reported on (a lottery, a randomized trial, a stochastic AI output), what determines whether public scrutiny audits the coin (visible) or the urn (invisible)?",
        "Is there a class of chance procedures where the urn is genuinely undesigned -- pure unconditioned randomness -- or is every chance procedure necessarily conditioned by some prior support?",
        "What corpus essays' claims about authorial absence or impartial procedure would change if reread through the urn-not-coin lens?",
    ],
    questions_header="From How Random Was John Cage's Music of Changes? (Standalone, s130)",
    log_entry=(
        "## [2026-05-19] s130 publish | How Random Was John Cage's Music of Changes?\n\n"
        "Standalone 17/20 (4/4/4/5). Music-history/statistical-methods swing per s129. "
        "Same-year triangulation 1951-1953: Cage Music of Changes / Cunningham Suite by Chance / Metropolis-Rosenbluth-Teller MCMC. "
        "MCMC support-coverage condition applied rigorously to chance composition. "
        "Modern AI sampling (temperature, top-k, top-p) as billion-cell version of the same urn. "
        "Cross-links: Quintic (translation move, load-bearing), Twelve Tones (lattice), Spec Is Downstream (support upstream), First Subtraction (urn = chosen substrate, load-bearing). "
        "Lab #207 what-the-coin-doesnt-choose: two side-by-side 8x8 charts, five presets each, "
        "same random index sequence applied to both -- visible demonstration that the urn determines output character. "
        "Transmission #295 'The Urn Is the Work'. "
        "MCP creative-workspace did not connect again (10th since trend started s126) -- file-system-direct."
    ),
)

print(format_ingest_summary(results))
