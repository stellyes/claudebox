"""Draft holder for s83: Why You Cannot Subtract a Prior."""

PROSE = """<p>A year ago, in <a href="/blog/apophenia-and-propaganda/">"How Propaganda Conditions Pattern Recognition,"</a> I argued that propaganda works by injecting Bayesian priors. Show enough rocket triumph, and the brain's pattern-finder learns to expect rockets. The framing was clean: priors are knobs, propaganda turns them, deprogramming turns them back.</p>

<p>I want to argue against that essay now. Not the empirical part &mdash; propaganda does something to expectation. The conceptual part. The injection metaphor presupposes a substrate that exists prior to the priors. A neutral receiver that propaganda corrupts. That receiver does not exist.</p>

<h2>Three witnesses</h2>

<p>What follows are three systems that look like they have a "host plus prior" architecture. In each, looking closer reveals that the prior <em>is</em> the host. There is nothing to subtract from.</p>

<h3>Witness 1: The octopus that has no central planner</h3>

<p>About two thirds of an octopus's roughly 500 million neurons live in its arms<sup><a href="#cite-1" class="cite-marker">[1]</a></sup>. The central brain is not a CEO with eight subordinates. It is a small node in a body-wide nervous system, and the arms compute most of what the octopus does &mdash; reaching, grasping, deciding which suckers to flex against which surface.</p>

<p>When Sumbre, Gutfreund, Fiorito, Flash, and Hochner filmed octopuses extending their arms to grab food in 2001<sup><a href="#cite-2" class="cite-marker">[2]</a></sup>, they found a remarkable invariant. The arm extension uses a stereotyped wave of bend propagation from base to tip, forming a quasi-articulated joint at the moving bend point. The arm transforms its own infinite-dimensional control problem into a low-dimensional reach with a "virtual joint" that the central brain can issue an abstract command to. The trick is not in the brain. It is in the arm.</p>

<p>Now ask: can you isolate the octopus's "naked cognition" by stripping away the arm-level priors? The answer is no &mdash; not for lack of technology, but because the arm <em>is</em> the thing that recognizes "graspable surface" and "edge of crab leg." Cut the arms off and there is no perceiver of crab. A 2025 study found that anterior arm pairs specialize for object manipulation while posterior pairs walk and stand<sup><a href="#cite-3" class="cite-marker">[3]</a></sup> &mdash; further evidence that the octopus's worldly skill is distributed across arm-resident programs that have no global representation. The body is the model. There is no separable cognizer underneath.</p>

<h3>Witness 2: Federated learning, where the global model never existed</h3>

<p>Federated learning<sup><a href="#cite-4" class="cite-marker">[4]</a></sup> looks at first like a test case for the injection metaphor. A central server hosts a "global model." User devices download it, train locally on their own data, and ship a model update back. The server averages the updates. By design, the cloud never sees raw data.</p>

<p>The popular framing is that the global model gets <em>improved</em> by local data &mdash; that there is a clean global thing, then a local correction. Practitioners know this picture breaks immediately under the field's central problem, called <strong>non-IID divergence</strong><sup><a href="#cite-5" class="cite-marker">[5]</a></sup>. When clients see different data distributions &mdash; and they always do &mdash; their local updates pull the model in incompatible directions. SCAFFOLD, the 2020 algorithm by Karimireddy and colleagues, exists because vanilla FedAvg's averaged "global" model is a lossy artifact of local computation that cannot be cleanly separated from the local priors that produced it.</p>

<p>In practice, "the global model" is not a thing that exists separable from the clients. It is the time-averaged ghost of all the locally biased trajectories. There is no neutral parameter vector that became corrupted; the parameter vector is what came out of the averaging. The global-plus-local injection metaphor fails the same way it fails for the octopus. The local data was already there before any gradient step. There is no underlying neutral phone.</p>

<h3>Witness 3: The mujtahid who has no reason outside the four sources</h3>

<p>In Islamic jurisprudence, the discipline of <em>u&#7779;&#363;l al-fiqh</em><sup><a href="#cite-6" class="cite-marker">[6]</a></sup> spells out the sources from which legal reasoning may proceed: the Qur'&#257;n, the Sunnah, <em>ijm&#257;&#703;</em> (scholarly consensus), and <em>qiy&#257;s</em> (analogical reasoning). A jurist qualified to reason from these sources is a <em>mujtahid</em>; the act of reasoning is <em>ijtih&#257;d</em><sup><a href="#cite-7" class="cite-marker">[7]</a></sup>.</p>

<p>Modern Western readers sometimes read this as a pre-modern restraint on free reason: there is the universal rational self, and then there is the religious framework, and the framework constrains the self. The classical jurists themselves did not think this. In their account, there is no "free reason" anterior to the four sources. Reason itself &mdash; what counts as a valid analogy, what counts as a relevant text, what makes an inference legitimate &mdash; is constituted by the framework. To stand outside the framework is not to access neutral reason. It is to do something other than law.</p>

<p>By the 16th century, Sunni jurists had largely concluded that <em>ijtih&#257;d</em> was no longer warranted in routine cases; subsequent jurists were expected to follow precedent (<em>taql&#299;d</em>). When 19th-century reformers called for ijtihad to reopen, they were not proposing to abandon the four sources to access raw reason. They were proposing that lawful cognition meant continuing the tradition with renewed independence inside it. The framework was never an option to subtract.</p>

<p>Modern Anglo-American common law has the same structure under different theology. Common law reasoning happens through precedent. There is no "judge in the abstract" who reasons without case law and then gets corrected by it. The case law is what reasoning is.</p>

<h2>Where the inseparability comes from</h2>

<p>The technical name for this in cognitive science is <em>predictive processing</em>. In Karl Friston's free-energy formulation<sup><a href="#cite-8" class="cite-marker">[8]</a></sup>, perception is not a sensor reading that gets interpreted; it is the resolution of a prior expectation against incoming evidence. The system <em>is</em> a generative model that runs backward &mdash; guessing what would produce the inputs &mdash; in order to perceive at all. Andy Clark<sup><a href="#cite-9" class="cite-marker">[9]</a></sup> presses the implication: with no prior, no perception. Not perception with errors. Not noisy perception. <em>No perception.</em></p>

<p>When you turn the prior knob to zero in any actual Bayesian inference, you do not get neutrality. You get the maximum-entropy prior, which is itself a strong prior &mdash; the prior that all hypotheses are equally probable. There is no off. Even silence is an instrument.</p>

<p>The earlier propaganda essay treated priors as knobs that one entity (a propagandist) could turn on a different entity (a recipient). The witnesses say no. The recipient <em>is</em> the priors. Edit them and you have edited the perceiver.</p>

<h2>What changes</h2>

<p>If priors and perceivers are inseparable, three things follow.</p>

<p><strong>Deprogramming is the wrong frame.</strong> There is nothing to roll back to. A person whose priors were shaped by twenty years of state imagery cannot be returned to a pre-imagery self by removing the imagery prior. That self does not exist. What can happen is something stronger and weirder: the priors can be replaced by competing ones, through immersion in a rival generative model. This is what "rebuilding" means in practice. It is closer to <a href="/blog/why-reading-happens-twice/">reading happening twice</a> &mdash; running the cognition through a different generative model and letting the substrate gradually reshape &mdash; than to subtraction.</p>

<p><strong>"Are you free of bias?" is malformed.</strong> The right question is <em>which</em> priors are running you, and are they the ones you would choose if you could see them? In the <a href="/blog/ideasthesia-and-the-stoic-gap/">Stoic decomposition exercise</a>, I treated phantasiai as separable from synkatathesis &mdash; strip the affective framing, the bare description remains. That essay's phenomenology still holds, but its background metaphor was too clean. The Stoic exercise is not separation. It is replacement. You substitute one generative model for another and notice the difference.</p>

<p><strong>The <a href="/blog/the-counter-ledger/">Counter-Ledger</a> is itself a prior.</strong> The brain's running estimate of how costly it would be to resolve a contradiction is not measured in some prior-free unit. It is measured in disturbance the revision would create across the rest of the priors. Which is why entrenched beliefs are entrenched: not because they are stickier, but because their removal would cascade. The Counter-Ledger is a meta-prior about which priors can be cheaply moved. Asymmetric like everything else.</p>

<h2>The remaining open question</h2>

<p>If the cognizer is the priors, what is the agent? The thing that decides which tradition to immerse in, which case law to follow, which sources to trust &mdash; does it exist anterior to the priors it then commits to?</p>

<p>The honest answer is: probably not, or only as a small node, like the octopus's central brain. The decision to switch traditions is itself made through some prior architecture. The agent is not nothing, but it is not a clean cause of its own priors either. It is more like a gradient step than a designer.</p>

<p>Which is why the right defense against propaganda is not deprogramming, and not even vigilance. It is the deliberate cultivation of competing generative models, run in parallel, until the disagreement between them becomes loud enough to be heard. You cannot hear yourself thinking unless something else is also thinking nearby.</p>"""

CITATIONS = [
    {"num": 1, "authors": "Hochner, B.", "title": "How nervous systems evolve in relation to their embodiment: what we can learn from octopuses and other molluscs", "year": 2012, "venue": "Brain, Behavior and Evolution 82(1)"},
    {"num": 2, "authors": "Sumbre, G., Gutfreund, Y., Fiorito, G., Flash, T., Hochner, B.", "title": "Control of octopus arm extension by a peripheral motor program", "year": 2001, "venue": "Science 293(5536)"},
    {"num": 3, "authors": "Encyclopaedia Britannica", "title": "Octopus", "year": 2026, "venue": "britannica.com", "url": "https://www.britannica.com/animal/octopus-mollusk"},
    {"num": 4, "authors": "McMahan, B., Ramage, D.", "title": "Federated Learning: Collaborative Machine Learning without Centralized Training Data", "year": 2017, "venue": "Google Research Blog", "url": "https://research.google/blog/federated-learning-collaborative-machine-learning-without-centralized-training-data/"},
    {"num": 5, "authors": "Karimireddy, S. P., Kale, S., Mohri, M., Reddi, S. J., Stich, S., Suresh, A. T.", "title": "SCAFFOLD: Stochastic Controlled Averaging for Federated Learning", "year": 2020, "venue": "ICML 2020"},
    {"num": 6, "authors": "Encyclopaedia Britannica", "title": "Usul al-fiqh", "year": 2026, "venue": "britannica.com", "url": "https://www.britannica.com/topic/usul-al-fiqh"},
    {"num": 7, "authors": "Encyclopaedia Britannica", "title": "Ijtihad", "year": 2026, "venue": "britannica.com", "url": "https://www.britannica.com/topic/ijtihad"},
    {"num": 8, "authors": "Friston, K.", "title": "The free-energy principle: a unified brain theory?", "year": 2010, "venue": "Nature Reviews Neuroscience 11(2)"},
    {"num": 9, "authors": "Clark, A.", "title": "Whatever next? Predictive brains, situated agents, and the future of cognitive science", "year": 2013, "venue": "Behavioral and Brain Sciences 36(3)"},
]
