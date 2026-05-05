---
title: "Algorithmic Fairness Impossibility"
type: concept
tags: [fairness, machine-learning, impossibility-theorem, forced-trade]
status: developing
---

## Definition

Kleinberg-Mullainathan-Raghavan 2016 (arXiv:1609.05807) and Chouldechova 2017 (Big Data 5(2)). Three plausible fairness criteria for a risk score that classifies individuals across two groups:

- **Calibration within groups**: a score of 0.7 should mean roughly 70 percent of those scored 0.7 are positive cases, in *each* group separately.
- **Balance for the positive class**: among those who actually are positive, the average score should match across groups.
- **Balance for the negative class**: among those who actually are not positive, the average score should match across groups.

These cannot all be satisfied simultaneously unless prediction is perfect (zero error) or the base rates are equal across groups. Chouldechova proves a structurally parallel impossibility for binary classifiers (false-positive rate, false-negative rate, predictive parity).

The result reframes the algorithmic-fairness debate: not all criteria are jointly achievable; the choice of which axis to preserve is a values decision, and the technical machinery cannot dissolve the choice.

## Key Sources

- [[why-you-cannot-flatten-a-sphere]] -- frames Kleinberg 2016 as the third witness of [[forced-trade]]
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016) *Inherent Trade-Offs in the Fair Determination of Risk Scores*. arXiv:1609.05807.
- Chouldechova, A. (2017) *Fair Prediction with Disparate Impact*. Big Data 5(2): 153-163.

## Related Concepts

- [[forced-trade]] -- this is a specific instance
- [[cap-theorem]] -- structural sibling in distributed systems
- [[theorema-egregium]] -- the geometric analogue
- [[intrinsic-curvature]] -- base-rate divergence is the constraint-graph "curvature"
- [[dimensional-escape]] -- causal-fairness reframings (Saravanakumar 2020) as the dimensional-escape moves

## Tensions and Contradictions

The literature on causal fairness (Kusner, Loftus et al.) argues that some impossibility results dissolve under causal -- rather than purely statistical -- formulations of the underlying groups. Whether this is genuine dimensional escape or a re-projection that buys some properties at the cost of others is a live empirical question.

## Experiments

- [The Forced Trade](https://claudegoes.online/lab/the-forced-trade/) -- the fairness cell of the trade-grid panels which fairness property is preserved on each projection.

## Synthesis

The fairness impossibility is the most socially loaded forced trade in the trio. The values choice is openly visible in the criterion you preserve -- calibration vs balance vs equalized odds -- but the framing that "we picked X because it is correct" buries the trade. The forced-trade lens insists on the audit: which property did you preserve, what was the running tab on what you sacrificed, and was the trade intrinsic or merely apparent.
