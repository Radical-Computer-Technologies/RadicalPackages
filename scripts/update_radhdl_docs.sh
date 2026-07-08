#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADHDL_SOURCE_DIR="${1:-$ROOT/../RadHDL}"
RADHDL_DOC_VERSION="${2:-${RADHDL_DOC_VERSION:-current}}"
RADHDL_SOURCE_BUILD_DIR="$ROOT/docs_src/radhdl"
RADHDL_DOC_OUTPUT="$ROOT/docs/radhdl/$RADHDL_DOC_VERSION"

python3 "$ROOT/scripts/update_radhdl_docs.py" "$RADHDL_SOURCE_DIR" --source-dir "$RADHDL_SOURCE_BUILD_DIR"

rm -rf "$RADHDL_DOC_OUTPUT"
mkdir -p "$RADHDL_DOC_OUTPUT"
sphinx-build -b html -d "$RADHDL_SOURCE_BUILD_DIR/.doctrees" "$RADHDL_SOURCE_BUILD_DIR" "$RADHDL_DOC_OUTPUT"

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
