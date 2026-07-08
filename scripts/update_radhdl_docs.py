#!/usr/bin/env python3
"""Generate Sphinx source pages for RadHDL documentation."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import shutil


EXCLUDE_PARTS = {
    ".git",
    ".Xil",
    "build",
    "dist",
    "release",
    "sim",
    "xsim.dir",
    "ip_user_files",
    ".ip_user_files",
}

ENTITY_RE = re.compile(r"(?im)^\s*entity\s+([a-zA-Z][a-zA-Z0-9_]*)\s+is\b")
PACKAGE_RE = re.compile(r"(?im)^\s*package\s+(?!body\b)([a-zA-Z][a-zA-Z0-9_]*)\s+is\b")


@dataclass(frozen=True)
class HdlFile:
    rel: Path
    entities: tuple[str, ...]
    packages: tuple[str, ...]
    category: str


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDE_PARTS for part in path.parts)


def category_for(rel: Path) -> str:
    parts = rel.parts
    if "testbenches" in parts or rel.name.startswith("tb_"):
        return "testbenches"
    if parts[0] == "dsp":
        return "dsp"
    if parts[0] == "interfaces":
        return "interfaces"
    if parts[0] == "debug":
        return "debug"
    if parts[0] == "projects":
        return "projects"
    return "other"


def scan_hdl(root: Path) -> list[HdlFile]:
    files: list[HdlFile] = []
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in {".vhd", ".vhdl"}:
            continue
        rel = path.relative_to(root)
        if should_skip(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        entities = tuple(ENTITY_RE.findall(text))
        packages = tuple(PACKAGE_RE.findall(text))
        if entities or packages:
            files.append(HdlFile(rel=rel, entities=entities, packages=packages, category=category_for(rel)))
    return files


def scan_markdown(root: Path) -> list[Path]:
    docs: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if should_skip(rel):
            continue
        docs.append(rel)
    return docs


def scan_address_maps(root: Path) -> list[Path]:
    maps: list[Path] = []
    for path in sorted(root.rglob("*.json")):
        rel = path.relative_to(root)
        if should_skip(rel):
            continue
        if "address" in rel.name.lower() or "address_map" in rel.parts or rel.name.endswith(".radlib.json"):
            maps.append(rel)
    return maps


def title(text: str) -> str:
    return f"{text}\n{'=' * len(text)}\n\n"


def section(text: str) -> str:
    return f"{text}\n{'-' * len(text)}\n\n"


def page_name(category: str) -> str:
    return f"{category}.rst"


def write_inventory_page(path: Path, heading: str, files: list[HdlFile]) -> None:
    lines = [title(heading)]
    if not files:
        lines.append("No VHDL declarations were found in this group.\n")
        path.write_text("".join(lines), encoding="utf-8")
        return

    lines.append(".. list-table::\n")
    lines.append("   :header-rows: 1\n")
    lines.append("   :widths: 28 34 18 20\n\n")
    lines.append("   * - File\n")
    lines.append("     - Entity declarations\n")
    lines.append("     - Package declarations\n")
    lines.append("     - Group\n")
    for item in files:
        entity_text = ", ".join(f"``{entity}``" for entity in item.entities) or "-"
        package_text = ", ".join(f"``{package}``" for package in item.packages) or "-"
        lines.append(f"   * - ``{item.rel.as_posix()}``\n")
        lines.append(f"     - {entity_text}\n")
        lines.append(f"     - {package_text}\n")
        lines.append(f"     - {item.category}\n")
    lines.append("\n")
    path.write_text("".join(lines), encoding="utf-8")


def write_reference_page(path: Path, files: list[HdlFile]) -> None:
    lines = [title("VHDL Autodoc Reference")]
    lines.append(
        "This page uses ``sphinx-vhdl`` autodoc directives over the current RadHDL source tree. "
        "Output quality improves as VHDL entities and packages gain structured ``--`` comments.\n\n"
    )

    packages = sorted({pkg for item in files for pkg in item.packages}, key=str.lower)
    entities = sorted({entity for item in files for entity in item.entities}, key=str.lower)

    if packages:
        lines.append(section("Packages"))
        for pkg in packages:
            lines.append(f".. vhdl:autopackage:: {pkg}\n\n")

    if entities:
        lines.append(section("Entities"))
        for entity in entities:
            lines.append(f".. vhdl:autoentity:: {entity}\n\n")

    path.write_text("".join(lines), encoding="utf-8")


def write_source_index(path: Path, markdown_files: list[Path], address_maps: list[Path]) -> None:
    lines = [title("Source Documentation Files")]
    lines.append("RadHDL source-side Markdown and address-map artifacts discovered during documentation generation.\n\n")

    lines.append(section("Markdown"))
    if markdown_files:
        for rel in markdown_files:
            lines.append(f"- ``{rel.as_posix()}``\n")
    else:
        lines.append("- None discovered.\n")

    lines.append("\n")
    lines.append(section("Address Maps"))
    if address_maps:
        for rel in address_maps:
            lines.append(f"- ``{rel.as_posix()}``\n")
    else:
        lines.append("- None discovered.\n")

    path.write_text("".join(lines), encoding="utf-8")


def write_conf(path: Path, radhdl_root: Path) -> None:
    text = f"""project = "RadHDL"
author = "Radical Computer Technologies"
extensions = ["myst_parser", "sphinxvhdl.vhdl"]
templates_path = []
exclude_patterns = ["_build"]
html_theme = "alabaster"
html_title = "RadHDL Documentation"
vhdl_autodoc_source_path = {str(radhdl_root)!r}
"""
    path.write_text(text, encoding="utf-8")


def write_index(path: Path, files: list[HdlFile], markdown_files: list[Path], address_maps: list[Path]) -> None:
    category_counts: dict[str, int] = {}
    for item in files:
        category_counts[item.category] = category_counts.get(item.category, 0) + 1
    entities = sum(len(item.entities) for item in files)
    packages = sum(len(item.packages) for item in files)
    categories = ["dsp", "interfaces", "debug", "projects", "testbenches", "other"]

    lines = [title("RadHDL Documentation")]
    lines.append(
        "RadHDL is the HDL library layer distributed with RadBuild through the ``radbuild-radhdl`` Debian package. "
        "The package installs the catalog and source assets at ``/usr/share/radbuild/radhdl`` so RadBuild, VSCode, "
        "and generated documentation can use a stable source root.\n\n"
    )
    lines.append(section("Current Snapshot"))
    lines.append("- Source root used for this build: RadHDL checkout or packaged ``/usr/share/radbuild/radhdl`` tree.\n")
    lines.append(f"- VHDL files with declarations: **{len(files)}**\n")
    lines.append(f"- Entity declarations: **{entities}**\n")
    lines.append(f"- Package declarations: **{packages}**\n")
    lines.append(f"- Markdown source docs: **{len(markdown_files)}**\n")
    lines.append(f"- Address-map artifacts: **{len(address_maps)}**\n\n")

    lines.append(section("Library Areas"))
    for category in categories:
        count = category_counts.get(category, 0)
        if count:
            lines.append(f"- :doc:`{category}`: {count} VHDL files with declarations.\n")
    lines.append("\n")

    lines.append(".. toctree::\n")
    lines.append("   :maxdepth: 2\n\n")
    for category in categories:
        if category_counts.get(category, 0):
            lines.append(f"   {category}\n")
    lines.append("   autodoc\n")
    lines.append("   source-files\n")
    lines.append("\n")

    path.write_text("".join(lines), encoding="utf-8")


def generate(radhdl_root: Path, source_dir: Path) -> None:
    if not radhdl_root.exists():
        raise FileNotFoundError(f"RadHDL source directory not found: {radhdl_root}")
    if source_dir.exists():
        shutil.rmtree(source_dir)
    source_dir.mkdir(parents=True, exist_ok=True)

    files = scan_hdl(radhdl_root)
    markdown_files = scan_markdown(radhdl_root)
    address_maps = scan_address_maps(radhdl_root)

    write_conf(source_dir / "conf.py", radhdl_root)
    write_index(source_dir / "index.rst", files, markdown_files, address_maps)
    write_reference_page(source_dir / "autodoc.rst", files)
    write_source_index(source_dir / "source-files.rst", markdown_files, address_maps)

    names = {
        "dsp": "DSP Cores",
        "interfaces": "Interface Cores",
        "debug": "Debug Cores",
        "projects": "Project Top Levels",
        "testbenches": "Testbenches",
        "other": "Other HDL",
    }
    for category, heading in names.items():
        group = [item for item in files if item.category == category]
        if group:
            write_inventory_page(source_dir / page_name(category), heading, group)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate RadHDL Sphinx source files.")
    parser.add_argument("radhdl_source", type=Path, nargs="?", default=Path("../RadHDL"))
    parser.add_argument("--source-dir", type=Path, default=Path("docs_src/radhdl"))
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    radhdl_source = args.radhdl_source if args.radhdl_source.is_absolute() else (repo / args.radhdl_source)
    source_dir = args.source_dir if args.source_dir.is_absolute() else (repo / args.source_dir)
    generate(radhdl_source.resolve(), source_dir.resolve())
    print(f"Generated RadHDL Sphinx sources at {source_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
