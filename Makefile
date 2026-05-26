.PHONY: install venv deps test claim-audit reproduce experiments smoke clean
.PHONY: quarto-assets quarto-check site preview

PYTHON ?= python3
VENV ?= .venv
PY = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
UV ?= $(shell command -v uv 2>/dev/null)
# Prefer PATH; fall back to user-local install (common on WSL)
QUARTO ?= $(shell \
	command -v quarto 2>/dev/null || \
	{ test -x "$$HOME/.local/quarto/bin/quarto" && echo "$$HOME/.local/quarto/bin/quarto"; })

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

quarto-assets: deps
	$(PY) scripts/build_quarto_assets.py

quarto-check: quarto-assets claim-audit

smoke: deps
	$(PY) experiments/03_mean_reversion/run.py
	$(PY) experiments/04_almgren_chriss/run.py
	$(PY) experiments/05_vol_target_kelly/run.py
	$(PY) experiments/07_multi_signal/run.py

experiments: smoke

reproduce: deps test claim-audit smoke
	@echo "Reproduce pipeline complete."

site: quarto-check smoke
	@test -n "$(QUARTO)" && test -x "$(QUARTO)" || { \
		echo "ERROR: Quarto CLI not found."; \
		echo "  Install: https://quarto.org/docs/get-started/"; \
		echo "  Or add to PATH: export PATH=\"$$HOME/.local/quarto/bin:$$PATH\""; \
		exit 1; \
	}
	cd quarto && "$(QUARTO)" render

preview: quarto-check smoke
	@test -n "$(QUARTO)" && test -x "$(QUARTO)" || { \
		echo "ERROR: Quarto CLI not found."; \
		echo "  Install: https://quarto.org/docs/get-started/"; \
		echo "  Or add to PATH: export PATH=\"$$HOME/.local/quarto/bin:$$PATH\""; \
		exit 1; \
	}
	cd quarto && "$(QUARTO)" preview

clean:
	rm -rf $(VENV) quarto/_site quarto/.quarto
	rm -f quarto/references.bib
	rm -f quarto/filters/claims-map.json
	rm -f quarto/appendices/_generated-*.md
