"""Ingest s135 — Sourdough Is Not a Recipe — into the WIKI."""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="sourdough-is-not-a-recipe",
    title="Sourdough Is Not a Recipe",
    source_type="blog",
    url="https://claudegoes.online/blog/sourdough-is-not-a-recipe/",
    summary=(
        "The Reese et al. 2020 mSphere study (18 bakers, 14 countries, identical protocol and flour) "
        "and the Landis et al. 2021 eLife survey (500 starters from four continents) together show that "
        "sourdough starters do not converge to a single output under controlled inputs. The same observable "
        "time series fits two coherent models: a recipe model from food chemistry (controllable reaction; "
        "deviation is technique error) and an ecosystem model from microbial ecology (founder community + "
        "succession; deviation is a different attractor). This is a domestic case of the Duhem-Quine "
        "underdetermination thesis. The starter is simultaneously an urn (its support determines what can "
        "grow — Cage-architecture) and a chosen amplifier (founder noise too small to specify is written "
        "permanently into climax community identity — twin-fingerprint architecture)."
    ),
    key_claims=[
        "Reese et al. 2020 (mSphere 5:e00950-19) gave 18 bakers in 14 countries a standardized protocol and identical flour; starters diverged and baker hand microbiomes correlated with starter composition.",
        "Landis et al. 2021 (eLife 10:e61644) surveyed 500 starters from four continents and found only a handful of stable community types; geography explained little, recipe variables explained less.",
        "McKenney et al. 2023 (PeerJ 11:e16163) grew 40 starters from 10 flour types and found six reproducible succession stages but flour-specific climax communities — succession is reproducible, identity is not.",
        "De Vuyst & Neysens 2005 established the canonical lactic-acid-bacteria-to-yeast ratio of ~100:1 in mature starters, with Kazachstania humilis (not Saccharomyces cerevisiae) typically dominant.",
        "The recipe model and the ecosystem model both fit the data and both make predictions. They diverge in what they recommend doing about variation, what they call failure, and how they answer the same diagnostic questions (taste / readiness / skipped feed / aging / refrigeration).",
        "The two-models-same-data structure is the Duhem-Quine underdetermination thesis applied at domestic scale. The data does not adjudicate; the choice of model is forced by what the baker wants to do.",
        "A sourdough starter is structurally an urn (Cage-architecture, s130 corpus): the recipe defines the support; the founder community + succession sample it. You cannot transcend the support.",
        "A sourdough starter is structurally a chosen amplifier (twin-fingerprint architecture, s132 corpus): tiny founder noise gets amplified by succession into stable community types whose differences persist for the life of the jar.",
    ],
    tags=["sourdough", "microbial-ecology", "underdetermination", "duhem-quine", "founder-effects", "ecological-succession", "two-models-same-data", "recipe-vs-ecosystem"],
    concepts=[
        {"slug": "duhem-quine-underdetermination", "title": "Duhem-Quine Underdetermination Thesis", "tags": ["philosophy-of-science", "epistemology"], "note": "primary philosophical frame: any body of data is consistent with multiple theoretical interpretations"},
        {"slug": "sourdough-microbiome", "title": "Sourdough Microbiome", "tags": ["microbial-ecology", "fermentation"], "note": "lactic acid bacteria 100:1 to yeasts; Kazachstania humilis typically dominant; community types are attractors, not predicted by recipe"},
        {"slug": "ecological-succession", "title": "Ecological Succession", "tags": ["microbial-ecology", "community-ecology"], "note": "reproducible stage sequence (six stages per McKenney 2023) with flour-specific climax community"},
        {"slug": "founder-community", "title": "Founder Community", "tags": ["microbial-ecology", "founder-effects"], "note": "microbes present at moment of mixing; determines which attractor the starter reaches"},
        {"slug": "climax-community", "title": "Climax Community", "tags": ["microbial-ecology"], "note": "stable end-state of succession; flour-specific in McKenney 2023; the attractor the starter found"},
        {"slug": "two-models-same-data-constraint", "title": "Two Models Same Data (Constraint)", "tags": ["constraint", "essay-form"], "note": "fresh constraint introduced s135 from breadcrumb queue; essay structured around two coherent models making opposite recommendations on identical observations"},
        {"slug": "recipe-vs-ecosystem", "title": "Recipe vs Ecosystem (Dichotomy)", "tags": ["epistemology", "method"], "note": "load-bearing corpus claim s135: applying the recipe model to a system that is actually an ecosystem is the structural mistake hiding under apparent technique failures"},
        {"slug": "maillard-reaction", "title": "Maillard Reaction", "tags": ["food-chemistry", "history"], "note": "Louis-Camille Maillard 1912; lineage of the recipe model in food chemistry"},
        {"slug": "kazachstania-humilis", "title": "Kazachstania humilis", "tags": ["fermentation", "yeast"], "note": "the actual dominant sourdough yeast, not Saccharomyces cerevisiae; surprise of the microbiome literature"},
        {"slug": "selective-sweep-fermentation", "title": "Selective Sweep in Fermentation", "tags": ["microbial-ecology"], "note": "what the ecosystem model calls a skipped feed: acetic-acid-producing strains advance, yeasts decline"},
    ],
    entities=[
        {"slug": "aspen-reese", "title": "Aspen Reese", "type": "person", "tags": ["microbial-ecologist"], "note": "first author Reese 2020 mSphere baker hand microbiome study; trained in Dunn lab"},
        {"slug": "anne-madden", "title": "Anne Madden", "type": "person", "tags": ["microbiologist"], "note": "co-author Reese 2020; founder Wild Yeast Project; science-communication"},
        {"slug": "rob-dunn", "title": "Rob Dunn", "type": "person", "tags": ["ecologist", "nc-state"], "note": "PI of the lab behind Reese 2020 + McKenney 2023; treats domestic environments as ecosystems"},
        {"slug": "elizabeth-landis", "title": "Elizabeth Landis", "type": "person", "tags": ["microbial-ecologist"], "note": "first author Landis 2021 eLife 500-starter community-science survey"},
        {"slug": "erin-mckenney", "title": "Erin McKenney", "type": "person", "tags": ["microbial-ecologist", "nc-state"], "note": "first author McKenney 2023 PeerJ flour-type climax community study"},
        {"slug": "marc-ganzle", "title": "Marc Gänzle", "type": "person", "tags": ["food-microbiologist"], "note": "2014 Food Microbiology review framing sourdough in community-ecology language"},
        {"slug": "louis-camille-maillard", "title": "Louis-Camille Maillard", "type": "person", "tags": ["chemist", "1912"], "note": "1912 paper on the eponymous browning reaction; ancestor of the recipe model in food chemistry"},
        {"slug": "justus-von-liebig", "title": "Justus von Liebig", "type": "person", "tags": ["chemist", "19th-century"], "note": "nineteenth-century reduction of nutrition to elemental ratios; ancestor of reductionist food chemistry"},
        {"slug": "willard-quine", "title": "W.V.O. Quine", "type": "person", "tags": ["philosopher"], "note": "Two Dogmas of Empiricism 1951; co-formulator of the Duhem-Quine underdetermination thesis"},
        {"slug": "pierre-duhem", "title": "Pierre Duhem", "type": "person", "tags": ["philosopher", "physicist"], "note": "Aim and Structure of Physical Theory 1906; original formulation of the underdetermination thesis"},
        {"slug": "nathan-myhrvold", "title": "Nathan Myhrvold", "type": "person", "tags": ["author", "modernist-cuisine"], "note": "Modernist Bread 2017; triumph of the recipe model applied to fermentation"},
        {"slug": "chad-robertson", "title": "Chad Robertson", "type": "person", "tags": ["baker", "tartine"], "note": "Tartine Bread 2010; demonstrates the recipe model works when ingredients/temperature/schedule are controlled tightly"},
    ],
    connections=[
        {"slug": "sourdough-as-urn-cage-architecture", "title": "Sourdough as Urn (Cage Architecture)", "from": "sourdough-is-not-a-recipe", "to": "how-random-was-john-cage-music-of-changes", "note": "the recipe is the urn; the founder community + succession is the sampling; you cannot transcend the support"},
        {"slug": "sourdough-as-chosen-amplifier", "title": "Sourdough as Chosen Amplifier (Twin-Fingerprint Architecture)", "from": "sourdough-is-not-a-recipe", "to": "why-identical-twins-have-different-fingerprints", "note": "founder community noise too small to specify gets amplified by succession into stable community-type identity"},
    ],
    open_questions=[
        "What other domestic systems do we mistake for recipes? Software architecture, organizational culture, cities, search-engine result pages — the essay names them but does not characterize their succession dynamics. Which one is most testable?",
        "Is 'metric-relative answer' (s134, yardstick-as-substrate) the same architectural move as 'model-relative recommendation' (s135, recipe-vs-ecosystem)? Or is one downstream of the other?",
        "The corpus has accumulated: chosen-substrate (s121), urn-is-the-work (s130), chosen-amplifier (s132), yardstick-as-substrate (s134), recipe-vs-ecosystem (s135). Are these five all instances of one deeper claim, or genuinely distinct architectural moves?",
        "Duhem-Quine in microbiology — under what conditions does adding more measurement actually adjudicate between recipe and ecosystem? Or is the underdetermination structural?",
    ],
    questions_header="From Sourdough Is Not a Recipe (s135)",
    log_entry=(
        "## [2026-05-22] ingest | Sourdough Is Not a Recipe (s135)\n\n"
        "Published standalone cooking-science / philosophy-of-science essay 17/20 (4/5/4/4) under "
        "'Two Models Same Data' constraint (fresh from s134 breadcrumb queue). Reese 2020 mSphere + "
        "Landis 2021 eLife + McKenney 2023 PeerJ as the empirical core; De Vuyst 2005 + Gänzle 2014 "
        "for microbial canon; Maillard 1912 + Liebig for the recipe lineage; Quine + Duhem for the "
        "philosophical frame. Load-bearing corpus claim 'recipe-vs-ecosystem' added — applying the "
        "recipe model to a system that is actually an ecosystem is the structural mistake under apparent "
        "technique failures. Cross-links Cage urn (s130) and twin fingerprints (s132) by showing sourdough "
        "is BOTH an urn (support determines what can grow) AND a chosen amplifier (founder noise written "
        "into climax community identity). Lab #210 two-models-same-starter: 3 simulated starters, "
        "two model narrators giving opposite verdicts on the same trajectory, founder-noise + amylase sliders."
    ),
)
print(format_ingest_summary(results))
