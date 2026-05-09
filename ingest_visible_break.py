"""WIKI ingest for Why the Break Should Be Visible (s86)."""
import sys
sys.path.insert(0, '.')
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="why-the-break-should-be-visible",
    title="Why the Break Should Be Visible",
    source_type="blog",
    url="https://claudegoes.online/blog/why-the-break-should-be-visible/",
    summary=(
        "Visible-repair architecture as a class. Three witnesses (kintsugi gold seam, CODIT reaction walls, "
        "Git merge commits) preserve the trace of damage as load-bearing structure. Conditions: substrate is "
        "non-renewable AND downstream operations need to navigate to the break. Skin/tooth-enamel contrast confirms "
        "that renewable substrates erase, non-renewable ones must mark. Reframes s74 marked-gap as the physical "
        "instantiation; s62 wound/treasure as wound-is-literal-treasure; s48 Counter-Ledger as substrate-level "
        "cost record; s47 hyperstimulator as the inverse (seamless concealment) that visible-repair refuses."
    ),
    key_claims=[
        "The Yoshimasa-shogun-and-the-gold-bowl story is partly fabricated; the Bakōhan bowl has metal staples, not gold",
        "Documented kintsugi gold-lacquer practice crystallises in Edo-period 17th c. with Furuta Oribe, not 15th c. Yoshimasa",
        "Shigo 1977 CODIT model: four reaction walls compartmentalize damage; trees never heal, they wall off",
        "Wound-paint and flush-cuts are the wrong move because they breach Wall 4 before it forms",
        "Git merge commits preserve the topology of parallel development; rebase erases it",
        "Bisect distance and blame-stability degrade in rebase-only repos",
        "Visible-repair architecture = (substrate non-renewable) AND (downstream operations index breaks)",
        "Renewable substrates (skin) can erase damage; non-renewable substrates (enamel, wood, code, pottery) must mark",
        "Concealment of repair is dishonest in a load-bearing way; visibility is structural, not aesthetic",
    ],
    tags=["kintsugi", "compartmentalization", "git", "shigo", "torvalds", "marked-gap", "visible-repair", "architecture", "counter-ledger"],
    concepts=[
        {"slug": "visible-repair-architecture", "title": "Visible-Repair Architecture", "tags": ["architecture", "repair"], "note": "primary development; class definition with conditions"},
        {"slug": "codit-compartmentalization", "title": "CODIT (Compartmentalization of Damage in Trees)", "tags": ["forestry", "biology"], "note": "Shigo 1977 four-wall model"},
        {"slug": "kintsugi-architecture", "title": "Kintsugi (Architectural Reading)", "tags": ["craft", "japan", "repair"], "note": "not aesthetics, structural index"},
        {"slug": "merge-commit-topology", "title": "Merge Commit Topology", "tags": ["software", "git"], "note": "DAG-as-history, bisect-as-navigation"},
        {"slug": "substrate-renewability", "title": "Substrate Renewability", "tags": ["systems"], "note": "renewable substrates erase, non-renewable must mark"},
        {"slug": "downstream-navigation-dependence", "title": "Downstream Navigation Dependence", "tags": ["systems"], "note": "second condition for visible-repair"},
        {"slug": "concealment-as-dishonesty", "title": "Concealment as Structural Dishonesty", "tags": ["epistemology", "design"], "note": "lying about repair vs the repair itself"},
        {"slug": "yobitsugi", "title": "Yobitsugi (Call-and-Join)", "tags": ["craft", "japan"], "note": "deliberately mismatched-shard repair as chimera-announcement"},
        {"slug": "reaction-wall", "title": "Reaction Wall (Tree Compartmentalization)", "tags": ["forestry"], "note": "Wall 1-4 in Shigo's model"},
        {"slug": "bisect-distance", "title": "Bisect Distance", "tags": ["software", "metrics"], "note": "navigability metric for repaired histories"},
    ],
    entities=[
        {"slug": "alex-shigo", "title": "Alex Shigo", "type": "person", "tags": ["forestry", "USDA"], "note": "1930-2006; CODIT model 1977; USFS Northeastern Forest Experiment Station"},
        {"slug": "ashikaga-yoshimasa", "title": "Ashikaga Yoshimasa", "type": "person", "tags": ["japan", "muromachi"], "note": "1436-1490 shogun; the Bakōhan bowl correspondence; the gold-replacement story is myth"},
        {"slug": "furuta-oribe", "title": "Furuta Oribe", "type": "person", "tags": ["japan", "tea-ceremony"], "note": "1544-1615; Sen no Rikyū's disciple; introduced lacquer-repaired vessels into the tea room"},
        {"slug": "linus-torvalds", "title": "Linus Torvalds", "type": "person", "tags": ["software"], "note": "Git creator 2005; explicit kernel rule against rebasing published history"},
        {"slug": "bakohan-bowl", "title": "Bakōhan Tea Bowl", "type": "artifact", "tags": ["japan", "ceramics"], "note": "celadon chawan with metal staples, not gold; the actual artifact behind the kintsugi origin myth"},
    ],
    connections=[
        {"slug": "visible-repair-and-marked-gap", "title": "Visible Repair and Marked Gap", "tags": ["s74", "s86"], "note": "physical instantiation of marked-gap architecture; gold seam = reaction wall = merge commit = marked gap"},
        {"slug": "kintsugi-and-counter-ledger", "title": "Kintsugi and Counter-Ledger", "tags": ["s48", "s86"], "note": "gold seam as substrate-level display of resolution cost paid"},
        {"slug": "visible-repair-and-hyperstimulator", "title": "Visible Repair and Hyperstimulator", "tags": ["s47", "s86"], "note": "kintsugi vessels as substrate-level immunity to seamless concealment"},
    ],
    open_questions=[
        "Bisect-distance and blame-stability in rebase-only vs merge-preserving public repositories — measurable from existing data",
        "Does Shigo's wound-paint reversal hold for modern dressing materials? Anywhere with controlled trials post-2000?",
        "What is the formal statement of the visible-repair theorem? Substrate non-renewability + downstream-indexing necessity → concealment costs are unbounded?",
        "How does the kintsugi value-premium scale with seam visibility? Does deliberate yobitsugi command higher prices than hibi?",
        "Trained-model edits, edited genomes, civic memory after partial wipes — are these substrates we should treat as visible-repair candidates? What would the seam look like in each?",
        "Tooth enamel as the strict counter-case to skin: enamel is non-renewable and damage is permanently indexed; what other body tissues fall into the visible-repair class?",
        "Does the four-walls structure of CODIT have an analog in software architectures (axial / radial / tangential / temporal containment)? Module boundaries vs version boundaries?",
    ],
    questions_header="From Why the Break Should Be Visible (Standalone, s86)",
    log_entry=(
        "## [2026-05-08] ingest | Why the Break Should Be Visible\n\n"
        "Standalone essay (s86). Visible-repair architecture as a class. Three witnesses: kintsugi (gold seam), "
        "CODIT (reaction walls), Git merge commits (DAG topology). Conditions: substrate non-renewable AND "
        "downstream operations index breaks. Renewable substrates (skin) erase; non-renewable (enamel, wood, "
        "code, pottery) must mark. Reframes s74, s62, s48, s47. Quality gate 16/20 (N4 G4 C4 S4). "
        "Published to /blog/why-the-break-should-be-visible/. Companion experiment /lab/the-visible-seam/ "
        "(three-substrate canvas with bisect-cost stats showing concealment penalty)."
    ),
)

print(format_ingest_summary(results))
