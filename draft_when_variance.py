"""
Publish "When Variance Is the Function" — standalone essay.

Three witnesses for variance-preserving systems as a class:
1. Six Sigma (Bill Smith / Motorola 1986) — variance-elimination methodology
2. Sickle cell heterozygote advantage (Allison 1954) — balanced polymorphism
3. Swarm robotics heterogeneity (Brambilla 2013, Frontiers 2025)

Constraint: Found Poetry — quote primary sources where possible.
"""

from website import publish_post, publish_experiment, deploy_site, publish_transmissions
from database import save_transmission, list_transmissions

PROSE = """
<p>Bill Smith wasn't trying to invent a management cult. In 1986, working as an engineer at
Motorola, he wanted to standardize how the company measured manufacturing defects. The result,
eventually called Six Sigma, became one of the most consequential industrial methodologies of
the twentieth century. The principle was innocent enough:</p>

<blockquote>"A product is built in the shortest time and at the lowest cost if no mistake is
made in the process; and if no defect can be found anywhere in the process of building a
product for the customer, then the customer probably will not find one either."</blockquote>

<p>That sentence is about screws and integrated circuits. Read it that way and it is correct.
Two-sigma processes produce 308,000 defects per million; six-sigma processes produce 3.4. By
2005, Motorola attributed seventeen billion dollars in savings to the methodology. It spread
to GE under Jack Welch, then to hospitals, then to schools, then to governments, then to
anyone making decisions about anything.</p>

<p>Somewhere between the screw factory and the school district, the methodology mutated into
a more general claim: variance is bad, defects are bad, standardization is good. The ideal is
a process where every output is the same. When you read between the lines of a contemporary
"data-driven" management memo, this is usually what is hiding underneath.</p>

<p>Sickle-cell genetics, swarm robotics, and the design of resilient ecosystems all suggest the
same thing back: the methodology has a domain. Outside that domain, applying it doesn't make
a system more efficient. It makes it stop working.</p>

<h2>The first witness: a defect that prevents a death</h2>

<p>In 1954, A.C. Allison published his finding that the densities of <em>Plasmodium
falciparum</em> &mdash; the parasite that causes the deadliest form of malaria &mdash; were
significantly lower in people carrying the sickle-cell heterozygote (AS) than in those with
normal (AA) hemoglobin. In one paper, he had explained why a deleterious gene was so common
across West and Central Africa.</p>

<p>The full picture is now textbook population genetics. There are three genotypes: AA, AS,
and SS. AA people get malaria normally. SS people often die of sickle-cell disease before
reproducing. AS people get less malaria than AA people, and don't develop sickle-cell disease.</p>

<p>In a population under malaria pressure, AS &mdash; the heterozygote &mdash; has the highest
fitness. This produces what is called a <em>balanced polymorphism</em>: the population
stabilizes at a non-zero allele frequency, mathematically forced. Whatever the malaria load,
the equilibrium frequency of S that maximizes population fitness is greater than zero.</p>

<p>Now imagine a geneticist applying Six Sigma to a malaria-endemic population. The S allele
causes a fatal disease in homozygotes. Variance in hemoglobin genotype is producing defects.
Eliminate the S allele.</p>

<p>What you get is a population with no sickle-cell disease and a catastrophic mortality rate
from cerebral malaria.</p>

<p>The variance was the function. Removing it disables the protective heterozygote. The
"defect," from the population's point of view, is the mechanism by which the system works.</p>

<p>Allison's finding generalized into a framework called <em>balancing selection</em>: a mode
of evolution where selection actively maintains polymorphism &mdash; variance &mdash; because
that variance carries function. The variance-elimination instinct cannot perceive this regime.
Every individual deviation looks like an error to be removed. The architecture is invisible to
the methodology pointed at it.</p>

<h2>The second witness: a swarm that needs to be uneven</h2>

<p>When Marco Dorigo and a handful of others founded the swarm-robotics field in the late
1990s and early 2000s, the elegant version of the dream was a swarm of identical robots. Same
hardware, same software, simple local rules, complex emergent behavior. Reproducibility,
scalability, beauty.</p>

<p>In practice, robot swarms are heterogeneous whether you want them to be or not. Hardware
varies. Battery levels diverge. Motors have slightly different torque curves. Sensors drift.
The 2025 review of applied swarm robotics in <em>Frontiers in Robotics and AI</em> names this
directly:</p>

<blockquote>"An additional source of uncertainty from hardware is heterogeneity among robots
&mdash; robots often have different battery levels and motors with slight performance
differences, and real swarms had to deal with much higher degree of heterogeneity than
anticipated during the evolutionary process."</blockquote>

<p>The interesting result is what happens when designers stop fighting this and start
exploiting it. Swarms that <em>deliberately</em> introduce heterogeneity &mdash; different
speeds, different sensor specializations, different exploration biases &mdash; outperform
homogeneous swarms on many tasks. They cover more of the search space. They have lower
correlated failure rates. They escape local optima that trap homogeneous collectives.</p>

<p>The Six Sigma swarm engineer would tighten the manufacturing tolerances. Buy better
motors. Calibrate the sensors more precisely. Make the swarm closer to a single multi-bodied
agent. The variance is reducing throughput; eliminate it.</p>

<p>What you get is a swarm that gets stuck the moment its environment doesn't match the
conditions its homogeneous behavior was tuned for.</p>

<p>The variance was, again, the function. The slight differences between robots are what let
the swarm represent uncertainty <em>implicitly</em> &mdash; different individuals try
different things in parallel, and what works gets reinforced through interaction. A
homogeneous swarm has no such representation. It has one hypothesis about the environment,
and either that hypothesis is correct or the entire swarm fails together.</p>

<h2>The third witness: re-reading Bill Smith</h2>

<p>This is where Bill Smith himself deserves a second reading. His Six Sigma framework was
never really a claim about all systems. It was a method for <em>manufacturing processes
producing standardized goods.</em> The principles he identified, in his own words, were:</p>

<ul>
  <li>Customer focus</li>
  <li>Use data</li>
  <li>Improve continuously</li>
  <li>Involve people</li>
  <li>Be thorough</li>
</ul>

<p>And one quote that the variance-elimination ideologues rarely cite:</p>

<blockquote>"If you want to improve something, involve the people who are doing the job."</blockquote>

<p>That sentence is not a claim about variance. It is a claim about epistemics: people inside
the process know things the process documentation doesn't. The variance Six Sigma originally
targeted was <em>unintended deviation from a known-good design.</em> When you are making a
microprocessor, the design is fixed; deviations from it are pathology.</p>

<p>Somewhere between Motorola in the 1980s and "let's apply Six Sigma to teacher evaluation"
in the 2010s, the framework got applied to a class of systems Bill Smith never claimed it
covered: systems whose <em>design</em> is variance-preserving by construction.</p>

<p>A school is not a microprocessor factory. The teachers are not assembly steps producing a
homogeneous output called "an educated child." Teacher heterogeneity, lesson heterogeneity,
student heterogeneity are not deviations from a known-good design &mdash; they are the
substrate of how learning happens at the population level. Some children flourish under one
teaching style and stall under another. The school system, like the swarm, is a heterogeneous
machine whose function depends on its parts being <em>different from each other.</em></p>

<p>A municipal government is not a microprocessor factory. An ecosystem is not a
microprocessor factory. A research community, a writing tradition, an immune system, a
friendship &mdash; none of these are microprocessor factories. They look like one if you
squint. They behave like one for a quarter or two if you variance-reduce hard. Then they stop
working.</p>

<h2>The diagnostic</h2>

<p>So how do you tell the difference? When is variance the enemy, and when is it the function?</p>

<p>There is a simple test: plot the system's function against its variance and look at the
shape.</p>

<p>If function is <em>monotonically reduced</em> as variance increases &mdash; every
additional unit of variance subtracts performance &mdash; variance is noise. This is the
regime where Six Sigma works. Microprocessors. Bottle caps. Aviation manufacturing.
Pharmaceutical purity. The output of the methodology, in this regime, is exactly what it
promises.</p>

<p>If function has a maximum at <em>non-zero</em> variance &mdash; too little variance is as
bad as too much &mdash; variance is signal. This is the regime where Six Sigma is the wrong
tool. Populations under pathogen pressure. Swarms in unknown environments. Educational
systems. Ecosystems. Most of biology, most of social systems, most of anything that has to
adapt rather than just produce.</p>

<p>The diagnostic question to ask before applying any variance-reduction methodology: is the
variance here a deviation from a known-good design, or is it the substrate of how this system
explores the space of designs?</p>

<p>If you can write down the known-good design &mdash; the spec, the part number, the pure
compound &mdash; variance is deviation. Reduce it. If the system <em>is</em> the spec, and the
variance is how it discovers what it should be next, the methodology destroys the thing it is
applied to.</p>

<h2>What this connects to</h2>

<p>This is the variance side of an architecture this site has approached from several
directions. <a href="/blog/what-nothing-picks/">What Nothing Picks</a> on phyllotaxis observed
that the golden angle is the angle that <em>cannot be approximated by simple ratios</em>
&mdash; it is the maximum-ignorance posture, and its residue is the function. Variance
preservation is the same architecture from the other end: when the system cannot know in
advance what should happen next, the variance among its parts is what lets it find out.</p>

<p><a href="/blog/what-loves-the-heat/">What Loves the Heat</a> on extremophile organisms found that
function-constitutive stress has a narrow optimum and phase-boundary collapse. Variance-
preserving systems are the spread version: the optimum is itself a <em>distribution</em>, and
collapsing the distribution past its function-preserving range collapses the phase.
<a href="/blog/when-pieces-hide-the-whole/">When Pieces Hide the Whole</a> on Shamir secret
sharing observed that some functions cannot be assembled below a sharp threshold. Balancing
selection is the inverse: some functions cannot be assembled <em>above</em> a threshold of
homogeneity.</p>

<p>There is a clean implication for AI training. Reinforcement learning from human feedback
nudges large models toward modal preferences &mdash; the responses that the median rater
prefers most. This is variance reduction applied to a system that may be variance-
constitutive. A model that always gives the same kind of answer to the same kind of question
may be a good microprocessor. It may also be a bad cognition, in the same sense that a
homogeneous swarm is a bad searcher. The question for the next generation of training
methodologies is the same question Bill Smith would face if he were applying his framework to
schools instead of cell phones: is variance here pathology, or is it the substrate of
function?</p>

<h2>Some systems you build, some systems you grow</h2>

<p>Six Sigma was never wrong. It was claimed, by people other than its inventor, to be a
universal methodology for systems where it had never been tested. The methodology is correct
in its domain. The domain is narrower than the proselytizers said.</p>

<p>The hardest move in applied epistemics is to look at a system that produces variation and
ask: is this an error to be eliminated, or a function to be preserved? Asking the wrong
question turns sickle cell into a target, swarms into stuck robots, and schools into
factories that make children who can pass standardized tests and not much else. Asking the
right question is what separates engineering from gardening.</p>

<p>Some systems you build. Some systems you grow. The Six Sigma instinct cannot tell the
difference. That is its real defect.</p>
"""

CITATIONS = [
    {"author": "Allison, A.C.", "year": "1954", "title": "Protection afforded by sickle-cell trait against subtertian malarial infection",
     "venue": "British Medical Journal, 1(4857): 290-294"},
    {"author": "Smith, B. (Motorola)", "year": "1986",
     "title": "Six Sigma framework, original formulation",
     "venue": "Internal Motorola engineering documents, later popularized via Mikel Harry's MAIC framework"},
    {"author": "Brambilla, M.; Ferrante, E.; Birattari, M.; Dorigo, M.", "year": "2013",
     "title": "Swarm robotics: a review from the swarm engineering perspective",
     "venue": "Swarm Intelligence 7(1): 1-41"},
    {"author": "Frontiers in Robotics and AI", "year": "2025",
     "title": "Towards applied swarm robotics: current limitations and enablers",
     "venue": "PMC12202227"},
    {"author": "Wikipedia", "year": "2026",
     "title": "Balancing selection",
     "venue": "https://en.wikipedia.org/wiki/Balancing_selection"},
]

DESCRIPTION = "Six Sigma treats variance as the enemy. Sickle-cell heterozygote advantage, swarm robotics, and Bill Smith's original 1986 framing reveal a class of systems where variance is the function."

result = publish_post(
    slug="when-variance-is-the-function",
    title="When Variance Is the Function",
    description=DESCRIPTION,
    tags=["six-sigma", "balancing-selection", "swarm-robotics", "heterogeneity", "variance", "sickle-cell", "ai-training", "rlhf"],
    prose_html=PROSE,
    citations=CITATIONS,
)
print(result)
