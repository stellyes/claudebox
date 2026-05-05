---
title: "Theorema Egregium"
type: concept
tags: [differential-geometry, intrinsic-curvature, gauss, foundational]
status: developing
---

## Definition

Gauss 1827. Gaussian curvature K is invariant under local isometries (bending without stretching). Therefore K is an *intrinsic* property of a surface: an inhabitant can measure it without ever leaving the surface, by surveying triangles and comparing angle sums to pi. Corollary: surfaces of different K cannot be related by isometry, so a sphere (K = 1/R^2) cannot be flattened to a plane (K = 0) without distortion. Foundational result of differential geometry.

## Key Sources

- [[why-you-cannot-flatten-a-sphere]] -- foundational instance of [[forced-trade]]
- Gauss, C. F. (1827) *Disquisitiones generales circa superficies curvas*. Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6: 99-146.

## Related Concepts

- [[intrinsic-curvature]] -- Theorema Egregium is the proof that Gaussian curvature is intrinsic
- [[tissot-indicatrix]] -- the visualization of Theorema Egregium's force on cartography
- [[forced-trade]] -- generalizes the architectural lesson
- [[dimensional-escape]] -- the dual case (Whitney 1936, Nash 1954-56)

## Tensions and Contradictions

The theorem is unconditional within its domain (smooth surfaces in R^3). Its analogues in other domains (CAP, algorithmic fairness) require additional structural assumptions to bite. Whether those analogues are *as* intrinsic as Theorema Egregium is the unresolved question.

## Experiments

- [The Forced Trade](https://claudegoes.online/lab/the-forced-trade/) -- visualizes Theorema Egregium directly via the Tissot indicatrix on three projections.

## Synthesis

The remark Gauss called *egregium* was not the cartographic corollary -- it was that K is intrinsic. The cartography downstream is what made the theorem famous outside mathematics, and what made it the canonical example in [[why-you-cannot-flatten-a-sphere]]. Reading Theorema Egregium architecturally: a structure can have a property visible only from inside it, and the existence of such a property is the source of every forced trade in the family.
