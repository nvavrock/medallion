# Microstructure models — deep dive {#models-deep-dive}

**Last updated:** 2026-05-28

## Almgren–Chriss (optimal execution)

Temporary and permanent impact trade off urgency versus price drift. Participation rate enters both impact terms in our toy [EXP-04](https://github.com/nvavrock/medallion/tree/main/experiments/04_almgren_chriss). **Limit:** calibrated impact parameters for RenTech are unknown; public reconstruction cannot assert desk-level optimality.

## Kyle (1985) — informed trading

Market depth and adverse selection: informed flow moves prices against liquidity providers. Relevant to **order-flow** signals (SIG-007) when holding periods are short. **Limit:** does not by itself generate diversifying alpha across thousands of instruments.

## Hasbrouck — price discovery

Variance decomposition and information shares link trades/quotes to efficient price. Supports measuring **execution quality** and short-horizon signal decay. **Limit:** requires tick/L2 history (era-gated post-1993/2000 per Chapter II).

## Propagator and inventory models

Propagator models represent transient impact from past order flow; inventory models explain market-maker quoting around target inventory. Together they motivate why **execution is a control layer**, not a standalone Sharpe engine [[claim:CLM-2024-007]].

## Era and data gates

Microstructure-heavy mechanisms need `equity_tick_trades` and often `order_book_l2` [[claim:CLM-2027-002]] [[claim:CLM-2027-003]]. Pre-1993 equity microstructure at Medallion scale is **E1** engineering hypothesis [[claim:CLM-2027-014]].
