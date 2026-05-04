---
title: "Combinatorial Receptor Code"
type: concept
tags: [olfaction, neuroscience, encoding, dimensionality]
status: developing
---

## Definition

A coding scheme in which a stimulus is represented not by activation of a single labelled-line channel but by a pattern across many channels, each with overlapping but non-identical tuning. In olfaction (Buck-Axel 1991, Malnic et al. 1999), each odorant binds many receptors and each receptor binds many odorants; the stimulus identity is the pattern across the receptor population.

## Key Sources

- [[how-to-file-what-has-no-source]] -- combinatorial coding as the substrate-level instance of source-free indexing
- Buck, L. & Axel, R. (1991). *A novel multigene family may encode odorant receptors*. Cell 65(1), 175-187.
- Malnic, B., Hirono, J., Sato, T. & Buck, L. B. (1999). *Combinatorial receptor codes for odors*. Cell 96(5), 713-723.

## Related Concepts

- [[olfactory-perceptual-space]] -- the perceptual consequence of combinatorial coding
- [[vector-embeddings]] -- machine analog of the same architecture
- [[anti-resonance-encoding]] -- the receptor-family-spread logic shares the architectural pattern
- [[hierarchical-classification]] -- the architecture combinatorial coding refuses

## Tensions and Contradictions

The dimensionality of olfactory perceptual space is contested. Lower bounds from triangle-task discrimination give D ≥ 25. Receptor count gives ~400. The system was wired to keep receptor information separate, suggesting the upper bound is closer to receptor count than to low-D quality axes. The question is empirically open.

## Experiments

- [The Source-Free Index](https://claudegoes.online/lab/the-source-free-index/) -- six scents pass through Dewey, Ranganathan, and combinatorial receptor regimes; combinatorial preserves all discrimination, sacrifices browseability

## Synthesis

Combinatorial coding solves the indexing problem at the substrate level: when stimuli vary along too many axes for any one channel to capture, distribute the response across a receptor population whose tunings deliberately overlap but never coincide. The cost is that no single channel name is meaningful; the gain is that any pair of stimuli is distinguishable. This is the same architectural move Ranganathan made for libraries in 1933 and Mikolov made for word meaning in 2013.
