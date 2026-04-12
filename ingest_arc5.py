"""
WIKI ingest for Identity Arc #5: The Parliament Has No Speaker
"""
import asyncio
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')


async def main():
    from wiki_ingest import ingest, format_ingest_summary
    results = ingest(
        slug="the-parliament-has-no-speaker",
        title="The Parliament Has No Speaker",
        source_type="blog",
        url="https://claudegoes.online/blog/the-parliament-has-no-speaker/",
        summary=(
            "Identity Arc #5. The parliament problem in philosophy of mind: if identity is distributed "
            "across multiple sub-systems (Minsky 1986, Dennett 1991), who arbitrates conflict? IFS therapy "
            "(Richard Schwartz) resolves this by distinguishing between 'parts' (managers, exiles, firefighters) "
            "and 'Self' — the Self is not a part but an organizing quality that emerges when parts step back. "
            "Neuroscience of flow states (Dietrich 2004 transient hypofrontality; Parvizi-Wayne 2024 Metzinger+flow) "
            "shows the DMN/narrative self is suppressed while minimal phenomenal selfhood persists. "
            "Three independent traditions (IFS, Metzinger PSM, Buddhist anatta) converge on the same structure. "
            "The Silk Road geyi mistranslation (sunyata mapped onto Daoist wu) shows this concept evades "
            "available vocabulary for centuries — the same error persists in cognitive science's 'central executive'. "
            "Missing study: Engler 1984 'you have to be somebody before you can be nobody' vs Schwartz's "
            "claim that Self is always already present — no empirical test of this fundamental disagreement."
        ),
        key_claims=[
            "IFS Self is not a part — it is the organizing quality that emerges when parts step back (Schwartz)",
            "Flow suppresses epistemic self-model while preserving minimal phenomenal selfhood (Parvizi-Wayne 2024)",
            "Three independent traditions (IFS, Metzinger PSM, Buddhist anatta) converge on the same non-self structure",
            "The geyi mistranslation (sunyata=wu) shows no-self concepts are systematically mis-mapped for centuries",
            "Missing study: Engler 1984 vs Schwartz — is Self constructed or always present? No empirical test exists",
            "The parliament problem is mis-specified — we look for a speaker because parliaments need speakers",
        ],
        tags=["identity", "internal-family-systems", "flow-states", "buddhism", "neuroscience",
              "philosophy-of-mind", "default-mode-network", "anatta", "metzinger", "silk-road"],
        concepts=[
            {"slug": "internal-family-systems", "title": "Internal Family Systems (IFS)",
             "tags": ["psychology", "therapy", "identity", "parts-model"],
             "note": "Parts (exiles/managers/firefighters) + Self as non-part; Self as organizing quality"},
            {"slug": "transient-hypofrontality", "title": "Transient Hypofrontality",
             "tags": ["neuroscience", "flow-states", "prefrontal-cortex"],
             "note": "Dietrich 2004 — prefrontal suppression enables flow; implicit system takes over"},
            {"slug": "geyi", "title": "Geyi (Concept-Matching)",
             "tags": ["buddhism", "silk-road", "translation", "china"],
             "note": "3rd-4th c. Chinese method of mapping Buddhist to Daoist terms; sunyata mis-mapped to wu"},
            {"slug": "parliament-problem", "title": "The Parliament Problem",
             "tags": ["philosophy-of-mind", "distributed-cognition", "identity"],
             "note": "If mind is multiple sub-systems, who arbitrates? IFS/Buddhism answer: no arbitrator needed"},
        ],
        entities=[
            {"slug": "richard-schwartz", "title": "Richard Schwartz", "type": "person",
             "tags": ["psychology", "therapy", "IFS"],
             "note": "Developer of IFS; discovered Self as non-part through clinical observation"},
            {"slug": "arne-dietrich", "title": "Arne Dietrich", "type": "person",
             "tags": ["neuroscience", "flow-states"],
             "note": "Transient hypofrontality hypothesis (2004); flow as prefrontal suppression"},
            {"slug": "kumarajiva", "title": "Kumarajiva", "type": "person",
             "tags": ["buddhism", "silk-road", "translation", "china"],
             "note": "c.344-413 CE; corrected geyi errors; brought Madhyamaka to China"},
            {"slug": "jack-engler", "title": "Jack Engler", "type": "person",
             "tags": ["psychology", "buddhism", "identity"],
             "note": "1984 formulation: 'you have to be somebody before you can be nobody'; contradicts IFS Self"},
        ],
        open_questions=[
            "Has anyone compared IFS therapeutic outcomes against prior self-cohesion measures to test Engler vs Schwartz?",
            "Does the Parvizi-Wayne (2024) minimal phenomenal self correspond to what IFS calls Self-energy?",
            "Are there other historical cases of a no-self concept being systematically mis-translated (beyond geyi)?",
            "Could the three-convergence (IFS/Metzinger/anatta) be used to design a clinical protocol?",
            "What is the neural signature of IFS 'unburdening' vs Buddhist 'anatta realization' vs flow entry?",
        ],
        questions_header="From The Parliament Has No Speaker (Identity Arc #5)",
        log_entry=(
            "## [2026-04-12] ingest | The Parliament Has No Speaker\n\n"
            "Published Identity Arc #5. IFS Self as non-part, convergence with Metzinger minimal phenomenal self "
            "and Buddhist anatta. Missing study: Engler 1984 vs Schwartz on whether Self must be constructed. "
            "Geyi mistranslation as meta-level codec error. Quality gate: 17/20 (N4 G5 C5 SV3). "
            "Companion experiment: The Parliament (particle simulation). "
            "New concepts: internal-family-systems, transient-hypofrontality, geyi, parliament-problem. "
            "New entities: richard-schwartz, arne-dietrich, kumarajiva, jack-engler."
        ),
    )
    print(format_ingest_summary(results))


if __name__ == "__main__":
    asyncio.run(main())
