---
title: "Marked Gap and Side Channel"
type: connection
tags: [marked-gap, decoupling, side-channel-leak, architecture]
---

## The Connection

Marking the gap closes the side channel. This is the structural dual of the [[side-channel-leak]] failure mode identified in [[why-decoupling-protocols-leak]]: when a decoupling protocol does not address its own absences, the substrate fills the assumed-empty space with residue tunneling through the next-most-available channel. When the protocol *does* address the absence — when the priest holds the binding, when the EEG timestamps the lapse, when the erasure flag is set — the substrate is told where the gap is and stops trying to fill it.

This is independent of (and composes with) the [[bandwidth-match]] conjecture. A protocol can have sufficient bandwidth and still leak if it does not flag its own absences. Both conditions are required and orthogonal.

## Diagnostic

For any candidate decoupling protocol, ask two independent questions:

1. **Bandwidth-match**: is the protocol bandwidth ≥ the layer's information bandwidth?
2. **Marked-gap**: does the protocol carry an explicit address for what it is *not* keeping?

If both hold, the severance can succeed. If either fails, residue tunnels.

## Why It Matters

The dual nature explains why some protocols hold and others leak even when bandwidth is ample. Time banking has plenty of bandwidth in principle (every transaction is a chance to flag context) but fails because the protocol does not articulate "this is not money." Schaeffer's reduced listening could mark "this is not a sound of source X" but does not. ZKP and bilā kayf hold because they mark the absence of witness/mechanism explicitly.

The marked-gap form is what allowed Canon 983 §1 to formalize a protocol that survives across centuries of social pressure: the priest holds the binding, refuses the contents, and is forbidden from acting on the content in ways that would leak the address-of-the-content. Holder-discretion privileges (spousal) lack the marked-gap form and erode faster.

## Sources

- [[how-a-marked-gap-doubles-recovery]] -- introduces the dual condition
- [[why-decoupling-protocols-leak]] -- the bandwidth-match conjecture
- [[without-asking-how]] -- bilā kayf as marked-gap theology
- [[the-past-has-no-witness]] -- reconsolidation as the unmarked failure mode
