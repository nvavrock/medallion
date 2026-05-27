# Alternative data

**Last updated:** 2026-05-26

Weather, shipping, satellite, news/NLP, macro releases, geopolitical events, and commodity flows—emphasizing **cost**, **latency**, and **alpha half-life** versus Phase III signals (especially SIG-011 and SIG-012).

## Cost and compute profile

| Row | Cost | Compute | Latency | Viability |
|-----|------|---------|---------|-----------|
| economic_releases | low | desktop | scheduled | medium |
| weather_gridded | low | desktop | daily | medium |
| news_wire_archives | high | cluster | minutes | high |
| text_corpora_financial | high | nlp_pipeline | hours | high |
| earnings_transcripts | medium | nlp_pipeline | event | high |
| sentiment_scores | medium | nlp | daily | medium |
| satellite_imagery | very_high | gpu_cluster | days | medium |
| shipping_ais | high | cluster | hours | medium |
| commodity_flows_freight | high | cluster | daily | medium |
| geopolitical_events_structured | high | desktop | hours | medium |
| crypto_spot | low | workstation | ms | not_applicable |

Alt-data is **not** RenTech-specific; industry surveys document adoption curves [[claim:CLM-2027-007]]–[[claim:CLM-2027-010]], [[claim:CLM-2027-015]]–[[claim:CLM-2027-017]].

## Text and NLP (SIG-011, SIG-013)

**News wire archives** — Mid-1990s commercial digitization [[claim:CLM-2027-007]]. Minutes-level latency was competitive before social media shortened half-lives.

**Text corpora financial** — Filings, news, and transcripts in unified corpora [[claim:CLM-2027-017]]; enables ensemble ML (SIG-013) beyond lexicon methods.

**Earnings transcripts** — Structured vendor products ~2000 [[claim:CLM-2027-008]]; event-driven drift decays as NLP commoditizes.

**Sentiment scores** — Vendor indices from ~2008; feature inputs with **months** half-life in [signals.yaml](../../data/signals.yaml), not standalone HFT alpha.

## Physical and flow alt-data (SIG-012)

**Satellite imagery** — Mid-2000s commercial category [[claim:CLM-2027-010]]; storage in terabytes/year; alpha at **quarterly** horizons, capacity-limited.

**Shipping AIS** — ~2010 commercial viability [[claim:CLM-2027-009]]; hours latency; complements freight and trade indices.

**Commodity flows / freight** (`commodity_flows_freight`) — Post-2000 payment and shipping datasets [[claim:CLM-2027-016]]; government trade stats exist earlier at lower frequency.

**Weather gridded** — Long history; ties to energy/ag futures more than equity microstructure.

## Macro and geopolitical

**Economic releases** — Low cost; scheduled timestamps matter for futures/FX (SIG-003, SIG-005).

**Geopolitical events structured** — Primarily 2000s+ vendor feeds [[claim:CLM-2027-015]]; sparse for equity tick strategies, more relevant to macro sleeves.

## Crypto (out of scope)

**Crypto spot** — Marked `not_applicable` for historical Medallion reconstruction [[claim:CLM-2027-018]]; included for matrix completeness only.

## Alpha half-life vs data latency

Alt-data with **days-to-quarters** latency (satellite, AIS, freight) cannot support SIG-002/SIG-007 microstructure horizons. NLP at **minutes-to-daily** can overlap SIG-011 but faces crowding. Phase VII experiments using these rows must document license and era constraints in [data/manifest.yaml](../../data/manifest.yaml).
