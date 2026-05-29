# Infrastructure Timeline {#infrastructure-timeline}

Sources: [@zuckerman2019], [@patterson2010], [@wikipedia_renaissance_technologies]. See [disclaimer](../about.html).

This table mixes **industry-wide** developments (usable as context) with **Renaissance-specific** claims only where we have citations. Petabyte-scale language is **modern journalism**, not audited engineering disclosure [[claim:CLM-2026-017]] [[claim:CLM-2026-018]].

| Era | Compute (public sketch) | Data (public sketch) | Execution / connectivity | Renaissance-specific (cited) |
|-----|-------------------------|----------------------|----------------------------|------------------------------|
| 1978–1988 | Unix-era workstations; early clusters industry-wide | Futures/FX; improving futures histories; limited equity tick | Phone/broker-era latency; manual ops common | Long Island operations; scientist-led data accumulation [[claim:CLM-2026-001]] [[claim:CLM-2026-016]] |
| 1989–1993 | Same class as leading quant shops of the era | EOD equities widely available; tick tape emerging | Floor + electronic transition period | Post-drawdown **system rewrite** under Berlekamp cohort [[claim:CLM-2026-006]] |
| 1993–2005 | Industry moves toward Linux clusters, more RAM | Consolidated US equity tape (see Phase II `equity_tick_trades`); options chains EOD | Co-location arms race begins for equity HFT broadly | IBM hires bring speech/NLP compute culture [[claim:CLM-2024-006]]; **2005** outside-investor buyout [[claim:CLM-2026-008]] |
| 2006–2014 | GPU experiments industry-wide; larger farms | Order-book vendor feeds (`order_book_l2`); options surfaces | Sub-ms races at cutting edge | Modern profiles allege **petabyte-scale** warehouse—treat as **characterization** [[claim:CLM-2026-017]] |
| 2015+ | Cloud + GPU norm for ML industry | Alt-data explosion (Phase II: news, transcripts, AIS, etc.) | Smart order routers, internalization debates | Secrecy dominates; internal pipeline **unknown** [[claim:CLM-2026-018]] |

## Cross-links to Phase II (data availability)

Use the matrix for **earliest_year** discipline when inferring what signals were even *possible* in each era:

1. **Equity tick consolidated tape** — see `equity_tick_trades` (post-1993 mainstream narrative).
2. **L2 order books** — see `order_book_l2` (2000+ in matrix).
3. **Options chains EOD** — see `options_chain_eod` (1990+).

Full YAML: [data_availability_matrix.yaml](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml).

## Industry vs firm (wording discipline)

**Industry-wide:** co-location, consolidated tape, vendor market data, GPU clusters for ML research.

**Firm-specific (still mostly E2 journalism):** East Setauket campus as hub [[claim:CLM-2026-016]]; overhaul episode under Berlekamp [[claim:CLM-2026-006]]; IBM hire cultural impact [[claim:CLM-2024-006]].

**Hypothesis (E1):** proprietary cleaning + workflow + organizational secrecy compounded generic hardware [[claim:CLM-2026-019]].

## Regulatory footnote

Adviser registration and form history: [[claim:CLM-2026-020]] — useful for **legal existence** and reporting events, not for reverse-engineering models.

## Reading discipline

When infrastructure claims appear in podcasts or documentaries, they often **compress decades** of industry progress into a single “they had supercomputers” beat. This chapter instead ties each era to **observable market-data milestones** (Phase II) and labels **RenTech-internal** machinery as unknown unless a named source provides a checkable fact [[claim:CLM-2026-018]]. The result is less cinematic but more auditable: readers can see which advantages were **generic** (everyone got consolidated tape) versus **hypothesized** (proprietary cleaning stacks) [[claim:CLM-2026-019]].
