# Manual QA checklist (20–40 min)

Run after `make qa` passes. For Gate E (full Quarto render), also run `make site` or `make qa-full`.

## 1. Synthesis overclaiming (~10 min)

- [ ] Read [research/phase_08_synthesis/synthesis.md](../research/phase_08_synthesis/synthesis.md)
- [ ] Read [research/phase_08_synthesis/experiment_integration.md](../research/phase_08_synthesis/experiment_integration.md)
- [ ] Sharpe and leverage stated as **bands** or hypothesis, not point facts
- [ ] Experiment table has “does not prove” column; toys labeled explicitly
- [ ] Win rate / hit rate **not** used as evidentiary metrics

## 2. Live or local site (~5 min)

- [ ] `make site` then open `quarto/_site/index.html`, **or** https://nvavrock.github.io/medallion/
- [ ] Corpus map links resolve
- [ ] Phase II anchors work (strategy / data chapters)

## 3. Evidence spot-check (~10–15 min)

```bash
make deps
.venv/bin/python scripts/sample_evidence.py --n 8 --seed 42
```

For each sampled `CLM-*`:

- [ ] `grep -r "[[claim:CLM-....]]" research/ quarto/` finds at least one cite (or note orphan policy)
- [ ] `evidence_level` matches prose tone (E1 → hypothesis language)
- [ ] `sources` keys exist in `data/bibliography.yaml`

## 4. CI / release (~2 min)

- [ ] GitHub Actions → **CI** green on latest `main` PR/push
- [ ] GitHub Actions → **Quarto Publish** green on `main`
- [ ] Optional: `gh run list -R nvavrock/medallion --workflow=quarto-publish.yml --limit 3`

## 5. Record findings

Write `docs/qa_reports/YYYY-MM-DD.md` with automated results, manual notes, and follow-ups.

See also [test_plan.md](test_plan.md) and [evidence_rubric.md](evidence_rubric.md).
