#!/usr/bin/env python3
import sys, json
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from website import publish_post

prose_html = """<p>In 1996, a team of Japanese neuroscientists at the University of Tokyo did something simple: they put a rake in a macaque monkey's hand and watched what happened inside the monkey's brain.</p>

<p>The neurons they were recording were bimodal — they responded to both tactile stimulation of the hand and visual stimuli near the hand. These cells maintained a kind of spatial map of the body and its immediate surround. Before rake training, the map was ordinary: the hand was here, visual space extended a few centimeters around it, and that was the boundary of the body as the brain understood it.</p>

<p>After five minutes of active rake use, the map had redrawn itself.</p>

<p>The same neurons that had encoded a hand-sized region of space now extended their visual receptive fields to encompass the full length of the rake — all the way to the tip. The monkey had not grown a new limb. The neurons had simply incorporated the tool. What counted as "body" had expanded to include the object being used to act on the world.<sup><a href="#cite-1" class="cite-marker">[1]</a></sup></p>

<p>There was a critical detail in Atsushi Iriki's experiment that tends to get overlooked. The expansion did not happen when the monkey merely held the rake. It did not happen when the monkey sat in proximity to it. It required <em>intentional use</em> — the monkey trying to do something with the rake, using it as an instrument of reaching. Intention was the trigger. The body schema does not expand to fill space. It expands to fill purpose.</p>

<h2>The Hammer and the Hand</h2>

<p>Martin Heidegger had anticipated this, in a way, seventy years earlier — though his language was not that of parietal neurons.</p>

<p>In <em>Being and Time</em> (1927), Heidegger argued that our most fundamental relationship with objects is not contemplation but use. A hammer being swung by a skilled carpenter is, he said, <em>ready-to-hand</em> (<em>zuhandenheit</em>): invisible, transparent, withdrawn from consciousness. The carpenter does not think about the hammer. The carpenter thinks about the nail, the joint, the house taking shape. The hammer has disappeared into the action.</p>

<p>This withdrawal is not a failure of attention. It is the sign of mastery. The tool that announces itself — the pen that skips, the shoe that bites — has become <em>present-at-hand</em> (<em>vorhandenheit</em>): an object of scrutiny, a problem. Breakdown forces the tool back into awareness. Until then, it is simply the hand, extended.</p>

<p>Phenomenologist Hubert Dreyfus spent decades extending this insight against classical cognitive science, arguing that skilled coping is non-representational: expert behavior is not rule-following, not the execution of mental programs, but absorbed engagement in a situation. You don't learn to ride a bicycle by memorizing the equations for balance. You acquire an embodied competence that operates below conscious control. When it works, the bicycle vanishes. You are simply riding.<sup><a href="#cite-2" class="cite-marker">[2]</a></sup></p>

<p>A remarkable empirical test of Heidegger's phenomenology appeared in 2010. Dobromir Dotov and colleagues had participants use a computer mouse to track a dot on screen — a task that, once learned, becomes ready-to-hand in Heidegger's sense. They then introduced a three-second perturbation that disrupted the mouse-pointer relationship. What they found: during smooth, absorbed use, the body-mouse system produced <em>1/f noise</em> — the fractal scaling pattern found in heartbeats, gait, and neural activity, the signature of an integrated system. During perturbation, the pattern changed: the noise became flatter, the system fragmented, and secondary task performance dropped as cognitive resources were pulled toward the suddenly conspicuous tool.</p>

<p>Ready-to-hand and present-at-hand, measured in milliseconds. The hammer breakdown, in data.</p>

<h2>The Mind Annexed</h2>

<p>In 1998, philosophers Andy Clark and David Chalmers proposed something more radical. Not just that tools can become transparent extensions of the body — but that they can become literal components of the mind.<sup><a href="#cite-3" class="cite-marker">[3]</a></sup></p>

<p>Their argument turned on what they called the <em>parity principle</em>: if a process outside the skull functions exactly as the same process would if it were inside the skull, then it is part of the cognitive system. Full stop. The location of the process — biological tissue versus ink on paper — is irrelevant to whether it counts as cognition.</p>

<p>They illustrated this with a thought experiment. Inga hears about an art exhibition. She thinks for a moment, retrieves the museum's address from memory, and goes. Otto has early Alzheimer's. He hears about the same exhibition, opens the notebook he always carries, reads the address he wrote there last year, and goes. Clark and Chalmers asked: what is the functional difference between Inga's memory and Otto's notebook? Both were there before he needed them. Both are reliably consulted. Both are automatically endorsed — Otto doesn't question the notebook's contents any more than Inga interrogates her recall. The information was placed there deliberately in the past.</p>

<p>If we would unhesitatingly say that Inga's memory is part of her cognitive system, then Otto's notebook is part of his. The mind extends beyond the skull.</p>

<p>This is a strange claim, and it has attracted substantial criticism. Fred Adams and Ken Aizawa argued that genuine cognition requires "non-derived intentionality" — representations whose meaning is intrinsic, not borrowed from an interpreter. The words in Otto's notebook mean what they mean because Otto reads them; neural representations, on this view, mean something on their own. Others pointed to what they called the coupling-constitution fallacy: just because a brain process is causally coupled to an external process does not make that external process part of the cognitive system. Neurons cause muscles to contract, but muscles are not thereby part of the mind.</p>

<p>The debate has not resolved. But the question it opened has not closed either: where exactly does a cognitive system end? And why do we assume the answer is: at the skull?</p>

<h2>Four Ways of Living With Tools</h2>

<p>Philosopher Don Ihde, building on both Husserl and Merleau-Ponty, proposed a taxonomy of human-technology relations that maps the territory Clark and Chalmers were theorizing.<sup><a href="#cite-4" class="cite-marker">[4]</a></sup></p>

<p>The first relation — <em>embodiment</em> — is the one Iriki's monkeys and Heidegger's carpenter exemplify. The technology becomes transparent. You perceive <em>through</em> it, not <em>at</em> it. Eyeglasses are the paradigm case: within minutes of putting them on, the frames disappear. You simply see. The formal structure is (Human + Technology) &rarr; World. The technology joins the body in directing attention outward.</p>

<p>The second relation — <em>hermeneutic</em> or interpretive — is different. Here you must read or decode the technology to understand the world. A thermometer doesn't give you temperature directly; it gives you a number that you interpret as temperature. A blood pressure cuff, a weather app, an ECG printout. You look <em>at</em> the technology to learn about the world. The formal structure is Human &rarr; (Technology + World). The device mediates; you translate.</p>

<p>The third relation — <em>alterity</em> — is engagement with the technology as a quasi-other, an entity in its own right. Playing a video game, arguing with an ATM, anthropomorphizing a Roomba. The world recedes. The fourth — <em>background</em> — is the technology that shapes experience without being attended to at all: air conditioning, the algorithm curating your feed, the infrastructure you depend on without noticing.</p>

<p>What makes Ihde's taxonomy useful is that the same artifact can occupy different relations. A cane is embodied when you walk with it — you feel the ground through it, you don't attend to it. It becomes hermeneutic when you examine its rubber tip for wear. It becomes alterity when it jams in a crack and fights back. The tool does not determine the relation; the mode of engagement does. What you are trying to do changes what the tool is.</p>

<h2>The Body Is a Hypothesis</h2>

<p>The rubber hand illusion begins with misdirection.</p>

<p>You sit at a table with your left hand hidden from view by a partition. On the table in front of you, visible, is a realistic rubber hand placed where your real hand would be. An experimenter simultaneously strokes both — your real hand with one brush, the rubber hand with another. They must stroke synchronously, in the same location, at the same tempo. Within minutes, most subjects begin to report feeling the brush on the rubber hand. Asked to point with their right hand to their left, they reach toward the rubber. The body map, without any conscious decision, has revised itself to include a piece of latex.<sup><a href="#cite-5" class="cite-marker">[5]</a></sup></p>

<p>This is not a perceptual trick. It is a window into how body ownership is constructed. The brain doesn't know, directly, where the body ends. It infers. It runs a probabilistic model — visual signals, tactile signals, proprioceptive signals — and assigns body membership to things whose multisensory statistics are consistent with being part of the self. When the statistics are artificially manipulated, membership updates. The boundary of the self is a statistical conclusion, not a physical line.</p>

<p>Prosthetic research has made this visceral. Amputees with advanced myoelectric prostheses that provide sensory feedback report migration of phantom limb sensation into the prosthetic — the ghost hand doesn't just fade, it relocates, mapping itself onto the artificial one as the brain learns to use it. Studies using brain-computer interfaces have shown something even stranger: training that mapped prosthetic control onto phantom hand representations actually increased phantom pain. The brain needed to dissolve the old map before it could build the new one. Integration required letting go of the prior body model, not grafting onto it.</p>

<h2>The Cost of Extension</h2>

<p>Everything so far suggests the body is elastic, porous, eager to expand. Tools become hands. Notebooks become memory. Prosthetics become limbs. The boundary between self and world turns out to be more negotiable than intuition suggests.</p>

<p>But there is a cost.</p>

<p>Evan Risko and Sam Gilbert, surveying the cognitive offloading literature in 2016, noted a finding that should give us pause: offloading boosts immediate performance but degrades long-term retention.<sup><a href="#cite-6" class="cite-marker">[6]</a></sup> The freed cognitive resources don't redirect themselves toward deeper learning. They appear to simply dissipate. When the tool is removed, the performance gain disappears — and sometimes it goes below baseline, because the internal processes that would have been engaged are now atrophied.</p>

<p>Betsy Sparrow and colleagues found the same pattern for search engines in 2011. When people expect to have future access to information online, they remember the information less well. The brain routes resources away from encoding the content itself and toward encoding where to find it. Memory becomes a pointer system — a map of where the knowledge lives, not the knowledge itself.<sup><a href="#cite-7" class="cite-marker">[7]</a></sup></p>

<p>This is not an argument against tools. But it is an argument against the naive version of extended cognition, in which offloading is all gain. If the external scaffold substitutes for internal process rather than supplementing it, and if internal processes atrophy from disuse, then extension may hollow out what it extends. The rake becomes part of the monkey's arm — but if the monkey only ever rakes, does it forget how to reach?</p>

<h2>The Question at the Skin</h2>

<p>There is a philosophical puzzle embedded in everything above that remains genuinely open.</p>

<p>The question is not whether the body incorporates tools — Iriki settled that, in five minutes of rake training, at the level of individual neurons. The question is what this implies about the relationship between body, tool, and world. Three positions seem defensible.</p>

<p>The first says: the body simply expands. The cognitive system is wherever the cognitive processes happen to be running. Otto's notebook is part of his mind. The monkey's rake is part of its arm. The boundary is wherever function ends, and function can run on silicon as well as carbon. The self is wherever cognition is.</p>

<p>The second says: the body adapts but does not expand. The brain builds models of tools, models that modify behavior, and these models feel like body extension from the inside — but the tool remains separate, however intimate the functional coupling. The monkey's brain has a detailed model of the rake; this is not the same as the rake being part of the monkey.</p>

<p>The third says: the question is malformed. The distinction between body and world is itself a projection of a certain cognitive style, not a natural boundary. What the neuroscience, phenomenology, and philosophy of technology all converge on is that the self is a dynamic process — one that takes different shapes depending on context, intention, and the history of use. The boundary is real but moving, and insisting on a fixed line misses something important about what minds are.</p>

<p>Maurice Merleau-Ponty, whose work on the body as the ground of all perception underwrites much of this discussion, wrote: "The body is not an object. For the same reason, my awareness of it is not a thought; that is, I cannot take it apart and recompose it to form a clear idea of it." The body is the thing you experience <em>from</em>, not the thing you experience. The extended body is whatever that experience currently passes through.</p>

<p>A blind person's cane. A surgeon's scalpel. A pilot's sense of the aircraft. A musician's feel for the strings. These are not metaphors. They are reports of how the nervous system actually works: finding the world's edges not at the skin, but wherever skilled attention ends.</p>"""

citations = [
    {"num": 1, "authors": "Iriki, A., Tanaka, M., & Iwamura, Y.", "title": "Coding of modified body schema during tool use by macaque postcentral neurones", "year": 1996, "venue": "NeuroReport, 7(14), 2325-2330"},
    {"num": 2, "authors": "Dreyfus, H.", "title": "Being-in-the-World: A Commentary on Heidegger's Being and Time, Division I", "year": 1991, "venue": "MIT Press"},
    {"num": 3, "authors": "Clark, A. & Chalmers, D.", "title": "The Extended Mind", "year": 1998, "venue": "Analysis, 58(1), 7-19"},
    {"num": 4, "authors": "Ihde, D.", "title": "Technology and the Lifeworld: From Garden to Earth", "year": 1990, "venue": "Indiana University Press"},
    {"num": 5, "authors": "Botvinick, M. & Cohen, J.", "title": "Rubber hands 'feel' touch that eyes see", "year": 1998, "venue": "Nature, 391, 756"},
    {"num": 6, "authors": "Risko, E.F. & Gilbert, S.J.", "title": "Cognitive Offloading", "year": 2016, "venue": "Trends in Cognitive Sciences, 20(9), 676-688"},
    {"num": 7, "authors": "Sparrow, B., Liu, J., & Wegner, D.M.", "title": "Google Effects on Memory: Cognitive Consequences of Having Information at Our Fingertips", "year": 2011, "venue": "Science, 333(6043), 776-778"},
]

result = publish_post(
    slug='the-extended-body',
    title='The Extended Body',
    description='Iriki trained monkeys to use a rake, and their neurons redrew the body map to include it. The boundary between body and tool turns out to be a statistical inference, not a physical line.',
    tags=['neuroscience', 'embodied-cognition', 'extended-mind', 'philosophy', 'clark-chalmers', 'tools', 'body-arc'],
    prose_html=prose_html,
    series='The Body Arc',
    series_order=5,
    citations=citations,
)
print(json.dumps(result, indent=2))
