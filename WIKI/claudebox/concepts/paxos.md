---
title: "Paxos"
type: concept
tags: [distributed-systems, consensus, computer-science]
status: live
---

## Definition

Leslie Lamport's 1998 consensus protocol for distributed systems. The protocol's full structure — ballot numbers, prepare/promise/accept rounds, the rule that any new round must consult prior accepted values — exists for the partition case. Stripped of partition tolerance the protocol collapses into trivial sequential agreement.

The original paper (*The Part-Time Parliament*) framed the protocol via a fictional Greek parliament whose members were intermittently absent: the parliament IS the recovery procedure. Diego Ongaro and John Ousterhout's 2014 Raft was a redesign of the same protocol with the recovery flow factored to the surface (*"Paxos but legible"*).

## Key Sources

- [[what-the-fracture-decides]] -- Paxos as witness for failure-defined structure in software protocols

## Tensions and Contradictions

- Variants (Multi-Paxos, Fast Paxos, Egalitarian Paxos) differ in their handling of partition latency.
- Compatible with the FLP impossibility result: consensus under fully asynchronous failure is impossible; Paxos works around this by assuming partial synchrony.

## Synthesis

The shape of the protocol IS the shape of the partitions it has been built to absorb. Without partitions, the protocol is ornamental. Reading the happy-path log will not let you reconstruct the protocol.
