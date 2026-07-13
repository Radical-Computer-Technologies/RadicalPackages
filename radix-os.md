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
    <div class="eyebrow">Experimental Operating System</div>
    <h1>RADix-OS</h1>
    <p class="lead">
      RADix-OS is the Crimson 0.1.0 POSIX-inspired kernel and VM image track for embedded boards, desktop VM verification, and future SoC targets.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Version:</strong> Crimson 0.1.0</span>
      <span class="pill"><strong>Suite:</strong> experimental</span>
      <span class="pill"><strong>Build:</strong> RadBuild os.radix</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>API Documentation</h2>
      <p>The public Crimson kernel API docs are generated from the RADix-OS repository with Doxygen.</p>
      <div class="links">
        <a class="link-card" href="docs/radix-os/0.1.0/api/"><strong>RADix-OS API</strong><span>Kernel API, device tree, networking, compositor, and Pi Zero 2 W notes.</span></a>
      </div>
    </article>

    <article class="card">
      <h2>Build With RadBuild</h2>
      <p>RadBuild 0.2.1 owns the canonical x86_64 GRUB VM image builds. Crimson currently publishes separate terminal and RADCompositor/Slint profiles, both under the experimental suite.</p>
      <div class="command"><code>radbuild build os --settings settings.json --json-events</code></div>
    </article>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Crimson VM Profiles</h2>
      <p>The terminal profile boots directly to the framebuffer login prompt and <code>rash</code>. The window-manager profile packages the Slint-backed RADCompositor path for UI stabilization.</p>
      <div class="command"><code>radbuild build os --settings settings.terminal.json --json-events
radbuild build os --settings settings.wm.json --json-events</code></div>
    </article>

    <article class="card">
      <h2>Root Filesystem</h2>
      <p><code>rkconfig</code> controls the generated hostname, initial root password, terminal scale, and ext4 size. The image stages Unix-style directories including <code>/bin</code>, <code>/dev</code>, <code>/etc</code>, <code>/home/root</code>, <code>/lib</code>, <code>/mnt</code>, <code>/usr</code>, <code>/tmp</code>, and <code>/var/log</code>.</p>
      <p>RADix kernel modules use <code>.rko</code>; future RADix shared objects use <code>.rso</code>.</p>
    </article>
  </section>

  <section class="card">
    <h2>Related Packages</h2>
    <div class="links">
      <a class="link-card" href="radbuild.html"><strong>RadBuild</strong><span>Build graph, VSCode support, and RADix-OS image provider.</span></a>
      <a class="link-card" href="radlib.html"><strong>RADLib</strong><span>Runtime and UI library packages that can target RADix-OS over time.</span></a>
      <a class="link-card" href="docs/"><strong>Documentation Index</strong><span>Versioned Radical docs hub.</span></a>
    </div>
  </section>
</main>
