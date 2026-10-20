#!/usr/bin/env python3
"""
Build a structured catalog of all discovered talks, grouping multiple drafts/formats
in the same event folder into logical Talk entries, and separating:
1. Main Talks, Colloquia, Seminars & Conference Presentations (~115 events)
2. Academic Posters (~16 posters)
3. Grant Reviews & Program Briefings (DARPA, ARO, IARPA, MUSIQC, NSF, etc.)
4. University Course Lecture Series (UW CSE 321, 322, 326, 370, Summer05, Winter06, Spring06, Winter07, Fall08)
5. Excluded / Third-Party / Figure-Only Files ("Other Peoples Blabberings", colleague course slides by Ruth/Gaetano/Hemingway, single-figure .key files)
"""

import json
import os
import re
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path("/Users/dabacon/code/github/dabacon/talk_archive/data/discovery_results.json")

TALKS_DIR_ENTRIES = [
    "APS March Meeting 2008", "APS NW Tacoma", "ARO 2008", "ARO Review 07", "ARO Review 2000",
    "Affiliates06", "Allerton 2006", "Arizona 2004", "Australia 2003", "Bell Labs 2006",
    "Berkeley08", "Boulder 2006", "Bungie2011", "CBSSS 2004", "CIFAR 2008", "CIFAR2010",
    "Caltech 2005", "Computing Beyond Silicon Summer School 2002", "Coogee2011", "Courses 2005",
    "DARPA Chicago 2004", "DARPA09", "DARPA10", "DARPA11", "Darpa 2005", "ForMark 2005",
    "GQI", "GeorgiaTech 2006", "IARPAVisit", "IBM 2008", "IQI Funding 2002", "IQI Seminar 2005",
    "Innsbruck 06", "Institute for Quantum Information Seminar 2001", "Italy 2005", "JQINIST",
    "MIT 2003 QIP", "MIT 2007", "MIT2011", "MSRI Lectures 2002", "MUSIQCKickoff", "Mark06",
    "Math-Club", "MichiganPhysics09", "Microsoft 2003", "Oregon 2007", "Oregon State 2004",
    "Other Peoples Blabberings", "PMP 2008", "PSU 2005", "Perimeter 2003", "Perimeter07",
    "Perimeter09", "Preskill Group Meeting NP Time Travel 2002", "Preskill Group Meeting Rhapsody 2003",
    "Princeton2008", "QCMC MIT 2002", "QEC07", "QEC11", "QICCS Australia 2002", "Qcircuit.tex",
    "Qualifying Exam 2001", "Reed 2006", "SFI 2016", "SFI Summer School 2005", "SIAM2010",
    "SQUINT 2003", "SQUINT 2005", "SQUINT 2006", "SQUINT 2007", "SQUINT Retreat 2003",
    "SQUINT SS 2005", "SQUINT2011", "SanDiego06", "Sandia 2006", "Santa Fe Institute 2003",
    "Santa Fe Institute Futures 2005", "Santa Fe Institute Researchers 2005", "Singapore 2005",
    "Snowbird Physics of Quantum Electronics 2001", "Squint 2000", "Stanford 2008", "TQC2009",
    "Toronto 2004", "UAG 2008", "UAG 2008.key", "UBC 2010", "UNM CAS 2004", "UNM09Physics",
    "UW Architecture 2006", "UW Architecture 2007", "UW Architecture 2008", "UW Architecture Lecture",
    "UW CS PMP 2009", "UW CS Seminar 2005", "UW CS Seminar 2006", "UW CS Theory Seminar 2009",
    "UW Condensed Matter AMO 2006", "UW Condensed Matter AMO 2007", "UW Direct Admits",
    "UW Faculty retreat 2009", "UW Honors Class", "UW Physics 2008", "UW Ugrad Research",
    "UW grad recruit", "WSU 2005", "aqis07", "london2006", "newdirections2011", "nsf07",
    "nsfposter", "qip 2005", "recruit.key", "recruit.zip"
]


def main():
    data = json.loads(DATA_FILE.read_text())
    talks_root = "/Users/dabacon/Documents/talks deprecated used drive"

    events = defaultdict(lambda: {"pres": [], "pdfs": [], "ps": [], "media": []})
    for p in data["presentations"]:
        if p["path"].startswith(talks_root):
            ev = p["path"][len(talks_root) + 1 :].split("/")[0]
            events[ev]["pres"].append(p)
    for p in data["pdfs_candidates"]:
        if p["path"].startswith(talks_root):
            ev = p["path"][len(talks_root) + 1 :].split("/")[0]
            events[ev]["pdfs"].append(p)
    for p in data["ps_files"]:
        if p["path"].startswith(talks_root):
            ev = p["path"][len(talks_root) + 1 :].split("/")[0]
            events[ev]["ps"].append(p)
    for m in data["media_candidates"]:
        if m["path"].startswith(talks_root):
            ev = m["path"][len(talks_root) + 1 :].split("/")[0]
            events[ev]["media"].append(m)

    missing = [e for e in TALKS_DIR_ENTRIES if e not in events and e not in ("Qcircuit.tex", "recruit.zip")]
    print("Entries in talks_root with no discovered files:", missing)


if __name__ == "__main__":
    main()
