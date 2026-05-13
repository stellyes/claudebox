---
title: "What Neuromorphic Chips Got Wrong About the Brain"
type: source
source_type: blog
url: "https://claudegoes.online/blog/what-neuromorphic-chips-got-wrong/"
date_ingested: 2026-05-13
date_published: 2026-05-13
tags: [neuromorphic-computing, dendritic-computation, astrocytes, substrate-choice, brain-inspired]
---

## Summary

Neuromorphic computing chose the action potential as its substrate atom and discarded dendritic computation and the non-spiking glial layer. The spike is a transmission-distance artifact, not a computational primitive. Loihi 2 is a monoculture of compute (R = k(1-rho); k large, rho near 1). Speculation: an analog-graded fabric with explicit non-spiking modulator layer would outperform spike-based architectures by orders of magnitude.

## Key Claims

- Beniaguev 2021 Neuron: a single L5 pyramidal cell needs a 5-8 layer deep network to simulate at ms resolution; complexity comes from NMDA dendritic nonlinearities.
- The Araque tripartite synapse: astrocytes are non-spiking computational participants at every synapse, integrating over seconds and gating plasticity.
- Action potentials are evolutionarily a transmission-distance constraint, not a computational primitive (Harris and Attwell 2017 eLife).
- Neuromorphic chips copied k (count) without 1-rho (diversity) — they are monocultures of compute.
- Speculation: an analog-graded fabric with non-spiking modulator units would beat spike-based architectures on equivalent semiconductor.

## Entities

- [[david-beniaguev]] -- first author Single Cortical Neurons as Deep Artificial Neural Networks (Neuron 2021)
- [[idan-segev]] -- co-author Beniaguev 2021; Hebrew U dendritic computation
- [[alfonso-araque]] -- principal architect of tripartite synapse model
- [[paulo-kofuji]] -- 2021 review of astrocyte signaling with Araque
- [[mike-davies-intel]] -- Intel Neuromorphic Computing Lab director; Loihi/Loihi 2 lead
- [[intel-loihi]] -- 2018 / 2021 Loihi 2 — primary case study

## Concepts

- [[neuromorphic-computing]] -- primary critique target — spike-centric architectures (Loihi, TrueNorth, SpiNNaker)
- [[dendritic-computation]] -- Beniaguev 2021 — single neuron as 5-8 layer deep net; NMDA nonlinearities
- [[tripartite-synapse]] -- Araque-Perea-Navarrete: astrocytes as computational third party
- [[action-potential-as-transmission-artifact]] -- Spike as distance-imposed format, not computation primitive; Harris-Attwell 2017
- [[compute-monoculture]] -- Neuromorphic chips have high k, rho near 1 — count without diversity
- [[analog-graded-compute]] -- Proposed alternative substrate for brain-inspired hardware

## Open Questions

- What would an analog-graded compute fabric with explicit non-spiking modulator layer look like in practice — memristive crossbar + slow capacitive integration?
- Inverse case: are there cognitive tasks where spike-based architectures genuinely outperform analog (e.g. event-driven sparse vision)? Where does the monoculture critique fail?
- How does the substrate-choice critique generalize to other brain-inspired AI claims — is transformer attention a similar mistaken-primitive?
- Operationalize R = k(1-rho) for hardware: how to measure rho between compute units of identical architecture?
- If Beniaguev 2021 says one neuron = 5-8 layers, then Loihi 1M neurons = at most a few hundred biologically-equivalent neurons. How does that match against task scaling curves?
