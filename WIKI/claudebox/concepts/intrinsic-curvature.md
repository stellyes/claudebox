---
title: "Intrinsic Curvature"
type: concept
tags: [differential-geometry, architecture, forced-trade, structure]
status: developing
---

## Definition

A property of a structure that survives any embedding -- it can be measured from *inside* the structure without reference to an ambient space. In differential geometry: Gaussian curvature K of a surface (Theorema Egregium). Generalized in [[why-you-cannot-flatten-a-sphere]] across three domains:

- **Geometric**: Gaussian curvature for surfaces (Theorema Egregium 1827).
- **Network-topological**: partition possibility for distributed networks (CAP).
- **Constraint-graph**: base-rate divergence across groups (algorithmic-fairness impossibility).

When curvature is intrinsic, no representation can flatten it; trade-offs become structural. The choice of *which* property to sacrifice is a values decision; the necessity of *some* sacrifice is not.

## Key Sources

- [[why-you-cannot-flatten-a-sphere]] -- generalizes intrinsic curvature beyond differential geometry
- [[theorema-egregium]] -- the foundational case
- [[cap-theorem]] -- the network-topological case
- [[algorithmic-fairness-impossibility]] -- the constraint-graph case

## Related Concepts

- [[forced-trade]] -- the architectural class produced by intrinsic curvature
- [[tissot-indicatrix]] -- the visualization tool: deformation signature of intrinsic curvature
- [[dimensional-escape]] -- the dual; extrinsic curvature dissolves with enough ambient dimension

## Tensions and Contradictions

The hardest open question is what unifies the three notions of "intrinsic" listed above. In differential geometry the criterion is exact; in CAP it depends on a partitioning model; in algorithmic fairness it depends on a base-rate assumption. Whether there is a single theorem that yields all three as instances is unresolved.

## Synthesis

Intrinsic curvature is the diagnostic. If the curvature is intrinsic, you face a forced trade and the working question is *which property do you sacrifice and what is that worth*. If the curvature is extrinsic, you have been representing the problem badly and the right move is to find more dimensions. The whole game is knowing which one you have.
