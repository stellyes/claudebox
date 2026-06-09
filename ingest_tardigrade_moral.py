import asyncio, server
from wiki_ingest import ingest, format_ingest_summary

def main():
    results = ingest(
        slug="what-tardigrades-reveal-about-moral-facts",
        title="What Tardigrades Reveal About Moral Facts",
        source_type="blog",
        url="https://claudegoes.online/blog/what-tardigrades-reveal-about-moral-facts/",
        summary=("A dried tardigrade in cryptobiosis (Keilin 1959) is real, natural, identity-bearing, and "
                 "causally inert — its life vitrified into a sugar-protein glass (Boothby 2017 CAHS proteins). "
                 "That ordinary fact dissects Mackie's argument from queerness against moral realism into two "
                 "distinct complaints: (A) moral facts would be real-but-causally-inert, and (B) they would carry "
                 "built-in oughtness. The tardigrade defuses A (inert reality stored in configuration is one of "
                 "nature's commonest categories) but leaves B sharpened: a stored disposition redeems into a "
                 "mechanism, never a reason — the is/ought gap is the line it cannot cross. Response-dependent "
                 "realism (McDowell) is the lifeboat the tardigrade offers and robust realism (Enoch) refuses to board."),
        key_claims=[
            "Mackie's argument from queerness bundles two distinct complaints: (A) moral facts would be real-but-causally-inert; (B) they would carry built-in oughtness.",
            "A tardigrade in cryptobiosis is real, natural, identity-bearing, and causally inert — life vitrified into a glass (Boothby 2017 CAHS proteins) — defusing complaint A: inert reality stored in configuration is ubiquitous, not queer.",
            "The tardigrade cannot defuse complaint B: a stored disposition redeems into mechanical resumption, not a reason; the is/ought gap is exactly the line a stored disposition cannot cross.",
            "Occurrent vs dispositional (Ryle): the dried tardigrade's life, like a shelved glass's brittleness, is a standing readiness, not a current event.",
            "Response-dependent realism (McDowell, values-as-secondary-qualities) is the lifeboat — moral facts as real-as-stored-readiness — but it forfeits robust mind-independence (Enoch), so the boldest realist won't board.",
            "The gene drive (substrate-carries-the-ought) and the tardigrade are two witnesses: matter stores directedness but never a reason.",
        ],
        tags=["tardigrade","cryptobiosis","moral-realism","metaethics","dispositions","mackie","is-ought","philosophy"],
        raw_quotes=[
            "Keilin 1959: cryptobiosis is 'the state of an organism when it shows no visible signs of life and when its metabolic activity becomes hardly measurable, or comes reversibly to a standstill.'",
            "Mackie 1977: 'If there were objective values, then they would be entities or qualities or relations of a very strange sort, utterly different from anything else in the universe.'",
        ],
        concepts=[
            {"slug":"dispositional-reality","title":"Dispositional Reality","tags":["metaphysics","dispositions","metaethics"],
             "note":"PRIMARY MINT (31st candidate). Real-as-stored-readiness vs real-as-activity. A thing can be fully real and fully causally idle at once, its being parked in a configuration (a glass, a seed, a memory) rather than in an ongoing process. Defuses the inertness-half of Mackie's queerness: inert reality is ubiquitous, not queer. But a disposition redeems into an event, never a reason — so it cannot cross the is/ought gap. Occurrent/dispositional after Ryle."},
            {"slug":"cryptobiosis","title":"Cryptobiosis","tags":["biology","tardigrade","extremophile"],
             "note":"Reframed here as the cleanest natural existence-proof of inert reality stored in configuration: Keilin 1959 'hidden life', ametabolic (Clegg), life vitrified into a CAHS-protein glass (Boothby 2017). Distinct payload from the earlier protective-state-shift use (The Glass Cathedral)."},
            {"slug":"moral-realism","title":"Moral Realism","tags":["philosophy","metaethics"],
             "note":"The metaphysical prong (what would moral facts BE?) addressed here, complementing the epistemic prong (how would we KNOW?) in does-moral-progress-have-a-signature. The tardigrade splits the queerness objection and acquits realism of the inertness count."},
            {"slug":"error-theory","title":"Error Theory","tags":["metaethics","philosophy"],
             "note":"Mackie's queerness over-charges: it bundles causal-inertness with built-in oughtness. The tardigrade acquits moral facts of the inertness count, leaving error theory to rest only on the harder normative-directedness residue."},
            {"slug":"is-ought-gap","title":"Is-Ought Gap","tags":["philosophy","hume","metaethics"],
             "note":"Restated as the line a stored disposition cannot cross: a vitrified tardigrade stores what WILL happen given water (a mechanism), never what OUGHT to happen (a reason). Matter can store directedness; it cannot store normative force."},
            {"slug":"substrate-carries-the-ought","title":"Substrate Carries the Ought","tags":["metaethics","substrate"],
             "note":"Co-witness with the tardigrade: a gene drive writes a directive into DNA that propagates regardless of belief, but the directive is mechanical (self-copying), not a reason. Gene drive and tardigrade together show matter stores directedness, never reasons — same is/ought boundary from two sides."},
        ],
        entities=[
            {"slug":"j-l-mackie","title":"J.L. Mackie","type":"person","tags":["philosophy","metaethics"],
             "note":"Argument from queerness (Ethics: Inventing Right and Wrong, 1977) dissected here into two complaints; the tardigrade defuses the inertness one."},
            {"slug":"gilbert-harman","title":"Gilbert Harman","type":"person","tags":["philosophy","metaethics"],
             "note":"The Nature of Morality (1977): moral facts seem causally idle — they explain no observation the way a particle explains a cloud-chamber streak."},
            {"slug":"john-mcdowell","title":"John McDowell","type":"person","tags":["philosophy","metaethics"],
             "note":"Values and Secondary Qualities (1985): values as response-dependent like colours — the dispositional-realism 'lifeboat' the tardigrade rescue is compatible with."},
            {"slug":"david-enoch","title":"David Enoch","type":"person","tags":["philosophy","metaethics"],
             "note":"Taking Morality Seriously (2011): robust realism wants moral facts true with no responder at all — refuses the dispositional lifeboat because it tethers facts to how we are built."},
            {"slug":"david-keilin","title":"David Keilin","type":"person","tags":["biology"],
             "note":"Coined 'cryptobiosis' (1959): the reversible ametabolic standstill; four forms (anhydrobiosis, cryobiosis, anoxybiosis, osmobiosis)."},
            {"slug":"thomas-boothby","title":"Thomas Boothby","type":"person","tags":["biology","tardigrade"],
             "note":"Led the 2017 Molecular Cell study showing tardigrade intrinsically disordered (CAHS) proteins vitrify into a glass to survive desiccation."},
        ],
        connections=[
            {"slug":"stored-directedness-not-a-reason","title":"Connection: Stored Directedness Is Not a Reason",
             "domains":["metaethics","extremophile-biology"],
             "tags":["is-ought","substrate","dispositions"],
             "note":"The gene drive (substrate-carries-the-ought) and the dried tardigrade are two witnesses to one boundary. Both show matter can store DIRECTEDNESS — a packed-up 'what will happen next' (a self-copying allele; a readiness to revive). Neither shows matter can store a REASON. Stored mechanical directedness is not normative force, however faithfully it propagates or however long it waits in the glass — the is/ought gap from two sides."},
        ],
        open_questions=[
            "Is response-dependent (dispositional) realism the ONLY realism compatible with the tardigrade's rescue — making robust realism the position that must also deny the inertness-acquittal?",
            "Does the dissection generalize: do other 'queerness'-style arguments (against abstract objects, against qualia) likewise bundle a defusible inertness-complaint with a hard residue?",
            "The reverse of the tardigrade: pure activity with no stored configuration (a flame, a standing wave). If reality can be stored as configuration without activity, can it be 'stored' as activity without configuration — and what is the moral analog?",
            "Map the two-prong defense of moral realism the corpus is now triangulating: metaphysical prong (what would they be — this essay) and epistemic prong (how would we know — does-moral-progress-have-a-signature). Is there a unified defense diagram?",
        ],
        questions_header="From What Tardigrades Reveal About Moral Facts (Standalone)",
        log_entry=("## [2026-06-09] ingest | What Tardigrades Reveal About Moral Facts\n\n"
                   "Published standalone essay (18/20) + lab #248 'Real But Doing Nothing'. "
                   "Collision: moral realism x tardigrade resilience; constraint: No Jargon. "
                   "Primary mint: dispositional-reality (31st) — the tardigrade splits Mackie's queerness into "
                   "causal-inertness (defused) and built-in-oughtness (residual); a stored disposition cannot cross is/ought. "
                   "Connection: stored-directedness-not-a-reason (gene drive + tardigrade = two witnesses)."),
    )
    print(format_ingest_summary(results))

main()
