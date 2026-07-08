<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="packages.html">Packages</a>
      <a href="docs/">Docs</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Package Catalog</div>
    <h1>Packages</h1>
    <p class="lead">
      Search the published Radical package families by product, release channel, version line, package name, or purpose.
      Product package pages contain install commands, package tables, and repository metadata links.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Stable:</strong> RADLib 0.1.0</span>
      <span class="pill"><strong>Experimental:</strong> RadBuild 0.2.0, RADBard 0.1.0 beta</span>
      <span class="pill"><strong>Architectures:</strong> amd64, arm64, all</span>
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
      <details class="doc-release" data-search-item data-search-text="radbuild experimental 0.2.0 crimson cli server vscode support radhdl docs graph build framework project fpga linux firmware software packages deploy all">
        <summary>RadBuild 0 - Crimson</summary>
        <div class="package-list">
          <a class="package package-link" href="radbuild.html"><code>radbuild</code><span>CLI tools, schemas, templates, providers, and packaging scripts.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-radhdl</code><span>Packaged RadHDL catalog and source assets.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-server</code><span>Optional web server, review DB, client, workers, and LLM helpers.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-vscode-support</code><span>VSCode extension support package.</span></a>
          <a class="package package-link" href="radbuild.html"><code>radbuild-doc</code><span>RadBuild documentation package.</span></a>
        </div>
      </details>
      <details class="doc-release" data-search-item data-search-text="radbard experimental 0.1.0 beta music audio composition editor notation mixer automation daw amd64 radlib ui media dsp">
        <summary>RADBard 0 - Crimson</summary>
        <div class="package-list">
          <a class="package package-link" href="radbard.html"><code>radbard</code><span>Experimental music and audio composition suite beta.</span></a>
        </div>
      </details>
    </details>
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
