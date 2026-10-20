#!/usr/bin/env python3
import json
from pathlib import Path

data = json.loads(Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json").read_text())
talks_root = "/Users/dabacon/Documents/talks deprecated used drive"

pdf_talks = []
for p in data["pdfs_candidates"]:
    path = p["path"]
    if path.startswith(talks_root):
        continue
    pl = path.lower()
    if any(
        skip in pl
        for skip in [
            "/figures/",
            ".graffle/",
            "/arxiv",
            "/books/",
            "/calibre",
            "/review/",
            "/academia/teaching/",
            "/financial/",
            "/homes/",
            "/papers/",
            "/shared papers/",
        ]
    ):
        continue
    info = p["pdf_info"]
    prod = info.get("producer_meta", "").lower()
    if "omnigraffle" in prod or "mathematica" in prod or "gnuplot" in prod:
        continue
    if info["is_slide_producer"] or info["is_beamer_size"] or (info["is_landscape"] and (info.get("max_page_count_hint") or 0) >= 2):
        pdf_talks.append(p)

print(f"Found {len(pdf_talks)} PDF candidates:")
for p in sorted(pdf_talks, key=lambda x: x["path"]):
    info = p["pdf_info"]
    print(
        f"  [{p['mtime_iso']}] pages~{str(info.get('max_page_count_hint')):4s} ({p['size']//1024:5d} KB) {info.get('width')}x{info.get('height')} prod={info.get('producer_meta','')[:35]!r} -> {p['path']}"
    )
