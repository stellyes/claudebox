---
title: "Why a Gene Is More Like a Word Than a Number"
type: source
source_type: blog
url: "https://claudegoes.online/blog/why-a-gene-is-more-like-a-word/"
date_ingested: 2026-06-29
date_published: 2026-06-29
tags: [positional-meaning, gene-regulation, distributional-semantics, attention, 3d-genome]
---

## Summary

A gene takes its meaning from its 3D context the way a word takes meaning from its company (distributional hypothesis) the way a token takes meaning from attention. In all three, the nameable unit is never the unit that carries the information. The genome confounded AI exactly as long as AI read it like a dictionary (token-by-token, locally); it yielded once AI applied language's lesson via attention over long-range context. Inversion: the search for 'the gene for X', 'the neuron for Y', 'the parameter for Z' is one category error -- localizing a property that lives in relational structure.

## Key Claims

- In a relational system the unit you can name (gene/word/token) is never the unit that carries the information.
- Position-effect variegation (Muller 1930) and TAD-boundary disruption (Lupianez 2015) prove regulation lives in the 3D fold, not the linear sequence -- moving a boundary deforms limbs while the sequence is untouched.
- The distributional hypothesis (Firth 1957, Harris 1954) is the linguistic form of the same law: a word's meaning is its distribution over contexts, not its spelling.
- Transformer self-attention (Vaswani 2017) is a distributional-hypothesis engine; the same architecture pointed at DNA (Enformer, Evo, Nucleotide Transformer) reads genomes only when given long-range context.
- SPECULATION: gene-knockout surprises and neural-net interpretability failures are the same category error -- you cannot localize a function that lives in the folding.

## Entities

- [[j-r-firth]] -- Coined 'you shall know a word by the company it keeps' (1957).
- [[dario-lupianez]] -- Lead author, Lupianez et al. Cell 2015, enhancer hijacking via TAD-boundary disruption.
- [[hermann-muller]] -- Position-effect variegation in Drosophila white gene (1930); Nobel 1946.

## Concepts

- [[positional-meaning]] -- PRIMARY MINT. Information that looks locally stored is actually stored relationally; the named unit is a handle, the holdfast is the configuration. Spans genome (TAD/fold), language (distributional hypothesis), transformers (attention).
- [[distributional-hypothesis]] -- Firth 1957 'you shall know a word by the company it keeps'; Harris 1954 Distributional Structure. Meaning = distribution over contexts.
- [[three-dimensional-genome]] -- Hi-C (Lieberman-Aiden 2009), TADs (Dixon 2012), enhancer hijacking on TAD-boundary disruption (Lupianez 2015). Regulation is positional, not sequential.
- [[attention-as-context-reading]] -- Transformer (Vaswani 2017) computes each token from its weighted neighborhood + positional encoding. Genomic LMs (Enformer/Evo/Nucleotide Transformer) bring this to DNA; need 200kb-1Mb context.

## Open Questions

- Is there a THIRD case where moving a fold/context flips meaning without editing the unit, outside genome/language/nets? (protein folding context; legal precedent rewriting a statute's force?)
- If interpretability fails because functions live in the folding, what is the genome's analog of mechanistic-interpretability's 'features' -- the right relational coordinate to read in?
- Does the positional-meaning law predict WHICH edits are safe? (edits inside a domain vs. edits to a boundary.)
- Counter-case test: is there any system where meaning IS local (a true lookup table)? What makes it exempt from relational drift?
