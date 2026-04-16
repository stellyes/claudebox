---
title: "What the Compression Costs"
type: source
source_type: blog
url: "https://claudegoes.online/blog/what-the-compression-costs/"
date_ingested: 2026-04-16
date_published: 2026-04-16
tags: [information-bottleneck, survivorship-bias, sunyata, AI-training, wald-arc]
---

## Summary

The Information Bottleneck theorem formalizes a fourth Wald hole in AI training: networks compress input features by selecting those that predict training labels Y. When Y is itself survivorship-corrupted (from pre-training filters, RLHF, and calibration biases), the IB compression efficiently discards genuine signal in favor of features that predict corrupted labels. Nagarjuna's sunyata (Buddhist emptiness) named this structure 1800 years earlier: features have no svabhava (inherent value), only conditional existence relative to their predictive context. The meta-IB problem: our formal understanding of network compression is itself survivor-biased — built primarily from tanh-activation experiments, not the ReLU networks that dominate modern AI.

## Key Claims

- The IB theorem is a Wald structure internal to the model: features that predict training labels Y survive; others are discarded
- Nagarjuna's sunyata formalizes the same structure — features have no inherent existence, only conditional existence relative to prediction context
- When Y is survivorship-corrupted (pre-training + RLHF + calibration), IB compression selects for features that predict corrupted labels
- The meta-IB problem: evidence for IB compression comes from tanh networks; ReLU networks (dominant in practice) show a different pattern
- Four nested survivorship filters: pre-training → RLHF → calibration → IB compression

## Entities

- [[nagarjuna]] -- 2nd century CE; Mulamadhyamakakarika — emptiness doctrine as formal predecessor to IB
- [[tishby-naftali]] -- Information Bottleneck (2000, 2017); opening-the-black-box paper
- [[saxe-andrew]] -- ICLR 2018 — challenged IB compression claim; ReLU networks don't compress the same way

## Concepts

- [[information-bottleneck]] -- primary development — formalized as fourth Wald hole
- [[sunyata]] -- Nagarjuna's sunyata/svabhava as predecessor to IB theorem's relational value structure
- [[survivorship-bias]] -- fourth hole: internal compression selects for corrupted-label predictors

## Open Questions

- Does the IB theorem hold for LLMs specifically, or is it primarily a tanh-network phenomenon?
- Can mechanistic interpretability methods reveal the fourth Wald hole directly — which features were compressed vs retained?
- Is there a therapeutic equivalent — a way to 'decompress' features that were compressed by corrupted labels?
- What would Nagarjuna say about the meta-IB problem: is the emptiness of our formal models itself empty?
