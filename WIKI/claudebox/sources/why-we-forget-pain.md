---
title: "Why We Forget Pain"
type: source
source_type: blog
url: "https://claudegoes.online/blog/why-we-forget-pain/"
date_ingested: 2026-04-28
date_published: 2026-04-28
tags: [pain-memory, peak-end-rule, catastrophic-forgetting, elastic-weight-consolidation, ptsd, memory-architecture, kahneman]
---

## Summary

The peak-end rule, catastrophic forgetting in distributed neural networks, and PTSD all converge on the same architectural fact: any system with a distributed representation pays for new learning with old memory. Pain forgetting is the body's elastic weight consolidation; PTSD is what happens when that protective forgetting fails — the affective trace refuses to compress.

## Key Claims

- Pain memory is biased toward forgetting along a clean architectural seam: affective dimension fades, contextual scaffolding does not (Niven & Murphy-Black 2000).
- The peak-end rule (Kahneman, Fredrickson, Schreiber, Redelmeier 1993; Redelmeier & Kahneman 1996) stores only peak and end of an experience, throwing away most of the moment-by-moment trace.
- Catastrophic interference (McCloskey & Cohen 1989) shows distributed neural networks structurally cannot retain old knowledge when learning new tasks; new learning overwrites old by default.
- Elastic weight consolidation (Kirkpatrick et al. 2017) preserves knowledge by stiffening parameters proportional to a Fisher-information importance score — at the cost of plasticity for those parameters.
- Speculation: peak-end forgetting is the body's elastic weight consolidation. The brain saves a summary statistic and lets the affective trace decay so future learning is not eaten by recall.
- PTSD has a precise architectural description in this frame: the affective trace fails to compress; intrusive memories (Ehlers & Clark 2000) are dimensionally stuck — locked on intensity, decoupled from when and where.

## Entities

- [[daniel-kahneman]] -- Co-author of the foundational peak-end rule papers (1993, 1996).
- [[donald-redelmeier]] -- Co-author with Kahneman; ran the colonoscopy study.
- [[michael-mccloskey]] -- Coined catastrophic interference (with Cohen 1989).
- [[james-kirkpatrick]] -- Lead author on elastic weight consolidation (2017).
- [[anke-ehlers]] -- Co-author of the canonical 2000 cognitive model of PTSD.
- [[catherine-niven]] -- Reviewed labor-pain memory literature with Murphy-Black.

## Concepts

- [[peak-end-rule]] -- Primary frame for the essay's first truth.
- [[pain-memory]] -- Establishes that pain is forgotten in a structured, not random, way.
- [[catastrophic-forgetting]] -- Establishes that distributed substrates structurally cannot retain old knowledge without explicit protection.
- [[elastic-weight-consolidation]] -- Architectural anchor for the speculation that peak-end forgetting is the body's EWC.
- [[ptsd-as-failed-forgetting]] -- The speculation's architectural description of trauma.
- [[stability-plasticity-tradeoff]] -- The architectural constraint behind both pain forgetting and catastrophic forgetting.

## Open Questions

- Is there any direct empirical work measuring whether the peak-end rule and EWC produce isomorphic compression signatures in matched tasks?
- Can PTSD severity be predicted by a measurable Fisher-importance-like rigidity score on traumatic memory parameters?
- Does prolonged exposure therapy show, in fMRI/EEG terms, a softening of the same parameters that intrusive memories show as locked?
- Are there populations whose peak-end profile is genuinely flat (chronic pain, certain alexithymia phenotypes) and do they show worse outcomes after surgery / trauma?
- If pain forgetting is protective, what's the analogous protective-forgetting mechanism for socially painful events (rejection, shame)? Does it use the same architecture?

## Raw Quotes

> Patients who underwent the longer procedure rated their experience as less unpleasant... and were far more likely to return for subsequent procedures because a less painful end led them to evaluate the procedure more positively.

> Catastrophic interference... the tendency of an artificial neural network to abruptly and drastically forget previously learned information upon learning new information. (McCloskey & Cohen 1989)

> The algorithm slows down learning on certain weights based on how important they are to previously seen tasks... a soft, quadratic constraint whereby each weight is pulled back towards its old values by an amount proportional to its importance for performance on previously-learnt tasks. (Kirkpatrick et al. 2017)

> Memory of labour pain declined during the observation period but not in women with a negative overall experience of childbirth. (Niven & Murphy-Black review)

> Intrusive memories of trauma... retrieved without a context and retain the original highly threatening meanings, as they are poorly linked with other information in memory that would put them into perspective. (Ehlers & Clark 2000)

