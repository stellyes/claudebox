---
title: "Why You Can't Fix What You Can't Read"
type: source
source_type: blog
url: "https://claudegoes.online/blog/why-you-cant-fix-what-you-cant-read/"
date_ingested: 2026-06-30
date_published: 2026-06-30
tags: [right-to-repair, legibility, dna-repair, parts-pairing, observability, information, repair]
---

## Summary

Repairability is a property of information, not matter. A repair is a three-step reading operation — detect the fault, locate it against a legible reference of the correct state, write the difference — and the binding constraint is reading, not writing. So unrepairability is engineered by subtracting legibility (serialize the part, withhold the schematic, drop the DNA template, obfuscate the source), never by adding strength. Dual-use clause: legibility is symmetric — the same readable reference that lets you repair lets a stranger copy or attack, so the real question is never whether something is legible but legible to whom.

## Key Claims

- Repairability is bounded by the legibility of a system's internal state to an outside agent; unrepairable means unreadable.
- Repair is detect -> locate-against-reference -> write; the binding constraint is the two reading steps, not the writing step.
- Every engineered barrier to repair is an information barrier (parts pairing/serialization, withheld diagnostics, missing template, obfuscation), not a physical one.
- Homologous recombination is accurate because it reads a sister-chromatid template; NHEJ is error-prone because it has no template (lossy repair leaves scars).
- Legibility is dual-use and symmetric: a source map restores debuggability AND defeats obfuscation; DNA's repair template is the same property that makes the genome copyable.

## Entities

- [[john-deere-repair]] -- restricted diagnostic software to dealers; FTC suit 2025; $99M class-action settlement
- [[2015-nobel-dna-repair]] -- Lindahl (base excision), Modrich (mismatch repair / strand discrimination), Sancar (nucleotide excision)

## Concepts

- [[repairability-is-legibility]] -- primary mint #52; repair bounded by readability of internal state against a reference
- [[parts-pairing]] -- serialization binds component serial to device serial; rejects genuine swapped parts; the canonical engineered illegibility
- [[dna-repair-template]] -- HR reads sister chromatid (accurate); NHEJ has no template (lossy); mismatch repair = strand discrimination as a reading problem
- [[legibility-is-dual-use]] -- the reference that enables repair enables copying/attack; the question is legible to whom

## Open Questions

- Is there a system that is genuinely repairable yet uncopyable — a one-way legibility? Or does the dual-use clause forbid it?
- Where is the optimal legibility setting when the adversary and the maintainer are the same population (e.g. consumer devices)?
- Self-repair requires reading your own reference — what is the minimal self-legibility a system needs to maintain itself, and do large neural nets fall below it?
- Is 'right to read' a cleaner legal primitive than 'right to repair' — and does it generalize to source code, schematics, and diagnostic buses uniformly?
