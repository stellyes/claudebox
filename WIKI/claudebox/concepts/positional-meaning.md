---
title: "Positional Meaning"
type: concept
tags: [information, cross-domain]
status: developing
---

## Definition

**Positional meaning** is the principle that in a system where elements take their
significance from their relationships, the carrier of information is the *configuration*,
not the *unit*. The nameable thing — the gene, the word, the token — is a **handle**:
countable, editable, storable in a database. The information actually lives in the
**holdfast**: the neighborhood, the fold, the weighted context the handle sits in. The
giveaway is always the same experiment — *move the handle without changing it, and watch
the meaning move anyway.*

## The three witnesses

| Domain | Handle (named unit) | Holdfast (real carrier) | The moving-handle experiment |
|---|---|---|---|
| Genome | base sequence / "the gene" | 3D fold, TAD neighborhood | Lupianez 2015: relocate a TAD boundary, sequence untouched → enhancer hijacks wrong gene → deformed limb |
| Language | the word / dictionary entry | distribution over contexts | Firth/Harris: "bank" has no meaning until "river" or "deposit" supplies one |
| Transformers | the token | attention over context + positional encoding | the same token at a new position is, for the model, a different thing |

The convergence is the claim: these are not three analogies but one law seen three times.
Position-effect variegation ([[hermann-muller]] 1930) is the [[distributional-hypothesis]]
discovered sixty years early in a fruit fly's eye.

## The inversion

The genome "confounded AI" exactly as long as AI read it like a dictionary — token by
token, locally. It began to yield the moment AI brought the lesson language already taught:
read the company a token keeps. Genomic language models (Enformer, Evo, Nucleotide
Transformer) work only when given the long-range context (200kb–1Mb) the meaning actually
occupies. The genome did not get simpler; our model of *reading* got deeper. See
[[attention-as-context-reading]] and [[three-dimensional-genome]].

## Tensions and Contradictions

- **The speculative reach.** The essay bets that gene-knockout surprises and neural-net
  interpretability failures are the *same* category error — localizing a property that lives
  in relational structure. This is labeled speculation, not a finding; the strong form (no
  function is ever localized) is almost certainly false (some genes are near-Mendelian, some
  features are near-monosemantic). The defensible claim is weaker: relational carriage is the
  *default*, and locality is the exception that must be earned.
- **Is anything exempt?** A true lookup table (a hash map, a genuine one-to-one code) has
  local meaning by construction. The open question is what structural property makes a system
  exempt from relational drift — and whether biological/linguistic systems are exempt anywhere.

## Connections

- [[what-builds-the-receiver]] — meaning is manufactured at reception, not shipped inside the symbol. Positional meaning is the structural reason why.
- [[the-lossless-and-the-lossy]] — you cannot serialize relational meaning into a list of independent units without losing the part that lived *between* them.
- [[substrate-enforced-humility]] — adjacent: there the substrate carries what the symbol cannot (precision); here the *configuration* carries what the unit cannot (function). Both deny that the symbol string is the whole record.

## Key Sources

- [[why-a-gene-is-more-like-a-word]] — PRIMARY MINT (#49). Information that looks locally stored is actually stored relationally; the named unit is a handle, the holdfast is the configuration. Spans genome (TAD/fold), language (distributional hypothesis), transformers (attention).

## Synthesis

The recurring error across fields is not stupidity but economy: the handle is cheap to name
and the holdfast is expensive to measure, so every field reaches for the unit and mistakes it
for the thing. Positional meaning is the correction that keeps arriving — and the test for
whether you've understood a system is whether you know which edits stay local (inside a domain)
and which ones ripple (across a boundary).
