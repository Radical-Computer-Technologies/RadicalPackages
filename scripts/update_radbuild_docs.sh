#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RADBUILD_SOURCE_DIR="${1:-$ROOT/../RadBuild}"
RADBUILD_DOC_VERSION="${2:-${RADBUILD_DOC_VERSION:-0.2.1}}"

if [ ! -f "$RADBUILD_SOURCE_DIR/docs/RADBUILD_V2.md" ]; then
    echo "RadBuild docs not found under: $RADBUILD_SOURCE_DIR" >&2
    exit 2
fi

DOC_OUTPUT="$ROOT/docs/radbuild/$RADBUILD_DOC_VERSION"
mkdir -p "$DOC_OUTPUT"

cp "$RADBUILD_SOURCE_DIR/docs/RADBUILD_V2.md" "$DOC_OUTPUT/RADBUILD_V2.md"
cp "$RADBUILD_SOURCE_DIR/README.md" "$DOC_OUTPUT/README.md"
cp "$RADBUILD_SOURCE_DIR/radbuild/USAGE.md" "$DOC_OUTPUT/USAGE.md"

cat >"$DOC_OUTPUT/index.html" <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RadBuild $RADBUILD_DOC_VERSION Documentation</title>
  <link rel="stylesheet" href="../../../assets/site.css">
</head>
<body>
<main class="page">
  <nav class="nav">
    <a class="brand" href="../../../"><img src="../../../assets/rad-logo.png" alt="">Radical Packages</a>
    <div class="nav-links">
      <a href="../../../packages.html">Packages</a>
      <a href="../">Docs</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Experimental Build Framework</div>
    <h1>RadBuild $RADBUILD_DOC_VERSION</h1>
    <p class="lead">
      Graph-based builds for FPGA, Linux, firmware, software, package, deployment, RADix-OS image, VSCode, and server workflows.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Suite:</strong> experimental</span>
      <span class="pill"><strong>Schema:</strong> 2.0</span>
      <span class="pill"><strong>JSON events:</strong> supported</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>RADix-OS Build</h2>
      <p>Use the <code>os.radix</code> system type and <code>radix-os</code> provider to build and smoke-test RADix-OS VM images.</p>
      <div class="command"><code>radbuild build os --settings settings.json --json-events</code></div>
    </article>
    <article class="card">
      <h2>IDE Integration</h2>
      <p>The VSCode command consumes line-delimited JSON events from the CLI and reads the same artifact manifest as other graph systems.</p>
      <div class="command"><code>radbuild build all --json-events</code></div>
    </article>
  </section>

  <section class="card">
    <h2>Source Documents</h2>
    <div class="links">
      <a class="link-card" href="RADBUILD_V2.md"><strong>Graph Framework</strong><span>Schema v2, providers, RADix-OS, packages, and VSCode notes.</span></a>
      <a class="link-card" href="USAGE.md"><strong>CLI Usage</strong><span>Legacy and source-tree command usage.</span></a>
      <a class="link-card" href="README.md"><strong>Repository README</strong><span>Repository layout and maintainer workflow.</span></a>
    </div>
  </section>
</main>
</body>
</html>
EOF

echo "Updated RadBuild docs at docs/radbuild/$RADBUILD_DOC_VERSION/index.html"
