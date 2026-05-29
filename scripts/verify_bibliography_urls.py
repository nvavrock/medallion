#!/usr/bin/env python3
"""Verify bibliography URLs in source YAML and rendered site HTML."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / ".cursor" / "debug-49b21d.log"
SESSION_ID = "49b21d"
BROKEN_BERKELEY = "2019/05/13/elwyn-b-j-berlekamp"
GOOD_BERKELEY = "2019/04/18/elwyn-berlekamp"


def _log(hypothesis_id: str, location: str, message: str, data: dict, run_id: str = "verify") -> None:
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


def _http_status(url: str) -> int | str:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "medallion-verify/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)


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
    _log(
        "H4",
        "verify_bibliography_urls.py:yaml",
        "YAML berkeley_news URL",
        {"url": berkeley_url, "has_broken_slug": BROKEN_BERKELEY in berkeley_url},
    )
    if BROKEN_BERKELEY in berkeley_url:
        errors.append(f"YAML still has broken Berkeley URL: {berkeley_url}")
    if GOOD_BERKELEY not in berkeley_url:
        errors.append(f"YAML missing expected Berkeley slug: {berkeley_url}")

    bib_file = ROOT / "quarto" / "references.bib"
    if bib_file.exists():
        bib_text = bib_file.read_text(encoding="utf-8")
        m = re.search(r"berkeley_news_berlekamp2019[\s\S]*?url = \{([^}]+)\}", bib_text)
        emitted = m.group(1) if m else ""
        _log(
            "H4",
            "verify_bibliography_urls.py:bib",
            "references.bib emitted URL",
            {"url": emitted, "has_broken_slug": BROKEN_BERKELEY in emitted},
        )
        if BROKEN_BERKELEY in bib_text:
            errors.append("references.bib still contains broken Berkeley slug")

    site = ROOT / "quarto" / "_site"
    html_files = list(site.rglob("*.html")) if site.is_dir() else []
    broken_hits: list[str] = []
    good_hits = 0
    for hp in html_files:
        text = hp.read_text(encoding="utf-8", errors="ignore")
        if BROKEN_BERKELEY in text:
            broken_hits.append(str(hp.relative_to(ROOT)))
        if GOOD_BERKELEY in text:
            good_hits += 1
    _log(
        "H2",
        "verify_bibliography_urls.py:site",
        "Local _site HTML scan",
        {
            "html_count": len(html_files),
            "broken_files": broken_hits,
            "files_with_good_slug": good_hits,
        },
    )
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
            live_broken = BROKEN_BERKELEY in live_html
            live_good = GOOD_BERKELEY in live_html
            internal_berkeley = 'href="#ref-berkeley_news_berlekamp2019"' in live_html
            external_berkeley = (
                "news.berkeley.edu/2019/04/18/elwyn-berlekamp" in live_html
                and 'role="doc-biblioref"' in live_html
            )
            _log(
                "H5",
                "verify_bibliography_urls.py:live",
                f"Live GitHub Pages {label}",
                {
                    "url": live_url,
                    "has_broken_slug": live_broken,
                    "has_good_slug": live_good,
                    "internal_berkeley_biblioref": internal_berkeley,
                    "external_berkeley_biblioref": external_berkeley,
                },
                run_id="post-fix",
            )
            if live_broken:
                errors.append(f"Live {label} still has broken Berkeley URL")
            if label == "history" and internal_berkeley:
                errors.append("Live history chapter still uses internal #ref-berkeley biblioref")
            if label == "history" and not external_berkeley:
                errors.append("Live history chapter missing external Berkeley biblioref link")
        except Exception as e:
            _log("H5", "verify_bibliography_urls.py:live", f"Live fetch failed ({label})", {"error": str(e)}, run_id="post-fix")
            errors.append(f"Could not fetch live {label}: {e}")

    if berkeley_url:
        head_status = _http_status(berkeley_url)
        get_status = _http_status_get(berkeley_url)
        _log(
            "H8",
            "verify_bibliography_urls.py:http",
            "Berkeley URL reachability",
            {"url": berkeley_url, "head_status": head_status, "get_status": get_status},
            run_id="post-fix",
        )
        if get_status != 200:
            errors.append(f"Berkeley URL GET returned {get_status}: {berkeley_url}")

    if errors:
        _log("ALL", "verify_bibliography_urls.py:exit", "Verification failed", {"errors": errors})
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    _log("ALL", "verify_bibliography_urls.py:exit", "Verification passed", {})
    print("Bibliography URL verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
