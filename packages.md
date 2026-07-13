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
    <div class="eyebrow">Package Catalog</div>
    <h1>Packages</h1>
    <p class="lead">
      Search the published Radical package families by product, release channel, version line, package name, package format, or purpose.
      Product package pages contain install commands, package tables, and repository metadata links.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Stable:</strong> RADLib 0.1.0</span>
      <span class="pill"><strong>Experimental:</strong> RadBuild 0.2.1, RADix-OS Crimson 0.1.0, RADBard 0.1.0 beta</span>
      <span class="pill"><strong>Architectures:</strong> amd64, arm64, all</span>
      <span class="pill"><strong>Hosting:</strong> GitHub Releases</span>
    </div>
  </section>

  <section class="card">
    <h2>APT Channels</h2>
    <p>Debian packages are published as signed flat APT repositories in GitHub Releases. GitHub Pages hosts the package catalog, docs, and public signing key.</p>
    <div class="links">
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/tag/apt-stable"><strong>Stable APT Release</strong><span>Stable package-manager channel assets.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/tag/apt-experimental"><strong>Experimental APT Release</strong><span>Beta and active development package-manager channel assets.</span></a>
      <a class="link-card" href="keys/radical-packages-archive-key.asc"><strong>APT Signing Key</strong><span>Public key for <code>signed-by</code> install instructions.</span></a>
      <a class="link-card" href="RELEASES.html"><strong>Release Runbook</strong><span>Maintainer workflow for staging and publishing release assets.</span></a>
    </div>
  </section>

  <section class="card">
    <h2>Package Families</h2>
    <input class="search-input" id="package-search" type="search" placeholder="Search package families and package names" aria-label="Search package families">

    <details class="doc-group package-search-group" data-search-group>
      <summary>Stable</summary>
      <details class="doc-release" data-search-item data-search-text="radlib stable 0.1.0 crimson runtime development dev modules docs examples tools core ui dsp media fpga web net database serial security installer update cli logging settings input display device power service data structures amd64 arm64">
        <summary>RADLib 0 - Crimson</summary>
        <div class="package-list">
          <a class="package package-link" href="radlib.html"><code>radlib</code><span>Aggregate runtime, development, docs, examples, and tools package.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-runtime</code><span>Latest runtime meta-package.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-dev</code><span>Public headers and CMake package files.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-doc</code><span>Generated API documentation package.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-core</code><span>Core event loop, system, JSON, and threading primitives.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-dsp</code><span>DSP primitives and transforms.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-fpga</code><span>FPGA transport and register-map helpers.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-ui</code><span>RADUi and Slint-backed UI primitives.</span></a>
        </div>
      </details>
    </details>

    <details class="doc-group package-search-group" data-search-group>
      <summary>Experimental</summary>
      <details class="doc-release" data-search-item data-search-text="radbuild experimental 0.2.1 crimson cli server vscode support radhdl docs graph build framework project fpga linux firmware software packages deploy all radix os image">
        <summary>RadBuild 0 - Crimson</summary>
        <div class="package-list">
          <a class="package package-link" href="radbuild.html"><code>radbuild</code><span>Frozen CLI and graph build helper executables.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-radhdl</code><span>Packaged RadHDL catalog and source assets.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-server</code><span>Optional web server, review DB, client, workers, and LLM helpers.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-vscode-support</code><span>VSCode extension support package.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-doc</code><span>RadBuild documentation package.</span></a>
        </div>
      </details>
      <details class="doc-release" data-search-item data-search-text="radix os experimental crimson 0.1.0 kernel vm image x86 slint posix radbuild docs radpm package repository">
        <summary>RADix-OS 0 - Crimson</summary>
        <div class="package-list">
          <a class="package package-link" href="radix-os.html"><code>RADix OS</code><span>Experimental OS hub, kernel API documentation, and VM image build path.</span></a>
          <a class="package package-link" href="radix-os.html"><code>docs/radix-os/0.1.0</code><span>Published Crimson kernel API documentation.</span></a>
        </div>
      </details>
      <details class="doc-release" data-search-item data-search-text="radbard experimental 0.1.0 beta music audio composition editor notation mixer automation daw amd64 radlib ui media dsp">
        <summary>RADBard 0 - Crimson</summary>
        <div class="package-list">
          <a class="package package-link" href="radbard.html"><code>radbard</code><span>Experimental music and audio composition suite beta.</span></a>
        </div>
      </details>
      <details class="doc-release" data-search-item data-search-text="radlib radical radix os experimental 0.1.1 crimson kernel radekernel bare metal hal simulator circle rtos vfs device terminal tasks memory">
        <summary>RADLib 0 - Crimson Experimental</summary>
        <div class="package-list">
          <a class="package package-link" href="radlib.html"><code>radlib-embedded-kernel</code><span>RADix-OS kernel service layer for simulator and bare-metal HAL backends.</span></a>
          <a class="package package-link" href="radlib.html"><code>radlib-embedded-kernel-0-1</code><span>ABI-pinned RADix-OS kernel runtime for RADLib 0.1.</span></a>
        </div>
      </details>
    </details>
  </section>

  <section class="card">
    <h2>RADix OS Packages</h2>
    <p>RADix packages use <code>.radpm</code> records with release-hosted archives. RadBuild is currently the installer for generated RADix root filesystems; in-OS package management is not enabled yet.</p>
    <div class="package-list">
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radix-core</code><span>Core RADix userspace layout and boot support metadata.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radlib</code><span>RADLib aggregate metadata for future RADix OS userspace and services.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radlib-runtime</code><span>RADLib runtime metadata for generated RADix root filesystems.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radlib-ui</code><span>RADLib UI and Slint-facing metadata for RADix OS builds.</span></a>
    </div>
    <div class="links">
      <a class="link-card" href="radix-os.html"><strong>RADix OS Hub</strong><span>Build profiles, API docs, and package repository notes.</span></a>
      <a class="link-card" href="radpm/dists/experimental/main/packages.json"><strong>Experimental .radpm Index</strong><span>Machine-readable RADix package metadata.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/tag/radix-os-0.1.0-beta.1"><strong>RADix Release Assets</strong><span>Current <code>.radpm</code> package archives and x86 images.</span></a>
      <a class="link-card" href="radpm/dists/stable/main/packages.json"><strong>Stable .radpm Index</strong><span>Reserved stable RADix package metadata.</span></a>
    </div>
  </section>
</main>

<script>
(() => {
  const input = document.getElementById("package-search");
  const items = Array.from(document.querySelectorAll("[data-search-item]"));
  if (!input) return;
  input.addEventListener("input", () => {
    const query = input.value.trim().toLowerCase();
    items.forEach((item) => {
      const text = item.dataset.searchText || "";
      const match = !query || text.includes(query);
      item.hidden = !match;
      if (query && match) {
        item.open = true;
        const group = item.closest("[data-search-group]");
        if (group) group.open = true;
      }
    });
  });
})();
</script>
