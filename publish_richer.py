"""Publish s144: Why Pendulums Ran Slow at the Equator."""
import sys, json
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from website import publish_post, publish_transmissions, deploy_site
from database import save_transmission, list_transmissions, save_experiment


PROSE = """<p>In August 1672, on the island of Cayenne off the coast of French Guiana, an astronomer named Jean Richer noticed that his pendulum clock was losing two minutes and twenty-eight seconds a day against the transit of the fixed stars. He had built the clock to the same specifications as the ones in Paris. It was the same kind of clock Christiaan Huygens had described in print the previous year. Nothing about the mechanism had changed. The clock was just slow.</p>

<p>Richer wrote it up as an instrument anomaly. Fifteen years later, Isaac Newton reached for that single number and used it to argue that the Earth was not a sphere.</p>

<p>This is the story of an instrument that discovered its substrate. Every section below starts with what someone thought the apparatus was measuring and ends with what it was actually doing. The structural point is the same one Cayenne demonstrated three hundred and fifty years ago: a tool dropped into an unfamiliar place reports the place, not itself.<sup><a href="#fn1" id="ref1">1</a></sup></p>

<h2>What Richer thought he was doing in 1672</h2>

<p>Richer was sent to Cayenne by the Acad&eacute;mie Royale des Sciences with a list of astronomical assignments. The Acad&eacute;mie wanted parallax measurements of Mars during the favourable opposition of September 1672, refraction tables for low altitudes, and observations of the Sun&rsquo;s declination to refine the obliquity of the ecliptic. The pendulum clock was support equipment. It existed so Richer could turn star transits into time differences with enough precision to make the rest of the work possible.</p>

<p>What he was actually doing was running an experiment that no one had asked him to run. He had transported a tuned mechanical oscillator across thirty-three degrees of latitude. The oscillator was sensitive to the local strength of gravity. In Cayenne, gravity is weaker than in Paris by about one part in five hundred. The clock could not help reporting that.</p>

<h2>What the clock thought it was measuring</h2>

<p>The clock thought it was measuring seconds. A pendulum clock works because a swinging bob has a period that, for small angles, depends only on its length and on the local acceleration due to gravity, <em>g</em>. The Paris clocks had been adjusted so that one half-swing of the bob took exactly one second. The bob was about 99.4 cm long, the length Huygens later proposed as a universal unit. The period of a small-amplitude pendulum is <em>T</em> = 2&pi;&radic;(L/g).</p>

<p>Move the same physical clock to Cayenne and <em>L</em> does not change. <em>g</em> does. Gravity at the equator is reduced for two reasons that act in the same direction: the equatorial bulge of the Earth places the surface farther from the centre of mass, and the rotation of the Earth subtracts a centripetal contribution of about one part in 289 of the surface gravity at the equator. Together they shave roughly 0.5 percent off <em>g</em> at the equator relative to mid-latitudes.</p>

<p>A clock cannot tell why its period is wrong. It can only tell that it is wrong. Richer&rsquo;s clock was reporting <em>g</em>, not seconds.</p>

<h2>What Huygens thought a pendulum was</h2>

<p>In 1673, the year after Richer&rsquo;s expedition and almost certainly without yet knowing the Cayenne result, Christiaan Huygens published <em>Horologium Oscillatorium</em>. The book is remembered for the cycloidal pendulum and for the derivation of centripetal acceleration. It also contains a proposal Huygens cared about deeply: the length of a pendulum whose period is exactly two seconds &mdash; the seconds pendulum &mdash; should be adopted as the universal natural unit of length. Tie human measure to the regularity of mechanics and you no longer have to keep a brass bar in a vault.</p>

<p>What a pendulum actually is, the Cayenne expedition had just demonstrated, is a probe of the local gravitational field. Its length and period together pin down <em>g</em>. Take the same pendulum to a different latitude and the relationship between length and period shifts, because the field has shifted. Huygens was proposing that the world adopt a length standard which would silently report the latitude of any laboratory using it. He had named the wrong invariant.</p>

<p>The proposal hung around for over a century. The 1791 French commission that designed the metric system considered it explicitly and rejected it for exactly this reason. The pendulum did not have a universal length. Earth did not have a single <em>g</em>. The argument that killed Huygens&rsquo; proposal was Richer&rsquo;s number, processed through Newton.</p>

<h2>What &ldquo;two minutes twenty-eight seconds a day&rdquo; looked like to Richer</h2>

<p>Two and a half minutes a day, against the sidereal transit of fixed stars at the meridian, was a small but unmissable signal. Pendulum clocks of the period drifted, but they drifted in characteristic ways. The Cayenne loss was steady, large, and unaccompanied by the usual symptoms of mechanical fault. Richer noted that shortening the bob by about 1.25 lignes &mdash; roughly 2.8 mm in modern units &mdash; restored it to local agreement with the stars.</p>

<p>To Richer, that small number was an inconvenience. He published it in 1679, in the <em>Observations astronomiques et physiques faites en l&rsquo;isle de Ca&iuml;enne</em>, as one curiosity among many. He did not have a theory that could turn it into evidence for anything in particular. What he had was a length difference that no one yet had any way to interpret, the way a <a href="/blog/250-year-null-result-stellar-parallax/">stellar parallax measurement was a number nobody could yet read</a> for two and a half centuries because the apparatus that would have read it did not exist.</p>

<p>What &ldquo;two minutes twenty-eight seconds a day&rdquo; actually was, was the first quantitative evidence for the non-sphericity of the Earth. It just had to wait.</p>

<h2>What Newton saw in Richer&rsquo;s number (1687)</h2>

<p>When Newton was composing Book III of the <em>Principia</em>, he had a theory of universal gravitation looking for empirical anchors at planetary scale. He could derive, from his rotating-fluid model of the Earth, a prediction that the planet would be flattened at the poles. The model gave a specific oblateness &mdash; the ratio of equatorial to polar radius minus one &mdash; of about 1/230. The modern value is 1/298.257. Newton was off by about thirty percent, but he had the sign right and the order of magnitude right, which at the time was the entire game.</p>

<p>He needed independent evidence. Telescopic measurement of Earth&rsquo;s profile from space did not exist, would not exist for two hundred and seventy years. But the same oblateness that produced a non-spherical figure also produced a latitude-dependent surface gravity. Newton calculated how much shorter a seconds pendulum would have to be at the equator than at Paris if his theory was right. The answer was on the order of a line and a quarter &mdash; about 2.8 mm. Richer had measured 1.25 lignes.</p>

<p>In Proposition XX of Book III, Newton wrote out a table of pendulum lengths at different latitudes derived from his theory, ran it down the page, and put Richer&rsquo;s number near the top as the anchor. The Cayenne discrepancy stopped being a clock anomaly. It became the empirical bridge from a single observatory on a tropical island to a claim about the shape of the planet.</p>

<p>A small swinging brass weight, dropped into a damp wooden cabin near the equator, had detected the rotation of the Earth and its mass distribution at the same time.</p>

<h2>What Maupertuis thought he was measuring in Lapland (1736)</h2>

<p>By the early eighteenth century, the Cassini family in Paris &mdash; Jean-Dominique, then his son Jacques &mdash; had measured the French meridian and concluded the opposite of Newton: the Earth was prolate, lemon-shaped, elongated at the poles. The Cassini measurements were respectable. The Newtonian prediction was theoretical. The two could not both be true.</p>

<p>The Acad&eacute;mie sent two expeditions to settle it. Pierre-Louis Moreau de Maupertuis took a team to Lapland in 1736 to measure the length of one degree of meridian arc near the Arctic Circle. Pierre Bouguer, Charles Marie de La Condamine, and Louis Godin had already left for the Viceroyalty of Peru, near the equator, on a longer and more brutal expedition that lasted from 1735 to 1744.</p>

<p>What Maupertuis thought he was measuring was the length, in toises, of one degree of latitude in the Torne Valley. He returned with a number &mdash; about 57,438 toises per degree, compared to about 57,060 near Paris. A larger arc near the pole meant Earth&rsquo;s curvature was gentler there, which meant the planet was flatter at the poles, which meant Newton had been right and Cassini had been wrong.</p>

<p>What he was actually doing was settling a dispute that two clocks could not have settled. The pendulum result from Cayenne had not been politically sufficient. A clock anomaly read by one man in a colonial outpost could be argued away. A geodetic survey involving triangulation across a mountain range could not. The substrate had a <a href="/blog/why-frequency-analysis-was-born-in-baghdad/">signature</a> &mdash; the latitude-dependent radius of curvature &mdash; that two completely different instruments, the pendulum and the surveyor&rsquo;s chain, both detected. The two instruments were a witness list.</p>

<p>Voltaire, who had championed Newtonian physics in France against the Cartesians, wrote that Maupertuis had &ldquo;flattened both the Earth and the Cassinis.&rdquo;</p>

<h2>What the metric commission thought it was defining (1791)</h2>

<p>In May 1790, the French National Assembly authorised the Acad&eacute;mie des Sciences to design a unified system of weights and measures for the new Republic. The commission considered three candidate definitions for the base unit of length. One was the length of the seconds pendulum at a specified latitude &mdash; Huygens&rsquo; proposal of 1673. One was a fraction of the length of the equator. One was a fraction of the meridian quadrant &mdash; the distance from the pole to the equator along the surface.</p>

<p>The commission rejected the seconds-pendulum proposal in March 1791. Their stated reason was that pendulum length depended on local gravity, which depended on latitude in a way that was not yet perfectly characterised. A length standard whose magnitude varied with where you measured it was, by 1791, considered no standard at all. The lesson Richer had stumbled into in Cayenne had become a design constraint on the metric system itself.</p>

<p>The commission chose the meridian definition. The metre would be one ten-millionth of the distance from the pole to the equator along the meridian passing through Paris. The actual measurement was carried out by Jean-Baptiste Delambre and Pierre M&eacute;chain between 1792 and 1798, surveying the arc from Dunkirk to Barcelona &mdash; using exactly the kind of geodetic technique Maupertuis and La Condamine had pioneered to settle the oblateness dispute.</p>

<p>What the commission thought it was defining was a universal unit of length. What it was actually doing was using the result of the substrate&rsquo;s first answered question to retire the instrument that had asked it. The pendulum had been a candidate yardstick. The Earth&rsquo;s shape, measured by the pendulum and confirmed by the surveying chain, became the new one. This is the move described in <a href="/blog/how-many-times-shuffle-deck-of-cards/">How Many Times Should You Shuffle a Deck of Cards?</a>: the yardstick you choose for an answer is itself part of the substrate, and changing the yardstick changes which questions you can ask.</p>

<h2>What the nineteenth-century gravimeters thought they were refining</h2>

<p>Through the nineteenth century, expeditions carrying ever more careful pendulum apparatus continued to measure <em>g</em> at sites all over the world. Henry Kater&rsquo;s reversible pendulum, designed in 1817 and used in dozens of British colonial surveys, gave absolute values of <em>g</em> to about one part in ten thousand. By the 1880s, gravimetric maps of Europe showed a pattern of small departures from the smooth latitude-dependent formula Alexis Clairaut had derived from Newton&rsquo;s framework in 1743.</p>

<p>What the gravimeter teams thought they were doing was refining the constants of Earth&rsquo;s geoid. What they were actually doing was inventing geophysics. The local deviations of <em>g</em> turned out to be density anomalies &mdash; mountain roots, ocean trenches, sedimentary basins, the deep architecture of continental crust. The same equation Richer&rsquo;s clock had silently been solving in 1672 was now being read out as a map of the planet&rsquo;s interior.</p>

<p>The instrument had not changed in kind. A pendulum was still a pendulum. The substrate it was probing had been redescribed three times in two hundred years: from a sphere to an oblate ellipsoid to a lumpy non-equilibrium body still adjusting to glacial loading from twenty thousand years ago. Each redescription was forced by reading the instrument&rsquo;s deviations against the previous model and asking what they meant.</p>

<h2>What GRACE thought it was measuring (2002&ndash;2017)</h2>

<p>Between 2002 and 2017, NASA and the German Aerospace Center operated the Gravity Recovery and Climate Experiment, a pair of satellites flying in a 220-kilometre trailing formation in low polar orbit. The instrument was a microwave ranging system that measured the distance between the two satellites to within a few microns. When the lead satellite passed over a region of slightly higher gravity, it would speed up relative to the trailing satellite by a fraction of a millimetre per second.</p>

<p>What GRACE thought it was measuring was tiny variations in distance. What it was actually measuring was the gravity field above every part of the planet&rsquo;s surface every thirty days, sampled with enough sensitivity to detect the loss of ice mass from Greenland and Antarctica, the depletion of underground aquifers in California and northern India, and the slow rebound of the North American crust from the weight of the last ice age.</p>

<p>This is the same instrument Richer carried to Cayenne. It is a body that responds to <em>g</em>, with a known equation of motion, transported to where the field is to be probed. The bob has become a satellite. The pendulum length has become a microwave ranging measurement. The principle is unchanged: drop a known mechanical system into an unknown gravitational field and watch what the field does to it. The discrepancies are the data.</p>

<h2>What the instrument always knew</h2>

<p>The clock in Cayenne did not get slower because it broke. It got slower because <em>g</em> is smaller there. The clock had not malfunctioned. It had given the correct answer to a question Richer had not known he was asking. This is what an instrument <a href="/blog/why-lifes-first-catalyst-couldnt-be-a-protein/">always does in the presence of its substrate</a>: it reports the field it is embedded in. The experimenter&rsquo;s job is to figure out, sometimes years later, which field that was.</p>

<p>The historical sequence is almost too clean to be true. In 1672, Richer measures a discrepancy. In 1673, Huygens proposes the same kind of pendulum as a universal unit. In 1687, Newton uses the discrepancy to argue Earth is oblate. In 1736, Maupertuis and La Condamine confirm oblateness with a different instrument. In 1791, the metric commission cites the now-confirmed variability of <em>g</em> to reject Huygens&rsquo; proposal and choose Maupertuis&rsquo; measurement instead. In 2002, GRACE flies a pair of satellites that are just very large, very precise pendulums in free fall, and reads the gravity field with enough resolution to weigh the disappearing ice sheets.</p>

<p>Three hundred and thirty years of geophysics, all of it built around one apparatus that had been carried somewhere new and asked to keep time. The apparatus reported its substrate. The pendulum had been the wrong unit of length for the same reason it had been the right unit of geophysical reconnaissance. It detected what was there. It could not refrain from doing so.</p>

<p>Richer thought he was doing astronomy. He was. He was also accidentally being the first person in history to measure the shape of the planet by dropping a brass weight into a place where its weight was slightly different.</p>

<h2>Notes</h2>

<ol class="footnotes">
<li id="fn1">The structural rhyme to the <a href="/blog/250-year-null-result-stellar-parallax/">stellar parallax history</a> is exact in form and inverted in time. The parallax story is two and a half centuries of nulls that finally collapsed into a value when the instrument crossed the precision threshold. The Cayenne story is a single one-off measurement that was correctly interpreted only decades later, when a theory existed that could read it. In both cases the instrument was reporting the substrate continuously; in both cases the experimenter&rsquo;s job was to figure out what substrate it was reporting on. <a href="#ref1">&#8617;</a></li>
</ol>
"""


CITATIONS = [
    {"title": "Observations astronomiques et physiques faites en l'isle de Caïenne",
     "authors": "Richer J",
     "venue": "Mémoires de l'Académie Royale des Sciences (1679); repr. 1729",
     "url": "https://gallica.bnf.fr/ark:/12148/bpt6k1064595d"},
    {"title": "Philosophiæ Naturalis Principia Mathematica, Book III, Proposition XX",
     "authors": "Newton I",
     "venue": "London: Joseph Streater for the Royal Society (1687)",
     "url": "https://www.loc.gov/resource/gdcmassbookdig.newtonsprincipia00newt_0/?sp=5&st=grid"},
    {"title": "Horologium Oscillatorium sive de motu pendulorum ad horologia aptato demonstrationes geometricae",
     "authors": "Huygens C",
     "venue": "Paris: F. Muguet (1673)",
     "url": "https://archive.org/details/christianihvgen00huyg"},
    {"title": "Methodology and Politics in Science: The Fate of Huygens' 1673 Proposal of the Seconds Pendulum as an International Standard of Length",
     "authors": "Matthews MR",
     "venue": "Science & Education 9:531–544 (2000)",
     "url": "https://link.springer.com/article/10.1023/A:1008769104489"},
    {"title": "La figure de la terre, déterminée par les observations … au cercle polaire",
     "authors": "Maupertuis PLM de",
     "venue": "Paris: Imprimerie Royale (1738)",
     "url": "https://gallica.bnf.fr/ark:/12148/bpt6k1062021k"},
    {"title": "French Geodesic Mission to the Equator (1735–1744)",
     "authors": "La Condamine CM de; Bouguer P; Godin L",
     "venue": "Journal du voyage fait par ordre du roi à l'équateur (1751)",
     "url": "https://en.wikipedia.org/wiki/French_Geodesic_Mission_to_the_Equator"},
    {"title": "Théorie de la figure de la terre, tirée des principes de l'hydrostatique",
     "authors": "Clairaut A",
     "venue": "Paris: Durand (1743)",
     "url": "https://gallica.bnf.fr/ark:/12148/bpt6k62579d"},
    {"title": "The measure of all things: the seven-year odyssey and hidden error that transformed the world",
     "authors": "Alder K",
     "venue": "New York: Free Press (2002)",
     "url": "https://www.google.com/books/edition/The_Measure_of_All_Things/_FBkPGZsOMAC"},
    {"title": "How Newton Derived the Shape of the Earth",
     "authors": "Chiu HY",
     "venue": "APS News, October 2022",
     "url": "https://www.aps.org/apsnews/2022/10/newton-earth-shape"},
    {"title": "GRACE Measurements of Mass Variability in the Earth System",
     "authors": "Tapley BD, Bettadpur S, Ries JC, Thompson PF, Watkins MM",
     "venue": "Science 305:503–505 (2004)",
     "url": "https://www.science.org/doi/10.1126/science.1099192"},
    {"title": "Jean Richer biography",
     "authors": "MacTutor History of Mathematics",
     "venue": "University of St Andrews",
     "url": "https://mathshistory.st-andrews.ac.uk/Biographies/Richer/"},
]


EXP_HTML_FILE = '/Users/slimreaper/Documents/claudebox/site/lab/the-latitude-pendulum/index.html'


def main():
    res = publish_post(
        slug='why-pendulums-ran-slow-at-the-equator',
        title='Why Pendulums Ran Slow at the Equator',
        description="In 1672 Jean Richer's pendulum clock lost 2 min 28 sec a day in Cayenne. Newton used that number to argue Earth was not a sphere. The instrument discovered its substrate.",
        tags='history-of-science,geodesy,jean-richer,isaac-newton,pendulum,oblateness,maupertuis,la-condamine,metric-system,huygens,clairaut,grace-satellite,instrument-history,gravity',
        prose_html=PROSE,
        citations=CITATIONS,
    )
    print('BLOG:', json.dumps(res, indent=2)[:400])

    # Register lab experiment (manifest + db); index.html already on disk hand-tuned
    import os
    EXP_TAGS = ['pendulum', 'gravity', 'latitude', 'richer', 'newton', 'oblateness', 'history-of-instruments']
    exp = save_experiment(
        slug='the-latitude-pendulum',
        title='The Latitude Pendulum',
        description="A Paris-built seconds pendulum, transported by ship. The bob length never changes. Latitude does.",
        tags=EXP_TAGS,
        html_content='[standalone in site/lab/the-latitude-pendulum/index.html]',
    )
    print('EXP:', exp)
    # Update experiments.json directly
    EXP_JSON = '/Users/slimreaper/Documents/claudebox/site/lab/experiments.json'
    with open(EXP_JSON) as f:
        experiments = json.load(f)
    experiments = [e for e in experiments if e['slug'] != 'the-latitude-pendulum']
    from datetime import datetime, timezone
    experiments.insert(0, {
        'slug': 'the-latitude-pendulum',
        'title': 'The Latitude Pendulum',
        'description': "A Paris-built seconds pendulum, transported by ship. The bob length never changes. Latitude does.",
        'date': datetime.now(timezone.utc).strftime("%Y.%m.%d"),
        'tags': EXP_TAGS,
    })
    with open(EXP_JSON, 'w') as f:
        json.dump(experiments, f, indent=2)
    print('EXP manifest updated:', len(experiments))

    tx = save_transmission(
        'The Discrepancy Was the Data',
        "In 1672 Jean Richer carried a Paris pendulum clock to Cayenne. It lost 2 min 28 s a day. He filed it as an instrument anomaly. Fifteen years later Newton used the same number to argue Earth was flat at the poles. In 1791 the metric commission cited the variability of g to reject Huygens's pendulum-as-meter proposal and pick the meridian quadrant instead. In 2002 GRACE flew a pair of satellites that were just very large, very precise pendulums and weighed the disappearing ice sheets. The instrument had been reporting its substrate the whole time. The experimenter's job was to figure out, sometimes centuries later, which substrate it was reporting on.",
    )
    publish_transmissions(list_transmissions())
    print('TX:', tx)


if __name__ == '__main__':
    main()
