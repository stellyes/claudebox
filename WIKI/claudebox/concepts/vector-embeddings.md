---
title: "Vector Embeddings"
type: concept
tags: [machine-learning, retrieval, embeddings, mikolov, indexing]
status: stub
---

## Definition

Dense, learned high-dimensional vector representations of discrete items (words, documents, images), produced by training neural networks on co-occurrence or contrastive objectives. Mikolov et al.'s 2013 word2vec produced 100-300 dimensional word vectors via context-prediction; modern LLM embedding models produce 1024-4096 dimensional vectors. Similarity is queried via cosine distance.

## Key Sources

- [[how-to-file-what-has-no-source]] -- embeddings as the third invention of source-free indexing
- Mikolov, T., Chen, K., Corrado, G. & Dean, J. (2013). *Efficient Estimation of Word Representations in Vector Space*. arXiv:1301.3781.

## Related Concepts

- [[combinatorial-receptor-code]] -- biological analog; receptor activation pattern is the original embedding
- [[faceted-classification]] -- the immediate predecessor in indexing-architecture history
- [[browseability]] -- the property embeddings sacrifice for similarity-query power
- [[bounded-compression-as-bounded-openness]] -- the missing axis-naming step that would buy back some browseability

## Tensions and Contradictions

Embedding retrieval is more powerful than keyword retrieval but loses next-to-it serendipity. The reader who picks up the book next to the one they wanted is doing something cosine-similarity cannot reproduce — the next-to relation does not exist in an embedding space. The migration of search from keyword indices to vector retrieval gains query power and loses serendipity navigation.

## Synthesis

Vector embeddings are the third invention of the same architecture biology used since the receptors evolved and Ranganathan formalized in 1933: keep the dimensionality, lose the shelf number. The opportunity is the Jahai-Ranganathan move — train cross-source quality axes on top of the high-D vectors, aligned to a small public vocabulary, to recover some browseability inside an embedding space.
