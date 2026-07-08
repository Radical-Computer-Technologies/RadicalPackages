<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="radlib.html">RADLib</a>
      <a href="radbard.html">RADBard</a>
      <a href="radbuild.html">RadBuild</a>
      <a href="docs/radlib/">Docs</a>
      <a href="debian/pool/main/">Pool</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Stable Package Line</div>
    <h1>RADLib Packages</h1>
    <p class="lead">
      RADLib packages are split into ABI-pinned runtime modules, unversioned convenience packages, development headers, documentation, examples, and tools.
      Stable currently tracks RADLib 0.1.0.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Version:</strong> 0.1.0</span>
      <span class="pill"><strong>ABI line:</strong> 0.1</span>
      <span class="pill"><strong>Architectures:</strong> amd64, arm64</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Full Install</h2>
      <p>Install the complete RADLib runtime, development files, docs, examples, and tools.</p>
      <div class="command"><code>sudo apt install radlib</code></div>
    </article>

    <article class="card">
      <h2>Lean Runtime Install</h2>
      <p>Install only the modules your application needs.</p>
      <div class="command"><code>sudo apt install radlib-core radlib-ui radlib-dsp
sudo apt install radlib-media radlib-fpga radlib-web</code></div>
    </article>
  </section>

  <section class="card">
    <h2>Core Packages</h2>
    <table class="package-table">
      <thead><tr><th>Package</th><th>Purpose</th><th>Install</th></tr></thead>
      <tbody>
        <tr><td><code>radlib</code></td><td>Aggregate RADLib package.</td><td><code>sudo apt install radlib</code></td></tr>
        <tr><td><code>radlib-runtime</code></td><td>Latest runtime meta-package.</td><td><code>sudo apt install radlib-runtime</code></td></tr>
        <tr><td><code>radlib-runtime-0-1</code></td><td>ABI-pinned RADLib 0.1 runtime meta-package.</td><td><code>sudo apt install radlib-runtime-0-1</code></td></tr>
        <tr><td><code>radlib-dev</code></td><td>Latest public headers and CMake package files.</td><td><code>sudo apt install radlib-dev</code></td></tr>
        <tr><td><code>radlib-dev-0-1</code></td><td>ABI-pinned RADLib 0.1 public headers and CMake package files.</td><td><code>sudo apt install radlib-dev-0-1</code></td></tr>
        <tr><td><code>radlib-doc</code></td><td>Generated API documentation package.</td><td><code>sudo apt install radlib-doc</code></td></tr>
        <tr><td><code>radlib-examples</code></td><td>Example applications and sample projects.</td><td><code>sudo apt install radlib-examples</code></td></tr>
        <tr><td><code>radlib-tools</code></td><td>SDK tools and protocol generator.</td><td><code>sudo apt install radlib-tools</code></td></tr>
      </tbody>
    </table>
  </section>

  <section class="card">
    <h2>Runtime Modules</h2>
    <p>Use unversioned module packages for the current line, or the matching <code>-0-1</code> package when an application should pin the RADLib 0.1 ABI runtime line.</p>
    <div class="package-list">
      <div class="package"><code>radlib-core</code><br><span>Core event loop, system, JSON, and threading primitives.</span></div>
      <div class="package"><code>radlib-ui</code><br><span>RADUi and Slint-backed UI primitives.</span></div>
      <div class="package"><code>radlib-dsp</code><br><span>DSP primitives and transforms.</span></div>
      <div class="package"><code>radlib-media</code><br><span>Audio, MIDI, SoundFont, WAV, and MusicXML support.</span></div>
      <div class="package"><code>radlib-fpga</code><br><span>FPGA transport and register-map helpers.</span></div>
      <div class="package"><code>radlib-web</code><br><span>WebKit-backed RADWeb browser components.</span></div>
      <div class="package"><code>radlib-net</code><br><span>Networking and protocol helpers.</span></div>
      <div class="package"><code>radlib-database</code><br><span>SQLite-backed database primitives.</span></div>
      <div class="package"><code>radlib-serial</code><br><span>Serial-port helpers.</span></div>
      <div class="package"><code>radlib-security</code><br><span>Security, capability, sandbox, and license helpers.</span></div>
      <div class="package"><code>radlib-installer</code><br><span>Installer manifest and desktop integration helpers.</span></div>
      <div class="package"><code>radlib-update</code><br><span>Update manifest and A/B update helpers.</span></div>
      <div class="package"><code>radlib-cli</code><br><span>Command-line interface primitives.</span></div>
      <div class="package"><code>radlib-logging</code><br><span>Logging support.</span></div>
      <div class="package"><code>radlib-settings</code><br><span>Application settings support.</span></div>
      <div class="package"><code>radlib-input</code><br><span>Input device primitives.</span></div>
      <div class="package"><code>radlib-display</code><br><span>Display and backlight helpers.</span></div>
      <div class="package"><code>radlib-device</code><br><span>Device discovery helpers.</span></div>
      <div class="package"><code>radlib-power</code><br><span>Power, thermal, and governor helpers.</span></div>
      <div class="package"><code>radlib-service</code><br><span>Service unit helpers.</span></div>
      <div class="package"><code>radlib-data-structures</code><br><span>Container and allocator primitives.</span></div>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Documentation</h2>
      <div class="links">
        <a class="link-card" href="docs/radlib/0.1.0/api/"><strong>RADLib 0.1.0 API</strong><span>Stable generated API docs</span></a>
        <a class="link-card" href="docs/radlib/api/"><strong>Current API</strong><span>Latest generated API docs</span></a>
      </div>
    </article>

    <article class="card">
      <h2>Package Metadata</h2>
      <div class="links">
        <a class="link-card" href="debian/dists/stable/main/binary-amd64/Packages"><strong>Stable amd64</strong><span>Package index</span></a>
        <a class="link-card" href="debian/dists/stable/main/binary-arm64/Packages"><strong>Stable arm64</strong><span>Package index</span></a>
      </div>
    </article>
  </section>
</main>
