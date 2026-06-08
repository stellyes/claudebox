---
title: "Connection: Screening by Implausibility <-> Population-Indexed Signal"
type: connection
domains: [information-security, signaling-theory, bayesian-inference]
tags: [signaling, screening, population]
---

## The Link

These two diagnostics are duals across the same communication channel. A [[population-indexed-signal]] is read *upstream*: its meaning is fixed by the distribution of who sends it (`P(source | marker)`), so flooding the senders re-indexes the meaning without touching the marker — the em-dash inverting from "careful human" to "probable machine." [[screening-by-implausibility]] acts *downstream*: the signal is engineered to *shape* the distribution of who responds, repelling the non-target so only the intended audience self-selects — the scam email tuned to be answered only by the gullible.

One end **infers** the crowd that produced the signal. The other end **sculpts** the crowd the signal will keep. Both treat a signal as an instrument operating on the demographics of a channel rather than as a carrier of fixed content.

## Evidence

- **Upstream / population-indexed:** [[why-the-em-dash-became-a-confession]] — the marker is frozen, its meaning floats on the sender base rate.
- **Downstream / screening:** [[why-scams-are-implausible-on-purpose]] — Herley 2012: the email is a classifier; implausibility minimises false positives by purifying the responder pool. Tooby's absurd coalition badges and Iannaccone's costly prohibitions are the same downstream filter.

## Implications

The pair suggests a unified object: a **channel-demographic operator**. Believability is the shared control variable but is used in opposite directions — you *maximise* it to inform and read sources cleanly, and you *spend* it to select and shape responders. The open question is whether a single formalism (a base-rate term the operator either reads or sets) covers both, and whether the cost that powers the downstream filter has a third possible address — the medium itself — beyond sender and receiver.
