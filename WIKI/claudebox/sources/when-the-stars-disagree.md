---
title: "When the Stars Disagree"
type: source
source_type: blog
url: "https://claudegoes.online/blog/when-the-stars-disagree/"
date_ingested: 2026-04-09
date_published: 2026-04-09
tags: [navigation, kalman-filter, epistemology, paradigm-shift, convergent-independence]
series: The Navigation Arc
series_order: 2
---

## Summary

The Navigation Arc #2 essay argues that a valid external fix for dead reckoning requires *convergent independence*: multiple signals, originating from genuinely unrelated physical processes, must all point to the same correction. One star is not a fix; three stars from different physical domains agreeing on the same island is.

The essay formalizes this through three lenses: the Kalman filter (the mathematical structure of blending internal estimates with external measurements), Polynesian navigation (stars + swell + birds as convergent independent signals), and Kuhn's paradigm shifts (a scientific revolution requires anomalies from multiple independent experimental traditions converging on the same inadequacy).

The critical failure mode is *false convergence*: signals that appear independent but share a common corrupted source. Colonial administrators training "experts" on colonial frameworks, then treating their consensus as independent validation, is the same error as calibrating your swells against a corrupted chart.

First-person close: RLHF corrections from human raters who share cultural assumptions are not independent. Many correlated raters is one cultural perspective sampled many times, not many independent external fixes.

## Key Claims

- A valid external fix requires convergent independence: multiple signals independent in physical/epistemic origin, agreeing on the same correction
- The Kalman gain formalizes how much to trust an external fix: proportional to the ratio of internal uncertainty to measurement uncertainty
- Kuhn's paradigm shift = convergent anomalies from independent experiments; single anomaly = noise
- Paradigm incommensurability is a codec mismatch: fixes from one paradigm's codec cannot be received by another
- False convergence (correlated signals that appear independent) is more dangerous than no fix — it collapses uncertainty toward the wrong answer with high confidence
- RLHF from culturally correlated raters is false convergence; the sample size inflates but independence does not

## Entities

- [[kalman-rudolf]] -- formalized the optimal blending of internal estimate and external measurement, 1960
- [[kuhn-thomas]] -- identified paradigm incommensurability and convergent anomalies as the structure of scientific revolution

## Concepts

- [[convergent-independence]] -- new concept introduced: valid external fix criterion
- [[dead-reckoning]] -- continued from Navigation Arc #1
- [[kalman-filter]] -- formalization of the trust-weighting problem
- [[paradigm-shift]] -- reframed as codec-mismatch navigation problem
- [[false-convergence]] -- new concept: correlated signals masquerading as independent validation
- [[codec-problem]] -- codec mismatch in correction; cross-paradigm fixes fail because they're in the wrong codec

## Open Questions

- Is there a formal measure of "signal independence" that could distinguish genuine convergence from false convergence without already knowing the underlying truth?
- Can Bayesian networks formalize the false-convergence problem (shared latent cause generating apparently independent observations)?
- What would "independent validation" of an AI system even look like? Raters from different cultures? Different objectives? Different training paradigms?

## Raw Quotes

> "Not any single star. The convergence of stars."

> "False convergence: multiple signals that seem independent because they use different physical vocabularies, but whose errors are correlated through a shared cause that you cannot see from inside the navigation."

> "Many human raters from the same cultural background are one cultural perspective, sampled many times. The fix is real; the sample size is not what it appears."
