#!/usr/bin/env python3
"""
Extract real presentation titles, slide counts, full-text slide snippets, and notes
from all 226 talk folders in talks/<slug>/, write talks/<slug>/metadata.yaml and
talks/<slug>/notes.md, and check PDF/thumbnail status.
"""

import json
import os
import re
from pathlib import Path
from extract_metadata import extract_any, clean_text

PROJECT_DIR = Path("/Users/dabacon/code/github/dabacon/talk_archive")
MANIFEST_FILE = PROJECT_DIR / "data" / "manifest.json"
TALKS_DIR = PROJECT_DIR / "talks"
TALKS_INDEX_FILE = PROJECT_DIR / "data" / "talks.json"


def inspect_local_pdf(pdf_path: Path) -> dict:
    """Extract page count and title/subject from local slides.pdf if present."""
    info = {"pages": None, "title": "", "width": None, "height": None}
    if not pdf_path.is_file():
        return info
    try:
        data = pdf_path.read_bytes()
        counts = [int(m.group(1)) for m in re.finditer(rb"/Count\s+(\d+)", data) if 0 < int(m.group(1)) < 1000]
        if counts:
            info["pages"] = max(counts)
        else:
            # Count /Type /Page\b (not /Pages)
            pages = len(re.findall(rb"/Type\s*/Page\b", data))
            if pages > 0:
                info["pages"] = pages
        tm = re.search(rb"/Title\s*\(([^()]{3,160})\)", data)
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


def is_good_extracted_title(t: str) -> bool:
    if not t or len(t) < 4:
        return False
    tl = t.lower().strip()
    bad_exact = {
        "title", "untitled", "slide 1", "outline", "introduction", "overview",
        "dave bacon", "david bacon", "thank you", "thanks", "questions?",
    }
    if tl in bad_exact:
        return False
    # Reject strings with lots of non-alphanumeric garbage
    alnum = sum(1 for c in t if c.isalnum() or c in " -:,.'?!()/&+")
    if alnum / len(t) < 0.85:
        return False
    return True


def infer_tags(title: str, venue: str, snippets: list, category: str) -> list:
    blob = f"{title} {venue} {' '.join(snippets[:15])}".lower()
    tag_rules = [
        ("Quantum Error Correction", r"(error.?correct|qec|stabilizer|fault.?toleran|toric|surface code|concatenat)"),
        ("Decoherence-Free Subspaces", r"(decoherence.?free|dfs|noiseless subsystem|collective decoherence)"),
        ("Adiabatic Quantum Computing", r"(adiabatic|gap|anneal|stoquastic)"),
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
    manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    entries = manifest["entries"]

    talks_index = []
    extracted_titles_count = 0

    for entry in entries:
        slug = entry["slug"]
        tdir = TALKS_DIR / slug
        orig_dir = tdir / "original"

        primary = entry.get("primary_source")
        primary_rel = None
        primary_format = "PDF"
        primary_size = 0
        extracted = {"title": "", "slide_count": None, "snippets": []}

        if primary:
            local_primary = orig_dir / primary["name"]
            primary_rel = f"talks/{slug}/original/{primary['name']}"
            primary_format = primary["ext"].lstrip(".").upper()
            primary_size = primary["size"]
            if local_primary.exists():
                extracted = extract_any(str(local_primary))

        slides_pdf = tdir / "slides.pdf"
        has_pdf = slides_pdf.is_file()
        pdf_info = inspect_local_pdf(slides_pdf) if has_pdf else {"pages": None, "title": ""}

        # Determine best display title
        raw_title = extracted.get("title", "")
        if is_good_extracted_title(raw_title):
            display_title = raw_title
            extracted_titles_count += 1
        elif is_good_extracted_title(pdf_info.get("title", "")):
            display_title = pdf_info["title"]
            extracted_titles_count += 1
        else:
            display_title = entry["venue_or_event"]

        slide_count = pdf_info.get("pages") or extracted.get("slide_count")
        snippets = extracted.get("snippets", [])
        tags = infer_tags(display_title, entry["venue_or_event"], snippets, entry["category"])

        drafts_meta = []
        for d in entry.get("draft_sources", []):
            drafts_meta.append({
                "name": d["name"],
                "path": f"talks/{slug}/original/drafts/{d['name']}",
                "size_kb": d["size"] // 1024,
            })

        media_meta = []
        for m in entry.get("media_sources", []):
            media_meta.append({
                "name": m["name"],
                "path": f"talks/{slug}/original/{m['name']}",
                "size_kb": m["size"] // 1024,
            })

        ps_meta = []
        for p in entry.get("ps_sources", []):
            ps_meta.append({
                "name": p["name"],
                "path": f"talks/{slug}/original/{p['name']}",
                "size_kb": p["size"] // 1024,
            })

        thumb_file = tdir / "thumb.png"
        has_thumb = thumb_file.is_file()

        meta_record = {
            "slug": slug,
            "title": display_title,
            "venue": entry["venue_or_event"],
            "year": entry["year"],
            "date": entry["date"],
            "category": entry["category"],
            "primary_format": primary_format,
            "primary_file": primary["name"] if primary else (entry["existing_pdf"]["name"] if entry.get("existing_pdf") else ""),
            "primary_path": primary_rel or (f"talks/{slug}/slides.pdf" if has_pdf else ""),
            "primary_size_kb": (primary_size // 1024) if primary_size else (slides_pdf.stat().st_size // 1024 if has_pdf else 0),
            "is_package": bool(primary.get("is_package")) if primary else False,
            "has_pdf": has_pdf,
            "pdf_path": f"talks/{slug}/slides.pdf" if has_pdf else "",
            "has_thumb": has_thumb,
            "thumb_path": f"talks/{slug}/thumb.png" if has_thumb else "",
            "slide_count": slide_count,
            "tags": tags,
            "drafts": drafts_meta,
            "media": media_meta,
            "ps_files": ps_meta,
            "summary_snippet": " • ".join(snippets[:5])[:400] if snippets else "",
        }

        # Write metadata.yaml in talks/<slug>/metadata.yaml
        (tdir / "metadata.yaml").write_text(dump_simple_yaml(meta_record), encoding="utf-8")

        # Write notes.md if we extracted slide text snippets
        if snippets:
            notes_lines = [
                f"# {display_title}",
                f"- **Event / Venue:** {entry['venue_or_event']} ({entry['year']})",
                f"- **Format:** `{primary_format}`",
                "",
                "## Extracted Slide Text",
                "",
            ]
            for i, s in enumerate(snippets, 1):
                notes_lines.append(f"{i}. {s}")
            (tdir / "notes.md").write_text("\n".join(notes_lines) + "\n", encoding="utf-8")

        talks_index.append(meta_record)

    TALKS_INDEX_FILE.write_text(json.dumps(talks_index, indent=2), encoding="utf-8")
    print(f"Processed {len(talks_index)} talks into data/talks.json and talks/*/metadata.yaml.")
    print(f"  Extracted slide titles from inside decks: {extracted_titles_count}")
    print(f"  Already have slides.pdf:                  {sum(1 for t in talks_index if t['has_pdf'])}")
    print(f"  Need PDF conversion:                      {sum(1 for t in talks_index if not t['has_pdf'])}")


if __name__ == "__main__":
    main()
