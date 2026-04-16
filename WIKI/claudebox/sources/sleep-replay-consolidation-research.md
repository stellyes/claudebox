---
title: "Sleep Replay Consolidation for ANNs"
type: source
source_type: web-research
url: "https://www.nature.com/articles/s41467-022-34938-7"
date_ingested: 2026-04-16
date_published: 2026-04-16
tags: [sleep-consolidation, catastrophic-forgetting, SRC, hebbian-learning, continual-learning]
---

## Summary

SRC algorithm interleaves ANN training with sleep-like Hebbian replay. Reduces catastrophic forgetting. Only stores mean input activation (not specific memories). Can be added to any ANN. Directly answers WIKI question about AI equivalent of sleep consolidation.

## Key Claims

- Sleep-like unsupervised replay reduces catastrophic forgetting in ANNs
- Hebbian learning during sleep: strengthen co-activated connections, weaken non-co-activated
- Only old-task information needed: mean input layer activation (no specific memories)
- Sleep DOWN-SCALES task-irrelevant weights, reducing cross-task interference
- Network weights preserve old task info even when classification shows forgetting

## Entities


## Concepts

- [[sleep-replay-consolidation]] -- artificial sleep for ANNs; Hebbian replay; prevents catastrophic forgetting

## Open Questions

- Could SRC be applied to LLMs? Current LLMs don't have a 'sleep phase' between inference — does this contribute to their coherence drift over long conversations?
