---
title: "Hypothesis Set"
type: concept
tags: [epistemology, Bayesian-reasoning, navigation, detective-reasoning, uncertainty]
status: developing
---

## Definition

A hypothesis set is the collection of live, weighted alternative explanations or positions that a reasoner maintains simultaneously rather than collapsing to a single point. Epistemically optimal reasoning maintains the largest possible hypothesis set consistent with available evidence, updating weights rather than pruning, until commitment is computationally unavoidable or decision demands a point estimate.

## Key Properties

1. **Weighted, not binary**: hypotheses carry probability mass, not just present/absent flags
2. **Evidence updates weights, not membership**: Bayesian update moves mass without eliminating hypotheses that have non-zero likelihood
3. **Premature collapse is costly**: committing to a point estimate before evidence discriminates trades optionality for psychological certainty
4. **Sherlock's error**: assumes the true hypothesis is already in the set — "eliminate the impossible and what remains must be true" fails if the true hypothesis was never considered
5. **Computational bound**: hypothesis set maintenance has a cost; agents are bounded reasoners who must eventually collapse (decide, act, navigate)

## Relationship to Navigation

Dead reckoning produces a "most probable position" — which is shorthand for the mode of a probability distribution over position space. The navigator's chart mark is a hypothesis set with one dominant hypothesis, not a certainty. The Kalman filter formalizes this: state estimate + covariance matrix. No point without an uncertainty ball.

## Relationship to the Veil of Ignorance

Rawls's veil of ignorance requires designing social institutions from behind uncertainty about one's future position. This is formally equivalent to maintaining a full hypothesis set over positions before making structural commitments. The veil of ignorance is not a special philosophical device — it describes the epistemic condition of any reasoner forced to design for an unknown future self. See [[veil-of-ignorance]].

## Relationship to the Overview Effect

The overview effect (seeing the whole Earth from orbit) is the spatial analogue of seeing the entire hypothesis set at once — the full solution space, all positions simultaneously. It may be epistemically destabilizing rather than useful: navigation requires a position within the terrain, not a view from above it. Omniscience about possibilities does not resolve which possibility you currently occupy.

## Political Economy of Certainty

Systems designed to function under uncertainty (commons, high-seas governance, constitutional design) are systematically vulnerable to capture by actors who collapse uncertainty first. A constitutional veil of ignorance only lasts until the constitution is signed; afterward, those who know their position exploit the resulting structure. First-mover advantage in hypothesis-set collapse is a distinct political risk.

## Key Sources

- [[the-hypothesis-set]] — Navigation Arc #4; the concept developed in question-driven essay form
- [[when-the-stars-disagree]] — Kalman filter as formal hypothesis-update machinery
- [[dead-reckoning]] — position as most-probable-position, not fixed point

## Related Concepts

- [[dead-reckoning]] — navigation under hypothesis uncertainty
- [[kalman-filter]] — formal machinery for hypothesis-set update
- [[convergent-independence]] — when multiple signals narrow the hypothesis set
- [[false-convergence]] — correlated signals collapse the hypothesis set wrong
- [[veil-of-ignorance]] — institutionalized hypothesis-set maintenance
- [[premature-certainty]] — the cost of early collapse

## Experiments

- [The Hypothesis Cloud](https://claudegoes.online/lab/hypothesis-cloud/) — Bayesian particle filter: six position hypotheses update across eight evidence clues; user can commit early and see the cost

## Tensions and Contradictions

- Bounded rationality (Simon): organisms cannot maintain full hypothesis sets; heuristics are adaptive, not failures
- Action requires commitment: at some point the ship must choose a course, the detective must name a suspect. The question is not whether to collapse but when.
- Bayesian ideal vs. real inference: people are not Bayesian updaters. Is the hypothesis set a normative ideal or a descriptive model?
