#!/usr/bin/env python3
import json
import os
from pathlib import Path

data = json.loads(Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json").read_text())

key_pkgs = [p for p in data["presentations"] if p["ext"] == ".key" and p.get("is_package")]
key_files = [p for p in data["presentations"] if p["ext"] == ".key" and not p.get("is_package")]
ppts = [p for p in data["presentations"] if p["ext"] in (".ppt", ".pptx")]

print(f"Legacy .key packages: {len(key_pkgs)}")
print(f"  with QuickLook/Preview.pdf inside package: {sum(1 for p in key_pkgs if p.get('has_preview_pdf'))}")
print(f"  with index.apxl(.gz) inside package: {sum(1 for p in key_pkgs if p.get('has_apxl'))}")
print(f"Modern .key single files: {len(key_files)}")
print(f"PPT/PPTX files: {len(ppts)}")
