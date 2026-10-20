#!/usr/bin/env python3
"""
Phase 2 Step 1 (Sandboxed): Build data/manifest.json from data/discovery_results.json.
Organizes all discovered files in the user's selected categories into logical talk entries:
- Core talks, colloquia, seminars & conference decks
- Academic posters
- Grant review & program briefing decks
- UW course lecture series (Dave Bacon's lectures)

For each talk entry:
- Selects the canonical/final presentation file as `primary_source`
- Places earlier progressive drafts into `draft_sources` (to be archived in original/drafts/)
- Attaches any existing exported PDF as `existing_pdf`
- Attaches any co-located media (.mov, .mp4, .avi) or PostScript (.ps) files
"""

import json
import os
import re
from collections import defaultdict
from pathlib import Path

PROJECT_DIR = Path("/Users/dabacon/code/github/dabacon/talk_archive")
DATA_FILE = PROJECT_DIR / "data" / "discovery_results.json"
MANIFEST_FILE = PROJECT_DIR / "data" / "manifest.json"

TALKS_ROOT = "/Users/dabacon/Documents/talks deprecated used drive"


def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-+", "-", s)


def infer_year(folder_name: str, filename: str, mtime_iso: str, btime_iso: str) -> str:
    combined = f"{folder_name} {filename}"
    # Look for explicit 4-digit year 1998..2026
    m4 = re.search(r"\b(199[89]|20[012]\d)\b", combined)
    if m4:
        return m4.group(1)
    # Look for 2-digit year suffix like 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11
    m2 = re.search(r"(?:^|[^0-9])(0[0-9]|1[0-9])(?:[^0-9]|$)", combined)
    if m2:
        yr = int(m2.group(1))
        return f"20{yr:02d}"
    # Fallback to mtime year if not 2008-03-07 bulk-copy date
    if mtime_iso and not mtime_iso.startswith("2008-03-07"):
        return mtime_iso[:4]
    return mtime_iso[:4] if mtime_iso else "2008"


def choose_primary_and_drafts(pres_list: list) -> tuple:
    """
    Given a list of presentation files representing versions of the SAME talk,
    pick the canonical final deck and return (primary, drafts_list).
    Heuristics:
    1. Prefer .key over .ppt/.pptx when both exist for the same talk (in 2008+, .ppt was often exported from .key for compatibility)
    2. Prefer filenames containing 'final', 'fin', 'new', 'colloquium', 'lecture', or highest version number, or largest/latest file
    3. Avoid tiny stub files (< 25 KB) if a larger file exists
    """
    if len(pres_list) == 1:
        return pres_list[0], []

    def rank_key(p):
        nl = p["name"].lower()
        stem = os.path.splitext(nl)[0]
        is_key = 1 if p["ext"] == ".key" else 0
        has_final = 2 if "final" in stem else (1 if "fin" in stem else 0)
        has_new = 1 if "new" in stem else 0
        is_not_backup = 0 if ("backup" in stem or "copy" in stem or "ohno" in stem or "untitled" in stem or ".bak" in stem) else 1
        is_substantial = 1 if p["size"] > 50 * 1024 else 0
        # Version number at end of stem
        vm = re.search(r"(\d+)$", stem)
        ver_num = int(vm.group(1)) if vm else 0
        return (
            is_substantial,
            is_not_backup,
            has_final,
            is_key,
            has_new,
            ver_num,
            p["size"],
            p["mtime"],
        )

    sorted_p = sorted(pres_list, key=rank_key, reverse=True)
    return sorted_p[0], sorted_p[1:]


def match_pdf_for_pres(pres_item: dict, pdfs_in_folder: list):
    """Find best matching PDF in the same folder if any."""
    if not pdfs_in_folder:
        return None
    p_stem = os.path.splitext(pres_item["name"])[0].lower()
    # Exact stem match
    for pdf in pdfs_in_folder:
        pdf_stem = os.path.splitext(pdf["name"])[0].lower()
        if pdf_stem == p_stem:
            return pdf
    # Partial stem match
    for pdf in pdfs_in_folder:
        pdf_stem = os.path.splitext(pdf["name"])[0].lower()
        if p_stem in pdf_stem or pdf_stem in p_stem:
            if "smaller" not in pdf_stem and "template" not in pdf_stem:
                return pdf
    # If only 1 substantial slide PDF in folder, use it
    substantial = [
        pdf for pdf in pdfs_in_folder
        if pdf["size"] > 80 * 1024
        and "template" not in pdf["name"].lower()
        and "physrev" not in pdf["name"].lower()
        and "droppedimage" not in pdf["name"].lower()
    ]
    if len(substantial) == 1:
        return substantial[0]
    return None


def main():
    data = json.loads(DATA_FILE.read_text())
    all_pres = data["presentations"]
    all_pdfs = data["pdfs_candidates"]
    all_ps = data["ps_files"]
    all_media = data["media_candidates"]

    entries = []
    seen_hashes = set()
    seen_paths = set()

    # 1. Process folders inside TALKS_ROOT (/Users/dabacon/Documents/talks deprecated used drive)
    folder_pres = defaultdict(list)
    folder_pdfs = defaultdict(list)
    folder_ps = defaultdict(list)
    folder_media = defaultdict(list)

    for p in all_pres:
        if p["path"].startswith(TALKS_ROOT):
            rel = p["path"][len(TALKS_ROOT) + 1 :]
            top = rel.split("/")[0]
            if top == "Other Peoples Blabberings":
                continue
            folder_pres[top].append(p)
            seen_hashes.add(p["hash"])
            seen_paths.add(p["path"])

    for p in all_pdfs:
        if p["path"].startswith(TALKS_ROOT):
            rel = p["path"][len(TALKS_ROOT) + 1 :]
            top = rel.split("/")[0]
            if top == "Other Peoples Blabberings":
                continue
            folder_pdfs[top].append(p)

    for p in all_ps:
        if p["path"].startswith(TALKS_ROOT):
            rel = p["path"][len(TALKS_ROOT) + 1 :]
            top = rel.split("/")[0]
            if top == "Other Peoples Blabberings":
                continue
            folder_ps[top].append(p)

    for m in all_media:
        if m["path"].startswith(TALKS_ROOT):
            rel = m["path"][len(TALKS_ROOT) + 1 :]
            top = rel.split("/")[0]
            if top == "Other Peoples Blabberings":
                continue
            folder_media[top].append(m)

    # Folders in TALKS_ROOT that contain multiple DISTINCT talks rather than drafts of 1 talk:
    MULTI_DISTINCT_FOLDERS = {
        "CBSSS 2004": [
            ("CBSSS 2004 - Lecture 1", ["cbsss1.ppt"]),
            ("CBSSS 2004 - Lecture 2", ["cbsss2.ppt"]),
            ("CBSSS 2004 - Lecture 3", ["cbsss3.ppt"]),
        ],
        "Computing Beyond Silicon Summer School 2002": [
            ("Computing Beyond Silicon Summer School 2002 - Lecture 1", ["cbsss1.ppt", "cbsss.ppt"]),
            ("Computing Beyond Silicon Summer School 2002 - Lecture 2", ["cbsss2.ppt"]),
            ("Computing Beyond Silicon Summer School 2002 - Lecture 5", ["cbsss5.ppt"]),
        ],
        "Courses 2005": [
            (f"UW Summer 2005 Course - Lecture {i}", [f"Lecture{i}.ppt"])
            for i in range(1, 10)
        ],
        "Italy 2005": [
            ("Italy 2005 Lecture Series - Lecture 1", ["ItalyLecture1.ppt", "Lecture1.ppt"]),
            ("Italy 2005 Lecture Series - Lecture 2", ["ItalyLecture2.ppt"]),
            ("Italy 2005 Lecture Series - Lecture 3", ["ItalyLecture3.ppt"]),
            ("Italy 2005 Lecture Series - Lecture 4", ["ItalyLecture4.ppt"]),
            ("Italy 2005 Lecture Series - Lecture 5", ["ItalyLecture5.ppt"]),
            ("Italy 2005 Lecture Series - Lecture 6", ["ItalyLecture6.ppt"]),
        ],
        "MSRI Lectures 2002": [
            ("MSRI 2002 - Quantum Error Correction", ["msriqecc.ppt"]),
            ("MSRI 2002 - Alternative Quantum Computing", ["msrialt.ppt"]),
        ],
        "Microsoft 2003": [
            ("Microsoft 2003 - Topological Quantum Computing", ["microtop.ppt"]),
            ("Microsoft 2003 - Plenty of Room at the Top", ["plentyatop.ppt"]),
        ],
        "Singapore 2005": [
            ("Singapore 2005 - Hidden Subgroup Problem", ["hsp.ppt"]),
            ("Singapore 2005 - Self-Correcting Quantum Computers", ["selfcorrect.ppt"]),
        ],
        "UNM09Physics": [
            ("UNM Physics Colloquium 2009", ["colloquium.key"]),
            ("UNM Physics Seminar 2009", ["seminar.key"]),
        ],
        "Bungie2011": [
            ("Bungie 2011 Talk", ["Bungie.key"]),
            ("Bacon for Shaw 2011", ["baconforshaw.key"]),
        ],
        "SFI 2016": [
            ("Santa Fe Institute 2016 - Postdoc Talk", ["sfipostdoc.key"]),
            ("Santa Fe Institute 2017 - Alt Academia", ["Bacon - Alt Academia.pptx"]),
            ("Santa Fe Institute 2017 - Postdoc Interdisciplinary", ["Bacon - Postdoc Interdisciplinary.pptx"]),
        ],
        "DARPA09": [
            ("DARPA 2009 Review", ["darpa09.key"]),
            ("DARPA 2009 - Gadgets", ["gadgets.key", "gadgets.ppt"]),
            ("DARPA 2009 Poster", ["poster.key"]),
        ],
        "DARPA10": [
            ("DARPA 2010 Review", ["Bacon_DARPA2010.key", "DARPA1.key", "darpaslides.key"]),
            ("DARPA 2010 Poster", ["Poster.key"]),
        ],
        "DARPA11": [
            ("DARPA QuEST 2011 Review", ["Bacon_QuEST11.key", "sidebar_slides_bacon.pptx", "baconforshaw.ppt"]),
            ("DARPA 2011 - Localize Me", ["localizeme.key"]),
            ("DARPA 2011 Poster", ["darpaposter.key"]),
        ],
        "ARO 2008": [
            ("ARO 2008 Review", ["reviewbacon08.key", "reviewbacon08.ppt", "fiveslidesnew.key", "fiveslides.ppt", "quadchartBacon08.key", "quadchartBacon08.ppt"]),
            ("ARO 2008 Poster", ["poster08.key"]),
        ],
        "ARO Review 07": [
            ("ARO Review 2007", ["reviewbacon07.ppt", "quadchartBacon07.ppt", "quadchart.ppt", "ChartTemplate.ppt"]),
            ("ARO Review 2007/2008 Poster", ["poster08.key"]),
        ],
        "QICCS Australia 2002": [
            ("QICCS Australia 2002 - Part 1", ["qicss1final.ppt", "qicss1fin.ppt", "qicss1.ppt", "qiccs1.ppt"]),
            ("QICCS Australia 2002 - Part 2", ["qicss2final.ppt", "qicss2.ppt", "specialqicss.ppt", "plentyatop.ppt"]),
        ],
        "Oregon State 2004": [
            ("Oregon State 2004 - Tales from the Boundary", ["talesfromboundary.ppt", "boundaryoregon1.ppt"]),
            ("Oregon State 2004 Seminar", ["seminaroregonstate2.ppt", "seminaroregonstate.ppt", "seminaroregonstate1.ppt", "seminarosu1.ppt", "seminarosu1ddd.ppt"]),
        ],
        "UBC 2010": [
            ("UBC 2010 - Talk 1 (Jan 2010)", ["ubc2.key"]),
            ("UBC 2010 - Talk 2 (Apr 2010)", ["ubc.key"]),
        ],
    }

    all_talk_folders = sorted(set(folder_pres.keys()) | set(folder_pdfs.keys()) | set(folder_ps.keys()))
    for top in all_talk_folders:
        # Skip standalone root UAG 2008.key since it's already in UAG 2008 folder
        if top == "UAG 2008.key":
            continue
        pres_items = folder_pres[top]
        pdf_items = folder_pdfs[top]
        ps_items = folder_ps[top]
        media_items = folder_media[top]

        if top in MULTI_DISTINCT_FOLDERS:
            for label, fnames in MULTI_DISTINCT_FOLDERS[top]:
                matched = [p for p in pres_items if p["name"] in fnames]
                if not matched:
                    continue
                primary, drafts = choose_primary_and_drafts(matched)
                pdf_match = match_pdf_for_pres(primary, pdf_items)
                year = infer_year(top, primary["name"], primary["mtime_iso"], primary["btime_iso"])
                cat = "poster" if "poster" in label.lower() else ("course" if "Courses 2005" in top else ("grant" if any(g in label.upper() for g in ["DARPA", "ARO"]) else "talk"))
                entries.append({
                    "slug": f"{year}-{slugify(label)}",
                    "year": int(year),
                    "date": primary["mtime_iso"] if not primary["mtime_iso"].startswith("2008-03-07") else f"{year}-01-01",
                    "venue_or_event": label,
                    "category": cat,
                    "primary_source": primary,
                    "draft_sources": drafts,
                    "existing_pdf": pdf_match,
                    "ps_sources": ps_items,
                    "media_sources": media_items,
                })
        elif pres_items:
            primary, drafts = choose_primary_and_drafts(pres_items)
            pdf_match = match_pdf_for_pres(primary, pdf_items)
            year = infer_year(top, primary["name"], primary["mtime_iso"], primary["btime_iso"])
            label = top[:-4] if top.endswith(".key") else top
            cat = "poster" if "poster" in label.lower() else ("grant" if any(g in label.upper() for g in ["DARPA", "ARO", "IARPA", "NSF", "MUSIQC"]) else "talk")
            entries.append({
                "slug": f"{year}-{slugify(label)}",
                "year": int(year),
                "date": primary["mtime_iso"] if not primary["mtime_iso"].startswith("2008-03-07") else f"{year}-01-01",
                "venue_or_event": label,
                "category": cat,
                "primary_source": primary,
                "draft_sources": drafts,
                "existing_pdf": pdf_match,
                "ps_sources": ps_items,
                "media_sources": media_items,
            })
        elif pdf_items:
            # Folder with only PDF/PS (e.g. nsfposter)
            pdf_primary = sorted(pdf_items, key=lambda x: x["size"], reverse=True)[0]
            year = infer_year(top, pdf_primary["name"], pdf_primary["mtime_iso"], pdf_primary["btime_iso"])
            cat = "poster" if "poster" in top.lower() else "talk"
            entries.append({
                "slug": f"{year}-{slugify(top)}",
                "year": int(year),
                "date": pdf_primary["mtime_iso"] if not pdf_primary["mtime_iso"].startswith("2008-03-07") else f"{year}-01-01",
                "venue_or_event": top,
                "category": cat,
                "primary_source": None,
                "draft_sources": [],
                "existing_pdf": pdf_primary,
                "ps_sources": ps_items,
                "media_sources": media_items,
            })

    # 2. Add Dropbox/shared talks that aren't already in TALKS_ROOT
    for p in all_pres:
        if "/Dropbox/shared talks/" in p["path"]:
            if p["name"] in ("Bacon_DARPA2010.key", "ubc2.key"):
                continue
            year = infer_year("Dropbox shared talks", p["name"], p["mtime_iso"], p["btime_iso"])
            label = os.path.splitext(p["name"])[0].replace(":", "-")
            entries.append({
                "slug": f"{year}-{slugify(label)}",
                "year": int(year),
                "date": label[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", label) else f"{year}-01-01",
                "venue_or_event": label,
                "category": "talk",
                "primary_source": p,
                "draft_sources": [],
                "existing_pdf": None,
                "ps_sources": [],
                "media_sources": [],
            })
            seen_hashes.add(p["hash"])

    # 3. Add Academic Posters from /Users/dabacon/Documents/posters and docs/poster.key & surp_poster.ppt
    for p in all_pres:
        if "/Documents/posters/" in p["path"] or p["path"].endswith("/Documents/docs/poster.key") or p["path"].endswith("surp_poster.ppt"):
            if p["hash"] in seen_hashes:
                continue
            stem = os.path.splitext(p["name"])[0]
            # Merge quist.ppt and quist2.ppt
            if stem == "quist":
                continue
            drafts = []
            if stem == "quist2":
                q1 = [x for x in all_pres if x["path"].endswith("/posters/quist.ppt")]
                drafts = q1
            year = infer_year("Posters", p["name"], p["mtime_iso"], p["btime_iso"])
            label = f"Poster - {stem}"
            entries.append({
                "slug": f"{year}-{slugify(label)}",
                "year": int(year),
                "date": p["mtime_iso"] if not p["mtime_iso"].startswith("2008-03-07") else f"{year}-01-01",
                "venue_or_event": label,
                "category": "poster",
                "primary_source": p,
                "draft_sources": drafts,
                "existing_pdf": None,
                "ps_sources": [],
                "media_sources": [],
            })
            seen_hashes.add(p["hash"])

    # 4. Add Grant Reviews & Briefings in /Users/dabacon/Documents/academia/grants (not already in TALKS_ROOT)
    GRANT_GROUPS = [
        ("2006", "ARO 2006 Quad Chart", ["/grants/aro/quadDaveBacon06.ppt", "/grants/aro/quad06.ppt"]),
        ("2006", "DTO 2006 - Questions Answered", ["/grants/dto 2006/bacon questions answered.ppt", "/grants/dto 2006/concat.ppt"]),
        ("2006", "Lockheed Martin QTEP Fault Tolerance", ["/grants/lockheadmartin/QTEP_FT.ppt", "/grants/lockheadmartin/QTEP_Overview_Template.ppt"]),
        ("2007", "NSF EMT Quantum Computing Presentation", ["/grants/nsf/emtbacon.ppt", "/grants/nsf/emtbaconpowerpoint.ppt", "/grants/nsf/emtpower.ppt"]),
        ("2010", "DARPA QuEST Year 1 Slides", ["/grants/darpa08/Baconyear1slides.key"]),
        ("2010", "QCS 2010 Briefing", ["/grants/QCS2010/QCS2010.key", "/grants/QCS2010.key"]),
        ("2010", "DARPA QuEST Task & Single Slide Briefing", ["/grants/darpaQuEST/DARPA.pptx", "/grants/darpaQuEST/PhaseII/QuEST Single Task Description.pptx", "/grants/darpaQuEST/QuEST Single Slide Bacon UW.ppt", "/grants/darpaQuEST/slidesbacon2011.ppt", "/grants/darpaQuEST/slidesbacon2011.pptx"]),
        ("2010", "MUSIQC Slides for Luming", ["/grants/MUSIQC/Slides for Luming.ppt", "/grants/MUSIQC/Slides for Luming.pptx", "/grants/MUSIQC/Slides for Luming.bak.pptx"]),
        ("2011", "MUSIQC 6-Month MPS Briefing", ["/grants/MUSIQC/mps.pptx", "/grants/MUSIQC/6monthsmps.ppt", "/grants/MUSIQC/6monthsmps.pptx", "/grants/MUSIQC/FT.pptx", "/grants/MUSIQC/boilerplate.pptx"]),
        ("2011", "MUSIQC Architecture Module Profile", ["/grants/MUSIQC/Architecture/ModuleProfile_v0.key"]),
        ("2011", "Sandia Aquarius - Not QUBO", ["/grants/SandiaAquarius/notqubo.key"]),
    ]
    for year, label, suffixes in GRANT_GROUPS:
        matched = [p for p in all_pres if any(p["path"].endswith(sfx) for sfx in suffixes)]
        if not matched:
            continue
        primary, drafts = choose_primary_and_drafts(matched)
        pdf_match = match_pdf_for_pres(primary, [pdf for pdf in all_pdfs if os.path.dirname(pdf["path"]) == os.path.dirname(primary["path"])])
        entries.append({
            "slug": f"{year}-{slugify(label)}",
            "year": int(year),
            "date": primary["mtime_iso"] if not primary["mtime_iso"].startswith("2008-03-07") else f"{year}-01-01",
            "venue_or_event": label,
            "category": "grant",
            "primary_source": primary,
            "draft_sources": drafts,
            "existing_pdf": pdf_match,
            "ps_sources": [],
            "media_sources": [],
        })

    # 5. Add standalone talks in Google Drive / Dropbox shared papers
    STANDALONE_EXTRA = [
        ("2009", "SURP Presentation - Mucking With Photosynthesis", ["/surp_stuff/SURP_PRESENTATION.ppt"]),
        ("2019", "Quantum Computing at UCLA 2019", ["/Google Drive/QC UCLA.pdf"]),
    ]
    for year, label, suffixes in STANDALONE_EXTRA:
        matched_p = [p for p in all_pres if any(p["path"].endswith(sfx) for sfx in suffixes)]
        matched_pdf = [p for p in all_pdfs if any(p["path"].endswith(sfx) for sfx in suffixes)]
        if matched_p:
            primary, drafts = choose_primary_and_drafts(matched_p)
            entries.append({
                "slug": f"{year}-{slugify(label)}",
                "year": int(year),
                "date": primary["mtime_iso"],
                "venue_or_event": label,
                "category": "talk",
                "primary_source": primary,
                "draft_sources": drafts,
                "existing_pdf": None,
                "ps_sources": [],
                "media_sources": [],
            })
        elif matched_pdf:
            pdf_item = matched_pdf[0]
            entries.append({
                "slug": f"{year}-{slugify(label)}",
                "year": int(year),
                "date": pdf_item["mtime_iso"],
                "venue_or_event": label,
                "category": "talk",
                "primary_source": None,
                "draft_sources": [],
                "existing_pdf": pdf_item,
                "ps_sources": [],
                "media_sources": [],
            })

    # 6. Add UW Course Lecture Series (Dave Bacon's own lectures in Teaching/)
    # Note: Summer05 is already included via Courses 2005/Summer2005 (9 lectures).
    # Let's add:
    # - Winter06/Lecture1.ppt
    # - Spring06/lecture01.ppt .. lecture28.ppt (pairing lectureXXnotes.ppt as drafts/variants)
    # - Winter07/ppt/lecture01-dave.ppt .. lecture26-dave.ppt
    # - 321/Review.ppt
    # - 322/CSE 322 Fall 08/fa.key & grids.key
    # - AlgorithmsMakeup/04greed.ppt & 04demo-interval-scheduling.ppt
    teaching_pres = [p for p in all_pres if "/Documents/academia/Teaching/" in p["path"]]
    teaching_pdfs = [p for p in all_pdfs if "/Documents/academia/Teaching/" in p["path"]]

    # Winter 2006
    w06 = [p for p in teaching_pres if "/Teaching/Winter06/Lecture1.ppt" in p["path"]]
    if w06:
        entries.append({
            "slug": "2006-uw-winter06-lecture-1",
            "year": 2006,
            "date": "2006-01-05",
            "venue_or_event": "UW Winter 2006 - Lecture 1",
            "category": "course",
            "primary_source": w06[0],
            "draft_sources": [],
            "existing_pdf": None,
            "ps_sources": [],
            "media_sources": [],
        })

    # Spring 2006 (CSE 370 / Digital Design lectures in Spring06 root)
    sp06_root = [
        p for p in teaching_pres
        if os.path.dirname(p["path"]).endswith("/Teaching/Spring06")
    ]
    sp06_pdfs = [
        p for p in teaching_pdfs
        if os.path.dirname(p["path"]).endswith("/Teaching/Spring06")
    ]
    # Group Spring06 by lecture number
    sp06_groups = defaultdict(list)
    for p in sp06_root:
        nl = p["name"].lower()
        m = re.search(r"lecture\s*(\d+)", nl)
        if m:
            num = int(m.group(1))
            sp06_groups[f"Lecture {num:02d}"].append(p)
        elif "final" in nl:
            sp06_groups["Final Review"].append(p)
    for lkey, items in sorted(sp06_groups.items()):
        # Prefer the non-notes slide deck as primary, or notes as draft
        non_notes = [x for x in items if "note" not in x["name"].lower()]
        notes_only = [x for x in items if "note" in x["name"].lower()]
        if non_notes:
            primary = sorted(non_notes, key=lambda x: x["size"], reverse=True)[0]
            drafts = [x for x in items if x != primary]
        else:
            primary, drafts = choose_primary_and_drafts(items)
        pdf_match = match_pdf_for_pres(primary, sp06_pdfs)
        label = f"UW Spring 2006 Course - {lkey}"
        entries.append({
            "slug": f"2006-{slugify(label)}",
            "year": 2006,
            "date": "2006-04-01",
            "venue_or_event": label,
            "category": "course",
            "primary_source": primary,
            "draft_sources": drafts,
            "existing_pdf": pdf_match,
            "ps_sources": [],
            "media_sources": [],
        })

    # Winter 2007 (CSE 326 Data Structures - lectureXX-dave.ppt)
    wi07_dave = [
        p for p in teaching_pres
        if "/Teaching/Winter07/ppt/" in p["path"] and "dave" in p["name"].lower()
    ]
    wi07_pdfs = [
        p for p in teaching_pdfs
        if "/Teaching/Winter07/ppt/" in p["path"]
    ]
    wi07_groups = defaultdict(list)
    for p in wi07_dave:
        m = re.search(r"lecture(\d+)", p["name"].lower())
        if m:
            wi07_groups[int(m.group(1))].append(p)
    for num, items in sorted(wi07_groups.items()):
        primary, drafts = choose_primary_and_drafts(items)
        pdf_match = match_pdf_for_pres(primary, wi07_pdfs)
        label = f"UW CSE 326 Winter 2007 - Lecture {num:02d}"
        entries.append({
            "slug": f"2007-{slugify(label)}",
            "year": 2007,
            "date": "2007-01-15",
            "venue_or_event": label,
            "category": "course",
            "primary_source": primary,
            "draft_sources": drafts,
            "existing_pdf": pdf_match,
            "ps_sources": [],
            "media_sources": [],
        })

    # CSE 321, CSE 322 Fall 08, AlgorithmsMakeup
    OTHER_COURSES = [
        ("2007", "UW CSE 321 - Course Review", ["/Teaching/321/Review.ppt", "/Teaching/321/reviewhandwriting.ppt", "/Teaching/321/midtermgrades.ppt"]),
        ("2008", "UW CSE 322 Fall 2008 - Finite Automata", ["/Teaching/322/CSE 322 Fall 08/fa.key"]),
        ("2008", "UW CSE 322 Fall 2008 - Regular & Context-Free Grids", ["/Teaching/322/CSE 322 Fall 08/grids.key"]),
        ("2009", "UW Algorithms - Greedy Algorithms & Interval Scheduling", ["/Teaching/AlgorithmsMakeup/04greed.ppt", "/Teaching/AlgorithmsMakeup/04demo-interval-scheduling.ppt"]),
    ]
    for year, label, suffixes in OTHER_COURSES:
        matched = [p for p in teaching_pres if any(p["path"].endswith(sfx) for sfx in suffixes)]
        if matched:
            primary, drafts = choose_primary_and_drafts(matched)
            pdf_match = match_pdf_for_pres(primary, [pdf for pdf in teaching_pdfs if os.path.dirname(pdf["path"]) == os.path.dirname(primary["path"])])
            entries.append({
                "slug": f"{year}-{slugify(label)}",
                "year": int(year),
                "date": primary["mtime_iso"] if not primary["mtime_iso"].startswith("2008-03-07") else f"{year}-01-01",
                "venue_or_event": label,
                "category": "course",
                "primary_source": primary,
                "draft_sources": drafts,
                "existing_pdf": pdf_match,
                "ps_sources": [],
                "media_sources": [],
            })

    # Ensure unique slugs
    slug_counts = defaultdict(int)
    for e in entries:
        base = e["slug"]
        slug_counts[base] += 1
        if slug_counts[base] > 1:
            e["slug"] = f"{base}-{slug_counts[base]}"

    entries.sort(key=lambda x: (x["year"], x["slug"]))

    summary = {
        "total_entries": len(entries),
        "by_category": {
            cat: sum(1 for e in entries if e["category"] == cat)
            for cat in ["talk", "poster", "grant", "course"]
        },
        "with_existing_pdf": sum(1 for e in entries if e["existing_pdf"] is not None),
        "needs_pdf_conversion": sum(1 for e in entries if e["existing_pdf"] is None and e["primary_source"] is not None),
        "entries": entries,
    }
    MANIFEST_FILE.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "entries"}, indent=2))
    print(f"Saved {len(entries)} entries to {MANIFEST_FILE}")


if __name__ == "__main__":
    main()
