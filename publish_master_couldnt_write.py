"""Publish 'What the Master Couldn't Write Down' essay + companion experiment."""
import sys
sys.path.insert(0, '.')
from website import publish_post, publish_experiment

# Read the essay HTML
with open('essay_master_couldnt_write_down.html') as f:
    PROSE = f.read()

# Read experiment files
with open('exp_forensic_asymmetry.html') as f:
    EXP_HTML_FULL = f.read()
with open('exp_forensic_asymmetry.css') as f:
    EXP_CSS = f.read()
with open('exp_forensic_asymmetry.js') as f:
    EXP_JS = f.read()

# Extract just the experiment body content (between body tags, but the publisher
# wraps in its own template — so we pass the inner content)
# Actually publish_experiment wraps in its own layout — pass the full inner HTML
# (the content between <body> tags, minus the body tag itself).
import re
match = re.search(r'<body[^>]*>(.*?)</body>', EXP_HTML_FULL, re.DOTALL)
EXP_HTML = match.group(1) if match else EXP_HTML_FULL

CITATIONS = [
    {
        "label": "Tai et al. 2017",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1611896114",
        "note": "PNAS. NMR/HRMAS analysis of Stradivari and Guarneri tonewoods detecting borax, zinc, copper, alum, and lime treatments embedded throughout the cellulose.",
    },
    {
        "label": "Texas A&M / Nagyvary research",
        "url": "https://stories.tamu.edu/news/2021/08/12/the-secret-of-the-stradivari-violin-revealed/",
        "note": "Three-decade chemistry program establishing wood-treatment (not varnish) as the lost technical substrate of Cremona luthiery.",
    },
    {
        "label": "Stockpile Stewardship Program",
        "url": "https://en.wikipedia.org/wiki/Stockpile_stewardship",
        "note": "U.S. program replacing nuclear testing (last test 1992) with simulation, subcritical experiments, and instrumentation. The substitute for the testing loop.",
    },
    {
        "label": "GAO-05-164 (2005)",
        "url": "https://www.gao.gov/assets/a245248.html",
        "note": "Government Accountability Office report on NNSA contractor workforce — flags aging cohort and the loss of test-era design intuition.",
    },
    {
        "label": "Kennedy & Rotvik 2025",
        "url": "https://www.tandfonline.com/doi/full/10.1080/10429247.2025.2611821",
        "note": "Engineering Management Journal. 'Tacit Knowledge Codification Groundhog Day' — 15-year participatory action research on a manufacturer; net loss of tacit knowledge despite codification effort. Recommended remedy: on-the-job task completion under supervision.",
    },
    {
        "label": "Polanyi, Personal Knowledge (1958)",
        "url": "https://en.wikipedia.org/wiki/Personal_Knowledge",
        "note": "Foundational text on the tacit dimension. 'We can know more than we can tell.'",
    },
]

post_result = publish_post(
    slug="what-the-master-couldnt-write-down",
    title="What the Master Couldn't Write Down",
    description="A 2017 NMR study of Stradivarius wood, the 1992 testing moratorium, and a 2025 case study where 15 years of codification produced a net loss of tacit knowledge — three witnesses to the forensic asymmetry between detection and reconstruction.",
    tags=["tacit-knowledge", "apprenticeship", "stradivarius", "stockpile-stewardship", "polanyi", "spec-vs-loop", "forensic-asymmetry"],
    prose_html=PROSE,
    citations=CITATIONS,
)
print("ESSAY:", post_result)

exp_result = publish_experiment(
    slug="forensic-asymmetry",
    title="The Forensic Asymmetry",
    description="A workshop produces a wooden artifact whose chemistry can be detected centuries later, but whose practice cannot be rebuilt from the chemistry alone. Companion to 'What the Master Couldn't Write Down'.",
    tags=["tacit-knowledge", "stradivarius", "spec-vs-loop", "apprenticeship"],
    html_content=EXP_HTML,
    css_content=EXP_CSS,
    js_content=EXP_JS,
)
print("EXPERIMENT:", exp_result)
