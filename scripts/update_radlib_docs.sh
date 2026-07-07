#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADLIB_SOURCE_DIR="${1:-$ROOT/../RADLib}"
RADLIB_DOC_VERSION="${2:-${RADLIB_DOC_VERSION:-}}"

if [ ! -f "$RADLIB_SOURCE_DIR/docs/Doxyfile" ]; then
    echo "RADLib Doxyfile not found under: $RADLIB_SOURCE_DIR" >&2
    exit 2
fi

if [ -z "$RADLIB_DOC_VERSION" ]; then
    if [ -f "$RADLIB_SOURCE_DIR/buildconfig.json" ]; then
        major="$(grep -m1 '"major"' "$RADLIB_SOURCE_DIR/buildconfig.json" | sed -E 's/[^0-9]*([0-9]+).*/\1/')"
        minor="$(grep -m1 '"minor"' "$RADLIB_SOURCE_DIR/buildconfig.json" | sed -E 's/[^0-9]*([0-9]+).*/\1/')"
        patch="$(grep -m1 '"patch"' "$RADLIB_SOURCE_DIR/buildconfig.json" | sed -E 's/[^0-9]*([0-9]+).*/\1/')"
        if [ -n "$major" ] && [ -n "$minor" ] && [ -n "$patch" ]; then
            RADLIB_DOC_VERSION="$major.$minor.$patch"
        fi
    fi
fi

if [ -z "$RADLIB_DOC_VERSION" ]; then
    echo "RADLib documentation version was not provided and could not be detected." >&2
    echo "usage: $0 /path/to/RADLib <version>" >&2
    exit 2
fi

DOC_OUTPUT="$ROOT/docs/radlib/$RADLIB_DOC_VERSION"
mkdir -p "$DOC_OUTPUT"

RADLIB_SOURCE_DIR="$RADLIB_SOURCE_DIR" \
RADLIB_DOCS_OUTPUT="$DOC_OUTPUT" \
    doxygen "$RADLIB_SOURCE_DIR/docs/Doxyfile"

echo "Updated RADLib Doxygen docs at docs/radlib/$RADLIB_DOC_VERSION/api/index.html"
