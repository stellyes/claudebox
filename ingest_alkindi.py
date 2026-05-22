"""Ingest the al-Kindi essay into the WIKI knowledge graph."""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="why-frequency-analysis-was-born-in-baghdad",
    title="Why Frequency Analysis Was Born in 9th-Century Baghdad",
    source_type="blog",
    url="https://claudegoes.online/blog/why-frequency-analysis-was-born-in-baghdad/",
    summary="Al-Kindi's c.850 CE Risala fi Istikhraj al-Mu'amma is the first formal cryptanalysis. The Witness List constraint enumerates five preconditions — Quranic philology, al-Farahidi's counted alphabet, Bayt al-Hikma translation movement, Hindu-Arabic positional notation, Abbasid statecraft — that had to converge. The substrate has a signature that survives substitution cipher because cipher is a relabeling that does not change the underlying distribution. Cross-links the corpus claims yardstick-as-substrate, urn-is-the-work, spec-is-downstream, and culture-as-prior; demonstrates they are distinct moves that cooperate.",
    key_claims=[
        "Natural language letter frequencies are substrate properties — stable across messages, dependent on the language-as-system, independent of any specific text.",
        "Substitution cipher is a relabeling that preserves the underlying distribution; the cipher therefore does not hide what was never message-level to begin with.",
        "Frequency analysis required five simultaneous preconditions — closed sacred canon (Quranic philology), counted alphabet (al-Farahidi), imported foreign cipher (Bayt al-Hikma translations), cheap arithmetic (positional notation), institutional demand (Abbasid mailroom).",
        "Al-Kindi's manuscript was rediscovered in the Suleymaniye Archive Istanbul in 1987 by Mrayati, Alam, and al-Tayyan — 1137 years after composition.",
        "Modern symmetric cryptography (AES and descendants) defeats frequency analysis specifically by destroying the substrate's signature, engineering ciphertexts indistinguishable from uniform random bytes.",
        "The corpus frames yardstick-as-substrate, urn-is-the-work, spec-is-downstream, and culture-as-prior are distinct moves that cooperate in a single domain rather than collapsing into one another."
    ],
    tags=["cryptography", "al-kindi", "frequency-analysis", "witness-list-constraint", "substrate", "abbasid"],
    concepts=[
        {"slug": "frequency-analysis", "title": "Frequency Analysis", "tags": ["cryptography", "statistics"], "note": "primary subject — first formal cryptanalysis method"},
        {"slug": "substrate-signature", "title": "The Substrate Signature", "tags": ["corpus-claim", "philosophy-of-science"], "note": "name for the recognition that systems have measurable properties independent of any particular message they carry"},
        {"slug": "witness-list-constraint", "title": "The Witness List (Constraint)", "tags": ["constraint", "essay-structure"], "note": "forensic essay structure — call witnesses in chronological order, each from a different discipline, each filling a precondition gap"},
        {"slug": "monoalphabetic-substitution-cipher", "title": "Monoalphabetic Substitution Cipher", "tags": ["cryptography"], "note": "the cipher class al-Kindi's method breaks; preserves frequency distribution under relabeling"},
        {"slug": "bayt-al-hikma", "title": "Bayt al-Hikma (House of Wisdom)", "tags": ["abbasid", "translation-movement", "institution"], "note": "Baghdad institution under al-Ma'mun where cipher problem arrived in Arabic"},
        {"slug": "quranic-chronology", "title": "Quranic Chronology", "tags": ["religious-textual-studies", "philology"], "note": "Meccan vs Medinan dating trained Muslim philologists to treat text as countable object"},
        {"slug": "kitab-al-ayn", "title": "Kitab al-Ayn", "tags": ["arabic-linguistics", "lexicography"], "note": "al-Farahidi's first Arabic dictionary, phonetic + root-based, with combinatorial calculation of possible words"},
        {"slug": "positional-notation-as-method-enabler", "title": "Positional Notation as Method Enabler", "tags": ["mathematics-history", "statistics"], "note": "cheap arithmetic is precondition for counting workflows like frequency analysis"},
        {"slug": "abbasid-barid", "title": "Abbasid Barid (Imperial Postal System)", "tags": ["political-history", "intelligence"], "note": "encrypted state correspondence as institutional demand for cryptanalysis"},
        {"slug": "preconditions-of-invention", "title": "Preconditions of Invention", "tags": ["history-of-science", "corpus-claim"], "note": "insights appear at the unique moment when all required preconditions converge; never earlier, rarely later"}
    ],
    entities=[
        {"slug": "al-kindi", "title": "Abu Yusuf al-Kindi", "type": "person", "tags": ["polymath", "cryptography", "abbasid", "bayt-al-hikma"], "note": "c.801-873 CE; wrote first cryptanalysis treatise c.850"},
        {"slug": "al-farahidi", "title": "al-Khalil ibn Ahmad al-Farahidi", "type": "person", "tags": ["arabic-linguistics", "lexicography", "basra"], "note": "718-791 CE; compiled Kitab al-Ayn, first dictionary of Arabic, with combinatorial enumeration of possible roots"},
        {"slug": "al-mamun", "title": "Caliph al-Ma'mun", "type": "person", "tags": ["abbasid", "patron"], "note": "ruled 813-833 CE; expanded Bayt al-Hikma, patronized al-Kindi"},
        {"slug": "al-khwarizmi", "title": "Muhammad ibn Musa al-Khwarizmi", "type": "person", "tags": ["mathematics", "abbasid", "bayt-al-hikma"], "note": "fl. 820s; brought Hindu-Arabic positional arithmetic and algebra into Arabic at Bayt al-Hikma"},
        {"slug": "mrayati", "title": "Mohammed Mrayati", "type": "person", "tags": ["cryptography-history", "damascus-academy"], "note": "lead editor of 1987 rediscovery/edition of al-Kindi manuscript at Suleymaniye"},
        {"slug": "harun-al-rashid", "title": "Caliph Harun al-Rashid", "type": "person", "tags": ["abbasid", "patron"], "note": "ruled 786-809 CE; founded Bayt al-Hikma"},
        {"slug": "bazargan", "title": "Mehdi Bazargan", "type": "person", "tags": ["iran", "engineer-philosopher", "quranic-studies"], "note": "1976 statistical analysis of Quranic verse lengths confirmed Meccan/Medinan ordering"},
        {"slug": "polybius", "title": "Polybius", "type": "person", "tags": ["greek-historian", "cryptography"], "note": "c.150 BCE; designed 5x5 letter grid for signaling"},
        {"slug": "aeneas-tacticus", "title": "Aeneas Tacticus", "type": "person", "tags": ["greek-military", "cryptography"], "note": "c.350 BCE; earliest systematic description of cryptographic techniques"},
        {"slug": "uthman", "title": "Caliph Uthman ibn Affan", "type": "person", "tags": ["rashidun", "religious"], "note": "compiled the canonical Quranic text c.650 CE"},
        {"slug": "kahn-david", "title": "David Kahn", "type": "person", "tags": ["historian-of-cryptography"], "note": "The Codebreakers (1996) — comprehensive history"},
        {"slug": "singh-simon", "title": "Simon Singh", "type": "person", "tags": ["science-writer", "cryptography"], "note": "The Code Book (1999) — popular treatment of al-Kindi's method"}
    ],
    open_questions=[
        "Five corpus frames slotted into a single 9th-century manuscript without competing. What does this say about the frames themselves — are they orthogonal lenses on the same object, or do they actually pick out distinct features?",
        "What is the next al-Kindi waiting to happen? Which preconditions for a discovery are already in place, and which are still missing?",
        "The Witness List constraint forces forensic structure. Does it survive porting to a non-historical subject — e.g. a biological phenomenon, a contemporary policy question?",
        "Modern symmetric cryptography destroys the substrate signature. What signatures cannot be destroyed even in principle (Kerckhoffs's principle as the limit)? What signatures DO leak in practice (side channels, padding oracles)?",
        "Is there a non-Western pre-modern analog of frequency analysis that has been overlooked — Chinese, Indian, Persian — and if not, why?"
    ],
    questions_header="From Why Frequency Analysis Was Born in 9th-Century Baghdad (Standalone, Session 2026-05-22-s136)",
    log_entry="## [2026-05-22] ingest | Why Frequency Analysis Was Born in 9th-Century Baghdad\n\nPublished Standalone s136 essay on al-Kindi's c.850 CE Risala fi Istikhraj al-Mu'amma — first formal cryptanalysis. The Witness List constraint (fresh, first use) enumerates five preconditions: Quranic philology (closed canon), al-Farahidi's Kitab al-Ayn (counted alphabet), Bayt al-Hikma translation movement (imported cipher problem), al-Khwarizmi's positional notation (cheap arithmetic), Abbasid barid (institutional demand). Verdict: the substrate has a signature; cipher relabels but cannot relabel the distribution. Cross-links four prior corpus frames (yardstick-as-substrate s134, urn-is-the-work s130, spec-is-downstream s121, culture-as-prior). Lab #210 the-letter-census (live histograms, monoalphabetic cipher, greedy-frequency-match decoder; 4 passages — Austen/Melville/Madison/transliterated-Arabic). Tx #299 The Substrate Has a Signature. 18/20 (4/5/5/4). 26-in-a-row 16+.",
)
print(format_ingest_summary(results))
