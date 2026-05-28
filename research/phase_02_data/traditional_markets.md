# Traditional markets data {#traditional-markets}

**Last updated:** 2026-05-26

Deep dive on core market datasets grouped by **latency tier**: end-of-day → intraday bars → tick/trades → limit order book (L2). Cross-reference [signal → data crosswalk](#signal-data-map) for Phase III links.

## End-of-day tier

**Equity daily OHLCV** (`equity_daily_ohlcv`) — CRSP-style histories from the 1960s [[claim:CLM-2027-001]] underpin momentum, stat-arb baskets, and factor neutralization (SIG-001, SIG-003). Storage is negligible versus tick; viability is **high** across the full reconstruction window.

**Fundamentals quarterly** (`fundamentals_quarterly`) — Compustat-class fields [[claim:CLM-2027-012]] support slower overlays and NLP context, not sub-day alpha. Point-in-time correctness is a known pitfall.

**Corporate actions** (`corporate_actions`) — Low storage, **high** viability; bad adjustments destroy any price signal [[claim:CLM-2027-014]]. **Rates and bonds EOD** (`rates_bonds_eod`) and **macro futures curves** (`macro_futures_curve`) anchor regime and carry signals (SIG-005, SIG-015).

**Options EOD chains** (`options_chain_eod`) — Listed US options widely available by the 1990s [[claim:CLM-2027-004]] for volatility arbitrage, VRP, and dispersion (SIG-008–SIG-010).

## Intraday bar tier

**Equity intraday OHLC** (`equity_intraday_ohlc`) — Bridges daily research and full tick before 1993 tape consolidation [[claim:CLM-2027-002]]. Useful for short-horizon mean reversion (SIG-002) when tick storage was prohibitive.

**Volatility surfaces** (`volatility_surfaces`) — Fitted from options quotes; EOD/intraday mix from mid-1990s. **Options intraday quotes** (`options_intraday_quotes`) add cost and storage post-2005 for surface arbitrage at shorter horizons.

## Tick / trade tier

**Equity tick trades** (`equity_tick_trades`) — Consolidated US tape from ~1993 [[claim:CLM-2027-002]]; enables microstructure and order-flow research at scale. Pre-1993: fragmented feeds, higher E1 weight on RenTech engineering [[claim:CLM-2027-014]].

**Futures continuous** (`futures_continuous`) and **index/micro futures** (`index_futures_micro`) — Documentable from ~1980 [[claim:CLM-2027-006]]; diversification away from single-name equity stat-arb.

**FX spot tick** (`fx_spot_tick`) — G10 electronic history ~1990 [[claim:CLM-2027-005]]. **FX forwards/swaps** (`fx_forwards_swaps`) support cross-currency relative value.

## Limit order book (L2)

**Order book L2** (`order_book_l2`) — Commercial US equity depth feeds ~2000s [[claim:CLM-2027-003]]; powers SIG-007 and execution research (SIG-014). Storage and compute are an order of magnitude above tick trades alone.

## Supporting reference data

**Equity index constituents** (`equity_index_constituents`) — Rebalance and membership effects for basket stat-arb (SIG-001) and dispersion (SIG-010).

**Short interest / borrow** (`short_interest_borrow`) — 2000s maturity [[claim:CLM-2027-013]]; constrains crowded equity shorts in stat-arb.

## Latency summary

| Tier | Example rows | Typical signals |
|------|----------------|-----------------|
| EOD | equity_daily_ohlcv, options_chain_eod | SIG-001, SIG-003, SIG-009 |
| Intraday | equity_intraday_ohlc, volatility_surfaces | SIG-002, SIG-008 |
| Tick | equity_tick_trades, fx_spot_tick, futures_continuous | SIG-002, SIG-007 |
| L2 | order_book_l2 | SIG-007, SIG-014 |

SEC market-structure reforms increased transparency over the 1990s–2000s [[claim:CLM-2027-011]], improving research-grade quote and trade data for US equities.
