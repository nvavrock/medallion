## Overview

**Last updated:** 2026-05-28

## Signal Hypothesis Database

Canonical store: [data/signals.yaml](https://github.com/nvavrock/medallion/blob/main/data/signals.yaml)

| Signal ID | Class | Era | Confidence |
|-----------|-------|-----|------------|
| SIG-001–004 | Core stat arb | 1980s+ | 0.55–0.75 |
| SIG-005–006 | Regime / state-space | 1990s+ | 0.35–0.50 |
| SIG-007 | Order flow | 2000s+ | 0.60 |
| SIG-008–010 | Options/volatility | 1990s+ | 0.40–0.55 |
| SIG-011–014 | Modern ML / alt data | 2005–2015+ | 0.30–0.55 |
| SIG-015 | Kelly sizing | 1980s+ | 0.40 |

## Chapter sections

| Essay | Signals | Requirement |
|-------|---------|-------------|
| [Core stat arb](#core-stat-arb) | SIG-001–007 | R3 |
| [Options / vol](#options-vol) | SIG-008–010 | R3a |
| [Modern ML](#modern-ml) | SIG-011–014, SIG-013 | R3b |

## Data dependencies (Phase II)

Before deepening signal essays or running Phase VII experiments, map each signal to datasets in [signal → data crosswalk](../chapters/02-data.html#signal-data-map) and cite matrix rows in experiment configs.

## Replication (Gate B)

Fifteen signals; **≥10** must have `replication` ≠ `not_attempted` (verified by `scripts/validate_signals.py`). Six signals upgraded to `partial` in v0.5.0 with explicit limitations (no silent `not_attempted` for industry-wide mechanisms).

## Evaluation criteria (per signal)

Each entry documents theory, evidence, replication, capacity, failure modes, and era plausibility.

Requirement: R3, R3a, R3b
