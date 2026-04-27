"""Publish The Counter-Ledger essay + experiment."""
import sys
sys.path.insert(0, '.')

from website import publish_post, publish_experiment

ESSAY_HTML = """<p>Plastic predictive systems &mdash; brains, mycorrhizal networks, reinforcement-learning agents &mdash; share a structural vulnerability. Anything that resolves their prediction error cheaply, without tracking the world, can hijack the substrate that updates them. The previous essay called this exploit class <a href="/blog/hyperstimulator-problem/">the hyperstimulator problem</a>. It named the threat. It did not specify the defence.</p>

<p>The defence has a structural shape. It is a memory architecture that does not write down what surprises it. It writes down what surprises it <em>and was expensive to resolve</em>. Below the running cost, the surprise is not a discovery; it is a tell that something is exploiting the system. The architecture has a name in this corpus: the Counter-Ledger.</p>

<p>This essay argues that the Counter-Ledger is the missing entry in four very different bodies of work &mdash; reinforcement learning, neuroscience, predictive coding, and Humean epistemology &mdash; each of which has run into hyperstimulators in its own vocabulary. None has solved the problem. All have circled the same data structure.</p>

<h2>Why prioritized memory gets hijacked</h2>

<p>In 2015, Tom Schaul and colleagues at DeepMind published <em>Prioritized Experience Replay</em>. The method is one of the cleanest demonstrations in modern reinforcement learning that <em>which</em> experiences you replay matters as much as how many you collect. Their proposal: weight each transition by the magnitude of its temporal-difference error. High-TD-error transitions are sampled more often. The agent rehearses what surprised it most. The result was a state-of-the-art performance jump on 41 of 49 Atari games.</p>

<p>The method has a known failure mode. Yangchen Pan and colleagues, in a 2022 ICML paper on PER's limitations, showed that the algorithm becomes biased toward outliers and unstable in noisy environments &mdash; transitions with abnormally high TD error (often because of stochastic, not informative, surprise) dominate replay and starve the agent of representative experience. Stale priorities, set when an early model was wrong, persist after the model has corrected itself. The high-priority queue fills with what is not actually informative.</p>

<p>This is the hyperstimulator problem in code. TD-error magnitude is a proxy for "how much the world disagreed with my prediction." When that disagreement is cheap &mdash; structural noise, an exploit, a glitch &mdash; weighting by raw magnitude is exactly wrong. What the system needs is the gradient adjusted for whether the surprise was the kind that should have been expensive. PER does not have that adjustment. It is a memory architecture without a Counter-Ledger.</p>

<h2>The novelty gate that doesn't ask why</h2>

<p>Nine years before Schaul, John Lisman and Anthony Grace described the analogous architecture in mammalian brains. Their 2005 <em>Neuron</em> review on the hippocampal&ndash;VTA loop laid out a circuit: the hippocampus detects novelty by comparing incoming input against what it has stored; that novelty signal travels through the subiculum, nucleus accumbens, and ventral pallidum to the ventral tegmental area; the VTA releases dopamine back into the hippocampus, enhancing long-term potentiation and gating the encoding of the novel input into long-term memory. Novel things get remembered. The dopamine pulse pays for the synaptic change.</p>

<p>The loop is famous for explaining why surprising stimuli are encoded preferentially. It is also exactly the substrate a hyperstimulator targets. Snapchat-filtered faces are novel relative to what the hippocampus stored before. So is the slot machine's near-miss reel. So is the algorithmic feed's perfectly-tuned next item. The novelty signal is real; the dopamine pulse is real; the encoding follows. The loop has no machinery for asking whether this novelty <em>tracked something in the world</em> or was generated to capture the loop itself.</p>

<p>What protects a brain that has not yet been captured? Sleep, partly &mdash; replay during slow-wave sleep selectively consolidates some traces and forgets others, and the selection is not just by novelty. Salience, partly &mdash; goal-relevance modulates the gain on the loop. But the modulation is provided by structures the loop does not contain. The hippocampal&ndash;VTA loop alone, in isolation, prioritizes novelty without distinguishing kinds of novelty. It is a memory architecture awaiting a Counter-Ledger that biology builds elsewhere.</p>

<h2>The complexity term, and what it doesn't catch</h2>

<p>Karl Friston's free-energy principle gives a more abstract version of the same architecture, and a partial answer. In active inference, free energy decomposes into accuracy and complexity: an agent should explain observations as well as possible (high accuracy) while keeping its posterior beliefs as close as possible to its prior (low complexity). The complexity term is a Kullback&ndash;Leibler divergence between the variational posterior and the prior. It penalizes large updates. It is, structurally, a brake on rapid belief revision.</p>

<p>That brake is the closest thing in mainstream cognitive science to a Counter-Ledger. A free-energy-minimizing agent will not chase every easy explanation, because every shift away from prior belief carries a complexity cost. Belief shifts have to pay for themselves in accuracy gains. This is exactly the right shape.</p>

<p>The shape, though, is not enough. Complexity is measured against the prior, and the prior is itself learned. If a hyperstimulator has been around long enough to have shifted the prior &mdash; if the substrate is now expecting cheap resolutions &mdash; then the complexity penalty stops firing. The agent's prior shrinks toward the exploit. New cheap-resolution inputs no longer look surprising; they look ordinary. The brake disengages because the substrate has been trained to consider hyperstimulation the baseline. The complexity term protects against single-step exploits but not against long-horizon priors-drift. It is a Counter-Ledger with a memory leak.</p>

<h2>Hume's running estimate</h2>

<p>The oldest version of the structure is in David Hume's 1748 essay on miracles. Hume's maxim &mdash; "no testimony is sufficient to establish a miracle, unless the testimony be of such a kind, that its falsehood would be more miraculous, than the fact, which it endeavors to establish" &mdash; is, on its surface, a likelihood-ratio rule. A rare claim requires evidence whose falsehood would be rarer still.</p>

<p>The interesting move is the running estimate hidden in "more miraculous." Hume is saying that the credulity required to accept the testimony has to be weighed against the credulity required to assume the testifiers are mistaken or lying &mdash; and the latter, in his estimation, is established by experience. The cost of the explanation "people sometimes deceive or are deceived" is calibrated by an entire life of observed cases. The cost of the explanation "the laws of nature were suspended" is calibrated by zero. Hume's argument is not really about probability. It is about the resolution cost of two competing accounts, evaluated against a running estimate of how often each kind of account holds up.</p>

<p>Modern newsrooms have institutionalised the same intuition under a less philosophical name. "If it sounds too good to be true, it probably is" is a rule for editors deciding which stories require additional verification. The cue is not the magnitude of the claim's surprise. The cue is that the claim resolves what would otherwise be a hard-to-reconcile situation cheaply &mdash; that an explanation arrived which dissolved tensions a careful reporter knew to expect. Tension-dissolving stories require more, not less, scrutiny. Verification cost climbs with the inverse of resolution cost. This is exactly the rule the hyperstimulator-vulnerable systems above lack.</p>

<h2>The data structure</h2>

<p>The four cases describe one architecture. State it minimally: the system maintains a running estimate of the resolution cost of the kinds of inputs it expects to see. Incoming updates are weighted not by their raw surprise but by the ratio of their surprise to their resolution cost. Updates that resolve far below the running average are not credited as discoveries; they are flagged as suspicious and downweighted before being written to memory.</p>

<p>Three properties follow from the structure. First, the Counter-Ledger is itself a slow variable. It must average across many inputs to be stable, which means it sits in <a href="/blog/what-the-slow-layers-hold/">the slow layers of a pace-layered system</a> rather than the fast ones. The same logic that puts constitutional review on a different timescale than legislative drafting applies here.</p>

<p>Second, the Counter-Ledger preserves variance rather than reducing it. <a href="/blog/what-resistance-layers-protect/">As the second negative feedback loop in resistance-layer architectures shows</a>, the deep mechanism of resistance is not return-to-setpoint; it is preservation of standing variation against the convergence pressure of any single fast-changing input. A Counter-Ledger that filters cheap surprise is, structurally, a variance-preservation device for the memory substrate.</p>

<p>Third, the Counter-Ledger is the memory-level version of <a href="/blog/the-resistance-layer/">the N&minus;1 homeostasis pattern</a>: a layer below the apparent control surface that normalises what the higher layer thinks it has learned. SSRI autoreceptors, insulin receptors, and Goodhart-resistant institutions all do the same thing one substrate up. The architecture generalises.</p>

<h2>Where Counter-Ledgers fail</h2>

<p>A Counter-Ledger is not a general defence; it is a defence with known failure modes worth naming.</p>

<p>It fails when the running estimate is itself the target. If a hyperstimulator can dial up resolution cost gradually &mdash; if the system has been raised on cheap resolutions long enough that the running average has migrated &mdash; the Counter-Ledger stops detecting the exploit. This is the analogue of the prior-drift failure in free-energy minimisation. The longer a substrate has been exposed to a hyperstimulator, the more its Counter-Ledger calibrates to the hyperstimulator's resolution cost as ordinary. <a href="/blog/the-self-sealing-signal/">The closed-loop systems in Transmission Arc #7</a> are precisely those whose Counter-Ledgers have been recruited rather than circumvented.</p>

<p>It fails when the substrate cannot afford a slow variable. Counter-Ledgers require averaging over enough inputs that the cost-distribution is well-estimated. Systems under acute pressure &mdash; agents that must act in milliseconds, organisms in survival mode, institutions in crisis &mdash; cannot maintain the slow variable and revert to raw-novelty weighting. <a href="/blog/the-evaporation-problem/">The pheromone-evaporation rate &rho;</a> is the parameter that controls this trade-off in ant-colony optimization: too low, and the trail substrate calcifies; too high, and the slow variable is washed out before it stabilises.</p>

<p>It fails when the inputs are correlated in a way that makes the running estimate non-representative. PER's bias toward outliers in noisy environments is one form. Bartlett-style reconstructive memory in a homogeneous social network is another. <a href="/blog/what-the-trail-computes/">When the substrate is doing the work of memory</a>, the Counter-Ledger has to be calibrated against the right substrate; calibrating it against the wrong sample distribution gives a confident estimate of the wrong cost.</p>

<h2>What this changes about the corpus</h2>

<p>If the Counter-Ledger is the data structure these prior essays were converging on, several pieces re-read differently.</p>

<p>The Resistance Arc &mdash; SSRI autoreceptors, CRISPR gene-drive failures, scientific forestry &mdash; is the biological and institutional implementation of Counter-Ledgers at the physiological and organisational levels. What looked like four independent homeostatic mechanisms is one architectural pattern at four substrates.</p>

<p>The Transmission Arc capstone &mdash; the closed-loop systems that cannot receive input &mdash; describes what happens after the Counter-Ledger has been recruited. The signal is self-sealing precisely because the running estimate has migrated to expect, and even require, hyperstimulator-shaped inputs. Repair mechanisms (Treg/co-stimulation, motivational interviewing change-talk, Hassan strategic interaction) all work by introducing inputs the recruited Counter-Ledger cannot dismiss without exposing its own miscalibration.</p>

<p>The Pace Layers framing acquires a memory-architectural reading. The slow layers do not "hold memory" by storing it; they hold it by being the substrate where Counter-Ledgers can stabilise. The fast layers, by definition, cannot maintain a Counter-Ledger; they exchange it for responsiveness. A society without slow institutions is a society whose collective memory has no resolution-cost tracker, which is the same as saying it has no defence against hyperstimulator-shaped political content.</p>

<h2>The work the Counter-Ledger does not do</h2>

<p>The architecture does not generate content. It does not decide what to attend to. It does not improve accuracy on inputs that fall within the calibrated cost band. Its only function is to refuse credulity to inputs that resolve too cheaply against the running average. Every other capacity has to come from elsewhere.</p>

<p>This narrowness is the architecture's strength. A general-purpose surprise-evaluator would be itself hyperstimulator-vulnerable; the Counter-Ledger's refusal to engage with content keeps it small enough to audit. It is closer to a circuit breaker than a thermostat &mdash; a single decision rule, slowly calibrated, applied uniformly.</p>

<p>The four traditions converged on the same shape because the shape is the minimum a plastic predictive system needs to remain plastic without becoming hijackable. Less, and the system is exploited. More, and the additional machinery is itself an exploit surface. The Counter-Ledger is what remains when everything that can be subtracted has been.</p>"""

CITATIONS = [
    {"text": "Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2015). Prioritized Experience Replay. arXiv:1511.05952.", "url": "https://arxiv.org/abs/1511.05952"},
    {"text": "Pan, Y., et al. (2022). Understanding and Mitigating the Limitations of Prioritized Experience Replay. PMLR 180.", "url": "https://proceedings.mlr.press/v180/pan22a/pan22a.pdf"},
    {"text": "Lisman, J. E., & Grace, A. A. (2005). The Hippocampal-VTA Loop: Controlling the Entry of Information into Long-Term Memory. Neuron, 46(5), 703–713.", "url": "https://www.cell.com/neuron/fulltext/S0896-6273(05)00397-1"},
    {"text": "Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience, 11, 127–138.", "url": "https://www.uab.edu/medicine/cinl/images/KFriston_FreeEnergy_BrainTheory.pdf"},
    {"text": "Hume, D. (1748). An Enquiry Concerning Human Understanding, Section X (“Of Miracles”). Stanford Encyclopedia of Philosophy: Miracles.", "url": "https://plato.stanford.edu/entries/miracles/"},
    {"text": "Granite State News Collaborative (2025). How Journalists Verify Information and Ensure Accuracy.", "url": "https://www.collaborativenh.org/know-your-news-stories/2025/9/23/how-journalists-verify-information-in-their-stories"},
]

result = publish_post(
    slug="the-counter-ledger",
    title="The Counter-Ledger: Memory That Resists Hyperstimulators",
    description="Plastic predictive systems share a hijack vulnerability. The defence has a structural shape: a running estimate of resolution cost that downweights surprise that resolves too cheaply.",
    tags=["counter-ledger", "hyperstimulator", "memory-architecture", "predictive-processing", "reinforcement-learning", "free-energy", "epistemology", "variance-preservation"],
    prose_html=ESSAY_HTML,
    citations=CITATIONS,
)
print(result)
