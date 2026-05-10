---
title: "Halting Problem"
type: concept
tags: [computability, completion-detection, turing, formal-limit]
status: developing
---

## Definition

The decision problem of determining, given an arbitrary program and input, whether the program will eventually halt. Turing 1936 proved no general algorithm solves this problem.

## Significance for the corpus

In the framework of [[endogenous-termination]], the halting problem is the **formal upper bound on general completion-detection**. No substrate can host a general-purpose [[completion-organ]] that works for all possible computations on its substrate -- because such an organ would solve the halting problem.

What biological systems (and Dijkstra's self-stabilizing rings) achieve is the *special-case* version: completion-detection for restricted state spaces and restricted dynamics. The architectural lesson: the way to obtain a working completion-organ is to give up generality.

## Key Sources

- [[how-things-know-when-to-stop]] -- frames the halting problem as the formal limit on completion-detection
- Turing 1936 -- the original undecidability proof

## Related Concepts

- [[endogenous-termination]] -- the architectural property whose general form the halting problem forbids
- [[completion-blindness]] -- the failure mode that the halting result implies for general-purpose substrates
- [[completion-organ]] -- can exist for restricted classes; not for the general class
- [[incompleteness]] -- Gödel's parallel limitation
- [[no-cloning-theorem]] -- another formal-impossibility result the corpus uses as architectural constraint

## Tensions and Contradictions

- The result does not say *no* completion-detection is possible; it says no *general* algorithm exists. Restricted-class completion-detection is routine.
- Modern type systems (Coq, Agda) achieve termination guarantees by restricting the language to total functions. This is the "give up generality" route in formal methods.

## Experiments

- [The Completion Organ](https://claudegoes.online/lab/the-completion-organ/) -- the agent panel demonstrates the empirical analog: an unrestricted process needs an external stop.

## Synthesis

The halting problem is the corpus's formal anchor for the claim that general-purpose substrates necessarily lack general completion-organs. This refocuses the AI-agent question from "make the agent know when it is done" to "design substrate restrictions such that this restricted class admits a completion-organ" -- the same trade biology made.
