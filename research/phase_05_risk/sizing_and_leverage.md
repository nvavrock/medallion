# Sizing, vol targeting, and leverage {#sizing-and-leverage}

**Last updated:** 2026-05-28

## Layer 3 — Position sizing

Volatility targeting scales exposure inversely to realized vol. Fractional Kelly variants translate estimated edge into growth-optimal weights with drawdown controls (SIG-015).

## Leverage band (hypothesis)

We hypothesize (E1) effective leverage often operated within **~5×–12×**, not a single constant [[claim:CLM-2024-004]]. Point estimates above that band without E3 sourcing should be labeled speculative.

## Sharpe bands (hypothesis)

Reported gross Sharpe **>5** in secondary sources is not audited [[claim:CLM-2024-003]]. Reconstruction uses a **~3–7+ speculative band** for discussion, not replication.

## EXP-05 interpretation

[EXP-05](https://github.com/nvavrock/medallion/tree/main/experiments/05_vol_target_kelly) shows **gross Sharpe can exceed net** when leverage adjustments trigger turnover costs. Sensitivity over `commission_bps` and leverage bands illustrates that sizing rules interact with costs — high gross Sharpe in toys does not map to Medallion claims.

## Failure modes

- Estimation error in covariance and edge
- Procyclical leverage into vol spikes
- Liquidity contraction when de-grossing
