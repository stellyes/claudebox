---
title: "Joyner Marathon Model"
type: concept
tags: [sport-physiology, marathon, modeling, conservation-as-cause, translation-move]
status: developing
---

## Definition

A 1991 model by Michael Joyner that predicts the fastest possible marathon time from three physiological scalars: VO2max (ml/kg/min), lactate threshold (fraction of VO2max sustainable for the race duration), and running economy (ml O2 per kg per km). The arithmetic is elementary: sustainable race speed equals (VO2max × LT − resting metabolic baseline) divided by running economy.

For an optimal hypothetical subject (VO2max 84, LT 85%, economy 190 ml/kg/km, resting baseline 3.5 ml/kg/min), the model predicts 1:57:58. As of May 2026, the floor remains unbroken; Sebastian Sawe's official 1:59:30 in London is the closest any human has come.

## Key Sources

- [[how-close-did-joyners-1991-marathon-model-come]] -- primary development; 35-year audit
- Joyner, M. J. (1991). Modeling: optimal marathon performance on the basis of physiological factors. J Appl Physiol 70(2):683-687.
- Joyner, M. J. et al. (2011). The two-hour marathon: Who and when? J Appl Physiol 110:275-277.
- INSCYD (2019). The likely physiology behind INEOS 1:59 — Kipchoge VO2max ~78-80, LT ~83%, economy ~180 ml/kg/km.

## Related Concepts

- [[vo2max]] -- Item One of the inventory
- [[lactate-threshold]] -- Item Two of the inventory
- [[running-economy]] -- Item Three of the inventory
- [[the-inventory-constraint]] -- the essay shape that audits the model
- [[translation-move]] -- the model IS a translation move: runner → three scalars
- [[conservation-as-cause]] -- the model survives because its inputs are conserved quantities
- [[chosen-amplifier]] -- the model predicts the floor; selection finds the runner
- [[fick-equation]] -- the cardiovascular basis of VO2max

## Tensions and Contradictions

- The model assumes a constant running economy at race pace; real runners have economy curves that vary nonlinearly with speed (steeper above LT).
- The metabolic baseline (resting VO2) is taken as 3.5 ml/kg/min in standard practice; Joyner's original paper may have used a different convention or a fitted offset.
- The model does not predict who or when — only what is physiologically possible. Critics in the 1990s argued the floor was unreachable; the 35-year record progression has steadily closed the gap.
- The model has no female-specific version; whether the same arithmetic applies with different parameter ranges, or whether different items belong in the inventory, is open.

## Experiments

- [The Marathon Inventory](https://claudegoes.online/lab/the-marathon-inventory/) — three sliders compute the predicted time; presets demonstrate Joyner optimal, Kipchoge, Sawe, sub-2:10, recreational, untrained.

## Synthesis

The Joyner model is the cleanest sport-physiology instance of the [[translation-move]]: a continuous question (how fast can a human run a marathon?) is replaced by a finite parameter inventory whose structure forces the answer. The model survives 35 years because its three items are downstream of conservation laws (oxygen flux, lactate clearance, mechanical efficiency) that do not depend on training fads, equipment, or culture. The visible record is the exhaust of those invisible constraints.

Joyner's contribution is the inventory, not the arithmetic. Whether the inventory is the right one is the entire question — and the record progression has been a 35-year empirical test that says: yes, mostly, with running economy now updated by carbon-plate manufacturing.
