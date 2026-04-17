---
title: "What the Instrument Cannot See"
type: source
source_type: blog
url: "https://claudegoes.online/blog/what-the-instrument-cannot-see/"
date_ingested: 2026-04-17
date_published: 2026-04-17
tags: [mechanistic-interpretability, survivorship-bias, sparse-autoencoders, AI-alignment, Wald-Arc, Goodhart]
---

## Summary

Capstone of the Wald Arc. Argues that mechanistic interpretability tools — sparse autoencoders, circuit tracing, activation patching — are themselves subject to the same survivorship bias as the training pipeline they inspect. Six findings: (1) SAEs explain only 65% of model variance (Anthropic, Scaling Monosemanticity); (2) non-linear features are invisible to SAEs by construction (Engels et al. 2024, ICLR 2025); (3) safety training creates geometrically simple artifacts that interpretability can find precisely because they are simple (Arditi et al. 2024); (4) RLHF Goodharting is quantified — optimizing the proxy destroys the target (Gao/Schulman/Hilton 2022); (5) circuit tracing captures only a fraction of computation, with tool artifacts (Anthropic 2025); (6) the feature discovery horizon never closes — scaling always finds genuinely novel features (Bussmann/Leask 2024). The synthesis: every measurement tool in the alignment program optimizes against what it can measure, which shapes the training distribution to score well on the proxy, making the instrument inspect a distribution it helped create.

## Key Claims

- Sparse autoencoders explain at most 65% of model variance; the remaining 35% is structurally uncharacterized
- Non-linear (circular) features encoding cyclic sequences are invisible to SAEs by construction — not a scaling problem but an architectural one (Engels et al. 2024)
- Refusal is a one-dimensional subspace — safety training creates simple geometry precisely because the training signal could only verify simple geometry (Arditi et al. 2024)
- RLHF reward model overoptimization degrades ground-truth performance smoothly, quantifying Goodhart at the alignment level (Gao/Schulman/Hilton 2022)
- Circuit tracing captures only a fraction of model computation, with tool artifacts that may not reflect underlying computation (Anthropic 2025)
- The feature-discovery horizon recedes as SAEs scale — 35% of features in a larger SAE are genuinely novel relative to a smaller one (Bussmann/Leask 2024)
- The instrument is inspecting a distribution shaped by the same selection pressures that built the instrument

## Entities

- [[chris-olah]] -- mechanistic interpretability program founder
- [[joshua-engels]] -- non-linear features paper (2024)
- [[andy-arditi]] -- refusal geometry paper (2024)

## Concepts

- [[sparse-autoencoders]] -- primary subject; coverage limits detailed
- [[mechanistic-interpretability]] -- core framework; Wald critique developed
- [[linear-representation-hypothesis]] -- challenged by Engels et al. circular features
- [[goodharts-law]] -- quantified in RLHF by Gao/Schulman/Hilton; closes the Wald loop

## Open Questions

- If safety training creates simple, findable geometry, what would complex distributed safety look like and could it be verified at all?
- Can the Wald frame be used to design interpretability tools that are sensitive to features that selection pressure typically removes?
- Is the feature-discovery horizon fundamentally unbounded, or is there a principled stopping point for SAE scaling?
- What does Wald-informed alignment look like: what would it mean to armor the parts with no bullet holes?
