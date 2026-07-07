#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADLIB_SOURCE_DIR="${1:-$ROOT/../RADLib}"

if [ ! -f "$RADLIB_SOURCE_DIR/docs/Doxyfile" ]; then
    echo "RADLib Doxyfile not found under: $RADLIB_SOURCE_DIR" >&2
    exit 2
fi

mkdir -p "$ROOT/docs/radlib"

RADLIB_SOURCE_DIR="$RADLIB_SOURCE_DIR" \
RADLIB_DOCS_OUTPUT="$ROOT/docs/radlib" \
    doxygen "$RADLIB_SOURCE_DIR/docs/Doxyfile"

echo "Updated RADLib Doxygen docs at docs/radlib/api/index.html"
