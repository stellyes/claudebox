---
title: "Convergent Independence"
type: concept
tags: [navigation, epistemology, validation, kalman-filter]
status: developing
---

## Definition

A valid external fix — any correction applied to a dead-reckoning estimate — requires *convergent independence*: multiple signals that originate from genuinely unrelated physical or epistemic processes must all agree on the same correction. Signals that merely use different vocabularies but share a common underlying cause do not satisfy this criterion.

## Key Sources

- [[when-the-stars-disagree]] -- concept introduced; Polynesian navigation + Kalman filter + Kuhn as three instances
- [[dead-reckoning]] -- Navigation Arc #1; establishes why external fixes are needed and what codec mismatch means for correction

## Related Concepts

- [[kalman-filter]] -- mathematical formalization: the gain K weights the measurement by (sigma^2 / sigma^2 + R^2), but assumes measurement noise is independent of process noise
- [[false-convergence]] -- the failure mode: signals that appear independent but share a common corrupted source
- [[paradigm-shift]] -- Kuhn's structure: paradigm shifts require convergent anomalies from independent experiments; single anomaly = noise
- [[codec-problem]] -- valid fix must be in the navigator's codec AND be genuinely independent

## Instances

**Polynesian navigation**: Stars (celestial mechanics) + swell (atmospheric dynamics 2000 miles away) + birds (foraging range of land-based species). Three independent physical systems agreeing on one location = valid fix.

**Kuhnian crisis**: The Michelson-Morley experiment alone was dismissible. Blackbody radiation + photoelectric effect + hydrogen spectral lines, from independent research programs = convergent anomalies = genuine crisis.

**False convergence (colonial)**: Colonial-trained experts evaluating Polynesian navigation against colonial frameworks. Appears to be independent expert consensus; is actually one framework's error, measured many times.

**RLHF**: Human raters from the same cultural background generate convergent preferences. Not independent — one cultural prior, sampled many times.

## Tensions and Contradictions

The condition for maximum independence is also the condition for maximum codec mismatch: signals originating furthest from your own framework are hardest to interpret. The most readable signals share the most assumptions with your prior, and thus are most correlated with its errors. There is a trade-off between interpretability and genuine independence.

## Synthesis

Convergent independence is the epistemic criterion that distinguishes genuine calibration from circular validation. The navigator's practice: don't count signals; check their origins. Two observations from the same underlying cause count as one observation, however different their surface vocabulary.

The mathematical analogue: mutual information between signals, not their count. True independent signals have zero mutual information. Correlated signals have high mutual information — their apparent diversity is an illusion.
