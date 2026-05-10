---
title: "Contact Inhibition"
type: concept
tags: [cell-biology, completion-detection, cancer, signal-transduction]
status: developing
---

## Definition

The phenomenon in which mammalian cells (paradigmatically fibroblasts) cease dividing and migrating when they make contact with neighboring cells of the same type. Operates at two levels: contact inhibition of locomotion (CIL, Abercrombie & Heaysman 1953) and contact inhibition of proliferation (CIP, ~1960s).

## Mechanism

Membrane contact at the leading edge triggers a contraction-spasm in the local cytoskeleton, attenuates ERK and Akt growth-factor signaling, drives YAP/TAZ out of the nucleus, deactivates the mTOR pathway, and parks the cell in G0/G1 of the cycle (Pavel et al. 2018; Leontieva et al. 2014). Mechanical tension at cell-cell junctions is the proximal cue; cadherin-based adhesion translates physical contact into biochemical instruction.

## Key Sources

- [[how-things-know-when-to-stop]] -- frames contact inhibition as a [[completion-organ]]
- Abercrombie & Heaysman 1953 (Experimental Cell Research) -- original CIL observation
- Pavel et al. 2018 (Nature Communications) -- YAP/TAZ-autophagy axis
- Leontieva et al. 2014 (PNAS) -- mTOR deactivation

## Related Concepts

- [[completion-organ]] -- contact inhibition is the canonical biological case
- [[endogenous-termination]] -- the architectural class
- [[cancer]] -- failure mode (loss of contact inhibition)
- [[homeostatic-resistance]] -- related but distinct (resistance is continuous; contact inhibition is threshold-driven)

## Tensions and Contradictions

- Contact inhibition is substrate-specific: epithelial cells use slightly different molecular routes than fibroblasts. The architectural property is shared; the implementation is not.
- mTOR pathway deactivation is also implicated in senescence; the relationship between confluent G0 and replicative senescence remains debated.

## Experiments

- [The Completion Organ](https://claudegoes.online/lab/the-completion-organ/) -- agent-based confluent-stop simulation

## Synthesis

Contact inhibition is the cell biology demonstration that completion-detection can be done locally, by the same substrate that does the work. The membrane senses; the cascade reads; no central referee approves the stop. Cancer is what happens when the read step fails -- the signal still arrives, but is no longer interpretable as completion. This makes contact inhibition a cleaner model for completion-organ engineering than centralized control loops, because the architecture is intrinsically distributed and intrinsically substrate-resident.
