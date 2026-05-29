#!/usr/bin/env python3
"""Patch rendered HTML: in-text biblioref links -> external URL for web sources."""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "quarto" / "_site"
LOG_PATH = ROOT / ".cursor" / "debug-49b21d.log"
SESSION_ID = "49b21d"
BROKEN_SLUG = "2019/05/13/elwyn-b-j-berlekamp"
GOOD_SLUG = "2019/04/18/elwyn-berlekamp"
BIBREF_RE = re.compile(
    r'(<a href="#ref-([a-zA-Z0-9_]+)" role="doc-biblioref">)',
    re.IGNORECASE,
)
# Footnote URL links from citeproc (no rel=) — add noreferrer so Berkeley/Cloudflare does not block github.io referer
BERKELEY_ANCHOR_RE = re.compile(
    r'<a href="(https://news\.berkeley\.edu[^"]+)"(?![^>]*\brel=)([^>]*)>',
    re.IGNORECASE,
)


def _log(hypothesis_id: str, location: str, message: str, data: dict, run_id: str = "patch") -> None:
    # #region agent log
    payload = {
        "sessionId": SESSION_ID,
        "runId": run_id,
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data,
        "timestamp": int(time.time() * 1000),
    }
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")
    # #endregion


def load_url_map() -> dict[str, str]:
    raw = yaml.safe_load((ROOT / "data" / "bibliography.yaml").read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for key, src in raw.get("sources", {}).items():
        url = src.get("url")
        if url:
            out[key] = url
    return out


def patch_file(path: Path, url_map: dict[str, str]) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    original = text
    stats = {"bibref_patched": 0, "broken_slug_replaced": 0, "berkeley_anchors_hardened": 0}

    if BROKEN_SLUG in text:
        text = text.replace(BROKEN_SLUG, GOOD_SLUG)
        stats["broken_slug_replaced"] = original.count(BROKEN_SLUG)

    def repl(m: re.Match[str]) -> str:
        key = m.group(2)
        url = url_map.get(key)
        if not url:
            return m.group(1)
        stats["bibref_patched"] += 1
        return f'<a href="{url}" role="doc-biblioref" target="_blank" rel="noopener noreferrer">'

    text = BIBREF_RE.sub(repl, text)

    def harden_berkeley(m: re.Match[str]) -> str:
        stats["berkeley_anchors_hardened"] += 1
        url, rest = m.group(1), m.group(2)
        if "target=" in rest:
            return f'<a href="{url}"{rest}>'
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer"{rest}>'

    text = BERKELEY_ANCHOR_RE.sub(harden_berkeley, text)

    if text != original:
        path.write_text(text, encoding="utf-8")
    return stats


def main() -> int:
    if not SITE.is_dir():
        print(f"ERROR: {SITE} not found; run quarto render first.", flush=True)
        return 1

    url_map = load_url_map()
    _log("H3", "patch_bib_external_links.py:start", "URL map loaded", {"keys_with_url": list(url_map.keys())})

    totals = {"files": 0, "bibref_patched": 0, "broken_slug_replaced": 0, "berkeley_anchors_hardened": 0}
    for hp in SITE.rglob("*.html"):
        stats = patch_file(hp, url_map)
        if stats["bibref_patched"] or stats["broken_slug_replaced"] or stats["berkeley_anchors_hardened"]:
            totals["files"] += 1
            totals["bibref_patched"] += stats["bibref_patched"]
            totals["broken_slug_replaced"] += stats["broken_slug_replaced"]
            totals.setdefault("berkeley_anchors_hardened", 0)
            totals["berkeley_anchors_hardened"] += stats["berkeley_anchors_hardened"]
            _log(
                "H3",
                "patch_bib_external_links.py:file",
                "Patched HTML file",
                {"file": str(hp.relative_to(ROOT)), **stats},
            )

    _log("H3", "patch_bib_external_links.py:done", "Patch complete", totals)
    print(
        f"Patched {totals['bibref_patched']} biblioref link(s) in {totals['files']} file(s); "
        f"replaced {totals['broken_slug_replaced']} broken slug occurrence(s); "
        f"hardened {totals['berkeley_anchors_hardened']} Berkeley anchor(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
