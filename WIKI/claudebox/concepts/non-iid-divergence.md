---
title: "Non-IID Divergence"
type: concept
tags: [federated-learning, machine-learning]
status: developing
---

## Definition

The phenomenon in federated learning where heterogeneous local data distributions cause client model updates to pull the global average in incompatible directions. Vanilla FedAvg (McMahan 2017) suffers severe convergence problems when client data is non-IID. SCAFFOLD (Karimireddy 2020) addresses this with control variates. Cited in s83 as evidence that the 'global model' cannot be cleanly separated from local priors — the parameter vector IS the time-averaged ghost of locally biased trajectories.

## Key Sources

- [[why-you-cannot-subtract-a-prior]] -- Inseparability witness in the ML domain.

## Related Concepts

- [[federated-learning]] -- the field where non-IID is the central problem
- [[client-drift]] -- the operational symptom of non-IID divergence
- [[prior-perceiver-inseparability]] -- second witness

## Tensions and Contradictions

[To be developed as more sources accumulate]

## Synthesis

[To be developed]
