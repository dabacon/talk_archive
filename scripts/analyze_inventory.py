#!/usr/bin/env python3
"""
Generate a comprehensive, human-readable inventory report of discovered talks
at data/inventory_report.md, categorizing into:
1. Main Talk Collections (Google Drive Talks, Documents/talks deprecated used drive, Dropbox/shared talks, Google Drive root)
2. Academic Course Lectures (Documents/academia/Teaching/...)
3. Posters & Grant Briefings (Documents/posters, Documents/academia/grants)
4. Standalone Figure Decks (e.g. figure.key, logos.ppt in paper directories)
"""

import json
import os
from collections import Counter, defaultdict
from pathlib import Path

DATA_FILE = Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json")
REPORT_FILE = Path("/Users/dabacon/code/github/dabacon/talk_archive/data/inventory_report.md")


def categorize_path(path_str: str) -> str:
    pl = path_str.lower()
    if "/my drive/talks" in pl or "/documents/talks" in pl or "/dropbox/shared talks" in pl:
        return "1_dedicated_talks_folders"
    if "/academia/teaching/" in pl:
        return "2_teaching_lectures"
    if "/documents/posters/" in pl or "poster" in os.path.basename(pl):
        return "3_posters"
    if "/academia/grants/" in pl:
        return "4_grants_and_program_reviews"
    if "/figures/" in pl or "fig" in os.path.basename(pl) or "logo" in os.path.basename(pl):
        return "6_paper_figures_and_assets"
    if "/my drive/" in pl or "/google drive/" in pl or "/documents/docs/" in pl or "/downloads/" in pl:
        return "5_other_presentations"
    return "5_other_presentations"


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    pres = data["presentations"]
    pdfs = data["pdfs_candidates"]

    lines = ["# Discovered Talks Inventory Report\n"]
    lines.append(f"- **Total Presentation Files (`.key`, `.ppt`, `.pptx`, `.odp`):** {len(pres)}")
    for ext, cnt in sorted(data["counts"]["presentations_by_ext"].items()):
        lines.append(f"  - `{ext}`: {cnt}")
    lines.append(f"- **Total High-Confidence Slide PDFs (`score >= 3`):** {data['counts']['pdfs_likely_talk_score_ge_3']}")

    # Top directories for presentations
    lines.append("\n## Top Presentation Directories\n")
    lines.append("| Count | Directory |")
    lines.append("| ---: | :--- |")
    dir_counts = Counter(os.path.dirname(p["path"]) for p in pres)
    for d, c in dir_counts.most_common(40):
        lines.append(f"| {c} | `{d}` |")

    # Group presentations by category
    by_cat = defaultdict(list)
    for p in pres:
        by_cat[categorize_path(p["path"])].append(p)

    # Also find PDFs inside dedicated talk folders that don't have a matching .key/.ppt in the same folder
    talk_folder_pdfs = [
        p for p in pdfs
        if categorize_path(p["path"]) == "1_dedicated_talks_folders"
        or "/my drive/" in p["path"].lower()
        or "/google drive/" in p["path"].lower()
    ]

    for cat in sorted(by_cat.keys()):
        items = sorted(by_cat[cat], key=lambda x: (x["mtime_iso"], x["path"]))
        lines.append(f"\n## Category: `{cat}` ({len(items)} presentation files)\n")
        lines.append("| Date (mtime) | Ext | Size (KB) | Package | Dataless | Path |")
        lines.append("| :--- | :--- | ---: | :--- | :--- | :--- |")
        for item in items:
            lines.append(
                f"| {item['mtime_iso']} | `{item['ext']}` | {item['size']//1024} | {item.get('is_package')} | {item.get('is_dataless')} | `{item['path']}` |"
            )

    lines.append(f"\n## PDFs in Dedicated Talk / Google Drive Folders ({len(talk_folder_pdfs)})\n")
    lines.append("| Date (mtime) | Score | Size (KB) | Dataless | Reasons | Path |")
    lines.append("| :--- | ---: | ---: | :--- | :--- | :--- |")
    for p in sorted(talk_folder_pdfs, key=lambda x: (x["mtime_iso"], x["path"])):
        lines.append(
            f"| {p['mtime_iso']} | {p['score']} | {p['size']//1024} | {p.get('is_dataless')} | {', '.join(p['reasons'])} | `{p['path']}` |"
        )

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(lines)} lines to {REPORT_FILE}")


if __name__ == "__main__":
    main()
