# Dave Bacon — Historical Talk & Lecture Archive (`talk_archive`)

A curated preservation archive and interactive timeline gallery of **143 presentations** (`6,306` slides across `2000–2020`), including:
- **111 Talks, Colloquia, Seminars & Conference Presentations** (QIP, SQUINT, SFI, Caltech IQI, MIT, Perimeter, APS, SIAM, Berkeley, Stanford, UW, etc.)
- **10 Academic Posters** (`dfsposter00`, `itpposter`, `quist`, `nsfflorida`, `sandiego06`, `ARO`, `DARPA`, `NSF`, etc.)
- **12 Grant Reviews & Program Briefings** (`DARPA QuEST`, `ARO`, `IARPA`, `MUSIQC`, `NSF EMT`, `Sandia Aquarius`, `Lockheed Martin`)
- **10 Selected University of Washington Course Lectures**

---

## Repository Structure

```text
talk_archive/
├── index.html                  # Main interactive archive gallery, career timeline rail & slide viewer
├── CURATE_TALKS.md             # Bidirectional Markdown checklist of kept/excluded talks
├── assets/
│   ├── style.css               # Archive UI, career timeline rail & chapter banner styling
│   ├── app.js                  # Instant search, era/category/topic filtering, scroll-spy & modal viewer
│   └── talks_data.js           # Bundled master catalog for zero-latency loading
├── talks/
│   └── <YYYY-slug>/
│       ├── metadata.yaml       # Title, venue, date, format, slide count, topic tags
│       ├── slides.pdf          # Web-ready vector PDF (original export or native QuickLook vector conversion)
│       ├── thumb.png           # Title-slide cover thumbnail
│       ├── notes.md            # Extracted slide text & speaker notes for full-text indexing
│       └── original/           # Untouched original presentation (.key.zip, .ppt, .pptx, .ps)
│           └── drafts/         # Preserved earlier progressive drafts (v1, v2, etc.)
├── data/
│   ├── talks.json              # Master JSON catalog of all 143 curated presentations
│   ├── manifest.json           # Source-to-archive ingestion manifest
│   ├── discovery_results.json  # Raw read-only home directory discovery output
│   └── inventory_report.md     # Full human-readable inventory report
└── scripts/
    ├── add_talk.py             # One-command CLI to ingest a new talk & update the website
    ├── curation_server.py      # Interactive local server with Keep/Exclude/Edit/Purge & Markdown sync
    ├── qlhtml2pdf.m            # Native macOS WebKit/Quartz vector PDF & thumbnail converter for PPT/Keynote
    ├── process_qlpreviews.py   # Batch QuickLook bundle processor & title/joke-slide normalizer
    ├── test_ppt_repair.py      # Binary PowerPoint PUA Symbol/Wingdings & WMF MT Extra equation font repair
    ├── discover_talks.py       # Read-only home directory presentation scanner
    ├── build_manifest.py       # Deduplication and talk grouping manifest builder
    ├── copy_originals.py       # Non-destructive copy into talks/<slug>/original/
    ├── extract_metadata.py     # Pure-Python .ppt / .pptx / .key slide & title extractor
    └── repair_and_convert.py   # PDF repair, archival slide PDF builder & thumbnail renderer
```

---

## Viewing & Curating the Website Locally

Start the interactive curation & static server from the repository root:

```bash
python3 scripts/curation_server.py 8124
```

Then open [http://localhost:8124](http://localhost:8124) in your browser.

---

## Adding a New Talk in the Future

Use [`scripts/add_talk.py`](scripts/add_talk.py) to ingest a new `.key`, `.ppt`, `.pptx`, or `.pdf` presentation, generate its thumbnail and archival PDF, and update the website index in one command:

```bash
python3 scripts/add_talk.py ~/Desktop/my_new_talk.key \
  --venue "QIP 2027" \
  --title "Quantum Fault Tolerance Beyond the Threshold" \
  --year 2027 \
  --category talk
```

Then commit and push to `main` — the included GitHub Actions workflow ([`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml)) automatically publishes the updated site to GitHub Pages.
