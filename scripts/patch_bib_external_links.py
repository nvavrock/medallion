#!/usr/bin/env python3
"""Patch rendered HTML: in-text biblioref links -> external URL for web sources."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "quarto" / "_site"
BROKEN_SLUG = "2019/05/13/elwyn-b-j-berlekamp"
BROKEN_URL = (
    "https://news.berkeley.edu/2019/05/13/"
    "elwyn-b-j-berlekamp-game-theorist-and-coding-pioneer-dies-at-78/"
)
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
BERKELEY_REF_EM_RE = re.compile(
    r'(<div id="ref-berkeley_news_berlekamp2019"[^>]*>[\s\S]*?)<em>([^<]+)</em>',
    re.IGNORECASE,
)


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
    stats = {
        "bibref_patched": 0,
        "broken_slug_replaced": 0,
        "berkeley_anchors_hardened": 0,
        "berkeley_title_linked": 0,
    }

    berkeley_url = url_map.get("berkeley_news_berlekamp2019", "")

    if BROKEN_SLUG in text:
        stats["broken_slug_replaced"] += text.count(BROKEN_SLUG)
        text = text.replace(BROKEN_SLUG, GOOD_SLUG)
    if BROKEN_URL in text and berkeley_url:
        stats["broken_slug_replaced"] += text.count(BROKEN_URL)
        text = text.replace(BROKEN_URL, berkeley_url)

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

    def link_title(m: re.Match[str]) -> str:
        prefix, title = m.group(1), m.group(2)
        if not berkeley_url or "<a href=" in prefix:
            return m.group(0)
        stats["berkeley_title_linked"] += 1
        return (
            f'{prefix}<a href="{berkeley_url}" target="_blank" rel="noopener noreferrer">'
            f"<em>{title}</em></a>"
        )

    text = BERKELEY_REF_EM_RE.sub(link_title, text, count=1)

    if text != original:
        path.write_text(text, encoding="utf-8")
    return stats


def main() -> int:
    if not SITE.is_dir():
        print(f"ERROR: {SITE} not found; run quarto render first.", flush=True)
        return 1

    url_map = load_url_map()

    totals = {
        "files": 0,
        "bibref_patched": 0,
        "broken_slug_replaced": 0,
        "berkeley_anchors_hardened": 0,
        "berkeley_title_linked": 0,
    }
    for hp in SITE.rglob("*.html"):
        stats = patch_file(hp, url_map)
        if (
            stats["bibref_patched"]
            or stats["broken_slug_replaced"]
            or stats["berkeley_anchors_hardened"]
            or stats["berkeley_title_linked"]
        ):
            totals["files"] += 1
            totals["bibref_patched"] += stats["bibref_patched"]
            totals["broken_slug_replaced"] += stats["broken_slug_replaced"]
            totals.setdefault("berkeley_anchors_hardened", 0)
            totals["berkeley_anchors_hardened"] += stats["berkeley_anchors_hardened"]
            totals["berkeley_title_linked"] += stats["berkeley_title_linked"]

    print(
        f"Patched {totals['bibref_patched']} biblioref link(s) in {totals['files']} file(s); "
        f"replaced {totals['broken_slug_replaced']} broken slug occurrence(s); "
        f"hardened {totals['berkeley_anchors_hardened']} Berkeley anchor(s); "
        f"linked {totals['berkeley_title_linked']} title(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
