# Era availability (1980s–2010s+)

**Last updated:** 2026-05-26

This document maps [data_availability_matrix.yaml](data_availability_matrix.yaml) rows to **industry-available** versus **plausible for Renaissance Technologies** eras, aligned with [Phase I strategy eras](../phase_01_history/strategy_evolution.md). Evidence anchors use `[[claim:CLM-...]]` from [data/evidence.yaml](../../data/evidence.yaml).

## 1980s — Monemetrics / early RenTech

**Industry-available:** US equity daily OHLCV from CRSP-style vendors [[claim:CLM-2027-001]]; continuous futures and Treasury EOD from major exchanges [[claim:CLM-2027-006]]; corporate actions at low frequency; gridded weather for commodity research; scheduled macro releases.

**Plausible for RenTech:** Berlekamp-era stat-arb on **daily** equities and futures is consistent with public narrative [[claim:CLM-2024-003]]. Tick-level US equity research at scale is **not** industry-standard until the consolidated tape transition [[claim:CLM-2027-002]]. We hypothesize manual bar construction and proprietary symbology were differentiators [[claim:CLM-2027-014]].

**Hypothesis only:** Order-book microstructure, NLP on news, and alt-data sleeves are absent or immature.

| Matrix row | Industry | RenTech plausibility |
|------------|----------|----------------------|
| equity_daily_ohlcv | Yes | High |
| futures_continuous | Yes | High |
| corporate_actions | Partial | High (quality E1) |
| equity_tick_trades | Fragmented | Low–medium (E1) |
| order_book_l2 | No | No |

## 1990s — Medallion scale-up, IBM hires

**Industry-available:** G10 FX electronic ticks by ~1990 [[claim:CLM-2027-005]]; listed options EOD chains [[claim:CLM-2027-004]]; consolidated equity tape ~1993 [[claim:CLM-2027-002]]; intraday OHLC bars; Compustat-style fundamentals [[claim:CLM-2027-012]]; digitized news wires mid-decade [[claim:CLM-2027-007]]; SEC transparency reforms accelerate quote data [[claim:CLM-2027-011]].

**Plausible for RenTech:** Mercer/Brown-era ensemble ML [[claim:CLM-2026-012]] sits atop expanding tick and options inputs. Volatility surfaces from mid-1990s support options sleeves (SIG-008, SIG-009). RenTech-specific cleaning pipelines remain **E1** [[claim:CLM-2027-014]].

**Hypothesis only:** Commercial L2 books (2000+), structured transcripts (2000+), satellite, AIS.

| Matrix row | Industry | RenTech plausibility |
|------------|----------|----------------------|
| equity_tick_trades | 1993+ | High post-tape |
| fx_spot_tick | 1990+ | High |
| options_chain_eod | 1990+ | High |
| news_wire_archives | 1995+ | Medium–high |
| order_book_l2 | ~2000 | Low until decade end |

## 2000s — Capacity, diversification, alt-data dawn

**Industry-available:** US equity L2 vendor feeds [[claim:CLM-2027-003]]; earnings transcripts as products [[claim:CLM-2027-008]]; financial text corpora [[claim:CLM-2027-017]]; satellite imagery category rises [[claim:CLM-2027-010]]; short interest datasets mature [[claim:CLM-2027-013]]; geopolitical structured feeds [[claim:CLM-2027-015]]; commodity/freight alt data [[claim:CLM-2027-016]].

**Plausible for RenTech:** Order-flow imbalance (SIG-007) and execution research become technically grounded. NLP features are plausible but **crowding and decay** accelerate after 2008 sentiment products. Public accounts still omit proprietary feed mix.

| Matrix row | Industry | RenTech plausibility |
|------------|----------|----------------------|
| order_book_l2 | Yes | High (E1 on depth) |
| earnings_transcripts | 2000+ | Medium |
| sentiment_scores | 2008+ | Medium |
| satellite_imagery | 2005+ | Speculative (E1) |

## 2010s+ — Alt-data arms race, crypto out of scope

**Industry-available:** AIS maritime tracking ~2010 [[claim:CLM-2027-009]]; options intraday quotes at scale; crypto spot markets (marked **not_applicable** for historical Medallion focus) [[claim:CLM-2027-018]]; reinforcement-learning execution research in industry (SIG-014) with uncertain RenTech confirmation.

**Plausible for RenTech:** Satellite/shipping alt data (SIG-012) and modern NLP (SIG-011) are **industry-wide**; attribution to Medallion remains E1–E2. Core short-horizon stat-arb likely still rests on price, futures, and FX microstructure with alt-data as diversifiers.

**Review Gate A:** Core traditional rows plus ≥6 alternative categories are present in the matrix; see [README.md](README.md) checklist.
