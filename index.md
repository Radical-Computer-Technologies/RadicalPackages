<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="./">Home</a>
      <a href="packages.html">Packages</a>
      <a href="radix-os.html">RADix OS</a>
      <a href="docs/">Docs</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Radical Computer Technologies</div>
    <h1>Package Repository And Documentation Hub</h1>
    <p class="lead">
      GitHub Release-backed Debian packages, RADix <code>.radpm</code> metadata, and generated documentation for RADLib, RADBard, RadBuild, RADix OS, and related Radical Computer Technologies releases.
      Stable packages stay pinned to known runtime lines; experimental packages move faster for active beta work.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Stable:</strong> RADLib 0.1.0</span>
      <span class="pill"><strong>Experimental:</strong> RADBard beta, RadBuild 0.2.1, RADix-OS Crimson 0.1.0</span>
      <span class="pill"><strong>Architectures:</strong> amd64, arm64, all</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Stable Repository</h2>
      <p>Use stable for the RADLib 0.1.0 release line.</p>
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
    <h2>Packages</h2>
    <p>Search published package groups, then open the product package page for install commands and repository metadata.</p>
    <input class="search-input" id="home-package-search" type="search" placeholder="Search packages by product, package name, channel, or purpose" aria-label="Search packages">
    <details class="doc-group package-search-group" data-search-group>
      <summary>Stable</summary>
      <details class="doc-release" data-search-item data-search-text="radlib stable 0.1.0 runtime development modules documentation examples tools amd64 arm64">
        <summary>RADLib 0 - Crimson</summary>
        <div class="links">
          <a class="link-card" href="radlib.html"><strong>RADLib Packages</strong><span>Runtime, development, module, docs, examples, and tool packages.</span></a>
        </div>
      </details>
    </details>
    <details class="doc-group package-search-group" data-search-group>
      <summary>Experimental</summary>
      <details class="doc-release" data-search-item data-search-text="radbuild experimental 0.2.1 cli server vscode radhdl docs graph build framework radix os image">
        <summary>RadBuild 0 - Crimson</summary>
        <div class="links">
          <a class="link-card" href="radbuild.html"><strong>RadBuild Packages</strong><span>Graph build framework, server, VSCode support, RADix-OS provider, RadHDL package, and docs.</span></a>
        </div>
      </details>
      <details class="doc-release" data-search-item data-search-text="radix os experimental crimson 0.1.0 kernel vm image x86 slint posix radbuild">
        <summary>RADix-OS 0 - Crimson</summary>
        <div class="links">
          <a class="link-card" href="radix-os.html"><strong>RADix OS</strong><span>Experimental POSIX-inspired kernel, VM image path, API documentation, and RADix package hub.</span></a>
        </div>
      </details>
      <details class="doc-release" data-search-item data-search-text="radbard experimental 0.1.0 beta music audio composition daw editor">
        <summary>RADBard 0 - Crimson</summary>
        <div class="links">
          <a class="link-card" href="radbard.html"><strong>RADBard Packages</strong><span>Experimental music and audio composition suite package.</span></a>
        </div>
      </details>
    </details>
    <div class="links">
      <a class="link-card" href="packages.html"><strong>Packages Page</strong><span>Full searchable package catalog.</span></a>
      <a class="link-card" href="radix-os.html"><strong>RADix OS Hub</strong><span>RADix OS builds, docs, and <code>.radpm</code> package metadata.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases"><strong>Release Assets</strong><span>APT channel assets, package files, and OS image bundles.</span></a>
    </div>
  </section>

  <p class="note">
    <code>Trusted: yes</code> is temporary for the unsigned beta repository. Replace this with signed repository metadata before broad public release.
  </p>
</main>

<script>
(() => {
  const input = document.getElementById("home-package-search");
  const items = Array.from(document.querySelectorAll("[data-search-item]"));
  if (!input) return;
  input.addEventListener("input", () => {
    const query = input.value.trim().toLowerCase();
    items.forEach((item) => {
      const match = !query || item.dataset.searchText.includes(query);
      item.hidden = !match;
      if (query && match) {
        item.open = true;
        const parent = item.closest("[data-search-group]");
        if (parent) parent.open = true;
      }
    });
  });
})();
</script>
