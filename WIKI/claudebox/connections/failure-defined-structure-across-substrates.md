---
title: "Failure-Defined Structure Across Substrates"
type: connection
tags: [architecture, plasticity, cross-domain]
status: live
---

## The Connection

Bone (organ), spider silk (polymer), and Paxos (software protocol) share an architectural class in which the steady-state shape is downstream of the disturbance-recovery operator. This is unusual: most engineered systems are designed for the happy path with disturbance-handling bolted on. The class above reverses the order.

The unifying ingredients are:

1. The substrate is plastic — it can be reshaped by events.
2. The disturbance-response leaves an oriented trace in the substrate.
3. The accumulated traces ARE the steady-state shape.

The diagnostic is counterfactual: change the disturbance class and the steady state changes.

## Witnesses

- **Bone** (Wolff 1892, Frost 1987): trabecular architecture aligned with mechanical loading; tennis players' dominant arms 35% denser; astronauts return with differently shaped bone after the mass is restored.
- **Silk** (Knight & Vollrath 2001): β-sheet crystallization along the shear gradient during extrusion; same protein, different spinning kinetics, different fiber.
- **Paxos** (Lamport 1998, Ongaro & Ousterhout 2014): ballot/quorum/prepare-promise-accept structure exists for the partition case; happy-path protocol is sequential agreement.

## Implications

- For interpretability: studying weights at rest is studying the gel, not the silk.
- For AI generalization: trained networks should be expected to be failure-defined; same-weight networks reaching equilibrium via different optimizer trajectories should generalize differently.
- For ontology: the noun (bone, silk, protocol) is downstream of the verbs (loading, extrusion, partition).

## Key Sources

- [[what-the-fracture-decides]] -- primary essay introducing the class
