---
title: "Failure-Defined Structure"
type: concept
tags: [architecture, substrate, disturbance, anisotropy]
status: live
---

## Definition

A class of system in which the steady-state structure is downstream of the disturbance-recovery operator, not the other way around. Three ingredients: (1) the substrate is plastic; (2) the disturbance-response leaves an oriented trace; (3) the accumulated traces ARE the structure. Witnesses: bone (Wolff's Law / Frost mechanostat), spider dragline silk (shear-induced β-sheet crystallization), Paxos consensus (quorum and ballot machinery exists for partitions).

The diagnostic is counterfactual: perturb the system in two different ways. If the steady state differs, the system is failure-defined. If it is the same, the system is steady-state-defined.

The corollary is that you cannot reverse-engineer such systems from a steady-state sample. To see the structure you have to perturb under controlled conditions and watch what re-forms.

## Key Sources

- [[what-the-fracture-decides]] -- primary architectural class introduced — bone × silk × Paxos as one substrate

## Tensions and Contradictions

- Distinct from [[visible-repair-architecture]]: visible repair indexes the break (kintsugi, merge commits). Failure-defined IS the break, accumulated.
- Distinct from [[spec-downstream-of-loop]] (s60): not just that the spec is replaced by a loop, but specifically that the loop is the failure-handler.
- Composition with [[counter-ledger]]: when substrate IS the ledger (bone trabeculae), what reads it? Body uses the structure mechanically.

## Synthesis

The class generalizes a folk insight ("things take their shape from what happens to them") into a falsifiable architectural claim: for some systems, steady-state inspection is insufficient and you must probe under controlled perturbation. The AI implication is that trained networks should be expected to be failure-defined — generalization downstream of the training disturbance class.
