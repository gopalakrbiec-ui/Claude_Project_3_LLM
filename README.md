# 🚀 FrontierLLM Academy

**A free, interactive educational website about frontier AI and large language models.**

FrontierLLM Academy helps learners at every level — from curious beginners to ML researchers — explore how modern LLMs work, what's happening at the AI frontier, and how to think about the field from multiple professional perspectives.

🌐 **Live site:** [gopalakrbiec-ui.github.io/FrontierLLM-Academy](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy)

---

## What This Project Is

A static educational website (pure HTML/CSS/JS — no framework, no build step, no backend) organized around:

- **8 Learning Modes** — switch perspective between Layman, Graduate, Researcher, Startup, Investor, Founder, Team, and Agentic mode
- **Deep-dive pages** — curated content on timelines, AI ecosystems, and engineering concepts
- **A blog** — long-form posts with diagrams, animations, and interactive examples
- **Daily AI News** — a live feed of what's happening in the field

Everything is served as static files. No login, no tracking, no paywall.

---

## Site Structure

### 🏠 Home
- [Home](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy) — Landing page with learning mode selector, site overview, and featured content

### 🧭 Explore — Deep-Dive Resources
- [FrontierAI Timeline](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/frontier-timeline.html) — A chronological map of major frontier model releases, capability jumps, and research milestones
- [Future Frontier](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/future-frontier.html) — Forward-looking analysis of where AI capability and safety research is heading
- [LLM Engineering](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/llm-engineering.html) — Practical concepts for building with LLMs — prompting, fine-tuning, RAG, agents, evals
- [Coding Agents](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/coding-agents.html) — Deep dive on coding agents & tools: evolution timeline, tool comparisons, MCP ecosystem, SWE-bench, investments, research papers, and future roadmap

### 🌏 AI Ecosystems — Country Deep Dives
- [Sovereign AI](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/sovereign-ai.html) — Comprehensive guide to sovereign AI — all countries, investment strategies, Pax Silica, and the four pillars
- [America AI](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/usa-ai.html) — US AI policy, hyperscaler investments, leading labs, and the Stargate project
- [China AI](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/china-ai.html) — China's AI strategy, frontier labs, regulatory environment, and key models
- [Europe AI](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/europe-ai.html) — European AI landscape — Mistral, EU AI Act, country hubs, and the path to AI sovereignty
- [India AI](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/india-ai.html) — India's AI landscape — domestic models, government initiatives, startup ecosystem

### 📰 News & Blog
- [Daily AI News](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/ai-news.html) — Curated AI news feed updated regularly
- [Blog](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/pages/blog.html) — All blog posts — full listing with cards

---

## 📝 Blog Posts

<!-- BLOG_POSTS_START -->
- 🧬 [Multimodality & The Great Consolidation ⭐](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/multimodal-consolidation.html) — Multimodal AI, Architecture, Research · 2026-07-03 · 26 min
- 🎙️ [Voice & Speech AI Models: The Complete Guide](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/voice-ai-models.html) — Speech AI, Audio, Deep Dive · 2026-07-01 · 24 min
- 🎨 [Image & Video AI Models: The Complete Guide](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/image-video-ai-models.html) — Generative AI, Computer Vision, Deep Dive · 2026-06-30 · 25 min
- 🎬 [The Complete Filmmaking Encyclopedia](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/filmmaking-encyclopedia.html) — Filmmaking, Creative Industry, Encyclopedia · 2026-06-27 · 30 min
- 💰 [Frontier Model Pricing: The Complete Guide](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/frontier-model-pricing.html) — Economics, Business, Research · 2026-06-23 · 20 min
- 📰 [AI News Digest — June 22, 2026](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/ai-news-june-22-2026.html) — News, Weekly Digest · 2026-06-22 · 8 min
- ⚡ [Loop Engineering: The New Meta for AI Agents](https://gopalakrbiec-ui.github.io/FrontierLLM-Academy/blog/agentic-loop-explained.html) — Agentic AI, Research · 2026-06-22 · 16 min
<!-- BLOG_POSTS_END -->

---

## 🗂 File Structure

```
FrontierLLM-Academy/
├── index.html              ← Home page
├── styles.css              ← All CSS (single file)
├── app.js                  ← All JS (single file)
├── pages/                  ← All sub-pages
│   ├── blog.html           ← Blog listing
│   ├── frontier-timeline.html
│   ├── future-frontier.html
│   ├── llm-engineering.html
│   ├── ai-news.html
│   ├── india-ai.html
│   ├── china-ai.html
│   └── usa-ai.html
├── blog/                   ← Blog posts
│   ├── index.json          ← Post manifest (source of truth)
│   ├── _template.html      ← Copy to create a new post
│   └── [slug].html         ← Individual post files
├── docs/
│   └── CONTRIBUTING.md     ← How to add pages and blog posts
├── scripts/
│   └── update_readme.py    ← Auto-updates blog list above
└── CLAUDE.md               ← AI agent context file
```

---

## 🛠 Tech Stack

- **Pure HTML5 / CSS3 / Vanilla JS** — no framework, no bundler
- **GitHub Pages** — static hosting, zero config
- **GitHub Actions** — auto-updates the blog list in this README on every push

---

## ➕ Adding Content

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for step-by-step guides on:
- Adding a new blog post (copy template → fill in → add to `blog/index.json`)
- Adding a new page (copy existing page → update nav panels across all files)

When you push a new entry to `blog/index.json`, the GitHub Action automatically regenerates the blog list in this README.

---

## 🤖 Auto-Update

The **Blog Posts** list above is auto-generated from `blog/index.json` by `.github/workflows/update-readme.yml`. It runs on every push that touches `blog/index.json` or any `blog/*.html` file. No manual README edits needed when adding or removing posts.
