#!/usr/bin/env python3
"""
Interactive Curation Server for dabacon/talk_archive (runs on http://localhost:8124).
Provides static file serving plus live curation API endpoints:
- GET  /api/status
- POST /api/curate          { "slug": "...", "status": "keep"|"exclude", "title": "...", "venue": "...", "category": "..." }
- POST /api/bulk-curate     { "slugs": [...], "status": "keep"|"exclude" }
- POST /api/sync-md         Re-reads CURATE_TALKS.md checkboxes into data/talks.json
- POST /api/purge-excluded  Removes excluded talks from talks/ and data/talks.json
Also keeps CURATE_TALKS.md, data/talks.json, and assets/talks_data.js in sync.
"""

import http.server
import json
import re
import shutil
import socketserver
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
TALKS_JSON = ROOT / "data" / "talks.json"
TALKS_JS = ROOT / "assets" / "talks_data.js"
CURATE_MD = ROOT / "CURATE_TALKS.md"


def load_talks() -> list:
    if not TALKS_JSON.exists():
        return []
    talks = json.loads(TALKS_JSON.read_text(encoding="utf-8"))
    changed = False
    for t in talks:
        if "status" not in t:
            t["status"] = "keep"
            changed = True
    if changed:
        save_talks(talks)
    return talks


def save_talks(talks: list) -> None:
    TALKS_JSON.write_text(json.dumps(talks, indent=2, ensure_ascii=False), encoding="utf-8")
    TALKS_JS.write_text(
        "window.TALKS_DATA = " + json.dumps(talks, indent=2, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    write_curate_md(talks)


def write_curate_md(talks: list) -> None:
    keep_cnt = sum(1 for t in talks if t.get("status", "keep") != "exclude")
    excl_cnt = len(talks) - keep_cnt
    lines = [
        "# Talk Archive Curation Checklist (`CURATE_TALKS.md`)",
        "",
        f"- **Total Entries:** {len(talks)} (**{keep_cnt} Kept**, **{excl_cnt} Excluded**)",
        "- **How to use:**",
        "  1. **In the Web UI (`http://localhost:8124`):** Click **Keep** / **Exclude** on any card, press `k` (Keep) or `x` (Exclude) while viewing slides, or use the **Bulk Curation** bar at the top.",
        "  2. **Or in this Markdown file:** Change `[x]` to `[ ]` to exclude an entry (or edit the title after `— **Title:**`), then click **Sync from CURATE_TALKS.md** in the Web UI (or run `python3 scripts/curation_server.py --sync-md`).",
        "",
    ]

    categories = [
        ("talk", "Talks, Colloquia & Seminars"),
        ("poster", "Academic Posters"),
        ("grant", "Grant Reviews & Program Briefings"),
        ("course", "University Course Lectures"),
    ]

    for cat_key, cat_label in categories:
        cat_items = [t for t in talks if t.get("category") == cat_key]
        if not cat_items:
            continue
        cat_keep = sum(1 for t in cat_items if t.get("status", "keep") != "exclude")
        lines.append(f"## {cat_label} ({cat_keep} / {len(cat_items)} kept)")
        lines.append("")
        for t in sorted(cat_items, key=lambda x: (x.get("year", 0), x.get("slug", ""))):
            chk = "x" if t.get("status", "keep") != "exclude" else " "
            sc = t.get("slide_count") or 0
            fmt = t.get("primary_format", "")
            fname = t.get("primary_file", "")
            lines.append(
                f"- [{chk}] `{t['slug']}` ({t.get('year')}, {fmt}, {sc}p, `{fname}`) — **Venue:** {t.get('venue', '')} — **Title:** {t.get('title', '')}"
            )
        lines.append("")

    CURATE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sync_from_curate_md() -> dict:
    if not CURATE_MD.exists():
        talks = load_talks()
        write_curate_md(talks)
        return {"updated": 0, "total": len(talks)}

    talks = load_talks()
    by_slug = {t["slug"]: t for t in talks}
    updated = 0

    pattern = re.compile(
        r"^\s*-\s*\[([ xX])\]\s*`([^`]+)`.*?—\s*\*\*Venue:\*\*\s*(.*?)\s*—\s*\*\*Title:\*\*\s*(.+)$"
    )
    for line in CURATE_MD.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line)
        if not m:
            continue
        chk, slug, venue, title = m.groups()
        if slug not in by_slug:
            continue
        t = by_slug[slug]
        new_status = "keep" if chk.lower() == "x" else "exclude"
        venue = venue.strip()
        title = title.strip()
        if t.get("status", "keep") != new_status or t.get("title") != title or t.get("venue") != venue:
            t["status"] = new_status
            if title:
                t["title"] = title
            if venue:
                t["venue"] = venue
            updated += 1

    save_talks(talks)
    return {"updated": updated, "total": len(talks)}


class CurationHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        super().end_headers()

    def log_message(self, format, *args):
        pass

    def _send_json(self, data: dict, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/status":
            talks = load_talks()
            keep_cnt = sum(1 for t in talks if t.get("status", "keep") != "exclude")
            self._send_json(
                {
                    "curation_enabled": True,
                    "total": len(talks),
                    "keep": keep_cnt,
                    "exclude": len(talks) - keep_cnt,
                }
            )
            return
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(length) if length > 0 else b"{}"
        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except Exception:
            payload = {}

        if parsed.path == "/api/curate":
            slug = payload.get("slug")
            talks = load_talks()
            target = next((t for t in talks if t["slug"] == slug), None)
            if not target:
                self._send_json({"error": "Talk not found"}, 404)
                return
            if "status" in payload and payload["status"] in ("keep", "exclude"):
                target["status"] = payload["status"]
            if "title" in payload and str(payload["title"]).strip():
                target["title"] = str(payload["title"]).strip()
            if "venue" in payload and str(payload["venue"]).strip():
                target["venue"] = str(payload["venue"]).strip()
            if "category" in payload and payload["category"] in ("talk", "poster", "grant", "course"):
                target["category"] = payload["category"]
            save_talks(talks)
            keep_cnt = sum(1 for t in talks if t.get("status", "keep") != "exclude")
            self._send_json(
                {
                    "ok": True,
                    "talk": target,
                    "total": len(talks),
                    "keep": keep_cnt,
                    "exclude": len(talks) - keep_cnt,
                }
            )
            return

        if parsed.path == "/api/bulk-curate":
            slugs = set(payload.get("slugs") or [])
            new_status = payload.get("status", "exclude")
            if new_status not in ("keep", "exclude"):
                self._send_json({"error": "Invalid status"}, 400)
                return
            talks = load_talks()
            changed = 0
            for t in talks:
                if t["slug"] in slugs and t.get("status", "keep") != new_status:
                    t["status"] = new_status
                    changed += 1
            save_talks(talks)
            keep_cnt = sum(1 for t in talks if t.get("status", "keep") != "exclude")
            self._send_json(
                {
                    "ok": True,
                    "changed": changed,
                    "total": len(talks),
                    "keep": keep_cnt,
                    "exclude": len(talks) - keep_cnt,
                }
            )
            return

        if parsed.path == "/api/sync-md":
            res = sync_from_curate_md()
            talks = load_talks()
            keep_cnt = sum(1 for t in talks if t.get("status", "keep") != "exclude")
            self._send_json(
                {
                    "ok": True,
                    "updated": res["updated"],
                    "total": len(talks),
                    "keep": keep_cnt,
                    "exclude": len(talks) - keep_cnt,
                    "talks": talks,
                }
            )
            return

        if parsed.path == "/api/purge-excluded":
            talks = load_talks()
            kept = []
            removed_slugs = []
            for t in talks:
                if t.get("status", "keep") == "exclude":
                    removed_slugs.append(t["slug"])
                    talk_dir = ROOT / "talks" / t["slug"]
                    if talk_dir.exists() and talk_dir.is_dir():
                        shutil.rmtree(talk_dir)
                else:
                    kept.append(t)
            save_talks(kept)
            self._send_json(
                {
                    "ok": True,
                    "removed_count": len(removed_slugs),
                    "removed_slugs": removed_slugs,
                    "remaining_total": len(kept),
                }
            )
            return

        self._send_json({"error": "Unknown endpoint"}, 404)


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    talks = load_talks()
    if "--sync-md" in sys.argv:
        res = sync_from_curate_md()
        print(f"Synced {res['updated']} entries from CURATE_TALKS.md (total {res['total']}).")
        sys.exit(0)
    if not CURATE_MD.exists():
        write_curate_md(talks)

    port = 8124
    for arg in sys.argv[1:]:
        if arg.isdigit():
            port = int(arg)

    with ReusableTCPServer(("127.0.0.1", port), CurationHandler) as httpd:
        print(f"Curation server listening on http://localhost:{port}")
        sys.stdout.flush()
        httpd.serve_forever()
