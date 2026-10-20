(function () {
  let talks = Array.isArray(window.TALKS_DATA) ? window.TALKS_DATA : [];

  const state = {
    query: "",
    category: "all",
    era: "all",
    tag: "all",
    format: "all",
    sort: "year-desc",
    cstatus: "all", // 'all' | 'keep' | 'exclude'
    curationEnabled: false,
    activeModalSlug: null,
  };

  const els = {
    statTotal: document.getElementById("statTotal"),
    statTalks: document.getElementById("statTalks"),
    statCourses: document.getElementById("statCourses"),
    statPostersGrants: document.getElementById("statPostersGrants"),
    curationBanner: document.getElementById("curationBanner"),
    curationStatusPills: document.getElementById("curationStatusPills"),
    cPillAll: document.getElementById("cPillAll"),
    cPillKeep: document.getElementById("cPillKeep"),
    cPillExclude: document.getElementById("cPillExclude"),
    bulkExcludeCoursesBtn: document.getElementById("bulkExcludeCoursesBtn"),
    bulkExcludeGrantsBtn: document.getElementById("bulkExcludeGrantsBtn"),
    bulkExcludePostersBtn: document.getElementById("bulkExcludePostersBtn"),
    bulkExcludeShortBtn: document.getElementById("bulkExcludeShortBtn"),
    bulkExcludeFilteredBtn: document.getElementById("bulkExcludeFilteredBtn"),
    bulkKeepFilteredBtn: document.getElementById("bulkKeepFilteredBtn"),
    syncMdBtn: document.getElementById("syncMdBtn"),
    purgeExcludedBtn: document.getElementById("purgeExcludedBtn"),
    searchInput: document.getElementById("searchInput"),
    clearSearchBtn: document.getElementById("clearSearchBtn"),
    formatFilter: document.getElementById("formatFilter"),
    sortSelect: document.getElementById("sortSelect"),
    categoryTabs: document.getElementById("categoryTabs"),
    eraPills: document.getElementById("eraPills"),
    tagPills: document.getElementById("tagPills"),
    resultsCount: document.getElementById("resultsCount"),
    resetFiltersBtn: document.getElementById("resetFiltersBtn"),
    timelineRail: document.getElementById("timelineRail"),
    talksTimeline: document.getElementById("talksTimeline"),
    modal: document.getElementById("talkModal"),
    closeModalBtn: document.getElementById("closeModalBtn"),
    modalBadges: document.getElementById("modalBadges"),
    modalTitle: document.getElementById("modalTitle"),
    modalVenue: document.getElementById("modalVenue"),
    modalCurationControls: document.getElementById("modalCurationControls"),
    modalPrevBtn: document.getElementById("modalPrevBtn"),
    modalKeepBtn: document.getElementById("modalKeepBtn"),
    modalExcludeBtn: document.getElementById("modalExcludeBtn"),
    modalEditTitleBtn: document.getElementById("modalEditTitleBtn"),
    modalNextBtn: document.getElementById("modalNextBtn"),
    modalPdfFrame: document.getElementById("modalPdfFrame"),
    modalDownloads: document.getElementById("modalDownloads"),
    modalDraftsSection: document.getElementById("modalDraftsSection"),
    modalDrafts: document.getElementById("modalDrafts"),
    modalMediaSection: document.getElementById("modalMediaSection"),
    modalMedia: document.getElementById("modalMedia"),
    modalSnippetSection: document.getElementById("modalSnippetSection"),
    modalSnippet: document.getElementById("modalSnippet"),
    modalNotesLink: document.getElementById("modalNotesLink"),
  };

  function formatSize(kb) {
    if (!kb || kb <= 0) return "";
    if (kb >= 1024) return `${(kb / 1024).toFixed(1)} MB`;
    return `${kb} KB`;
  }

  function categoryLabel(cat) {
    switch (cat) {
      case "talk":
        return "Talk / Colloquium";
      case "poster":
        return "Poster";
      case "grant":
        return "Grant Review";
      case "course":
        return "Course Lecture";
      default:
        return "Presentation";
    }
  }

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function updateCurationCounts() {
    const kept = talks.filter((t) => (t.status || "keep") !== "exclude");
    const excl = talks.length - kept.length;
    if (els.cPillAll) els.cPillAll.textContent = `All (${talks.length})`;
    if (els.cPillKeep) els.cPillKeep.textContent = `✓ Kept (${kept.length})`;
    if (els.cPillExclude) els.cPillExclude.textContent = `✕ Excluded (${excl})`;
    if (els.purgeExcludedBtn) {
      els.purgeExcludedBtn.textContent = `Finalize & Delete Excluded (${excl})`;
      els.purgeExcludedBtn.disabled = excl === 0;
    }

    // Header stats reflect Kept items
    const talkCnt = kept.filter((t) => t.category === "talk").length;
    const courseCnt = kept.filter((t) => t.category === "course").length;
    const pgCnt = kept.filter((t) => t.category === "poster" || t.category === "grant").length;

    if (els.statTotal) els.statTotal.textContent = kept.length;
    if (els.statTalks) els.statTalks.textContent = talkCnt;
    if (els.statCourses) els.statCourses.textContent = courseCnt;
    if (els.statPostersGrants) els.statPostersGrants.textContent = pgCnt;
  }

  function initStatsAndTags() {
    updateCurationCounts();

    const tagCounts = {};
    talks.forEach((t) => {
      (t.tags || []).forEach((tag) => {
        if (tag === "Poster" || tag === "Course Lecture" || tag === "Program Review") return;
        tagCounts[tag] = (tagCounts[tag] || 0) + 1;
      });
    });

    const sortedTags = Object.entries(tagCounts)
      .sort((a, b) => b[1] - a[1])
      .map(([tag]) => tag);

    const pillsHtml = [
      `<button class="pill active" data-tag="all">All Topics</button>`,
      ...sortedTags.map(
        (tag) =>
          `<button class="pill" data-tag="${escapeHtml(tag)}">${escapeHtml(tag)} (${tagCounts[tag]})</button>`
      ),
    ].join("");
    els.tagPills.innerHTML = pillsHtml;
  }

  function matchesFilters(t) {
    const st = t.status || "keep";
    if (state.cstatus !== "all" && st !== state.cstatus) return false;
    if (state.category !== "all" && t.category !== state.category) return false;
    if (state.format !== "all" && t.primary_format !== state.format) return false;
    if (state.tag !== "all" && !(t.tags || []).includes(state.tag)) return false;

    if (state.era !== "all") {
      const [minY, maxY] = state.era.split("-").map(Number);
      if (t.year < minY || t.year > maxY) return false;
    }

    if (state.query) {
      const q = state.query.toLowerCase();
      const hay = [
        t.title,
        t.venue,
        t.year,
        t.primary_file,
        t.summary_snippet,
        ...(t.tags || []),
      ]
        .join(" ")
        .toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  }

  function getFilteredOrderedTalks() {
    const filtered = talks.filter(matchesFilters);
    if (state.sort === "title-asc") {
      return [...filtered].sort((a, b) => a.title.localeCompare(b.title));
    }
    return [...filtered].sort((a, b) => {
      if (a.year !== b.year) {
        return state.sort === "year-asc" ? a.year - b.year : b.year - a.year;
      }
      return a.slug.localeCompare(b.slug);
    });
  }

  function render() {
    updateCurationCounts();
    const filtered = talks.filter(matchesFilters);

    const isFiltered =
      state.query !== "" ||
      state.category !== "all" ||
      state.era !== "all" ||
      state.tag !== "all" ||
      state.format !== "all" ||
      state.cstatus !== "all";
    els.resetFiltersBtn.hidden = !isFiltered;
    els.clearSearchBtn.hidden = state.query === "";
    els.resultsCount.textContent = `Showing ${filtered.length} of ${talks.length} archived presentations`;

    if (filtered.length === 0) {
      if (els.timelineRail) els.timelineRail.hidden = true;
      els.talksTimeline.innerHTML = `
        <div style="text-align:center; padding: 3.5rem 1rem; color: var(--text-muted);">
          <p style="font-size:1.1rem; margin-bottom:0.75rem;">No presentations match your current filters.</p>
          <button class="btn" onclick="document.getElementById('resetFiltersBtn').click()">Reset Filters</button>
        </div>
      `;
      return;
    }

    if (state.sort === "title-asc") {
      if (els.timelineRail) els.timelineRail.hidden = true;
      const sorted = [...filtered].sort((a, b) => a.title.localeCompare(b.title));
      els.talksTimeline.innerHTML = `<div class="cards-grid">${sorted.map(renderCard).join("")}</div>`;
      return;
    }

    const byYear = {};
    filtered.forEach((t) => {
      if (!byYear[t.year]) byYear[t.year] = [];
      byYear[t.year].push(t);
    });

    const years = Object.keys(byYear)
      .map(Number)
      .sort((a, b) => (state.sort === "year-asc" ? a - b : b - a));

    renderTimelineRail(years, byYear);

    let lastChapterId = null;
    const htmlBlocks = [];

    years.forEach((yr) => {
      const items = byYear[yr];
      const chap = getChapterForYear(yr);
      if (chap && chap.id !== lastChapterId) {
        lastChapterId = chap.id;
        // Compute chapter totals across currently filtered years in this chapter
        const chapYears = years.filter((y) => y >= chap.minYear && y <= chap.maxYear);
        const chapDecks = chapYears.reduce((acc, y) => acc + byYear[y].length, 0);
        const chapSlides = chapYears.reduce(
          (acc, y) => acc + byYear[y].reduce((s, item) => s + (item.slide_count || 0), 0),
          0
        );
        htmlBlocks.push(`
          <div class="chapter-banner" id="chapter-${chap.id}" style="--era-color: ${chap.color};">
            <div class="chapter-banner-main">
              <div class="chapter-eyebrow">${escapeHtml(chap.badge)} • ${escapeHtml(chap.range)}</div>
              <h2 class="chapter-title">${escapeHtml(chap.title)}</h2>
              <p class="chapter-desc">${escapeHtml(chap.desc)}</p>
            </div>
            <div class="chapter-stats">
              <span class="chapter-stat-pill"><strong>${chapDecks}</strong> ${chapDecks === 1 ? "deck" : "decks"}</span>
              <span class="chapter-stat-pill"><strong>${chapSlides.toLocaleString()}</strong> slides</span>
            </div>
          </div>
        `);
      }

      const eraColor = chap ? chap.color : "#38bdf8";
      const instLabel = YEAR_INSTITUTION[yr] || (chap ? chap.shortInst : "");
      const yearSlides = items.reduce((s, item) => s + (item.slide_count || 0), 0);
      const fmtCounts = {};
      items.forEach((item) => {
        const f = item.primary_format || "DECK";
        fmtCounts[f] = (fmtCounts[f] || 0) + 1;
      });
      const fmtSummary = Object.entries(fmtCounts)
        .map(([k, v]) => `${v} ${k}`)
        .join(" • ");

      htmlBlocks.push(`
        <div class="year-section" id="year-section-${yr}" data-year="${yr}" style="--era-color: ${eraColor};">
          <span class="year-node-dot" aria-hidden="true"></span>
          <h2 class="year-heading">
            <span class="year-badge-num">${yr}</span>
            ${instLabel ? `<span class="year-era-chip">${escapeHtml(instLabel)}</span>` : ""}
            <span class="year-meta-pills">
              <span class="year-meta-tag">${items.length} ${items.length === 1 ? "deck" : "decks"}</span>
              ${fmtSummary ? `<span class="year-meta-tag">${escapeHtml(fmtSummary)}</span>` : ""}
              ${yearSlides ? `<span class="year-meta-tag">${yearSlides.toLocaleString()} slides</span>` : ""}
            </span>
          </h2>
          <div class="cards-grid">
            ${items.map(renderCard).join("")}
          </div>
        </div>
      `);
    });

    els.talksTimeline.innerHTML = htmlBlocks.join("");
    setupScrollSpy();
  }

  const CAREER_CHAPTERS = [
    {
      id: "2010-2020",
      minYear: 2010,
      maxYear: 2020,
      range: "2010–2020",
      badge: "Chapter IV",
      shortInst: "UW CSE, SFI & Industry",
      title: "UW CSE, Santa Fe Institute & Industry Era",
      desc: "Adiabatic gate teleportation, quantum transistors, closed timelike curves, quantum video games, and reflections on quantum computing.",
      color: "#10b981",
    },
    {
      id: "2007-2009",
      minYear: 2007,
      maxYear: 2009,
      range: "2007–2009",
      badge: "Chapter III",
      shortInst: "UW CSE & Physics",
      title: "University of Washington — CSE & Physics",
      desc: "Doubling the toric code, quantum walk speedups, frustration-free Hamiltonians, and fault-tolerant quantum architectures.",
      color: "#38bdf8",
    },
    {
      id: "2004-2006",
      minYear: 2004,
      maxYear: 2006,
      range: "2004–2006",
      badge: "Chapter II",
      shortInst: "SFI & Early UW",
      title: "Santa Fe Institute & Early UW Faculty Years",
      desc: "Operator quantum error correction, Bacon–Shor subsystem codes, the 2D quantum compass model, and non-Abelian hidden subgroup algorithms.",
      color: "#a855f7",
    },
    {
      id: "2000-2003",
      minYear: 2000,
      maxYear: 2003,
      range: "2000–2003",
      badge: "Chapter I",
      shortInst: "UC Berkeley & Caltech IQI",
      title: "UC Berkeley PhD & Caltech IQI Postdoctoral Years",
      desc: "Decoherence-free subspaces, universal exchange-only quantum computation, communication complexity of singlet correlations, and topological quantum computing.",
      color: "#f59e0b",
    },
  ];

  const YEAR_INSTITUTION = {
    2000: "UC Berkeley • PhD Physics",
    2001: "UC Berkeley & Caltech IQI",
    2002: "Caltech IQI • Postdoc",
    2003: "Caltech IQI • Postdoc",
    2004: "Santa Fe Institute • Postdoc",
    2005: "SFI & Univ. of Washington",
    2006: "Univ. of Washington • CSE",
    2007: "Univ. of Washington • CSE & Physics",
    2008: "Univ. of Washington • CSE & Physics",
    2009: "Univ. of Washington • CSE & Physics",
    2010: "Univ. of Washington • CSE & Physics",
    2011: "Univ. of Washington • CSE & Physics",
    2016: "Santa Fe Institute • Postdoc Talk",
    2020: "Quantum Computing Overview",
  };

  function getChapterForYear(yr) {
    return CAREER_CHAPTERS.find((c) => yr >= c.minYear && yr <= c.maxYear) || null;
  }

  let scrollObserver = null;

  function renderTimelineRail(years, byYear) {
    if (!els.timelineRail) return;
    els.timelineRail.hidden = false;

    const maxCount = Math.max(1, ...years.map((y) => byYear[y].length));
    const orderedChapters =
      state.sort === "year-asc" ? [...CAREER_CHAPTERS].reverse() : [...CAREER_CHAPTERS];

    const chaptersHtml = orderedChapters
      .map((chap) => {
        const chapYears = years.filter((y) => y >= chap.minYear && y <= chap.maxYear);
        if (chapYears.length === 0) return "";
        const firstYear = chapYears[0];
        const yearsHtml = chapYears
          .map((yr) => {
            const cnt = byYear[yr].length;
            const pct = Math.max(12, Math.round((cnt / maxCount) * 100));
            return `
              <button type="button" class="rail-year-item" data-jump-year="${yr}" style="--era-color: ${chap.color};" title="Jump to ${yr} (${cnt} ${cnt === 1 ? "deck" : "decks"})">
                <span>${yr}</span>
                <span class="rail-bar-track"><span class="rail-bar-fill" style="width:${pct}%"></span></span>
                <span class="rail-year-count">${cnt}</span>
              </button>
            `;
          })
          .join("");

        return `
          <div class="rail-chapter" style="--era-color: ${chap.color};">
            <button type="button" class="rail-chapter-header" data-jump-year="${firstYear}" title="Jump to ${escapeHtml(chap.title)}">
              <span class="rail-chapter-years">${escapeHtml(chap.range)}</span>
              <span class="rail-chapter-inst">${escapeHtml(chap.shortInst)}</span>
            </button>
            <div class="rail-years-list">
              ${yearsHtml}
            </div>
          </div>
        `;
      })
      .join("");

    els.timelineRail.innerHTML = `
      <div class="rail-header">
        <span class="rail-title">Timeline</span>
        <span class="rail-subtitle">${years.length} ${years.length === 1 ? "yr" : "yrs"}</span>
      </div>
      ${chaptersHtml}
    `;
  }

  function setActiveRailYear(yr) {
    if (!els.timelineRail) return;
    const btns = els.timelineRail.querySelectorAll(".rail-year-item[data-jump-year]");
    btns.forEach((b) => {
      const match = Number(b.dataset.jumpYear) === Number(yr);
      b.classList.toggle("is-active", match);
    });
  }

  function setupScrollSpy() {
    if (scrollObserver) {
      scrollObserver.disconnect();
      scrollObserver = null;
    }
    const sections = document.querySelectorAll(".year-section[data-year]");
    if (!sections.length) return;

    // Highlight first visible year by default
    setActiveRailYear(sections[0].dataset.year);

    if (!("IntersectionObserver" in window)) return;
    scrollObserver = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible.length > 0) {
          setActiveRailYear(visible[0].target.dataset.year);
        }
      },
      {
        rootMargin: "-12% 0px -65% 0px",
        threshold: 0,
      }
    );
    sections.forEach((sec) => scrollObserver.observe(sec));
  }

  const CACHE_BUST = "?v=6";

  function resolveOriginalUrl(relPath) {
    if (!relPath) return "";
    if (window.location.hostname.endsWith("github.io")) {
      return `https://github.com/dabacon/talk_archive/raw/main/${encodeURI(relPath)}`;
    }
    return relPath;
  }

  function renderCard(t) {
    const st = t.status || "keep";
    const isExcluded = st === "exclude";
    const thumbSrc = t.has_thumb && t.thumb_path ? `${t.thumb_path}${CACHE_BUST}` : "";
    const pdfHref = t.pdf_path ? `${t.pdf_path}${CACHE_BUST}` : "";
    const slidesLabel = t.slide_count ? `${t.slide_count} slides` : "";
    const tagsHtml = (t.tags || [])
      .slice(0, 3)
      .map((tag) => `<span class="tag-chip">${escapeHtml(tag)}</span>`)
      .join("");

    const origBtn =
      t.primary_path && t.primary_path !== t.pdf_path
        ? `<a class="btn" href="${escapeHtml(resolveOriginalUrl(t.primary_path))}" download title="Download preserved original (${escapeHtml(t.primary_file)})">Original .${escapeHtml(t.primary_format.toLowerCase())}</a>`
        : "";

    const curationBarHtml = state.curationEnabled
      ? `
        <div class="curation-card-bar">
          <button class="btn btn-keep ${!isExcluded ? "is-active" : ""}" data-curate-slug="${escapeHtml(t.slug)}" data-curate-status="keep" title="Keep this talk in the archive">✓ Keep</button>
          <button class="btn btn-exclude ${isExcluded ? "is-active" : ""}" data-curate-slug="${escapeHtml(t.slug)}" data-curate-status="exclude" title="Mark this entry for removal">✕ Exclude</button>
          <button class="btn" data-edit-slug="${escapeHtml(t.slug)}" title="Edit title or venue">✎</button>
        </div>
      `
      : "";

    return `
      <article class="talk-card ${isExcluded ? "is-excluded" : "is-kept"}" data-slug="${escapeHtml(t.slug)}">
        ${curationBarHtml}
        <div class="card-thumb-wrap" data-open-slug="${escapeHtml(t.slug)}">
          ${
            thumbSrc
              ? `<img src="${escapeHtml(thumbSrc)}" alt="${escapeHtml(t.title)}" loading="lazy" />`
              : `<div style="display:flex;align-items:center;justify-content:center;height:100%;padding:1rem;text-align:center;color:var(--text-muted);font-weight:600;">${escapeHtml(t.venue)}</div>`
          }
          <div class="card-overlays">
            <span class="badge badge-fmt-${escapeHtml(t.primary_format)}">${escapeHtml(t.primary_format)}</span>
            ${slidesLabel ? `<span class="badge">${escapeHtml(slidesLabel)}</span>` : ""}
          </div>
        </div>
        <div class="card-body">
          <div class="card-venue">${escapeHtml(t.venue)} • ${escapeHtml(categoryLabel(t.category))} • <code>${escapeHtml(t.primary_file)}</code></div>
          <h3 class="card-title" data-open-slug="${escapeHtml(t.slug)}" title="${escapeHtml(t.title)}">
            ${escapeHtml(t.title)}
          </h3>
          ${
            t.summary_snippet
              ? `<p class="card-snippet">${escapeHtml(t.summary_snippet)}</p>`
              : ""
          }
          <div class="card-tags">${tagsHtml}</div>
          <div class="card-actions">
            <button class="btn btn-primary" data-open-slug="${escapeHtml(t.slug)}">View Slides</button>
            ${
              pdfHref
                ? `<a class="btn" href="${escapeHtml(pdfHref)}" target="_blank" rel="noopener">PDF</a>`
                : ""
            }
            ${origBtn}
          </div>
        </div>
      </article>
    `;
  }

  async function setTalkStatus(slug, status, extraFields) {
    const t = talks.find((x) => x.slug === slug);
    if (!t) return;
    t.status = status;
    if (extraFields) {
      if (extraFields.title) t.title = extraFields.title;
      if (extraFields.venue) t.venue = extraFields.venue;
      if (extraFields.category) t.category = extraFields.category;
    }
    render();
    if (state.activeModalSlug === slug) {
      refreshModalHeader(t);
    }

    if (state.curationEnabled) {
      try {
        await fetch("/api/curate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ slug, status, ...(extraFields || {}) }),
        });
      } catch (err) {
        console.error("Failed to save curation status:", err);
      }
    }
  }

  async function bulkSetStatus(slugs, status) {
    if (!slugs.length) return;
    const set = new Set(slugs);
    talks.forEach((t) => {
      if (set.has(t.slug)) t.status = status;
    });
    render();
    if (state.curationEnabled) {
      try {
        await fetch("/api/bulk-curate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ slugs, status }),
        });
      } catch (err) {
        console.error("Failed bulk curation:", err);
      }
    }
  }

  function promptEditTalk(slug) {
    const t = talks.find((x) => x.slug === slug);
    if (!t) return;
    const newTitle = window.prompt("Edit Talk Title:", t.title);
    if (newTitle === null) return;
    const newVenue = window.prompt("Edit Event / Venue:", t.venue);
    if (newVenue === null) return;
    setTalkStatus(slug, t.status || "keep", {
      title: newTitle.trim() || t.title,
      venue: newVenue.trim() || t.venue,
    });
  }

  function refreshModalHeader(t) {
    const isExcluded = (t.status || "keep") === "exclude";
    els.modalBadges.innerHTML = `
      <span class="badge badge-fmt-${escapeHtml(t.primary_format)}">${escapeHtml(t.primary_format)}</span>
      <span class="badge">${escapeHtml(categoryLabel(t.category))}</span>
      <span class="badge">${escapeHtml(t.year)}</span>
      ${t.slide_count ? `<span class="badge">${escapeHtml(t.slide_count)} slides</span>` : ""}
      ${
        isExcluded
          ? `<span class="badge" style="border-color:#ef4444;color:#fca5a5;">✕ EXCLUDED</span>`
          : `<span class="badge" style="border-color:#10b981;color:#6ee7b7;">✓ KEPT</span>`
      }
    `;
    els.modalTitle.textContent = t.title;
    els.modalVenue.textContent = `${t.venue} (${t.year}) — Source file: ${t.primary_file}`;
    if (els.modalKeepBtn && els.modalExcludeBtn) {
      els.modalKeepBtn.classList.toggle("is-active", !isExcluded);
      els.modalExcludeBtn.classList.toggle("is-active", isExcluded);
    }
  }

  function openModal(slug) {
    const t = talks.find((x) => x.slug === slug);
    if (!t) return;
    state.activeModalSlug = slug;

    refreshModalHeader(t);
    if (els.modalCurationControls) {
      els.modalCurationControls.hidden = !state.curationEnabled;
    }

    els.modalPdfFrame.src = t.pdf_path ? `${t.pdf_path}${CACHE_BUST}#view=Fit` : "about:blank";

    const dlItems = [];
    if (t.pdf_path) {
      dlItems.push(
        `<a class="btn btn-primary" href="${escapeHtml(t.pdf_path + CACHE_BUST)}" target="_blank" rel="noopener">Open Archival PDF in New Tab</a>`
      );
    }
    if (t.primary_path) {
      dlItems.push(
        `<a class="btn" href="${escapeHtml(resolveOriginalUrl(t.primary_path))}" download>Download Untouched Original (${escapeHtml(t.primary_file)}, ${formatSize(t.primary_size_kb)})</a>`
      );
    }
    els.modalDownloads.innerHTML = dlItems.join("");

    if (t.drafts && t.drafts.length > 0) {
      els.modalDraftsSection.hidden = false;
      els.modalDrafts.innerHTML = t.drafts
        .map(
          (d) =>
            `<a class="btn" href="${escapeHtml(resolveOriginalUrl(d.path))}" download>${escapeHtml(d.name)} (${formatSize(d.size_kb)})</a>`
        )
        .join("");
    } else {
      els.modalDraftsSection.hidden = true;
    }

    if (t.media && t.media.length > 0) {
      els.modalMediaSection.hidden = false;
      els.modalMedia.innerHTML = t.media
        .map(
          (m) =>
            `<a class="btn" href="${escapeHtml(resolveOriginalUrl(m.path))}" download>🎬 ${escapeHtml(m.name)} (${formatSize(m.size_kb)})</a>`
        )
        .join("");
    } else {
      els.modalMediaSection.hidden = true;
    }

    if (t.summary_snippet) {
      els.modalSnippetSection.hidden = false;
      els.modalSnippet.textContent = t.summary_snippet;
      els.modalNotesLink.href = `talks/${t.slug}/notes.md`;
    } else {
      els.modalSnippetSection.hidden = true;
    }

    els.modal.hidden = false;
    els.modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function stepModal(delta) {
    if (!state.activeModalSlug) return;
    const ordered = getFilteredOrderedTalks();
    if (!ordered.length) return;
    const idx = ordered.findIndex((t) => t.slug === state.activeModalSlug);
    const nextIdx = idx < 0 ? 0 : (idx + delta + ordered.length) % ordered.length;
    openModal(ordered[nextIdx].slug);
  }

  function closeModal() {
    state.activeModalSlug = null;
    els.modal.hidden = true;
    els.modal.setAttribute("aria-hidden", "true");
    els.modalPdfFrame.src = "about:blank";
    document.body.style.overflow = "";
  }

  // Event listeners
  els.searchInput.addEventListener("input", (e) => {
    state.query = e.target.value.trim();
    render();
  });

  els.clearSearchBtn.addEventListener("click", () => {
    state.query = "";
    els.searchInput.value = "";
    render();
  });

  els.formatFilter.addEventListener("change", (e) => {
    state.format = e.target.value;
    render();
  });

  els.sortSelect.addEventListener("change", (e) => {
    state.sort = e.target.value;
    render();
  });

  els.categoryTabs.addEventListener("click", (e) => {
    const btn = e.target.closest(".tab-btn");
    if (!btn) return;
    els.categoryTabs.querySelectorAll(".tab-btn").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    state.category = btn.dataset.category;
    render();
  });

  els.eraPills.addEventListener("click", (e) => {
    const btn = e.target.closest(".pill");
    if (!btn) return;
    els.eraPills.querySelectorAll(".pill").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    state.era = btn.dataset.era;
    render();
  });

  els.tagPills.addEventListener("click", (e) => {
    const btn = e.target.closest(".pill");
    if (!btn) return;
    els.tagPills.querySelectorAll(".pill").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    state.tag = btn.dataset.tag;
    render();
  });

  if (els.curationStatusPills) {
    els.curationStatusPills.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-cstatus]");
      if (!btn) return;
      els.curationStatusPills
        .querySelectorAll(".curation-stat-pill")
        .forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      state.cstatus = btn.dataset.cstatus;
      render();
    });
  }

  if (els.bulkExcludeCoursesBtn) {
    els.bulkExcludeCoursesBtn.addEventListener("click", () => {
      const slugs = talks.filter((t) => t.category === "course").map((t) => t.slug);
      bulkSetStatus(slugs, "exclude");
    });
  }

  if (els.bulkExcludeGrantsBtn) {
    els.bulkExcludeGrantsBtn.addEventListener("click", () => {
      const slugs = talks.filter((t) => t.category === "grant").map((t) => t.slug);
      bulkSetStatus(slugs, "exclude");
    });
  }

  if (els.bulkExcludePostersBtn) {
    els.bulkExcludePostersBtn.addEventListener("click", () => {
      const slugs = talks.filter((t) => t.category === "poster").map((t) => t.slug);
      bulkSetStatus(slugs, "exclude");
    });
  }

  if (els.bulkExcludeShortBtn) {
    els.bulkExcludeShortBtn.addEventListener("click", () => {
      const slugs = talks.filter((t) => (t.slide_count || 0) <= 3).map((t) => t.slug);
      bulkSetStatus(slugs, "exclude");
    });
  }

  if (els.bulkExcludeFilteredBtn) {
    els.bulkExcludeFilteredBtn.addEventListener("click", () => {
      const slugs = talks.filter(matchesFilters).map((t) => t.slug);
      bulkSetStatus(slugs, "exclude");
    });
  }

  if (els.bulkKeepFilteredBtn) {
    els.bulkKeepFilteredBtn.addEventListener("click", () => {
      const slugs = talks.filter(matchesFilters).map((t) => t.slug);
      bulkSetStatus(slugs, "keep");
    });
  }

  if (els.syncMdBtn) {
    els.syncMdBtn.addEventListener("click", async () => {
      try {
        const res = await fetch("/api/sync-md", { method: "POST" });
        const data = await res.json();
        if (data.ok && Array.isArray(data.talks)) {
          talks = data.talks;
          render();
          window.alert(`Synced ${data.updated} changes from CURATE_TALKS.md!`);
        }
      } catch (err) {
        console.error(err);
      }
    });
  }

  if (els.purgeExcludedBtn) {
    els.purgeExcludedBtn.addEventListener("click", async () => {
      const exclCount = talks.filter((t) => (t.status || "keep") === "exclude").length;
      if (exclCount === 0) return;
      const ok = window.confirm(
        `Remove ${exclCount} excluded presentations from this archive repository (talks/ and data/talks.json)?\n\n(Your original files outside talk_archive are never touched.)`
      );
      if (!ok) return;
      try {
        const res = await fetch("/api/purge-excluded", { method: "POST" });
        const data = await res.json();
        if (data.ok) {
          talks = talks.filter((t) => (t.status || "keep") !== "exclude");
          state.cstatus = "all";
          render();
          window.alert(`Removed ${data.removed_count} excluded entries. ${data.remaining_total} presentations remain in the archive.`);
        }
      } catch (err) {
        console.error(err);
      }
    });
  }

  els.resetFiltersBtn.addEventListener("click", () => {
    state.query = "";
    state.category = "all";
    state.era = "all";
    state.tag = "all";
    state.format = "all";
    state.cstatus = "all";
    els.searchInput.value = "";
    els.formatFilter.value = "all";
    els.categoryTabs.querySelectorAll(".tab-btn").forEach((b) => b.classList.toggle("active", b.dataset.category === "all"));
    els.eraPills.querySelectorAll(".pill").forEach((b) => b.classList.toggle("active", b.dataset.era === "all"));
    els.tagPills.querySelectorAll(".pill").forEach((b) => b.classList.toggle("active", b.dataset.tag === "all"));
    if (els.curationStatusPills) {
      els.curationStatusPills
        .querySelectorAll(".curation-stat-pill")
        .forEach((b) => b.classList.toggle("active", b.dataset.cstatus === "all"));
    }
    render();
  });

  if (els.timelineRail) {
    els.timelineRail.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-jump-year]");
      if (!btn) return;
      const yr = btn.dataset.jumpYear;
      setActiveRailYear(yr);
      const sec = document.getElementById(`year-section-${yr}`);
      if (sec) {
        sec.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  }

  els.talksTimeline.addEventListener("click", (e) => {
    const curateBtn = e.target.closest("[data-curate-slug]");
    if (curateBtn) {
      e.stopPropagation();
      setTalkStatus(curateBtn.dataset.curateSlug, curateBtn.dataset.curateStatus);
      return;
    }
    const editBtn = e.target.closest("[data-edit-slug]");
    if (editBtn) {
      e.stopPropagation();
      promptEditTalk(editBtn.dataset.editSlug);
      return;
    }
    const trigger = e.target.closest("[data-open-slug]");
    if (!trigger) return;
    openModal(trigger.dataset.openSlug);
  });

  if (els.modalPrevBtn) els.modalPrevBtn.addEventListener("click", () => stepModal(-1));
  if (els.modalNextBtn) els.modalNextBtn.addEventListener("click", () => stepModal(1));
  if (els.modalKeepBtn) {
    els.modalKeepBtn.addEventListener("click", () => {
      if (!state.activeModalSlug) return;
      const slug = state.activeModalSlug;
      stepModal(1);
      setTalkStatus(slug, "keep");
    });
  }
  if (els.modalExcludeBtn) {
    els.modalExcludeBtn.addEventListener("click", () => {
      if (!state.activeModalSlug) return;
      const slug = state.activeModalSlug;
      stepModal(1);
      setTalkStatus(slug, "exclude");
    });
  }
  if (els.modalEditTitleBtn) {
    els.modalEditTitleBtn.addEventListener("click", () => {
      if (state.activeModalSlug) promptEditTalk(state.activeModalSlug);
    });
  }

  els.closeModalBtn.addEventListener("click", closeModal);
  els.modal.addEventListener("click", (e) => {
    if (e.target === els.modal) closeModal();
  });
  document.addEventListener("keydown", (e) => {
    if (els.modal.hidden) return;
    if (e.key === "Escape") {
      closeModal();
    } else if (e.key === "ArrowRight") {
      stepModal(1);
    } else if (e.key === "ArrowLeft") {
      stepModal(-1);
    } else if (state.curationEnabled && (e.key === "k" || e.key === "K")) {
      const slug = state.activeModalSlug;
      stepModal(1);
      setTalkStatus(slug, "keep");
    } else if (state.curationEnabled && (e.key === "x" || e.key === "X")) {
      const slug = state.activeModalSlug;
      stepModal(1);
      setTalkStatus(slug, "exclude");
    }
  });

  async function detectCurationServer() {
    try {
      const res = await fetch("/api/status", { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        if (data && data.curation_enabled) {
          state.curationEnabled = true;
          if (els.curationBanner) els.curationBanner.hidden = false;
          render();
        }
      }
    } catch (_) {
      // Static mode (e.g. GitHub Pages)
    }
  }

  initStatsAndTags();
  render();
  detectCurationServer();
})();
