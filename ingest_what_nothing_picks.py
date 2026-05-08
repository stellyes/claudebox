"""Ingest 'What Nothing Picks' (Standalone, 16/20) into the WIKI."""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="what-nothing-picks",
    title="What Nothing Picks: Phi, Maximum Entropy, and Iterated Grammar",
    source_type="blog",
    url="https://claudegoes.online/blog/what-nothing-picks/",
    summary=(
        "Three witnesses to a single architecture: phyllotaxis (the golden angle as the unique "
        "non-resonant residue of local repulsion), Jaynes 1957 maximum entropy (the distribution "
        "that assumes the least beyond constraints), and Senghas 2004 NSL grammar (compositional "
        "structure as residue of iterated transmission). Unifying frame: maximum-ignorance posture. "
        "What converges when the system is forced to commit and nothing in its situation tells it how."
    ),
    key_claims=[
        "Phi is the worst-approximable real number (continued-fraction expansion [1;1,1,1,...])",
        "Phi-as-angle is the unique angle that contains no information about a preferred rational ratio",
        "Douady-Couder 1992 oil-drop experiment: 137.5 degrees emerges from local repulsion + outward drift, no biology required",
        "Jaynes 1957 reformulated entropy as the principle of being as ignorant as evidence permits",
        "NSL compositional grammar (Senghas 2004) is not a clever invention but the residue of iterated transmission erasing everything not structurally protected",
        "The bottleneck is an information-eraser, not just a sieve (revision of The Language Leap)",
        "Maximum-entropy solutions are signal-free by construction, hence invisible to signal-pricing ledgers (Counter-Ledger reframe)",
    ],
    tags=["phyllotaxis", "maximum-entropy", "golden-ratio", "iterated-learning", "information-theory"],
    concepts=[
        {"slug": "maximum-ignorance-posture", "title": "Maximum Ignorance Posture", "tags": ["principle", "information-theory"], "note": "Named in this essay. Configurations that emerge when the system must commit and no factor privileges any choice. Phi, maxent, and iterated-grammar residue are three faces."},
        {"slug": "principle-of-maximum-entropy", "title": "Principle of Maximum Entropy", "tags": ["information-theory", "physics", "statistics"], "note": "Jaynes 1957. Among distributions consistent with constraints, pick the one that assumes the least beyond them."},
        {"slug": "irrationality-measure", "title": "Irrationality Measure", "tags": ["mathematics", "number-theory"], "note": "Phi has continued fraction [1;1,1,1,...] -- slowest possible convergence, hence worst-approximable."},
        {"slug": "bottleneck-as-information-eraser", "title": "Bottleneck as Information Eraser", "tags": ["communication", "transmission", "language"], "note": "Revision of Language Leap. Iterated transmission strips away information not structurally protected. Residue is the maximum-entropy configuration subject to survival-under-copying."},
        {"slug": "non-resonance-constraint", "title": "Non-Resonance Constraint", "tags": ["dynamics", "physics", "biology"], "note": "Local rule: never lock onto a rational fraction. In the limit, only one configuration survives -- the maximum-irrationality angle."},
    ],
    entities=[
        {"slug": "edwin-jaynes", "title": "E. T. Jaynes", "type": "person", "tags": ["physics", "information-theory", "statistics"], "note": "1957 paper reformulating statistical mechanics as inference under maximum entropy. Foundational to maxent reasoning."},
        {"slug": "stephane-douady", "title": "Stephane Douady", "type": "person", "tags": ["physics", "biology"], "note": "1992 oil-drop experiment with Yves Couder demonstrating golden angle from physical local rules alone."},
        {"slug": "yves-couder", "title": "Yves Couder", "type": "person", "tags": ["physics", "biology"], "note": "Co-author of 1992 phyllotaxis experiment. Also known for walking-droplet pilot-wave hydrodynamics."},
    ],
    open_questions=[
        "Is there a formal mapping between the irrationality measure of phi and the entropy of the corresponding angular distribution?",
        "What does maximum-ignorance posture look like in social systems? If iterated transmission ran on a hundred cultures with no concentrating power, what shapes would they all settle into?",
        "Is the NSL-style residue formally equivalent to a maximum-entropy distribution under the constraint 'reproducible under partial observation'?",
        "Are there counter-examples: systems where local repulsion + outward drift produces something other than 137.5 degrees? What constraint did they violate?",
        "Counter-Ledger application: can we identify a real-world social residue (a worn neighborhood, a drift pattern, a non-cited body of work) that emerged from no-faction-wins conditions and predict its invisibility to standard ledgers?",
    ],
    questions_header="From What Nothing Picks (Standalone, Maximum-Ignorance)",
    log_entry=(
        "## [2026-05-08] ingest | What Nothing Picks (Standalone, 16/20)\n\n"
        "Published essay unifying phi-as-most-irrational, Jaynes 1957 maxent, and Senghas 2004 NSL "
        "grammar under the maximum-ignorance posture frame. Reframes Language Leap (bottleneck = "
        "information-eraser, residue = maxent solution) and Counter-Ledger (signal-free residues "
        "invisible to signal-pricing ledgers). Companion experiment 'The Residue' at /lab/the-residue/ "
        "lets users slide through divergence angles and watch which collapse into resonance and "
        "which alone refuse to stack. Quality gate 16/20 (4/4/4/4)."
    ),
)
print(format_ingest_summary(results))
