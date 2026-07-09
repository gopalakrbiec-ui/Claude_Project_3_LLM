# FrontierAIModels Academy — Claude Agent Context

## Project Type
Static educational website. No build step, no framework, no backend.
All pages are plain HTML/CSS/JS served as files.

## File Structure
```
FrontierAIModels-Academy/
├── index.html              ← Home page (stays in root, always)
├── styles.css              ← All CSS (single file)
├── app.js                  ← All JS (single file)
├── pages/                  ← All sub-pages live here
│   ├── blog.html
│   ├── frontier-timeline.html
│   ├── future-frontier.html
│   ├── llm-engineering.html
│   ├── ai-news.html
│   ├── india-ai.html
│   ├── china-ai.html
│   └── usa-ai.html
├── blog/                   ← Blog posts + manifest
│   ├── index.json          ← Post manifest (source of truth for all blog UI)
│   ├── _template.html      ← Copy this to create a new post
│   └── [slug].html         ← Individual post files
└── docs/
    └── CONTRIBUTING.md     ← How to add pages and posts
```

## Path Rules (critical)
| File location | styles.css | app.js | index.html | Other pages |
|---|---|---|---|---|
| `index.html` (root) | `styles.css` | `app.js` | — | `pages/foo.html` |
| `pages/*.html` | `../styles.css` | `../app.js` | `../index.html` | `foo.html` (same dir) |
| `blog/*.html` | `../styles.css` | `../app.js` | `../index.html` | `../pages/foo.html` |

## Navbar Architecture
Two-ribbon fixed navbar:
- Ribbon 1 (`.navbar-brand`, 46px): indigo gradient, logo only
- Ribbon 2 (`.navbar-main`, 48px): white, 4 tab buttons + 1 direct link
- Total navbar height: **94px** — all pages set `padding-top: 94px` on first element after nav

Nav tabs open slide-down panels (`.nav-panel`) — NOT CSS hover dropdowns.
Panel JS lives in `app.js`: `initNavPanels()`, `closeAllNavPanels()`.
Backdrop (`#navBackdrop`) closes panels on click.

### Nav panels inserted after `</nav>` in every HTML file:
```html
<div class="nav-backdrop" id="navBackdrop"></div>
<div class="nav-panel-wrap" id="navPanelWrap">
  <div class="nav-panel" id="navPanel-mode">...</div>
  <div class="nav-panel" id="navPanel-explore">...</div>
  <div class="nav-panel" id="navPanel-ecosystems">...</div>
  <div class="nav-panel" id="navPanel-blog">...</div>
</div>
```

## Learning Modes
8 modes: layman, graduate, researcher, team, startup, investor, founder, agentmode.
- On `index.html`: mode buttons use `onclick="setMode('mode')"` with `id="modeBtn_mode"`
- On `pages/*.html` and `blog/*.html`: mode links use `href="../index.html?mode=X"` or `href="index.html?mode=X"`
- Mode state persisted via `sessionStorage('llm-mode')`
- URL param `?mode=X` read on load in `app.js`

## Blog System
- Manifest: `blog/index.json` — add entry here to publish a post
- Template: `blog/_template.html` — copy and fill in
- Nav Recent Posts: `loadBlogNavPosts()` in `app.js` — reads manifest, populates `#blogNavMenu`
- Blog listing page: `pages/blog.html` — reads manifest, renders cards

### blog/index.json schema:
```json
{
  "slug": "post-slug",
  "title": "Post Title",
  "excerpt": "One-two sentence summary.",
  "author": "Author Name",
  "authorInitials": "AN",
  "date": "2026-06-22",
  "readTime": "5 min",
  "tags": ["Tag1", "Tag2"],
  "emoji": "🧠",
  "featured": false
}
```
Only one post should have `"featured": true` at a time.

## CSS Conventions
- All CSS in `styles.css` — append new sections at the bottom with a banner comment
- CSS variables in `:root`: `--accent`, `--accent2`, `--accent3`, `--text`, `--border`, `--bg-card`, etc.
- Light theme only (no dark mode toggle)
- Mobile breakpoint at `768px`

## Adding a New Page
1. Copy an existing page from `pages/` as your template
2. Place the new file in `pages/`
3. Update the nav panel in ALL HTML files (use a Python bulk-replace script — see `docs/CONTRIBUTING.md`)
4. Paths: use `../styles.css`, `../app.js`, `../index.html` at top

## Git Branch
Active development branch: `claude/trusting-mendel-u9s1oh`
Remote: `gopalakrbiec-ui/Claude_Project_3_LLM` (also mirrors to `gopalakrbiec-ui/FrontierAIModels-Academy`)
