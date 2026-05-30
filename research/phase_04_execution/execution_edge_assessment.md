# Can execution edge alone explain Medallion? {#execution-edge-assessment}

**Last updated:** 2026-05-28

## Research question

**Can execution edge alone explain a significant fraction of reported Medallion performance?**

## Answer

**No** as a sole explanation [[claim:CLM-2024-007]]. Public reconstruction treats execution as **necessary** (cost and impact control) but **insufficient** without diversified predictive signals (Chapter III) and risk stacking (Chapter V).

## EXP-04 interpretation (toy)

[EXP-04](https://github.com/nvavrock/medallion/tree/main/experiments/04_almgren_chriss) aggregates many small per-trade edges minus costs and Almgren–Chriss-style impact. Sensitivity over `participation_rate` shows impact rising with participation — higher turnover strategies face steeper implementation shortfall.

Typical frozen run magnitudes are **negative net Sharpe** at modest edge_bps once costs and impact bind. Directional lesson: **microstructure alpha must exceed impact plus fees**; labeling execution as “the secret” without signal capacity is inconsistent with toys and with industry microstructure literature.

## Regulatory / structural increments (E1)

Liquidity rebates, fee tiers, and tax-aware routing may add incremental net return (Chapter VIII). These are not quantified here.

Requirement: R4
