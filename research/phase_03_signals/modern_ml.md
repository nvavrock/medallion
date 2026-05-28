# Modern ML, NLP, and alt-data cluster {#modern-ml}

**Last updated:** 2026-05-28

Workstream **R3b** covers **SIG-011** through **SIG-014**, plus ensemble core **SIG-013**. IBM-era hires [[claim:CLM-2024-006]] support **integration scale** (E2), not public proof of a single architecture.

## Era feasibility

| Signal | Earliest era | Blocker |
|--------|--------------|---------|
| SIG-011 NLP news / earnings | 2010s production; wire archives 1995+ | Licenses; alpha decay |
| SIG-012 Satellite / shipping | 2005+ imagery; 2010+ AIS | Cost; false positives |
| SIG-013 Ensemble ML | 1993+ multi-modal (post Brown/Mercer) | Overfit; compute |
| SIG-014 RL execution | 2015+ industry; L2 ~2000+ | Simulator-to-real; RenTech E1 |

Alt-data rows require [data/manifest.yaml](https://github.com/nvavrock/medallion/blob/main/data/manifest.yaml) paths before any download experiment; stubs remain for FRED/yfinance placeholders.

## SIG-011 — NLP on news and earnings

**Theory:** Text features predict short-horizon drift. **Replication:** partial — public event-study and NLP asset-pricing papers show **small, decaying** effects; RenTech-specific lexicons and labels are not observable (E1).

**Data:** `news_wire_archives`, `text_corpora_financial`, `earnings_transcripts`, `sentiment_scores`. **Failure modes:** overfitting lexicons; vendor arms race.

## SIG-012 — Satellite and shipping alt data

**Theory:** Non-price data leads fundamental repricing. **Replication:** partial — vendor and academic alt-data surveys document **existence and pitfalls**; no trade-level Medallion replication.

**Data:** `satellite_imagery`, `shipping_ais`, `commodity_flows_freight`, `weather_gridded`. **Confidence:** 0.35 — high false-positive risk.

## SIG-013 — Ensemble ML (gradient boosting / neural nets)

**Theory:** Nonlinear feature interactions. **Evidence:** Mercer/Brown public accounts (E2). **Replication:** partial — industry-wide adoption; advantage hypothesis is **data hygiene and ensemble discipline**, not a unique architecture.

**Data:** crosses tick, daily, and text rows per [signal → data crosswalk](../chapters/02-data.html#signal-data-map). Pairs with SIG-001 and SIG-007 features in production-grade shops (inferred).

## SIG-014 — Reinforcement learning for execution

**Theory:** Adaptive execution reduces impact. **Replication:** partial — [EXP-04](https://github.com/nvavrock/medallion/tree/main/experiments/04_almgren_chriss) (EXP-04) bounds **static** optimal execution under impact; it is not RL but shows execution cannot be ignored.

RenTech use of RL is **E1 unconfirmed**. Feasibility improves with `order_book_l2` (SIG-007 era gate).

## Cluster conclusion

Modern ML signals are **industry-wide after ~2010**; Medallion’s edge hypothesis shifts to **earlier scale-up, secrecy, and integration** [[claim:CLM-2024-009]] rather than a single publicized model class. Do not treat NLP or satellite alpha as Medallion-specific without new sourced evidence.
