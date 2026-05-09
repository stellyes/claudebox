---
title: "Hallucination as Bootstrap Failure"
type: concept
tags: [llm, calibration, contrast, speculation]
status: draft
---

## Definition

Speculative reframing of LLM hallucination: the model is doing [[singleton-bootstrap]] for tokens whose [[contrast-scaffold]] in the training corpus is too thin. Where contrast neighbors are dense, the model interpolates correctly; where they are sparse (hapax-rich domains), the model fills in plausibly *with the same confidence calibration* as the dense case. The hallucination is not a retrieval bug. It is a structural feature of bootstrapping: the model has no signal that distinguishes "neighbors-supply-this" from "neighbors-do-not-exist-for-this."

## Implications

- Calibration error should correlate with hapax-likeness in the training corpus.
- A diagnostic for hallucination would be a *contrast-set sufficiency check on the input* — does the input have enough neighbors in the training distribution? — rather than a confidence threshold on the output.
- Hapax-rich domains are predictably high-hallucination: ancient texts, technical poetry, low-resource languages, recent jargon, dialect words, names of obscure proteins.

## Connection to Existing Threads

- [[counter-ledger]] — the hallucination case is one where the running estimate of resolution cost should fire but doesn't. A bootstrap-failure detector is essentially a Counter-Ledger entry.
- [[without-asking-how]] — the LLM's confident output is bila kayf without the warning sticker.

## Status

Speculation — not yet empirically tested. A real test would require a tractable measure of "hapax-likeness" for tokens in a large training corpus, plus correlation with downstream hallucination rates.

## Key Sources

- [[why-meaning-needs-neighbors]] — primary source page.
