---
title: "Erasure Coding"
type: concept
tags: [information-theory, codes, error-correction, redundancy]
status: stub
---

## Definition

A class of error-correcting codes in which corruption positions are *known* to the decoder (an "erasure" rather than an "error"). For a Reed-Solomon code with distance d = n − k + 1 (Singleton-bound-achieving), the decoder corrects any pattern of l errors and s erasures provided 2l + s < d. With l = 0 you correct 2t erasures; with s = 0 you correct t errors. Same code, doubled capacity when corruption is marked.

The mathematical reason is that error correction has two phases: locate (using parity to find an error-locator polynomial via Berlekamp-Massey or Euclidean algorithm) and estimate magnitude. They share the same parity budget. Marking erasures in advance does the locate step by hand, freeing all parity for magnitude estimation.

## Key Sources

- [[how-a-marked-gap-doubles-recovery]] -- erasure coding as the mathematical instance of [[marked-gap]]; the 2:1 ratio is the architecture
- [[the-code-that-predates-shannon]] -- broader treatment of error-correcting codes including Reed-Solomon as instance

## Related Concepts

- [[reed-solomon]] -- the canonical erasure code
- [[singleton-bound]] -- proves the 2:1 ratio
- [[marked-gap]] -- the abstracted architecture
- [[redundancy]] -- the parity substrate

## Applications

- RAID arrays mark whole failed drives as erasures; reconstruction is faster than scanning for unknown corruption.
- Streaming protocols flag dropped packet IDs and resend at half the redundancy cost.
- DNA data storage uses erasure codes with sequencing dropouts marked as erasures.
- QR codes use Reed-Solomon for partial-block recovery.

## Cross-Pollination

The architecture generalizes far beyond engineering. In the marked-gap framing, any system that addresses its absences (sacramental seal, microsleep EEG marker, ZKP verifier-state) is doing erasure decoding on the appropriate substrate.
