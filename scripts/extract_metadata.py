#!/usr/bin/env python3
"""
Enhanced pure-Python slide-by-slide extractor for:
- Legacy PowerPoint (.ppt) via PowerPoint record atoms (Slide 0x03EE, TextCharsAtom 0x0FA0, TextBytesAtom 0x0FA8)
- Modern PowerPoint (.pptx) via ppt/slides/slide*.xml
- Legacy Apple Keynote packages (.key bundles) via index.apxl.gz / index.apxl XML
- Modern Apple Keynote single-file archives (.key zip/iwa)
"""

import gzip
import json
import os
import re
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


def clean_text(s: str) -> str:
    # Replace private-use Dingbats/Symbol bullets (\uf000-\uf0ff) with bullet/arrow symbols
    s = s.replace("\uf0ba", "≡").replace("\uf0de", "⇒").replace("\uf0ae", "→").replace("\uf0be", "⊗")
    s = re.sub(r"[\uf000-\uf0ff]", "• ", s)
    s = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


BOILERPLATE_SUBSTRINGS = [
    "click to edit master",
    "double-click to edit",
    "second level",
    "third level",
    "fourth level",
    "fifth level",
    "times new roman",
    "default design",
    "master slide",
]

NON_TITLE_PATTERNS = re.compile(
    r"^(?:"
    r"abstract:?|"
    r"outline:?|"
    r"introduction:?|"
    r"overview:?|"
    r"summary:?|"
    r"conclusion[s]?:?|"
    r"motivation:?|"
    r"background:?|"
    r"dave bacon.*|"
    r"david bacon.*|"
    r"department of .*|"
    r"university of .*|"
    r"california institute of technology.*|"
    r"caltech.*|"
    r"uc berkeley.*|"
    r"santa fe institute.*|"
    r"http[s]?://.*|"
    r"www\..*|"
    r"[uU]\(\d+\)|"
    r"slide \d+|"
    r"\d+"
    r")$",
    re.IGNORECASE,
)


def is_master_boilerplate(t: str) -> bool:
    tl = t.lower()
    return any(bp in tl for bp in BOILERPLATE_SUBSTRINGS)


def pick_best_title(candidates: list, fallback: str = "") -> str:
    """Pick the most informative talk title from the first slide's text boxes."""
    valid = []
    for c in candidates:
        t = clean_text(c)
        if not t or len(t) < 4:
            continue
        if is_master_boilerplate(t):
            continue
        # Strip trailing author/institution if separated by newline or bullet in raw text
        alnum = sum(1 for ch in t if ch.isalnum() or ch in " -:,.'?!()/&+≡⇒→⊗")
        if alnum / len(t) < 0.80:
            continue
        valid.append(t)

    # First pass: prefer candidates that don't match NON_TITLE_PATTERNS and have >= 6 chars
    for t in valid:
        if not NON_TITLE_PATTERNS.match(t) and len(t) >= 6:
            return t[:160]
    # Second pass: any valid candidate not matching NON_TITLE_PATTERNS
    for t in valid:
        if not NON_TITLE_PATTERNS.match(t):
            return t[:160]
    # Third pass: first valid candidate
    if valid:
        return valid[0][:160]
    return fallback


def parse_ppt_text_atoms(buf: bytes) -> list:
    """Extract ordered text strings from a slice of a PowerPoint Document stream."""
    texts = []
    n = len(buf)
    for m in re.finditer(b"[\x00\x10\x20\x30\x40\x50\x60\x70\x80\x90\xa0\xb0\xc0\xd0\xe0\xf0][\x00-\x0f](\xa0\x0f|\xa8\x0f)", buf):
        idx = m.start()
        if idx + 8 > n:
            continue
        ver_inst, rec_type, rec_len = struct.unpack_from("<HHI", buf, idx)
        if (ver_inst & 0x0F) != 0:
            continue
        if rec_len == 0 or rec_len > 16000 or idx + 8 + rec_len > n:
            continue
        payload = buf[idx + 8 : idx + 8 + rec_len]
        if rec_type == 0x0FA0:
            if rec_len % 2 != 0:
                continue
            try:
                raw = payload.decode("utf-16-le", errors="strict")
            except Exception:
                continue
        else:
            try:
                raw = payload.decode("latin-1", errors="ignore")
            except Exception:
                continue

        printable = sum(1 for c in raw if c.isprintable() or c in "\r\n\t")
        if len(raw) < 2 or printable / len(raw) < 0.85:
            continue

        # Split by carriage return (\r) into lines/paragraphs within the text box
        lines = [clean_text(line) for line in re.split(r"[\r\n]+", raw) if clean_text(line)]
        if not lines:
            continue
        joined = " — ".join(lines) if len(lines) <= 2 else lines[0]
        for l in lines:
            if len(l) >= 2 and not is_master_boilerplate(l):
                texts.append(l)
    return texts


def extract_ppt_binary(path: Path) -> dict:
    """Extract slide-by-slide text, slide count, and title from binary .ppt file."""
    res = {"title": "", "slide_count": 0, "slides": [], "snippets": [], "notes": []}
    try:
        data = path.read_bytes()
    except Exception as e:
        return {"error": str(e), **res}

    n = len(data)
    # Find Slide container records: recVer=0xF (container), recType=0x03EE (1006)
    # Header bytes: [\x0f\x1f\x2f...] [\x00] \xee \x03 <4-byte length>
    slide_chunks = []
    for m in re.finditer(b"[\x0f\x1f\x2f\x3f]\x00\xee\x03", data):
        idx = m.start()
        if idx + 8 > n:
            continue
        ver_inst, rec_type, rec_len = struct.unpack_from("<HHI", data, idx)
        if rec_len < 16 or rec_len > 2_000_000 or idx + 8 + rec_len > n:
            continue
        slide_chunks.append(data[idx + 8 : idx + 8 + rec_len])

    slides = []
    if slide_chunks:
        for chunk in slide_chunks:
            lines = parse_ppt_text_atoms(chunk)
            if lines:
                slides.append({
                    "title": lines[0][:120],
                    "bullets": lines[1:12],
                })
            else:
                slides.append({"title": "", "bullets": []})

    # Also check SlideListWithText (0x0FF0 = 4080) where PowerPoint often stores slide text
    all_lines = parse_ppt_text_atoms(data)
    if not slides or all(not s["title"] for s in slides):
        # Group all_lines into slides of ~5 lines each
        chunk_size = 5
        slides = []
        for i in range(0, len(all_lines), chunk_size):
            grp = all_lines[i : i + chunk_size]
            slides.append({"title": grp[0][:120], "bullets": grp[1:]})
    elif sum(len(s["bullets"]) + (1 if s["title"] else 0) for s in slides) < len(all_lines) // 2:
        # Slide containers only had drawings while text was in SlideListWithText!
        # Distribute all_lines across the known number of slide containers
        num_slides = max(1, len(slide_chunks))
        per_slide = max(1, (len(all_lines) + num_slides - 1) // num_slides)
        slides = []
        for i in range(0, len(all_lines), per_slide):
            grp = all_lines[i : i + per_slide]
            slides.append({"title": grp[0][:120], "bullets": grp[1:12]})

    res["slide_count"] = max(len(slide_chunks), len(slides)) if (slide_chunks or slides) else 1
    res["slides"] = slides[:120]
    res["title"] = pick_best_title(all_lines[:12])
    res["snippets"] = [
        (" — ".join([s["title"]] + s["bullets"][:3]))[:240]
        for s in slides
        if s["title"] or s["bullets"]
    ][:50]
    return res


def extract_pptx(path: Path) -> dict:
    res = {"title": "", "slide_count": 0, "slides": [], "snippets": [], "notes": []}
    try:
        with zipfile.ZipFile(path, "r") as zf:
            slide_names = sorted(
                [name for name in zf.namelist() if re.match(r"^ppt/slides/slide\d+\.xml$", name)],
                key=lambda x: int(re.findall(r"\d+", x)[0]),
            )
            res["slide_count"] = len(slide_names)
            first_slide_candidates = []
            for idx, sname in enumerate(slide_names):
                xml_bytes = zf.read(sname)
                root = ET.fromstring(xml_bytes)
                # Group text by paragraph <a:p>
                paras = []
                for p_el in root.iter():
                    if p_el.tag.endswith("}p"):
                        runs = [el.text for el in p_el.iter() if el.tag.endswith("}t") and el.text]
                        if runs:
                            t = clean_text("".join(runs))
                            if t and not is_master_boilerplate(t):
                                paras.append(t)
                if idx == 0:
                    first_slide_candidates.extend(paras)
                if paras:
                    res["slides"].append({"title": paras[0][:120], "bullets": paras[1:12]})
                    res["snippets"].append((" — ".join(paras[:4]))[:240])
                else:
                    res["slides"].append({"title": f"Slide {idx+1}", "bullets": []})
            res["title"] = pick_best_title(first_slide_candidates)
    except Exception as e:
        res["error"] = str(e)
    return res


def extract_key_package(path: Path) -> dict:
    """Extract slide-by-slide title, bullets, thumb path, and figure paths from legacy .key bundle."""
    res = {"title": "", "slide_count": 0, "slides": [], "snippets": [], "notes": []}
    apxl_gz = path / "index.apxl.gz"
    apxl_plain = path / "index.apxl"
    try:
        if apxl_gz.exists():
            with gzip.open(apxl_gz, "rb") as f:
                xml_bytes = f.read()
        elif apxl_plain.exists():
            xml_bytes = apxl_plain.read_bytes()
        else:
            return res

        root = ET.fromstring(xml_bytes)
        slide_els = [el for el in root.iter() if el.tag.endswith("}slide")]
        res["slide_count"] = len(slide_els)

        first_candidates = []
        for idx, slide in enumerate(slide_els):
            slide_texts = []
            thumb_ref = ""
            figures = []
            for el in slide.iter():
                tag = el.tag.split("}")[-1]
                # Check for sf:path attributes (thumbnails or figures)
                for attr_k, attr_v in el.attrib.items():
                    if attr_k.endswith("path") and attr_v:
                        if attr_v.startswith("thumbs/"):
                            thumb_ref = attr_v
                        elif not attr_v.startswith("theme-files/"):
                            if attr_v not in figures:
                                figures.append(attr_v)
                if tag == "p":
                    txt = clean_text("".join(el.itertext()))
                    if txt and len(txt) >= 2 and not is_master_boilerplate(txt):
                        if txt not in slide_texts:
                            slide_texts.append(txt)
            if idx <= 1:
                first_candidates.extend(slide_texts)
            stitle = slide_texts[0][:120] if slide_texts else f"Slide {idx+1}"
            sbullets = slide_texts[1:12] if len(slide_texts) > 1 else []
            res["slides"].append({
                "title": stitle,
                "bullets": sbullets,
                "thumb": thumb_ref,
                "figures": figures[:4],
            })
            if slide_texts:
                res["snippets"].append((" | ".join(slide_texts[:4]))[:240])

        res["title"] = pick_best_title(first_candidates)
    except Exception as e:
        res["error"] = str(e)
    return res


def extract_key_modern(path: Path) -> dict:
    """Extract metadata and slide previews from modern single-file .key archive."""
    res = {"title": "", "slide_count": 0, "slides": [], "snippets": [], "has_preview_jpg": False}
    try:
        with zipfile.ZipFile(path, "r") as zf:
            names = zf.namelist()
            res["has_preview_jpg"] = "preview.jpg" in names
            slide_iwas = [n for n in names if re.match(r"^Index/Slide.*\.iwa$", n)]
            st_jpgs = sorted([n for n in names if re.match(r"^Data/st-.*\.jpg$", n)])
            res["slide_count"] = max(len(slide_iwas), len(st_jpgs), 1)
            for idx in range(res["slide_count"]):
                res["slides"].append({
                    "title": f"Slide {idx+1}",
                    "bullets": [],
                    "thumb_zip_member": st_jpgs[idx] if idx < len(st_jpgs) else ("preview.jpg" if idx == 0 and res["has_preview_jpg"] else ""),
                })
    except Exception as e:
        res["error"] = str(e)
    return res


def extract_any(path_str: str) -> dict:
    p = Path(path_str)
    ext = p.suffix.lower()
    if ext == ".key":
        if p.is_dir():
            return extract_key_package(p)
        else:
            return extract_key_modern(p)
    elif ext == ".pptx":
        return extract_pptx(p)
    elif ext == ".ppt":
        return extract_ppt_binary(p)
    return {"title": "", "slide_count": None, "slides": [], "snippets": []}


if __name__ == "__main__":
    for sample in sys.argv[1:]:
        print(sample, "->", json.dumps(extract_any(sample), indent=2))
