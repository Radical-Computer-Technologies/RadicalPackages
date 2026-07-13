#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADBUILD_SOURCE_DIR="${1:-$ROOT/../RadBuild}"
RADBUILD_DOC_VERSION="${2:-${RADBUILD_DOC_VERSION:-0.2.1}}"

SOURCE_DOCS="$RADBUILD_SOURCE_DIR/docs/radbuild/$RADBUILD_DOC_VERSION"

if [ ! -d "$SOURCE_DOCS" ]; then
    echo "Curated RadBuild docs not found under: $SOURCE_DOCS" >&2
    exit 2
fi

DOC_OUTPUT="$ROOT/docs/radbuild/$RADBUILD_DOC_VERSION"
rm -rf "$DOC_OUTPUT"
mkdir -p "$(dirname "$DOC_OUTPUT")"
cp -R "$SOURCE_DOCS" "$DOC_OUTPUT"
python3 "$ROOT/scripts/render_markdown_docs.py"
find "$DOC_OUTPUT" -name '*.md' -type f -delete

echo "Updated RadBuild docs at docs/radbuild/$RADBUILD_DOC_VERSION/index.html"
