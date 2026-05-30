## Strategy Evolution Map {#strategy-evolution-map}

Sources: [@zuckerman2019], [@patterson2010], [@wikipedia_renaissance_technologies]. See [disclaimer](../about.html).

The diagram below is a **pedagogical** partition. Public sources emphasize **continuity** and overlapping sleeves rather than four clean handoffs [[claim:CLM-2024-002]].

```mermaid
flowchart LR
  A[Currencies_Futures_1978toLate1980s] --> B[Crisis_Overhaul_1989to1993]
  B --> C[StatArb_Equities_1993to2009]
  C --> D[Capacity_Secrecy_2005plus]
```

### Stage A — Currencies and futures (late 1970s–late 1980s)

**Instruments (public):** Currencies first under Monemetrics [[claim:CLM-2026-001]]; Baum/Ax lineage extended models toward **commodity futures** more broadly [[claim:CLM-2026-011]]. **Holding period:** public sources rarely give clean half-lives for this era; we do not invent numbers.

**Data available then (cross-check Chapter II):** Daily futures and FX existed; consolidated **equity tick** tape and modern **L2 order books** were **not** broadly available at today’s granularity until later decades. See [data_availability_matrix.yaml](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml) rows `futures_continuous`, `fx_spot_tick`, `equity_tick_trades`, `order_book_l2`.

**Narrative:** Simons accumulated price data and iterated on models while recruiting mathematicians rather than traditional traders [[claim:CLM-2026-003]] [[claim:CLM-2024-009]].

### Stage B — Crisis, overhaul, employee-only pivot (1989–1993)

**Instruments:** Still futures/currency-heavy in public accounts, but Medallion’s **system rewrite** under Berlekamp is the hinge [[claim:CLM-2026-005]] [[claim:CLM-2026-006]]. **Laufer** and **Straus** appear in overhaul timelines [[claim:CLM-2026-015]] [[claim:CLM-2026-009]].

**Data:** Same as Stage A, plus improving equity **EOD** coverage (Chapter II row `equity_daily_ohlcv`).

**Narrative:** The drawdown and Ax departure forced a discipline shift toward short-horizon statistical pattern recognition in journalistic accounts (not a verifiable code dump) [[claim:CLM-2026-006]]. **1993** closes the fund to outsiders—structurally changes incentive and capacity [[claim:CLM-2026-007]].

### Stage C — Statistical equities, IBM speech talent, Simons CEO era (1993–2009)

**Instruments:** Public narrative: broader **equities** and cross-sectional statistical effects alongside legacy futures work [[claim:CLM-2024-002]]. **IBM hires 1993** brought speech/NLP-style computational talent that later maps to “ML at scale” stories [[claim:CLM-2024-006]] [@patterson2010].

**Data:** **Options chains EOD** and richer **equity** datasets become industry-standard through the 1990s–2000s (Chapter II rows `options_chain_eod`, `equity_tick_trades` with post-1993 tick consolidation caveat).

**Narrative:** Patterson influences hiring and culture [[claim:CLM-2026-014]]. Performance **bands** remain contested [[claim:CLM-2024-003]]; we do not anchor strategy claims to unverified Sharpe point estimates.

### Stage D — Capacity, secrecy, outsider buyout (2005 onward)

**Instruments:** Publicly under-specified mix; options/vol sleeves are **plausible** but thinly sourced [[claim:CLM-2024-008]].

**Data:** **Alt data** and **NLP** become industry-wide post-2010 (Chapter II rows `news_wire_archives`, `sentiment_scores`, `satellite_imagery` with later `earliest_year`).

**Narrative:** Last outside investor bought out in **2005** [[claim:CLM-2026-008]]. Secrecy and NDAs limit what can be said about current sleeves [[claim:CLM-2026-018]]. **Hypothesis:** edge combined industry inputs with proprietary cleaning and workflow—not a single visible “secret model” [[claim:CLM-2026-019]].

### Counter-narrative: blending vs stages

Discrete stages help readers; the evidence supports **overlapping** evolution more than sharp boundaries [[claim:CLM-2024-002]]. Chapter III will formalize **signal hypotheses** (SIG-001 onward) rather than repeating performance folklore here.

### Forward link

Detailed **dataset-era feasibility** lives in [Chapter II — Data](../chapters/02-data.html) and the [availability matrix YAML](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml).

### Bridge to later phases (scope control)

Chapter I intentionally **does not** estimate Sharpe, alpha, or capacity numbers beyond what is already isolated in evidence records [[claim:CLM-2024-003]] [[claim:CLM-2024-004]]. **Chapter III** will map candidate **signal classes** to eras; **Chapter VII** will run toy **replications** whose parameters must cite rows from the Chapter II matrix (e.g., do not attribute 2005-era alt-data signals to 1988 without an explicit **counterfactual** label). When you extend this chapter, add new `CLM-*` rows **before** inserting additional table rows so `make claim-audit` stays green.

**Peer context:** Patterson’s industry-wide account of IBM speech hires and quant culture helps interpret **Mercer/Brown** as part of a broader **speech→finance** talent pipeline—not a uniquely RenTech invention [[claim:CLM-2024-006]] [@patterson2010]. That framing reduces **survivorship** exaggeration when reading Medallion-only lore.

**Regulatory:** For adviser existence and form timelines, prefer **IAPD** pulls over forum posts [[claim:CLM-2026-020]]. Filings will not validate performance but can anchor **registration dates** when cross-checking journalism.

**What readers should not conclude:** That a clean four-stage diagram implies four internal reorganizations; that **petabyte** language implies a verified warehouse size; or that **1990 return** figures are SEC-audited—they remain **fund-letter / secondary** chains in public discourse [[claim:CLM-2026-006]] [[claim:CLM-2026-017]].
