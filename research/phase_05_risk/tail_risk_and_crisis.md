## Tail risk and crisis behavior {#tail-risk-and-crisis}

**Last updated:** 2026-05-28

### Layer 6 — Tail risk

**Function:** Limit drawdowns and correlation breakdown damage during crises.

### Contrasts with failed peers

LTCM illustrates concentration and leverage in relative-value structures [[claim:CLM-2024-010]]. Medallion’s shorter horizons (inferred), diversification, and capacity caps (employee-only fund [[claim:CLM-2026-007]]) differ — **survivorship bias** cautions against winner-only comparisons.

### Plausible mechanisms (E1–E2 mix)

- Active de-grossing when correlation spikes
- Volatility scaling down automatically
- Options/vol sleeves (SIG-008–010) with gap risk — under-sourced for RenTech [[claim:CLM-2024-008]]

### Options tail lessons

Variance risk premium harvesting earns carry until vol spikes (2008, 2020). Any vol sleeve must be sized within tail constraints (SIG-009 failure modes).

### What we cannot verify

Crisis PnL paths, prime-broker terms, and internal stress models are not public [[claim:CLM-2026-018]].
