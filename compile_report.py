#!/usr/bin/env python3
import re
from pathlib import Path

FILES = [
    "0_title_page.md",
    "1_introduction.md",
    "2_background.md",
    "3_methodology.md",
    "4_solution.md",
    "5_discussion.md",
    "6_references.md",
    "appendix.md",
]

def slugify(h):
    s = h.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s

def extract_headings(md_text):
    headings = []
    for line in md_text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            headings.append((level, text, slugify(text)))
    return headings

def build_toc(headings, max_level=3):
    toc = []
    for level, text, anchor in headings:
        if level <= max_level:
            indent = "  " * (level - 1)
            toc.append(f"{indent}- [{text}](#{anchor})")
    return "\n".join(toc)

def main():
    here = Path(__file__).parent
    body_parts = []

    for fname in FILES:
        p = here / fname
        if not p.exists():
            raise FileNotFoundError(f"Missing section file: {fname}")
        body_parts.append(p.read_text(encoding="utf-8").strip())

    # join without title because TOC comes after title
    title = body_parts[0]
    content = "\n\n\n".join(body_parts[1:])

    # extract headings from all sections except the title
    headings = extract_headings(content)
    toc = build_toc(headings, max_level=3)

    merged = [
        title,
        "## Table of Contents",
        "",
        toc,
        "",
        content,
    ]

    out = here / "report_merged.md"
    out.write_text("\n".join(merged), encoding="utf-8")
    print(f"✅ Built {out.name} with title, TOC, and merged content.")

if __name__ == "__main__":
    main()
