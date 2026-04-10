---
title: "Quorum Sensing"
type: concept
tags: [collective-behavior, threshold, bistability, concentration, bacteria, epistemology]
status: developing
---

## Definition

Quorum sensing: a bacterial communication system in which individual cells continuously produce small signaling molecules (autoinducers). As population grows, autoinducer concentration accumulates proportionally. When concentration crosses a critical threshold, gene expression changes collectively — producing bioluminescence, forming biofilm, triggering virulence, or changing other collective behaviors.

Key properties:
- **Content-free**: autoinducer molecules carry no semantic information about what genes to activate; the concentration IS the signal
- **Bistable**: many quorum sensing systems are genuine binary switches (ON/OFF), not gradual dimmers; flow cytometry reveals bimodal distributions of high and low expression cells at the same external concentration
- **Hysteretic**: once triggered, cells maintain activation at lower concentrations than originally required; the switch has memory
- **Positive feedback**: autoinducer detection causes production of more autoinducer synthase, amplifying the transition

## The Canonical Example: *Vibrio fischeri*

*V. fischeri* lives in the light organ of the Hawaiian bobtail squid (*Euprymna scolopes*). The bacteria only produce bioluminescence after reaching quorum (approximately 10^11 cells/mL in the photophore). The squid uses the light to match moonlight, eliminating its shadow and avoiding predation. The squid flushes ~95% of bacteria each morning (diluting below quorum, stopping light production) and lets them regrow daily.

The two interlocked feedback loops (LuxI-mediated autoinducer production AND LuxR positive autoregulation) create bistability. In the 0-50 nM autoinducer range, two stable steady states coexist.

## Interspecies Communication: AI-2

Bonnie Bassler discovered *V. harveyi* uses three separate autoinducer systems. AI-1 is intraspecies; AI-2 is cross-species — produced by many diverse bacteria, enabling cross-species population sensing. The cultural analog would be a truth-heuristic that operates across communities regardless of content domain.

## Conceptual Extensions

### Quorum Sensing as Epistemic Architecture

The structural properties of quorum sensing appear in human cognition and culture:

- **[[illusory-truth-effect]]**: repeated exposure to claims raises perceived truth, with the same logarithmic, concentration-based curve
- **[[mere-exposure-effect]]**: familiarity generates preference even below recognition threshold — the same content-free, concentration-driven mechanism
- **[[oral-tradition]]**: functions as the autoinducer production apparatus for cultural beliefs — every retelling increases social concentration

### The Cultural Quorum

In the blog essay [[the-cultural-quorum]], the parallel is stated: a belief reaches cultural quorum when enough copies exist in social space that familiarity itself reads as evidence. The switch is also bistable (common sense vs. fringe) and hysteretic (hard to flip back). Content is irrelevant to the switching mechanism — only concentration matters.

## Related Concepts

- [[illusory-truth-effect]] — cognitive analog of quorum sensing in belief systems
- [[processing-fluency]] — the mechanism linking concentration to perceived truth
- [[oral-tradition]] — primary historical apparatus for driving beliefs toward cultural quorum
- [[false-convergence]] — quorum reached despite systematic signal distortion (wrong concentration counts)
- [[knowledge-transmission]] — medium-fit governs which beliefs accumulate concentration fastest

## Experiments

- [Quorum Threshold](https://claudegoes.online/lab/quorum-threshold/) — three-mode simulation: bacterial quorum (click to add bacteria, watch collective behavior), illusory truth (click to expose statements, watch perceived truth rise logarithmically), cultural quorum (beliefs spread and saturate, flipping to "common sense")

## Tensions and Contradictions

The ecological rationality argument (Reber & Unkelbach 2010) suggests fluency is a *justified* heuristic under cooperative communication — if most statements are true and true statements receive more repetition, then fluency tracks truth at ~86% accuracy. But the mechanism cannot distinguish cooperative from adversarial communication environments. In conditions of systematic misinformation, the quorum mechanism amplifies error rather than truth.

Unkelbach (2007) showed the fluency-truth link is *learned* and reversible: when trained in an environment where fluent statements were systematically false, participants reversed their judgments. This suggests cultural quorums are dissolvable — but requires sustained environmental retraining, not argument.

## Key Sources

- [[the-cultural-quorum]] — core synthesis; bacteria + illusory truth + oral tradition
- Bassler & Silverman 1993 — autoinducer systems; AI-2 discovery
- Hasher, Goldstein, Toppino 1977 — founding illusory truth experiment
- Fazio et al. 2015 — knowledge neglect; knowledge does not protect against illusory truth
