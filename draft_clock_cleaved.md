# Why Circadian Was the One Behavior Mendelism Worked For

In 1965, Seymour Benzer was the world's leading bacteriophage geneticist. He had spent a decade dissecting the rII gene of T4 phage into more than 2,000 mutational sites — the finest-grained genetic map ever assembled. Then he left it. He moved to Caltech, set up a fly room, and bet that the rough Mendelism of phage genes could be carried, intact, into a brain.

The bet was not quite right and not quite wrong. Across the next decade his lab and others screened Drosophila for behavioral mutants — for vision, for learning, for courtship, for shaking under ether, for falling out of beam-balance tests. The screens found genes. They almost never found Mendelism in the sense Benzer started with. The dosage of one gene did not give you a quantitative gradient of a behavior.

Except once.

In 1971, Ronald Konopka, Benzer's graduate student, isolated three mutants on the X chromosome that produced not one phenotype but three: a fly whose circadian period ran fast at 19 hours, a fly whose period ran slow at 28 hours, and a fly whose period collapsed altogether. The three alleles mapped to the same locus. The dosage of one gene gave you a quantitative gradient of a behavior. They named it *period*.

It is the only time this has ever happened cleanly.

What follows is the census.

## Entry 1: phototaxis (1967)

Benzer's first published screen was for walking toward light. He let mutagenized flies walk down a tube and counted what fraction made it to the light end. He found mutants — many — that lost the preference. But the behavior was already the sum of several systems: photoreceptors, motor coordination, the decision to walk at all. A "non-phototactic" mutant could be blind, lame, or unmotivated. The screen scored a yes-or-no on the integrated output. It found genes. It did not find a function from one gene to a number.

## Entry 2: shaker (Kaplan & Trout 1969)

William Kaplan and William Trout, also Caltech, anesthetized flies with ether and watched them shake their legs in irregular bursts as they came out from under. They found mutants that shook more, kept shaking longer, or shook with different temporal patterns. Several lines mapped to a single locus called *shaker*. Eighteen years later, Lily and Yuh Nung Jan cloned the gene and discovered it encoded a voltage-gated potassium channel — the first such channel cloned in any organism. The screen worked. But the behavioral output was a categorical observation under a fluorescent light: did this fly twitch under ether or not? There was no graded scale on which the alleles arranged themselves.

## Entry 3: dunce (Dudai, Jan, Byers, Quinn & Benzer 1976)

A learning screen. Flies were trained to associate one odor with electric shock, then offered a choice between that odor and a control. Wild-type flies avoided the trained odor. *Dunce* mutants did not. The mutation mapped to a single locus and, in 1981, Duncan Byers showed it disrupted the gene encoding cyclic AMP phosphodiesterase. A clean single gene, a clean biochemical lesion. But the behavioral phenotype was, again, binary: did the fly learn or not. Mutants differed slightly in how badly they failed the test. No one ever saw an allelic series of "dunces" with finely graded learning quality. The screen could resolve presence from absence; it could not resolve quantity.

## Entry 4: fruitless (Hall 1978; Ryner et al 1996)

The screen targeted male courtship. A *fruitless* male would court other males as well as females and would fail to copulate. The behavioral phenotype was rich and pleiotropic — courtship song, orientation, attempted mating, all simultaneously affected. The mutation mapped to a single locus. Twenty years later, Lisa Ryner and Barbara Taylor's group at Oregon State showed that *fruitless* encoded a transcription factor whose mRNA was alternatively spliced in a sex-specific manner — the gene was downstream of the sex-determination cascade. A single gene, yes, but its molecular biology was so wired into developmental sex that no allelic series of "courtship quality" was possible. You could not tune the gene to court 30% more.

## Entry 5: norpA (Pak, Grossfield & Arnold 1970)

The vision screens at Purdue used the electroretinogram — a needle electrode in the eye, recording the photoreceptor's response to a light flash. Mutants without a normal waveform were classified by which feature of the trace was missing. *norpA* (no receptor potential A) eliminated the receptor potential entirely. The gene, cloned in 1988, encoded a phospholipase C — a single biochemical step in the phototransduction cascade. The screen found a single gene cleanly. But the readout was a presence-or-absence of a waveform feature, not a graded behavioral measurement. Different *norpA* alleles gave you "still has signal" or "doesn't" — not a continuum.

## Entry 6: period (Konopka & Benzer 1971)

The screen counted when adult flies emerged from their pupal cases ("eclosion") under constant darkness. In wild type, eclosions occur in clusters with a 24-hour period — the flies remember the dawn even when the dawn is gone. Konopka tested mutagenized lines for this rhythm. He found three. One eclosed every 19 hours. One every 28. One never clustered at all. The same screen, run on the same locus, gave him three different numerical phenotypes — a continuum punctuated by a null. This is what the other screens did not produce.

The locomotor activity of individual flies, recorded separately, showed the same three periods. Not just population eclosion: the clock was inside each fly, with the same numbers.

The fly is two millimeters long. The clock is a number. The number depends, by dosage, on a single locus.

## The Pattern in the Census

Read down the list. The screens that produced single genes are the majority. Phototaxis, shaker, dunce, fruitless, norpA — each cleaved at one locus. Benzer's phage-style logic transferred. What did not transfer was the quantitative part. *period* alone gave a behavior whose dose-response curve to the gene was visible.

The difference is not in the gene. *period* is not biochemically more elegant than the others. The phosphodiesterase of *dunce* is a more familiar enzyme. The channel of *shaker* is a more important molecule. The transcription factor of *fruitless* sits closer to the brain's developmental program.

The difference is in the readout. *Period* yields a number that runs along the real line. The same fly, observed for a week, gives you 24.07 or 19.16 or 28.43. You can take a mean. You can compute a confidence interval. You can draw a histogram. You can ask whether the histogram for one allele is shifted from the histogram for another by a continuous amount.

The other behaviors do not yield numbers in this sense. "Did the fly learn?" is a Bernoulli trial. "Did the fly court?" is a Bernoulli trial of a multi-stage script. "Does the fly shake under ether?" is observed by eye. You can make these quantitative — count successes, time the bouts — but the underlying behavior is a categorical event that either occurred or did not. There is no native real-valued axis along which alleles can space themselves.

## The Mechanism That Lets a Scalar Behavior Exist

Why does *period* give a number? Because the underlying machinery is, transparently, an oscillator with a single rate-limiting step. Paul Hardin, Jeffrey Hall, and Michael Rosbash showed in 1990 that PER protein accumulates in the nucleus, represses its own gene's transcription, and is degraded — a delay-feedback loop. Michael Young's lab found TIMELESS (1994) and DOUBLETIME (1998), the partners that determine when PER reaches the nucleus and how fast PER is degraded.

The period of such a loop is set by the slowest step — in this case, the rate of PER turnover, which DOUBLETIME (a casein kinase I homolog) phosphorylates PER to set. Allelic variants of *period* slow or speed PER's behavior in this loop. Each allele shifts the period of the oscillator by a continuous amount. Period is the scalar output of a delay-line.

The other behaviors are not single delay-lines. Learning is the integration of a stimulus history; courtship is a state machine with branch points; phototaxis is a decision among competing reflexes. None of these has a single rate-limiting parameter that, if perturbed, would yield a one-parameter family of output curves.

In other words: *period* gave Mendelism a target only because the underlying biology happens to be a delay-feedback oscillator whose period depends, almost trivially, on a single time constant. The molecular oscillator is the kind of thing we have called <a href="/blog/why-identical-twins-have-different-fingerprints/">a chosen amplifier</a> — a mechanism designed (here by selection, not by an embryologist) to take microscopic variation in a single rate constant and write it permanently into a macroscale output. Twin fingerprints write down noise; the circadian oscillator writes down gene dosage. The amplifier is what makes the readout scalar.

## What This Says About Reductionism

There is a question hidden in the census. Reductionism — the program of finding single genes for complex traits — works in proportion to whether the trait has a real-valued output controlled by a single rate-limiting variable. It does not work in proportion to whether the underlying biology is "simple" or "elegant" in some deeper sense.

Philip Anderson, in his 1972 essay <em>More Is Different</em>, argued that emergent levels of organization had their own laws and could not be predicted from below. The census suggests a corollary. Reductionism finds clean single-gene answers when the emergent level happens to expose a scalar parameter to the underlying machinery. When it doesn't, reductionism finds genes — many of them — but loses the gradient. The screen still works as a finding device. It stops working as a measuring device.

This rhymes with <a href="/blog/how-many-times-shuffle-deck-of-cards/">a recent observation about deck shuffling</a>, where the question "how many shuffles" has a different answer depending on which metric one uses to measure mixing — the yardstick is the substrate of the answer. Here it is not the metric that is chosen; the metric is given by the biology. Some behaviors expose a real-valued axis to genetics. Most do not. The screen will still find a gene; it will not find a series of alleles spaced along a line.

It rhymes with another, deeper observation as well. In <a href="/blog/sourdough-is-not-a-recipe/">Sourdough Is Not a Recipe</a> the argument was that some systems behave like recipes (single causal chain, controllable, deviation = technique error) while others behave like ecosystems (founder communities, multiple attractors, deviation = different stable state). Most behaviors are ecosystems in this sense — the brain is an ecosystem, learning is an ecosystem of associations, courtship is an ecosystem of sub-routines. Circadian rhythm, almost alone, is a recipe. *Period* is its main ingredient.

## What Else Has This Shape?

If the diagnostic for Mendelian-tractable behavior is "a scalar output that depends on a single rate-limiting step," then we can predict where the next allelic series might come from. Sleep duration is plausible — sleep is partially controlled by the same circadian machinery and has a single output (hours per cycle). Voice pitch in songbirds has been studied with a small number of clean genes (FOXP2 lineage), and the output is a number. Cardiac rhythm — both vertebrate and the larval Drosophila heart that *period* itself affects — is another candidate. The marathon predicted by <a href="/blog/how-close-did-joyners-1991-marathon-model-come/">Michael Joyner's 1991 three-scalar model</a> has the same character: a number on the real line, traceable to a small number of physiological rate constants. Where physiology yields a clock — where the behavior IS a number — Mendelism works.

Most behaviors will not have this shape. Most behaviors are integrals over histories, not values of delay-line oscillators. The census does not predict that we will find genes for them; it predicts that when we do, the genes will not arrange themselves into allelic series on a real number line.

What Konopka found in 1971 — three flies, three numbers, one gene — is not the template for behavior genetics. It is the exception that defines the limit. The dog that almost didn't bark, except this time it did, exactly once, on a clock.

---

The 2017 Nobel Prize in Physiology or Medicine went to Hall, Rosbash, and Young for their work on the molecular mechanism the gene encodes. Konopka was not on the citation. He had died in 2015. Benzer had died in 2007. The gene they screened for is in every mammalian cell. We carry it now.
