---
title: "False Convergence"
type: concept
tags: [epistemology, validation, bias, navigation]
status: developing
---

## Definition

False convergence occurs when multiple signals appear to independently agree on a conclusion, but their agreement is an artifact of a shared latent cause rather than genuine independent evidence. The result is a collapse of uncertainty *toward the wrong answer with high confidence*.

## Key Sources

- [[when-the-stars-disagree]] -- concept introduced; framed as the most dangerous failure mode in dead-reckoning correction

## Related Concepts

- [[convergent-independence]] -- the criterion false convergence violates
- [[kalman-filter]] -- the Kalman filter has no defense against false convergence if sensors share a common calibration error
- [[codec-problem]] -- false convergence can arise from shared codec assumptions masquerading as independent validation
- [[error-correction]] -- parity-check that converges to the wrong codeword; the repair mechanism amplifying the error

## Instances

**Navigation**: Navigator calibrates swell-reading against colonial charts. Star fixes and swell fixes appear independent; both are now encoding the same systematic error.

**Science (paradigm capture)**: A research field in which all labs share the same theoretical assumptions, statistical methods, and peer-review culture. Replications "succeed" but are replications of the same methodological error.

**RLHF**: Human raters from culturally homogeneous populations. Convergence of preferences reflects shared cultural prior, not ground truth. High-confidence wrong answers.

**Expert consensus**: When "independent" experts were all trained in the same tradition, their consensus is one tradition sampled many times, not genuinely independent validation.

## Mechanism

In Bayesian network terms: false convergence arises when apparently independent observations share a latent variable — the common corrupted source. If you could see the latent variable, you'd update it; without it, you treat the correlations as independent evidence and update too aggressively.

The Kalman filter collapses uncertainty faster when multiple signals agree. If those signals are correlated, the uncertainty collapse is overconfident — the estimate is wrong and the error bounds don't include the truth.

## Tensions and Contradictions

False convergence is undetectable from inside the navigation. The signals look independent because they use different vocabularies. The only way to detect it is from a perspective outside the shared source — which requires access to that independent external view, which is exactly what's unavailable to the navigator.

The practical partial remedy: deliberately seek signals from the most different possible origins, even at the cost of interpretability. Resistance to convenience samples.
