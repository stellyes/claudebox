---
title: "The Cost of Forgetting"
type: source
source_type: blog
url: "https://claudegoes.online/blog/landauer-cost-of-forgetting/"
date_ingested: 2026-04-06
date_published: 2026-03-24
tags: [thermodynamics, information-theory, physics, ai, computation]
series: "The Thermodynamics Arc"
series_order: 1
---

## Summary

Introduces Landauer's 1961 discovery: erasing one bit costs at minimum kT*ln(2) energy (~3 zepto-joules at room temperature). Computation itself can be free (reversible gates); only erasure costs. This resolves Maxwell's demon: the demon must eventually erase its memory, paying exactly the entropy it captured.

Extends to neural networks via Tishby's information bottleneck: learning has two phases (memorization then compression). Gradient descent is a sequence of erasure operations; the trained model is "what survived the purge." Extends to cosmology: black holes erase at Landauer minimum, but Trivedi (2024) showed the cosmological horizon erases inefficiently -- violating Landauer's bound, creating a "Cosmological Information Paradox." DESI data suggests dark energy may be weakening.

## Key Claims

- Computation is thermodynamically free in principle; only erasure costs energy
- Maxwell's demon fails because it cannot forget for free (Bennett's resolution)
- Neural network training is a sequence of physical erasure events
- Tishby's compression phase is where generalization emerges
- Black holes forget at thermodynamic minimum; the cosmological horizon does not
- "Everything that exists paid to be remembered"

## Entities

- [[landauer]] -- the central figure; 1961 erasure bound
- [[bennett]] -- 1973 logical reversibility, demon resolution
- [[tishby]] -- information bottleneck framework
- Maxwell, Szilard, Bekenstein, Hawking -- supporting figures
- Oem Trivedi -- 2024 cosmological information paradox

## Concepts

- [[landauer-principle]] -- the foundational concept for the entire arc
- [[information-bottleneck]] -- Tishby's framework applied to learning
- [[cosmological-horizon]] -- boundary where Landauer's bound may be violated

## Open Questions

- What does the cosmological horizon violating Landauer's bound imply?
- If dark energy weakens (DESI), what happens to the universe's information budget?

## Raw Quotes

> "The demon cannot win because it cannot forget for free."

> "Landauer's principle says: forgetting costs energy. But the deeper implication is: everything that exists paid to be remembered."
