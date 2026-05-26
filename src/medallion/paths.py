from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
SCHEMAS_DIR = ROOT / "schemas"
RESEARCH_DIR = ROOT / "research"
EXPERIMENTS_DIR = ROOT / "experiments"

EVIDENCE_PATH = DATA_DIR / "evidence.yaml"
SIGNALS_PATH = DATA_DIR / "signals.yaml"
BIBLIOGRAPHY_PATH = DATA_DIR / "bibliography.yaml"
