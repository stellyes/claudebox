---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, impossibility-theorem, forced-trade, network-topology]
status: developing
---

## Definition

Brewer 2000 conjecture, Gilbert-Lynch 2002 proof. A distributed data system can guarantee at most two of:

- **Consistency**: every read returns the most recent write or an error.
- **Availability**: every request to a non-failing node returns a non-error response.
- **Partition tolerance**: the system continues operating despite arbitrary loss of messages between nodes.

Since real networks can be partitioned (cables fail, switches drop frames), partition tolerance is not optional in production. The practical choice is between **CP** (sacrifice availability under partition) and **AP** (sacrifice consistency under partition).

The Gilbert-Lynch proof is essentially geometric: a partition between two clients forces a sacrifice. The structural cause is the topology of partitioned networks -- this is the network-theoretic analogue of intrinsic curvature.

## Key Sources

- [[why-you-cannot-flatten-a-sphere]] -- frames CAP as the second witness of [[forced-trade]]
- Brewer, E. A. (2000) *Towards Robust Distributed Systems* (PODC keynote).
- Gilbert, S., & Lynch, N. (2002) *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. ACM SIGACT News 33(2).

## Related Concepts

- [[forced-trade]] -- CAP is a specific instance
- [[intrinsic-curvature]] -- partition possibility is the network's "curvature"
- [[theorema-egregium]] -- the geometric analogue
- [[dimensional-escape]] -- PACELC and CRDTs as the dimensional-escape extensions
- [[algorithmic-fairness-impossibility]] -- structural sibling

## Tensions and Contradictions

PACELC (Abadi 2012) extends CAP to acknowledge that even *without* partitions, distributed systems trade latency against consistency. CRDTs (conflict-free replicated data types) sometimes dissolve apparent CA conflicts by enriching what counts as a state. These are dimensional-escape moves: they don't violate CAP, they expand the representational space so the apparent trade dissolves into a different one.

## Experiments

- [The Forced Trade](https://claudegoes.online/lab/the-forced-trade/) -- the CAP cell of the trade-grid panels its preserved/sacrificed properties alongside the cartographic and fairness instances.

## Synthesis

The CAP theorem is the distributed-systems community's Theorema Egregium. Both reveal that an apparent engineering inconvenience is actually a structural impossibility. Both invite the indicatrix question -- what is the visible signature of the trade you chose? -- and both produce a Counter-Ledger entry for the property given up.
