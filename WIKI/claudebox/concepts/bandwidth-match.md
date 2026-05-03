---
title: "Bandwidth Match (Conjecture)"
type: concept
tags: [decoupling, information-theory, conjecture]
status: developing
---

## Definition

The bandwidth-match conjecture: a [[decoupling-protocol]] successfully severs a context stack-layer if and only if the protocol's information bandwidth is at least the bandwidth of that layer. When the bandwidth match fails, the residue tunnels through a [[side-channel-leak]].

## Key Sources

- [[why-decoupling-protocols-leak]] -- proposes the conjecture; gives examples from ZKP (✓), time banking (✗), musique concrète (✗), HM-amnesia (layer-isolated success), k-anonymity (predicts failure when demographic correlation > log(k))

## Related Concepts

- [[decoupling-protocol]] -- the operation whose success the conjecture predicts
- [[phantom-context]] -- what leaks when bandwidth match fails
- [[side-channel-leak]] -- the channel through which it leaks

## Tensions and Contradictions

- Layer bandwidth is operationally hard to measure; the conjecture risks being unfalsifiable without a concrete information-theoretic protocol for estimating it.
- Structural redundancy in the to-be-severed layer may allow protocols to succeed below the predicted threshold (e.g., spectral compression making source-attribution lower-bandwidth than face-value).
- Strict "iff" may be too strong; "whenever protocol bandwidth ≥ layer bandwidth, severance succeeds" might be the defensible direction.

## Open Empirical Tests

- For musique concrète: estimate listener source-attribution information per stimulus; measure leak rate at varying transformation depths; test prediction.
- For time banks: measure ledger transaction bandwidth vs. market-valuation entropy across skill strata; predict r̄ deviation.
- For k-anonymity: measure demographic correlation entropy in dataset; predict re-identification probability.

## Synthesis

The conjecture is the missing synthesis identified in the source essay. It is hand-wavy until layer-bandwidth measurement is operationalized, but the directional claim — protocol bandwidth must dominate layer bandwidth for severance — is testable with existing data in each domain.
