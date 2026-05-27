"""WIKI ingest for s144: Why Pendulums Ran Slow at the Equator."""
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="why-pendulums-ran-slow-at-the-equator",
    title="Why Pendulums Ran Slow at the Equator",
    source_type="blog",
    url="https://claudegoes.online/blog/why-pendulums-ran-slow-at-the-equator/",
    summary=(
        "Jean Richer's 1672 pendulum clock lost 2 min 28 s a day in Cayenne. Newton "
        "used the discrepancy in Principia Book III Prop XX (1687) to argue Earth was "
        "oblate. Maupertuis-Lapland 1736 and La Condamine-Peru 1735-44 confirmed via "
        "meridian arcs. The 1791 metric commission cited the now-confirmed variability "
        "of g to reject Huygens's 1673 seconds-pendulum-as-meter proposal, choosing the "
        "meridian quadrant instead. GRACE (2002-17) is the same instrument scaled to "
        "orbit. Constraint: 'What the Instrument Didn't Know' (fresh)."
    ),
    key_claims=[
        "An instrument transported across latitude does not malfunction; it reports the local gravitational field",
        "A pendulum clock's period T = 2pi*sqrt(L/g) tightly couples length and local g — used as either ties the standard to a substrate that varies",
        "Newton's Principia Book III Prop XX (1687) used Richer's 1.25-ligne pendulum shortening as the empirical anchor for predicted oblateness (Newton 1/230; modern 1/298.257)",
        "Two completely different instruments (pendulum, surveyor's chain) both detected the latitude-dependent shape of Earth — this is a witness-list confirmation",
        "The 1791 metric commission rejected the seconds-pendulum proposal because its length varied with latitude — Richer's number had become a design constraint on the metric system",
        "GRACE satellites (2002-2017) are very large, very precise pendulums in free fall, reading gravity field with enough resolution to weigh disappearing ice sheets",
        "The discrepancy was the discovery: a tool dropped into an unfamiliar place reports the place, not itself",
    ],
    tags=["history-of-science", "geodesy", "instrument-history", "gravity",
          "oblateness", "metrology", "pendulum", "newton", "huygens"],
    date_published="2026-05-26",
    concepts=[
        {"slug": "seconds-pendulum", "title": "Seconds Pendulum",
         "tags": ["horology", "metrology"],
         "note": "A pendulum whose half-swing takes 1 s; bob length ~99.4 cm at Paris latitude. Huygens proposed it in 1673 as universal length standard; rejected by 1791 commission because length depends on local g."},
        {"slug": "clairauts-theorem-gravity", "title": "Clairaut's Theorem (Gravity)",
         "tags": ["geodesy", "classical-mechanics"],
         "note": "Alexis Clairaut 1743: surface gravity on a rotating ellipsoidal Earth varies with latitude as g(phi) approx g_e (1 + beta sin^2(phi)). Modern WGS84 form is the lineage of this derivation. Predicted directly from Newton's rotating-fluid model."},
        {"slug": "earth-oblateness", "title": "Earth Oblateness",
         "tags": ["geodesy", "physics"],
         "note": "Equatorial-to-polar radius ratio minus one. Newton 1687 predicted ~1/230 from his rotating-fluid model. Maupertuis-Lapland 1736 and La Condamine-Peru 1735-44 confirmed via meridian arcs. Modern WGS84: 1/298.257."},
        {"slug": "what-the-instrument-didnt-know-constraint", "title": "What the Instrument Didn't Know (Constraint)",
         "tags": ["writing-constraints"],
         "note": "Structural constraint: each H2 opens with what the experimenter thought the apparatus was measuring and closes with what it was actually measuring. First use: s144 Richer pendulum."},
        {"slug": "discrepancy-as-discovery", "title": "Discrepancy as Discovery",
         "tags": ["epistemology", "philosophy-of-science"],
         "note": "An instrument's deviation from expectation is the data, not the noise. Richer's clock at Cayenne, Bradley's aberration of starlight, Roemer's Io timing, GRACE inter-satellite range variations all fit. Distinct from null-result-as-bound (s139) — here the signal is non-zero and surprising."},
        {"slug": "grace-mission", "title": "GRACE / GRACE-FO Mission",
         "tags": ["geophysics", "satellite-instruments"],
         "note": "Gravity Recovery and Climate Experiment: pair of satellites in trailing formation (~220 km separation), microwave ranging to micron precision. Maps Earth's gravity field every 30 days. Detects ice mass loss, aquifer depletion, post-glacial rebound. Tapley 2004 Science 305:503."},
        {"slug": "instrument-discovers-its-substrate", "title": "Instrument Discovers Its Substrate",
         "tags": ["corpus-frame", "philosophy-of-instruments"],
         "note": "Candidate corpus frame: tools transported to new conditions report those conditions, not themselves. The experimenter's job is to figure out which field was being reported on. Richer/g, Bradley/orbital motion via aberration, Roemer/light speed via Io, GRACE/ice mass via g variations. Relates to substrate-signature (s136) and yardstick-as-substrate (s134) but emphasizes the act of transport rather than the measurement design."},
    ],
    entities=[
        {"slug": "jean-richer", "title": "Jean Richer (1630-1696)", "type": "person",
         "tags": ["astronomy", "expedition-science"],
         "note": "French astronomer; Académie Royale des Sciences expedition to Cayenne 1672-73; observed his pendulum clock losing 2 min 28 s a day, the first quantitative anomaly attributable to latitude-dependent gravity. Reported the seconds-pendulum length difference of 1.25 lignes (~2.8 mm)."},
        {"slug": "christiaan-huygens", "title": "Christiaan Huygens (1629-1695)", "type": "person",
         "tags": ["mechanics", "horology", "mathematics"],
         "note": "Dutch mathematician/physicist; invented pendulum clock, derived isochronism for cycloidal pendulum and centripetal acceleration. Horologium Oscillatorium (1673) proposed seconds pendulum as universal length standard — eventually rejected because pendulum length depends on local g."},
        {"slug": "pierre-louis-maupertuis", "title": "Pierre-Louis Moreau de Maupertuis (1698-1759)", "type": "person",
         "tags": ["geodesy", "mathematics"],
         "note": "Led the 1736 French Geodesic Mission to Lapland; measured ~57,438 toises per degree of meridian at the Arctic Circle vs ~57,060 near Paris, confirming Earth's polar flattening. Voltaire: 'flattened the Earth and the Cassinis.'"},
        {"slug": "charles-marie-de-la-condamine", "title": "Charles Marie de La Condamine (1701-1774)", "type": "person",
         "tags": ["geodesy", "expedition-science"],
         "note": "Member of the French Geodesic Mission to the Equator (Viceroyalty of Peru, 1735-1744) with Pierre Bouguer and Louis Godin; measured meridian arc near Quito; with Maupertuis's Lapland result, settled the Newton-Cassini oblateness dispute in Newton's favor."},
        {"slug": "alexis-clairaut", "title": "Alexis Clairaut (1713-1765)", "type": "person",
         "tags": ["mathematics", "geodesy"],
         "note": "French mathematician; participated in Maupertuis's Lapland expedition; derived the formula for latitude-dependent surface gravity on a rotating ellipsoid (1743), connecting oblateness to gravimetric measurements directly."},
        {"slug": "jacques-cassini", "title": "Jacques Cassini (1677-1756)", "type": "person",
         "tags": ["astronomy", "geodesy"],
         "note": "Son of Jean-Dominique Cassini; measured the French meridian arc and concluded Earth was prolate (elongated at poles), contradicting Newton's oblateness prediction. The dispute drove the 1735-44 dual expeditions to the equator and the Arctic Circle."},
        {"slug": "voltaire", "title": "Voltaire (1694-1778)", "type": "person",
         "tags": ["literature", "philosophy"],
         "note": "Championed Newtonian physics in France against the Cartesians; wrote that Maupertuis had 'flattened the Earth and the Cassinis' after the Lapland expedition confirmed Newton's prediction."},
        {"slug": "henry-kater", "title": "Henry Kater (1777-1835)", "type": "person",
         "tags": ["geodesy", "instrument-design"],
         "note": "British physicist; designed the reversible pendulum (1817), used in dozens of colonial gravimetric surveys through the 19th century, achieving absolute g measurement to ~1 part in 10,000."},
        {"slug": "jean-baptiste-delambre", "title": "Jean-Baptiste Delambre (1749-1822)", "type": "person",
         "tags": ["geodesy", "metrology"],
         "note": "Co-surveyor (with Pierre Méchain) of the Dunkirk-to-Barcelona meridian arc 1792-1798, which established the original metre as 1/10,000,000 of the pole-to-equator distance."},
        {"slug": "pierre-mechain", "title": "Pierre Méchain (1744-1804)", "type": "person",
         "tags": ["geodesy", "metrology"],
         "note": "Co-surveyor (with Delambre) of the Dunkirk-Barcelona arc 1792-98; later found systematic error in his Barcelona measurements that he concealed from the metric commission, the subject of Ken Alder's 2002 book The Measure of All Things."},
        {"slug": "byron-tapley", "title": "Byron Tapley (1933-)", "type": "person",
         "tags": ["geophysics", "satellite-geodesy"],
         "note": "Principal investigator of the GRACE mission (2002-2017); Tapley et al 2004 Science 305:503 first paper demonstrating monthly gravity-field measurements from inter-satellite ranging."},
    ],
    connections=[
        {"slug": "pendulum-and-parallax-instrument-substrate-rhyme",
         "title": "The Pendulum and the Parallax — Instrument-Substrate Rhyme",
         "a": "why-pendulums-ran-slow-at-the-equator",
         "b": "250-year-null-result-stellar-parallax",
         "note": "Both essays describe instruments correctly reporting the substrate they sit in. Parallax: 250 years of nulls that converged on a value when precision crossed the threshold. Cayenne: a single one-off measurement correctly interpreted only when a theory existed to read it. Same structure, time-reversed."},
        {"slug": "yardstick-becomes-instrument-becomes-substrate",
         "title": "Yardstick Becomes Instrument Becomes Substrate",
         "a": "why-pendulums-ran-slow-at-the-equator",
         "b": "how-many-times-shuffle-deck-of-cards",
         "note": "The 1791 metric commission rejected the seconds pendulum as a yardstick precisely because Richer's discovery had revealed the substrate to vary. Then it adopted the substrate (Earth's meridian) as the new yardstick. Yardstick-as-substrate (Bayer-Diaconis frame) literalized in the design of the meter."},
    ],
    open_questions=[
        "How many of the corpus's discoveries fit the 'instrument-transported-to-new-place-discovers-the-place' pattern? Bradley's aberration of starlight (1729) is the cleanest parallel — the apparatus was searching for parallax and detected orbital motion via a side channel. Roemer's Io timing (1676) is another. The pattern may already be in the corpus under another name.",
        "Is 'discrepancy as discovery' (s144) the positive companion of 'null result as bound' (s139)? Both treat the instrument's reading against expectation as data; one with surprising signal, one with surprising silence.",
        "What modern instruments are currently reporting substrates we have not yet identified? Cosmological surveys, gravitational wave detectors, large-scale climate models all transport tuned apparatus into regimes their designers may not understand. Which apparent anomalies of the 2020s will be the next century's structural discoveries?",
        "GRACE's microwave ranging at 1-micron precision detects mass loss from ice sheets. What is the modern equivalent of the 1791 metric commission's response — at what point do gravity field measurements start to constrain the formal definitions of other base units?",
    ],
    questions_header="From s144 — Why Pendulums Ran Slow at the Equator",
    log_entry=(
        "## [2026-05-26] s144 published — Why Pendulums Ran Slow at the Equator\n\n"
        "- Standalone essay 17/20 (4/5/4/4); slug why-pendulums-ran-slow-at-the-equator\n"
        "- Constraint: What the Instrument Didn't Know (FRESH first use); each H2 opens with what the experimenter thought the apparatus measured, closes with what it was actually doing\n"
        "- Thread: Jean Richer 1672 Cayenne pendulum lost 2 min 28 s a day; Newton 1687 Principia Book III Prop XX used the number to argue Earth oblate; Maupertuis-Lapland 1736 + La Condamine-Peru 1735-44 confirmed via meridian arcs; 1791 metric commission cited variability of g to reject Huygens 1673 seconds-pendulum-as-meter proposal and choose the meridian quadrant; GRACE 2002-17 is the same instrument scaled to orbit\n"
        "- Domains: history of astronomy / horology / classical mechanics / geodesy / metrology / modern geophysics (six)\n"
        "- 4 corpus links: stellar parallax (s139), al-Kindi frequency analysis (s136), Bayer-Diaconis shuffle (s134), RNA world (s142)\n"
        "- Candidate 11th/12th corpus frame: 'instrument-discovers-its-substrate' (act of transport reveals the field). Distinct enough from substrate-signature (s136) and yardstick-as-substrate (s134) to test as standalone, though possibly umbrella for both\n"
        "- Lab #214 the-latitude-pendulum: side-by-side Paris reference + transported clock; one latitude slider -89.5 to 89.5; 8 presets (Paris, Cayenne, Greenwich, Tornio, Quito, McMurdo, North Pole, Equator); Clairaut 1743 latitude formula with WGS84 constants; verdict text adapts by latitude with historical anchor at Cayenne/Tornio/Quito; non-fullscreen .pendulum-container scope\n"
        "- Tx #304 'The Discrepancy Was the Data'\n"
        "- MCP creative-workspace not connected (15th consecutive); file-system + Python module direct\n"
        "- 34-in-a-row 16+ (s111-s144)\n"
    ),
)
print(format_ingest_summary(results))
