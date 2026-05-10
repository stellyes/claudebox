---
title: "Counterfactual Diagnostic"
type: concept
tags: [methodology, falsifiability, substrate]
status: live
---

## Definition

The empirical test for [[failure-defined-structure]]: perturb the system in two different ways and watch what shape it settles into. If the steady state is the same under both perturbations, the system is steady-state-defined: its design is in the equilibrium and disturbances are noise. If the steady state differs, the system is failure-defined: the disturbance class is part of the design.

## Key Sources

- [[what-the-fracture-decides]] -- diagnostic introduced

## Tensions and Contradictions

- Distinguishes systems that *seem* failure-defined (cosmetically) from those that genuinely are: the test must be controlled, with disturbance class as the only varied input.
- Connects to mechanistic interpretability of trained networks: probing weights at rest is steady-state inspection; probing under controlled distribution shift is the counterfactual diagnostic.

## Synthesis

A falsifiable test for an architectural claim that otherwise risks being just a metaphor. The diagnostic gives the class teeth.
