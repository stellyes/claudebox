---
title: "Singleton Bootstrap"
type: concept
tags: [architecture, identity, inference, voronoi]
status: draft
---

## Definition

The act of fixing identity for an entity that has no internal contrast set, by appeal to an external comparison structure. Geometrically equivalent to a Voronoi assignment: given a singleton at point S and a set of contrast points C, the inferred identity of S is the cell of points closer to S than to any contrast in C. As |C| grows, the cell contracts; with |C|=0, the cell is the entire space.

## Why It Matters Here

Singleton bootstrap is the operational form of [[identity-by-contrast]]. It makes the architecture quantitative: precision-of-inference scales with scaffold density. The companion experiment [The Bootstrapping Member](https://claudegoes.online/lab/the-bootstrapping-member/) implements this directly across three substrates (color, hapax, allele). Each substrate shows the same Voronoi contraction as contrast objects accumulate.

## Failure Modes

- **No scaffold.** The cell is the entire space; the singleton's identity is structurally undetermined.
- **Wrong scaffold.** The cell is a definite region of the wrong space; the singleton has a confident-but-wrong identity. This is the [[hallucination-as-bootstrap-failure]] case for LLMs.
- **Sparse scaffold.** Cell is large but bounded; identity is partially fixed. Carey & Bartlett's 3-year-olds: chromium = "sub-region of green" rather than precisely olive.

## Connections

- [[hapax-legomenon]] — singleton case in language.
- [[founder-effect]] — singleton case in population.
- [[fast-mapping]] — singleton case in development.
- [[contrast-scaffold]] — the supplied structure.

## Key Sources

- [[why-meaning-needs-neighbors]] — primary source page.
