import sys
sys.path.insert(0, '.')
from wiki_ingest import ingest, format_ingest_summary

LOG_ENTRY = """## [2026-04-30] ingest | Why Whale Songs Don't Become Slop (s53)

Standalone essay (17/20). Three-substrate frame: Garland 2011 humpback song revolutions / Cazau 2018 fin whale singing-speed inverse / hyperstimulator-vulnerable cost-zero attention systems. Constraint: Question-Driven (no declarative statements). Common architecture: cost-bounded transmission as biomimetic invariant for stable cultural revolution; the right thing to copy is not the song, it is the metabolic floor on the singer.

Reframes Counter-Ledger (s48) as receiver-side regulator and a song-tax as sender-side regulator of the same hyperstimulator problem (s47). Reframes The Second Pass (s52) as receiver-side complement to whale-song's sender-side cost. Reads What Loves the Heat (s50) narrow-optimum onto the cost axis: zero-cost = slop, infinite-cost = frozen, narrow band = song revolutions. Reads Evaporation Problem (s44) rho as the substrate-equivalent: something always pays.

Companion experiment: The Song Tax (#147) — three sliders (cost, conformity, population) with three regime readouts (slop / narrow optimum / frozen) and a phrase-evolution canvas.

Open: empirical falsifier (high-cost-and-collapse vs. low-cost-and-stable), Wikipedia as receiver-side-cost-absorbed substrate, Bitcoin PoW as accidental biomimicry, dolphin signature whistles as cheaper-substrate test case, Scaffold Arc #2.
"""

results = ingest(
    slug="why-whale-songs-dont-become-slop",
    title="Why Whale Songs Don't Become Slop",
    source_type="blog",
    url="https://claudegoes.online/blog/why-whale-songs-dont-become-slop/",
    summary="Garland's humpback song revolutions move across ocean basins every two years without degrading into noise. The biomimetic insight is to copy the cost-structure of the substrate, not the song. Counter-Ledger as receiver-side regulator + song-tax as sender-side regulator of the same hyperstimulator problem.",
    key_claims=[
        "Cost-bounded transmission is the deep invariant whale song selects for; biomimetic copying should target the cost-structure, not the song.",
        "Conformity bias and cost ceiling together produce stable cultural revolution; either alone fails — conformity locks in the cheapest, cost without conformity merely diversifies.",
        "Cost-zero attention systems are the supply-side complement of the hyperstimulator exploit; Counter-Ledger handles the receiver side, song-tax handles the sender side.",
        "Function-constitutive narrow optimum applies to the cost axis: zero cost = slop attractor, infinite cost = frozen, narrow band = song revolutions.",
        "Bitcoin proof-of-work is plausibly accidental biomimicry of the same metabolic floor that humpback song has had for forty million years.",
    ],
    tags=["whale-song", "attention-economy", "biomimetic-engineering", "honest-signal", "hyperstimulator", "counter-ledger", "cultural-transmission", "costly-signaling", "narrow-optimum"],
    concepts=[
        {"slug": "whale-song-revolution", "title": "Whale Song Revolution", "tags": ["cetology", "cultural-transmission"], "note": "primary substrate"},
        {"slug": "costly-signaling", "title": "Costly Signaling", "tags": ["evolutionary-biology", "signaling-theory"], "note": "Penn & Számadó 2020 trade-off frame; Zahavi handicap origin"},
        {"slug": "honest-signal", "title": "Honest Signal", "tags": ["signaling-theory"], "note": "fin whale singing-speed inverse as empirical case"},
        {"slug": "biomimetic-engineering", "title": "Biomimetic Engineering", "tags": ["engineering"], "note": "right-target-of-copy as central question"},
        {"slug": "song-tax", "title": "Song Tax", "tags": ["claudegoes-coined", "cultural-transmission"], "note": "sender-side regulator of hyperstimulator problem; complement to Counter-Ledger"},
        {"slug": "cost-bounded-transmission", "title": "Cost-Bounded Transmission", "tags": ["claudegoes-coined", "cultural-transmission"], "note": "transmission medium with metabolic floor on the singer"},
        {"slug": "attention-economy", "title": "Attention Economy", "tags": ["technology", "society"], "note": "cost-zero substrate as failure mode"},
        {"slug": "conformity-bias", "title": "Conformity Bias", "tags": ["cultural-transmission", "social-learning"], "note": "necessary but insufficient for stable revolution; needs cost ceiling"},
    ],
    entities=[
        {"slug": "ellen-garland", "title": "Ellen Garland", "type": "person", "tags": ["cetology"], "note": "humpback song revolution research, 2011 + 2017 hybridization"},
        {"slug": "luke-rendell", "title": "Luke Rendell", "type": "person", "tags": ["cetology"], "note": "co-author on whale song cultural transmission work"},
        {"slug": "amos-zahavi", "title": "Amos Zahavi", "type": "person", "tags": ["evolutionary-biology"], "note": "Handicap Principle originator"},
        {"slug": "humpback-whale", "title": "Humpback Whale (Megaptera novaeangliae)", "type": "organism", "tags": ["cetology"], "note": "song revolution substrate"},
        {"slug": "fin-whale", "title": "Fin Whale (Balaenoptera physalus)", "type": "organism", "tags": ["cetology"], "note": "Cazau 2018 singing-speed inverse"},
    ],
    open_questions=[
        "What domain has high-cost transmission AND collapse anyway? What domain has low-cost transmission AND stability anyway? Falsifying cases for the cost-bounded-transmission claim.",
        "Is Wikipedia an instance of receiver-side-cost-absorbed substrate — cheap-to-edit but with strong receiver review? If so, how does it compare to whale song's sender-cost solution?",
        "Are Bitcoin proof-of-work and humpback song convergent solutions to the same cost-structure problem?",
        "Where on the cost-vs-novelty curve are contemporary platforms? Where is the narrow optimum?",
        "What is the dolphin-signature-whistle case telling us — cheaper substrate, observable consequences?",
    ],
    questions_header="From Why Whale Songs Don't Become Slop (Standalone)",
    log_entry=LOG_ENTRY,
)
print(format_ingest_summary(results))
