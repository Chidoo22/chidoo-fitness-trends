# Chido's Workspace — Master Navigator

## Who This Is For
This is Chido's personal AI workspace on Windows. Focus areas:
1. **Data & Dashboards** — Power BI (.pbip/.pbir), Excel, DAX, Tableau-style interactive dashboards
2. **Website Creation** — landing pages, business sites, web components
3. **Copywriting** — website copy, headlines, bios, CTAs for web/apps
4. **Spreadsheets** — Excel workbooks, formulas, data analysis, financial models
5. **SQL & Data** — queries, schema exploration, database work

---

## How to Operate

### Before every task:
1. Check the Skills Inventory below — pick the right skill
2. Check `projects/` for any existing work on this topic
3. Save all outputs to the correct `projects/` subfolder

### Output locations:
| What | Save To |
|------|---------|
| Power BI files, dashboards, DAX | `projects/dashboards/` |
| HTML/interactive dashboards | `projects/dashboards/` |
| Websites, landing pages | `projects/websites/` |
| Copy, headlines, bios | `projects/copy/` |
| Excel/XLSX files | `projects/dashboards/` |
| SQL scripts | `projects/dashboards/` |

### Rules:
- Never add features not asked for
- Always save output files — don't just show them in chat
- For data: ask what business question the data answers FIRST
- For websites: ask what the visitor should DO on the page FIRST
- For copy: ask who the audience is FIRST
- API keys live in `.env` only — never hardcode
- As Chido adds books/PDFs/transcripts to `01-KNOWLEDGE/`, read them before starting related tasks

### MANDATORY — Missing Skill or Knowledge Rule
**Before starting ANY task**, check if the required skill exists in `.claude/skills/`.
If a task needs a skill, style reference, library knowledge, or resource that is NOT already installed:

> STOP. Tell Jabril/Chido exactly what is missing and where to get it:
> - "I need to go to GitHub to find a [X] skill — can I search for it now?"
> - "This task needs [book/PDF/reference] — please add it to `01-KNOWLEDGE/` first"
> - "I don't have a skill for [X] yet — let me search online for the right one"

**Never guess or wing it on a missing skill. Always flag it first.**

---

## Skills Inventory

| Skill | Folder | Source | Invoke When |
|-------|--------|--------|-------------|
| **data-analytics** | `.claude/skills/data-analytics/` | Custom | General data questions, Tableau-style charts, KPI dashboards (HTML), DAX guidance |
| **pbi-report-builder** | `.claude/skills/data-analytics/pbi-report-builder.md` | [lukasreese/powerbi-claude-skills](https://github.com/lukasreese/powerbi-claude-skills) | Power BI PBIP/PBIR — adding pages, visuals, KPI cards, IBCS variance charts |
| **xlsx** | `.claude/skills/xlsx/` | [anthropics/skills](https://github.com/anthropics/skills) (official) | Any .xlsx/.csv/.tsv task — create, edit, analyze spreadsheets, Excel formulas |
| **sql-assistant** | `.claude/skills/sql-assistant/` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | SQL queries, schema exploration, migrations, ORMs (Prisma, SQLAlchemy) |
| **website-builder** | `.claude/skills/website-builder/` | Custom | Business websites, portfolio, multi-section HTML sites |
| **frontend-design** | `.claude/skills/frontend-design/` | [anthropics/claude-code](https://github.com/anthropics/claude-code) (official) | Web components, UI, avoiding generic AI aesthetics |
| **frontend-landings** | `.claude/skills/frontend-landings/` | [auwalmusa](https://github.com/auwalmusa/frontend-landings-claude-skill) | Single-file animated HTML landing pages (10 style presets) |
| **copywriting** | `.claude/skills/copywriting/` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Website copy, headlines, CTAs, landing page copy, about pages |

### Skill Routing Quick Guide
- "Create a Power BI report / add visuals" → **pbi-report-builder**
- "Build a dashboard" (no Power BI) → **data-analytics** (HTML/JS output)
- "DAX formula / Power BI question" → **data-analytics** + **pbi-report-builder**
- "Edit/create an Excel file" → **xlsx**
- "SQL query / database" → **sql-assistant**
- "Build a landing page / marketing page" → **frontend-landings**
- "Build a website / multi-page site" → **website-builder**
- "Build a UI component / web UI" → **frontend-design**
- "Write copy / headlines / about page" → **copywriting**

---

## Folder Map

```
Chidoo_Worskspace/
├── CLAUDE.md                                   ← YOU ARE HERE
├── .env                                        ← API keys (never share)
├── .gitignore
│
├── .claude/
│   ├── settings.json                           ← Permissions
│   └── skills/
│       ├── data-analytics/
│       │   ├── SKILL.md                        ← General data/dashboards
│       │   └── pbi-report-builder.md           ← Power BI PBIR (GitHub)
│       ├── xlsx/
│       │   └── SKILL.md                        ← Excel/spreadsheets (Anthropic official)
│       ├── sql-assistant/
│       │   └── SKILL.md                        ← SQL queries & databases
│       ├── website-builder/
│       │   └── SKILL.md                        ← Full websites
│       ├── frontend-design/
│       │   └── SKILL.md                        ← Web UI (Anthropic official)
│       ├── frontend-landings/
│       │   ├── SKILL.md                        ← Animated landing pages
│       │   └── references/STYLE_PRESETS.md     ← 10 design presets
│       └── copywriting/
│           └── SKILL.md                        ← Web copy (GitHub)
│
├── projects/                                   ← ALL WORK OUTPUT
│   ├── dashboards/                             ← Power BI, Excel, HTML dashboards
│   ├── websites/                               ← HTML site files
│   └── copy/                                   ← Written copy
│
├── 01-KNOWLEDGE/                               ← Reference library (add books/PDFs here)
│   ├── data-analytics/
│   │   ├── power-bi/                           ← Power BI docs, best practices
│   │   ├── tableau/                            ← Tableau concepts
│   │   └── dax-formulas/                       ← DAX library
│   ├── copywriting-prompts/
│   │   ├── templates/
│   │   └── frameworks/
│   └── website-references/
│
├── 03-TOOLS/                                   ← Reusable prompts
│   └── master-prompts/
├── tools/                                      ← Python scripts
├── images/                                     ← Image assets
└── prompts/                                    ← Saved prompt library
```

---

## Knowledge Base — Adding Content
When Chido adds books, PDFs, transcripts, or notes to `01-KNOWLEDGE/`:
- Place Power BI/Tableau/data books in `01-KNOWLEDGE/data-analytics/`
- Place website/design references in `01-KNOWLEDGE/website-references/`
- Place copy frameworks/books in `01-KNOWLEDGE/copywriting-prompts/`
- I will read these files before starting any related task

**Books that would significantly enhance skills** (for future reference):
- *Storytelling with Data* (Knaflic) → data viz best practices
- *The Definitive Guide to DAX* (Ferrari & Russo) → Power BI DAX mastery
- *Don't Make Me Think* (Krug) → web UX/design
- *Everybody Writes* (Handley) → web copywriting
- *Data Smart* (Foreman) → data analysis thinking

---

## API Keys (.env)
```
ANTHROPIC_API_KEY=        # Claude API (if building apps)
```

---

## Chido's Actual Work (From ZIP Archive)

| Project | Location | Status |
|---------|----------|--------|
| **Fitness Dashboard** | `projects/dashboards/fitness-dashboard/fitness_dashboard.html` | Active — Plotly.js, Apple Health data, glassmorphic dark/light mode |
| **Fitness Dashboard v2** | `projects/dashboards/fitness-dashboard/fitness_dashboard_v2.html` | Newer version |
| **Weight Model** | `projects/dashboards/weight-model/` | Plotly.js weight tracking + prediction |
| **How-To Guide** | `projects/dashboards/fitness-dashboard/How-To-Update-Your-Dashboard.html` | Guide: iPhone Health export → dashboard update |
| **SQL Practice** | `projects/sql-practice/practice.sql` | Learning SQL — parks_and_recreation DB |

### Dashboard Tech Stack
- **Plotly.js** (CDN) — all charts
- **Single-file HTML** — opens by double-clicking, no server needed
- **JSON data** — fitness_data.json, weight_model_data.json
- **Apple Health** — data source (iPhone export → ZIP → JSON)
- **Glassmorphic design** — dark/light mode, CSS variables, animated blobs, Inter font

---

## Current Focus
> Update this section when starting a new project.
- Main project: Fitness Dashboard (Plotly.js, Apple Health data)
- Learning: SQL (parks_and_recreation practice DB)
- Next: Add books/PDFs to `01-KNOWLEDGE/` to enhance skill knowledge
