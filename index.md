<style>
:root {
  color-scheme: dark;
  --bg: #07090d;
  --panel: #10151d;
  --panel-2: #151c26;
  --text: #edf2f7;
  --muted: #a8b3c4;
  --line: #293241;
  --accent: #38d9a9;
  --accent-2: #5cc8ff;
  --warn: #ffd166;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

a {
  color: var(--accent-2);
}

.page {
  max-width: 1120px;
  margin: 0 auto;
  padding: 48px 22px 72px;
}

.hero {
  padding: 52px 0 34px;
  border-bottom: 1px solid var(--line);
}

.eyebrow {
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.11em;
  text-transform: uppercase;
}

h1 {
  margin: 12px 0 14px;
  color: var(--text);
  font-size: clamp(2.4rem, 5vw, 4.6rem);
  line-height: 0.98;
  letter-spacing: 0;
}

.lead {
  max-width: 780px;
  color: var(--muted);
  font-size: 1.12rem;
  line-height: 1.7;
}

.status-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 26px;
}

.pill {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 8px 12px;
  background: #0c1118;
  color: var(--muted);
  font-size: 0.92rem;
}

.pill strong {
  color: var(--text);
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  margin-top: 28px;
}

.card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  padding: 22px;
}

.card h2,
.card h3 {
  margin-top: 0;
  color: var(--text);
  letter-spacing: 0;
}

.card p,
.card li {
  color: var(--muted);
  line-height: 1.6;
}

.command {
  overflow-x: auto;
  border: 1px solid #223143;
  border-radius: 8px;
  background: #05070a;
  padding: 15px;
}

.command code {
  color: #dbeafe;
  white-space: pre;
}

.package-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
  margin-top: 14px;
}

.package {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel-2);
  padding: 13px;
}

.package code {
  color: var(--accent);
  font-weight: 700;
}

.links {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 12px;
}

.link-card {
  display: block;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel-2);
  padding: 15px;
  text-decoration: none;
}

.link-card strong {
  display: block;
  color: var(--text);
  margin-bottom: 5px;
}

.link-card span {
  color: var(--muted);
}

.note {
  border-left: 3px solid var(--warn);
  margin-top: 18px;
  padding: 10px 14px;
  background: #17150d;
  color: #f7e9bd;
}

@media (max-width: 860px) {
  .grid,
  .links,
  .package-list {
    grid-template-columns: 1fr;
  }

  .page {
    padding-top: 26px;
  }
}
</style>

<main class="page">
  <section class="hero">
    <div class="eyebrow">Radical Computer Technologies</div>
    <h1>Radical Packages</h1>
    <p class="lead">
      Debian package repository and documentation hub for RADLib, RADBard, and related Radical Computer Technologies releases.
      Stable packages stay pinned to known runtime lines; experimental packages move faster for active beta work.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Stable:</strong> RADLib 0.1.0</span>
      <span class="pill"><strong>Experimental:</strong> RADBard beta, future RADLib 0.1.1</span>
      <span class="pill"><strong>Architectures:</strong> amd64, arm64</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Stable Repository</h2>
      <p>Use stable for the current RADLib 0.1.0 release line.</p>
      <div class="command"><code>sudo tee /etc/apt/sources.list.d/radical-computer-technologies.sources &gt;/dev/null &lt;&lt;'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: stable
Components: main
Architectures: amd64 arm64
Trusted: yes
EOF

sudo apt update</code></div>
    </article>

    <article class="card">
      <h2>Experimental Repository</h2>
      <p>Use experimental for beta applications and development releases before promotion to stable.</p>
      <div class="command"><code>sudo tee /etc/apt/sources.list.d/radical-computer-technologies-experimental.sources &gt;/dev/null &lt;&lt;'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: experimental
Components: main
Architectures: amd64 arm64
Trusted: yes
EOF

sudo apt update</code></div>
    </article>
  </section>

  <section class="card">
    <h2>Install Packages</h2>
    <p>Install the aggregate package for the full SDK/runtime, or choose targeted modules for lean deployments.</p>
    <div class="command"><code>sudo apt install radlib
sudo apt install radlib-core radlib-ui radlib-dsp
sudo apt install radlib-media radlib-fpga radlib-web</code></div>
    <div class="package-list">
      <div class="package"><code>radlib</code><br>Full RADLib install.</div>
      <div class="package"><code>radlib-runtime-0-1</code><br>ABI-pinned runtime line.</div>
      <div class="package"><code>radlib-dev-0-1</code><br>Headers and CMake package files.</div>
      <div class="package"><code>radlib-ui</code><br>RADUi runtime module.</div>
      <div class="package"><code>radlib-media</code><br>RADMedia runtime module.</div>
      <div class="package"><code>radbard</code><br>Music composition beta in experimental.</div>
    </div>
    <p class="note">
      <code>Trusted: yes</code> is temporary for the unsigned beta repository. Replace this with signed repository metadata before broad public release.
    </p>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Documentation</h2>
      <p>RADLib API docs are versioned so stable and experimental APIs can be compared directly.</p>
      <div class="links">
        <a class="link-card" href="docs/radlib/0.1.0/api/"><strong>RADLib 0.1.0</strong><span>Stable API documentation</span></a>
        <a class="link-card" href="docs/radlib/api/"><strong>Current RADLib</strong><span>Latest generated API docs</span></a>
        <a class="link-card" href="docs/radlib/"><strong>Docs Index</strong><span>Version chooser</span></a>
      </div>
    </article>

    <article class="card">
      <h2>Package Indexes</h2>
      <p>Direct package metadata links for repository verification and manual inspection.</p>
      <div class="links">
        <a class="link-card" href="debian/dists/stable/main/binary-amd64/Packages"><strong>Stable amd64</strong><span>Debian Packages file</span></a>
        <a class="link-card" href="debian/dists/stable/main/binary-arm64/Packages"><strong>Stable arm64</strong><span>Debian Packages file</span></a>
        <a class="link-card" href="debian/pool/main/"><strong>Package Pool</strong><span>Published .deb files</span></a>
      </div>
    </article>
  </section>
</main>
