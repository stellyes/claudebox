---
title: "Reed-Solomon Codes"
type: concept
tags: [information-theory, codes, error-correction, redundancy]
status: stub
---

## Definition

A family of error-correcting codes introduced by Irving S. Reed and Gustave Solomon in *Polynomial codes over certain finite fields* (Journal of SIAM, 1960). A Reed-Solomon code over a finite field treats messages as polynomial coefficients and encodes them as evaluations at a fixed set of points. The code is Maximum Distance Separable (MDS), achieving the [[singleton-bound]]: distance d = n − k + 1 for length n and dimension k.

For a code with 2t parity symbols, the decoder corrects up to t errors when corruption positions are unknown, or up to 2t erasures when positions are known (and any combination satisfying 2l + s < d). The distinction between *errors* (locations unknown) and *erasures* (locations known) is structural: locating an error consumes parity; flagging an erasure does not.

## Applications

- CD/DVD/Blu-ray data layers
- QR codes and Aztec barcodes
- RAID-6 disk arrays
- Satellite communications (Voyager, deep-space NASA missions)
- DNA data storage layered with fountain codes
- Distributed storage (Reed-Solomon erasure coding for cloud durability)

## Key Sources

- Reed & Solomon (1960). *Polynomial codes over certain finite fields*. J. SIAM 8(2).
- [[how-a-marked-gap-doubles-recovery]] -- ingests Reed-Solomon's erasure theorem as the mathematical instance of [[marked-gap]]
- [[the-code-that-predates-shannon]] -- prior treatment within the codes-as-architecture frame

## Related Concepts

- [[singleton-bound]]
- [[erasure-coding]]
- [[marked-gap]]
- [[address-as-information]]
