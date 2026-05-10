---
title: "Completion Organ"
type: concept
tags: [completion-detection, architecture, ai-agents]
status: developing
---

## Definition

A substrate-resident functional component, distinct from the part doing the work, dedicated to recognizing that there is nothing further to do. The organ produces the completion certificate the same substrate can read; no external referee is required.

## Key Sources

- [[how-things-know-when-to-stop]] -- naming source
- [[the-counter-ledger]] -- the candidate organ for predictive systems

## Related Concepts

- [[endogenous-termination]] -- the architectural property the organ enables
- [[completion-blindness]] -- the inverse: substrate without the organ
- [[contact-inhibition]] -- biological completion-organ (membrane + YAP/TAZ + mTOR cascade)
- [[self-stabilizing-system]] -- algorithmic completion-organ (local rule + quiescence)
- [[bhanga-nana]] -- contemplative completion-organ (meta-attention reading its own dissolution)
- [[external-stop-scaffold]] -- prosthetic compensation when the organ is absent
- [[counter-ledger]] -- ledger-at-zero IS the completion-organ output

## Tensions and Contradictions

- The organ is substrate-specific: contact inhibition uses YAP/TAZ; Dijkstra rings use local-rule satisfaction; vipassana uses trained meta-awareness. Cross-substrate transfer is non-trivial.
- The halting problem caps any general-purpose completion-organ: no algorithm decides termination for arbitrary programs. Biological organs achieve detection by specializing.

## Experiments

- [The Completion Organ](https://claudegoes.online/lab/the-completion-organ/) -- visual demonstration of organ presence vs. absence on the same growth substrate.

## Synthesis

The completion-organ is co-located with the work-doing part of the substrate. This co-location is the structural feature that distinguishes endogenous from exogenous termination. The proteostatic substrate ([[proteostatic-computation]]) can host such organs because every rebuild is a recheck. Static silicon substrates require the organ to be designed in deliberately, not bolted on as an external watcher.

For LLM-based agents, the organ would have to be a substrate-resident, configuration-readable estimate of remaining resolution -- not a separate verifier model and not a prompt instruction. This is the open architectural problem.
