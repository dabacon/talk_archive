#!/usr/bin/env python3
import json
from pathlib import Path

data = json.loads(Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json").read_text())
print("permission_errors_count:", data.get("permission_errors_count"))

for key in ["presentations", "pdfs_candidates", "ps_files", "tex_slides", "media_candidates"]:
    items = [x for x in data[key] if "Talks" in x["path"] or "talks" in x["path"]]
    print(f"{key} with Talks/talks: {len(items)}")
    by_top = {}
    for x in items:
        parts = x["path"].split("/")
        top = "/".join(parts[:6])
        by_top[top] = by_top.get(top, 0) + 1
    for k, v in sorted(by_top.items()):
        print(f"   {v:4d}  {k}")
