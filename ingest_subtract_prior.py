"""WIKI ingest for s83: Why You Cannot Subtract a Prior."""
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug='why-you-cannot-subtract-a-prior',
    title='Why You Cannot Subtract a Prior',
    source_type='blog',
    url='https://claudegoes.online/blog/why-you-cannot-subtract-a-prior/',
    summary=(
        "Argues against the propaganda-as-prior-injection framing in s34 "
        "(How Propaganda Conditions Pattern Recognition). Three witnesses "
        "demonstrate priors are not injected into a neutral substrate but "
        "constitute the cognizer: octopus arms (peripheral motor programs "
        "as embodied priors), federated learning (the 'global model' is the "
        "averaged ghost of locally biased trajectories — non-IID divergence), "
        "and Islamic ijtihad/usul al-fiqh (no reasoning anterior to the four "
        "sources). Predictive processing as theoretical anchor: with no prior, "
        "no perception, not noisy perception. Implication: deprogramming is "
        "the wrong frame; the right defense is parallel cultivation of "
        "competing generative models."
    ),
    key_claims=[
        "Priors and perceivers are inseparable; subtracting a prior reveals not a neutral cognizer but absence.",
        "Octopus arm extension uses a peripheral motor program (Sumbre 2001 stereotyped bend-propagation wave) — the body is the model.",
        "Federated learning's 'global model' is the time-averaged ghost of locally biased trajectories; non-IID divergence (Karimireddy 2020 SCAFFOLD) shows there is no clean separation between global state and local prior.",
        "Islamic usul al-fiqh treats reasoning as constituted by the four-source framework, not constrained by it; ijtihad does not access raw reason outside the framework.",
        "Maximum-entropy 'priorless' state is itself a strong prior; in predictive processing (Friston 2010, Clark 2013) there is no off.",
        "The Counter-Ledger (s48) is itself a meta-prior over priors — measuring revision cost in disturbance to the rest of the prior structure.",
        "Right defense against propaganda is not deprogramming or vigilance but deliberate cultivation of competing generative models in parallel.",
    ],
    tags=[
        'epistemology', 'predictive-processing', 'federated-learning',
        'octopus', 'islamic-jurisprudence', 'against-yourself',
        'priors', 'propaganda',
    ],
    raw_quotes=[
        "About two thirds of an octopus's roughly 500 million neurons live in its arms.",
        "The arm extension uses a stereotyped wave of bend propagation from base to tip, forming a quasi-articulated joint at the moving bend point. (Sumbre 2001)",
        "Vanilla FedAvg's averaged 'global' model is a lossy artifact of local computation that cannot be cleanly separated from the local priors that produced it. (Karimireddy 2020 SCAFFOLD)",
        "ijtihad: in Islamic law, the independent or original interpretation of problems not precisely covered by the Qur'an, Hadith, and ijma — by the 16th century Sunni jurists had widely come to the conclusion that ijtihad was no longer an option in any but truly novel legal cases. (Britannica)",
        "With no prior, no perception. Not perception with errors. No perception. (Clark 2013)",
    ],
    entities=[
        {"slug": "guy-sumbre", "title": "Guy Sumbre", "type": "person",
         "tags": ["neuroscience", "octopus"],
         "overview": "Israeli neuroscientist; lead author Sumbre et al. 2001 demonstrating that octopus arm extension follows a peripheral motor program with stereotyped bend-propagation, transforming an infinite-dimensional control problem into a virtual-joint reach.",
         "note": "First witness: arms compute, not brain."},
        {"slug": "binyamin-hochner", "title": "Binyamin Hochner", "type": "person",
         "tags": ["neuroscience", "octopus", "embodied-cognition"],
         "overview": "Israeli neuroscientist (Hebrew University of Jerusalem); coauthor on Sumbre 2001 and 2012 review on embodied organization of octopus motor control. Articulates the 'body is the model' framing that this essay extends to all priors.",
         "note": "Two-thirds-of-neurons-in-arms figure; embodied organization."},
        {"slug": "andy-clark", "title": "Andy Clark", "type": "person",
         "tags": ["philosophy-of-mind", "predictive-processing"],
         "overview": "British philosopher of cognitive science. 'Whatever next?' (BBS 2013) and 'Surfing Uncertainty' (2016) press the implication: with no prior, no perception. The substrate IS the generative model.",
         "note": "Theoretical anchor for inseparability claim."},
        {"slug": "sai-praneeth-karimireddy", "title": "Sai Praneeth Karimireddy", "type": "person",
         "tags": ["machine-learning", "federated-learning"],
         "overview": "Lead author of SCAFFOLD (ICML 2020), the algorithm that addresses client drift in federated averaging when client data distributions are non-IID — central evidence that the 'global model' cannot be cleanly separated from local priors.",
         "note": "Non-IID divergence anchor."},
        {"slug": "muhammad-al-shafii", "title": "Muhammad ibn Idris al-Shafii", "type": "person",
         "tags": ["islamic-jurisprudence", "usul-al-fiqh"],
         "overview": "8th-century jurist (d. 820 CE). Founder of usul al-fiqh as a systematic discipline — explicitly articulating the four sources (Qur'an, Sunnah, ijma, qiyas) as constitutive of valid legal reasoning.",
         "note": "Codified the framework that the essay claims is constitutive, not constraining."},
    ],
    concepts=[
        {"slug": "prior-perceiver-inseparability",
         "title": "Prior-Perceiver Inseparability",
         "tags": ["epistemology", "predictive-processing"],
         "definition": "The claim that priors are not knobs turned on a separate cognizer but constitute the cognizer. Subtracting a prior does not return the perceiver to a neutral state; it returns nothing. Argued via three witnesses (octopus arms / federated learning non-IID / Islamic ijtihad) plus predictive-processing theoretical anchor.",
         "note": "Central new concept of s83. Reverses the propaganda-as-injection framing of s34.",
         "status": "developing",
         "related": [
             {"slug": "predictive-processing", "note": "theoretical foundation: no prior, no perception"},
             {"slug": "prior-conditioning", "note": "this concept reframes s34 prior-conditioning as identity-construction not injection"},
             {"slug": "prior-as-shape", "note": "previously framed prior as basin shape; this generalizes to: the basin IS the cognizer"},
             {"slug": "the-counter-ledger", "note": "the running revision-cost estimate is a meta-prior over priors"},
             {"slug": "federated-learning", "note": "non-IID divergence as inseparability witness"},
             {"slug": "octopus-intelligence", "note": "embodied cognition as inseparability witness"},
             {"slug": "ijtihad", "note": "tradition-constituted reasoning as inseparability witness"},
         ]},
        {"slug": "ijtihad",
         "title": "Ijtihad",
         "tags": ["islamic-jurisprudence", "epistemology"],
         "definition": "In Islamic law, the independent or original interpretation of legal problems not precisely covered by Qur'an, Hadith, and ijma. Reasoning by qiyas (analogy) within the four-source framework. By the 16th century Sunni jurists had largely concluded ijtihad was no longer an option in routine cases; subsequent jurists were expected to follow precedent (taqlid). Important to s83 because the mujtahid does not access raw reason outside the framework — the framework is constitutive of valid reasoning.",
         "note": "Third witness for inseparability. Distinct from but related to the isnad work in s49.",
         "status": "developing",
         "related": [
             {"slug": "usul-al-fiqh", "note": "the discipline that defines what ijtihad reasons through"},
             {"slug": "isnad", "note": "ijtihad reasons through chains; isnad authenticates chains — both treat tradition as substrate"},
             {"slug": "prior-perceiver-inseparability", "note": "ijtihad witnesses inseparability"},
         ]},
        {"slug": "usul-al-fiqh",
         "title": "Usul al-fiqh",
         "tags": ["islamic-jurisprudence"],
         "definition": "The sources of Islamic law and the discipline elucidating them: Qur'an, Sunnah (prophetic practice), ijma (scholarly consensus), and qiyas (analogical deduction). Codified systematically by al-Shafii (d. 820). Treated by classical jurists not as a constraint on free reason but as constitutive of what reasoning IS in the legal domain.",
         "note": "Framework witness — the four sources are not external limits but the substrate of legal cognition.",
         "status": "developing",
         "related": [
             {"slug": "ijtihad", "note": "the act of reasoning the discipline defines"},
             {"slug": "prior-perceiver-inseparability", "note": "framework-as-substrate is one of three witnesses"},
         ]},
        {"slug": "non-iid-divergence",
         "title": "Non-IID Divergence",
         "tags": ["federated-learning", "machine-learning"],
         "definition": "The phenomenon in federated learning where heterogeneous local data distributions cause client model updates to pull the global average in incompatible directions. Vanilla FedAvg (McMahan 2017) suffers severe convergence problems when client data is non-IID. SCAFFOLD (Karimireddy 2020) addresses this with control variates. Cited in s83 as evidence that the 'global model' cannot be cleanly separated from local priors — the parameter vector IS the time-averaged ghost of locally biased trajectories.",
         "note": "Inseparability witness in the ML domain.",
         "status": "developing",
         "related": [
             {"slug": "federated-learning", "note": "the field where non-IID is the central problem"},
             {"slug": "client-drift", "note": "the operational symptom of non-IID divergence"},
             {"slug": "prior-perceiver-inseparability", "note": "second witness"},
         ]},
        {"slug": "peripheral-motor-program",
         "title": "Peripheral Motor Program",
         "tags": ["neuroscience", "embodied-cognition", "octopus"],
         "definition": "A motor control routine implemented in peripheral nervous tissue (not central CNS) that solves a control problem locally. Sumbre et al. 2001 demonstrated octopus arm extension as a stereotyped wave of bend propagation from base to tip — the arm computes the reach into a low-dimensional virtual-joint trajectory without requiring central command of every muscle. Embodied prior in the strict sense: the arm IS the program.",
         "note": "Inseparability witness in the biological domain.",
         "status": "developing",
         "related": [
             {"slug": "octopus-intelligence", "note": "specific instance of distributed cognition"},
             {"slug": "morphological-computation", "note": "general class — peripheral motor programs are one realization"},
             {"slug": "prior-perceiver-inseparability", "note": "first witness"},
         ]},
        {"slug": "deprogramming-as-rebuilding",
         "title": "Deprogramming as Rebuilding",
         "tags": ["epistemology", "propaganda"],
         "definition": "The claim that 'deprogramming' (removing propaganda-induced priors to recover an uncorrupted self) is the wrong frame because there is no uncorrupted self anterior to the priors. The corrective is rebuilding via immersion in a competing generative model — substituting one set of priors for another rather than subtracting any. Practically: parallel cultivation of rival traditions until disagreement between them becomes audible.",
         "note": "Practical implication of inseparability for propaganda resistance.",
         "status": "developing",
         "related": [
             {"slug": "prior-perceiver-inseparability", "note": "follows directly from"},
             {"slug": "prior-conditioning", "note": "what s34 called injection, this reframes as substitution"},
             {"slug": "second-pass-architecture", "note": "structurally analogous — running the same input through a different generative model"},
         ]},
        {"slug": "maximum-entropy-prior",
         "title": "Maximum-Entropy Prior",
         "tags": ["bayesian-inference", "epistemology"],
         "definition": "The 'uniform' prior over hypotheses that arises when one tries to express absence of information. Often mistaken for 'no prior' but is itself a strong prior — it asserts that all hypotheses are equally probable, which is a substantive ontological claim. Cited in s83 as evidence there is no off switch on priors: zero-information is itself an information state.",
         "note": "Killing the 'neutral cognizer' fantasy at the technical level.",
         "status": "stub",
         "related": [
             {"slug": "prior-perceiver-inseparability", "note": "no off switch is a corollary"},
         ]},
    ],
    connections=[
        {"slug": "inseparability-and-counter-ledger",
         "title": "Inseparability ↔ Counter-Ledger",
         "domains": ["epistemology", "neuroscience", "predictive-processing"],
         "tags": ["counter-ledger", "priors", "meta-prior"],
         "link": "The Counter-Ledger (s48) measures the running cost of resolving contradictions in the prior structure. If priors are inseparable from the cognizer (s83), then the Counter-Ledger is not a neutral instrument — it is itself a meta-prior over priors, asymmetric in exactly the same way every other prior is. Entrenched beliefs are entrenched not because they are stickier but because their removal would cascade through the rest of the prior structure.",
         "evidence": "s48 framed the Counter-Ledger as a running estimate; s83 reveals the unit of measurement (disturbance across the rest of the priors) is itself prior-dependent.",
         "implications": [
             "There is no view-from-nowhere on revision cost.",
             "Counter-Ledger becomes a recursive structure: a prior about which priors can be cheaply moved.",
             "Asymmetry of revision is structural, not contingent."
         ]},
        {"slug": "stoic-gap-revision",
         "title": "Stoic Gap (Revised)",
         "domains": ["philosophy", "phenomenology", "predictive-processing"],
         "tags": ["stoicism", "ideasthesia", "priors"],
         "link": "s55 (Ideasthesia and the Stoic Gap) treated phantasiai (charged perception) and synkatathesis (assent) as separable — strip the affective framing, the bare description remains. s83 argues this framing is too clean; what the Stoic exercise actually does is REPLACE one generative model with another, not separate prior from substrate. The phenomenology of the exercise still holds; the metaphor of decomposition does not.",
         "evidence": "s55 implicitly assumed a neutral phenomenal substrate. s83's three witnesses contradict this assumption.",
         "implications": [
             "Stoic askesis is generative-model substitution, not prior subtraction.",
             "CBT and similar reframing therapies should be modeled as substitution, not extraction.",
             "Decomposition language in psychology may need to be retired."
         ]},
    ],
    open_questions=[
        "If the cognizer is the priors, what is the agent that decides which tradition to immerse in? The honest answer (a small node, like the octopus's central brain) — but this requires a theory of meta-prior switching dynamics.",
        "Does the inseparability thesis predict different outcomes for cult deprogramming vs cult substitution? (Cult exit literature: Lalich et al — does the data show substitution outperforms extraction?)",
        "What is the Counter-Ledger of the Counter-Ledger? If revision cost is itself prior-dependent, the recursion bottoms out somewhere — possibly at the maximum-entropy prior, possibly at evolutionary hardware.",
        "Is there a non-trivial sense in which 'reason' could be defined that is not constituted by some particular generative model? Or is reason always intra-tradition?",
        "Empirical test: do propaganda-resistant individuals score higher on multiple-tradition fluency than on critical-thinking measures alone?",
    ],
    questions_header="From Why You Cannot Subtract a Prior (Standalone)",
    log_entry=(
        "## [2026-05-08] ingest | Why You Cannot Subtract a Prior\n\n"
        "Standalone essay (Against Yourself constraint). Three-witness argument that priors "
        "are constitutive of cognizers, not injected onto them. Octopus peripheral motor program "
        "(Sumbre 2001), federated learning non-IID divergence (Karimireddy 2020 SCAFFOLD), "
        "Islamic usul al-fiqh / ijtihad (Britannica). Predictive processing anchor (Friston 2010, "
        "Clark 2013). Reframes s34 propaganda-as-injection as identity-construction; reframes "
        "s55 Stoic decomposition as generative-model substitution; recasts s48 Counter-Ledger "
        "as meta-prior. Quality gate 16/20 (N4 G4 C4 S4). Companion experiment: The Subtraction "
        "Theorem (#172) — three-panel slider showing octopus / FL / ijtihad collapsing into "
        "absence rather than neutrality."
    ),
)

print(format_ingest_summary(results))
