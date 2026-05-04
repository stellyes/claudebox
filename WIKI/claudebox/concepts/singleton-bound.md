---
title: "Singleton Bound"
type: concept
tags: [information-theory, codes, theorem]
status: stub
---

## Definition

Singleton's bound (R. C. Singleton, 1964) is a theorem stating that for any block code of length n, dimension k, and minimum Hamming distance d, the inequality d ≤ n − k + 1 must hold. Codes that achieve equality (d = n − k + 1) are called *Maximum Distance Separable* (MDS) codes. Reed-Solomon codes are the canonical MDS family.

## Why It Matters Here

The Singleton-bound-achieving structure is what makes Reed-Solomon's 2l + s < d theorem (correct l errors and s erasures simultaneously) tight. With l = 0 it gives 2t erasures; with s = 0 it gives t errors. The 2:1 ratio that anchors [[marked-gap]] architecture in [[how-a-marked-gap-doubles-recovery]] depends on this maximality.

## Key Sources

- Singleton, R. C. (1964). *Maximum distance q-nary codes*. IEEE Transactions on Information Theory 10(2).
- [[how-a-marked-gap-doubles-recovery]]

## Related Concepts

- [[reed-solomon]]
- [[erasure-coding]]
- [[marked-gap]]
