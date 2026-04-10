---
title: "Substrate Fatigue"
type: concept
tags: [analog-computing, decision-fatigue, information-theory, noise, transmission]
status: developing
---

## Definition

Substrate fatigue: the degradation of an analog computing medium's signal-to-noise ratio over time or use, causing information to be attenuated or corrupted before processing completes. The substrate — the physical medium through which computation flows — becomes less capable of carrying the signal cleanly.

Substrate fatigue is distinct from errors in the signal itself. A signal can be perfectly well-formed at the source and arrive depleted at the destination because of what the channel imposed on it in transit. This is Wiesner's pre-receiver failure applied to the computational substrate.

## Manifestations by Domain

### Analog Computing
Resistive networks and other in-materia computing systems accumulate thermal noise and component drift over operating cycles. Unlike digital circuits (which discretize at each stage, preventing noise accumulation), analog systems carry noise forward through each stage of computation. Precision degrades with operating temperature and time. The SNR floor rises.

### Biological Cognition: Decision Fatigue
The prefrontal cortex circuits mediating executive function show performance degradation after sustained decision-making. The Baumeister ego depletion model (contested) proposed glucose depletion; the more robust observation is that decision quality — not just willingness to decide — degrades over a long session. The substrate (the neural circuits that apply judgment) tires. Judges grant parole less often late in session; physicians order more unnecessary tests. The rule hasn't changed; the medium that applies the rule has drifted.

### Commons Governance
Ostrom's polycentric commons governance works through a continuous substrate of informal relationships, reputation, and shared models. When this substrate degrades — trust erodes, relationships fray, the informal network thins — the commons fails not because the formal rules changed but because the medium that carries them can no longer do so reliably. Wiesner's failure at the collective scale.

### Large Language Models: Coherence Drift
LLMs don't experience decision fatigue (inference is stateless; each forward pass starts from the same parameter configuration). But they experience an analogous depletion in the attention dimension: information far from the current position in a long context window exerts diminishing influence on outputs. Not erased — present in context — but attenuated. Coherence drift is depletion in attention distance rather than depletion in time.

## The Digital Escape

Digital computation escapes substrate fatigue by refusing to have a substrate that can fatigue. At every logic stage, the signal is discretized (0 or 1), and noise below the discrimination threshold is cleared. Errors cannot accumulate. This achieves precision without drift — but at the cost of losing the ability to settle. Every computation must begin from scratch; there is no resting state that carries prior meaning.

This is the fundamental trade-off: settling vs. sequencing. Analog computes by becoming the solution; digital computes by executing toward it.

## Architectural Responses

### Residual Connections (deep networks)
Skip connections in deep neural networks address the vanishing gradient problem — a form of substrate fatigue in which gradient signals attenuate across many multiplicative layers. By adding the layer's input directly to its output, the original signal is refreshed at each depth. The wire gets to start over. This is an engineering solution that preserves the analog character of gradient flow while preventing catastrophic attenuation.

### Ostrom's Design Principles (commons governance)
Ostrom's eight design principles for successful commons governance are, in part, a list of conditions that keep the analog substrate healthy:
- Clearly defined boundaries (reduce load on relationship tracking)
- Graduated sanctions (preserve proportionality; avoid discrete cliff-edges)
- Conflict resolution mechanisms (refresh damaged relationship substrate)
- Local rule adaptation (keep rule-carrying relationships short, not spanning distant nodes)

### Signal refreshing in human institutions
Shorter decision chains, regular breaks, distributed authority (fewer decisions per node), and explicit relationship maintenance are institutional analogs of residual connections — ways of keeping the substrate from tiring before the signal finishes its journey.

## Related Concepts

- [[analog-computation]] -- the computing mode vulnerable to substrate fatigue
- [[wiesner-pre-receiver-failure]] -- pre-receiver failure as the general category
- [[decision-fatigue]] -- human form of substrate fatigue
- [[residual-connections]] -- engineering fix for gradient-form substrate fatigue
- [[commons-governance]] -- Ostrom's substrate health = commons viability
- [[coherence-drift]] -- LLM form of substrate fatigue (attention-distance variant)
- [[digital-discretization]] -- the escape from substrate fatigue, and its cost

## Tensions and Contradictions

The concept assumes that the distinction between "substrate failure" and "signal failure" is clean. But in many real systems, they confound: decision fatigue might make a person more susceptible to misleading signals, so substrate and signal degrade together. The useful case is where a good signal fails because the substrate tires — but substrate and signal health are partially coupled, not independent.

## Key Sources

- [[what-arrives-depleted]] -- primary synthesis; introduces substrate fatigue as a unifying frame
- Baumeister et al. 1998 — original ego depletion; glucose model (contested)
- Shai Danziger et al. 2011 — judicial decision fatigue (criticized for confounds, but pattern robust)
- Ostrom 1990 — Governing the Commons; design principles for healthy governance substrate
- He et al. 2016 — residual connections (ResNet); skip connections as gradient-refreshing
- Wiesner 1983 (written 1969) — pre-receiver failure; quantum money and cryptography
