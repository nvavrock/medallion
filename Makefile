.PHONY: install venv deps test claim-audit reproduce experiments smoke clean

PYTHON ?= python3
VENV ?= .venv
PY = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
UV ?= $(shell command -v uv 2>/dev/null)

# Create .venv if missing (uv works without apt python3-venv; falls back to python3 -m venv)
venv:
ifeq ($(UV),)
	@test -x $(PY) || ( $(PYTHON) -m venv $(VENV) || { \
		echo ""; \
		echo "ERROR: python3-venv is not installed."; \
		echo "  sudo apt install python3-venv   # or: python3.14-venv"; \
		echo "Or install uv: https://docs.astral.sh/uv/"; \
		exit 1; \
	} )
else
	@test -x $(PY) || $(UV) venv $(VENV)
endif

deps: venv
ifeq ($(UV),)
	$(PIP) install -e ".[dev]"
else
	$(UV) pip install -e ".[dev]" --python $(PY)
endif

install: deps

test: deps
	$(PY) -m pytest tests/ -q

claim-audit: deps
	$(PY) scripts/claim_audit.py

smoke: deps
	$(PY) experiments/03_mean_reversion/run.py
	$(PY) experiments/04_almgren_chriss/run.py
	$(PY) experiments/05_vol_target_kelly/run.py
	$(PY) experiments/07_multi_signal/run.py

experiments: smoke

reproduce: deps test claim-audit smoke
	@echo "Reproduce pipeline complete."

clean:
	rm -rf $(VENV)
