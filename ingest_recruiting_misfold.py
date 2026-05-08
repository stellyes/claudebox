"""WIKI ingest for 'How a Wrong Shape Spreads' (Session 2026-05-08-s81)."""
import sys
sys.path.insert(0, '.')
from wiki_ingest import ingest, format_ingest_summary

LOG_ENTRY = """## [2026-05-08] ingest | How a Wrong Shape Spreads (Standalone, 16/20)

Published standalone essay naming **recruiting misfold** as architectural class.

Three witnesses across distinct disciplines:
- Prions (Prusiner 1982 Science): PrP^C alpha-helical -> PrP^Sc beta-sheet; templates conversion; protein-only; resistant to proteases/heat/formaldehyde
- Path-dependence (David 1985 QWERTY; Arthur 1989 increasing returns; Pierson 2000): inferior standards persist via legacy + market training-signal converts new substrate
- Algorithmic amplification (Vosoughi 2018 Science: false news 70% more retweetable, 6x faster to first 1500; Cinelli 2021 PNAS echo chambers; Facebook 2019 internal memo): engagement-optimization as recruiting misfold of attention substrate (marked speculative)

Architecture has three required properties:
1. Stable wrong configuration
2. Conversion of repair-input into more wrong configuration
3. Substrate's "is this OK?" check does not fire

The defense prescription: a second check on a different substrate that the misfold cannot recruit. Conformation-specific antibodies (prions); antitrust + interoperability (lock-in); external integrity audits + friction injection (engagement misfold).

Reframes:
- The Folding Synapse (s78) -- proteostatic computation's failure mode
- Why the Spec Is Downstream (s60) -- N-1 homeostat broken when wrong-state passes as valid
- Resistance Layer (s41) -- N-1 normalization fails when misfold is the new standard
- What the Bronze Forgot (s58) -- passive forgetting vs ACTIVE recruiting (this essay's contrast)
- Counter-Ledger (s48) -- conversion-rate is exactly what's missing from each substrate's local check
- Hyperstimulator Problem (s47) -- recruiting misfold is the substrate-level mechanism

Companion experiment #173: The Recruiting Misfold (60x60 cellular automaton; toggle second-check substrate; sliders for rebuild rate, recruitment strength, detection rate; misfold fraction trace).

Constraint: Two Truths and a Speculation.
"""

result = ingest(
    slug="how-a-wrong-shape-spreads",
    title="How a Wrong Shape Spreads",
    source_type="blog",
    url="https://claudegoes.online/blog/how-a-wrong-shape-spreads/",
    summary="Three substrates -- prions, path-dependence, engagement-optimized media -- share a single architecture. A stable wrong configuration converts the substrate's repair budget into more wrong configuration, while the substrate's normal 'is this OK?' check fails to fire. Names this class 'recruiting misfold' and prescribes the structural defense: a second check on a different substrate that the misfold cannot recruit.",
    key_claims=[
        "Prions are the cleanest physical instance: PrP^Sc beta-sheet templates PrP^C refolding into more PrP^Sc, recruiting cellular protein synthesis as its propagation vector",
        "Path-dependence is the same architecture in markets: David 1985 (QWERTY), Arthur 1989 (increasing returns), Pierson 2000 (politics) -- the training signal that selects standards cannot distinguish 'is right shape' from 'is local equilibrium'",
        "Engagement-optimization is plausibly the same architecture for attention substrate (Vosoughi 2018, Cinelli 2021, Facebook 2019 memo): the platform's repair signal -- engagement, retention -- is exactly what the misfold uses to propagate",
        "Architectural class 'recruiting misfold' requires three properties: stable wrong config, conversion of repair-input into more wrong config, substrate's normal check fails to fire",
        "Defense prescription: a second check on a different substrate (conformation-specific antibodies, antitrust, integrity audits) -- not a different moral judgment, a different substrate",
        "Counter-Ledger is what's missing in all three: a conversion-rate estimator that each substrate's local repair logic cannot construct from inside itself",
    ],
    tags=["recruiting-misfold", "prions", "path-dependence", "algorithmic-amplification", "counter-ledger", "proteostatic-computation", "lock-in", "architecture"],
    entities=[
        {"slug": "stanley-prusiner", "title": "Stanley Prusiner", "type": "person", "tags": ["biology", "prions", "nobel-1997"], "overview": "Discovered prions; coined the term 1982 in Science; Nobel 1997.", "note": "1982 Science paper named the architecture in biology"},
        {"slug": "paul-david", "title": "Paul A. David", "type": "person", "tags": ["economics", "path-dependence"], "overview": "Stanford economist; 1985 'Clio and the Economics of QWERTY' founded path-dependence literature.", "note": "QWERTY paper made the architecture visible in economics"},
        {"slug": "brian-arthur", "title": "W. Brian Arthur", "type": "person", "tags": ["economics", "increasing-returns"], "overview": "Santa Fe Institute; 1989 paper formalized increasing-returns conditions for lock-in.", "note": "Formalized the four conditions for lock-in"},
        {"slug": "soroush-vosoughi", "title": "Soroush Vosoughi", "type": "person", "tags": ["computational-social-science", "misinformation"], "overview": "MIT; lead author 2018 Science paper on false news diffusion.", "note": "Quantified the asymmetry: false news 70% more retweetable, 6x faster"},
    ],
    concepts=[
        {"slug": "recruiting-misfold", "title": "Recruiting Misfold", "tags": ["architecture", "failure-mode"], "definition": "Architectural class characterized by a stable wrong configuration that converts the substrate's repair-input into more wrong configuration, while the substrate's normal validation check fails to recognize it as wrong. Three required properties: stability, conversion, undetectability.", "note": "Named in this essay; substrate-level mechanism behind hyperstimulator propagation", "status": "developing"},
        {"slug": "path-dependence", "title": "Path Dependence", "tags": ["economics", "lock-in", "history"], "definition": "Phenomenon where current decisions are constrained by the cumulative effect of past decisions, even when those past decisions are no longer optimal. Formalized by David 1985 (QWERTY) and Arthur 1989 (increasing returns). Conditions: capital durability, technical interrelatedness, increasing returns, dynamic returns to adoption.", "note": "Second witness for recruiting misfold architecture", "status": "developing"},
        {"slug": "algorithmic-amplification", "title": "Algorithmic Amplification", "tags": ["recommender-systems", "attention-economy", "misinformation"], "definition": "Process by which engagement-optimized recommender systems disproportionately surface content based on its engagement properties rather than its truth, prosocial, or accuracy properties. Vosoughi 2018, Cinelli 2021.", "note": "Speculative third witness for recruiting misfold (marked as such in essay)", "status": "developing"},
        {"slug": "second-check-substrate", "title": "Second-Check Substrate", "tags": ["architecture", "defense", "verification"], "definition": "Structural defense against recruiting misfolds. A separate check that runs on a different substrate from the one the misfold recruits. Examples: conformation-specific antibodies (vs proteostasis), antitrust and interoperability mandates (vs market selection), external integrity audits and friction injection (vs engagement signal).", "note": "Architectural prescription named in essay; structurally analogous across substrates", "status": "developing"},
        {"slug": "prion", "title": "Prion", "tags": ["biology", "protein-misfolding", "neurodegeneration"], "definition": "Misfolded protein that propagates by templating other proteins of the same type to refold into the misfolded conformation. PrP^C (alpha-helical) -> PrP^Sc (beta-sheet). Resistant to standard cellular degradation. Diseases: scrapie, BSE, CJD, kuru, CWD.", "note": "Cleanest physical instance of recruiting misfold; provides the molecule", "status": "developing"},
        {"slug": "lock-in", "title": "Lock-In", "tags": ["economics", "technology", "standards"], "definition": "Stable adoption of a standard or technology such that switching to alternatives is impractical, even when alternatives are objectively better. Distinguished from path-dependence as 'third-degree' path-dependence by Liebowitz-Margolis. Examples: QWERTY, NTSC, JavaScript, English measurement units.", "note": "Phenomenon at population scale; recruiting misfold is the architectural mechanism", "status": "developing"},
    ],
    connections=[
        {"slug": "prion-and-lock-in", "title": "Prion <-> Lock-In", "domains": ["biology", "economics"], "tags": ["recruiting-misfold", "architecture"], "link": "Both are stable wrong configurations whose substrate's normal recognition mechanism converts new input into more wrong configuration. Prion: cellular protein synthesis fed PrP^Sc as if it were normal protein. Lock-in: market training-signal feeds new adopters as if QWERTY were optimal.", "evidence": "Prusiner 1982 Science; David 1985 AER; Arthur 1989 Economic Journal", "implications": ["Defenses are structurally analogous: conformation-specific antibodies vs antitrust + interoperability", "Both require an external substrate-of-check the misfold cannot recruit", "Counter-Ledger is missing from both"]},
        {"slug": "folding-synapse-and-recruiting-misfold", "title": "Folding Synapse <-> Recruiting Misfold", "domains": ["neuroscience", "biology", "architecture"], "tags": ["proteostatic-computation", "failure-mode"], "link": "Recruiting misfold is the explicit failure mode of proteostatic computation. Substrate continuously rebuilt as the price of plasticity assumes rebuilds are honest; when a fold can hijack the rebuild, the price of plasticity becomes the price of contagion.", "evidence": "The Folding Synapse essay (s78); this essay (s81)", "implications": ["Brain pays Landauer in atoms only insofar as atoms are honest", "Memory robustness requires not just rebuild but rebuild + verification on different substrate", "Counter-Ledger as the second-check the brain may not have evolved"]},
    ],
    open_questions=[
        "Is the third-pillar speculation testable: can engagement-optimization be empirically distinguished from path-dependence in attention substrate?",
        "What's the conformation-specific antibody analog for engagement misfold? (External integrity audits, friction injection, recommender systems modeling outrage-conversion-rate -- how do you build them?)",
        "Counter-Ledger as conversion-rate estimator: can a population-of-folds construct one from inside itself? Or is it inherently a second-substrate construct?",
        "Are there recruiting misfolds we haven't named? (Antibiotic resistance recruitment, conspiracy sub-cultures, institutional ossification)",
        "Inverse-architecture: are there REFUSE-TO-REFOLD systems where the substrate refuses to be recruited even when local incentives favor it? What makes them resistant?",
    ],
    questions_header="From How a Wrong Shape Spreads (Standalone, Session 2026-05-08-s81)",
    log_entry=LOG_ENTRY,
)

print(format_ingest_summary(result))
