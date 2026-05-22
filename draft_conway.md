# Why the Conway Knot Took 50 Years to Untie

In 2018, a graduate student named Lisa Piccirillo learned about an open problem in knot theory at a conference. She solved it in less than a week. The Conway knot, an 11-crossing tangle that John Conway had drawn in the late 1960s, had resisted every attempt to determine whether it bounds a smooth disk in four-dimensional space. The list of mathematicians who had tried and failed includes essentially everyone who works in the field. Piccirillo's proof appeared in the *Annals of Mathematics* in 2020.

She did not invent a new invariant. She did not run a new computation. She found a *different knot* with the same four-dimensional properties as the Conway knot and asked the question there. The new knot answered easily.

That is the move, and it is older than knot theory.

## Is the Conway knot slice?

A knot is *slice* if it bounds an embedded disk in the four-ball — that is, if you can fill the knot in with a disk that lives one dimension up. Why care? Because sliceness is the cleanest test of which knots are, in a four-dimensional sense, trivial. A slice knot is one that could be the equator of an honest two-dimensional disk hiding in four dimensions; if you had four-dimensional eyes, you could see why it cannot really be tied.

Around 1970, Conway published an enumeration of all knots up to 11 crossings. Most of the sliceness questions were quickly resolved using classical tools. One holdout remained for 50 years: the knot now known as 11n34, the *Conway knot*. Every classical invariant that other mathematicians threw at it stayed silent.

The real question wasn't whether Conway's knot was slice. It was whether anyone could see far enough into four dimensions to tell.

## Is it slice topologically, or smoothly?

This question only makes sense if there is more than one way to bound a disk. There is.

In 1982, Michael Freedman classified topological four-manifolds and proved, among other things, that the Conway knot is *topologically* slice — it bounds a disk that is merely continuous and locally flat. The same year, Simon Donaldson proved that the smooth category in dimension four is wild in a way no other dimension is wild: there exist smooth structures on Euclidean four-space that are not the standard one. Topological four-manifolds can carry uncountably many distinct smooth structures, or none at all, in ways that dimensions three and five cannot.

So the topological category and the smooth category disagree in dimension four. A topologically slice knot may or may not be smoothly slice. The Conway knot was known to be topologically slice in the 1980s, and the smooth question stayed open for thirty more years.

The question wasn't "is it slice." It was "in which category does the bounding disk live?" Dimension four is the only dimension where that question can have two different answers.

## Why didn't the invariants tell us?

Knot theory is built on invariants — numbers, polynomials, homology groups that you can compute from a diagram of a knot, with the property that any two diagrams of the same knot give the same answer. The Alexander polynomial. The Jones polynomial. The signature. Each one is a *projection* of the knot down to something simpler, and the price of projection is information loss.

The Conway knot has the same Alexander polynomial as the unknot (trivially 1). It has the same Jones polynomial as the *Kinoshita–Terasaka knot*, an 11-crossing knot discovered by Kinoshita and Terasaka in 1957 in *Osaka Mathematical Journal*. Conway and Kinoshita–Terasaka are related by an operation called *mutation* — cutting out a four-ended tangle and gluing it back after a 180-degree rotation — which preserves almost every classical invariant.

The Kinoshita–Terasaka knot is smoothly slice. Conway might or might not be. Every invariant strong enough to distinguish them on sliceness was, until 2018, also fooled by mutation.

This is the same architecture as the [letter-frequency analysis](/blog/why-frequency-analysis-was-born-in-baghdad/) story from al-Kindi's Baghdad: the substrate (the alphabet's frequency profile, here the knot's four-dimensional shape) has a signature, and the relabeling (substitution cipher, here mutation) preserves the signature even as it scrambles the surface. The invariants saw the relabeling and concluded the substrates were the same.

## Can we just compute more invariants?

Yes — and people did. In the early 2000s, Mikhail Khovanov categorified the Jones polynomial, replacing a polynomial with a chain complex whose Euler characteristic recovers the polynomial. Jacob Rasmussen's 2010 *Inventiones* paper showed how to extract from Khovanov homology an integer-valued invariant — the *s-invariant* — that gives a lower bound on the smooth slice genus. If s(K) is nonzero, K is not smoothly slice. The s-invariant is sensitive to information the Jones polynomial loses.

Compute s of the Conway knot. You get zero. So the s-invariant cannot rule it out. The Kinoshita–Terasaka knot, being slice, also has s = 0. Mutation again.

The real question wasn't "do we have a strong enough invariant" but "what *object* should the invariant be computed on." Invariants are tied to an object. The Conway knot was the wrong object.

## Is the question about the knot?

Take the four-ball B⁴. Pick a knot K sitting on its boundary three-sphere. Attach a *two-handle* — thicken a disk and glue it onto the boundary along K, with the standard framing. The result is a four-manifold called the *zero-trace* X₀(K). It is what you get when you fill in the knot with a disk and remember the disk's neighborhood.

Here is the lemma that broke the problem: K is smoothly slice if and only if X₀(K) embeds smoothly in S⁴. Sliceness is not really a property of the knot. It is a property of the trace.

That means two knots with the same trace must have the same sliceness. They are *trace-equivalent*. The classical invariants — Alexander, Jones, signature, Khovanov, s-invariant — are functions of the knot diagram and can differ on trace-equivalent knots, even though the property the invariants are *supposed to* detect cannot differ. The invariants were looking at the diagram. The property was hiding in the four-manifold.

Once you accept this reframing, the strategy becomes obvious. To resolve a knot's sliceness, find another knot with the same trace whose s-invariant is computable and nonzero.

The question wasn't about the Conway knot. It was about the manifold the Conway knot bounds.

## Can we find another knot with the same trace?

In the 2000s, John Osoinach described an operation called *annulus twisting*: take a knot with a specific embedded annulus, twist along the annulus, and you get a different knot whose trace is the same. Most knots do not have such an annulus, and most annulus twists do not produce knots whose s-invariant is computable to a useful value. The Conway knot does have an annulus presentation, and Piccirillo's contribution was to find an annulus twist that produces a knot K' for which Rasmussen's s-invariant computes to nonzero.

She computed s(K') and got a nonzero value, so K' is not slice. By the trace lemma, since X₀(Conway) = X₀(K') and K' is not slice, Conway is not slice.

That is the entire proof, modulo the diagrammatic gymnastics needed to verify the trace equality and the (substantial) computation of s on a knot with a few dozen crossings.

The real question wasn't "is the Conway knot slice." It was "which knot, equivalent to the Conway knot at the level where the property lives, gives the property up?"

## Did Piccirillo find a new invariant?

No. The s-invariant existed before her work, as did the trace construction and the annulus-twisting machinery. Each piece had been used by other people for other purposes. Piccirillo's contribution was to assemble them and identify the right K' — the *witness*. The intellectual move was not invention. It was *translation*.

This is the same architecture as what Évariste Galois did when [he could not solve the quintic](/blog/why-the-quintic-has-no-formula/). The quintic equation has no general formula in radicals; everyone before Galois had tried to find one and failed. Galois translated the question. He stopped asking "is there a formula" and started asking "what does the group of permutations of the roots look like." A formula in radicals corresponds to a *solvable* group. The quintic's permutation group, A₅, is the smallest nonabelian simple group and is not solvable. The answer to the original question fell out of the answer to the translated question, because the translated question was being asked of the right object.

The Conway move is a knot-theoretic Galois move. Stop asking about the knot. Ask about the four-manifold the knot bounds, then find a representative of that manifold's equivalence class whose surface diagram you can compute on.

## Is this a knot-theory move or a more general one?

It is the same move that John Cage's *Music of Changes* puts on display in a different register. As the [Cage essay](/blog/how-random-was-john-cage-music-of-changes/) argues, the work is not the score — the work is the *urn* of chance operations that produced the score. To analyze the music, do not analyze the notes; analyze the operations. Cage chose his substrate; what came out was downstream.

It is the same move [Michael Joyner](/blog/how-close-did-joyners-1991-marathon-model-come/) made when he predicted the men's marathon floor not by predicting a race but by translating a marathoner into three numbers — VO2max, lactate threshold, running economy — and predicting *those*. The translation moved the question to where the physiology was, not where the race happened to be staged.

It is the move that turns linguistic competence into a phonotactic distribution that a frequency-counting cryptanalyst can attack, the move that turns morphogenesis into a reaction-diffusion equation, the move that turns the sliceness of a knot into the embedding of a four-manifold.

Stated abstractly: when a question about object X resists every direct attack, the property you are asking about may live one level up, on some richer structure that X is one instance of. Find a different instance whose surface is friendlier. Ask the question there.

The move has been around for at least a century and a half. It is not specific to mathematics; it shows up wherever someone gets stuck and recovers by changing what they are looking at. What Piccirillo showed is that it still works on problems where every direct tool has been tried and failed.

## How long was the question really open?

If you mark its opening at Conway's 1969 enumeration, the question was open for 51 years. But this answer is misleading. The trace construction wasn't formalized until much later. The s-invariant didn't exist until 2004. Khovanov homology didn't exist until 2000. Donaldson's wildness in dimension four wasn't proven until 1982. The annulus-twisting machinery wasn't published until the 2000s. Each component of the eventual proof took decades to come into being.

What this resembles is the [250-year search for stellar parallax](/blog/250-year-null-result-stellar-parallax/) — Tycho looked, Hooke looked, Bradley looked, and they all failed not because parallax wasn't there, but because their instruments couldn't see it. Their nulls weren't dead ends; they were measurements of an upper bound on parallax, and that bound told you the universe was much bigger than anyone had wanted to admit.

For 50 years, the world's knot theorists also returned null. Each null measured a lower bound on the cleverness required. The Conway knot wasn't unknowable; it was a measurement of how much machinery a proof would have to draw on. The bound was 50 years of accumulating tools, ending in 2018 when one person assembled them.

The real question wasn't how long the problem stayed open. It was what the answer's eventual price would be.

## What gets untied when the knot is untied?

The Conway knot is not slice. That is the answer Piccirillo gave. It completes the classification of slice knots with at most 12 crossings. It also gives the first example of a knot that is topologically slice but not smoothly slice *and* is a positive mutant of a slice knot — the cleanest possible witness to the asymmetry of mutation under sliceness.

But the larger thing that got untied is the assumption that the knot itself was the relevant object. Piccirillo's proof retrofits onto the 50-year history a different telling: not that the invariants weren't strong enough, but that they were being asked of the wrong thing. The Conway knot was a label for an equivalence class — the class of all knots with that particular zero-trace — and the property of sliceness lived on the class, not on any one representative. The invariants saw the representative.

Once that is named, the corpus has another instance of a pattern it has been tracking: the property you want to measure lives somewhere other than the object you can hold. The substrate has a signature, the urn is the work, the marathon is three scalars, the trace is the manifold. The knot was hiding in plain sight on top of the only thing that mattered, and for 50 years everyone looked at the knot.

Lisa Piccirillo looked at what the knot was sitting on.

---

*This essay's structure follows a constraint: each section asks an apparent question and reveals a deeper one. The move is the essay's subject — the Conway knot was undetectable because the apparent question (is K slice?) was hiding the real one (does X₀(K) embed?). Piccirillo's trick was to recognize that and translate.*
