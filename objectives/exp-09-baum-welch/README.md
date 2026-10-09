# Primary objective — EXP-09 Baum–Welch lineage toy

**Status:** active. This folder is the current primary objective for the Medallion repo. Other work waits until the checklist is done.

**Plan:** [Baum–Welch experiment (EXP-09)](PLAN.md). Finish criteria live in [CHECKLIST.md](CHECKLIST.md).

Start here next session: open [PLAN.md](PLAN.md), then work [CHECKLIST.md](CHECKLIST.md) from the top.

## What this objective is

Medallion (1988) “builds on Baum/Ax model lineage” ([[claim:CLM-2026-004]]). The public build, from claims already in the corpus, is:

- **Baum:** statistical currency models; Baum–Welch is his HMM algorithm. He later left pure systematic modeling ([[claim:CLM-2026-010]]).
- **Ax:** kept the systematic book and widened it from currencies to commodity futures. He left after the 1989 drawdown ([[claim:CLM-2026-011]], [[claim:CLM-2026-005]]).
- **The build on that lineage** is not a bigger HMM. Berlekamp, Straus, and Laufer replaced a concentrated model book with short-horizon statistical bets ([[claim:CLM-2026-006]]).
- **Mercer/Brown** are a later IBM-speech HMM culture ([[claim:CLM-2024-006]]). They stay out of this toy.

[experiments/08_regime_filter](../../experiments/08_regime_filter) is a rolling-vol gate. Its contract says “Not HMM estimation.” [SIG-005](../../data/signals.yaml) is still E1 and dated “1990s–present,” which skips the 1978–1989 book this experiment is about.

No public source gives state count, emissions, or holding period. The executable will not invent those as RenTech facts.

## Done means

`make test` and `make smoke` pass, and `make quarto-check` passes if Quarto is on `PATH`. No version bump and no git tag.
