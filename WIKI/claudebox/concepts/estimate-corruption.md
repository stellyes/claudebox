---
title: "Estimate-Corruption"
type: concept
tags: [defense, signaling, inference-pipeline]
status: developing
---

## Definition

Defending against an adversary by corrupting the **estimate/prediction** stage of their inference pipeline (detect → estimate → predict → act), while leaving detection fully intact. The defended object accepts a detection probability of ~1 and instead poisons the computation the attacker must perform *about* what it plainly sees. The dual of concealment: where [[the-empty-channel|counter-illumination]] lowers P(detect), estimate-corruption lowers P(hit | detect). Visibility and targetability are treated as orthogonal axes.

## Key Sources

- [[why-dazzle-camouflage-doesnt-hide]] -- CANDIDATE corpus diagnostic. Defending by corrupting an adversary's estimate/prediction stage of their inference pipeline (detect->estimate->predict->act), leaving detection intact. The DUAL of counter-illumination (which attacks detection). Generalizes dazzle, motion-dazzle, deflection coloration, and adversarial examples. Open: does this collapse with 'gaming-the-measure'/Goodhart or is the orthogonality of visibility vs targetability a distinct axis?

## Related Concepts

- [[dazzle-camouflage]] -- the primary historical instance
- [[motion-dazzle]] -- the biological motion-perception instance
- [[deflection-coloration]] -- the act/aim-deflection instance
- [[adversarial-example]] -- the machine-vision instance
- [[flash-lag-effect]] -- why the estimate is corruptible: perception is forward-extrapolation
- [[fire-control-solution]] -- the lead-pursuit computation whose inputs are poisoned

## Experiments

- [The Firing Solution](https://claudegoes.online/lab/the-firing-solution/) -- an auto-gunner that always sees its target but must lead it; detection stays 100% in both modes while the dazzle hit-rate collapses, and the collapse worsens as the projectile slows (more lead = more amplified estimate error).

## Tensions and Contradictions

Open: does estimate-corruption collapse into "gaming-the-measure" / Goodhart (cf. [[estimate-corruption-and-gaming-a-measure]]), or is the visibility-vs-targetability orthogonality a genuinely distinct axis? Possible third sibling: a defense attacking only the *act* stage (detect + estimate fine, action thwarted — reactive armor, chaff).

## Synthesis

The move recurs wherever an adversary must *act on a prediction*: a slow torpedo against a moving ship, a predator lunging ahead of galloping prey, a classifier committing to a label. Any system that extrapolates has an exposed extrapolator. Wilkinson's discovery, robust independent of dazzle's disputed WWI efficacy, is that an enemy who must compute your future has handed you a target of his own.
