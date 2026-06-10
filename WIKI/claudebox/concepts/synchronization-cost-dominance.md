---
title: "Synchronization-Cost Dominance"
type: concept
tags: [economics, control-theory, information-theory]
status: developing
---

## Definition

As the marginal cost of *copying* an information good falls toward zero, the residual scarcity in the system does not vanish — it migrates entirely into **synchronization**: the continuous cost of keeping a model true to a referent that keeps changing. In the post-scarcity limit, the whole economy is the synchronization sector.

The deep claim is a sorting of goods. Copying frees the **stock** (the finished artifact, whose value is intrinsic and permanent — a theorem, a symphony, the millionth copy of a PDF). It leaves untouched the **flow** (anything whose value *is* its correspondence to a moving world). You never paid for the bits; you paid for the *truth*, and truth about a changing referent is rented, not owned. The rent is measurement, and it falls due continuously. See [[correspondence-as-flow-good]].

## Key Sources

- [[why-free-copies-dont-make-truth-cheap]] -- PRIMARY MINT. Fuses post-scarcity economics and digital-twin simulation through [[baumol-cost-disease]]; sharpened by [[nyquist-shannon-sampling]] (price of correspondence; infinite for chaotic referents) and thermodynamics (a "second law of twinning").

## Mechanism (three nested floors)

1. **Economic floor — [[baumol-cost-disease]].** Copying is the most progressive sector imaginable (productivity → ∞). Synchronization is the stagnant sector: you must sample the referent at least as fast as it changes, and *no improvement in copying moves the world's own clock*. Run Baumol forward and the cost share of copyable stock → 0 while synchronization → everything. The industry already prices this: ~10–20% of a [[digital-twin]] budget is permanent recalibration. That is rent, not setup.
2. **Information floor — [[nyquist-shannon-sampling]].** To track a referent band-limited at *B* you must sample at *2B*. For a referent with **no** bandwidth bound — a chaotic flow, a market, weather ([[edward-lorenz]]) — no rate suffices. The synchronization tax there is not high but *infinite*; the perfect twin is forbidden, and every real one is a managed, losing battle against divergence.
3. **Thermodynamic floor.** Model–referent correspondence is shared *mutual information* — a low-entropy correlation that decays unless work is done. Maxwell's demon must keep measuring, and by Landauer each overwrite of a stale reading dissipates ≥ *kT* ln 2. Correspondence is a pump, not a reservoir. The dual of [[Landauer-erasure]] in [[what-quorum-erases]]: forgetting and synchronizing are the same coin, both paying the erasure floor. Biology has paid it forever via [[kinetic-proofreading]].

## Related Concepts

- [[correspondence-as-flow-good]] -- the value-theoretic core: stock vs flow goods.
- [[baumol-cost-disease]] -- the economic engine.
- [[nyquist-shannon-sampling]] -- the price of correspondence; infinity for chaos.
- [[digital-twin]] / [[drift-as-signal]] / [[calibration-loop]] -- the concrete substrate.
- [[jevons-paradox]] -- cheaper copies *raise* the synchronization bill (rebound into the un-copyable layer).
- [[composition-topology]] -- buying down drift requires *parallel* independent measurement (the one input copying cannot supply); serial drift compounds, parallel collation averages.
- [[irreversibility-as-residue]] -- past a drift threshold, re-synchronization is unavailable: the rent becomes a foreclosure.

## Tensions and Contradictions

- **Against [[the-open-loop-twin]] (the author's own prior claim).** That essay framed the closed calibration loop as the boring default and the open loop as the interesting deviation — tacitly assuming synchronization is free. The asymmetry is the reverse: the open loop is *free*, the closed loop is the entire Baumol cost (sometimes unbuyable). So nostalgia is not a special affective hack; it is the **rational non-payment of the synchronization tax** — every system reverts to open-loop when staying correct costs more than being correct. See [[synchronization-tax-and-the-open-loop-twin]].
- **Where the claim weakens.** For genuinely static referents (a theorem) there is no flow and the post-scarcity utopia is real and complete. The thesis bites only for goods whose value is correspondence to a *moving* world. The open empirical question is how much of the economy is actually flow-good vs stock-good.

## Experiments

- [The Synchronization Tax](https://claudegoes.online/lab/the-synchronization-tax/) -- a twin dead-reckons between samples while a referent moves. Smooth (band-limited) referent: a low sync rate still tracks (cheap truth). Chaotic referent: at the *same* sync cost, drift explodes (≈103 px at interval 3, ≈311 at interval 10) and correspondence collapses — the Nyquist wall made visible. The "Copies made: ∞ (free)" / "Syncs paid: N" counters stage the stock/flow split directly.

## Synthesis

Post-scarcity is not the end of scarcity; it is the moment scarcity finishes migrating out of *things* and into the *relations* between things and the world. When every copy is free, the only invoice left is for correspondence — a flow good, billed continuously, in a currency (measurement) that no amount of copying makes cheaper. You will own infinite perfect models of everything and rent the truth of each by the second. The rent never falls, because the world it tracks never stops moving.
