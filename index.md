<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="radlib.html">RADLib</a>
      <a href="radbard.html">RADBard</a>
      <a href="radbuild.html">RadBuild</a>
      <a href="docs/">Docs</a>
      <a href="debian/pool/main/">Pool</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Radical Computer Technologies</div>
    <h1>Package Repository And Documentation Hub</h1>
    <p class="lead">
      Debian packages and generated documentation for RADLib, RADBard, and related Radical Computer Technologies releases.
      Stable packages stay pinned to known runtime lines; experimental packages move faster for active beta work.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Stable:</strong> RADLib 0.1.0</span>
      <span class="pill"><strong>Experimental:</strong> RADBard beta, RadBuild 0.2.0, future RADLib 0.1.1</span>
      <span class="pill"><strong>Architectures:</strong> amd64, arm64, all</span>
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

  <section class="grid">
    <a class="link-card" href="radlib.html">
      <strong>RADLib Packages</strong>
      <span>Runtime, development, module, docs, examples, and tool package list.</span>
    </a>
    <a class="link-card" href="radbard.html">
      <strong>RADBard Packages</strong>
      <span>Experimental music composition suite package information.</span>
    </a>
    <a class="link-card" href="radbuild.html">
      <strong>RadBuild Packages</strong>
      <span>Graph build framework, server, VSCode support, and docs packages.</span>
    </a>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Documentation</h2>
      <p>RADLib API docs are versioned so stable and experimental APIs can be compared directly.</p>
      <div class="links">
        <a class="link-card" href="docs/radlib/0.1.0/api/"><strong>RADLib 0.1.0</strong><span>Stable API documentation</span></a>
        <a class="link-card" href="docs/radlib/api/"><strong>Current RADLib</strong><span>Latest generated API docs</span></a>
        <a class="link-card" href="docs/radhdl/current/"><strong>RadHDL Current</strong><span>HDL library inventory and VHDL autodoc</span></a>
        <a class="link-card" href="docs/"><strong>Docs Index</strong><span>Version chooser</span></a>
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

  <p class="note">
    <code>Trusted: yes</code> is temporary for the unsigned beta repository. Replace this with signed repository metadata before broad public release.
  </p>
</main>
