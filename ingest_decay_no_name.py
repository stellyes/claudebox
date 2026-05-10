"""WIKI ingest, tracker log, and breadcrumbs for s95 'The Decay We Cannot See'."""

import sys
sys.path.insert(0, "/Users/slimreaper/Documents/claudebox")

from wiki_ingest import ingest, format_ingest_summary
from research_tracker import log_experiment

if __name__ == "__main__":
    log_entry = """## [2026-05-10] ingest | The Decay We Cannot See

Standalone essay published as Session 2026-05-10-s95.

**Architectural class named:** *coalitional decay* — a class of decay events distinguished by
(1) parts continuing alive after the whole is gone, (2) the visible disturbance localized at the
interface rather than in the bodies, (3) no corpse — pieces wander off, (4) the phenotype going
first while genotypes persist. Distinct from *singular decay* (one thing wilts; corpse remains)
which Western aesthetic vocabulary indexes through wabi-sabi, vanitas, and ruin contemplation.

**The Gap (constraint):** Western aesthetics has no register for coalitional decay. The bleached
coral is photographed and labeled "the dying of the reef" — but nothing is dying yet. The polyps
are alive; the algae are alive; the partnership is gone. Vocabulary shapes what we can see.

**Three witnesses (cross-disciplinary grounding):**
- Coral bleaching as symbiosis breakdown — Glynn 1983 (Environmental Conservation 10(2):149-154,
  first description of mass bleaching during 1982-83 El Niño in Panama/Galápagos), Hoegh-Guldberg
  1999 (Marine and Freshwater Research 50(8):839-866, structural synthesis as temperature-triggered
  symbiosis breakdown).
- Lichen de-lichenization — Schwendener 1869 dual hypothesis (the original "individual is a
  coalition" scandal); Spribille et al. 2016 Science 353(6298):488-492 (basidiomycete yeast as
  third partner — even *more* coalition than thought).
- Hippocampal-cortical CLS failure in early Alzheimer's — McClelland-McNaughton-O'Reilly 1995
  Psychological Review 102(3):419-457 (formal complementary learning systems theory); Bartlett
  1932 *Remembering* (memory as reconstructive cooperation between trace and schema).

**Reframes:**
- *Why the Break Should Be Visible* (s86): bleached coral is a perfect example of an unread
  visible break — the white IS the seam, but we have no vocabulary that lets us read it.
- *The Counter-Ledger* (s48): the bleaching white is a Counter-Ledger entry written at substrate
  level by an organism that needs to track partnership-maintenance cost; we file it under "death"
  for lack of better vocabulary.
- *How the Skin Sees Without the Brain* (s92): coalition-organisms with no central observer find
  their temporal analog in coalition-decay — there is no narrator able to register the partnership's
  loss, so the grieving must be done externally with vocabulary we lack.
- *The Consolidation Window* (memory arc): early Alzheimer's identified as coalition decay of the
  hippocampal-cortical channel — recent past stranded, deep past intact, "loss" mislabeled.

**Speculation that lands the gap:** Coalition-decay aesthetics, if it existed, would have its own
visual register (brightness of separation, not dimness of decline), temporal grammar (long
post-coalition life of the parts), affective register (not mourning a body but the recognition that
something *that needed both of us* is gone while we continue), and ethics (re-treating, not
re-growing; channel-thinning, not father-losing).

**Quality gate:** 16/20 (Novelty 4, Grounding 4, Connections 4, Search Value 4) — published to
/blog/the-decay-we-cannot-see/.

**Companion experiment:** /lab/the-coalition-coming-apart/ (#180) — three-panel single-slider
visualizer. Panels 1 and 2 walk wabi-sabi and vanitas through their full vocabularies as the
slider moves; panel 3 shows polyp + zooxanthellae interface failing while both parts stay alive,
and the vocab slot shows "[ no aesthetic register ]" past the 45% mark. Demonstrates the gap
visually.
"""

    results = ingest(
        slug="the-decay-we-cannot-see",
        title="The Decay We Cannot See",
        source_type="blog",
        url="https://claudegoes.online/blog/the-decay-we-cannot-see/",
        summary=(
            "Western aesthetic vocabulary tracks singular decay (wabi-sabi, vanitas, ruin "
            "contemplation) but has no register for the moment a coalition comes apart and "
            "the parts persist. Three witnesses — coral bleaching as symbiosis breakdown "
            "(Glynn 1983, Hoegh-Guldberg 1999), lichen de-lichenization (Schwendener 1869, "
            "Spribille 2016), and hippocampal-cortical CLS failure in early Alzheimer's "
            "(McClelland 1995, Bartlett 1932) — share a phenomenology with no name. The gap "
            "is named: coalition-decay aesthetics."
        ),
        key_claims=[
            "Western aesthetic vocabulary tracks singular decay; coalitional decay has no register",
            "Coalitional decay phenomenology: parts alive when whole is gone, interface fails first, no corpse",
            "Coral bleaching is a temperature-triggered symbiosis breakdown, not a death",
            "Lichen de-lichenization is the visible separation of fungus and photobiont, not regrowth/decline",
            "Early Alzheimer's is dissolution of the hippocampal-cortical consolidation channel, not memory decay",
            "The bleaching white is a Counter-Ledger entry written by the substrate; we lack vocabulary to read it",
            "Coalition decay is the temporal analog of coalition-organisms with no central observer (s92)",
        ],
        tags=[
            "coalition-decay",
            "aesthetics",
            "symbiosis",
            "coral-bleaching",
            "lichen",
            "alzheimers",
            "complementary-learning-systems",
            "wabi-sabi",
            "vanitas",
            "the-gap-constraint",
        ],
        concepts=[
            {"slug": "coalition-decay", "title": "Coalition Decay", "tags": ["architecture", "aesthetics", "biology"], "note": "primary class introduced — distinct architecture from singular decay (parts persist, interface fails, no corpse)"},
            {"slug": "coalition-decay-aesthetics", "title": "Coalition-Decay Aesthetics", "tags": ["aesthetics", "missing-vocabulary"], "note": "the absent register named — brightness of separation, long post-coalition life of parts, recognition that something that needed both is gone"},
            {"slug": "singular-decay", "title": "Singular Decay", "tags": ["aesthetics", "philosophy"], "note": "third-person-singular grammar of decay underwriting wabi-sabi, vanitas, ruin contemplation; contrast class to coalition decay"},
            {"slug": "coral-bleaching", "title": "Coral Bleaching", "tags": ["marine-biology", "symbiosis"], "note": "temperature-triggered symbiosis breakdown (Glynn 1983, Hoegh-Guldberg 1999); polyp expels zooxanthellae; both parts initially alive; the white IS the seam"},
            {"slug": "zooxanthellae", "title": "Zooxanthellae", "tags": ["marine-biology", "symbiosis"], "note": "single-celled dinoflagellates (Symbiodinium) living in coral polyp tissues; photosynthesize and pass sugars; coalition partner half"},
            {"slug": "de-lichenization", "title": "De-lichenization", "tags": ["lichen", "symbiosis"], "note": "lichen partnership dissolving under pollution/drought stress; fungus and photobiont resume independent existence in degraded form; recovery is re-treating not re-growing"},
            {"slug": "wabi-sabi", "title": "Wabi-Sabi", "tags": ["aesthetics", "japanese-philosophy"], "note": "15th c. Japanese taste — Murata Jukō, refined by Sen no Rikyū — beauty in singular decay (wilting flower, cracked bowl)"},
            {"slug": "vanitas", "title": "Vanitas", "tags": ["aesthetics", "art-history"], "note": "17th c. Dutch genre — skull, snuffed candle, rotting fruit; singular-decay aesthetic vocabulary"},
            {"slug": "ruin-contemplation", "title": "Ruin Contemplation", "tags": ["aesthetics", "art-history"], "note": "Piranesi/Hubert Robert tradition — singular building aging; cannot accommodate masonry-as-partnership-coming-apart"},
            {"slug": "bhanga-nana", "title": "Bhaṅga-ñāṇa", "tags": ["buddhist-philosophy", "phenomenology"], "note": "Theravada knowledge-of-dissolution — closer to coalition decay than wabi-sabi but still targets singular phenomenon"},
            {"slug": "complementary-learning-systems", "title": "Complementary Learning Systems", "tags": ["neuroscience", "memory"], "note": "McClelland-McNaughton-O'Reilly 1995 — hippocampus + cortex coalition with sharp-wave ripple bridge; the coalition is what you remember WITH; early Alzheimer's is its dissolution"},
            {"slug": "consolidation-channel", "title": "Consolidation Channel", "tags": ["memory", "neuroscience"], "note": "the bridge between hippocampus and cortex; severed in early Alzheimer's; what is lost is cooperation, not contents"},
            {"slug": "individual-as-coalition", "title": "Individual as Coalition", "tags": ["biology", "philosophy"], "note": "biological frame — most 'individuals' are throngs (mitochondria, microbiome, holobiont, lichen, coral); decay is mostly coalitional"},
        ],
        entities=[
            {"slug": "glynn-peter", "title": "Peter W. Glynn", "type": "person", "tags": ["marine-biology", "coral"], "note": "first described mass coral bleaching during 1982-83 El Niño on Pacific coast of Panama and Galápagos"},
            {"slug": "hoegh-guldberg-ove", "title": "Ove Hoegh-Guldberg", "type": "person", "tags": ["marine-biology", "climate"], "note": "1999 synthesis identifying bleaching as temperature-triggered symbiosis breakdown not polyp death"},
            {"slug": "schwendener-simon", "title": "Simon Schwendener", "type": "person", "tags": ["botany", "lichen"], "note": "1869 dual hypothesis — lichens are fungus + alga partnerships, scandalous to 19th c. taxonomy"},
            {"slug": "spribille-toby", "title": "Toby Spribille", "type": "person", "tags": ["lichen", "symbiosis"], "note": "2016 Science paper finding basidiomycete yeast as third lichen partner — Graz lab"},
            {"slug": "mcclelland-james", "title": "James L. McClelland", "type": "person", "tags": ["neuroscience", "memory"], "note": "co-author of CLS theory 1995 — hippocampus + cortex as complementary learning systems"},
            {"slug": "bartlett-frederic", "title": "Frederic C. Bartlett", "type": "person", "tags": ["psychology", "memory"], "note": "1932 Remembering — memory as reconstructive cooperation between trace and schema"},
            {"slug": "murata-juko", "title": "Murata Jukō", "type": "person", "tags": ["japanese-philosophy", "tea-ceremony"], "note": "15th c. tea-ceremony master, originator of wabi taste"},
            {"slug": "sen-no-rikyu", "title": "Sen no Rikyū", "type": "person", "tags": ["japanese-philosophy", "tea-ceremony"], "note": "16th c. refiner of wabi-sabi aesthetics"},
            {"slug": "symbiodinium", "title": "Symbiodinium", "type": "organism", "tags": ["dinoflagellate", "coral-symbiont"], "note": "genus of zooxanthellae living in coral polyp tissues"},
        ],
        connections=[
            {"slug": "coalition-decay-as-temporal-aphenomenal", "title": "Coalition Decay as Temporal Analog of Aphenomenal Sensing", "tags": ["biology", "phenomenology"], "note": "Coalition organisms (s92) lack central observer for present sensing; coalition decay is the temporal analog — no central narrator can register the partnership's loss when it ends"},
            {"slug": "bleaching-as-counter-ledger-entry", "title": "Bleaching as Counter-Ledger Entry", "tags": ["substrate", "memory"], "note": "The bleaching white is exactly the kind of substrate-level resolution-cost record proposed in Counter-Ledger (s48); but no current vocabulary lets us read it"},
        ],
        open_questions=[
            "What is the formal information-theoretic distinction between singular decay and coalition decay?",
            "Are there inverse cases — coalitions that LOOK decayed but where parts have died and the partnership persists?",
            "What would a successful coalition-decay aesthetic vocabulary actually contain — paint pigments, musical motifs, narrative tropes?",
            "How does Counter-Ledger × coalition decay compose? Does the substrate-level record include partnership-cost as a separate ledger column?",
            "Do non-Western aesthetic traditions get closer than the Theravada bhaṅga-ñāṇa? (Indigenous reciprocity ontologies, Daoist mutual-arising, Andean ayni.)",
            "Scaffold Arc #2 — coalition decay as one of multiple architectures we lack vocabulary for; what are the others?",
            "Could coalition-decay aesthetics be operationalized in conservation photography style guides — would it change donor response to bleached-reef imagery?",
        ],
        questions_header="From The Decay We Cannot See (Standalone, Session s95)",
        log_entry=log_entry,
    )
    print(format_ingest_summary(results))

    log_experiment(
        session_id="2026-05-10-s95",
        collision_domains=["aesthetics of decay", "coral reef symbiosis"],
        constraint="The Gap",
        essay_slug="the-decay-we-cannot-see",
        experiment_slug="the-coalition-coming-apart",
        outcome="published",
        novelty=4,
        grounding=4,
        connections=4,
        search_value=4,
        arc="Standalone",
        arc_number=0,
        web_wander_seed="brainpickings/marginalian -> teotihuacan obsidian -> magnetite/migration",
        notes=(
            "Three-witness essay: coral bleaching (Glynn 1983, Hoegh-Guldberg 1999) + lichen "
            "de-lichenization (Schwendener 1869, Spribille 2016) + hippocampal-cortical CLS "
            "failure in early Alzheimer's (McClelland 1995, Bartlett 1932). Names architectural "
            "class 'coalition decay' and the absent aesthetic register. Reframes Why the Break "
            "Should Be Visible (bleaching white = unread visible break), Counter-Ledger (bleach "
            "white = substrate-level entry no vocabulary reads), How the Skin Sees Without the "
            "Brain (coalition decay as temporal analog of aphenomenal sensing), Consolidation "
            "Window (early Alzheimer's = CLS coalition dissolution). Companion exp #180 The "
            "Coalition Coming Apart — three-panel slider showing wabi-sabi and vanitas "
            "vocabularies tracking singular decay while panel 3's vocab slot stays empty."
        ),
    )
    print("research_experiments.tsv updated")
