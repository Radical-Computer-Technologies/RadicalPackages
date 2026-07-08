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
    <div class="eyebrow">Experimental Build Framework</div>
    <h1>RadBuild Packages</h1>
    <p class="lead">
      RadBuild is the graph-based build framework for FPGA, Linux, firmware, software, package, deployment, VSCode, and optional server workflows.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Version:</strong> 0.2.0</span>
      <span class="pill"><strong>Suite:</strong> experimental</span>
      <span class="pill"><strong>Architecture:</strong> all</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Install RadBuild</h2>
      <p>Add the experimental repository from the home page, then install the CLI and optional components.</p>
      <div class="command"><code>sudo apt update
sudo apt install radbuild
sudo apt install radbuild-radhdl radbuild-server radbuild-vscode-support radbuild-doc</code></div>
    </article>

    <article class="card">
      <h2>Commands</h2>
      <div class="package-list">
        <div class="package"><code>radbuild project validate</code><br><span>Validate graph settings.</span></div>
        <div class="package"><code>radbuild build all --json-events</code><br><span>Run graph builds with machine-readable progress.</span></div>
        <div class="package"><code>radbuild-graph</code><br><span>Inspect dependency order.</span></div>
        <div class="package"><code>radbuild-hdlgen</code><br><span>Browse/generate RadHDL assets.</span></div>
      </div>
    </article>
  </section>

  <section class="card">
    <h2>Published Packages</h2>
    <table class="package-table">
      <thead><tr><th>Package</th><th>Purpose</th><th>Install</th></tr></thead>
      <tbody>
        <tr><td><code>radbuild</code></td><td>CLI tools, schemas, templates, provider generators, and packaging scripts.</td><td><code>sudo apt install radbuild</code></td></tr>
        <tr><td><code>radbuild-radhdl</code></td><td>Packaged RadHDL catalog and source assets installed at <code>/usr/share/radbuild/radhdl</code>.</td><td><code>sudo apt install radbuild-radhdl</code></td></tr>
        <tr><td><code>radbuild-server</code></td><td>Optional web server, review DB, client, worker, and LLM helper tools.</td><td><code>sudo apt install radbuild-server</code></td></tr>
        <tr><td><code>radbuild-vscode-support</code></td><td>VSCode extension source and compiled support files.</td><td><code>sudo apt install radbuild-vscode-support</code></td></tr>
        <tr><td><code>radbuild-doc</code></td><td>RadBuild documentation.</td><td><code>sudo apt install radbuild-doc</code></td></tr>
      </tbody>
    </table>
  </section>

  <details class="doc-group">
    <summary>Repository Metadata</summary>
      <div class="links">
        <a class="link-card" href="debian/dists/experimental/main/binary-all/Packages"><strong>Experimental all</strong><span>Package index</span></a>
        <a class="link-card" href="debian/pool/main/r/radbuild/"><strong>radbuild Pool</strong><span>Published CLI package</span></a>
        <a class="link-card" href="debian/pool/main/r/radbuild-radhdl/"><strong>radbuild-radhdl Pool</strong><span>Published RadHDL package</span></a>
        <a class="link-card" href="debian/pool/main/r/radbuild-server/"><strong>radbuild-server Pool</strong><span>Published server package</span></a>
      </div>
  </details>

  <section class="card">
      <h2>Related Packages</h2>
      <div class="links">
        <a class="link-card" href="radlib.html"><strong>RADLib</strong><span>Runtime libraries consumed by target systems</span></a>
        <a class="link-card" href="radbard.html"><strong>RADBard</strong><span>Experimental application package track</span></a>
      </div>
  </section>
</main>
