#!/usr/bin/env python3
"""Verify bibliography URLs in source YAML and rendered site HTML."""

from __future__ import annotations

import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BROKEN_BERKELEY = "2019/05/13/elwyn-b-j-berlekamp"
GOOD_BERKELEY = "2019/04/18/elwyn-berlekamp"


def _http_status_get(url: str) -> int | str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; medallion-verify/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)


def main() -> int:
    import yaml

    bib_path = ROOT / "data" / "bibliography.yaml"
    sources = yaml.safe_load(bib_path.read_text(encoding="utf-8")).get("sources", {})
    errors: list[str] = []

    berkeley = sources.get("berkeley_news_berlekamp2019", {})
    berkeley_url = berkeley.get("url", "")
    if BROKEN_BERKELEY in berkeley_url:
        errors.append(f"YAML still has broken Berkeley URL: {berkeley_url}")
    if GOOD_BERKELEY not in berkeley_url:
        errors.append(f"YAML missing expected Berkeley slug: {berkeley_url}")

    bib_file = ROOT / "quarto" / "references.bib"
    if bib_file.exists() and BROKEN_BERKELEY in bib_file.read_text(encoding="utf-8"):
        errors.append("references.bib still contains broken Berkeley slug")

    site = ROOT / "quarto" / "_site"
    if site.is_dir():
        broken_hits = [
            str(hp.relative_to(ROOT))
            for hp in site.rglob("*.html")
            if BROKEN_BERKELEY in hp.read_text(encoding="utf-8", errors="ignore")
        ]
        if broken_hits:
            errors.append(f"Broken Berkeley URL in local HTML: {broken_hits}")

    live_pages = {
        "bibliography": "https://nvavrock.github.io/medallion/appendices/bibliography.html",
        "history": "https://nvavrock.github.io/medallion/chapters/01-history.html",
    }
    for label, live_url in live_pages.items():
        try:
            with urllib.request.urlopen(
                urllib.request.Request(live_url, headers={"User-Agent": "medallion-verify/1.0"}),
                timeout=20,
            ) as resp:
                live_html = resp.read().decode("utf-8", errors="ignore")
            if BROKEN_BERKELEY in live_html:
                errors.append(f"Live {label} still has broken Berkeley URL")
            if label == "history":
                if 'href="#ref-berkeley_news_berlekamp2019"' in live_html:
                    errors.append("Live history chapter still uses internal #ref-berkeley biblioref")
                if "news.berkeley.edu/2019/04/18/elwyn-berlekamp" not in live_html:
                    errors.append("Live history chapter missing external Berkeley biblioref link")
        except Exception as e:
            errors.append(f"Could not fetch live {label}: {e}")

    if berkeley_url and _http_status_get(berkeley_url) != 200:
        errors.append(f"Berkeley URL GET returned non-200: {berkeley_url}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("Bibliography URL verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
