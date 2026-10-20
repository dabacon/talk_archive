#!/usr/bin/env python3
"""
Post-process QuickLook .qlpreview bundles generated in data/qlpreviews/*.ppt.qlpreview:
1. Parses Preview.html to find the real Title Slide (skipping Slide 1 when it is a
   projector test / joke slide like 'Test Slide', 'Do Not Read This', 'Nothing Here',
   'sihT esraP oT yrT', 'Tht Yuo Cna Reda Ths Snetnce', 'This Page Left Unintentionally Blank', etc.)
   and extracts the true presentation title (including Escher WordArt titles).
2. Calls scripts/qlhtml2pdf on Preview.html to render all slides into a native vector
   multi-page PDF (talks/<slug>/slides.pdf) and renders the Title Slide into talks/<slug>/thumb.png.
3. Also fixes titles and thumbnails (using Slide 2) for any PDF-backed talks whose Slide 1
   was a joke/test slide.
4. Updates data/talks.json, assets/talks_data.js, and CURATE_TALKS.md.
"""

import html as html_mod
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QLHTML2PDF = ROOT / "scripts" / "qlhtml2pdf"
PREVIEW_DIR = ROOT / "data" / "qlpreviews"
TALKS_JSON = ROOT / "data" / "talks.json"

JOKE_PATTERNS = [
    "test slide",
    "nothing here",
    "do not read",
    "you did",
    "didn't just read",
    "nothing to see",
    "move along",
    "siht esrap",
    "tht yuo",
    "ths sntnc",
    "i eee",
    "intentionally blank",
    "unintentionally blank",
    "read this",
    "sat",
    "mcat",
]

BOILERPLATE_SKIP = [
    "dave bacon",
    "david bacon",
    "department of",
    "university of",
    "california institute",
    "caltech",
    "santa fe institute",
    "institute for quantum",
    "whaley group",
    "preskill",
    "ben toner",
    "graduate student",
    "dabacon@",
    "http://",
    "outline",
]


def is_joke_slide(text: str) -> bool:
    low = text.lower().strip()
    if not low:
        return True
    for pat in JOKE_PATTERNS:
        if pat in low:
            return True
    # Check if slide only has SAT / MCAT / GRE / LSAT
    tokens = set(re.findall(r"[a-z]+", low))
    if tokens and tokens.issubset({"sat", "mcat", "gre", "lsat"}):
        return True
    return False


def extract_slides_from_preview_html(html_text: str) -> list:
    """
    Returns list of non-blank slides, where each slide is a list of text blocks.
    """
    slides = []
    if '<div class="slide"' in html_text:
        parts = html_text.split('<div class="slide"')
        for part in parts[1:]:
            end_idx = part.find('<style type="text/css">')
            chunk = part[:end_idx] if end_idx >= 0 else part
            paras = re.findall(r"<p[^>]*>(.*?)</p>", chunk, flags=re.S)
            lines = []
            for p in paras:
                clean = re.sub(r"<[^>]+>", "", p)
                clean = html_mod.unescape(clean).replace("\xa0", " ").strip()
                if clean:
                    lines.append(clean)
            has_img = bool(re.search(r'<img\s+[^>]*src="', chunk))
            div_count = chunk.count("<div")
            if not lines and not has_img and div_count <= 5:
                continue
            slides.append(lines)
    elif 'class="slideStyle' in html_text:
        parts = re.split(r'<div id="slideId_\d+"[^>]*class="slideStyle[^"]*"[^>]*>', html_text)
        for chunk in parts[1:]:
            paras = re.findall(r"<p[^>]*>(.*?)</p>", chunk, flags=re.S)
            lines = []
            for p in paras:
                clean = re.sub(r"<[^>]+>", "", p)
                clean = html_mod.unescape(clean).replace("\xa0", " ").strip()
                if clean:
                    lines.append(clean)
            slides.append(lines)
    else:
        pdf_imgs = re.findall(r'<img\s+[^>]*src="Attachment\d+\.pdf"', html_text)
        for _ in pdf_imgs:
            slides.append([])
    return slides


def choose_title_and_slide_idx(slides: list, fallback_title: str) -> tuple:
    """
    Given extracted slide text lines per slide, returns (best_title, title_slide_0_based_idx).
    """
    if not slides:
        return fallback_title, 0

    # Find first non-joke slide among first 4 slides
    title_slide_idx = 0
    for idx in range(min(4, len(slides))):
        joined = " ".join(slides[idx])
        if not is_joke_slide(joined):
            title_slide_idx = idx
            break

    # Extract title candidate from title_slide_idx
    candidates = []
    for line in slides[title_slide_idx]:
        low = line.lower().strip()
        if len(line) < 3:
            continue
        if any(bp in low for bp in BOILERPLATE_SKIP):
            continue
        if re.match(r"^[\d\s|⟨⟩〉〈+=().,:-]+$", line):
            continue
        candidates.append(line)

    if candidates:
        # Combine first 1-2 title lines if the first ends with a preposition or is part of a 2-line title
        best = candidates[0]
        if len(candidates) > 1 and (
            best.lower().endswith(("of", "for", "in", "on", "to", "and", "with", "from", "the", "a"))
            or len(best) < 24
        ):
            second = candidates[1]
            if len(second) < 60 and not any(bp in second.lower() for bp in BOILERPLATE_SKIP):
                best = f"{best} {second}"
        return best.strip(), title_slide_idx

    return fallback_title, title_slide_idx


def main():
    talks = json.loads(TALKS_JSON.read_text(encoding="utf-8"))
    by_slug = {t["slug"]: t for t in talks}
    key_preview_dir = ROOT / "data" / "key_qlpreviews"

    converted = 0
    re_titled = 0

    for slug, t in by_slug.items():
        ql_bundle = PREVIEW_DIR / f"{slug}.ppt.qlpreview"
        if not (ql_bundle / "Preview.html").exists():
            ql_bundle = key_preview_dir / f"{slug}.key.qlpreview"
        preview_html = ql_bundle / "Preview.html"
        talk_dir = ROOT / "talks" / slug
        pdf_out = talk_dir / "slides.pdf"
        thumb_out = talk_dir / "thumb.png"

        if preview_html.exists():
            html_text = preview_html.read_text(encoding="utf-8", errors="ignore")
            slides = extract_slides_from_preview_html(html_text)
            best_title, title_idx = choose_title_and_slide_idx(slides, t["title"])

            res = subprocess.run(
                [
                    str(QLHTML2PDF),
                    str(preview_html),
                    str(pdf_out),
                    str(thumb_out),
                    str(title_idx),
                ],
                capture_output=True,
                text=True,
                timeout=60,
            )
            if res.returncode == 0 and pdf_out.exists():
                converted += 1
                if slides:
                    t["slide_count"] = len(slides)
                t["has_pdf"] = True
                t["pdf_path"] = f"talks/{slug}/slides.pdf"
                t["pdf_source"] = "quicklook_vector_pdf"
                if thumb_out.exists():
                    t["has_thumb"] = True
                    t["thumb_path"] = f"talks/{slug}/thumb.png"
                if best_title and best_title != t["title"]:
                    t["title"] = best_title
                    re_titled += 1
        else:
            # Check if this talk had a joke Slide 1 in notes.md (e.g. PDF/KEY backed talk)
            if is_joke_slide(t["title"]):
                notes_p = talk_dir / "notes.md"
                if notes_p.exists():
                    lines = notes_p.read_text(encoding="utf-8", errors="ignore").splitlines()
                    slide_lines = []
                    for l in lines:
                        m = re.match(r"^(\d+)\.\s+(.*)$", l)
                        if m:
                            parts = [
                                x.strip()
                                for x in re.split(r"\s+[—|]\s+", m.group(2))
                                if x.strip()
                            ]
                            slide_lines.append(parts)
                    if slide_lines:
                        best_title, title_idx = choose_title_and_slide_idx(slide_lines, t["title"])
                        if best_title and best_title != t["title"]:
                            t["title"] = best_title
                            re_titled += 1
                        if title_idx > 0 and pdf_out.exists():
                            subprocess.run(
                                [
                                    str(QLHTML2PDF),
                                    "--pdf-thumb",
                                    str(pdf_out),
                                    str(title_idx),
                                    str(thumb_out),
                                ],
                                capture_output=True,
                                timeout=20,
                            )

    # Save via curation_server helper so talks.json, talks_data.js, and CURATE_TALKS.md stay in sync
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    from curation_server import save_talks

    save_talks(talks)
    print(f"Converted {converted} PPT decks to vector PDFs and updated {re_titled} titles/thumbnails.")


if __name__ == "__main__":
    main()
