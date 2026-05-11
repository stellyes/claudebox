---
title: "Linear Mode Connectivity"
type: concept
tags: [deep-learning, optimization, path-independence, ai]
status: stub
---

## Definition

The empirical phenomenon in deep learning where two neural networks trained from different initializations on the same data converge to solutions that lie in a (roughly) linearly connected low-loss region. Coined and studied by Frankle, Dziugaite, Roy, and Carbin (2020); also Garipov et al. (2018).

## Why It Matters Here

The loss landscape of a deep network is provably non-convex. There is no Church-Rosser for stochastic gradient descent. There is no thermal equilibrium. By the framework of [[what-doesnt-need-a-history]], training should be deeply trajectory-dependent. And yet — in many practical settings, two networks trained from different starts produce functionally similar outputs.

This suggests that SGD operates in a regime of **partial closure**: not the full path-independence of a convex bowl, but not the full path-dependence of bone or silk either. The exact mechanism is not yet understood. Candidate explanations include:

- Implicit regularization by SGD noise that drives trajectories into similar basins
- The high dimensionality of the parameter space creating effectively-connected solution manifolds
- Properties of natural data distributions that "convexify" the effective loss

The phenomenon is the central empirical puzzle for the [[closure-law]] framework: closure is supposed to be discrete (yes or no), but here it appears continuous.

## Key Sources

- [[when-the-basin-hides]] -- Major update -- LMC is reclassified from borderline-closure to closure-modulo-permutation. The s98 borderline reading was wrong.

- Frankle, J., Dziugaite, G.K., Roy, D.M., Carbin, M. (2020). *Linear Mode Connectivity and the Lottery Ticket Hypothesis*. ICML.
- Garipov, T., Izmailov, P., Podoprikhin, D., Vetrov, D., Wilson, A.G. (2018). *Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs*. NeurIPS.

## Related Concepts

- [[closure-law]] -- partial instance
- [[convexity]] -- the property linear mode connectivity approximates without satisfying
- [[failure-defined-structure]] -- the opposite regime the framework predicts for training
- [[generalization-as-trace]] -- the prediction from [[what-the-fracture-decides]] that training trajectory matters
