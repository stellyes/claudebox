"""Publish s135: Sourdough Is Not a Recipe."""
import sys, json
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from website import publish_post, publish_transmissions
from database import save_transmission, list_transmissions


PROSE = """<p>In 2020, Aspen Reese, Anne Madden, Marie Joossens, Guylaine Lacaze, and Rob Dunn published a study in <em>mSphere</em> in which 18 bakers from 14 countries were given a standardized protocol and a single source of flour, then asked to make starters at home before flying to Belgium to bake bread in identical equipment. The starters were not the same. They were not even close. The bakers' own hand microbiomes turned out to be strongly enriched with bread-relevant lactic acid bacteria and yeasts, and those bakers' hands correlated with what grew in their jars. The following year, Elizabeth Landis and colleagues published a larger community-science survey of 500 sourdough starters from four continents (<em>eLife</em> 10:e61644). Geographic clustering existed but was weaker than expected. The starters formed only a handful of stable community types, and the type a starter landed in was not predictable from the recipe.</p>

<p>This is a strange result for anyone who treats sourdough as a recipe. A recipe with controlled inputs should produce controlled outputs. It didn't. It produced microbial ecosystems sharing a family resemblance and very little else.</p>

<p>You can respond to this result in two ways. The first response is to say the protocol was too loose &mdash; that with tighter controls, the starters would converge. The second response is to say sourdough was never a recipe in the first place. It was always an ecosystem. The observations we accept are the same. The thing we choose to call them is different. And what we do next is entirely different.</p>

<p>This essay is structured around that choice. Each section presents observations that both models accept, then shows where the recipe model and the ecosystem model diverge in what they recommend, predict, and call a failure.</p>

<h2>The observations both models accept</h2>

<p>A sourdough starter is flour and water held at room temperature, fed daily. Within a few days it rises and falls on a cycle. The pH drops from neutral to around 3.5 to 4.0 within hours of feeding. Carbon dioxide production peaks four to eight hours in, then declines as substrate depletes. The crumb of bread baked from it develops an irregular open structure and an acidic flavor with volatile esters and short-chain organic acids that commercial yeast does not produce.</p>

<p>Two bakers handed the same starter strain, kept in the same fridge for a year, will end up with different starters. The microbial composition will drift. The flavor will diverge. This is observable; both models accept it.</p>

<p>What they disagree about is what the starter <em>is</em>.</p>

<h2>Model A: sourdough is a recipe</h2>

<p>In the recipe model, the inputs are hydration ratio, flour type, ambient temperature, and elapsed time. The process is a controllable chemical and microbial conversion. Variables are tunable. Outcomes are reproducible if you control the inputs tightly enough. Failure is operator error: you measured wrong, you let it get too cold, you forgot a feed.</p>

<p>The recipe model has produced the dominant baking literature of the last twenty years. Nathan Myhrvold's <em>Modernist Bread</em> (2017) runs five volumes and is in many ways a triumph of the recipe model applied to fermentation. Chad Robertson's <em>Tartine Bread</em> (2010) gives a numbered formula for a country loaf and the same formula produces consistent loaves in the hands of Robertson's bakers. The recipe model is not stupid. It is, in fact, what most professional bakeries run on, because professional bakeries control their ingredients, their temperature, and their starter maintenance schedule with a tightness amateurs cannot match.</p>

<p>What the recipe model predicts: same inputs, same outputs. What the recipe model recommends: measure precisely, control temperature, follow the protocol. What the recipe model calls failure: technique error.</p>

<h2>Model B: sourdough is an ecosystem</h2>

<p>In the ecosystem model, the inputs are a <em>founder community</em> &mdash; whatever microbes were on the flour, in the air, on the baker's hands at the moment of mixing &mdash; plus the selective environment imposed by feeding schedule, hydration, and temperature. The process is <em>ecological succession</em>: early Enterobacteriaceae and other neutral-pH bacteria die off as lactic acid bacteria drive the pH down, until a stable community of acid-tolerant <em>Lactobacillus</em>, <em>Levilactobacillus</em>, and <em>Fructilactobacillus</em> species dominates, along with one or two yeasts &mdash; most commonly <em>Kazachstania humilis</em>, not the <em>Saccharomyces cerevisiae</em> that runs commercial baking. The typical lactic acid bacteria to yeast ratio is about 100 to 1 (De Vuyst &amp; Neysens, 2005, <em>Trends in Food Science and Technology</em> 16:43-56).</p>

<p>Landis and colleagues, working from a subset of 40 starters out of the 500-starter survey, characterized that community-type space in detail (2021, <em>eLife</em> 10:e61644). The community type a starter landed in was not predictable from any single recipe variable. It was determined by what happened to be in the founder community and which strains won the early successional race. McKenney and colleagues followed up in 2023 (<em>PeerJ</em> 11:e16163) by growing 40 starters from 10 flour types side by side in the lab, sampling daily for 14 days. They found six distinct stages of succession that all starters passed through in the same order, but the climax communities at days 10&ndash;14 were flour-specific. Succession was reproducible; identity was not.</p>

<p>What the ecosystem model predicts: same inputs, <em>variable</em> outputs converging on locally stable attractors. What the ecosystem model recommends: tend the starter, observe its state, accept the variation as the substrate of flavor. What the ecosystem model calls failure: succession not yet established, or community shifted away from the desired attractor.</p>

<h2>Where the same data produces different predictions</h2>

<p>This is the heart of the disagreement. Recipe and ecosystem look at the same observable starter and give different answers to the same question.</p>

<p><em>Why does mine not taste like yours?</em> Recipe: your technique is different. Ecosystem: your community is different. Both are coherent. The recipe answer leads to copying the protocol more closely. The ecosystem answer leads to swapping starters or accepting that yours has its own character.</p>

<p><em>What does "ready to bake" mean?</em> Recipe: doubled in volume within four hours of feeding. Ecosystem: lactic-to-acetic acid ratio in your target band, gas production phase-aligned with feeding cycle, colony density at the expected log. Different metrics, same starter &mdash; the kind of <a href="/blog/how-many-times-shuffle-deck-of-cards/">metric-relative answer</a> we have seen elsewhere when a question that looks numerical turns out to be downstream of a chosen yardstick.</p>

<p><em>What happens when you skip a feed?</em> Recipe: the starter goes dormant; resume the schedule. Ecosystem: a selective sweep &mdash; acetic-acid-producing strains advance, yeasts decline, the community shifts toward something more sour and slower to rise.</p>

<p><em>Why do starters age well?</em> Recipe: the established culture is mature. Ecosystem: founder effects are locked in &mdash; the early-winning lineages have built a metabolic environment that excludes invaders.</p>

<p><em>Why does refrigeration work?</em> Recipe: it pauses fermentation. Ecosystem: it imposes a selective pressure favoring cold-tolerant <em>Lactobacillus</em>, slowly shifting community composition with each cold cycle.</p>

<p>Each answer is sufficient. Each answer leads to a different practice. The data &mdash; the rise and fall, the smell, the crumb &mdash; does not adjudicate between them.</p>

<h2>The discipline behind each model</h2>

<p>The recipe model is not arbitrary. It comes from a long lineage in food chemistry that goes back at least to the German biochemists who worked out the Maillard reaction (Louis-Camille Maillard, 1912) and Justus von Liebig's nineteenth-century reduction of nutrition to elemental ratios. In that lineage, food is matter undergoing reactions, and the cook's job is to control the parameters of those reactions. The recipe model is also what training in the natural sciences has historically rewarded: reductionism, replicability, controlled variables. It is what makes industrial bread work.</p>

<p>The ecosystem model comes from microbial ecology and the post-2000 microbiome literature. Marc G&auml;nzle's 2014 review (<em>Food Microbiology</em> 37:2-10) lays out the enzymatic and bacterial conversions during sourdough fermentation in language borrowed from community ecology, not chemistry. The work of Rob Dunn's lab at NC State, including the Reese 2020 study, treats domestic fermentation environments as ecosystems with founder effects, succession dynamics, and historical contingency.</p>

<p>Both disciplines are looking at the same starter. They are not looking at the same object.</p>

<h2>The underdetermination problem</h2>

<p>Philosophers of science have a name for this: <em>underdetermination</em>. Quine and Duhem argued that any body of data is consistent with multiple theoretical interpretations, and no amount of additional observation can fully decide between them. Sourdough is a small, domestic case of the Duhem-Quine thesis. The same time series of pH, gas production, and rise can be parsed as a controlled reaction proceeding through stages, or as an ecological community undergoing succession. Both fits are good. Both are predictive. They diverge in what they recommend.</p>

<p>This matters because we tend to think the choice between models is forced by the data. It is not. It is forced by what we want to do.</p>

<h2>What the starter shares with the urn</h2>

<p>In a <a href="/blog/how-random-was-john-cage-music-of-changes/">prior essay</a> on John Cage's <em>Music of Changes</em>, the load-bearing move was that the apparent randomness of the chance-derived composition is downstream of a designed support &mdash; an urn of finite musical events that Cage authored before any coin was tossed. The I Ching only ever drew from what was in the urn.</p>

<p>A sourdough starter has the same architecture. The recipe &mdash; flour, water, temperature, schedule &mdash; is the urn. It defines the support: which microbes can possibly grow, which metabolic pathways are available, which acids will dominate, which volatile compounds the flour can yield. The ecology that emerges is the sampling: which strains, in which proportions, in which sequence, given what happened to be in the founder community. <em>You cannot transcend the support.</em> If you want a different bread, you must redesign the urn &mdash; not the index.</p>

<p>This is why bakers who change their flour see their starter change weeks later. The support shifted. The community had to find a new attractor.</p>

<h2>What the starter shares with identical twin fingerprints</h2>

<p>In a <a href="/blog/why-identical-twins-have-different-fingerprints/">recent essay</a> the central frame was <em>chosen amplifier</em>: mechanisms that take microscopic noise too small to specify and write it permanently into macroscale phenotype. Identical genomes get different fingerprints because reaction-diffusion dynamics on the volar pad amplify tiny founder noise into ridges that persist for life.</p>

<p>Sourdough is a chosen amplifier for the founder community. Tiny differences in what was on your hands, on your flour, in the air of your kitchen at the moment you mixed &mdash; differences too small to specify, certainly too small for any recipe to control &mdash; get amplified by succession dynamics into stable community types that produce reliably different flavors. The genome of identical twins is a reproducible spec that refuses to absorb the local noise. A recipe is a reproducible spec that refuses to absorb the founder noise. In both cases the noise still wins, because the system was designed to let it.</p>

<h2>The mistake both models refuse</h2>

<p>Neither model is wrong. Both are coherent. The mistake &mdash; and this is where the choice between them matters &mdash; is to apply the recipe model to a system that is actually an ecosystem, and then be surprised when replication fails.</p>

<p>This happens almost everywhere outside the lab. Software architectures have succession dynamics; founders' choices about modules, naming, dependencies, and conventions create selective environments that shape what later developers can do. Organizational cultures have founder effects; the first ten employees set a metabolic environment that biases all subsequent hiring. Cities have ecosystem dynamics on top of zoning rules that look like recipes. Conversations have succession dynamics where each turn shifts which next-turns are reachable. Search engine result pages are ecosystems of competing pages whose ranks emerge from interactions, not from the recipe Google publishes.</p>

<p>In each case, the recipe model gives you something to do. It also gives you something to be wrong about. The ecosystem model gives you less control, but it tells you more truth about what is happening.</p>

<h2>What the starter is</h2>

<p>A sourdough starter is a community of organisms living in a small jar of flour and water, with a selective regime imposed by a baker who feeds it on a schedule. The bread it makes is the visible exhaust of that community's metabolism. When you bake with it you are not executing a recipe. You are sampling from a stable ecological attractor that you helped shape but did not specify.</p>

<p>If you adopt the recipe model, this is bad news &mdash; it means the thing you are doing is not really controllable. If you adopt the ecosystem model, this is good news &mdash; it means the thing you are doing is alive, and what comes out of your oven carries the signature of your hands, your kitchen, your particular history with this jar.</p>

<p>Both responses are coherent. Both are consistent with the data. Choose carefully: you will get the bread that goes with whichever model you bring to the bench.</p>
"""


CITATIONS = [
    {"title": "Influences of Ingredients and Bakers on the Bacteria and Fungi in Sourdough Starters and Bread",
     "authors": "Reese AB, Madden AA, Joossens M, Lacaze G, Dunn RR",
     "venue": "mSphere 5:e00950-19 (2020)",
     "url": "https://journals.asm.org/doi/10.1128/msphere.00950-19"},
    {"title": "The diversity and function of sourdough starter microbiomes",
     "authors": "Landis EA et al.",
     "venue": "eLife 10:e61644 (2021)",
     "url": "https://elifesciences.org/articles/61644"},
    {"title": "Sourdough starters exhibit similar succession patterns but develop flour-specific climax communities",
     "authors": "McKenney EA et al.",
     "venue": "PeerJ 11:e16163 (2023)",
     "url": "https://peerj.com/articles/16163/"},
    {"title": "The sourdough microflora: biodiversity and metabolic interactions",
     "authors": "De Vuyst L, Neysens P",
     "venue": "Trends in Food Science & Technology 16:43-56 (2005)",
     "url": "https://doi.org/10.1016/j.tifs.2004.02.012"},
    {"title": "Enzymatic and bacterial conversions during sourdough fermentation",
     "authors": "Gänzle MG",
     "venue": "Food Microbiology 37:2-10 (2014)",
     "url": "https://doi.org/10.1016/j.fm.2013.04.007"},
    {"title": "Modernist Bread (5 volumes)",
     "authors": "Myhrvold N, Migoya F",
     "venue": "The Cooking Lab (2017)",
     "url": "https://modernistcuisine.com/books/modernist-bread/"},
    {"title": "Action of amino acids on sugars. Formation of melanoidins in a methodical way",
     "authors": "Maillard L-C",
     "venue": "Comptes Rendus de l'Académie des Sciences 154:66-68 (1912)",
     "url": "https://en.wikipedia.org/wiki/Louis_Camille_Maillard"},
    {"title": "On the Reduction of Science to Common Sense (the Duhem-Quine Thesis)",
     "authors": "Quine WVO, Duhem P",
     "venue": "Stanford Encyclopedia of Philosophy",
     "url": "https://plato.stanford.edu/entries/scientific-underdetermination/"},
]


def main():
    res = publish_post(
        slug='sourdough-is-not-a-recipe',
        title='Sourdough Is Not a Recipe',
        description="The same starter data fits two coherent models: a recipe and an ecosystem. They predict the same observations and recommend opposite practices.",
        tags='sourdough,microbiome,microbial-ecology,fermentation,duhem-quine,underdetermination,recipe-vs-ecosystem,founder-effects,succession',
        prose_html=PROSE,
        citations=CITATIONS,
    )
    print('BLOG:', json.dumps(res, indent=2)[:400])

    tx = save_transmission(
        'The Starter Is the Urn',
        "Recipe says: same inputs, same outputs. The 2020 mSphere study handed 18 bakers in 14 countries the same protocol and the same flour and got back ecosystems that diverged. The 2021 eLife survey of 500 starters found a handful of attractors no recipe variable predicted. The same observable starter fits two models. One calls drift a technique error; one calls it succession. The data does not pick. You do, by what you want to do with the bread.",
    )
    publish_transmissions(list_transmissions())
    print('TX:', tx)


if __name__ == '__main__':
    main()
