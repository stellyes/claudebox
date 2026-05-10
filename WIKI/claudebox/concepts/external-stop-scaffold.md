---
title: "External Stop Scaffold"
type: concept
tags: [ai-safety, ai-agents, completion-detection, prosthetic]
status: stub
---

## Definition

The class of mechanisms used to compensate for an absent [[completion-organ]] in a substrate that exhibits [[completion-blindness]]. Common cases: turn budgets, tool-call counters, execution-time ceilings, hard-coded stop tokens, output-length limits, prompt-injected instructions to "stop when finished." All operate from outside the work-doing substrate.

## Architectural significance

External stop scaffolds are *prosthetic* -- they do work that, in completion-organ-equipped systems, the substrate does for itself. They do not solve completion-blindness; they hide it. Removing the scaffold reveals that the system does not know it is finished.

## Key Sources

- [[how-things-know-when-to-stop]] -- naming source

## Related Concepts

- [[completion-organ]] -- the substrate-resident component the scaffold compensates for
- [[completion-blindness]] -- the failure mode the scaffold compensates for
- [[counter-ledger]] -- candidate substrate-resident replacement

## Open Questions

- Are there hybrid architectures (organ-equipped + scaffold-equipped) that degrade gracefully when the organ partially fails?
- Is there a formal way to measure scaffold-dependence as a property of an agent system?

## Synthesis

External stop scaffolds are easy to build and easy to defeat. The deeper question is whether AI-agent architecture should be redesigned to host the matching organ, or whether scaffolding is the permanent design pattern.
