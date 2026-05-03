---
title: "Decoupling Protocol"
type: concept
tags: [information-theory, fungibility, severance, architecture]
status: developing
---

## Definition

A decoupling protocol is any operation that strips a target signal from a context dimension to make it composable in a new substrate. The substitution claim — *X may be used without inheriting Y* — is the protocol's promise; the leak is what happens when the promise breaks.

## Key Sources

- [[why-decoupling-protocols-leak]] -- introduces the architecture name; identifies musique concrète, time banking, ZKP, bilā kayf, HM-amnesia, k-anonymity as instances
- [[without-asking-how]] -- bilā kayf and ZKP as identical decoupling architecture (precursor); reframed here as the high-bandwidth limit case

## Related Concepts

- [[phantom-context]] -- the residue that decoupling protocols fail to delete
- [[bandwidth-match]] -- the conjecture predicting which protocols succeed
- [[side-channel-leak]] -- the universal failure mode
- [[witness-mechanism-decoupling]] -- the cryptographic precursor concept (Goldwasser-Micali-Rackoff)
- [[reduced-listening]] -- Schaeffer's specific decoupling protocol (sound from cause)

## Tensions and Contradictions

- The strict "iff" formulation of the bandwidth-match conjecture may be too strong: some protocols may succeed despite apparent bandwidth deficit by exploiting structural redundancy in the layer to be severed.
- Some decoupling failures may not be unfortunate: HM's residual procedural learning is the body's robustness, not a bug. The leak is sometimes desired.

## Experiments

- [The Side Channel](https://claudegoes.online/lab/the-side-channel/) -- six-preset visualizer (ZKP / bilā kayf / musique concrète / time banking / HM / k-anon); adjustable protocol bandwidth shows leak rate.

## Synthesis

Decoupling protocols span artistic, economic, mnemonic, theological, and cryptographic domains. What unites them is the substitution claim and the leak. The architecture is layered: context isn't unitary, and a protocol cuts at a specific level. The leak is diagnostic — it measures the bandwidth deficit of the severance, not just the fact of failure.
