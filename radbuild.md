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
    <div class="eyebrow">Experimental Build Framework</div>
    <h1>RadBuild Packages</h1>
    <p class="lead">
      RadBuild is the graph-based build framework for FPGA, Linux, firmware, software, package, deployment, RADix-OS image, VSCode, and optional server workflows.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Version:</strong> 0.2.1</span>
      <span class="pill"><strong>Suite:</strong> experimental</span>
      <span class="pill"><strong>Runtime:</strong> frozen executables</span>
      <span class="pill"><strong>Architectures:</strong> amd64 runtime, all docs/assets</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Install RadBuild</h2>
      <p>Add the signed experimental repository from the home page, then install the frozen CLI and optional components.</p>
      <div class="command"><code>sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://radical-computer-technologies.github.io/RadicalPackages/keys/radical-packages-archive-key.asc \
  | sudo gpg --dearmor -o /etc/apt/keyrings/radical-packages.gpg

sudo tee /etc/apt/sources.list.d/radical-computer-technologies-experimental.sources &gt;/dev/null &lt;&lt;'EOF'
Types: deb
URIs: https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/apt-experimental
Suites: ./
Signed-By: /etc/apt/keyrings/radical-packages.gpg
Architectures: amd64 arm64
EOF

sudo apt update
sudo apt install radbuild
sudo apt install radbuild-radhdl radbuild-server radbuild-vscode-support radbuild-doc</code></div>
    </article>

    <article class="card">
      <h2>Commands</h2>
      <div class="package-list">
        <div class="package"><code>radbuild project validate</code><br><span>Validate graph settings.</span></div>
        <div class="package"><code>radbuild build os --json-events</code><br><span>Build and smoke RADix-OS images.</span></div>
        <div class="package"><code>settings.terminal.json / settings.wm.json</code><br><span>Select terminal-only or RADCompositor/Slint RADix profiles.</span></div>
        <div class="package"><code>rkconfig</code><br><span>Configure RADix hostname, root password, terminal scale, and rootfs sizing.</span></div>
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
        <tr><td><code>radbuild</code></td><td>Frozen CLI tools, graph build providers, and helper commands.</td><td><code>sudo apt install radbuild</code></td></tr>
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
        <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/tag/apt-experimental"><strong>Experimental APT Release</strong><span>Signed package-manager metadata and package assets.</span></a>
        <a class="link-card" href="keys/radical-packages-archive-key.asc"><strong>APT Signing Key</strong><span>Public key for <code>Signed-By</code> install instructions.</span></a>
        <a class="link-card" href="docs/radbuild/0.2.1/"><strong>RadBuild 0.2.1 Docs</strong><span>Install, FPGA builds, OS builds, packaging, examples, and compatibility notes.</span></a>
      </div>
  </details>

  <section class="card">
      <h2>Related Packages</h2>
      <div class="links">
        <a class="link-card" href="radlib.html"><strong>RADLib</strong><span>Runtime libraries consumed by target systems</span></a>
        <a class="link-card" href="radix-os.html"><strong>RADix-OS</strong><span>Experimental OS image and kernel API track</span></a>
        <a class="link-card" href="radbard.html"><strong>RADBard</strong><span>Experimental application package track</span></a>
      </div>
  </section>
</main>
