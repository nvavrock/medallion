# Core statistical arbitrage cluster {#core-stat-arb}

**Last updated:** 2026-05-28

Signals **SIG-001** through **SIG-007** form the best-sourced reconstruction cluster: equity and futures stat-arb, short-horizon mean reversion, momentum, pairs/cointegration, state-space tools, and order-flow microstructure. Each row below ties the hypothesis to Phase II data rows in [signal → data crosswalk](../chapters/02-data.html#signal-data-map).

## SIG-001 — Statistical arbitrage (equity baskets)

**Theory:** Mean-reverting residuals after factor neutralization. **Evidence level:** E2. **Replication:** partial — industry and journalistic narrative, not Medallion trade logs.

**Data dependencies:** `equity_daily_ohlcv`, `corporate_actions`, `equity_index_constituents`, `short_interest_borrow` (borrow from ~2003 [[claim:CLM-2027-001]]). **Era:** 1990s–present for diversified baskets; earlier futures/currency sleeves per [[claim:CLM-2024-002]].

**Capacity:** Alpha half-life months–years; crowding and factor regime shifts are primary failure modes. Cross-asset diversification extends capacity versus single-name pairs.

**Counterargument:** Public “stat arb” labels may bundle heterogeneous models; we cannot verify RenTech’s neutralization stack.

## SIG-002 — Short-horizon mean reversion

**Theory:** Microstructure overreaction and liquidity provision. **Replication:** partial — toy replication in [EXP-03](https://github.com/nvavrock/medallion/tree/main/experiments/03_mean_reversion) (EXP-03) on synthetic data with explicit costs.

**Data:** `equity_tick_trades`, `equity_intraday_ohlc`, `fx_spot_tick`, `order_book_l2` (L2 from ~2000s [[claim:CLM-2027-003]]). **Era gate:** consolidated US tape ~1993 [[claim:CLM-2027-002]].

**Capacity:** High turnover; transaction costs dominate at scale [[claim:CLM-2024-007]]. Linked to execution layer (Phase IV), not standalone “Medallion explanation.”

## SIG-003 — Momentum

**Theory:** Slow information diffusion. **Replication:** replicated — factor literature and multi-sleeve toy [EXP-07](https://github.com/nvavrock/medallion/tree/main/experiments/07_multi_signal) (EXP-07) combine with mean reversion under costs.

**Data:** `equity_daily_ohlcv`, `futures_continuous`, `fx_spot_tick`, `economic_releases`. **Failure mode:** momentum crashes (2009, 2020-style episodes).

## SIG-004 — Cointegration / pairs

**Theory:** Stationary spreads from shared drivers. **Era:** 1980s–1990s primary in Berlekamp-era public narrative [[claim:CLM-2024-005]]; auxiliary thereafter. **Replication:** partial — structural breaks limit live pairs count at scale.

## SIG-005 — Hidden Markov / regime (meta-signal)

**Theory:** Latent states govern return distributions. **Evidence:** E1 inference. **Replication:** partial — no fitted HMM on RenTech data; EXP-07 documents that **combining sleeves** can improve net Sharpe versus a single sleeve under costs without claiming regime identification.

**Data:** `equity_daily_ohlcv`, `rates_bonds_eod`, `macro_futures_curve`, `geopolitical_events_structured`. Treat as **sizing and risk overlay**, not standalone alpha.

## SIG-006 — Kalman / state-space

**Theory:** Dynamic betas and evolving spreads. Standard stat-arb toolkit (E2). **Replication:** partial — implementation-dependent; pairs with SIG-001 and SIG-004.

## SIG-007 — Order-flow imbalance

**Theory:** Signed volume predicts short-horizon prices (Hasbrouck, Kyle). **Replication:** partial — microstructure literature; no proprietary order-book replay.

**Data:** tick + L2 era 2000s+. **Capacity:** HFT-scale at minutes; capacity rises with holding period. Feeds Phase IV execution analysis and SIG-014 (inference).

## Cluster conclusion

Core sleeves plausibly explain **diversified short-horizon alpha** but not reported Sharpe or leverage alone. Risk stacking (SIG-015, Phase V) and costs (Phase IV) are required for a coherent public reconstruction.
