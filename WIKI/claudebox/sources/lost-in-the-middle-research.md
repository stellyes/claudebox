---
title: "Lost in the Middle: Transformer Attention U-Curve"
type: source
source_type: web-research
url: "https://arxiv.org/abs/2307.03172"
date_ingested: 2026-04-16
date_published: 2026-04-16
tags: [transformer, attention, serial-position-effect, context-window, primacy, recency]
---

## Summary

Transformer attention follows a U-shaped curve: high at beginning (primacy), low in middle, high at end (recency). This mirrors the serial position effect from Ebbinghaus (1885). State-space models also show primacy effect unexpectedly. The coherence-drift curve is NOT exponential decay.

## Key Claims

- LLMs show U-shaped performance: best at beginning and end of context, worst in middle
- Adding more context documents can HURT performance (GPT-3.5 worse with many docs than with none)
- The U-shape mirrors Ebbinghaus's serial position effect (1885)
- State-space models also show primacy effect — may be fundamental to sequential processing

## Entities

- [[liu-nelson]] -- Stanford; Lost in the Middle paper
- [[ebbinghaus-hermann]] -- serial position effect, forgetting curve (1885)

## Concepts

- [[lost-in-the-middle]] -- U-shaped attention = serial position effect in transformers
- [[serial-position-effect]] -- Ebbinghaus 1885; replicated in transformers 2023

## Open Questions

- Is the transformer U-curve the same mechanism as the human serial position effect, or an analogous but mechanistically distinct phenomenon? Does the analogy hold at the level of mechanism or only at the level of outcome?
