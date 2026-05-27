# Phase III — Signal Reconstruction

## Signal Hypothesis Database

Canonical store: [data/signals.yaml](../../data/signals.yaml)

| Signal ID | Class | Era | Confidence |
|-----------|-------|-----|------------|
| SIG-001–004 | Core stat arb | 1980s+ | 0.55–0.75 |
| SIG-005–006 | Regime / state-space | 1990s+ | 0.35–0.50 |
| SIG-007 | Order flow | 2000s+ | 0.60 |
| SIG-008–010 | Options/volatility | 1990s+ | 0.40–0.55 |
| SIG-011–014 | Modern ML / alt data | 2005–2015+ | 0.30–0.55 |
| SIG-015 | Kelly sizing | 1980s+ | 0.40 |

## Data dependencies (Phase II)

Before deepening signal essays or running Phase VII experiments, map each signal to datasets in [phase_02_data/signal_data_map.md](../phase_02_data/signal_data_map.md) and cite matrix rows in experiment configs.

## PDF workstreams

- **Options/volatility:** SIG-008, SIG-009, SIG-010 (see tags `options`, `volatility`)
- **Modern ML/NLP:** SIG-011, SIG-012, SIG-013, SIG-014 (tag `ml`)

## Evaluation criteria (per signal)

Each entry documents theory, evidence, replication, capacity, failure modes, and era plausibility.

Requirement: R3, R3a, R3b
