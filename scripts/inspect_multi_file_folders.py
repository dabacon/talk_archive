#!/usr/bin/env python3
import json
import os
from collections import defaultdict
from pathlib import Path

data = json.loads(Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json").read_text())

by_dir = defaultdict(list)
for p in data["presentations"]:
    pl = p["path"].lower()
    if "other peoples blabberings" in pl or "/downloads/" in pl or "/cloudstorage/" in pl:
        continue
    if any(x in pl for x in ["/gaetano/", "/hemingway/", "/cse326-wi06-slides/"]):
        continue
    by_dir[os.path.dirname(p["path"])].append(p)

for d, items in sorted(by_dir.items()):
    if len(items) > 1:
        print(f"\n=== {d} ({len(items)} files) ===")
        for x in sorted(items, key=lambda i: i["name"]):
            print(f"  {x['name']:40s}  {x['size']//1024:6d} KB  mtime={x['mtime_iso']}  hash={x['hash']}")
