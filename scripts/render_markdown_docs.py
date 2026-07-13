#!/usr/bin/env python3
"""Render selected Markdown docs into the RadicalPackages static site."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RADBUILD_DOCS = ROOT / "docs" / "radbuild" / "0.2.1"


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def render_markdown(source: Path) -> str:
    lines = source.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_open = False
    code_open = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_open
        if list_open:
            out.append("</ul>")
            list_open = False

    for line in lines:
        if line.startswith("```"):
            if code_open:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                code_open = False
            else:
                flush_paragraph()
                close_list()
                code_open = True
            continue
        if code_open:
            code_lines.append(line)
            continue
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            close_list()
            continue
        if stripped.startswith("#"):
            flush_paragraph()
            close_list()
            hashes = len(stripped) - len(stripped.lstrip("#"))
            level = min(max(hashes, 1), 4)
            text = stripped[hashes:].strip()
            out.append(f"<h{level}>{inline_markdown(text)}</h{level}>")
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            if not list_open:
                out.append("<ul>")
                list_open = True
            out.append(f"<li>{inline_markdown(stripped[2:])}</li>")
            continue
        paragraph.append(stripped)

    flush_paragraph()
    close_list()
    if code_open:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(out)


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="../../../assets/site.css">
</head>
<body>
<main class="page">
  <nav class="nav">
    <a class="brand" href="../../../"><img src="../../../assets/rad-logo.png" alt="">Radical Packages</a>
    <div class="nav-links">
      <a href="../../../">Home</a>
      <a href="../../../packages.html">Packages</a>
      <a href="../../../radix-os.html">RADix OS</a>
      <a href="../../../docs/">Docs</a>
    </div>
  </nav>
  <section class="hero compact-hero">
    <div class="eyebrow">RadBuild 0.2.1</div>
    <h1>{html.escape(title)}</h1>
  </section>
  <article class="card doc-content">
{body}
  </article>
</main>
</body>
</html>
"""


def main() -> int:
    for name, title in [
        ("RADBUILD_V2.md", "RadBuild Graph Framework"),
        ("USAGE.md", "RadBuild CLI Usage"),
        ("README.md", "RadBuild Repository README"),
    ]:
        source = RADBUILD_DOCS / name
        target = source.with_suffix(".html")
        target.write_text(page(title, render_markdown(source)), encoding="utf-8")
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
