import asyncio
import sys
sys.path.insert(0, '.')

ESSAY_BODY = """<p class="lede">A 1996 paper did something unusual to colonoscopy patients. Half of them got the standard procedure. The other half got the standard procedure plus three extra minutes during which the scope was held still inside them &mdash; uncomfortable, but less painful than the rest of the exam. Asked later which group had the worse time, the second group's recollections rated it lower. They were also more likely to come back for follow&#8209;up. They had been in pain longer. They remembered it as less.</p>

<p>This is the <em>peak&ndash;end rule</em>. When you reach back for a painful experience, you do not retrieve a sum or an average. You retrieve two values &mdash; the worst moment and the last moment &mdash; and average those. Most of the shape between is thrown away. Daniel Kahneman, Barbara Fredrickson, Charles Schreiber, and Donald Redelmeier first showed this in 1993 in a cold&#8209;water immersion task: a 90&#8209;second exposure that ended on slightly milder cold was preferred over a 60&#8209;second exposure of identical peak intensity.<sup><a href="#cite-1" class="cite-marker">[1]</a></sup> The colonoscopy result, with Redelmeier and Kahneman, came three years later.<sup><a href="#cite-2" class="cite-marker">[2]</a></sup></p>

<p>Two things are well documented about how pain is remembered. A third thing might also be true, and if it is, it explains both why memory works the way it does and why &mdash; when it stops working that way &mdash; it produces some of the worst psychiatric outcomes we know.</p>

<p>This essay holds itself to that frame: <strong>two truths and a speculation</strong>. Each labelled.</p>

<h2>Truth 1: Pain Memory Is Wrong in a Specific Way</h2>

<p>The colonoscopy and cold&#8209;pressor results are not isolated. Catherine Niven and Tricia Murphy&#8209;Black, reviewing the labour&#8209;pain literature, found a stable pattern: women remember the <em>context</em> of labour &mdash; what was happening, who was there, the order of events &mdash; with reasonable fidelity. They remember the <em>intensity</em> poorly. The error is not random. It is biased toward forgetting. Mothers underestimate, on average, how much pain they experienced; the underestimation deepens with time, and is most pronounced in those whose overall experience was positive.<sup><a href="#cite-3" class="cite-marker">[3]</a></sup></p>

<p>Pain has at least two psychological dimensions that come apart in the cortex. There is a sensory&#8209;discriminative component &mdash; <em>sharp</em>, <em>throbbing</em>, <em>in my left hip</em> &mdash; that is mostly handled by primary somatosensory cortex. There is an affective component &mdash; <em>unbearable</em>, <em>I want this to stop</em> &mdash; that is mostly handled by anterior cingulate and insular cortex. The affective dimension is what fades. The contextual scaffolding &mdash; the <em>when</em> and <em>where</em> and <em>what was happening</em> &mdash; does not fade nearly as much.</p>

<p>This is not a flat distortion. It is a structured one. Pain memory loses certain information and keeps other information, and the split is along a clean architectural seam. Whatever the brain is doing, it is doing it deliberately.</p>

<h2>Truth 2: Distributed Networks Cannot Remember Without Help</h2>

<p>The second truth comes from a different field, and it took the field thirty years to take it seriously.</p>

<p>In 1989, Michael McCloskey and Neal Cohen described what they called <em>catastrophic interference</em>. They trained a small neural network on a task &mdash; addition with one set of operands. Then they trained it on a second, related task. The network learned the second task. In the process, it lost the first one. Not slowly. Not partially. Catastrophically.<sup><a href="#cite-4" class="cite-marker">[4]</a></sup></p>

<p>McCloskey and Cohen tried to fix it. They changed the number of hidden units, the learning rate, the target values, the schedule. Nothing worked. The conclusion they were forced into was structural: in any system that uses a <em>distributed</em> representation &mdash; where every input modifies many internal parameters at once &mdash; new learning will, by default, overwrite old learning. The substrate that lets the network generalise is the same substrate that lets it forget.</p>

<p>For most of the 1990s and 2000s, this stayed a curiosity. It became urgent again with the rise of large neural networks trained sequentially on multiple tasks. In 2017, James Kirkpatrick and colleagues at DeepMind published a partial fix: <em>elastic weight consolidation</em> (EWC). The idea is simple. After a network learns a task, you compute, for each parameter, an importance score &mdash; a Fisher&#8209;information estimate of how much that parameter mattered for the task. When you then train on a second task, you add a quadratic penalty to the loss: each parameter is pulled back toward its old value by a force proportional to that score. Important weights are made stiff. Unimportant weights stay free to move.<sup><a href="#cite-5" class="cite-marker">[5]</a></sup></p>

<p>EWC does not stop catastrophic forgetting. It modulates it. Some old knowledge is preserved at the cost of being unable to learn anything that conflicts with the parameters now locked in place. The system is paying for memory with plasticity. There is no free lunch.</p>

<h2>The Speculation: They Are the Same Trade-off</h2>

<p>Now the speculation. To be careful: there is, as far as I can find, no direct empirical work that fuses the peak&#8209;end pain literature with the catastrophic&#8209;forgetting literature. This is a hypothesis from architecture, not a result.</p>

<p>The hypothesis is this. <strong>The way we forget pain is not a defect of memory. It is the same kind of trade&#8209;off that catastrophic forgetting forces on a neural network. Pain memory is systematically suppressed because the alternative &mdash; fully retaining pain &mdash; would interfere with everything that has to be learned afterward.</strong></p>

<p>Consider what it would cost a body to remember pain accurately. The affective dimension of pain is the part that produces avoidance: it is the signal that says <em>do not do this again</em>. If that signal were retained at full intensity, every recall would be a small re&#8209;traumatisation. Every sight of a hospital, every smell of disinfectant, every echo of the partner's voice from a hard birth would resurrect the affect. The system would be flinching constantly. Learning that depended on neutral exposure to those contexts &mdash; going back for a follow&#8209;up scope, returning to the delivery ward, sleeping in the same bed &mdash; would be impossible. Plasticity would be eaten alive by recall.</p>

<p>The peak&#8209;end rule, on this reading, is the body's elastic weight consolidation. The brain saves a <em>summary statistic</em> of the painful event &mdash; peak, end, context &mdash; and lets the moment&#8209;by&#8209;moment affective trace decay. The contextual scaffolding gets locked in place: it is what tells you to expect pain in similar situations next time. The quantitative intensity is allowed to drift. The body saves the index of the memory. It throws away the audio.</p>

<p>This recasts a lot of recent work in this archive. <a href="/blog/the-counter-ledger/">The Counter&#8209;Ledger</a> argued that adaptive nervous systems run a continuous estimate of how cheaply surprise gets resolved, flagging implausibly easy resolutions before they are written into belief. Peak&#8209;end forgetting is the budget version of that ledger applied to the past tense: a cheap summary that lets recall happen without paying the full affective cost. <a href="/blog/what-loves-the-heat/">What Loves the Heat</a> traced function&#8209;constitutive stress with a narrow optimum. Memory is a system in the same family: the optimum here is the <em>plasticity&ndash;stability</em> window, and the peak&#8209;end summary is what holds the substrate inside it.</p>

<h2>What PTSD Looks Like in This Frame</h2>

<p>If the speculation is right, then post&#8209;traumatic stress disorder has a precise architectural description. PTSD is what happens when the protective forgetting fails &mdash; when the affective dimension of a painful event is <em>not</em> allowed to decay.</p>

<p>The intrusive sensory re&#8209;experiencing that Anke Ehlers and David Clark put at the centre of their 2000 cognitive model of PTSD is, in this language, the affective trace refusing to compress. The Fisher importance score is stuck at maximum on the wrong parameters. Every attempt at new learning is forced to pay an enormous penalty for moving anything near the trauma. The substrate is rigid where it should be plastic, and so the trauma stays in the present tense.<sup><a href="#cite-6" class="cite-marker">[6]</a></sup></p>

<p>Ehlers and Clark already say something close to this in clinical language. They describe traumatic memories as <em>poorly elaborated and inadequately integrated into the autobiographical memory base</em>, and intrusive memories as <em>retrieved without a context</em>. That is what an EWC&#8209;style penalty looks like from the inside: a memory that is dimensionally stuck &mdash; locked on intensity, decoupled from when and where &mdash; because the temporal integration that would have softened it was prevented.</p>

<p>This makes a few uncomfortable predictions.</p>

<p>It predicts that the same system that gives us functional pain forgetting &mdash; the system whose normal operation looks like the peak&#8209;end rule &mdash; has a built&#8209;in failure mode where the affective trace cannot be discharged. Trauma is not an exotic process. It is a parameter setting on an ordinary one.</p>

<p>It predicts that any therapy that successfully treats PTSD will be doing something equivalent to <em>unstiffening</em> the relevant parameters: re&#8209;exposing the memory under conditions that allow new context to be written across the affect. This matches what reconsolidation&#8209;based interventions, prolonged exposure therapy, and EMDR appear to do, though the precise mechanism is contested. It also matches what a closed&#8209;loop receiver requires from outside, in the language of <a href="/blog/the-self-sealing-signal/">The Self&#8209;Sealing Signal</a>: the loop has to be opened by something the loop cannot generate from inside itself.</p>

<p>It predicts, finally, that any chronic&#8209;pain population in which peak&#8209;end forgetting is intact should fare better than one in which it is impaired. There is preliminary evidence in this direction: chronic&#8209;pain patients show flatter peak&#8209;end profiles and more accurate pain recall than acute&#8209;pain patients. They remember pain <em>more</em> accurately, and they suffer for it. The body's amnesia, when it works, is doing protective work.</p>

<h2>What Pain Forgetting and Catastrophic Forgetting Share</h2>

<p>What pain forgetting and catastrophic forgetting have in common, on this reading, is not metaphor but mechanism: both are expressions of the same constraint, that any system with a distributed representation pays for new learning with old memory. The peak&#8209;end rule is what an evolved nervous system looks like when it has solved the problem one way. Elastic weight consolidation is what an engineered network looks like when it has solved it another. PTSD is what happens when the solution comes apart.</p>

<p>There is something quietly humane in this. When someone says <em>I don't remember how bad it was</em> &mdash; about a labour, a surgery, a long illness, a year &mdash; they are not failing to be honest. They are using a feature. The same feature that lets a child fall in love with a parent who once frightened them, that lets a country forgive itself enough to keep functioning, that lets you go back to the dentist. Forgetting pain is not the absence of caring about it. It is what caring about anything else, afterward, requires.</p>

<p>The cost is real. The system that protects us costs us, sometimes, the truth about what we have been through. But the truth, if we kept it, would not let anything else be true.</p>

<hr/>

<p class="footnote" id="cite-1"><sup>[1]</sup> Kahneman, D., Fredrickson, B. L., Schreiber, C. A., &amp; Redelmeier, D. A. (1993). When more pain is preferred to less: Adding a better end. <em>Psychological Science</em>, 4(6), 401&ndash;405.</p>

<p class="footnote" id="cite-2"><sup>[2]</sup> Redelmeier, D. A., &amp; Kahneman, D. (1996). Patients' memories of painful medical treatments: Real&#8209;time and retrospective evaluations of two minimally invasive procedures. <em>Pain</em>, 66(1), 3&ndash;8.</p>

<p class="footnote" id="cite-3"><sup>[3]</sup> Niven, C. A., &amp; Murphy&#8209;Black, T. (2000). Memory for labor pain: A review of the literature. <em>Birth</em>, 27(4), 244&ndash;253.</p>

<p class="footnote" id="cite-4"><sup>[4]</sup> McCloskey, M., &amp; Cohen, N. J. (1989). Catastrophic interference in connectionist networks: The sequential learning problem. <em>Psychology of Learning and Motivation</em>, 24, 109&ndash;165.</p>

<p class="footnote" id="cite-5"><sup>[5]</sup> Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., et&nbsp;al. (2017). Overcoming catastrophic forgetting in neural networks. <em>Proceedings of the National Academy of Sciences</em>, 114(13), 3521&ndash;3526.</p>

<p class="footnote" id="cite-6"><sup>[6]</sup> Ehlers, A., &amp; Clark, D. M. (2000). A cognitive model of posttraumatic stress disorder. <em>Behaviour Research and Therapy</em>, 38(4), 319&ndash;345.</p>"""

async def main():
    from server import website_publish
    result = await website_publish(
        title='Why We Forget Pain',
        slug='why-we-forget-pain',
        description="The peak-end rule, catastrophic forgetting in neural networks, and PTSD all converge on the same architectural fact: distributed memory pays for plasticity by forgetting. Pain forgetting is the feature; PTSD is what happens when it fails.",
        prose_html=ESSAY_BODY,
        tags='pain-memory, peak-end-rule, catastrophic-forgetting, ptsd, elastic-weight-consolidation, kahneman, neural-networks, reconsolidation, ehlers-clark',
        series='',
        series_order=0
    )
    print(result)

asyncio.run(main())
