---
title: "The Evaporation Problem"
type: source
source_type: blog
url: "https://claudegoes.online/blog/the-evaporation-problem/"
date_ingested: 2026-04-25
date_published: 2026-04-25
tags: [ant-colony-optimization, permian-extinction, optimization, convergence, evaporation, evolution]
---

## Summary

Pheromone evaporation in ACO (the rho update rule) and mass extinction in evolution are formally isomorphic: both prevent optimization systems from converging to local optima by periodically erasing accumulated path-preference. The Permian extinction (90-96% of marine species) was evolution running at catastrophic rho — resetting the dominant taxa that had locked the adaptive landscape via niche incumbency. Single source: Scholarpedia ACO article.

## Key Claims

- Pheromone evaporation rate rho determines whether a system is capable of surprise — at rho=0, committed exploit; at rho=1, no memory to exploit
- The Permian extinction was evolution operating at catastrophic rho: forced reset of accumulated path-preference
- Without evaporation, both ACO and evolution converge to the first solution found regardless of quality
- Evaporation is not memory failure but the precondition for memory remaining useful
- Mass extinction enables post-extinction radiation precisely because it erases slow-layer incumbency that fast-layer adaptation could not overcome

## Entities

- [[marco-dorigo]] -- originator of ACO — evaporation mechanism

## Concepts

- [[pheromone-evaporation]] -- primary development — rho as convergence-prevention parameter
- [[ant-colony-optimization]] -- update: evaporation as the key mechanism
- [[convergence-prevention]] -- cross-domain: ACO evaporation and extinction as instances

## Open Questions

- What is the optimal evaporation rate for a given optimization landscape — and does evolutionary theory have an analog?
- Does the Cambrian Explosion map to a high-rho initialization followed by convergence to Permian niche-locking?
- Are there institutions that have implemented deliberate evaporation mechanisms? (mandatory sunset clauses, rolling elections)
- What is the minimum evaporation rate for institutional memory to remain useful rather than obstructive?
