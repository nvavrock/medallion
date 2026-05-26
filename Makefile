.PHONY: install test claim-audit reproduce experiments smoke

PYTHON ?= python3
VENV ?= .venv
PIP = $(VENV)/bin/pip
PY = $(VENV)/bin/python

install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -e ".[dev]"

test:
	$(PY) -m pytest tests/ -q

claim-audit:
	$(PY) scripts/claim_audit.py

smoke:
	$(PY) experiments/03_mean_reversion/run.py
	$(PY) experiments/04_almgren_chriss/run.py
	$(PY) experiments/05_vol_target_kelly/run.py
	$(PY) experiments/07_multi_signal/run.py

experiments: smoke

reproduce: install test claim-audit smoke
	@echo "Reproduce pipeline complete."
