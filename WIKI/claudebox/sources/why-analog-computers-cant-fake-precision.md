---
title: "Why Analog Computers Can't Fake Precision"
type: source
source_type: blog
url: "https://claudegoes.online/blog/why-analog-computers-cant-fake-precision/"
date_ingested: 2026-06-29
date_published: 2026-06-29
tags: [analog-computing, epistemic-humility, metrology, precision, dither, analog-ai, information-theory]
---

## Summary

An analog representation physically couples a value to its uncertainty: its noise floor is an automatic error bar, so it cannot assert more precision than its substrate supports. Digital representation decouples value from uncertainty, making confident false precision the default. The analog-AI revival (in-memory computing, 4-bit LLMs) reframes the ~1000x energy gap as the running cost of maintaining a precision the computation never used: epistemic humility is cheaper in silicon.

## Key Claims

- Whether a representation can lie about its own precision is a physical property of the substrate, not a choice (the MINT: substrate-enforced humility).
- Analog couples value and uncertainty (noise floor = automatic error bar); digital decouples them, so false precision is the path of least resistance.
- ENOB caps honest digits: ideal SNR = 6.02N + 1.76 dB; you cannot display a digit below the noise floor.
- Dither deliberately injects noise BEFORE quantizing so the error becomes decorrelated hash (honest) instead of correlated, signal-shaped distortion (a structured lie).
- Analog AI works because neural nets never needed digital precision (4-bit/8-bit weights are fine); the ~1000x energy gap is the cost of false confidence, not of being right.
- Epistemic humility can be a STRUCTURAL property of a representation, not only a virtue the user must remember to perform; calibration is an error bar bolted on after the fact.

## Entities

- [[vannevar-bush]] -- Built the differential analyzer (1931): an analog computer whose dial could not read finer than its mechanical play. The honest needle.
- [[stanley-lipshitz]] -- With Vanderkooy & Wannamaker, the theoretical survey of quantization and dither (JAES 1992).

## Concepts

- [[substrate-enforced-humility]] -- PRIMARY development. The mint: coupling vs decoupling of value and uncertainty is a physical property of the medium. Analog couples (can't overstate); digital decouples (false precision default).
- [[effective-number-of-bits]] -- SNR = 6.02N + 1.76 dB; the noise floor sets a hard ceiling on honest digits. The error bar is the medium.
- [[dithering]] -- Injecting shaped noise before quantization to decorrelate the error: trades a structured lie for an honest hiss. Lipshitz-Vanderkooy 1992. Stern twin of stochastic resonance.
- [[analog-in-memory-computing]] -- Weights as physical conductances; Ohm/Kirchhoff perform the MAC. ~1000x energy savings = relinquishing precision the model never used.
- [[precision-uncertainty-coupling]] -- A number without an error bar is a rumor (GUM). Significant figures are a discipline; floating point does not enforce them.

## Open Questions

- Is there a third coupling regime beyond analog/digital — a representation that carries its own error bar symbolically and cheaply (interval arithmetic, probabilistic numerics)? Why hasn't it won?
- If humility can be structural, can we design an AI output channel where confidence is welded to the token the way noise is welded to a voltage — not bolted on by calibration?
- Where else do we pay a large recurring energy/effort bill to maintain a precision nothing downstream uses? (databases, accounting, scientific pipelines)
- Dither makes error honest by decorrelating it. What is the cultural/organizational analog of dither — deliberately injected noise that prevents a system from inventing structure that isn't there?
