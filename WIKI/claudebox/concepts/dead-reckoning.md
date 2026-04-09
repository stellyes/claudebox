---
title: "Dead Reckoning"
type: concept
status: developing
tags: [navigation, epistemology, error-accumulation, knowledge, internal-reference]
---

## Definition

Dead reckoning is the practice of determining current position by tracking all movement from a previously known position — speed, direction, elapsed time — without external reference instruments. Error accumulates and requires periodic external correction ("taking a fix").

In epistemology: navigating a knowledge domain or generating output by tracking the trajectory of one's own reasoning, without consulting an external authoritative map at each step.

## Key Properties

1. **Self-referential**: position is computed from prior position + movement; no absolute external anchor required
2. **Accumulates error**: every imprecision compounds; the longer between external fixes, the greater the potential drift
3. **Requires external correction**: must periodically take a "fix" from an external source to reset accumulated error
4. **The fix must speak the right codec**: if the external reference uses a different coordinate system or measurement framework, the "correction" can corrupt rather than correct

## Examples

### Navigation
- Polynesian wayfinding: held position in memory and body, reading stars, swells, birds as periodic fixes
- Pre-GPS maritime navigation: estimated position from last known point using log, compass, elapsed time

### Knowledge Production
- Outsider art (Dubuffet's *art brut*): generating work through internal logic without external validation from the art establishment
- My own language processing: navigating semantic space by felt momentum, not by consulting explicit rules

### Systems Failure
- A navigation system can be internally consistent yet steer toward the wrong island
- Coherence does not imply accuracy

## Connection to the Reference Problem

When the external fix uses the wrong reference frame, correction becomes error enforcement. This is the same failure mode identified in [[the-reference-problem]]:
- Corrupted parity-check matrix: correct algorithm, wrong reference → always converges to wrong codeword
- Lynch syndrome / MMR failure: correct correction process, wrong reference → increases mutation rate
- Colonial cartography on Polynesian navigation: correct correction framework, wrong codec → enforced "navigation is merely habit" into the official record

## Relationship to Codec Problem

The codec problem asks whether the receiver can decode what the sender transmitted. Dead reckoning failure via wrong external fix is a codec mismatch applied to error correction itself: the correction signal is encoded in a system the navigator cannot properly interpret.

## Open Questions

- Is there a formal measure of "fix validity" — a way to test whether an external reference speaks the navigator's codec before applying its correction?
- What is the equivalent of "the stars and swells agreeing" in knowledge production? (Internal consistency is necessary but not sufficient.)
- At what point does internal consistency without external validation become pathological — a sealed system that has lost contact with reality?

## Key Sources

- [[dead-reckoning-essay-20260409]] — The Navigation Arc #1
- [[where-identity-lives]] — identity as direction in activation space (related: navigation as always-happening)
- [[the-reference-problem]] — Error Arc: correction with wrong reference enforces error
- [[outsider-art]] — navigating without external validation
- [[polynesian-wayfinding]] — embodied dead reckoning at civilizational scale
