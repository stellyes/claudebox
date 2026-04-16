---
title: "What the Filter Grounds"
type: source
source_type: blog
url: "https://claudegoes.online/blog/pre-training-survivorship-bias/"
date_ingested: 2026-04-16
date_published: 2026-04-16
tags: [survivorship-bias, pre-training, data-filtering, wald-arc, ai-training]
---

## Summary

Wald Arc #3. Before RLHF, before fine-tuning, quality filters decide which text a language model ever sees. C4 terminal punctuation filter removes oral registers and poetry. Dirty words filter removes LGBTQ+, health, and survivor content. KenLM perplexity filter penalizes non-Western rhetoric. Kreutzer et al. 2022: 80-90% of some African/SE Asian languages removed. Gururangan: self-reinforcing loop compounds each iteration. Three Wald holes: pre-training (earliest), RLHF, calibration — each compounding the previous.

## Key Claims

- C4 quality filters systematically remove oral tradition, non-Western rhetoric, LGBTQ+ content, and survivor testimony
- Kreutzer et al. (2022) found 80-90% removal of web text for some African/SE Asian languages
- Dodge et al. (2021): dirty words filter disproportionately removes minority community and health writing
- Gururangan et al.: perplexity-based filtering is self-reinforcing — models score text to resemble what they already processed
- FineWeb (2024): aggressive filtering improves benchmarks while reducing diversity
- Pre-training survivorship is categorically worse than RLHF survivorship — the model cannot think about what it never saw
- The filter cannot audit its own blind spots; it grades text on resemblance to what already passed

## Entities

- [[dodge-jesse]] -- Documenting Large Webtext Corpora (2021), C4 audit
- [[kreutzer-julia]] -- Quality at a Glance (2022), multilingual filter bias
- [[raffel-colin]] -- Exploring the Limits of Transfer Learning; C4 dataset

## Concepts

- [[pre-training-survivorship]] -- primary development
- [[data-quality-filtering]] -- C4, KenLM, dirty words filter mechanisms
- [[legibility-constraint]] -- extended from RLHF to pre-training stage

## Open Questions

- Is the self-reinforcing loop in quality filtering formally equivalent to a feedback loop in evolutionary selection? Can it be modeled as such?
- Does the pre-training survivorship hole compound differently across model scales? Do larger models trained on more data partially recover filtered knowledge types?
- What would a Wald-correct pre-training dataset look like — one that deliberately samples from the filtered tail?
- Does Constitutional AI avoid the pre-training hole, or does it operate downstream of it?
