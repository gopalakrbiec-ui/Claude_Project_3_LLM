#!/usr/bin/env python3
"""
Regenerates the Blog Posts table in README.md from blog/index.json.
Run manually or via GitHub Actions on every push.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
MANIFEST = ROOT / "blog" / "index.json"
README = ROOT / "README.md"
BASE_URL = "https://gopalakrbiec-ui.github.io/FrontierLLM-Academy"

MARKER_START = "<!-- BLOG_POSTS_START -->"
MARKER_END   = "<!-- BLOG_POSTS_END -->"

def build_table(posts):
    lines = [
        "| | Title | Tags | Date | Read |",
        "|---|---|---|---|---|",
    ]
    for p in posts:
        emoji  = p.get("emoji", "📝")
        title  = p.get("title", "Untitled")
        slug   = p.get("slug", "")
        tags   = ", ".join(p.get("tags", []))
        date   = p.get("date", "")
        rt     = p.get("readTime", "")
        url    = f"{BASE_URL}/blog/{slug}.html"
        featured = " ⭐" if p.get("featured") else ""
        lines.append(f"| {emoji} | [{title}{featured}]({url}) | {tags} | {date} | {rt} |")
    return "\n".join(lines)

def update_readme():
    with open(MANIFEST, encoding="utf-8") as f:
        data = json.load(f)
    posts = data.get("posts", [])

    with open(README, encoding="utf-8") as f:
        content = f.read()

    table = build_table(posts)
    new_block = f"{MARKER_START}\n{table}\n{MARKER_END}"

    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL
    )
    if not pattern.search(content):
        print("ERROR: markers not found in README.md")
        return 1

    updated = pattern.sub(new_block, content)
    with open(README, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"README updated — {len(posts)} post(s) written.")
    return 0

if __name__ == "__main__":
    raise SystemExit(update_readme())
