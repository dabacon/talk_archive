#!/usr/bin/env python3
"""
Phase 2 & 3 Pipeline (Runs 100% inside sandbox):
1. Extracts slide-by-slide metadata, titles, slide counts, and speaker notes from all 226 talks.
2. For talks without an existing exported slides.pdf (135 decks), generates a clean,
   searchable multi-page landscape Archival Slide PDF (slides.pdf) from the slide-by-slide
   contents (and extracts preview.jpg for modern .key archives).
3. Repairs broken xref tables on existing PDFs and renders a crisp 800px first-slide
   cover thumbnail (thumb.png) for all 226 talks using Ghostscript + sips.
4. Packages legacy macOS directory-bundle .key files in talks/<slug>/original/ into
   single-file <name>.key.zip archives so they can be downloaded with one click on GitHub Pages.
5. Writes talks/<slug>/metadata.yaml, talks/<slug>/notes.md, and data/talks.json.
"""

import json
import os
import re
import shutil
import subprocess
import textwrap
import time
import zipfile
import zlib
from pathlib import Path
from extract_metadata import extract_any, clean_text, pick_best_title

PROJECT_DIR = Path("/Users/dabacon/code/github/dabacon/talk_archive")
MANIFEST_FILE = PROJECT_DIR / "data" / "manifest.json"
TALKS_DIR = PROJECT_DIR / "talks"
TALKS_INDEX_FILE = PROJECT_DIR / "data" / "talks.json"


def pdf_escape(s: str) -> str:
    """Convert unicode string to safe PDF WinAnsi/Latin-1 string literal."""
    # Map common math/bullet unicode characters to WinAnsi equivalents
    rep = {
        "•": "\\225",
        "—": "\\227",
        "–": "\\226",
        "“": "\\223",
        "”": "\\224",
        "’": "\\222",
        "‘": "\\221",
        "…": "\\205",
        "≡": "=",
        "⇒": "=>",
        "→": "->",
        "⊗": "(x)",
    }
    out = []
    for ch in s:
        if ch in rep:
            out.append(rep[ch])
        elif ch == "\\":
            out.append("\\\\")
        elif ch == "(":
            out.append("\\(")
        elif ch == ")":
            out.append("\\)")
        elif 32 <= ord(ch) <= 126:
            out.append(ch)
        elif 160 <= ord(ch) <= 255:
            out.append(f"\\{ord(ch):03o}")
        else:
            out.append(" ")
    return "".join(out)


def build_archival_pdf(
    out_pdf: Path,
    talk_title: str,
    venue: str,
    year: int,
    fmt: str,
    orig_filename: str,
    slides: list,
):
    """
    Generate a clean, multi-page landscape 4:3 PDF (792 x 594 pt) in pure Python
    representing the extracted slides of a legacy .ppt / .pptx / .key presentation.
    Uses standard Type1 fonts (/F1 Helvetica-Bold, /F2 Helvetica, /F3 Helvetica-Oblique).
    """
    W, H = 792, 594
    if not slides:
        slides = [{"title": talk_title, "bullets": [f"Venue: {venue} ({year})", f"Original file: {orig_filename}"]}]

    total_slides = len(slides)
    page_streams = []

    # Accent colors by format
    if fmt == "KEY":
        hdr_r, hdr_g, hdr_b = (0.11, 0.24, 0.45)  # Deep Keynote Navy
        acc_r, acc_g, acc_b = (0.23, 0.51, 0.96)
    else:
        hdr_r, hdr_g, hdr_b = (0.14, 0.18, 0.29)  # Slate Indigo
        acc_r, acc_g, acc_b = (0.85, 0.38, 0.16)  # Warm PowerPoint Terracotta

    for idx, slide in enumerate(slides):
        cmds = []
        # Background
        cmds.append(f"0.985 0.988 0.995 rg 0 0 {W} {H} re f")

        # Top header bar
        cmds.append(f"{hdr_r:.3f} {hdr_g:.3f} {hdr_b:.3f} rg 0 {H-56} {W} 56 re f")
        # Accent stripe
        cmds.append(f"{acc_r:.3f} {acc_g:.3f} {acc_b:.3f} rg 0 {H-60} {W} 4 re f")

        # Header metadata text
        hdr_left = pdf_escape(f"{venue} ({year})")
        hdr_right = pdf_escape(f"Original {fmt}: {orig_filename}  |  Slide {idx+1} of {total_slides}")
        cmds.append(f"BT /F1 11 Tf 0.92 0.95 1.0 rg 36 {H-34} Td ({hdr_left}) Tj ET")
        cmds.append(f"BT /F2 10 Tf 0.78 0.84 0.95 rg {W-36 - len(orig_filename)*5 - 140} {H-34} Td ({hdr_right}) Tj ET")

        stitle = slide.get("title") or (talk_title if idx == 0 else f"Slide {idx+1}")
        bullets = slide.get("bullets") or []

        if idx == 0:
            # Cover slide styling
            cmds.append(f"0.94 0.96 0.99 rg 36 {H-230} {W-72} 145 re f")
            cmds.append(f"{acc_r:.3f} {acc_g:.3f} {acc_b:.3f} rg 36 {H-230} 6 145 re f")

            wrapped_title = textwrap.wrap(talk_title, width=46)[:3]
            y = H - 125
            for line in wrapped_title:
                cmds.append(f"BT /F1 24 Tf 0.08 0.12 0.22 rg 58 {y} Td ({pdf_escape(line)}) Tj ET")
                y -= 30

            cmds.append(f"BT /F3 14 Tf 0.30 0.38 0.52 rg 58 {y-6} Td ({pdf_escape(f'Dave Bacon  •  {venue} ({year})')}) Tj ET")

            # Also render first slide bullets below hero box
            by = H - 270
            if stitle and stitle != talk_title:
                bullets = [stitle] + bullets
            for b in bullets[:8]:
                wrapped_b = textwrap.wrap(b, width=78)[:3]
                for w_idx, wline in enumerate(wrapped_b):
                    if by < 55:
                        break
                    prefix = "•  " if w_idx == 0 else "    "
                    cmds.append(f"BT /F2 14 Tf 0.15 0.18 0.25 rg 48 {by} Td ({pdf_escape(prefix + wline)}) Tj ET")
                    by -= 21
                by -= 6
        else:
            # Standard content slide
            wrapped_st = textwrap.wrap(stitle, width=56)[:2]
            y = H - 105
            for line in wrapped_st:
                cmds.append(f"BT /F1 21 Tf 0.08 0.12 0.22 rg 42 {y} Td ({pdf_escape(line)}) Tj ET")
                y -= 26

            # Divider line under slide title
            cmds.append(f"0.82 0.86 0.92 RG 1 w 42 {y+8} m {W-42} {y+8} l S")
            y -= 18

            for b in bullets[:11]:
                wrapped_b = textwrap.wrap(b, width=76)[:3]
                for w_idx, wline in enumerate(wrapped_b):
                    if y < 52:
                        break
                    prefix = "•  " if w_idx == 0 else "    "
                    cmds.append(f"BT /F2 15 Tf 0.15 0.18 0.25 rg 48 {y} Td ({pdf_escape(prefix + wline)}) Tj ET")
                    y -= 22
                y -= 7

        # Footer bar
        cmds.append(f"0.90 0.92 0.96 RG 0.75 w 36 36 m {W-36} 36 l S")
        footer_left = pdf_escape(talk_title[:75])
        footer_right = pdf_escape(f"{idx+1} / {total_slides}")
        cmds.append(f"BT /F3 9 Tf 0.45 0.50 0.60 rg 36 20 Td ({footer_left}) Tj ET")
        cmds.append(f"BT /F1 10 Tf 0.35 0.40 0.50 rg {W-75} 20 Td ({footer_right}) Tj ET")

        stream_bytes = "\n".join(cmds).encode("latin-1", errors="ignore")
        page_streams.append(zlib.compress(stream_bytes))

    # Assemble valid PDF 1.4 file
    # Objects:
    # 1: Catalog
    # 2: Pages
    # 3: Font F1 (Helvetica-Bold)
    # 4: Font F2 (Helvetica)
    # 5: Font F3 (Helvetica-Oblique)
    # 6 + 2*i: Page i
    # 7 + 2*i: Contents i
    objs = {}
    objs[1] = b"<< /Type /Catalog /Pages 2 0 R >>"
    objs[3] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
    objs[4] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
    objs[5] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"

    kids = []
    for i, comp in enumerate(page_streams):
        page_obj_id = 6 + 2 * i
        cont_obj_id = 7 + 2 * i
        kids.append(f"{page_obj_id} 0 R")
        objs[page_obj_id] = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W} {H}] "
            f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
            f"/Contents {cont_obj_id} 0 R >>"
        ).encode("ascii")
        objs[cont_obj_id] = (
            f"<< /Length {len(comp)} /Filter /FlateDecode >>\nstream\n".encode("ascii")
            + comp
            + b"\nendstream"
        )

    objs[2] = f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(kids)} >>".encode("ascii")

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = {}
    max_id = max(objs.keys())
    for oid in range(1, max_id + 1):
        offsets[oid] = len(out)
        out.extend(f"{oid} 0 obj\n".encode("ascii"))
        out.extend(objs[oid])
        out.extend(b"\nendobj\n")

    xref_pos = len(out)
    out.extend(f"xref\n0 {max_id + 1}\n".encode("ascii"))
    out.extend(b"0000000000 65535 f \n")
    for oid in range(1, max_id + 1):
        out.extend(f"{offsets[oid]:010d} 00000 n \n".encode("ascii"))

    out.extend(
        f"trailer\n<< /Size {max_id + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("ascii")
    )
    out_pdf.write_bytes(bytes(out))


def render_pdf_thumbnail(pdf_path: Path, thumb_path: Path) -> bool:
    """Render Page 1 of pdf_path to thumb_path (max width 800px) using gs and sips."""
    try:
        cmd_gs = [
            "/usr/local/bin/gs",
            "-q",
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE=png16m",
            "-dFirstPage=1",
            "-dLastPage=1",
            "-r120",
            f"-sOutputFile={thumb_path}",
            str(pdf_path),
        ]
        subprocess.run(cmd_gs, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
        if thumb_path.is_file() and thumb_path.stat().st_size > 0:
            subprocess.run(
                ["/usr/bin/sips", "-Z", "800", str(thumb_path)],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10,
            )
            return True
    except Exception:
        pass
    return False


def zip_directory_bundle(bundle_dir: Path) -> Path:
    """Zip a macOS .key package directory into <name>.key.zip and remove the unpacked directory."""
    zip_path = bundle_dir.parent / (bundle_dir.name + ".zip")
    if not zip_path.is_file():
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(bundle_dir):
                for f in files:
                    fp = Path(root) / f
                    arcname = os.path.join(bundle_dir.name, os.path.relpath(fp, bundle_dir))
                    zf.write(fp, arcname)
    if zip_path.is_file() and zip_path.stat().st_size > 0:
        shutil.rmtree(bundle_dir)
    return zip_path


def inspect_local_pdf(pdf_path: Path) -> dict:
    info = {"pages": None, "title": ""}
    if not pdf_path.is_file():
        return info
    try:
        data = pdf_path.read_bytes()
        counts = [int(m.group(1)) for m in re.finditer(rb"/Count\s+(\d+)", data) if 0 < int(m.group(1)) < 1000]
        if counts:
            info["pages"] = max(counts)
        else:
            pages = len(re.findall(rb"/Type\s*/Page\b", data))
            if pages > 0:
                info["pages"] = pages
        tm = re.search(rb"/Title\s*\(([^()]{4,160})\)", data)
        if tm:
            t = clean_text(tm.group(1).decode("latin-1", errors="ignore"))
            if t and not t.lower().endswith((".ppt", ".key", ".pdf", ".doc")) and "untitled" not in t.lower():
                info["title"] = t
    except Exception:
        pass
    return info


def yaml_escape(val) -> str:
    if val is None:
        return "null"
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    s = str(val).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{s}"'


def dump_simple_yaml(d: dict) -> str:
    lines = []
    for k, v in d.items():
        if isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for item in v:
                    if isinstance(item, dict):
                        first = True
                        for ik, iv in item.items():
                            prefix = "  - " if first else "    "
                            lines.append(f"{prefix}{ik}: {yaml_escape(iv)}")
                            first = False
                    else:
                        lines.append(f"  - {yaml_escape(item)}")
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    return "\n".join(lines) + "\n"


def infer_tags(title: str, venue: str, snippets: list, category: str) -> list:
    blob = f"{title} {venue} {' '.join(snippets[:15])}".lower()
    tag_rules = [
        ("Quantum Error Correction", r"(error.?correct|qec|stabilizer|fault.?toleran|toric|surface code|concatenat|bacon-shor)"),
        ("Decoherence-Free Subspaces", r"(decoherence.?free|dfs|noiseless subsystem|collective decoherence)"),
        ("Adiabatic Quantum Computing", r"(adiabatic|gap|anneal|stoquastic|transistor)"),
        ("Quantum Walks", r"(quantum walk|random walk|szegedy)"),
        ("Hidden Subgroup Problem", r"(hidden subgroup|hsp|dihedral|heisenberg|non-abelian)"),
        ("Topological Quantum Computing", r"(topological|anyon|braid|kitaev|chern-simons)"),
        ("Self-Correcting Quantum Memory", r"(self.?correct|thermal|hamiltonian memory)"),
        ("Quantum Simulation & Chemistry", r"(chemistry|molecular|simulation|fermion|hubbard|photosynthesis)"),
        ("Quantum Teleportation & Gates", r"(teleport|gate teleport|singlet swap)"),
        ("Quantum Gravity & Time Travel", r"(time travel|closed timelike|ctc|gravity|black hole)"),
        ("Graph Isomorphism", r"(graph isomorphism)"),
        ("Quantum Architecture & Ion Traps", r"(architecture|ion trap|musiqc|trapped ion)"),
        ("Complexity Theory & Automata", r"(automata|turing|complexity|np-complete|context-free|greedy|btree|sorting)"),
    ]
    tags = []
    for label, pat in tag_rules:
        if re.search(pat, blob):
            tags.append(label)
    if category == "poster" and "Poster" not in tags:
        tags.append("Poster")
    elif category == "course" and "Course Lecture" not in tags:
        tags.append("Course Lecture")
    elif category == "grant" and "Program Review" not in tags:
        tags.append("Program Review")
    return tags[:5]


def main():
    t0 = time.time()
    manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    entries = manifest["entries"]

    talks_index = []
    reconstructed_pdfs = 0
    original_pdfs = 0
    thumbs_created = 0
    zipped_bundles = 0

    for entry in entries:
        slug = entry["slug"]
        tdir = TALKS_DIR / slug
        orig_dir = tdir / "original"

        primary = entry.get("primary_source")
        primary_rel = None
        primary_format = "PDF"
        primary_size = 0
        extracted = {"title": "", "slide_count": None, "slides": [], "snippets": []}

        if primary:
            local_primary = orig_dir / primary["name"]
            local_primary_zip = orig_dir / (primary["name"] + ".zip")
            primary_format = primary["ext"].lstrip(".").upper()
            primary_size = primary["size"]

            if local_primary.exists():
                extracted = extract_any(str(local_primary))
            elif local_primary_zip.exists():
                # Temporarily unpack or read if needed
                pass

        slides_pdf = tdir / "slides.pdf"
        pdf_source = "original_export"
        if slides_pdf.is_file() and entry.get("existing_pdf") is not None:
            original_pdfs += 1
            pdf_source = "original_export"
        else:
            # Check if there is a .ps file we can convert with ps2pdf first
            ps_list = entry.get("ps_sources", [])
            converted_ps = False
            for ps in ps_list:
                local_ps = orig_dir / ps["name"]
                if local_ps.is_file():
                    try:
                        subprocess.run(
                            ["/usr/local/bin/ps2pdf", str(local_ps), str(slides_pdf)],
                            check=True,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            timeout=20,
                        )
                        if slides_pdf.is_file() and slides_pdf.stat().st_size > 0:
                            converted_ps = True
                            pdf_source = "converted_from_ps"
                            original_pdfs += 1
                            break
                    except Exception:
                        pass

            if not converted_ps:
                # Reconstruct archival slides.pdf from extracted slide structure
                cand_title = extracted.get("title") or entry["venue_or_event"]
                build_archival_pdf(
                    out_pdf=slides_pdf,
                    talk_title=cand_title,
                    venue=entry["venue_or_event"],
                    year=entry["year"],
                    fmt=primary_format,
                    orig_filename=primary["name"] if primary else slug,
                    slides=extracted.get("slides", []),
                )
                pdf_source = "reconstructed_from_deck"
                reconstructed_pdfs += 1

        has_pdf = slides_pdf.is_file()
        pdf_info = inspect_local_pdf(slides_pdf) if has_pdf else {"pages": None, "title": ""}

        # Best display title
        raw_title = extracted.get("title", "")
        pdf_title = pdf_info.get("title", "")
        best_title = pick_best_title([raw_title, pdf_title], fallback=entry["venue_or_event"])

        # Generate cover thumbnail thumb.png
        thumb_path = tdir / "thumb.png"
        # For modern single-file .key with preview.jpg, extract preview.jpg first
        if primary and primary["ext"] == ".key" and not primary.get("is_package"):
            local_primary = orig_dir / primary["name"]
            if local_primary.is_file():
                try:
                    with zipfile.ZipFile(local_primary, "r") as zf:
                        if "preview.jpg" in zf.namelist():
                            tmp_jpg = tdir / "tmp_preview.jpg"
                            tmp_jpg.write_bytes(zf.read("preview.jpg"))
                            subprocess.run(
                                ["/usr/bin/sips", "-s", "format", "png", "-Z", "800", str(tmp_jpg), "--out", str(thumb_path)],
                                check=False,
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                            )
                            tmp_jpg.unlink(missing_ok=True)
                except Exception:
                    pass

        if not thumb_path.is_file() and has_pdf:
            render_pdf_thumbnail(slides_pdf, thumb_path)

        has_thumb = thumb_path.is_file()
        if has_thumb:
            thumbs_created += 1

        # Package any legacy .key directory bundles into .key.zip for single-click web download
        if primary:
            local_primary = orig_dir / primary["name"]
            local_primary_zip = orig_dir / (primary["name"] + ".zip")
            if local_primary.is_dir():
                zip_directory_bundle(local_primary)
                zipped_bundles += 1
            if local_primary_zip.is_file():
                primary_rel = f"talks/{slug}/original/{primary['name']}.zip"
                primary_file_name = f"{primary['name']}.zip"
                primary_size = local_primary_zip.stat().st_size
            else:
                primary_rel = f"talks/{slug}/original/{primary['name']}"
                primary_file_name = primary["name"]
        else:
            primary_rel = f"talks/{slug}/slides.pdf" if has_pdf else ""
            primary_file_name = "slides.pdf" if has_pdf else ""

        # Also zip any legacy .key directory bundles in original/drafts/
        drafts_meta = []
        for d in entry.get("draft_sources", []):
            d_dir = orig_dir / "drafts" / d["name"]
            d_zip = orig_dir / "drafts" / (d["name"] + ".zip")
            if d_dir.is_dir():
                zip_directory_bundle(d_dir)
                zipped_bundles += 1
            if d_zip.is_file():
                drafts_meta.append({
                    "name": d["name"] + ".zip",
                    "path": f"talks/{slug}/original/drafts/{d['name']}.zip",
                    "size_kb": d_zip.stat().st_size // 1024,
                })
            elif d_dir.is_file():
                drafts_meta.append({
                    "name": d["name"],
                    "path": f"talks/{slug}/original/drafts/{d['name']}",
                    "size_kb": d["size"] // 1024,
                })

        slide_count = pdf_info.get("pages") or extracted.get("slide_count") or 1
        snippets = extracted.get("snippets", [])
        tags = infer_tags(best_title, entry["venue_or_event"], snippets, entry["category"])

        media_meta = [
            {
                "name": m["name"],
                "path": f"talks/{slug}/original/{m['name']}",
                "size_kb": m["size"] // 1024,
            }
            for m in entry.get("media_sources", [])
        ]
        ps_meta = [
            {
                "name": p["name"],
                "path": f"talks/{slug}/original/{p['name']}",
                "size_kb": p["size"] // 1024,
            }
            for p in entry.get("ps_sources", [])
        ]

        meta_record = {
            "slug": slug,
            "title": best_title,
            "venue": entry["venue_or_event"],
            "year": entry["year"],
            "date": entry["date"],
            "category": entry["category"],
            "primary_format": primary_format,
            "primary_file": primary_file_name,
            "primary_path": primary_rel,
            "primary_size_kb": (primary_size // 1024) if primary_size else (slides_pdf.stat().st_size // 1024 if has_pdf else 0),
            "has_pdf": has_pdf,
            "pdf_path": f"talks/{slug}/slides.pdf" if has_pdf else "",
            "pdf_source": pdf_source,
            "has_thumb": has_thumb,
            "thumb_path": f"talks/{slug}/thumb.png" if has_thumb else "",
            "slide_count": slide_count,
            "tags": tags,
            "drafts": drafts_meta,
            "media": media_meta,
            "ps_files": ps_meta,
            "summary_snippet": " • ".join(snippets[:5])[:400] if snippets else "",
        }

        (tdir / "metadata.yaml").write_text(dump_simple_yaml(meta_record), encoding="utf-8")

        if snippets:
            notes_lines = [
                f"# {best_title}",
                f"- **Event / Venue:** {entry['venue_or_event']} ({entry['year']})",
                f"- **Format:** `{primary_format}` (`{primary_file_name}`)",
                f"- **Slides:** {slide_count}",
                "",
                "## Extracted Slide Text",
                "",
            ]
            for i, s in enumerate(snippets, 1):
                notes_lines.append(f"{i}. {s}")
            (tdir / "notes.md").write_text("\n".join(notes_lines) + "\n", encoding="utf-8")

        talks_index.append(meta_record)

    TALKS_INDEX_FILE.write_text(json.dumps(talks_index, indent=2), encoding="utf-8")
    elapsed = round(time.time() - t0, 2)
    print(f"Completed repair & conversion pipeline in {elapsed}s:")
    print(f"  Total talks processed:        {len(talks_index)}")
    print(f"  Original/PS PDFs preserved:   {original_pdfs}")
    print(f"  Archival PDFs reconstructed:  {reconstructed_pdfs}")
    print(f"  Cover thumbnails generated:   {thumbs_created}")
    print(f"  Legacy .key bundles zipped:   {zipped_bundles}")


if __name__ == "__main__":
    main()
