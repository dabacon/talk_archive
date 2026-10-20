#!/usr/bin/env python3
import json
from pathlib import Path

data = json.loads(Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json").read_text())
for folder in ["CSE 322 Fall 08", "370ppts", "Spring08", "Winter06"]:
    items = [p for p in data["pdfs_candidates"] if folder in p["path"]]
    print(f"=== {folder} ({len(items)} PDFs) ===")
    for p in sorted(items, key=lambda x: x["name"])[:20]:
        print(f"  {p['name']:40s}  {p['size']//1024:5d} KB  {p['pdf_info'].get('width')}x{p['pdf_info'].get('height')}  prod={p['pdf_info'].get('producer_meta','')[:30]!r}")
