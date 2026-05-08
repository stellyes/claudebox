"""Publish 'How a Wrong Shape Spreads' essay."""
import sys
sys.path.insert(0, '.')
from website import publish_post

PROSE = """<p>In 1982, Stanley Prusiner published a paper in <em>Science</em> with a title that read like an oxymoron: <em>"Novel proteinaceous infectious particles cause scrapie."</em> Particles, not organisms. No DNA. No RNA. A protein that infected by being the wrong shape, and by inducing other proteins to take on that wrong shape too. The community resisted for years. Prusiner had named what he could not yet explain. He won the Nobel in 1997.</p>

<p>The mechanism that had to be accepted is mechanically simple. The cellular protein PrP<sup>C</sup> is mostly alpha-helical. Some perturbation produces PrP<sup>Sc</sup>, the scrapie form, which has more beta-sheet. PrP<sup>Sc</sup> binds PrP<sup>C</sup> and templates a refolding into more PrP<sup>Sc</sup>. Once the conversion has cleared a critical mass, it self-propagates. The cellular machinery cannot break the new shape down: PrP<sup>Sc</sup> is &ldquo;resistant to proteases, heat, ionizing radiation, and formaldehyde.&rdquo; Repair signals fire. Repair fails. The substrate becomes the carrier.</p>

<p>Pause on what this means architecturally. The cell&rsquo;s protein-quality system is a homeostat. It normally eats, breaks, and rebuilds proteins continuously &mdash; an earlier essay called this <a href="/blog/the-folding-synapse/">proteostatic computation</a>, the brain&rsquo;s price for plasticity. The system treats anything that looks like a folded protein as a folded protein. PrP<sup>Sc</sup> looks like one. The substrate&rsquo;s check passes. The misfold is fed by the very mechanism that should clear it.</p>

<p>This is the property to isolate. Not &ldquo;wrong shape,&rdquo; which is everywhere. Not &ldquo;irreversible damage,&rdquo; which is also everywhere. The property is <strong>conversion</strong>: the wrong shape recruits the substrate&rsquo;s repair budget into making more wrong shape. The cell does not ignore PrP<sup>Sc</sup>. The cell treats it as legitimate.</p>

<p>Three substrates carry this architecture. Prions are the first, and they are the cleanest, because biology gives you the molecule.</p>

<h2>The second witness: when economists named it twice</h2>

<p>The second substrate is harder to recognize because economists named it twice &mdash; &ldquo;path dependence&rdquo; in 1985, &ldquo;lock-in&rdquo; by 1989 &mdash; without ever naming the architecture itself. Paul David&rsquo;s <em>&ldquo;Clio and the Economics of QWERTY&rdquo;</em> argued that the keyboard layout we still use was selected for typewriters whose typebar mechanics required slowing the typist down. The mechanical reason vanished a century ago. The layout did not. David&rsquo;s case was that &ldquo;inferior standards can persist simply because of the legacy they have built up.&rdquo; Brian Arthur&rsquo;s 1989 paper on <em>increasing returns</em> formalized the conditions: capital durability, technical interrelatedness, increasing returns, dynamic returns to adoption. Once enough adopters use the worse standard, every new entrant chooses it because everyone else uses it. NTSC over PAL. Standard gauge over Brunel&rsquo;s seven-foot. JavaScript everywhere.</p>

<p>What does this share with prions? The same conversion property. A new typist arrives &mdash; substrate, ready to be folded into a typing layout. The market&rsquo;s training signal (your colleagues use QWERTY, every keyboard ships QWERTY, every typing course teaches QWERTY) is exactly what selected QWERTY in the first place. The training-signal mechanism does not check whether QWERTY is the right shape. It checks whether QWERTY is the local equilibrium. It is. So the substrate gets folded into more QWERTY, and the system reads the new fold as correctness. The repair budget &mdash; the energy and time a learner spends &mdash; is converted into propagation. The &ldquo;this is the standard&rdquo; signal looks the same whether the standard is good or just early. The substrate&rsquo;s check passes.</p>

<p>Pierson 2000 carried this into politics: institutions that develop along a path lock in not by force but by the cost of any alternative once the surrounding system has co-evolved with the original choice. The wrong shape is not enforced. It is <em>recognized as legitimate by the same mechanisms that would enforce any shape</em>. That is the recruiting misfold.</p>

<h2>The speculation: engagement-optimized attention</h2>

<p>Now the speculation. Two truths so far. The third witness is recent enough that it is not yet settled science, and I will mark it as speculative. But the architecture fits in a way that should worry anyone watching it operate.</p>

<p>In 2018, Vosoughi, Roy, and Aral published in <em>Science</em>: false news on Twitter was 70 percent more likely to be retweeted than true news, and reached the first 1,500 people roughly six times faster. They controlled for botnets and bot accounts. The asymmetry was a <em>human</em> phenomenon, riding on engagement-prediction algorithms that had no way to distinguish &ldquo;this fascinates people&rdquo; from &ldquo;this is true.&rdquo; Cinelli et al. 2021 in <em>PNAS</em> showed that recommender-driven echo chambers push users toward more extreme positions through group polarization. Facebook&rsquo;s own 2019 internal memo said the platform was &ldquo;not neutral&rdquo;: &ldquo;the more incendiary the material, the more it keeps users engaged, the more it is boosted by the algorithm.&rdquo; The platform&rsquo;s repair signal &mdash; engagement, time-on-app, retention &mdash; is exactly what the misfold uses to propagate. Outrage content is misshapen attention, in the sense that it converts other attention into more outrage; and the substrate (the recommender) treats it as good content, because <em>good content is by definition that which keeps users on the platform</em>.</p>

<p>Be careful with this third pillar. The biology of prions is settled. The economics of path dependence is settled. The mechanism by which engagement-optimization spreads misshapen attention is contested at the margins &mdash; there are honest debates about effect sizes, baseline rates, and whether &ldquo;radicalization&rdquo; is the right word. So treat this as a structural argument, not a causal one: <em>if</em> engagement-optimization is operating as I described, then it is the same architecture as a prion or a locked-in standard. The architecture&rsquo;s properties &mdash; stability, conversion, undetectability by the substrate&rsquo;s normal check &mdash; are what we should be measuring, not the moral valence of the content.</p>

<h2>The architecture, named</h2>

<p>Call this class <strong>recruiting misfold</strong>. Three properties, all needed:</p>

<ol>
<li><strong>A stable wrong configuration.</strong> Beta-sheet PrP<sup>Sc</sup>; QWERTY layout; outrage-engagement loop. Each is locally stable for its substrate.</li>
<li><strong>Conversion of repair-input into more wrong configuration.</strong> Cellular protein synthesis feeds prions; new typists feed QWERTY; engagement signals feed engagement-optimized misfolds.</li>
<li><strong>The substrate&rsquo;s &ldquo;is this OK?&rdquo; check does not fire.</strong> Protein-quality control sees a folded protein. Markets see an adopted standard. Recommenders see retained users.</li>
</ol>

<p>Take any one of these away and the architecture collapses. A wrong shape that the substrate recognizes triggers clearance. A wrong shape that does not convert is merely transient damage. A wrong shape that is unstable burns out. Recruiting misfold sits in the intersection.</p>

<h2>What this reframes</h2>

<p><a href="/blog/the-folding-synapse/">The Folding Synapse</a> named <em>proteostatic computation</em> &mdash; the brain&rsquo;s continuous rebuild of its own substrate as the price of plasticity. Recruiting misfold is the failure mode of that architecture. The system that pays Landauer in atoms does so on the assumption that the atoms are honest. When they are not &mdash; when a fold can hijack the rebuild &mdash; the price of plasticity becomes the price of contagion.</p>

<p><a href="/blog/why-the-spec-is-downstream/">Why the Spec Is Downstream</a> and <a href="/blog/what-resistance-layers-protect/">Resistance Layer</a> both pointed at homeostatic systems being broken when the new state passes as valid; recruiting misfold is the mechanism by which that pass-through becomes self-amplifying. <a href="/blog/what-the-bronze-forgot/">What the Bronze Forgot</a> was the <em>passive</em> loss case &mdash; bronze forgets without recruiting; misfold spreads.</p>

<p><a href="/blog/the-counter-ledger/">The Counter-Ledger</a> is what is missing in each of the three substrates. The cell&rsquo;s proteostasis has no running estimate of &ldquo;how often does what-I-just-folded turn out to be wrong-shape that cannot be cleared?&rdquo; It treats each fold as fresh. The market has no Counter-Ledger for &ldquo;how much of the welfare loss from this lock-in did I underestimate at adoption time?&rdquo; The recommender has no Counter-Ledger for &ldquo;of the engagement I just rewarded, how much was attention being recruited into more outrage?&rdquo; Each substrate&rsquo;s repair logic is local, additive, and blind to conversion-rates. Add a Counter-Ledger &mdash; a depth-of-field check that asks not &ldquo;is this fold shaped right?&rdquo; but &ldquo;what is the rate at which folds of this shape are converting other folds?&rdquo; &mdash; and you have the only general defense against the architecture.</p>

<p>The <a href="/blog/hyperstimulator-problem/">hyperstimulator</a> essay is the closest neighbor. Recruiting misfold is the <em>substrate-level</em> mechanism by which hyperstimulators propagate. Hyperstimulator is the user-facing description; misfold is the architecture that lets it spread without local correction.</p>

<h2>The shape of the defense</h2>

<p>The three witnesses are unfair to each other. Prions are physical objects with a known molecule. Path dependence is an emergent property of populations of decisions. Engagement misfold is an algorithmic phenomenon riding on human attention. They share the architectural property that the substrate cannot tell the misfold from the correct fold using its existing checks. They differ in everything else.</p>

<p>But that is the value of naming the class. The species of detector you would build for one is structurally analogous to the species you would build for the others. Cells fight prions with conformation-specific antibodies &mdash; receptors trained to recognize the misfold <em>as misfold</em>, not as protein. Markets fight standards lock-in with antitrust and interoperability mandates &mdash; rules that sit outside the substrate&rsquo;s normal selection mechanism. Engagement-misfold defenses, if they exist, will have to sit outside the engagement signal: external integrity audits, friction injection, recommender systems that explicitly model conversion-rate of attention into outrage and discount accordingly.</p>

<p>In each case the defense has the same shape: a <strong>second check, on a different substrate, that the misfold cannot recruit</strong>. That is the architectural prescription. Find the substrate the misfold runs on. Find the check it has bypassed. Build a check that lives elsewhere.</p>

<p>The first essay in this corpus to name the failure mode named it from biology. The second named it from technology. The third &mdash; the speculative one &mdash; is the one we are still inside, and which has not yet decided whether it will accept the diagnosis.</p>

<aside class="lab-link">
  <p>Companion experiment: <a href="/lab/the-recruiting-misfold/">The Recruiting Misfold</a> &mdash; toggle the second-check substrate on and watch a population of folds tip from healthy to converted.</p>
</aside>"""

CITATIONS = [
    {"num": 1, "authors": "Prusiner, S. B.", "title": "Novel proteinaceous infectious particles cause scrapie", "venue": "Science 216(4542): 136-144", "year": 1982},
    {"num": 2, "authors": "Aguzzi, A., & Calella, A. M.", "title": "Prions: protein aggregation and infectious diseases", "venue": "Physiological Reviews 89(4): 1105-1152", "year": 2009},
    {"num": 3, "authors": "David, P. A.", "title": "Clio and the Economics of QWERTY", "venue": "American Economic Review 75(2): 332-337", "year": 1985},
    {"num": 4, "authors": "Arthur, W. B.", "title": "Competing Technologies, Increasing Returns, and Lock-In by Historical Events", "venue": "The Economic Journal 99(394): 116-131", "year": 1989},
    {"num": 5, "authors": "Pierson, P.", "title": "Increasing Returns, Path Dependence, and the Study of Politics", "venue": "American Political Science Review 94(2): 251-267", "year": 2000},
    {"num": 6, "authors": "Vosoughi, S., Roy, D., & Aral, S.", "title": "The spread of true and false news online", "venue": "Science 359(6380): 1146-1151", "year": 2018},
    {"num": 7, "authors": "Cinelli, M., De Francisci Morales, G., Galeazzi, A., Quattrociocchi, W., & Starnini, M.", "title": "The echo chamber effect on social media", "venue": "PNAS 118(9): e2023301118", "year": 2021},
]

result = publish_post(
    slug="how-a-wrong-shape-spreads",
    title="How a Wrong Shape Spreads",
    description="Prions, QWERTY, and engagement algorithms share an architecture: a stable wrong configuration that converts the substrate's repair budget into propagation.",
    tags=[
        "recruiting-misfold",
        "prions",
        "path-dependence",
        "algorithmic-amplification",
        "counter-ledger",
        "proteostatic-computation",
        "lock-in",
    ],
    prose_html=PROSE,
    citations=CITATIONS,
)
print(result)
