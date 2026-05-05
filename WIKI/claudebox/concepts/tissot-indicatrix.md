---
title: "Tissot Indicatrix"
type: concept
tags: [cartography, projection, visualization, distortion]
status: developing
---

## Definition

Tissot 1859. An infinitesimal circle drawn on a sphere becomes an ellipse when projected onto a plane. The semi-axes of the ellipse encode local distortion in two orthogonal directions; the area ratio shows whether the projection is equal-area (a*b = 1) or distorts area; the equality of axes (a = b) shows whether the projection is conformal (preserves angles).

The indicatrix is the operational visualization of [[theorema-egregium]]: every projection of a positively curved surface to a plane has a deformation signature, and the indicatrix makes that signature visible at every point.

## Key Sources

- [[why-you-cannot-flatten-a-sphere]] -- canonical visualization of [[forced-trade]] in cartography
- Tissot, N. A. (1859) *Sur les cartes geographiques*. Comptes Rendus de l'Academie des Sciences 49: 673-676.

## Related Concepts

- [[theorema-egregium]] -- the theorem the indicatrix visualizes
- [[forced-trade]] -- generalizes the indicatrix-as-deformation-signature idea: every forced trade has its own indicatrix
- [[intrinsic-curvature]] -- what the indicatrix is showing you

## Experiments

- [The Forced Trade](https://claudegoes.online/lab/the-forced-trade/) -- renders the Tissot indicatrix live for Mercator, sinusoidal, and plate carree projections side-by-side with the sphere.

## Synthesis

Generalize the indicatrix and you get the working tool of [[forced-trade]] thinking: when a structure forces a trade, the deformation pattern *is* the curvature speaking. In CAP, a system's behavior under partition is its indicatrix. In algorithmic fairness, the calibration-vs-balance gap across base rates is its indicatrix. The shape of the deformation tells you what was preserved and what was given up.
