#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADHDL_SOURCE_DIR="${1:-$ROOT/../RadHDL}"
RADHDL_DOC_VERSION="${2:-${RADHDL_DOC_VERSION:-current}}"
RADHDL_DOC_OUTPUT="$ROOT/docs/radhdl/$RADHDL_DOC_VERSION"
RADHDL_DOCGEN="${RADHDL_DOCGEN:-$RADHDL_SOURCE_DIR/scripts/radhdl_docgen.py}"

if [[ ! -x "$RADHDL_DOCGEN" && ! -f "$RADHDL_DOCGEN" ]]; then
  if command -v radhdl-docgen >/dev/null 2>&1; then
    RADHDL_DOCGEN="$(command -v radhdl-docgen)"
  else
    echo "radhdl-docgen not found. Set RADHDL_DOCGEN or install radbuild-radhdl." >&2
    exit 1
  fi
fi

rm -rf "$RADHDL_DOC_OUTPUT"
mkdir -p "$RADHDL_DOC_OUTPUT"

DOCGEN_ARGS=(build --radhdl "$RADHDL_SOURCE_DIR" --out "$RADHDL_DOC_OUTPUT")
if [[ "${RADHDL_DOCGEN_RUN_SIMS:-0}" == "1" ]]; then
  DOCGEN_ARGS+=(--run-sims)
fi
if [[ -n "${RADHDL_DOCGEN_STOP_TIME:-}" ]]; then
  DOCGEN_ARGS+=(--stop-time "$RADHDL_DOCGEN_STOP_TIME")
fi

if [[ "$RADHDL_DOCGEN" == *.py ]]; then
  python3 "$RADHDL_DOCGEN" "${DOCGEN_ARGS[@]}"
else
  "$RADHDL_DOCGEN" "${DOCGEN_ARGS[@]}"
fi

cat > "$ROOT/docs/radhdl/index.html" <<'HTML'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>RadHDL Documentation</title>
</head>
<body>
  <h1>RadHDL Documentation</h1>
  <ul>
    <li><a href="current/">Current RadHDL Documentation</a></li>
  </ul>
</body>
</html>
HTML

echo "Updated RadHDL docs at docs/radhdl/$RADHDL_DOC_VERSION/index.html"
