# Phase IV — Market Microstructure & Execution

## Models studied

- **Almgren–Chriss** — optimal execution with temporary/permanent impact [almgren_chriss2000]
- **Kyle (1985)** — informed trading and market depth [kyle1985]
- **Hasbrouck** — microstructure econometrics [hasbrouck2007]

## Research question

**Can execution edge alone explain a significant fraction of reported Medallion performance?**

Public evidence suggests **no** as a sole explanation [[claim:CLM-2024-007]]: transaction costs, impact, and capacity constrain microstructure-only stories unless paired with predictive alpha.

## Experiment

See [experiments/04_almgren_chriss/](../../experiments/04_almgren_chriss/) — cost-aware execution edge toy model.

## Regulatory / structural edges (inference)

We hypothesize (E1) that liquidity rebates, fee tiers, and tax-aware trading may add **incremental** net return but are under-documented publicly. Full treatment in Phase VIII — Synthesis (see `research/phase_08_synthesis/synthesis.md` or the site chapter *Phase VIII*).

Requirements: R4, R4b
