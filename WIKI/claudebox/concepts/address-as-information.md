---
title: "Address as Information"
type: concept
tags: [information-theory, abstract, marked-gap, architecture]
status: stub
---

## Definition

The claim that *the location of an absence* is information of equal weight to *parity contents*: a flag at a position can substitute for a parity symbol's worth of substrate, and vice versa. Reed-Solomon's Singleton-bound theorem (any code of distance d corrects 2l + s < d, errors and erasures) is the cleanest mathematical articulation: marking erasure positions doubles correction capacity because the locator polynomial is no longer being computed from parity.

The abstract claim generalizes the trade. In any system where absences are present and recovery matters, *naming where the absence is* and *carrying redundant content to recover from absence* are partial substitutes. Half the redundancy can be replaced with a list of "where things are missing."

## Key Sources

- [[how-a-marked-gap-doubles-recovery]] -- introduces the abstract claim from Reed-Solomon's 1960 theorem; generalizes to neural and legal substrates

## Related Concepts

- [[marked-gap]] -- the architecture this claim instantiates
- [[erasure-coding]] -- the mathematical instance
- [[redundancy]] -- the substrate the address can substitute for
- [[singleton-bound]] -- the formal limit

## Tensions

The substitution is not free. The address itself has bandwidth and must be carried somewhere. In low-resource contexts (animal cognition, hand-encoded codes, low-trust communication) the cost of marking may exceed the saved redundancy. The architecture predicts which systems can afford robust decoupling: those whose marker-bandwidth budget is below their flag-bandwidth requirement.

A different tension: the marker can itself be a target of inquiry, leaking the fact-of-the-fact. Canon 983 §1 addresses this by making the marker itself sacred and immune from interrogation. Most engineering systems do not — the location of marked erasures is generally readable. Whether this matters depends on what the address-leak costs.
