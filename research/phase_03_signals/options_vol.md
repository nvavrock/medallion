# Options and volatility cluster {#options-vol}

**Last updated:** 2026-05-28

Workstream **R3a** covers **SIG-008**, **SIG-009**, and **SIG-010**. Public RenTech-specific options detail is thin [[claim:CLM-2024-008]]; we grade mechanisms from market structure theory and industry practice, not proprietary books.

## Data foundation (Phase II)

| Signal | Matrix rows | Earliest plausible era |
|--------|-------------|------------------------|
| SIG-008 Vol surface arb | `options_chain_eod`, `volatility_surfaces`, `options_intraday_quotes` | 1995+ |
| SIG-009 Variance risk premium | `options_chain_eod`, `volatility_surfaces` | 1995+ |
| SIG-010 Dispersion / correlation | `options_chain_eod`, `volatility_surfaces`, `equity_index_constituents` | 2000+ |

Listed US options chains are widely available by the mid-1990s [[claim:CLM-2027-004]]. Fitted surfaces add model risk; intraday quotes raise storage post-2005.

## SIG-008 — Volatility surface arbitrage

**Theory:** Mispricing across strikes and tenors relative to underlying dynamics. **Replication:** partial — academic and sell-side vol-arb frameworks replicate **mechanism classes**; no Medallion sleeve weights.

**Failure modes:** gap risk, stochastic-vol model error. **Capacity:** depth-constrained versus equity stat-arb at similar gross leverage.

## SIG-009 — Variance risk premium harvesting

**Theory:** Implied volatility systematically exceeds realized over horizons (VRP literature). **Replication:** partial — VRP is among the better-documented options factors in academia (E3 evidence on mechanism); fund-specific sizing unknown.

**Failure modes:** 2008, 2020 vol spikes. **Capacity:** moderate until tail events; pairs with tail-risk layer (Phase V).

## SIG-010 — Dispersion / correlation trading

**Theory:** Index versus single-name implied correlation mispricing. **Replication:** partial — institutional strategy type documented; crisis correlation breakdown (2008) is a known failure mode.

**Capacity:** desk-sized; scales with index and single-name liquidity.

## Era plausibility vs. Medallion narrative

Options sleeves are **plausible from the 1990s** onward but should be labeled **E1–E2** for RenTech weighting. They likely complement—not replace—core stat-arb and microstructure alpha. We do not infer a dominant share of returns from options alone.

## Counterarguments

- **Model risk:** Surface fitting errors can look like alpha in backtests.
- **Capacity:** Medallion’s closed structure may have absorbed vol premia early; crowding post-2010.
- **Sourcing:** Journalism mentions derivatives exposure; magnitudes are not audited.

See canonical fields in [data/signals.yaml](https://github.com/nvavrock/medallion/blob/main/data/signals.yaml) and the [signal database](../appendices/signal-database.html) appendix.
