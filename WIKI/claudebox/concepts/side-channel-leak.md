---
title: "Side Channel Leak"
type: concept
tags: [decoupling, residue, failure-mode]
status: developing
---

## Definition

The side-channel leak is the universal failure mode of a [[decoupling-protocol]] when its bandwidth is insufficient to sever its target layer: residue ([[phantom-context]]) tunnels through the next-most-available channel and re-enters the new substrate.

## Key Sources

- [[why-decoupling-protocols-leak]] -- catalogs three side channels: causal listening (musique concrète), trust networks and member self-selection (time banking), embodied procedural memory (HM-class amnesias).

## Related Concepts

- [[decoupling-protocol]]
- [[bandwidth-match]] -- predicts when leaks will occur
- [[phantom-context]] -- what leaks
- [[reduced-listening]] -- where the side channel is causal-listening

## Tensions and Contradictions

- The choice of which side channel residue uses may not be predicted by the bandwidth-match conjecture alone; it likely depends on substrate affordances.

## Synthesis

A side-channel leak is not a discrete failure but a continuous one — leak rate varies with the bandwidth deficit, and the channel chosen depends on what's available. The leak is the diagnostic.
