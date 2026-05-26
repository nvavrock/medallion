# Phase VIII — Synthesis

See [disclaimer](../../docs/disclaimer.md).

## What plausibly explains performance

1. **Diversified short-horizon predictive signals** (stat arb, momentum, micro) with rigorous neutralization (SIG-001–007).
2. **Risk stack** — vol targeting, banded leverage [[claim:CLM-2024-004]], portfolio diversification [[claim:CLM-2024-003]].
3. **Execution quality** — reduces drag but unlikely sole driver [[claim:CLM-2024-007]].
4. **Options/volatility sleeves** — plausible but under-sourced [[claim:CLM-2024-008]] (SIG-008–010).
5. **Organizational moat** — hiring, secrecy, long-horizon R&D [[claim:CLM-2024-009]].

## What remains unexplained

- Exact signal weights and model architectures (proprietary).
- Precise net Sharpe and leverage paths (public range only).
- Full regulatory/tax optimization magnitude (E1 hypothesis below).

## Survivorship and failed peers

LTCM demonstrates concentration and leverage risks in relative-value structures [[claim:CLM-2024-010]]. Medallion’s shorter holding periods, diversification, and capacity caps (inferred) differ materially — **survivorship bias** cautions against comparing only winners.

DE Shaw spin-outs and other quant funds show that talent dispersion does not guarantee Medallion-level returns.

## Regulatory / structural edges (hypothesis)

We hypothesize (E1) incremental net benefits from:

- Tax-aware trading and wash-sale management
- Liquidity rebates and maker-taker optimization
- Preferential fee tiers at brokers (unverified for RenTech)

These cannot be quantified from public data; they belong in sensitivity analysis, not point estimates.

## Modern ML

Post-2010 NLP and alt-data (SIG-011–012) are **industry-wide**; RenTech’s early ML scale-up [[claim:CLM-2024-006]] suggests advantage in **integration and data hygiene**, not necessarily novel architectures alone.

## Simulation limits

Experiments under `experiments/` include costs and capacity but are **toys**. They support directional claims (e.g., costs erode naive Sharpe) not replication of Medallion returns.

## Counterarguments

- **Luck and selection:** One flagship fund among many strategies.
- **Reporting bias:** External LP anecdotes may overweight gross returns.
- **Capacity:** Past returns may not scale; fund closed to outsiders.

Requirement: R8
