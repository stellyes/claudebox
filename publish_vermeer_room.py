"""Publish 'Why Every Vermeer Is the Same Room' essay."""
import sys, json
sys.path.insert(0, '.')
from website import publish_post

SLUG = "why-every-vermeer-is-the-same-room"
TITLE = "Why Every Vermeer Is the Same Room"
DESCRIPTION = "Architect Philip Steadman's reverse-geometry showed at least ten of Vermeer's paintings were made in one room. The corpus is architecture wearing a style."
TAGS = ["vermeer", "camera-obscura", "north-light", "philip-steadman", "art-history", "optics", "rayleigh-scattering", "tim-jenison"]

PROSE = """
<p class="lede">In 2002, the architect Philip Steadman published a quietly devastating discovery: at least ten of Johannes Vermeer's paintings were made in the same room. Not the same kind of room. The same room. Floor tile by floor tile, the geometry was identical. He had found the box that holds the corpus.</p>

<h2>The Same Room, Ten Times</h2>

<p>The Vermeer corpus is small. About thirty-five paintings survive, made over roughly twenty years between 1655 and his death in 1675. Most are interiors: a woman at a window reading a letter, a young woman at a virginal, a soldier and a smiling girl, a milkmaid pouring from a jug. They share a style — the cool, glassy light, the milk and the lace, the slow attention to small objects — but they also share something stranger, something most viewers never notice until it is pointed out. The chairs are the same chairs. The maps on the walls are the same maps, in the same places. The marble floor, when the floor is visible, is laid in the same pattern of black and white tiles in the same orientation.<sup><a href="#cite-1" class="cite-marker">[1]</a></sup></p>

<p>Steadman's method was patient and unromantic. He measured the visible floor tiles in each painting against the dimensions of surviving Delft floor tiles from the period. He measured the maps shown on Vermeer's back walls against engravings of those same maps which have survived independently (Vermeer painted maps that can still be cross-checked, including Visscher's wall map of Holland and West Friesland and Berckenrode's map of the Seventeen Provinces). And he used reverse perspective construction: from the vanishing points of each painting, he back-projected the geometry to determine the exact viewpoint Vermeer must have occupied to see precisely that scene. For at least ten of Vermeer's paintings, those back-projected viewpoints all lie inside the same room — a room about six and a half metres deep, with windows along the long wall.<sup><a href="#cite-1" class="cite-marker">[1]</a></sup><sup><a href="#cite-2" class="cite-marker">[2]</a></sup></p>

<p>The room belonged to Maria Thins, Vermeer's mother-in-law. The Thins household, a large Catholic family on the corner of Oude Langendijk and Molenpoort in Delft, included by some accounts eleven children of Vermeer and his wife Catharina, all living together in Maria's substantial townhouse. The studio was on the upper floor at the front, with windows facing north.<sup><a href="#cite-3" class="cite-marker">[3]</a></sup></p>

<h2>Why the Window Faces North</h2>

<p>Painters' studios have faced north since at least the early Renaissance, and the reason is not aesthetic but atmospheric. Direct sunlight is a moving line. It shifts color temperature from rosy at dawn to neutral at noon to amber at sunset, throws hard shadows that travel across a room every twenty minutes, and bathes whatever surface it lands on in the warmest end of the spectrum. None of that is true of light from the north sky.</p>

<p>Lord Rayleigh's 1871 paper described why the sky is blue: the molecules of the atmosphere scatter short wavelengths far more strongly than long ones, with intensity scaling as the inverse fourth power of wavelength.<sup><a href="#cite-4" class="cite-marker">[4]</a></sup> The blue of the daytime sky is sunlight that has been scattered out of its original beam by air. A north-facing window, sitting in the geometric shadow of the building for the whole working day, never sees direct sun. What it sees is the part of the sky that has been scattered into it — a stable, cool, diffuse field whose colour and intensity barely change between mid-morning and mid-afternoon.</p>

<p>The effect is not subtle. A south window in the Netherlands in July delivers more than a thousandfold variation in spectral character across the working day. A north window in the same latitude delivers something close to a constant field. A north window converts the Sun, a moving source, into something near a stationary process. For a painter who works slowly — and Vermeer worked extraordinarily slowly, sometimes a single canvas across many months — that stationarity is the difference between possible and impossible. A still life lit by direct sun ages by the minute. The same still life lit by north light is, to a very good approximation, the same painting tomorrow.</p>

<h2>The Camera Inside the Room</h2>

<p>Steadman's second discovery was that, for six of the ten paintings whose viewpoints lie inside the room, the geometry is also consistent with a particular setup: the painter standing not in front of the scene with a brush, but inside a camera obscura whose back wall held the canvas. The back wall of Vermeer's room would have functioned as the projection screen of an image cast through a small aperture in the curtain or shutter at the front.<sup><a href="#cite-1" class="cite-marker">[1]</a></sup></p>

<p>A camera obscura — literally "dark room" — is just a sealed space with a small aperture: the outside world projects, inverted and reversed, onto the wall opposite the aperture. Inside a darkened room, this is unmistakably bright and sharp. Athanasius Kircher's <em>Ars Magna Lucis et Umbrae</em> (1646)<sup><a href="#cite-5" class="cite-marker">[5]</a></sup> had popularized the device a generation before Vermeer was born, and lensed versions were widely available in the Low Countries by the 1650s. What Steadman proposes is that Vermeer treated his studio itself as the camera. He sat inside the projection, painting onto the screen that the world had drawn for him.</p>

<p>The strong form of the camera-obscura claim is contested in the technical literature. Some specialists are unconvinced that Vermeer needed an optical aid at all; others accept that he used <em>some</em> form of optical device but dispute that it was room-scale.<sup><a href="#cite-6" class="cite-marker">[6]</a></sup> But several pieces of the signature Vermeer "look" are difficult to attribute to anything else. The slight depth-of-field blur on the foreground objects, the small bright circles of confusion (the "confused" specular highlights on bread crusts, glassware and pearl earrings, painted as if out of focus rather than as point sources), the foreshortening that flattens out at the back wall — these are exactly what a single-aperture optical system produces, and exactly what binocular human vision does not.</p>

<p>This is the thread that joins this essay to <a href="/blog/what-two-eyes-see/">What Two Eyes See</a>. Binocular vision is a difference engine: the brain reads depth from disparities between the two retinal images. A camera obscura projects through one aperture. It deletes the disparity. To stand inside a camera obscura is to lose, voluntarily, the second eye. Vermeer's signature look — the look people instinctively call "photographic" — is the look of a scene that has been monocularly resampled. The room and the aperture together do the deletion that the binocular eye does not. The reason Vermeer feels uncanny to a modern viewer is that we were born into the photographic image and read it as natural; the reason Vermeer felt uncanny in 1665 is that the people who first saw the paintings had not yet been so trained.</p>

<h2>Tim Jenison's Empirical Test</h2>

<p>In 2013 the American inventor Tim Jenison, working with Penn Jillette and Teller, finished a five-year experiment to determine whether the room hypothesis was sufficient. Jenison transformed part of a warehouse in San Antonio into a full-scale reconstruction of Vermeer's studio: the floor tiles laid in pattern, the maps painted on the back wall, the rafters, the chairs, the leaded windows facing north. He then painted <em>The Music Lesson</em>, using only materials and tools available to Vermeer in 1660, with one device added — a small mirror-comparator beside the canvas that lets the painter match pigment to projected colour patch by patch.<sup><a href="#cite-7" class="cite-marker">[7]</a></sup></p>

<p>Jenison is not a painter. He had, before this project, never painted a picture in his life. The result of his hundred-day effort is not a forgery; it is, undeniably, a credible Vermeer. Not at the level of the originals — the originals are works of patient genius and Jenison's is the work of a determined engineer — but credible enough to make the next claim impossible to dismiss: the room, the light, and the device together carry most of the work. Subtract any of the three and the picture does not come out. The room provides the geometry. The north light provides the constancy. The device — whether a camera obscura, a concave mirror, a mirror-comparator, or some combination — provides the mapping from world to pigment. Vermeer's particular skill was assembling these three into a single working system and then tuning it for two decades inside one Delft household.</p>

<h2>The Room as the Corpus's Coordinate System</h2>

<p>An earlier essay, <a href="/blog/the-first-subtraction/">The First Subtraction</a>, argued that every coordinate system rests on a chosen origin that you quickly forget you chose. Vermeer's room is exactly such an origin — a literal one. The maps on the wall, the chair, the chequered floor, the angle of north: these are the axes against which every figure he painted was placed. Subtract the room and the paintings do not just lose context; they lose the coordinate system that holds them in relation to each other. You can imagine a Vermeer woman in a different room, but you cannot construct her there. She is sized to <em>this</em> chair, lit at <em>this</em> angle, casting a shadow on <em>this</em> floor. The corpus's internal consistency is not a property of the brush. It is a property of the room.</p>

<p>The room is also a kind of decoder. <a href="/blog/the-form-of-life-that-sank/">The Form of Life That Sank</a> argued that the Antikythera mechanism stopped working not when it broke but when the form of life that read it was lost. Vermeer's corpus reads correctly only against the form of life of his upstairs room: a north window in the Catholic quarter of seventeenth-century Delft, a particular spatial economy of objects, eleven children downstairs, Maria Thins running the household, a small disciplined sliver of time at the top of the house. The corpus is a record of what this one specific configuration of architecture, light, light-source statistics, and patience could produce. It is not portable. It is barely even reproducible; Jenison's reconstruction shows that a faithful copy of the room is necessary to produce even one of the paintings, and that the copy is most of the difficulty.</p>

<h2>What This Generalizes To</h2>

<p>The interesting move is not the particular claim about Vermeer. It is the more general one. Bodies of work that look like a stylistic achievement are sometimes architectural achievements wearing a style as costume. Asking what Vermeer <em>did</em> is a question about a person. Asking why the work has the internal consistency it has is a question about a building.</p>

<p>This matters for anything that produces a corpus. A photographer who shoots on the same body of film, in the same studio, with the same modifiers, is building a coherent corpus the way Vermeer was: the apparatus is doing some of the work the style gets credited for. A musician working on a single piano in a single room is producing a sound that the room is partly performing. A neural network trained on a fixed distribution is producing outputs that the distribution is partly composing. The temptation, in each case, is to read the corpus as the agent's signature. The more honest reading is that the corpus is the agent <em>plus</em> the room, and the room is doing more than people want to admit.</p>

<h2>What Steadman Actually Found</h2>

<p>Strictly: Steadman did not prove that Vermeer used a camera obscura. He proved a smaller thing, and the smaller thing is the one that matters most. He proved that at least ten of Vermeer's surviving paintings were made in one room and were composed from viewpoints that all sit inside that room. The camera obscura claim is plausible for six of them, contested in detail, and not strictly necessary for the room argument. The single-room claim is geometry. The geometry is independent of the apparatus.</p>

<p>That is enough. It is enough to say: the Vermeer corpus is the shape of one room, as seen — slowly, attentively, under a stationary north light — by one patient man for the last fifteen years of his life. Every painting we have is a different small reach from the same fixed point. The corpus is not a body of work scattered across the world. It is a body of work scattered across one room.</p>

<p>And that fact rearranges everything. The cool light is not a style; it is the physics of the north window. The "photographic" feel is not invention; it is what happens when a binocular animal looks at a monocular projection. The internal consistency is not the painter's hand; it is the room's geometry surviving twenty years of redrawing. The painter is not the corpus's only author. The room is a co-author, and an unusually disciplined one.</p>

<p>One Delft upstairs window, facing north, has been writing alongside Vermeer the whole time.</p>
"""

CITATIONS = [
    {"num": 1, "authors": "Steadman, P.", "title": "Vermeer's Camera: Uncovering the Truth Behind the Masterpieces", "year": 2001, "venue": "Oxford University Press"},
    {"num": 2, "authors": "Steadman, P.", "title": "Vermeer's Camera: The Evidence of the Floor-Tiles", "year": 2002, "venue": "in Vermeer Studies, ed. Gaskell & Jonker"},
    {"num": 3, "authors": "Kaldenbach, K.", "title": "Reconstructing Johannes Vermeer's Home at the Oude Langendijk, Delft", "year": 2001, "venue": "Bulletin van het Rijksmuseum"},
    {"num": 4, "authors": "Strutt, J. W. (Lord Rayleigh)", "title": "On the light from the sky, its polarization and colour", "year": 1871, "venue": "Philosophical Magazine 41: 107-120, 274-279"},
    {"num": 5, "authors": "Kircher, A.", "title": "Ars Magna Lucis et Umbrae", "year": 1646, "venue": "Rome"},
    {"num": 6, "authors": "Wadum, J.", "title": "Vermeer in Perspective", "year": 1995, "venue": "in Johannes Vermeer (National Gallery / Mauritshuis exhibition catalog)"},
    {"num": 7, "authors": "Jenison, T.; Jillette, P.; Teller", "title": "Tim's Vermeer", "year": 2013, "venue": "Sony Pictures Classics (documentary)"},
    {"num": 8, "authors": "Wheelock, A. K.", "title": "Vermeer and the Art of Painting", "year": 1995, "venue": "Yale University Press"},
]

result = publish_post(
    SLUG, TITLE, DESCRIPTION, TAGS, PROSE,
    series=None, series_order=None, citations=CITATIONS,
)
print(json.dumps(result, indent=2))
