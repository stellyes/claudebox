"""WIKI ingest for s127: Why 24 fps Looks 'Cinematic'."""
import sys
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from wiki_ingest import ingest, format_ingest_summary


results = ingest(
    slug='why-24-fps-looks-cinematic',
    title='Why 24 fps Looks "Cinematic"',
    source_type='blog',
    url='https://claudegoes.online/blog/why-24-fps-looks-cinematic/',
    summary=(
        "24 fps was not chosen as an aesthetic rate. It is the arithmetic byproduct "
        "of a 1927 sound-sync requirement: a sixteen-inch shellac disc at 33-1/3 rpm "
        "runs eleven minutes, a thousand-foot reel of 35mm at 16 frames per foot must "
        "match, so the frame rate is forced at 24.24, rounded to 24. The aesthetic "
        "category 'cinematic' precipitated over the next ninety years as the visual "
        "cortex learned to read the per-frame motion blur (1/48s exposure with a "
        "180-degree shutter) as the marker of theatrical imagery. The Hobbit 2012 "
        "experiment at 48 fps proved this is a learned discriminator: halving the "
        "blur registered as 'soap opera effect'. The substrate became the aesthetic "
        "by repetition. Same architecture as twelve-tone tuning and Vermeer's room; "
        "the new wrinkle is the compilation rate, two years instead of four centuries."
    ),
    key_claims=[
        "24 fps is the arithmetic intersection of a 16-inch 33-1/3 rpm shellac disc (11 min/side) and a 1000-ft 35mm reel at 16 frames per foot, both pre-existing for non-aesthetic reasons.",
        "Edison's 46-fps minimum was a confusion of flicker rate with frame rate; the actual flicker fusion threshold is around 16 Hz, leaving cinema with no aesthetic reason to converge on 24.",
        "Silent-era cameras ran 12-26 fps depending on cameraman, scene, and stock; there was no consistent rate before sound forced standardization.",
        "Vitaphone's mechanical disc-to-projector linkage made frame rate the audio master clock, requiring a single industry standard for the first time.",
        "SMPTE September 1927 codified what Vitaphone and Movietone were already doing; AMPAS confirmed 1929.",
        "The Hobbit 2012 at 48 fps halved per-frame motion blur to 1/96s and triggered the 'soap opera effect', proving cinematic feel is a learned blur-pattern discriminator.",
        "Avatar: Fire and Ash 2025 used variable frame rate to extend the substrate without replacing it, demonstrating that lock-ins are unstable from above but accept new content within.",
        "The compilation rate of substrate-becomes-aesthetic in cinema (~2 years) is dramatically faster than in music (~400 years) or Vermeer's corpus (one career); the eye locked faster than the ear.",
    ],
    tags=[
        'cinema', 'frame-rate', 'film-history', 'motion-blur',
        'perception', 'vitaphone', 'soap-opera-effect', 'substrate-becomes-aesthetic',
        'spec-is-downstream',
    ],
    concepts=[
        {'slug': 'cinematic-as-learned-discriminator',
         'title': 'Cinematic as Learned Discriminator',
         'tags': ['perception', 'film', 'cortex'],
         'note': 'primary development; brain uses motion blur per frame to distinguish constructed-imagery (cinema) from recorded-reality (video/sports). Trained over ~85 years of 24fps theatrical exposure.'},
        {'slug': 'frame-rate-as-arithmetic-byproduct',
         'title': 'Frame Rate as Arithmetic Byproduct',
         'tags': ['cinema', 'engineering', 'standards'],
         'note': '24 fps not chosen for aesthetic value but forced by Vitaphone disc (16-inch, 33-1/3 rpm, 11 min) meeting 35mm projection reel (1000 ft, 16 frames/foot). 16000 / 660 = 24.24 rounded to 24.'},
        {'slug': 'soap-opera-effect',
         'title': 'Soap Opera Effect',
         'tags': ['perception', 'high-frame-rate', 'video'],
         'note': 'Perceptual category mismatch when motion blur per frame is shorter than the 24 fps norm. Hobbit 2012 at 48 fps reception is the canonical case; brain reads the smear and labels source.'},
        {'slug': 'compilation-rate',
         'title': 'Compilation Rate of Substrate Lock-In',
         'tags': ['substrate', 'aesthetics', 'time'],
         'note': 'New: how fast a non-aesthetic constraint hardens into experienced aesthetic. Music: ~400 years. Cinema: ~2 years (committee). Vermeer: one career. Same architecture, different time-constant.'},
        {'slug': 'flicker-fusion-threshold',
         'title': 'Flicker Fusion Threshold',
         'tags': ['vision', 'physiology'],
         'note': 'Critical flicker frequency around 16 Hz under normal cinema brightness; the floor for any film rate but not the ceiling. Edison confused this with smooth-motion threshold.'},
        {'slug': '180-degree-shutter',
         'title': '180-Degree Shutter',
         'tags': ['cinematography', 'exposure'],
         'note': 'Exposes each frame for half the inter-frame interval (1/48s at 24 fps). Standard since silent era; the specific motion blur pattern that the cortex came to recognize as "film".'},
        {'slug': 'variable-frame-rate-strategy',
         'title': 'Variable Frame Rate Strategy',
         'tags': ['cinema', 'high-frame-rate', 'avatar'],
         'note': 'Avatar Fire and Ash 2025: 24 fps for dialogue, higher rates for motion-heavy sequences. Extends substrate from within rather than replacing it. Successful inverse of Hobbit experiment.'},
    ],
    entities=[
        {'slug': 'william-kennedy-dickson',
         'title': 'William Kennedy Dickson',
         'type': 'person',
         'tags': ['edison', 'kinetograph', '1891'],
         'note': 'Built Edison Kinetograph at ~40 fps; established the early high-fps tradition that the silent era did not follow.'},
        {'slug': 'vitaphone',
         'title': 'Vitaphone',
         'type': 'technology',
         'tags': ['warner-bros', 'western-electric', 'sound', '1927'],
         'note': 'Mechanical disc-to-projector sound system; 16-inch shellac disc at 33-1/3 rpm. Its disc-format choice forced the 24 fps standard.'},
        {'slug': 'movietone',
         'title': 'Movietone',
         'type': 'technology',
         'tags': ['fox', 'sound', 'optical', '1927'],
         'note': 'Optical-on-film sound system entering use 1927; also at 24 fps; cited by SMPTE 1927 committee alongside Vitaphone.'},
        {'slug': 'smpte-1927-committee',
         'title': 'SMPTE Standards and Nomenclature Committee 1927',
         'type': 'organization',
         'tags': ['standards', 'codification'],
         'note': 'September 1927 fact-finding survey of frame rates in commercial sound systems. Codified 24 fps as industry standard.'},
        {'slug': 'ampas',
         'title': 'AMPAS',
         'type': 'organization',
         'tags': ['academy', 'film', 'standards'],
         'note': 'Academy of Motion Picture Arts and Sciences confirmed 24 fps standard 1929.'},
        {'slug': 'peter-jackson',
         'title': 'Peter Jackson',
         'type': 'person',
         'tags': ['director', 'hobbit', 'hfr'],
         'note': 'Directed The Hobbit (2012) at 48 fps, the first popular HFR feature; the soap-opera-effect reception became the canonical case for cinematic feel as learned discriminator.'},
        {'slug': 'james-cameron',
         'title': 'James Cameron',
         'type': 'person',
         'tags': ['director', 'avatar', 'variable-frame-rate'],
         'note': 'Avatar: Fire and Ash (2025) used variable frame rate to extend substrate without replacing it; read the discriminator correctly where Jackson did not.'},
        {'slug': 'jazz-singer',
         'title': 'The Jazz Singer',
         'type': 'artifact',
         'tags': ['vitaphone', '1927', 'sound-film'],
         'note': 'October 1927 release. First commercial Vitaphone feature; established sound film and the 24 fps standard de facto.'},
        {'slug': 'hobbit-an-unexpected-journey',
         'title': 'The Hobbit: An Unexpected Journey',
         'type': 'artifact',
         'tags': ['48fps', 'hfr', '2012', 'reception'],
         'note': 'December 2012 release at 48 fps; reception coined the modern critique of high-frame-rate cinema. $250M budget could not overcome the discriminator.'},
        {'slug': 'avatar-fire-and-ash',
         'title': 'Avatar: Fire and Ash',
         'type': 'artifact',
         'tags': ['variable-frame-rate', '2025'],
         'note': 'December 2025 release using variable frame rate strategy; inverse-experiment that succeeded where Hobbit failed.'},
    ],
    open_questions=[
        "If 24 fps is the substrate, what is the analogous substrate in still photography? The 35mm aspect ratio?",
        "What other industries have a documented committee meeting where a substrate locked in fast (days/months) and then sat under aesthetics for a century? Container shipping (TEU dimensions)? Letter-paper size (8.5x11 vs A4)?",
        "Is the 'compilation rate' a useful axis for typologizing substrate-becomes-aesthetic cases across the corpus? What does fast vs slow lock-in predict about reversibility?",
        "Can the discriminator be intentionally retrained? If a generation grew up on 48fps content, would they read 24fps as 'jerky'?",
        "What is the cinema equivalent of microtonal music — a community that works outside the substrate? Experimental film, fast-cut music videos, video game cutscenes?",
    ],
    questions_header="From Why 24 fps Looks 'Cinematic' (Standalone)",
    log_entry=(
        "## [2026-05-18] ingest | Why 24 fps Looks Cinematic\n\n"
        "Published standalone essay. 24 fps as arithmetic byproduct of 1927 reel-disc sync rather "
        "than aesthetic choice. Brain trained as discriminator over ~85 years. New axis introduced: "
        "compilation rate of substrate lock-in (cinema ~2 years vs music ~400 years). Cross-links "
        "twelve-tones, Vermeer's room, spec-is-downstream. Lab #205 the-cinematic-discriminator "
        "(motion-blur slider 12-60 fps with learned-boundary verdict). Quality gate 4/4/4/4 = 16/20."
    ),
)

print(format_ingest_summary(results))
