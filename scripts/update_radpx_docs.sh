#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADPX_SOURCE_DIR="${1:-$ROOT/../RADPx-OS}"
RADPX_DOC_VERSION="${2:-${RADPX_DOC_VERSION:-0.1.4}}"

if [ ! -f "$RADPX_SOURCE_DIR/docs/Doxyfile" ]; then
    echo "RADPx-OS Doxyfile not found under: $RADPX_SOURCE_DIR" >&2
    exit 2
fi

DOC_OUTPUT="$ROOT/docs/radpx-os/$RADPX_DOC_VERSION"
mkdir -p "$DOC_OUTPUT"

RAD_SOURCE_DIR="$RADPX_SOURCE_DIR" \
RAD_DOCS_OUTPUT="$DOC_OUTPUT" \
    doxygen "$RADPX_SOURCE_DIR/docs/Doxyfile"

echo "Updated RADPx-OS Doxygen docs at docs/radpx-os/$RADPX_DOC_VERSION/api/index.html"
