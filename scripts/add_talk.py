#!/usr/bin/env python3
"""
CLI utility to easily add a new talk to the archive in the future:
Usage:
  python3 scripts/add_talk.py /path/to/deck.key --title "My Talk Title" --venue "QIP 2027" --year 2027 --category talk [--pdf /path/to/exported.pdf]
"""

import argparse
import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from extract_metadata import extract_any, pick_best_title
from repair_and_convert import (
    build_archival_pdf,
    dump_simple_yaml,
    infer_tags,
    inspect_local_pdf,
    render_pdf_thumbnail,
    zip_directory_bundle,
)

PROJECT_DIR = Path("/Users/dabacon/code/github/dabacon/talk_archive")
TALKS_DIR = PROJECT_DIR / "talks"
TALKS_INDEX_FILE = PROJECT_DIR / "data" / "talks.json"
TALKS_JS_FILE = PROJECT_DIR / "assets" / "talks_data.js"


def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-+", "-", s)


def main():
    parser = argparse.ArgumentParser(description="Add a new talk to talk_archive and rebuild the site index.")
    parser.add_argument("file", help="Path to presentation file (.key, .ppt, .pptx, .pdf)")
    parser.add_argument("--title", default="", help="Talk title (auto-extracted if omitted)")
    parser.add_argument("--venue", required=True, help="Conference, seminar, or venue name")
    parser.add_argument("--year", type=int, default=datetime.now().year, help="Four-digit year")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="ISO date YYYY-MM-DD")
    parser.add_argument("--category", choices=["talk", "poster", "grant", "course"], default="talk")
    parser.add_argument("--pdf", default="", help="Optional path to an already-exported PDF")
    args = parser.parse_args()

    src = Path(args.file).expanduser().resolve()
    if not src.exists():
        raise SystemExit(f"Source file not found: {src}")

    slug = f"{args.year}-{slugify(args.venue)}"
    tdir = TALKS_DIR / slug
    orig_dir = tdir / "original"
    orig_dir.mkdir(parents=True, exist_ok=True)

    dst = orig_dir / src.name
    if not dst.exists():
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    ext = src.suffix.lower()
    fmt = ext.lstrip(".").upper()
    extracted = extract_any(str(dst)) if ext != ".pdf" else {"title": "", "slide_count": None, "slides": [], "snippets": []}

    slides_pdf = tdir / "slides.pdf"
    if ext == ".pdf":
        shutil.copy2(dst, slides_pdf)
        pdf_source = "original_export"
    elif args.pdf:
        shutil.copy2(Path(args.pdf).expanduser().resolve(), slides_pdf)
        pdf_source = "original_export"
    else:
        title_cand = args.title or extracted.get("title") or args.venue
        build_archival_pdf(
            out_pdf=slides_pdf,
            talk_title=title_cand,
            venue=args.venue,
            year=args.year,
            fmt=fmt,
            orig_filename=src.name,
            slides=extracted.get("slides", []),
        )
        pdf_source = "reconstructed_from_deck"

    pdf_info = inspect_local_pdf(slides_pdf)
    best_title = args.title or pick_best_title([extracted.get("title", ""), pdf_info.get("title", "")], fallback=args.venue)

    thumb_path = tdir / "thumb.png"
    render_pdf_thumbnail(slides_pdf, thumb_path)

    if dst.is_dir():
        zip_path = zip_directory_bundle(dst)
        primary_file = zip_path.name
        primary_rel = f"talks/{slug}/original/{zip_path.name}"
        primary_size_kb = zip_path.stat().st_size // 1024
    else:
        primary_file = dst.name
        primary_rel = f"talks/{slug}/original/{dst.name}"
        primary_size_kb = dst.stat().st_size // 1024

    snippets = extracted.get("snippets", [])
    tags = infer_tags(best_title, args.venue, snippets, args.category)
    slide_count = pdf_info.get("pages") or extracted.get("slide_count") or 1

    meta_record = {
        "slug": slug,
        "title": best_title,
        "venue": args.venue,
        "year": args.year,
        "date": args.date,
        "category": args.category,
        "primary_format": fmt,
        "primary_file": primary_file,
        "primary_path": primary_rel,
        "primary_size_kb": primary_size_kb,
        "has_pdf": True,
        "pdf_path": f"talks/{slug}/slides.pdf",
        "pdf_source": pdf_source,
        "has_thumb": thumb_path.is_file(),
        "thumb_path": f"talks/{slug}/thumb.png" if thumb_path.is_file() else "",
        "slide_count": slide_count,
        "tags": tags,
        "drafts": [],
        "media": [],
        "ps_files": [],
        "summary_snippet": " • ".join(snippets[:5])[:400] if snippets else "",
    }

    (tdir / "metadata.yaml").write_text(dump_simple_yaml(meta_record), encoding="utf-8")

    # Update data/talks.json and assets/talks_data.js
    talks = json.loads(TALKS_INDEX_FILE.read_text(encoding="utf-8")) if TALKS_INDEX_FILE.is_file() else []
    talks = [t for t in talks if t["slug"] != slug]
    talks.append(meta_record)
    talks.sort(key=lambda x: (x["year"], x["slug"]))
    TALKS_INDEX_FILE.write_text(json.dumps(talks, indent=2), encoding="utf-8")
    TALKS_JS_FILE.write_text(f"window.TALKS_DATA = {json.dumps(talks, indent=2)};\n", encoding="utf-8")
    print(f"Added talk '{best_title}' at talks/{slug}/ and updated website index.")


if __name__ == "__main__":
    main()
