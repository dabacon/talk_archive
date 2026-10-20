#!/usr/bin/env python3
import json
from pathlib import Path

data = json.loads(Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json").read_text())

total_pres_bytes = 0
large_files = []
for p in data["presentations"]:
    pl = p["path"].lower()
    if "other peoples blabberings" in pl or "/downloads/" in pl or "/cloudstorage/" in pl:
        continue
    if any(x in pl for x in ["/gaetano/", "/hemingway/", "/cse326-wi06-slides/"]):
        continue
    total_pres_bytes += p["size"]
    if p["size"] > 25 * 1024 * 1024:
        large_files.append((p["size"], p["path"]))

print(f"Total presentation size in scope: {total_pres_bytes / (1024*1024):.1f} MB")
print("Files > 25 MB:")
for sz, path in sorted(large_files, reverse=True):
    print(f"  {sz/(1024*1024):6.1f} MB  {path}")
