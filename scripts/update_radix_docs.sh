#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADIX_SOURCE_DIR="${1:-$ROOT/../RADix-OS}"
RADIX_DOC_VERSION="${2:-${RADIX_DOC_VERSION:-0.1.0}}"

if [ ! -f "$RADIX_SOURCE_DIR/docs/Doxyfile" ]; then
    echo "RADix-OS Doxyfile not found under: $RADIX_SOURCE_DIR" >&2
    exit 2
fi

DOC_OUTPUT="$ROOT/docs/radix-os/$RADIX_DOC_VERSION"
mkdir -p "$DOC_OUTPUT"

RADIX_SOURCE_DIR="$RADIX_SOURCE_DIR" \
RADIX_DOCS_OUTPUT="$DOC_OUTPUT" \
    doxygen "$RADIX_SOURCE_DIR/docs/Doxyfile"

echo "Updated RADix-OS Doxygen docs at docs/radix-os/$RADIX_DOC_VERSION/api/index.html"
