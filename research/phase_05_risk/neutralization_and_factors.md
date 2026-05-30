## Neutralization and factor control {#neutralization-and-factors}

**Last updated:** 2026-05-28

### Layer 2 — Neutralization

**Function:** Remove unintended exposure to market, sector, and style factors so sleeve PnL reflects stock-specific or residual alpha.

### Plausible mechanisms

- Dollar and beta neutrality for equity stat-arb (SIG-001)
- Industry and factor constraints on baskets
- Eigenfactor or shrinkage covariance estimates (industry practice; RenTech-specific factors unknown)

### Evidence stance

Industry-standard for market-neutral funds (E2). We do not observe RenTech’s factor set or rebalance frequency [[claim:CLM-2026-018]].

### Failure modes

- Factor model misspecification (hidden beta in crises)
- Crowding in popular neutralization bases
- Regime shifts where historical factor loadings fail

### Data dependencies

`equity_daily_ohlcv`, `equity_index_constituents`, `corporate_actions` per [signal crosswalk](../chapters/02-data.html#signal-data-map).
