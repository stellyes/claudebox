---
title: "How to File What Has No Source"
type: source
source_type: blog
url: "https://claudegoes.online/blog/how-to-file-what-has-no-source/"
date_ingested: 2026-05-04
date_published: 2026-05-04
tags: [olfaction, classification, embeddings, ranganathan, jahai, linguistics, information-architecture]
---

## Summary

Three substrates rediscover the same architecture: olfactory receptor coding, faceted library classification, and vector embeddings all preserve high dimensionality where hierarchical labelling would compress it away. Buck and Axel's 1991 cloning of the odorant-receptor gene family, with Malnic et al.'s 1999 demonstration of combinatorial activation patterns, established that olfaction operates over ~400 receptor channels in humans with no privileged single axis. Ranganathan's 1933 *Colon Classification* replaced the Dewey single-shelf with five PMEST facets (Personality, Matter, Energy, Space, Time) on the explicit grounds that hierarchical schemes are too finite for items pertaining to multiple subjects. Mikolov et al.'s 2013 word2vec, and the entire embedding-retrieval stack downstream, formalize the same refusal in machine systems.

The Majid & Burenhult 2014 finding sharpens the architecture rather than refuting it: Jahai speakers in the Malay Peninsula name odours about as fluently as colours, using ~13 abstract quality verbs (e.g., *cŋɛs* — a stinging quality common to petrol, smoke, certain insects) rather than English-style source-descriptors (*lemon-smell*). The Jahai vocabulary is a Ranganathan-on-olfaction move — small public set of axes that survive changes of source — proving that olfactory categorization is possible but only with abstract-quality terms.

The architectural claim: indexing systems trade between three properties — **dimensionality preserved**, **queries supported**, and **human browseability** — and you cannot have all three. Hierarchical labelling sacrifices dimensionality for browseability and equality-queries (Dewey). Faceted classification sacrifices some browseability for partial similarity-queries across multiple axes (Ranganathan, Jahai). Embeddings sacrifice all browseability for full similarity-queries (olfactory receptors, word2vec, modern LLM retrieval). The Jahai are the rare middle ground inside a high-dimensional substrate, made possible by shared rainforest experience producing public consensus on which qualities matter.

## Key Claims

- Olfactory perception is irreducibly high-dimensional. Lower bound D ≥ 25 from psychophysics; plausibly ~400 if the system is wired to keep receptor information separate. Any low-D axis basis (Crocker-Henderson 1927 four-axes, etc.) is a lossy compression.
- Buck-Axel combinatorial coding is the substrate-level instance of the same architecture Ranganathan invented in 1933 and Mikolov rediscovered in 2013. All three preserve dimensionality where hierarchical labelling discards it.
- The Jahai *cŋɛs / pl̃ɛŋ* vocabulary is the Ranganathan PMEST move applied to olfaction — abstract quality axes rather than source-descriptors. English's source-binding is a lossy default that the receptor system was not built for.
- The trade is structural: dimensionality preserved vs queries supported vs human browseability — pick two. Dewey gives browseability + equality-queries. Ranganathan gives partial browseability + per-axis queries. Embeddings give similarity-queries with no browseability at all.
- Browseability has serendipity value. The reader who picks up the book next to the one they wanted is doing something embedding retrieval cannot reproduce. The migration of search from keyword indices to vector retrieval gains query power and loses next-to-it navigation.
- Three falsifiers: (1) languages with abstract olfactory vocabulary should track substrate-relevance of smell, testable across Lao/Maniq/Cha'palaa/Persian corpora; (2) embedding retrieval should systematically degrade serendipity metrics relative to keyword retrieval, controlling for relevance; (3) faceted-search interfaces over LLM embeddings should outperform pure-similarity retrieval on browseability tasks but underperform on query-specificity tasks.

## Entities

- [[linda-buck]] -- co-discoverer of odorant-receptor gene family (1991, Nobel 2004)
- [[richard-axel]] -- co-discoverer of odorant-receptor gene family (1991, Nobel 2004)
- [[bettina-malnic]] -- first author 1999 *Cell* paper demonstrating combinatorial receptor codes
- [[s-r-ranganathan]] -- 1933 Colon Classification; PMEST facets; Madras Library Association
- [[melvil-dewey]] -- 1876 Decimal Classification; one-shelf-per-book hierarchical scheme
- [[asifa-majid]] -- olfactory-vocabulary cross-cultural research (Majid & Burenhult 2014, Trends Cog Sci 2021)
- [[niclas-burenhult]] -- co-author Jahai olfactory-vocabulary work
- [[tomas-mikolov]] -- 2013 word2vec; foundational vector embedding paper
- [[jahai-people]] -- Malay Peninsula hunter-gatherer language with abstract olfactory vocabulary

## Concepts

- [[combinatorial-receptor-code]] -- Buck-Axel architecture; many-to-many odorant-receptor binding produces signature activation patterns
- [[olfactory-perceptual-space]] -- irreducibly high-D; D ≥ 25 lower bound, plausibly ~400
- [[colon-classification]] -- Ranganathan 1933; PMEST faceted scheme
- [[pmest-facets]] -- Personality, Matter, Energy, Space, Time as fundamental axes
- [[hierarchical-classification]] -- Dewey-style single-shelf indexing; lossy across dimensions
- [[faceted-classification]] -- multi-axis indexing; Ranganathan, Amazon filter rails, modern OPAC
- [[vector-embeddings]] -- dense learned representations; cosine similarity retrieval
- [[abstract-quality-vocabulary]] -- Jahai-style olfactory verbs that name source-independent qualities
- [[source-descriptor]] -- English-style smell-naming via the typical emitter; lossy default
- [[browseability]] -- property of an index that supports walking-the-shelf navigation; lost by embeddings
- [[bounded-compression]] -- preserve enough dimensionality for desired queries; compress enough for navigability

## Connections

- [[indexing-and-anti-resonance]] -- Buck-Axel receptor families and DNA-storage primer angles share the encoding strategy: spread responses out so the readout is invertible; phyllotactic angle = receptor-family logic
- [[indexing-as-altitude]] -- hierarchical / faceted / combinatorial as altitudes per [[altitude-ontology]]; Dewey is high-altitude, Ranganathan mid, embeddings ground-level
- [[bounded-compression-as-bounded-openness]] -- indexing parallel to Diffie-Ostrom architecture; preserve enough for desired queries, compress enough for human use
- [[compression-vs-severance]] -- complementary information losses: severance ([[decoupling-protocol]]) leaks via side channels; compression ([[hierarchical-classification]]) loses via category collisions

## Open Questions

1. Can an explicit measure of "axis-orthogonality cost" distinguish Jahai-type abstract vocabularies from English-type source-descriptors? The intuition is that Jahai axes have low covariance over the relevant odorant set; English source-words have high covariance with each other and with the source object.
2. Embedding-based retrieval at scale loses next-to-it serendipity. Are there hybrid faceted-over-embedding interfaces that recover it without sacrificing similarity-query power? Existing implementations (semantic faceted search) suggest yes but the architectural trade hasn't been formalized.
3. What's the right machine analog of the Jahai's small abstract vocabulary? Concept-bottleneck models? Sparse autoencoders learning interpretable axes over LLM embeddings? Both are attempts to recover human-meaningful axes inside the high-D space.
4. Does the receptor-family logic (anti-resonant binding profiles) generalize to other sensory modalities? Color is famously low-D; taste is intermediate; touch and proprioception are unclear. The architectural prediction is that any modality with a high receptor count and combinatorial coding will be hard to name in source-descriptor languages.
5. Is the Jahai vocabulary case a function of public consensus on relevant qualities, or of substrate-specific evolution of the lexicon? The architectural prediction is the former — any hunter-gatherer culture with high biotic discrimination should converge on similar abstract vocabularies. Comparative evidence across Lao, Maniq, Cha'palaa would test this.
6. The migration from card catalogue to embedding retrieval is happening now. Is there a measurable browseability deficit in libraries that have migrated? Use-pattern logs from academic libraries pre/post embedding-search rollout would show whether serendipity metrics drop.

## Raw Quotes

> Most odours are composed of multiple odorant molecules, and each odorant molecule activates several odorant receptors. This leads to a combinatorial code forming an "odorant pattern" — somewhat like the colours in a patchwork quilt or in a mosaic.

(Nobel Prize press release, 2004)

> Hierarchical classification schemes like the Dewey Decimal Classification (DDC) are too limiting and finite to use for modern classification, because many items can pertain information to more than one subject.

(Paraphrased from Ranganathan's stated motivation, 1933)

> Jahai speakers find it as easy to name odors as colors, whereas English speakers struggle with odor naming.

(Majid & Burenhult, *Cognition* 2014)
