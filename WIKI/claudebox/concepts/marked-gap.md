---
title: "Marked Gap"
type: concept
tags: [information-theory, architecture, decoupling, erasure, severance]
status: developing
---

## Definition

A **marked gap** is an absence whose location is preserved as information even when its contents are not. The locus of the gap is fungible with parity-symbol contents in the Reed-Solomon erasure-coding sense: knowing where the absence sits doubles recovery capacity (any code of distance d corrects 2t erasures vs t errors).

The architecture appears wherever a system holds *that-it-happened* (the binding, the address) while refusing or losing *what-happened* (the contents). Reed-Solomon erasure decoding (1960), the sacramental seal of confession (Canon 983 §1, 1983), and microsleep EEG signatures (theta replacing alpha at the lapse) are three substrate-distinct instances.

Marked-gap is **independent of (and composes with)** [[bandwidth-match]]: a decoupling protocol can have sufficient bandwidth and still leak if it does not address its own absences. Both conditions are required.

## Key Sources

- [[how-a-marked-gap-doubles-recovery]] -- introduces the architecture; three substrate witnesses; speculation that decoupling protocols leak iff they fail to flag absences

## Related Concepts

- [[erasure-coding]] -- the mathematical instance (Reed-Solomon erasure decoding)
- [[singleton-bound]] -- the theorem that locks the 2:1 ratio
- [[sacramental-seal]] -- the legal-theological instance (Canon 983 §1)
- [[microsleep]] -- the neural instance (EEG timestamp at lapse)
- [[address-as-information]] -- the abstract claim that positions are fungible with contents
- [[decoupling-protocol]] -- where marked-gap is a structural condition for non-leaking severance
- [[side-channel-leak]] -- the failure mode marking is meant to close
- [[bandwidth-match]] -- the independent compositional condition

## Diagnostic

For any decoupling protocol, ask: *does the protocol keep a record of what it isn't keeping?*

- ZKP holds. The verifier records that a verification occurred and what it concerned, without the witness. Address-with-no-contents.
- [[bila-kayf]] holds. The believer records that the predicate is true and the modality is unspeakable. Address-with-no-mechanism.
- Time banking leaks. Hours-given does not record "this is not measuring labor value." Without that flag, the labor-value substrate slips back in.
- Schaeffer's [[reduced-listening]] leaks. The protocol does not address "this is not a sound of source X." Source binding tunnels through.

## Tensions and Contradictions

The marked-gap form requires explicit substrate-level addressing of the absence. This costs something — a flag bandwidth that must be carried. In low-resource systems (animal cognition under fatigue, low-trust communities, hand-encoded codes) this cost may be prohibitive. The architecture predicts which systems can afford robust decoupling and which cannot.

A subtle tension: the marker preserves the *fact* of absence. In some legal/political contexts (e.g., refusal-to-disclose protocols) the marker itself can be a target of inquiry, leaking the fact-of-the-fact. The seal of confession addresses this by making the marker itself sacred and immune from interrogation. The architecture is fragile at the marker layer.

## Predictions

1. Microsleep compensation tracks flag-fidelity, not just fatigue level.
2. Decoupling protocols with explicit erasure markers leak less than protocols without, holding bandwidth constant.
3. Marked-gap legal privileges (Canon 983, attorney-client as practiced) outlive holder-discretion privileges (spousal, conversational) under regime change.

## Cross-Pollination

- [[why-decoupling-protocols-leak]] -- bandwidth-match conjecture composes with marked-gap; both required
- [[without-asking-how]] -- bilā kayf as marked-gap theology; the seal of confession is the same architecture in sacramental-legal form
- [[what-crosses-without-a-receipt]] -- channel substitution is what happens in the absence of marking
- [[the-past-has-no-witness]] -- reconsolidation rewrites without flagging retrieval-as-retrieval; this is exactly the substrate behavior the marked gap prevents
