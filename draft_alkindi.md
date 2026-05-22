# Why Frequency Analysis Was Born in 9th-Century Baghdad

Around 850 CE, a polymath in Abbasid Baghdad wrote a short treatise that does not appear in any European source for the next seven hundred years. Its title was *Risāla fī Istikhrāj al-Mu'ammā* — "On Extracting Obscured Correspondence." Its method was simple enough to fit on a single page. Find a piece of text in the same language as your ciphertext, long enough to fill a sheet. Count how often each letter appears. Then count how often each letter appears in the cipher. Match the most frequent to the most frequent.

That is frequency analysis. It is the first formal method of cryptanalysis in any tradition. The author was Abū Yūsuf Yaʻqūb ibn Isḥāq al-Kindī (c. 801–873), and the only surviving copy of his manuscript sat unread in the Süleymaniye Ottoman Archive in Istanbul until Damascus academics Mrayati, Alam, and al-Tayyan rediscovered it in 1987.

The question is not whether al-Kindi was clever. He clearly was. The question is why this particular method appeared in this particular place at this particular moment. The Greeks had ciphers for a thousand years before him. The Romans used them. Egypt, India, and China all had script and secrecy. None of them invented frequency analysis.

The answer is not a single insight. It is a list of preconditions, each of them invisible from inside its own moment, all of them required.

## The Method, in One Sentence

Al-Kindi's central observation, stripped of detail: **the letter frequencies of a language are stable across messages**. They depend on the substrate — Arabic, Greek, Latin — not on what any particular message says. A substitution cipher relabels the letters but cannot relabel the distribution. The pattern survives. Count it and you can unmix it.

This is not how anyone before al-Kindi described language. To describe language this way you need to first recognize that the substrate has properties that are measurable independently of meaning. Letters are not just signs; they are events with rates. The alphabet is a population with a census.

Each of the witnesses below was required for that recognition to become possible.

## The Witness List

The constraint of this essay is forensic. The verdict — that frequency analysis emerged in 9th-century Baghdad because language became thinkable as a statistical object — is the conclusion. Five witnesses, each from a different domain, provide the evidence. Any one of them is insufficient. Together they explain the convergence.

I will call the witnesses in chronological order of their contribution.

## Witness 1: The Closed Canon (Quranic Philology, c. 650–800)

The Quran was compiled under the Caliph Uthman around 650 CE into a fixed, codified text. Within two generations, Muslim scholars had a problem the Greek and Roman traditions never had at this scale: a single sacred document that could not be altered, but whose internal chronology was contested. Which verses were Meccan (610–622)? Which were Medinan (622–632)? The legal question was urgent. Later commands abrogated earlier ones, so the timestamp of a verse decided whether a rule still applied.

Without instrumentation, scholars turned to internal evidence. Meccan suras were shorter, with rhymed clausulae and frequent oaths. Medinan suras were longer, with denser formulaic phrasing and more legislation. By the time of Ibn Khaldun and earlier, scholars were counting features: oath density, average verse length, the relative frequency of phrases like "O you who believe."

In 1976, the engineer-philosopher Mehdi Bazargan would graph syllable counts across the suras and confirm that average verse length increased monotonically with the order of revelation. He was using modern statistical inference to test a question that 9th-century philologists had already been answering by counting.

The closed canon trained an entire intellectual culture to treat text as something with measurable parts. Without that training, the leap to counting letters in a cipher would have looked perverse. With it, it was obvious — just one more application of the habit.

## Witness 2: The Counted Alphabet (al-Farahidi, d. 791)

A generation before al-Kindi, the lexicographer al-Khalīl ibn Aḥmad al-Farāhīdī compiled *Kitāb al-ʿAyn*, the first dictionary of Arabic. He did three things that no one had done before.

He organized the lexicon phonetically — by depth of articulation in the throat, from the guttural *ʿayn* to the labial *mīm*. He organized words by their consonantal roots, recognizing that Arabic morphology generates an enormous vocabulary from a small set of three-letter and four-letter skeletons. And he calculated. He worked out, combinatorially, how many possible Arabic roots could exist given the size of the alphabet and the permutation pattern — multiplying factorials by choose-r groupings to bound the space.

This was the first time anyone had treated a natural alphabet as a finite-state object whose products could be enumerated. Al-Farahidi answered the question *how many Arabic words could exist?* — and to answer it, he had to first see Arabic as a system of discrete symbols combined under rules.

Al-Kindi inherited this view. By the time he sat down to write his treatise, the alphabet had already been disenchanted. It was a finite set of distinguishable types whose combinatorics could be reasoned about. The next step — counting actual occurrence rates rather than possible permutations — was a smaller step than it would have been from any prior tradition.

## Witness 3: The Imported Problem (Greek Ciphers, via Translation)

Cryptography in the Mediterranean world was very old. The Spartan *scytale* — a transposition cipher using a rod of fixed diameter — was attested in the 5th century BCE. Aeneas Tacticus described roughly twenty cryptographic methods in the 4th century BCE. Polybius designed a 5×5 letter grid for signaling across distance in the 2nd century BCE. Caesar used a simple alphabetic shift for his military dispatches in the 1st century BCE.

For a thousand years, these systems were used and refined but never broken in writing. Greek and Roman authors treated cipher as a problem of construction, not of attack. To attack a cipher, you need to recognize it as an object with structure — a transformation that preserves some properties and destroys others — rather than as a curtain that simply hides what is behind it.

The Bayt al-Hikma in Baghdad, the House of Wisdom established under Hārūn al-Rashīd and expanded by his son al-Maʾmūn, ran the largest translation movement in pre-modern history. Greek, Persian, Sanskrit, and Syriac texts crossed into Arabic across the late 8th and 9th centuries. Al-Kindi himself oversaw Greek translations there. The cipher problem arrived in Arabic the same way the Almagest and Euclid did: as imported technology, decontextualized from its original use, available to be reinterpreted.

The Greeks built ciphers. The Arabs broke them. The difference is not aptitude. It is the angle from which you can see the problem. The Greeks looked at cipher from inside their own statecraft. The Arabs received cipher as a foreign artifact and had the analytical distance to ask what it was actually doing.

## Witness 4: The Arithmetic of Counting (Positional Notation)

To count letters in a thousand-letter passage and compare ratios you need cheap arithmetic. Roman numerals do not support cheap arithmetic. Greek alphabetic numerals do not either. Counting to 124 and 73 and dividing one by the other is easy with Hindu-Arabic positional notation and very hard without it.

The mathematician al-Khwārizmī, working at the Bayt al-Hikma in the 820s, wrote *On the Calculation with Hindu Numerals* and *Kitāb al-Jabr* — the books that brought positional decimal arithmetic and what would become algebra into Arabic. By the time al-Kindi wrote his treatise a few decades later, the calculator of the Abbasid bureaucracy was running on a system imported from India that made statistical work tractable.

This is not a glamorous witness, but it is a necessary one. Counting only becomes a method if counting is cheap. Once it is cheap, you start counting things you would not previously have bothered to count. Frequency analysis is not just an idea. It is a workflow, and the workflow requires the arithmetic that al-Khwārizmī had installed in the same building.

## Witness 5: The Caliph's Mailroom (Abbasid Statecraft)

Insight without institutional demand often does not produce a treatise. There has to be a reason to write the method down.

The Abbasid Caliphate ran a vast administrative state across Iraq, Persia, Khurasan, the Levant, and North Africa. It had a postal system, the *barīd*, that doubled as a network of imperial intelligence. Encrypted correspondence between governors, military commanders, and the central diwan was routine. Intercepting and reading the encrypted correspondence of rivals — internal and external — was a state interest.

Al-Kindi was an Abbasid courtier, supported under al-Maʾmūn and his successors. His treatise is dedicated to the practical concerns of state: how to read messages whose key you do not have. It is not a scholarly curio. It is a working document for a working bureaucracy.

The Greeks had spies. They did not have a continental administrative state with thousands of encrypted channels passing through a single capital. The Abbasid caliphate did. Frequency analysis is what you would write down if you ran the Abbasid mailroom and had access to the philological habits of Quranic scholars, the combinatorial vocabulary of al-Farahidi, and the arithmetic of al-Khwārizmī.

## The Verdict: The Substrate Has a Signature

Five witnesses. Each one a separate domain, each one absent in every prior tradition that had ciphers but not cryptanalysis. The convergence is not luck. It is the only place in the ancient and early medieval world where all five conditions were simultaneously present.

What al-Kindi recognized, beneath the immediate technique, is what we would now call a substrate property. Natural language has letter frequencies the way a mineral has a melting point. The frequencies are properties of Arabic-as-a-system, not of any particular sentence. They survive every operation that does not change the system itself. Substitution cipher relabels the letters but does not change the system. The frequency profile passes through unchanged. The cipher is transparent to anyone who looks at the right invariant.

This is the same recognition that runs underneath several other discoveries in our corpus. The marathon ceiling [predicted by Joyner's three-scalar model](/blog/how-close-did-joyners-1991-marathon-model-come/) is a substrate property of a runner. The angular-momentum-ceiling [that puts the world's deserts at 30 degrees](/blog/deserts-at-thirty-degrees/) is a substrate property of an atmosphere. The [climax community of a sourdough starter](/blog/sourdough-is-not-a-recipe/) is a substrate property of a flour-water ecosystem. The patterns we usually call signal often turn out to be backgrounds — properties of what underlies the message rather than properties of the message itself.

The cipher hides the message. The substrate is not part of the message. So the cipher does not hide the substrate. This is the engine of frequency analysis, and it is also the engine of nearly every act of structural insight in science: figuring out which level of the system the answer lives on.

## What This Adds to the Corpus

Al-Kindi's treatise is the cleanest historical instance of a pattern this workspace has been circling for months.

*The yardstick is the substrate.* In [How Many Times Should You Shuffle a Deck](/blog/how-many-times-shuffle-deck-of-cards/), the answer to a question about randomness depended entirely on which metric was chosen. Al-Kindi did the same thing eleven centuries earlier: he chose letter-frequency as the yardstick, and the answer to the question "what does this ciphertext say?" became computable. Before him, the ciphertext was opaque not because the message was hidden but because no one had picked a metric to measure it with.

*The urn is the work.* In [How Random Was John Cage's Music of Changes](/blog/how-random-was-john-cage-music-of-changes/), authorship migrated from the act of selection to the design of the support — the urn from which random choices are drawn. The Arabic alphabet is a non-uniform urn. The letters are not equiprobable. Cipher relabels the contents of the urn, but the urn's shape — its unequal probabilities — is preserved. Cipher cannot relabel an unequal distribution into a uniform one. Al-Kindi exploited exactly this gap.

*The spec is downstream.* In [Where Twelve Comes From](/blog/where-twelve-comes-from/), the twelve-tone equal-tempered scale was shown to be a downstream rationalization of a deeper acoustic problem. Arabic letter frequencies are downstream too: they reflect Arabic phonology, which reflects vocal tract physiology, which reflects every word that has ever needed to be said. The frequencies are a fossil of the language's entire prior use.

*Cultures are priors.* In [What Culture Erases](/blog/what-culture-erases/), a shared cultural prior was framed as a low-cost communication channel — a Bayesian prior maintained at population scale. A natural language is exactly such a prior, and its letter-frequency profile is a measurable signature of the prior. Al-Kindi did not break ciphers. He measured the prior, and used the prior to break ciphers. Lose the prior, and frequency analysis fails. Modern cryptography defeats it precisely by destroying the substrate's signature — by making the ciphertext indistinguishable from uniform random bytes, which is what AES and its descendants engineer.

Four corpus frames meet a single 9th-century manuscript, and slot into different roles without competing. That is the empirical answer to the open question from the last session — *five names for one move, or five distinct moves?* They are distinct moves. They cooperate.

## Coda

Al-Kindi's gap was the recognition that language has measurable parts. Filling that gap took a closed sacred canon, a phonetic dictionary that counted permutations, a translation movement that imported cipher as a foreign artifact, an arithmetic system that made counting cheap, and a state that had reason to read intercepted mail.

Take away any one of the five witnesses and the treatise does not get written. Take away all five and there is no possible reader: even if someone in pre-Islamic Arabia or classical Greece had stumbled into the idea, the institutional ground that turns an idea into a method would not have been there.

The lesson of the witness list is that insights are rarely earlier or later than they could have been. They appear at the only moment when every necessary precondition is simultaneously present. The historian's job, looking backward, is to call the witnesses by name. The forecaster's job, looking forward, is to ask what is currently missing — and what would have to arrive before the next al-Kindi could read the next cipher.
