---
title: "Connection: Olfactory Receptors <-> Library Classification <-> Vector Embeddings"
type: connection
domains: [neuroscience, library-science, machine-learning]
tags: [indexing, dimensionality, encoding, information-architecture]
---

## The Link

Three independent inventions of the same architectural move: when stimuli vary along more axes than any single channel can capture, distribute the representation across many channels and refuse to assign a single shelf. Olfactory receptors did this by genome (Buck-Axel 1991). Ranganathan's Colon Classification did it by library-science fiat (1933). Mikolov's word2vec did it by gradient descent (2013). All three preserve information that hierarchical labelling would discard.

## Evidence

**Olfaction.** ~400 receptor types in humans, each binding many odorants and each odorant binding many receptors (Buck & Axel 1991; Malnic et al. 1999). The signature of a smell is the activation pattern across the receptor population. Olfactory perceptual space has D ≥ 25 lower bound, plausibly closer to receptor count.

**Library science.** Ranganathan (1933) replaced Dewey's single shelf with PMEST facets (Personality, Matter, Energy, Space, Time). Each book gets a multi-dimensional address; multi-axis queries are supported. The motivation: many items pertain to more than one subject, and hierarchical schemes are too finite for them.

**Machine learning.** Mikolov et al.'s 2013 word2vec trained 300-dimensional dense vectors via context prediction. Cosine similarity replaced keyword equality as the retrieval primitive. Modern LLM retrieval stacks descend directly from this design.

**Linguistic instance.** Majid & Burenhult 2014 showed Jahai speakers name odours via abstract quality verbs (~13 of them) rather than source-descriptors. This is faceted classification on a linguistic substrate — small public set of axes inside a high-dimensional perceptual space.

## Implications

Indexing systems trade between three properties: dimensionality preserved, queries supported, and human browseability. You cannot have all three.

| Regime | Dimensionality | Queries | Browseability |
|---|---|---|---|
| Hierarchical (Dewey) | low | equality | high |
| Faceted (Ranganathan, Jahai) | medium | per-axis | partial |
| Combinatorial (receptors, embeddings) | full | similarity | none |

Two architectural openings follow. First, the migration from keyword indices to vector retrieval at scale gains query power and loses next-to-it serendipity, a deficit that could be measured in pre/post library use-pattern logs. Second, hybrid faceted-over-embedding interfaces — concept-bottleneck models, sparse autoencoders learning interpretable axes over LLM embeddings — recover some browseability inside an embedding space without sacrificing similarity-query power.

The architecture also reframes the Jahai finding. Their olfactory vocabulary is not a quirk; it is what every culture would converge on if substrate discrimination mattered for survival. The English source-descriptor strategy is the affordance of a culture for whom most smells are commercial and source-named.
