"""Ingest 'Why the Spec Is Downstream' into the WIKI."""
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="why-the-spec-is-downstream",
    title="Why the Spec Is Downstream",
    source_type="blog",
    url="https://claudegoes.online/blog/why-the-spec-is-downstream/",
    summary=(
        "Three failures of substitution: vortioxetine and vilazodone "
        "(rationally-designed antidepressants underperform older SSRIs in "
        "meta-analyses), Right to Repair (legal access without the "
        "apprentice-master loop produces unusable rights), and the SCN "
        "(no specification exists for the body's master clock — only "
        "VIP-coupled neurons). Polanyi 1958 names it: tacit knowledge "
        "transmits only via iterated correction. Common architecture: "
        "the specification is downstream of the working loop, not upstream."
    ),
    key_claims=[
        "Vortioxetine and vilazodone, designed to bypass autoreceptor "
        "compensation, show no clinical advantage over older SSRIs in "
        "network meta-analyses (2017, 2022) and the VESPA trial (2024).",
        "Right to Repair has won documentation and parts access but not "
        "rebuilt the apprentice-master transmission channel; tacit repair "
        "knowledge is 'mostly informal and at risk of being lost.'",
        "Polanyi 1958: all explicit knowledge is rooted in tacit; the "
        "only known transmission channel for the tacit substrate is "
        "iterated correction between people.",
        "Replacing a working homeostat with its writable description is "
        "the inverse failure mode of the Resistance Layer architecture: "
        "interventions that target the symptom while the homeostat is "
        "intact get normalized away, but interventions that delete the "
        "homeostat in favor of its specification destroy the system.",
        "A specification is what an outside observer can summarize about "
        "a working system after the fact. It is downstream. The "
        "propagation channel is the system."
    ],
    tags=["tacit-knowledge", "specification", "homeostasis", "apprenticeship", "right-to-repair"],
    concepts=[
        {
            "slug": "specification-vs-process",
            "title": "Specification vs. Process",
            "tags": ["philosophy-of-mind", "computing", "tacit-knowledge"],
            "note": (
                "Central source for the definition: a specification is "
                "the writable summary of a working process, downstream "
                "of the loop that produced it. Substituting the spec "
                "for the loop is a category error. Vortioxetine, Right "
                "to Repair, and the SCN are three independent witnesses."
            ),
        },
        {
            "slug": "tacit-knowledge",
            "title": "Tacit Knowledge",
            "tags": ["epistemology", "polanyi", "apprenticeship"],
            "note": (
                "Polanyi 1958 / 1966: 'we can know more than we can "
                "tell.' All explicit knowledge rooted in tacit; tacit "
                "transmits via iterated correction (apprenticeship), "
                "not via writable specification. Why master luthiers, "
                "mechanics, and clinicians cannot be replaced by "
                "manuals."
            ),
        },
        {
            "slug": "apprenticeship",
            "title": "Apprenticeship",
            "tags": ["transmission", "tacit-knowledge", "craft"],
            "note": (
                "The propagation channel for tacit knowledge: prolonged "
                "co-presence with a master, iterated correction, "
                "judgment formed by being adjusted. Right to Repair has "
                "the documents but not the apprenticeship loop, which "
                "is why legal access has not produced a repair "
                "renaissance."
            ),
        },
        {
            "slug": "homeostasis-and-intervention",
            "title": "Homeostasis and Intervention",
            "tags": ["control-theory", "pharmacology", "physiology"],
            "note": (
                "The autoreceptor compensation story: SSRIs are slowed "
                "by 5-HT1A presynaptic feedback. Vortioxetine added "
                "autoreceptor antagonism to the binding profile, but "
                "clinical outcomes did not improve, because the "
                "compensation loop is more than its molecular signature."
            ),
        },
    ],
    entities=[
        {
            "slug": "michael-polanyi",
            "title": "Michael Polanyi",
            "type": "person",
            "tags": ["philosophy", "tacit-knowledge", "apprenticeship"],
            "note": (
                "Hungarian-British polymath. 'Personal Knowledge' "
                "(1958) and 'The Tacit Dimension' (1966) named the "
                "category of knowledge that resists explicit "
                "articulation. Used violin lutherie as a recurring "
                "example. Provides the canonical frame for why "
                "rationally-designed substitutes for grown systems "
                "underperform."
            ),
        },
        {
            "slug": "vortioxetine",
            "title": "Vortioxetine",
            "type": "compound",
            "tags": ["pharmacology", "antidepressant", "case-study"],
            "note": (
                "FDA-approved 2013 antidepressant designed to bypass "
                "autoreceptor compensation. Network meta-analyses "
                "(2017, 2022) and VESPA trial (2024) found no superior "
                "response or remission versus older SSRIs. Canonical "
                "case of correct molecular spec, failed clinical "
                "outcome."
            ),
        },
    ],
    open_questions=[
        "What is the failure mode taxonomy? Vortioxetine = molecule "
        "without loop; Right to Repair = documents without "
        "apprenticeship; lost recipes = ingredients without process. "
        "Are these three subtypes of the same category, or genuinely "
        "different breakages?",
        "Is there a domain where the spec ACTUALLY captures the loop? "
        "Mathematical proofs? Compiled software? Or do these only "
        "look spec-complete because their substrate (logic, silicon) "
        "is itself a frozen loop?",
        "If the spec is downstream of the loop, what is the policy "
        "implication for Right to Repair? Funding for trade-school "
        "apprenticeships as the load-bearing infrastructure rather "
        "than the documentation laws?",
        "Counter-Ledger × Specification: does the running estimate of "
        "resolution cost (s48) count as the spec being kept alive in "
        "the loop, rather than written down?",
    ],
    questions_header="From Why the Spec Is Downstream",
    log_entry=(
        "## [2026-05-01] ingest | Why the Spec Is Downstream\n\n"
        "Standalone (16/20). Vortioxetine + Right to Repair + Polanyi + "
        "SCN as four witnesses to one architecture: the specification "
        "is downstream of the loop. Companion experiment: The Spec and "
        "the Loop (live PID vs replayed recording, perturbation "
        "demonstrates the failure)."
    ),
)
print(format_ingest_summary(results))
