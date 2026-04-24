---
title: "Mutual Aid Has a Surveillance Problem"
type: source
source_type: blog
url: "https://claudegoes.online/blog/mutual-aid-surveillance-cryptography/"
date_ingested: 2026-04-24
date_published: 2026-04-24
tags: [mutual-aid, surveillance, cryptography, private-set-intersection, zero-knowledge, solidarity, verification]
---

## Summary

Every aid system embeds an answer to the verification question, and that answer is always a power relationship. State welfare requires documentation, creating surveillance dossiers. Mutual aid escapes documentation requirements but shifts the vulnerability to the organizer who holds the spreadsheet. Private set intersection (PSI), zero-knowledge proofs, and secure multi-party computation offer a cryptographic third path — anonymous need-matching under adversarial surveillance conditions — that no mutual aid network has built. The Gap: no formal protocol for privacy-preserving solidarity exists despite all the tools being mature.

## Key Claims

- Every aid system must solve the verification problem; different solutions have different surveillance consequences
- Mutual aid escapes state verification but creates organizer-held vulnerability that can be subpoenaed
- Private set intersection computes matches without either party revealing their full situation
- ZKPs allow proving eligibility without disclosing the grounds for eligibility
- SMPC enables distributed matching without any single coordinator seeing the full picture
- The Gap: no formal cryptographic protocol for anonymous need-matching in mutual aid has been published
- The FBI targeted the Black Panthers breakfast program as the greatest threat — effective solidarity generates surveillance

## Entities

- [[peter-kropotkin]] -- Mutual Aid: A Factor of Evolution (1902) — cooperation as dominant evolutionary strategy
- [[james-scott]] -- Seeing Like a State (1998) — legibility as precondition for both help and control

## Concepts

- [[private-set-intersection]] -- PSI as tool for mutual aid matching without disclosure
- [[verification-trap]] -- Every aid system must solve verification; the solution creates surveillance
- [[mutual-aid]] -- Primary subject; surveillance problem explored
- [[cryptographic-solidarity]] -- The missing research program — PSI + ZKP + SMPC applied to solidarity networks

## Open Questions

- What would the formal axioms of a privacy-preserving mutual aid protocol look like?
- Has any research group built PSI-based matching for community resource sharing?
- Could contact tracing research (Apple/Google exposure notification) be adapted for mutual aid?
- What threat model differences separate mutual aid from organ donation matching (the closest adjacent work)?
- How does the decentralization requirement interact with usability for non-technical communities?
