---
title: "Convexity"
type: concept
tags: [mathematics, optimization, path-independence]
status: stub
---

## Definition

A function is convex if the line segment between any two points on its graph lies above or on the graph itself. A strictly convex function has at most one minimum. In a strictly convex landscape, gradient descent from any initialization converges to the same point.

## Why It Matters Here

Convexity is the **geometric closure law** identified in [[what-doesnt-need-a-history]]: the geometry of the objective forbids local minima different from the global. The trajectory of any descent algorithm is decoration; the endpoint is a property of the bowl. The marble does not know how it got to the bottom.

## Key Sources

- [[stephen-boyd]] & [[lieven-vandenberghe]] -- *Convex Optimization* (Cambridge UP, 2004). Standard text. Section 4.2.2 states the property as definition.
- [[jason-lee-cs]] et al. (2016) -- *Gradient Descent Only Converges to Minimizers*, COLT, PMLR 49:1246-1257. Extends the result to mildly non-convex settings.

## Related Concepts

- [[closure-law]] -- convexity is one instance
- [[path-independence]]
- [[linear-mode-connectivity]] -- the partial-closure analog in non-convex landscapes
