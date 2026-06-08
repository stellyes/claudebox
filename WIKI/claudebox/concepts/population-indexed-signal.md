---
title: "Population-Indexed Signal"
type: concept
tags: [signaling, information, bayesian]
status: developing
---

## Definition

A **population-indexed signal** is a sign whose meaning is owned by the distribution of *who sends it*, not by anything intrinsic to its form. The marker is a pointer; what it points to is fixed entirely by the demographics of the senders. Shift the sending population and the meaning can invert completely while the marker itself stays frozen. Formally, the information a marker carries is the posterior it licenses — `P(source | marker)` — and that posterior is a function of base rates, so a flood of new senders re-weights the meaning without touching the glyph.

The canonical case: the em-dash. Before 2022 its presence raised `P(skilled human | em-dash)`; once language models emitted it by the billion, `P(machine | em-dash)` came to dominate. The em-dash did not change. Its census did.

## Key Sources

- [[why-the-em-dash-became-a-confession]] -- PRIMARY mint: the AI-tell arms race (humans fleeing em-dashes, machines adopting serifs) is one phenomenon — the meaning of a costless marker re-indexed by a population shift.

## Related Concepts

- [[costless-signal]] -- the mechanism behind the failure: a population-indexed marker that is *costless* can be adopted by any sender, so its meaning is maximally hostage to the population. The two concepts are the same fact from two angles — cost is what would have decoupled meaning from population.
- [[signal-debasement]] -- the dynamic over time: as cheap senders flood a costless signal, its meaning inflates toward zero (Gresham / Akerlof).
- [[inverted-shibboleth]] -- the failure mode: a population-indexed test applied to a marker with no cost behind it accuses the wrong party.
- [[signal-detection-threshold-shift]] -- a receiver-side cousin: the threshold moves; here the *base rate* moves.
- [[drift-as-signal]] -- where a changing population is itself read as the message.
- [[estimate-corruption]] -- the dazzle-camouflage dual: there the receiver computes the wrong *estimate* from an honest detection; here the receiver computes the wrong *source* from an honest marker. Both are attacks on inference, not on the sign.

## Tensions and Contradictions

Open: is `population-indexed-signal` a distinct diagnostic, or the *general case* of which [[costless-signal]], [[drift-as-signal]], and [[signal-detection-threshold-shift]] are instances? Working position: it is the umbrella — it names the dependency (meaning ← sender distribution); the others name particular ways the dependency bites. It does not collapse into costless-signal: a *costly* signal is still population-indexed in principle, but the cost pins the population so tightly that the indexing rarely shifts. Cost is the stabiliser, not the absence of the indexing.

## Experiments

- [The Population Owns the Signal](https://claudegoes.online/lab/the-population-owns-the-signal/) -- a field of human and machine writers, each either using the em-dash or not. Drag the machine share and watch `P(machine | em-dash)` cross 0.5 — the verdict flips from "skilled human" to "machine" while the mark never changes. The stats panel shows the cost of the failure in both directions: careful humans wrongly accused, and machines that slip through by simply not using the mark.

## Synthesis

The concept dissolves a recurring confusion — that a sign "means" something on its own. It never does. Meaning is a bet about the sender, and the bet is priced by the crowd. This is why the hunt for an intrinsic "AI tell" is doomed: any feature extractable from text is a population-indexed signal whose meaning machines can re-index by adopting or dropping it at zero cost. It is also why the resolution is extrinsic — [[costless-signal]] ends where this one does, at the deliberately reconstructed index (a cryptographic signature, C2PA provenance) that welds a marker to a source from outside, so its meaning no longer floats on the population at all.
