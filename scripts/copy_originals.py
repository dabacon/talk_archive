#!/usr/bin/env python3
"""
Copy untouched original presentation files, intermediate drafts, existing PDFs,
PostScript files, and companion media into /Users/dabacon/code/github/dabacon/talk_archive/talks/<slug>/
according to data/manifest.json.
Zero-destruction guarantee: only reads from source paths and copies into talk_archive/talks/.
"""

import json
import os
import shutil
import time
from pathlib import Path

PROJECT_DIR = Path("/Users/dabacon/code/github/dabacon/talk_archive")
MANIFEST_FILE = PROJECT_DIR / "data" / "manifest.json"
TALKS_DIR = PROJECT_DIR / "talks"


def copy_item(src_path: str, dst_path: Path):
    src = Path(src_path)
    if not src.exists():
        return False
    if dst_path.exists():
        return True
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst_path, symlinks=False)
    else:
        shutil.copy2(src, dst_path)
    return True


def main():
    t0 = time.time()
    manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    entries = manifest["entries"]

    copied_primary = 0
    copied_drafts = 0
    copied_pdfs = 0
    copied_media = 0
    errors = []

    for entry in entries:
        slug = entry["slug"]
        tdir = TALKS_DIR / slug
        orig_dir = tdir / "original"
        orig_dir.mkdir(parents=True, exist_ok=True)

        primary = entry.get("primary_source")
        if primary:
            dst = orig_dir / primary["name"]
            try:
                if copy_item(primary["path"], dst):
                    copied_primary += 1
            except Exception as e:
                errors.append(f"Primary {primary['path']}: {e}")

        for draft in entry.get("draft_sources", []):
            drafts_dir = orig_dir / "drafts"
            dst = drafts_dir / draft["name"]
            try:
                if copy_item(draft["path"], dst):
                    copied_drafts += 1
            except Exception as e:
                errors.append(f"Draft {draft['path']}: {e}")

        existing_pdf = entry.get("existing_pdf")
        if existing_pdf:
            slides_pdf = tdir / "slides.pdf"
            try:
                if copy_item(existing_pdf["path"], slides_pdf):
                    copied_pdfs += 1
            except Exception as e:
                errors.append(f"PDF {existing_pdf['path']}: {e}")

        for ps in entry.get("ps_sources", []):
            dst = orig_dir / ps["name"]
            try:
                copy_item(ps["path"], dst)
            except Exception as e:
                errors.append(f"PS {ps['path']}: {e}")

        for m in entry.get("media_sources", []):
            dst = orig_dir / m["name"]
            try:
                if copy_item(m["path"], dst):
                    copied_media += 1
            except Exception as e:
                errors.append(f"Media {m['path']}: {e}")

    elapsed = round(time.time() - t0, 2)
    print(f"Finished copying in {elapsed}s:")
    print(f"  Primary presentations copied: {copied_primary}")
    print(f"  Draft presentations copied:   {copied_drafts}")
    print(f"  Existing PDFs copied:         {copied_pdfs}")
    print(f"  Companion media copied:       {copied_media}")
    print(f"  Errors:                       {len(errors)}")
    for err in errors[:20]:
        print("   ERROR:", err)


if __name__ == "__main__":
    main()
