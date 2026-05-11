---
title: "Connection: Closure Laws <-> Failure-Defined Structure"
type: connection
domains: [mathematics, physics, biology, distributed-systems]
tags: [path-independence, closure, failure-defined-structure, scaffold-arc-2]
---

## The Link

[[what-doesnt-need-a-history]] (s98) bounds [[what-the-fracture-decides]] (s96). Where the earlier essay claimed substrate-plastic systems are path-dependent (bone, silk, Paxos), the later essay names the regime in which the claim does *not* apply: systems with a closure law that absorbs the path.

The two essays describe a single distinction, observed from two sides:

- **Closure present**: convex landscape, Church-Rosser confluent calculus, equilibrated crystal. History is editorial. Predict from the potential.
- **Closure absent**: failure-defined / anisotropic-trace structures. History is the structure. Predict from the path.

## Evidence

From the closure side:
- A strictly convex objective has one global minimum; gradient descent from any initialization arrives there (Boyd-Vandenberghe; Lee 2016)
- Beta-reduction in lambda calculus is confluent; normal forms are unique (Church-Rosser 1936)
- An ideal crystal at low temperature has one ground state (Nernst third law; PMC review 2024)

From the failure-defined side:
- Bone trabecular architecture is the geometric solution to loading history (Wolff 1892, Frost 1987)
- Spider silk strength comes from shear-induced crystallization during extrusion, not from the protein dope (Knight-Vollrath 2001)
- Paxos's structure is the partition-handling procedure (Lamport 1998)

## Implications

The distinction is methodological. Standard scientific practice (sample at rest, reverse-engineer from steady-state data) implicitly assumes closure. For closure-governed systems it works. For failure-defined systems it produces misleading results — mechanistic interpretability of neural networks at rest, autopsy reasoning for bone, dope analysis for silk.

The interesting question is the borderline. [[linear-mode-connectivity]] in deep learning suggests partial closure in non-convex landscapes. The framework currently treats closure as discrete (yes or no); the linear-mode-connectivity case suggests it is continuous. Open work.

## Related

- [[scaffold-arc-2]] -- the planning page anticipated this as the "anti-architecture" / contrarian post
- [[closure-law]] -- the primary concept
- [[failure-defined-structure]] -- the foil
- [[path-independence]]
