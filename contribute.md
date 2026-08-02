<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="./">Home</a>
      <a href="packages.html">Packages</a>
      <a href="radpx-os.html">RADPx OS</a>
      <a href="docs/">Docs</a>
      <a href="contribute.html">Contribute</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Open Source Contribution</div>
    <h1>Build Portable Hardware And Systems With Us</h1>
    <p class="lead">
      RadHDL and RADPx OS/Kernel are open-source Radical Computer Technologies projects.
      The current focus is practical portability: vendor-agnostic FPGA primitives and interfaces, repeatable RadBuild flows, and a small POSIX-inspired OS that can grow from embedded boards to desktop-class targets.
    </p>
  </section>

  <section class="grid">
    <article class="card">
      <h2>RadHDL</h2>
      <p>
        RadHDL is the VHDL library track for reusable FPGA systems. Current contribution areas include RadPrimitive vendor wrappers, CDC/FIFO/RAM/DSP portability, simulation matrix coverage, interface IP, and example projects such as the FPiGA Audio Hat.
      </p>
      <div class="links">
        <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RadHDL"><strong>RadHDL Repository</strong><span>Clone the source, open issues, and send pull requests.</span></a>
        <a class="link-card" href="docs/radhdl/0.2.2-beta.1/"><strong>RadHDL Docs</strong><span>Getting started, datasheets, guides, and Crimson change notes.</span></a>
      </div>
    </article>

    <article class="card">
      <h2>RADPx OS/Kernel</h2>
      <p>
        RADPx OS is the experimental kernel and userspace track. Current contribution areas include POSIX compatibility, filesystems, terminal applications, services, networking, AArch64 ports, and hardware-oriented scheduling work.
      </p>
      <div class="links">
        <a class="link-card" href="https://github.com/Radical-Computer-Technologies/RADix-OS"><strong>RADPx OS Repository</strong><span>Kernel, services, userspace, build profiles, and VM images.</span></a>
        <a class="link-card" href="docs/radpx-os/0.1.5/api/"><strong>RADPx OS Docs</strong><span>Kernel API and experimental Crimson documentation.</span></a>
      </div>
    </article>
  </section>

  <section class="card">
    <h2>How To Get Involved</h2>
    <ol>
      <li>Install RadBuild from the experimental APT channel so project generation, package metadata, and HDL documentation tools match the release docs.</li>
      <li>Clone the repository you want to work on, then create a feature branch from the current Crimson development branch or the repository default branch.</li>
      <li>Run the smallest relevant validation first: GHDL or xsim for HDL primitives, RadBuild project validation for build templates, or the RADPx terminal VM smoke path for kernel changes.</li>
      <li>Open a pull request with the target board/toolchain, command output, and any generated figures or simulation evidence that reviewers need to reproduce the result.</li>
    </ol>
  </section>

  <section class="card">
    <h2>Good First Areas</h2>
    <div class="package-list">
      <div class="package"><code>RadPrimitive</code><br><span>Add or verify RAM, FIFO, DSP, clocking, and CDC wrappers for FPGA families.</span></div>
      <div class="package"><code>Simulation Matrix</code><br><span>Make generic and vendor-specific models prove equivalent under common testbenches.</span></div>
      <div class="package"><code>RadBuild Templates</code><br><span>Add reproducible projects for boards, FPGA flows, RADPx images, Buildroot, and PetaLinux.</span></div>
      <div class="package"><code>RADPx Services</code><br><span>Improve JSON-defined services, networking, time sync, logging, and shell tooling.</span></div>
      <div class="package"><code>Documentation</code><br><span>Expand guides, screenshots, command output, and board bring-up notes.</span></div>
    </div>
  </section>
</main>
