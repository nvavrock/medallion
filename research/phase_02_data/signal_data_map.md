# Signal → data crosswalk {#signal-data-map}

**Last updated:** 2026-05-26

Maps each Phase III signal (`SIG-001` … `SIG-015` in [data/signals.yaml](https://github.com/nvavrock/medallion/blob/main/data/signals.yaml)) to required [matrix](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml) rows, earliest plausible Medallion era, and blockers. Use before Phase VII experiments.

| Signal | Required matrix rows | Earliest Medallion era | Blockers |
|--------|----------------------|------------------------|----------|
| SIG-001 Stat-arb baskets | equity_daily_ohlcv, corporate_actions, equity_index_constituents, short_interest_borrow | 1988+ daily; 2003+ short data | Borrow costs; crowding |
| SIG-002 Short-horizon mean reversion | equity_tick_trades, equity_intraday_ohlc, fx_spot_tick, order_book_l2 | 1993+ tick; 2000+ L2 | Transaction costs; capacity |
| SIG-003 Momentum | equity_daily_ohlcv, futures_continuous, fx_spot_tick, economic_releases | 1988+ | Crowding in equities |
| SIG-004 Cointegration / pairs | equity_daily_ohlcv, futures_continuous, fx_forwards_swaps | 1988+ | Structural breaks |
| SIG-005 HMM / regime | equity_daily_ohlcv, rates_bonds_eod, macro_futures_curve, geopolitical_events_structured | 1988+; 2002+ geo | Overfitting; meta-signal |
| SIG-006 Kalman / state-space | equity_daily_ohlcv, equity_tick_trades | 1990+ | Model risk |
| SIG-007 Order-flow imbalance | equity_tick_trades, order_book_l2 | 1993+ tick; 2000+ L2 | Adverse selection; HFT scale |
| SIG-008 Vol surface arb | options_chain_eod, volatility_surfaces, options_intraday_quotes | 1995+ | Gap risk; depth |
| SIG-009 Variance risk premium | options_chain_eod, volatility_surfaces | 1995+ | Tail events |
| SIG-010 Dispersion / correlation | options_chain_eod, volatility_surfaces, equity_index_constituents | 2000+ | Crisis correlation breakdown |
| SIG-011 NLP news / earnings | news_wire_archives, text_corpora_financial, earnings_transcripts, sentiment_scores | 1995+ wire; 2000+ transcripts | License; alpha decay |
| SIG-012 Satellite / shipping alt | satellite_imagery, shipping_ais, commodity_flows_freight, weather_gridded | 2005+ sat; 2010+ AIS | Cost; false positives |
| SIG-013 Ensemble ML | equity_tick_trades, equity_daily_ohlcv, text_corpora_financial, sentiment_scores | 1993+ multi-modal | Overfit; compute |
| SIG-014 RL execution | order_book_l2, equity_tick_trades | 2000+ | Simulator-to-real; E1 at RenTech |
| SIG-015 Kelly sizing | equity_daily_ohlcv, rates_bonds_eod (risk inputs) | 1988+ | Estimation error |

## Row → signal index

| Matrix row | Linked signals |
|------------|----------------|
| equity_tick_trades | SIG-002, SIG-007 |
| equity_daily_ohlcv | SIG-001, SIG-003, SIG-004 |
| equity_intraday_ohlc | SIG-002, SIG-003 |
| futures_continuous | SIG-003, SIG-004 |
| index_futures_micro | SIG-001, SIG-010 |
| fx_spot_tick | SIG-002, SIG-003 |
| fx_forwards_swaps | SIG-004 |
| order_book_l2 | SIG-007, SIG-014 |
| options_chain_eod | SIG-008, SIG-009, SIG-010 |
| options_intraday_quotes | SIG-008 |
| volatility_surfaces | SIG-008, SIG-009 |
| corporate_actions | SIG-001, SIG-013 |
| fundamentals_quarterly | SIG-001, SIG-011 |
| short_interest_borrow | SIG-001 |
| rates_bonds_eod | SIG-005, SIG-015 |
| weather_gridded | SIG-012 |
| satellite_imagery | SIG-012 |
| news_wire_archives | SIG-011 |
| text_corpora_financial | SIG-011, SIG-013 |
| earnings_transcripts | SIG-011 |
| economic_releases | SIG-003, SIG-005 |
| shipping_ais | SIG-012 |
| sentiment_scores | SIG-011, SIG-013 |
| geopolitical_events_structured | SIG-005 |
| commodity_flows_freight | SIG-012 |
| crypto_spot | — |
| equity_index_constituents | SIG-001, SIG-010 |
| macro_futures_curve | SIG-003, SIG-005 |

Tape consolidation [[claim:CLM-2027-002]] and L2 vendor eras [[claim:CLM-2027-003]] are the main **era gates** for microstructure signals. Alt-data rows require manifest paths before Phase VII download (see [data/manifest.yaml](https://github.com/nvavrock/medallion/blob/main/data/manifest.yaml)).
