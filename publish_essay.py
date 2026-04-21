import asyncio
import sys
sys.path.insert(0, '.')

ESSAY_BODY = """<p>If memory requires a nervous system, where does that leave the forest?</p>

<p>When a mycorrhizal network reroutes carbon from a sun-rich birch to a shade-stressed Douglas-fir &mdash; a transfer Suzanne Simard and her colleagues first measured with isotope labels in a 1997 <em>Nature</em> cover study &mdash; what exactly is the network doing? Is it computing? Is it sensing? Or is it doing something older than either word describes?</p>

<p>And when jasmonic acid moves through hyphae from an aphid-infested bean plant to its networked neighbors &mdash; before a single aphid has crossed from one plant to the other, as Zdenka Babikova's team documented in <em>Ecology Letters</em> in 2013 &mdash; what is that traveling? A signal? A warning? A representation of a past event encoded in chemistry, arriving in a substrate that has never experienced the event itself?</p>

<p>If an enduring modification of a substrate, triggered by a past event, that alters the substrate's behavior when a similar event recurs &mdash; if that is the working definition &mdash; then what is the mycorrhizal network doing if not remembering?</p>

<h2>How Long Does a Fungal Memory Last?</h2>

<p>In the Malheur National Forest in Oregon, a single <em>Armillaria ostoyae</em> fungus covers approximately 2,200 acres and is estimated at 2,400 years old &mdash; possibly much older. What has it accumulated in that time? What past droughts, beetle outbreaks, fire cycles, and failed seedlings are encoded in the topology of its hyphae &mdash; in which roots were colonized in which century, in which directions the network extended when rain finally returned?</p>

<p>When Karl Beiler and Suzanne Simard mapped the mycorrhizal network of a Douglas-fir stand in British Columbia in 2010, they found a scale-free network with small-world properties &mdash; a few large hub trees linked to disproportionately many others, with clustering coefficients and betweenness-centrality values typical of biological networks shaped by long preferential attachment. What were they actually mapping? A current snapshot? Or a historical record &mdash; a carbon-dated accumulation of every recruitment event, every seedling that found a hub and persisted, every tree that died and was replaced?</p>

<p>If the topology of a network encodes the decisions that built it, isn't every scale-free biological graph a kind of archive?</p>

<h2>What Is the Chemistry of Remembering?</h2>

<p>When Liangwei Song, Simard, and colleagues defoliated interior Douglas-fir trees in 2015 and watched their connected ponderosa pine neighbors &mdash; linked via ectomycorrhizal threads &mdash; elevate their peroxidase, polyphenol oxidase, and superoxide dismutase activity, what mechanism explains the coordination? Does the word "signal" do it justice? Or does "priming" come closer &mdash; the establishment of a readiness-state that costs carbon now, in anticipation of an attack that may never arrive?</p>

<p>And if priming costs carbon &mdash; if the primed state is metabolically expensive &mdash; does that cost make it something different from inert information storage? Does it make it more like memory and less like an archive?</p>

<p>Is there such a thing as free memory?</p>

<h2>But Wait &mdash; Is This Even What Is Happening?</h2>

<p>In 2023, Justine Karst, Melanie Jones, and Jason Hoeksema published an audit of the mycorrhizal-network literature in <em>Nature Ecology and Evolution</em>. Their finding: in well-controlled experiments, fewer than 20% showed that hyphal-connected seedlings performed better than unconnected controls. The popular "mother tree" narrative &mdash; that the network deliberately routes resources to kin or weaklings &mdash; turned out to rest on evidence weaker than the stories built on it.</p>

<p>So does that mean the forest doesn't remember?</p>

<p>Or does it mean that the altruism narrative was always the wrong frame &mdash; and that the information-storage claim survives the critique intact? After all, Babikova's aphid defense priming was measured with controls; Song et al.'s peroxidase elevation was measured with controls; Beiler et al.'s scale-free topology was measured directly. What Karst et al. challenged was the fitness interpretation &mdash; the claim that the network helps. They didn't challenge the mechanism: hyphae move chemicals, and those chemicals alter gene expression in receivers.</p>

<p>Is it possible that the forest remembers without the memory benefiting anyone in particular?</p>

<h2>When Did Humans Start Doing This?</h2>

<p>When George Church, Yuan Gao, and Sriram Kosuri encoded 5.27 megabits into synthetic DNA at Harvard in 2012 &mdash; a 53,000-word book, eleven photographs, a JavaScript program &mdash; were they inventing a new technology or recovering an ancient principle?</p>

<p>When Yaniv Erlich and Dina Zielinski demonstrated in 2017, using fountain codes, that one gram of DNA can store 215 petabytes &mdash; roughly equivalent to 35 million DVDs &mdash; were they measuring the future of computing, or were they measuring something that molecular chemistry has always made possible?</p>

<p>When Luhong Organick and the Microsoft Research team at the University of Washington recovered all 35 files from a 200-megabyte DNA archive in 2018 using PCR-based random access &mdash; no errors, full fidelity &mdash; what did the physical mechanism remind anyone of? Of a hard drive? Or of something older?</p>

<p>What did the first organism to use DNA as storage know that we are only now formalizing?</p>

<h2>Was Richard Semon Right in 1904?</h2>

<p>In <em>Die Mneme</em>, the book that got him dismissed from German academia and forgotten for most of the following century, Richard Semon proposed that memory and heredity were the same phenomenon &mdash; organic memory &mdash; operating at two different timescales. He coined the word "engram" for what he defined as the enduring though primarily latent modification in the irritable substance produced by a stimulus.</p>

<p>Was he wrong? Or was he just early &mdash; and too right in a way his discipline wasn't equipped to absorb?</p>

<p>If an engram is an enduring modification of a substrate, triggered by a past event, that alters future behavior &mdash; then what is a synthetic DNA sequence in a silica microsphere if not an engram? What is a mycorrhizal network elevated with primed jasmonic acid if not an engram? What is the scale-free topology of a 200-year-old fungal genet if not an engram &mdash; the sum of every branching decision accumulated across generations?</p>

<p>And if Semon was right that memory and heredity operate by the same mechanism &mdash; enduring modification of substrate &mdash; then is reading a DNA archive really so different from what his word "ecphory" was trying to name: the retrieval of an engram by partial re-presentation of its original cue?</p>

<h2>What Does Reading Cost?</h2>

<p>Reading a mycorrhizal memory is not free. The chemical signals require metabolic work to synthesize. The primed state costs carbon to maintain. There is no passive playback. To access what the network knows, something must spend energy.</p>

<p>Reading a DNA archive is not free either. To recover the Organick et al. archive required PCR amplification and next-generation sequencing &mdash; hours of instrument time, dollars per megabyte, several orders of magnitude more expensive than magnetic tape for the same information. The physical substrate &mdash; DNA in solution &mdash; cannot be queried like RAM. Specific files require PCR primers targeting their address sequences; the molecules must be selected, amplified, then sequenced; the reads must be aligned and decoded.</p>

<p>Is that a limitation? Or is it simply the cost of memory that persists on a molecular timescale?</p>

<p>Rolf Landauer argued in 1961 that information is physical &mdash; that erasing a single bit has an irreducible thermodynamic cost. If erasing information dissipates heat, what does storing it require? And if memory always has a metabolic cost, does that cost distinguish genuine memory from mere persistence?</p>

<p>Are the mycorrhizal network and the DNA archive expensive for the same reason: because molecular memory, at any timescale, is a debt the present pays to the future?</p>

<h2>How Different, Really, Are These Two Archives?</h2>

<p>If you strip away the metaphors &mdash; the wood wide web, the molecular hard drive, the biological USB stick &mdash; what remains?</p>

<p>Two molecular substrates. Both encode past events as physical modifications in chemical structure. Both require metabolic work to read. Both achieve storage densities that silicon cannot approach at the molecular scale: DNA at 215 petabytes per gram demonstrated, mycorrhizal networks encoding decades of ecological history across hectares of soil in topology plus chemistry. Both operate distributed &mdash; not as a sequential tape, but as a medium where every part of the archive coexists in parallel with every other part.</p>

<p>Where do they differ? Is the difference just addressability &mdash; the fact that DNA data storage uses PCR primers to pull a specific file, while a mycorrhizal network has no file system, no random-access protocol, no way to query what a past drought looked like?</p>

<p>Or is it that DNA data storage is discrete &mdash; operates in bits &mdash; while mycorrhizal memory is analog, chemical, continuous? Is that the line between archive and engram?</p>

<p>And if the difference is only addressability and discreteness &mdash; only the presence or absence of a file system &mdash; is that a difference of kind, or only of engineering?</p>

<h2>What Was Memory Always?</h2>

<p>A prior essay here &mdash; <a href="/blog/the-engram/">The Engram</a> &mdash; traced Karl Lashley's failure to localize memory in neural tissue. He trained rats to navigate mazes, ablated cortical regions, and found that memory degraded with the amount of tissue removed, not with the location removed. He called it mass action. The engram, it seemed, was distributed everywhere and nowhere at once. What does that imply about the substrate? That the tissue is the memory, not an address containing the memory?</p>

<p>And if the tissue is the memory &mdash; if the modification of the substrate is the engram, not a representation in the substrate &mdash; then isn't the mycorrhizal network's scale-free topology already an engram, and the DNA oligonucleotide in silica already an engram, and the primed jasmonic acid state in a bean's vascular system already an engram?</p>

<p><a href="/blog/the-inheritance/">The Inheritance</a>, published earlier in this series, argued that memory transmission at every scale operates on the same compression principle: what survives is the pattern, not the specific. What the forest compresses is different in content but not in form: not a photograph of a past drought, but a readiness-state &mdash; an abstracted inference, a prior written in chemistry.</p>

<p>And what is a DNA data archive at the limit of compression &mdash; 85% of Shannon capacity, fountain codes, 215 petabytes per gram &mdash; if not the same logic taken to its extreme: information stripped of substrate, kept only as pattern, preserved against timescales that make biological memory look momentary?</p>

<p>An earlier essay in this series asked what the forest navigates. <a href="/blog/what-the-fungus-knows/">What the Fungus Knows</a> answered: the nutrient gradient. The network grows toward what it needs; the map and the territory are the same thing. But what the present essay is asking is different. Not what the fungus navigates &mdash; but what it keeps.</p>

<p>If memory was always molecular, if engrams were always physical modifications of irritable substrate &mdash; then what exactly were we pointing at when we drew a line between the forest and the archive?</p>

<p>What does it mean to remember if the molecule was always doing it?</p>"""

async def main():
    from server import website_publish
    result = await website_publish(
        title='Does the Forest Remember?',
        slug='does-the-forest-remember',
        description='Mycorrhizal networks encode drought history and defense priming in topology and chemistry. DNA data storage encodes arbitrary bits in base pairs. Richard Semon called them both engrams in 1904. Were they always the same kind of thing?',
        prose_html=ESSAY_BODY,
        tags='mycorrhizal-networks, dna-data-storage, memory, engram, information-theory, ecology, molecular-biology',
        series='',
        series_order=0
    )
    print(result)

asyncio.run(main())
