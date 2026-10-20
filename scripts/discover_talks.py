#!/usr/bin/env python3
"""
Read-only discovery script to scan /Users/dabacon for old talks:
- Keynote (.key files and legacy .key package directories)
- PowerPoint (.ppt, .pptx, .pps, .ppsx, .odp)
- PDFs (.pdf) analyzed for slide characteristics (aspect ratio, Producer/Creator, keywords, co-location)
- PostScript (.ps) analyzed for slide characteristics
- Video/Audio recordings (.mp4, .mov, .m4v, .mkv, .avi, .webm, .mp3, .m4a)
- LaTeX slide decks (.tex using beamer/prosper/slides/foiltex)
"""

import os
import re
import sys
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime

HOME = Path("/Users/dabacon")
PROJECT_DIR = Path("/Users/dabacon/code/github/dabacon/talk_archive")
DATA_DIR = PROJECT_DIR / "data"

# Directories in HOME/Library to ALLOW (iCloud Drive, Keynote iCloud, CloudStorage like Dropbox/GDrive)
ALLOWED_LIBRARY_SUBDIRS = {
    "Mobile Documents",
    "CloudStorage",
}

# Directory names to skip anywhere in the tree
SKIP_DIR_NAMES = {
    ".Trash",
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    "bower_components",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".tox",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".cache",
    ".npm",
    ".yarn",
    ".pnpm-store",
    ".cargo",
    ".rustup",
    ".pyenv",
    ".conda",
    "miniconda3",
    "anaconda3",
    ".gemini",
    ".cursor",
    ".vscode",
    ".vscode-insiders",
    ".gradle",
    ".m2",
    ".ivy2",
    "Pods",
    "DerivedData",
    "site-packages",
    "dist-packages",
    "sdk",
    "ndk",
    "Steam",
    "Photos Library.photoslibrary",
    "Photo Booth Library",
    "Music",
}

PRESENTATION_EXTS = {".key", ".ppt", ".pptx", ".pps", ".ppsx", ".odp", ".sxi"}
PDF_EXTS = {".pdf"}
PS_EXTS = {".ps"}
MEDIA_EXTS = {".mp4", ".mov", ".m4v", ".mkv", ".avi", ".webm", ".mp3", ".m4a", ".wav"}
TEX_EXTS = {".tex"}

TALK_KEYWORDS = re.compile(
    r"(talk|slide|pres|lect|colloq|seminar|keynote|workshop|tutorial|defense|qip|aps|march|siam|darpa|iarpa|qec|quantum|walk|bacon|invited|panel|symposium|conf|congress|school|course|class|deck|pitch|briefing)",
    re.IGNORECASE,
)

NON_TALK_KEYWORDS = re.compile(
    r"(receipt|invoice|statement|tax|w2|1099|form|manual|datasheet|syllabus|cv|resume|passport|ticket|boarding|itinerary|contract|agreement|lease|bill|bank|insurance|EOB|book|ebook)",
    re.IGNORECASE,
)

SLIDE_PRODUCERS = re.compile(
    r"(Keynote|PowerPoint|Microsoft.*PowerPoint|Impress|OpenOffice|LibreOffice|beamer|prosper|foiltex|Google Docs|Prezi|Deckset|Marp|Reveal|pdf2svg|Context|ConTeXt)",
    re.IGNORECASE,
)

MEDIABOX_RE = re.compile(rb"/MediaBox\s*\[\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*\]")
PRODUCER_RE = re.compile(rb"/(?:Producer|Creator|Title|Subject|Author)\s*\(([^()]{1,200})\)")
ROTATE_RE = re.compile(rb"/Rotate\s+(\d+)")
COUNT_RE = re.compile(rb"/Count\s+(\d+)")


SF_DATALESS = 0x40000000


def is_cloud_or_dataless(path: Path, st=None) -> bool:
    p_str = str(path)
    if "/Library/CloudStorage/" in p_str or "/Library/Mobile Documents/" in p_str:
        return True
    if st is not None and (getattr(st, "st_flags", 0) & SF_DATALESS):
        return True
    return False


def get_dir_size_and_mtime(path: Path):
    total_size = 0
    latest_mtime = 0.0
    earliest_ctime = float("inf")
    has_preview_pdf = False
    has_apxl = False
    has_index_zip = False
    cloud = is_cloud_or_dataless(path)
    try:
        st = path.lstat()
        latest_mtime = st.st_mtime
        earliest_ctime = getattr(st, "st_birthtime", st.st_ctime)
        total_size = st.st_size
    except Exception:
        pass

    if not cloud:
        try:
            for root, dirs, files in os.walk(path):
                for f in files:
                    fp = Path(root) / f
                    fl = f.lower()
                    if fl == "preview.pdf":
                        has_preview_pdf = True
                    elif fl in ("index.apxl", "index.apxl.gz"):
                        has_apxl = True
                    elif fl == "index.zip":
                        has_index_zip = True
                    try:
                        st = fp.lstat()
                        total_size += st.st_size
                        if st.st_mtime > latest_mtime:
                            latest_mtime = st.st_mtime
                        btime = getattr(st, "st_birthtime", st.st_ctime)
                        if btime < earliest_ctime:
                            earliest_ctime = btime
                    except Exception:
                        pass
        except Exception:
            pass
    return {
        "size": total_size,
        "mtime": latest_mtime,
        "btime": earliest_ctime if earliest_ctime != float("inf") else latest_mtime,
        "is_package": True,
        "is_cloud": cloud,
        "has_preview_pdf": has_preview_pdf,
        "has_apxl": has_apxl,
        "has_index_zip": has_index_zip,
    }


def fast_hash(path: Path, is_package: bool = False, size: int = 0, st=None) -> str:
    """Compute a fast fingerprint (first 64KB + middle 64KB + last 64KB + size) or metadata hash for cloud files."""
    if is_cloud_or_dataless(path, st):
        return f"cloud:{size}:{path.name}"

    if is_package:
        h = hashlib.sha256()
        for candidate in ["Index.zip", "index.apxl.gz", "index.apxl", "QuickLook/Preview.pdf"]:
            cp = path / candidate
            try:
                cst = cp.lstat()
                if not (getattr(cst, "st_flags", 0) & SF_DATALESS) and (cst.st_mode & 0o170000) == 0o100000:
                    with open(cp, "rb") as f:
                        h.update(f.read(65536))
            except Exception:
                pass
        return f"pkg:{size}:{h.hexdigest()[:16]}"

    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            if size <= 1024 * 1024:
                while chunk := f.read(65536):
                    h.update(chunk)
            else:
                h.update(f.read(65536))
                f.seek(size // 2)
                h.update(f.read(65536))
                f.seek(max(0, size - 65536))
                h.update(f.read(65536))
        return f"{size}:{h.hexdigest()[:16]}"
    except Exception:
        return f"err:{size}"


def inspect_pdf(path: Path, size: int, st=None) -> dict:
    """Fast binary inspection of PDF metadata, MediaBox aspect ratio, Producer/Creator, and page count."""
    info = {
        "width": None,
        "height": None,
        "aspect": None,
        "is_landscape": False,
        "is_beamer_size": False,
        "producer_meta": "",
        "is_slide_producer": False,
        "max_page_count_hint": None,
        "is_cloud": is_cloud_or_dataless(path, st),
    }
    if info["is_cloud"]:
        return info
    try:
        with open(path, "rb") as f:
            head = f.read(65536)
            tail = b""
            if size > 65536:
                f.seek(max(0, size - 65536))
                tail = f.read(65536)
            buf = head + b"\n" + tail

        # Find MediaBox
        m = MEDIABOX_RE.search(buf)
        if m:
            x0, y0, x1, y1 = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))
            w = abs(x1 - x0)
            h = abs(y1 - y0)
            # Check Rotate
            rot_m = ROTATE_RE.search(buf)
            rot = int(rot_m.group(1)) if rot_m else 0
            if rot in (90, 270):
                w, h = h, w
            if h > 0 and w > 0:
                info["width"] = round(w, 1)
                info["height"] = round(h, 1)
                aspect = w / h
                info["aspect"] = round(aspect, 2)
                if 1.2 <= aspect <= 2.4:
                    info["is_landscape"] = True
                # Beamer standard sizes: ~362.8 x 272.1 (4:3) or ~453.5 x 255.1 (16:9)
                if (355 <= w <= 370 and 265 <= h <= 280) or (445 <= w <= 460 and 250 <= h <= 260):
                    info["is_beamer_size"] = True

        # Find Producer/Creator strings
        metas = []
        for pm in PRODUCER_RE.finditer(buf):
            try:
                s = pm.group(1).decode("latin-1", errors="ignore").strip()
                if s and s not in metas:
                    metas.append(s)
            except Exception:
                pass
        meta_str = " | ".join(metas[:6])
        info["producer_meta"] = meta_str
        if SLIDE_PRODUCERS.search(meta_str) or b"beamer" in buf.lower() or b"keynote" in buf.lower() or b"powerpoint" in buf.lower():
            info["is_slide_producer"] = True

        # Page count hints
        counts = [int(cm.group(1)) for cm in COUNT_RE.finditer(buf) if int(cm.group(1)) < 2000]
        if counts:
            info["max_page_count_hint"] = max(counts)
    except Exception:
        pass
    return info


def inspect_ps(path: Path, size: int, st=None) -> dict:
    """Inspect PostScript header for Creator/Title/Orientation."""
    info = {"creator": "", "title": "", "orientation": "", "is_slides": False, "is_cloud": is_cloud_or_dataless(path, st)}
    if info["is_cloud"]:
        return info
    try:
        with open(path, "rb") as f:
            head = f.read(16384).decode("latin-1", errors="ignore")
        for line in head.splitlines()[:100]:
            if line.startswith("%%Creator:"):
                info["creator"] = line.split(":", 1)[1].strip()
            elif line.startswith("%%Title:"):
                info["title"] = line.split(":", 1)[1].strip()
            elif line.startswith("%%Orientation:"):
                info["orientation"] = line.split(":", 1)[1].strip()
        combined = f"{info['creator']} {info['title']} {info['orientation']}"
        if SLIDE_PRODUCERS.search(combined) or "landscape" in info["orientation"].lower() or "foil" in combined.lower() or "seminar" in combined.lower() or "prosper" in combined.lower():
            info["is_slides"] = True
    except Exception:
        pass
    return info


def inspect_tex(path: Path, st=None) -> bool:
    """Return True if .tex file looks like a slide presentation (beamer, prosper, seminar, foiltex, slides)."""
    if is_cloud_or_dataless(path, st):
        return bool(TALK_KEYWORDS.search(str(path)))
    try:
        with open(path, "rb") as f:
            head = f.read(8192).decode("latin-1", errors="ignore")
        if re.search(r"\\documentclass\s*(?:\[[^\]]*\])?\s*\{\s*(?:beamer|prosper|slides|foiltex|seminar|powerdot)\s*\}", head, re.IGNORECASE):
            return True
    except Exception:
        pass
    return False


def main():
    t0 = time.time()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    presentations = []
    pdfs = []
    ps_files = []
    media_files = []
    tex_slides = []
    dirs_scanned = 0
    permission_errors = []

    for root, dirs, files in os.walk(HOME, topdown=True, followlinks=False):
        dirs_scanned += 1
        root_path = Path(root)

        # Skip the talk_archive destination repo itself
        if root_path == PROJECT_DIR or PROJECT_DIR in root_path.parents:
            dirs[:] = []
            continue

        # Handle /Users/dabacon/Library specially: only enter ALLOWED_LIBRARY_SUBDIRS
        if root_path == HOME / "Library":
            dirs[:] = [d for d in dirs if d in ALLOWED_LIBRARY_SUBDIRS]
            continue

        next_dirs = []
        for d in dirs:
            if d in SKIP_DIR_NAMES:
                continue
            if d.startswith(".") and d not in (".",):
                # Skip hidden directories like .local, .config, etc.
                continue
            dl = d.lower()
            if dl.endswith(".app") or dl.endswith(".framework") or dl.endswith(".bundle") or dl.endswith(".xcodeproj") or dl.endswith(".xcworkspace") or dl.endswith(".photoslibrary") or dl.endswith(".musiclibrary") or dl.endswith(".tvlibrary"):
                continue
            if dl.endswith(".key"):
                # Legacy Keynote bundle directory! Record as presentation and do NOT recurse into it!
                pkg_path = root_path / d
                pkg_info = get_dir_size_and_mtime(pkg_path)
                fhash = fast_hash(pkg_path, is_package=True, size=pkg_info["size"])
                presentations.append({
                    "path": str(pkg_path),
                    "name": d,
                    "ext": ".key",
                    "is_package": True,
                    "size": pkg_info["size"],
                    "mtime": pkg_info["mtime"],
                    "btime": pkg_info["btime"],
                    "mtime_iso": datetime.fromtimestamp(pkg_info["mtime"]).strftime("%Y-%m-%d") if pkg_info["mtime"] else "",
                    "btime_iso": datetime.fromtimestamp(pkg_info["btime"]).strftime("%Y-%m-%d") if pkg_info["btime"] else "",
                    "has_preview_pdf": pkg_info["has_preview_pdf"],
                    "has_apxl": pkg_info["has_apxl"],
                    "has_index_zip": pkg_info["has_index_zip"],
                    "hash": fhash,
                })
                continue
            next_dirs.append(d)
        dirs[:] = next_dirs

        # Inspect files in root
        for f in files:
            if f.startswith("._") or f == ".DS_Store":
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext not in PRESENTATION_EXTS and ext not in PDF_EXTS and ext not in PS_EXTS and ext not in MEDIA_EXTS and ext not in TEX_EXTS:
                continue

            fp = root_path / f
            try:
                st = fp.lstat()
            except Exception:
                permission_errors.append(str(fp))
                continue

            size = st.st_size
            if size == 0:
                continue
            mtime = st.st_mtime
            btime = getattr(st, "st_birthtime", st.st_ctime)
            mtime_iso = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            btime_iso = datetime.fromtimestamp(btime).strftime("%Y-%m-%d")
            dataless = bool(getattr(st, "st_flags", 0) & SF_DATALESS)

            if ext in PRESENTATION_EXTS:
                presentations.append({
                    "path": str(fp),
                    "name": f,
                    "ext": ext,
                    "is_package": False,
                    "is_dataless": dataless,
                    "size": size,
                    "mtime": mtime,
                    "btime": btime,
                    "mtime_iso": mtime_iso,
                    "btime_iso": btime_iso,
                    "hash": fast_hash(fp, is_package=False, size=size, st=st),
                })
            elif ext in PDF_EXTS:
                pdf_info = inspect_pdf(fp, size, st=st)
                path_str = str(fp)
                has_talk_kw = bool(TALK_KEYWORDS.search(path_str))
                in_talks_dir = bool(re.search(r"/(?:talks?|presentations?|slides|colloqui(?:a|um)|seminars?|lectures?)/", path_str, re.IGNORECASE))
                has_nontalk_kw = bool(NON_TALK_KEYWORDS.search(f))
                # Score PDF as a talk candidate
                score = 0
                reasons = []
                if pdf_info["is_slide_producer"]:
                    score += 3
                    reasons.append(f"producer({pdf_info['producer_meta'][:40]})")
                if pdf_info["is_beamer_size"]:
                    score += 4
                    reasons.append("beamer_dimensions")
                elif pdf_info["is_landscape"]:
                    score += 2
                    reasons.append(f"landscape({pdf_info['width']}x{pdf_info['height']})")
                if in_talks_dir:
                    score += 3
                    reasons.append("in_talks_dir")
                elif has_talk_kw:
                    score += 2
                    reasons.append("talk_keyword_in_path")
                if has_nontalk_kw:
                    score -= 3
                    reasons.append("non_talk_keyword")

                pdfs.append({
                    "path": path_str,
                    "name": f,
                    "ext": ext,
                    "is_dataless": dataless,
                    "size": size,
                    "mtime": mtime,
                    "btime": btime,
                    "mtime_iso": mtime_iso,
                    "btime_iso": btime_iso,
                    "score": score,
                    "reasons": reasons,
                    "pdf_info": pdf_info,
                    "hash": fast_hash(fp, is_package=False, size=size, st=st) if score >= 2 else "",
                })
            elif ext in PS_EXTS:
                ps_info = inspect_ps(fp, size, st=st)
                path_str = str(fp)
                has_talk_kw = bool(TALK_KEYWORDS.search(path_str))
                ps_files.append({
                    "path": path_str,
                    "name": f,
                    "ext": ext,
                    "is_dataless": dataless,
                    "size": size,
                    "mtime": mtime,
                    "btime": btime,
                    "mtime_iso": mtime_iso,
                    "btime_iso": btime_iso,
                    "has_talk_kw": has_talk_kw,
                    "ps_info": ps_info,
                    "hash": fast_hash(fp, is_package=False, size=size, st=st),
                })
            elif ext in MEDIA_EXTS:
                path_str = str(fp)
                has_talk_kw = bool(TALK_KEYWORDS.search(path_str))
                media_files.append({
                    "path": path_str,
                    "name": f,
                    "ext": ext,
                    "is_dataless": dataless,
                    "size": size,
                    "mtime": mtime,
                    "btime": btime,
                    "mtime_iso": mtime_iso,
                    "btime_iso": btime_iso,
                    "has_talk_kw": has_talk_kw,
                })
            elif ext in TEX_EXTS:
                if inspect_tex(fp, st=st):
                    tex_slides.append({
                        "path": str(fp),
                        "name": f,
                        "ext": ext,
                        "is_dataless": dataless,
                        "size": size,
                        "mtime": mtime,
                        "btime": btime,
                        "mtime_iso": mtime_iso,
                        "btime_iso": btime_iso,
                    })

    # Post-process: Boost PDFs and Media files that share a directory with a Presentation or TeX slide deck
    pres_dirs = {os.path.dirname(p["path"]) for p in presentations} | {os.path.dirname(t["path"]) for t in tex_slides}
    for p in pdfs:
        if os.path.dirname(p["path"]) in pres_dirs:
            p["score"] += 3
            p["reasons"].append("colocated_with_deck")
            if not p["hash"]:
                p["hash"] = fast_hash(Path(p["path"]), is_package=False, size=p["size"])

    for m in media_files:
        m["colocated_with_deck"] = os.path.dirname(m["path"]) in pres_dirs

    elapsed = round(time.time() - t0, 2)
    summary = {
        "elapsed_sec": elapsed,
        "dirs_scanned": dirs_scanned,
        "permission_errors_count": len(permission_errors),
        "counts": {
            "presentations_total": len(presentations),
            "presentations_by_ext": {},
            "pdfs_total": len(pdfs),
            "pdfs_likely_talk_score_ge_3": sum(1 for p in pdfs if p["score"] >= 3),
            "pdfs_possible_talk_score_2": sum(1 for p in pdfs if p["score"] == 2),
            "ps_total": len(ps_files),
            "tex_slides_total": len(tex_slides),
            "media_total": len(media_files),
            "media_talk_or_colocated": sum(1 for m in media_files if m["has_talk_kw"] or m.get("colocated_with_deck")),
        },
        "presentations": presentations,
        "pdfs_candidates": [p for p in pdfs if p["score"] >= 2],
        "ps_files": ps_files,
        "tex_slides": tex_slides,
        "media_candidates": [m for m in media_files if m["has_talk_kw"] or m.get("colocated_with_deck")],
    }
    for p in presentations:
        ext = p["ext"]
        summary["counts"]["presentations_by_ext"][ext] = summary["counts"]["presentations_by_ext"].get(ext, 0) + 1

    out_file = DATA_DIR / "discovery_results.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Scan finished in {elapsed}s across {dirs_scanned} directories.")
    print(json.dumps(summary["counts"], indent=2))
    print(f"Saved detailed results to {out_file}")


if __name__ == "__main__":
    main()
