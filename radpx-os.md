<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="./">Home</a>
      <a href="packages.html">Packages</a>
      <a href="radpx-os.html">RADPx OS</a>
      <a href="docs/">Docs</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Experimental Operating System</div>
    <h1>RADPx OS</h1>
    <p class="lead">
      RADPx OS is the Crimson 0.1.4 experimental package line for the POSIX-inspired kernel, x86 VM image track, embedded board ports, future SoC targets, and RADPx <code>.radpm</code> package metadata.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Version:</strong> Crimson 0.1.4</span>
      <span class="pill"><strong>Suite:</strong> experimental</span>
      <span class="pill"><strong>Build:</strong> RadBuild os.radpx</span>
      <span class="pill"><strong>Current x86:</strong> 0.1.4 beta 2</span>
    </div>
  </section>

  <section class="card">
    <h2>Current Crimson x86 Release</h2>
    <p>The current x86_64 GRUB release bundles include the bootable ISO, ext4 root filesystem image, FAT image, checksums, and helper scripts where available.</p>
    <div class="links">
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/tag/radpx-os-0.1.4-beta.2"><strong>RADPx OS 0.1.4 beta 2</strong><span>Versioned GitHub Release for Crimson x86 terminal, smoke-test, RADCompositor images, and RADpm packages.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/radpx-os-0.1.4-beta.2/radpx-os-crimson_0.1.4-beta.2_x86_64-grub-terminal-interactive.tar.gz"><strong>x86_64 Interactive Terminal Bundle</strong><span>Framebuffer login shell profile with Vim tiny, ncurses metadata, ISO, ext4, and FAT images.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/radpx-os-0.1.4-beta.2/radpx-os-crimson_0.1.4-beta.2_x86_64-grub-terminal-smoke.tar.gz"><strong>x86_64 Smoke Terminal Bundle</strong><span>Autologin/autotest terminal profile for scripted VM checks.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/radpx-os-0.1.4-beta.2/radpx-os-crimson_0.1.4-beta.2_x86_64-grub-wm.tar.gz"><strong>x86_64 RADCompositor Bundle</strong><span>Slint/RADCompositor profile with Vim tiny, ISO, ext4, and FAT images.</span></a>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>API Documentation</h2>
      <p>The public Crimson kernel API docs are generated from the RADPx-OS repository with Doxygen.</p>
      <div class="links">
      <a class="link-card" href="docs/radpx-os/0.1.4/api/"><strong>RADPx-OS API</strong><span>Kernel API, device tree, networking, compositor, and Pi Zero 2 W notes.</span></a>
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
      <p>RADPx kernel modules use <code>.rko</code>; future RADPx shared objects use <code>.rso</code>.</p>
    </article>
  </section>

  <section class="card">
    <h2>RADPx Package Repository</h2>
    <p>RadicalPackages hosts RADPx <code>.radpm</code> metadata and release archives beside Debian packages. In this release line, RadBuild is the installer: it resolves package metadata and stages package archives into generated root filesystems.</p>
    <p>Common OS images should select packagegroups first, then add explicit packages only when needed. Packagegroups keep terminal, desktop, networking, and SDK selections reproducible while still letting RadBuild report missing dependencies without silently changing a project.</p>
    <div class="package-list">
      <a class="package package-link" href="radpm/dists/experimental/main/packagegroups/radpx-terminal-base.json"><code>radpx-terminal-base</code><span>Core terminal image set with RADLib, ncurses, and Vim tiny.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packagegroups/radpx-desktop-base.json"><code>radpx-desktop-base</code><span>RADCompositor/RADLib UI image set for the window-manager profile.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packagegroups/radpx-networking.json"><code>radpx-networking</code><span>Network, DNS resolver, time sync, and timezone packages.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packagegroups/radpx-dev-sdk.json"><code>radpx-dev-sdk</code><span>Development/sysroot package set for RADPx terminal application ports.</span></a>
    </div>
    <div class="package-list">
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-core</code><span>Core RADPx userspace layout and boot support metadata.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-ncurses</code><span>RADPx ncurses/tinfo shared runtime, <code>.rso</code> libraries, static archives, and terminal UI headers.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-vim-tiny</code><span>Tiny upstream Vim port metadata, RADPx defaults, and Vim license for terminal images.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radlib</code><span>RADLib aggregate metadata for future RADPx userspace and service packages.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radlib-runtime</code><span>RADLib runtime package metadata for generated RADPx root filesystems.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radlib-ui</code><span>RADLib UI and Slint-facing metadata for RADPx OS builds.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-network</code><span>RADPx network service package metadata.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-dns-resolver</code><span>DNS resolver service package metadata.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-time-sync</code><span>NTP/time synchronization service package metadata.</span></a>
      <a class="package package-link" href="radpm/dists/experimental/main/packages.json"><code>radpx-tzdata</code><span>Timezone data package metadata.</span></a>
    </div>
    <div class="links">
      <a class="link-card" href="radpm/dists/experimental/main/packages.json"><strong>Experimental .radpm Index</strong><span>Machine-readable package records for RadBuild.</span></a>
      <a class="link-card" href="radpm/dists/experimental/main/packagegroups.json"><strong>Experimental Packagegroups</strong><span>Machine-readable terminal, desktop, networking, and SDK group records.</span></a>
      <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/tag/radpx-os-0.1.4-beta.2"><strong>RADPx Release Assets</strong><span>Current <code>.radpm</code> archives and x86 image bundles.</span></a>
      <a class="link-card" href="packages.html"><strong>Package Catalog</strong><span>Debian and RADPx package listings.</span></a>
    </div>
  </section>

  <section class="card">
    <h2>Create an Image From Scratch</h2>
    <p>Install RadBuild, create a RADPx project from a packaged template, use menuconfig to select packagegroups and runtime settings, then run the emitted VM script.</p>
    <div class="command"><code>sudo apt install radbuild
radbuild project create ~/radpx-work --non-interactive --template radpx-os-terminal --project-name radpx-terminal
cd ~/radpx-work/radpx-terminal
radbuild menuconfig --settings settings.json
radbuild build os --settings settings.json --json-events
./artifacts/radpx/x86_64-grub-terminal/run-radpx-vm.sh</code></div>
    <div class="links">
      <a class="link-card" href="docs/radbuild/0.2.1/examples/radpx-from-scratch.html"><strong>Full Walkthrough</strong><span>Template, source checkout, packagegroups, rkconfig, SDK, artifacts, and VM checks.</span></a>
      <a class="link-card" href="docs/radbuild/0.2.1/settings-fields.html"><strong>Configuration Reference</strong><span>All important RADPx, RADpm, rkconfig, and SDK settings.</span></a>
    </div>
  </section>

  <section class="card">
    <h2>Related Tools</h2>
    <div class="links">
      <a class="link-card" href="radbuild.html"><strong>RadBuild</strong><span>Build graph, VSCode support, and RADPx-OS image provider.</span></a>
      <a class="link-card" href="radlib.html"><strong>RADLib</strong><span>Runtime and UI library packages that can target RADPx-OS over time.</span></a>
      <a class="link-card" href="docs/"><strong>Documentation Index</strong><span>Versioned Radical docs hub.</span></a>
    </div>
  </section>
</main>
