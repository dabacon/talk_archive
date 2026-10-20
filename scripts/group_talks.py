#!/usr/bin/env python3
"""
Group discovered files into logical talk candidates and summarize by category:
1. Main Talks & Seminars (from Documents/talks deprecated used drive, Dropbox/shared talks, Google Drive, Downloads)
2. Academic Posters (Documents/posters + poster decks in talks/grants)
3. Grant Reviews & Program Briefings (DARPA, ARO, IARPA, MUSIQC, NSF)
4. University Teaching / Course Lectures (UW CSE 321, 322, 326, 370, Summer05, Winter06, Spring06, Winter07, Fall08)
5. Other People's Talks ("Other Peoples Blabberings", Ruth Anderson / Gaetano Borriello / Hemingway course slides)
"""

import json
import os
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json")


def main():
    data = json.loads(DATA_FILE.read_text())
    pres = data["presentations"]
    pdfs = data["pdfs_candidates"]
    ps_files = data["ps_files"]
    media = data["media_candidates"]

    # Check all subfolders of '/Users/dabacon/Documents/talks deprecated used drive'
    talks_root = "/Users/dabacon/Documents/talks deprecated used drive"
    talk_events = defaultdict(lambda: {"pres": [], "pdfs": [], "ps": [], "media": []})

    for p in pres:
        if p["path"].startswith(talks_root):
            rel = p["path"][len(talks_root) + 1 :]
            event = rel.split("/")[0]
            talk_events[event]["pres"].append(p)
    for p in pdfs:
        if p["path"].startswith(talks_root):
            rel = p["path"][len(talks_root) + 1 :]
            event = rel.split("/")[0]
            talk_events[event]["pdfs"].append(p)
    for p in ps_files:
        if p["path"].startswith(talks_root):
            rel = p["path"][len(talks_root) + 1 :]
            event = rel.split("/")[0]
            talk_events[event]["ps"].append(p)
    for m in media:
        if m["path"].startswith(talks_root):
            rel = m["path"][len(talks_root) + 1 :]
            event = rel.split("/")[0]
            talk_events[event]["media"].append(m)

    print(f"Total talk folders in '{talks_root}': {len(talk_events)}")
    has_pdf = sum(1 for ev, d in talk_events.items() if d["pdfs"])
    no_pdf = sum(1 for ev, d in talk_events.items() if not d["pdfs"] and d["pres"])
    only_pdf_or_ps = sum(1 for ev, d in talk_events.items() if not d["pres"] and (d["pdfs"] or d["ps"]))
    print(f"  - Folders with both presentation (.key/.ppt) and existing PDF: {has_pdf}")
    print(f"  - Folders with presentation (.key/.ppt) but NO PDF yet (needs conversion): {no_pdf}")
    print(f"  - Folders with only PDF/PS: {only_pdf_or_ps}")

    # Also check talks outside 'talks deprecated used drive'
    other_dave_talks = []
    for p in pres:
        if p["path"].startswith(talks_root):
            continue
        pl = p["path"].lower()
        if "/academia/teaching/" in pl:
            continue
        other_dave_talks.append(p)

    print(f"\nPresentations outside '{talks_root}' and outside Teaching: {len(other_dave_talks)}")
    for p in sorted(other_dave_talks, key=lambda x: x["path"]):
        print(f"  [{p['mtime_iso']}] {p['ext']:5s} ({p['size']//1024:6d} KB) {p['path']}")


if __name__ == "__main__":
    main()
