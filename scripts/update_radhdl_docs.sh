#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADHDL_SOURCE_DIR="${1:-$ROOT/../RadHDL}"
RADHDL_DOC_VERSION="${2:-${RADHDL_DOC_VERSION:-0.2.0}}"
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
DOCGEN_ARGS+=(--theme "${RADHDL_DOCGEN_THEME:-dark}")
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
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RadHDL Documentation</title>
  <link rel="stylesheet" href="../../assets/site.css">
</head>
<body>
<main class="page">
  <nav class="nav">
    <a class="brand" href="../../">Radical Packages</a>
    <div class="nav-links">
      <a href="../../packages.html">Packages</a>
      <a href="../">Docs</a>
    </div>
  </nav>
  <section class="hero">
    <div class="eyebrow">RadHDL Documentation</div>
    <h1>RadHDL Documentation</h1>
    <p class="lead">Versioned datasheet documentation for RadHDL modules.</p>
  </section>
  <details class="doc-group">
    <summary>RadHDL Versions</summary>
    <details class="doc-release">
      <summary>Stable</summary>
      <p class="doc-note">No stable RadHDL documentation has been published yet.</p>
    </details>
    <details class="doc-release">
      <summary>Experimental</summary>
      <details class="doc-release">
        <summary>RadHDL 0 - Crimson</summary>
        <div class="links">
          <a class="link-card" href="0.2.1/"><strong>RadHDL 0.2.1</strong><span>Experimental HDL module datasheets, register maps, and simulation evidence</span></a>
          <a class="link-card" href="0.2.0/"><strong>RadHDL 0.2.0</strong><span>Experimental HDL module datasheets, register maps, and simulation evidence</span></a>
        </div>
      </details>
    </details>
  </details>
</main>
</body>
</html>
HTML

echo "Updated RadHDL docs at docs/radhdl/$RADHDL_DOC_VERSION/index.html"
