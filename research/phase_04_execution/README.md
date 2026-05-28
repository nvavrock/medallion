## Overview

**Last updated:** 2026-05-28

See [disclaimer](../about.html).

## Models studied

| Model | Role | Citation |
|-------|------|----------|
| **Almgren–Chriss** | Optimal execution with temporary/permanent impact | [almgren_chriss2000] |
| **Kyle (1985)** | Informed trading, market depth, adverse selection | [kyle1985] |
| **Hasbrouck** | Microstructure econometrics, price discovery | [hasbrouck2007] |
| **Propagator / impact** | Transient impact from order flow (literature analogue) | Industry microstructure surveys |

## Mechanisms evaluated

### Order-flow imbalance and short-horizon prediction

Signed volume and queue position predict prices at horizons from seconds to days (SIG-007). Consolidated US tape from ~1993 and L2 feeds from ~2000s [[claim:CLM-2027-002]] [[claim:CLM-2027-003]] set the **era gate** for replicating microstructure alpha at scale.

### Inventory and liquidity provision

Market makers and HFT liquidity providers earn spreads but face inventory risk; Kyle-type models formalize when informed flow erodes that edge. Medallion’s holding periods (inferred shorter than LTCM-style convergence trades) change the relevant horizon.

### Cross-venue execution and latency

Multi-venue routing, colocation, and fee tiers are **E1** for RenTech specifically but well documented industry-wide. They interact with regulatory edges (rebates, maker-taker) treated in Phase VIII.

### Market impact and capacity

Permanent and temporary impact constrain how much notional can be turned over before alpha is arbitraged away. This is central to the capacity narrative for stat-arb and micro sleeves.

## Research question

**Can execution edge alone explain a significant fraction of reported Medallion performance?**

**Answer (sourced inference):** **No** as a sole explanation [[claim:CLM-2024-007]]. Transaction costs, impact, and capacity bind microstructure-only stories unless paired with predictive alpha. Execution is a **necessary cost control layer** (Phase V layer 4), not a substitute for signal diversity (Phase III).

## Experiment (R4b)

[EXP-04](https://github.com/nvavrock/medallion/tree/main/experiments/04_almgren_chriss) — EXP-04 implements a cost-aware Almgren–Chriss-style toy:

- Inputs: participation rate, impact coefficients, commission and slippage bps
- Outputs: implementation shortfall versus naive schedule
- Linked signals: SIG-007 (microstructure), SIG-014 (execution inference)

Sensitivity: vary `participation_rate` per the [test plan](https://github.com/nvavrock/medallion/blob/main/docs/test_plan.md); record in `results/summary.json`.

## Reinforcement learning (inference)

SIG-014 remains **E1** at RenTech. EXP-04 bounds **static** optimal execution; RL may improve paths but cannot be replicated here without proprietary simulators.

## Regulatory / structural edges (inference)

We hypothesize (E1) that liquidity rebates, fee tiers, and tax-aware trading add **incremental** net return but are under-documented publicly. Quantitative treatment: Phase VIII — Synthesis.

Requirements: R4, R4b
