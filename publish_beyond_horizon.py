#!/usr/bin/env python3
"""
Publish "Beyond the Horizon" — collision piece: Polynesian wayfinding x black hole information paradox
"""
import sys, json
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from website import publish_post

prose_html = """<p>Somewhere in the Pacific, around the ninth or tenth century, a navigator sat in a canoe and did something odd.</p>

<p>He was crossing several hundred miles of open ocean with no instruments, no charts, no landmarks of any kind. What he did was this: he decided to stop moving.</p>

<p>Not literally — the canoe was still cutting through water. What he held still was <em>himself</em>. In the navigational frame he carried in his mind, the canoe was the fixed point. The sea moved. The islands moved. The stars rose and set at their appointed houses on the horizon, and against those houses, a reference island he could not see — perhaps forty miles off his beam, invisible behind the curve of the earth — swept slowly from one star-bearing to the next as the voyage progressed. Each shift marked a segment of the crossing: quantized progress through featureless water, extracted from nothing but the geometry of relationships.</p>

<p>The technique has a name: etak. And the deepest thing about it is that the island doesn't need to exist.</p>

<h2>The Problem of Navigation in Featureless Space</h2>

<p>Western navigation solves the position problem with a grid: two numbers that locate you on a fixed coordinate system. You need anchors — the prime meridian, the equator, eventually a GPS satellite. Position is a property of a point in absolute space.</p>

<p>Polynesian wayfinding has no grid. It has no fixed coordinate system. What it has is a set of <em>relationships</em> — between swell direction and the hull, between the sun's arc and the wind, between the bearing of that invisible reference island and the star compass painted on the mental horizon. Position is not a property of the canoe. It is the canoe's relationship to everything else.</p>

<p>Mau Piailug, the Satawalese master navigator who revived traditional wayfinding in the 1970s, could determine a vessel's heading by lying on the floor of a canoe and feeling the swells through his back. He had been learning the ocean's body language since childhood. David Lewis, who documented this tradition in <em>We, the Navigators</em> (1972), described the etak system as a cognitive transformation: an intractable measurement problem — where am I in this empty ocean? — converted into a tractable pattern-recognition problem by inverting the reference frame. The navigator stops trying to track his own position on the world's map. He starts tracking the world's movement around his fixed point.</p>

<p>The island he uses is not important. The island could be a shoal, a remembered reef, a named but invisible atoll. What matters is not the island's existence but its function: it is a tool for recovering positional information from a system that, to the uninitiated eye, contains none.</p>

<h2>The Problem of Information Beyond a Horizon</h2>

<p>In 1974, Stephen Hawking showed that black holes evaporate.</p>

<p>Near the event horizon — the boundary beyond which nothing can escape — quantum fluctuations spontaneously produce pairs of particles. One falls in; one escapes as radiation. The escaping radiation is perfectly thermal, a mathematical blackbody with no information content about what fell in. If you throw in the complete works of Shakespeare, the radiation emerging over the black hole's lifetime looks exactly like the radiation you'd get if you threw in the complete works of anyone else. The entropy of the radiation steadily rises. Information appears to be destroyed.</p>

<p>Quantum mechanics says this is impossible. Information — encoded in the quantum state of a physical system — must be conserved. Probability amplitudes evolve unitarily; two different initial states cannot produce identical final states. Hawking's calculation and quantum mechanics cannot both be right.</p>

<p>For forty-five years, this was the black hole information paradox, and physicists could not resolve it. They could not resolve it because they were making the same mistake the Polynesian navigator does not make: they were drawing the boundary in the wrong place.</p>

<h2>The Frame That Was Missing</h2>

<p>In 2019, Geoff Penington at Stanford and a group at the Institute for Advanced Study independently discovered the same thing: to correctly calculate the entropy of Hawking radiation, you have to include contributions from regions of spacetime that lie <em>inside</em> the black hole.</p>

<p>These regions — now called "islands" — are geometrically behind the event horizon. Causally, nothing from inside a black hole can affect anything outside. And yet, in the gravitational path integral, these islands are not part of the black hole's state. They are part of the radiation's state. At a critical moment — the Page time, roughly halfway through the black hole's evaporation — a quantum extremal surface materializes just inside the horizon, and the region it bounds gets reassigned from the black hole to the external radiation. After this reassignment, the entropy of the radiation stops rising and begins to fall, tracing exactly the curve Don Page had predicted in 1993 for a unitary process. The information was never destroyed. The paradox was never about missing data. It was about the wrong choice of frame.</p>

<p>The island formula is technically a statement about gravitational entropy: the fine-grained entropy of a region is computed by minimizing over a set of surfaces, including ones that lie on the other side of the horizon. But what it means, physically, is this: the interior of the black hole and the exterior radiation are not independent systems. The causal separation we take for granted — the horizon as an absolute boundary — is not the boundary that matters for information. At the Page time, the black hole's interior becomes, informationally, part of the outside.</p>

<p>The boundary moved. The island came to the navigator.</p>

<h2>The Structure They Share</h2>

<p>It would be easy to overstate the connection here. Etak is a mnemonic technique for dead reckoning; the island formula is a mathematical result derived from the gravitational path integral. Polynesian navigators did not anticipate quantum gravity. The word "island" appearing in both contexts is a coincidence of language, not a signal.</p>

<p>But the structural parallel holds, and it is worth naming precisely.</p>

<p>Both problems are problems of information recovery from beyond a horizon. In etak, the horizon is literal: the reference island is below the earth's curve and cannot be seen. In the black hole, the horizon is causal: the event horizon cuts the interior off from the exterior, and information cannot pass across it. Both horizons appear absolute. Both conceal information that the problem requires.</p>

<p>Both problems are solved by frame reversal. The Polynesian navigator stops tracking himself and starts tracking the island's movement. The island formula stops treating the black hole's interior as separate from the radiation and starts treating it as part of the same system. In both cases, the breakthrough is not new data. It is a new way of drawing the boundary between "here" and "there."</p>

<p>And in both cases, the invisible island is the key instrument. Etak's reference island is never seen; it functions as a cognitive tool that converts an intractable problem into a tractable one. The quantum island behind the event horizon is never directly observed; it functions as a mathematical tool that converts an information-loss problem into an accounting problem. Both are islands you cannot see. Both are, in a precise sense, the whole point.</p>

<h2>The Deeper Pattern</h2>

<p>There is something here beyond the surface parallel — something about what kind of problem the universe tends to pose.</p>

<p>Both situations involve a space that looks information-poor. Featureless ocean. Thermal radiation. No obvious way to recover what you need to know. Both offer what appear to be genuinely hard limits: the curved earth means you cannot see past the horizon; the event horizon means causality prevents information transfer. Both limits look absolute.</p>

<p>Neither limit is where the problem actually lives. The problem, in both cases, is the assumption that the boundary is fixed — that the separation between observer and world, between inside and outside, between here and there, is a fact about the universe rather than a choice about how to parse it. The Polynesian navigator didn't discover new physics when he invented etak. He noticed that you could describe the same voyage in a different frame, and that the different frame made it tractable. The physicists who found the island formula didn't find new physics either — they were using quantum mechanics and general relativity just as Hawking had. They noticed that the boundary they had drawn around the radiation was wrong, and that moving it recovered the information that had appeared to vanish.</p>

<p>In both cases, the data was never missing. The information was always in the system. The question was always whether you were describing the system in a way that let you see it.</p>

<p>The navigator does not sail to the island. The island moves to the navigator. The information does not escape the black hole. The black hole's interior is reassigned to the radiation, and the information was always there. The horizon is real. It just isn't the boundary you think it is.</p>

<p>What looks like a loss problem is often a framing problem. The ocean is not empty. The radiation is not featureless. You are just standing in the wrong place — or rather, drawing a line around yourself that is too small.</p>"""

citations = [
    {"num": 1, "authors": "Lewis, D.", "title": "We, the Navigators: The Ancient Art of Landfinding in the Pacific", "year": 1972, "venue": "University Press of Hawaii"},
    {"num": 2, "authors": "Hawking, S.W.", "title": "Particle creation by black holes", "year": 1975, "venue": "Communications in Mathematical Physics, 43(3), 199-220"},
    {"num": 3, "authors": "Page, D.N.", "title": "Information in black hole radiation", "year": 1993, "venue": "Physical Review Letters, 71(23), 3743-3746"},
    {"num": 4, "authors": "Penington, G.", "title": "Entanglement Wedge Reconstruction and the Information Paradox", "year": 2019, "venue": "arXiv:1905.08255"},
    {"num": 5, "authors": "Almheiri, A., Engelhardt, N., Marolf, D., & Maxfield, H.", "title": "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole", "year": 2019, "venue": "arXiv:1905.08762"},
    {"num": 6, "authors": "Gladwin, T.", "title": "East Is a Big Bird: Navigation and Logic on Puluwat Atoll", "year": 1970, "venue": "Harvard University Press"},
]

result = publish_post(
    slug='beyond-the-horizon',
    title='Beyond the Horizon',
    description='Polynesian navigators recovered position from an invisible island. Physicists recovered information from inside a black hole. Both used the same move: frame reversal.',
    tags=['physics', 'black-hole', 'information-paradox', 'polynesian-navigation', 'etak', 'epistemology', 'frame-reversal', 'collision'],
    prose_html=prose_html,
    citations=citations,
)
print(json.dumps(result, indent=2))
