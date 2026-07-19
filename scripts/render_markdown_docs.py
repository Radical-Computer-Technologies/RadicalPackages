#!/usr/bin/env python3
"""Render curated Markdown docs into the RadicalPackages static site."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
RADBUILD_DOCS = ROOT / "docs" / "radbuild" / "0.2.1"


def local_doc_href(href: str) -> str:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return href
    path = parsed.path
    if path.endswith(".md"):
        path = path[:-3] + ".html"
    elif path.endswith("/index.md"):
        path = path[:-9]
    return urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, parsed.fragment))


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: f'<a href="{html.escape(local_doc_href(match.group(2)), quote=True)}">{match.group(1)}</a>',
        escaped,
    )
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


def markdown_title(source: Path) -> str:
    for line in source.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return source.stem.replace("-", " ").title()


def page(title: str, body: str, rel_root: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{rel_root}assets/site.css">
</head>
<body>
<main class="page">
  <nav class="nav">
    <a class="brand" href="{rel_root}"><img src="{rel_root}assets/rad-logo.png" alt="">Radical Packages</a>
    <div class="nav-links">
      <a href="{rel_root}">Home</a>
      <a href="{rel_root}packages.html">Packages</a>
      <a href="{rel_root}radpx-os.html">RADPx-OS</a>
      <a href="{rel_root}docs/">Docs</a>
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
    for source in sorted(RADBUILD_DOCS.rglob("*.md")):
        title = markdown_title(source)
        target = source.with_suffix(".html")
        depth = len(target.relative_to(ROOT).parents) - 1
        rel_root = "../" * depth
        target.write_text(page(title, render_markdown(source), rel_root), encoding="utf-8")
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
