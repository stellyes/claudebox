---
title: "Path Independence"
type: concept
tags: [systems, mathematics, physics, philosophy]
status: developing
---

## Definition

A system exhibits path independence when its final state is determined by the parameters of its potential or constraint structure, with no reference to the trajectory by which the state was reached. Two systems started differently and run differently end in the same place.

The property is produced by a [[closure-law]] — a mechanism that absorbs the path. Without a closure law operating, path-dependence is the default: history is part of the structure, and the final state cannot be specified independent of the route.

## Where It Holds

- Strictly convex optimization (geometric closure)
- Normalizing reductions in Church-Rosser systems (syntactic closure)
- Equilibrium thermodynamics with fast relaxation (temporal closure)
- State functions in physics (energy, entropy, free energy) — the canonical case
- Pure mathematics: theorems are path-independent in their proofs

## Where It Fails

- [[failure-defined-structure]] — bone, silk, Paxos protocols
- Glasses and metastable solids that retain cooling history
- Biological evolution
- Neural network training (partial — see [[linear-mode-connectivity]])
- Most coalition / institutional / cultural dynamics

## Why It Matters

The distinction is methodological. When path-independence holds, one can predict the final state by minimizing the appropriate potential — this is the entire engineering paradigm of "specify the design, solve the optimization." When it fails, one has to model the trajectory itself; sampling the steady state is not enough information.

A great deal of standard scientific practice (taking measurements at rest, reverse-engineering from samples) implicitly assumes path independence. For systems in which the assumption is wrong, the practice produces misleading data — studying bone with no record of loading, weights with no record of optimizer trajectory.

## Related Concepts

- [[closure-law]] -- the mechanism that produces path independence
- [[failure-defined-structure]] -- the opposite regime
- [[editorial-trajectory]] -- another name for the closure-governed regime
- [[counterfactual-diagnostic]] -- the test that distinguishes the two regimes empirically

## Synthesis

Path independence is not a feature of "good" or "well-designed" systems. It is a feature of systems with the right structural property — a closure law. Many engineered systems have closure by design (well-posed optimization problems, deterministic algorithms with confluent operational semantics, reactors operated near equilibrium). Many physical systems acquire closure by limit (the ideal crystal at T → 0). Most biological and social systems lack closure entirely, and to describe them as if they had it is to lose their structure.
