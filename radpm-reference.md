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
    <div class="eyebrow">Package Format Reference</div>
    <h1>RADpm Reference</h1>
    <p class="lead">
      RADpm is the RADPx-OS package model: signed <code>.radpm</code> archives described by machine-readable
      JSON indexes that RadBuild reads to resolve and stage packages into generated root filesystems.
      This page documents the on-disk schema and packaging model that the published indexes currently
      express only by example.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Tool:</strong> radpm</span>
      <span class="pill"><strong>Index schema:</strong> radpm-package-index</span>
      <span class="pill"><strong>schema_version:</strong> 1</span>
      <span class="pill"><strong>Suites:</strong> stable, experimental</span>
    </div>
  </section>

  <section class="card">
    <h2>What RADpm Is</h2>
    <p>
      RADpm is the RADPx-OS package system. A package is a <code>.radpm</code> archive (a tar archive that
      unpacks into a <code>rootfs/</code> tree and/or standard top-level directories such as <code>bin</code>,
      <code>etc</code>, <code>lib</code>, <code>usr</code>) plus a JSON metadata record. The metadata records
      are gathered into a <strong>package index</strong> and an optional <strong>packagegroup index</strong>
      per suite and component.
    </p>
    <p>
      The <code>radpm</code> tool (source: <code>RADLib/tools/radpm/radpm.cpp</code>) reads these indexes and
      supports the commands <code>list</code>, <code>resolve</code>, <code>verify</code>, <code>install</code>,
      and <code>cache-toolchain</code>. In the current release line RadBuild is the installer: it resolves
      package metadata and stages package archives into generated RADPx root filesystems. In-OS package
      management is not enabled yet.
    </p>
    <p>
      Indexes live under a fixed repository layout. For a repository root, suite, and component the tool
      derives the paths <code>radpm/dists/&lt;suite&gt;/main/packages.json</code> and
      <code>radpm/dists/&lt;suite&gt;/main/packagegroups.json</code> (see <code>indexLocation()</code> in
      <code>radpm.cpp</code>). The default suite is <code>experimental</code>; <code>stable</code> is also
      published. A repository may also be pointed directly at a single <code>.json</code> index file, or at
      an <code>http(s)://</code> base URL.
    </p>
  </section>

  <section class="card">
    <h2>Package Index Schema (<code>radpm-package-index</code>)</h2>
    <p>
      The package index is a JSON object. Top-level fields observed in the published indexes
      (<code>radpm/dists/&lt;suite&gt;/main/packages.json</code>):
    </p>
    <ul>
      <li><code>schema</code> — string identifier, always <code>"radpm-package-index"</code>. Present in every index; a format marker.</li>
      <li><code>schema_version</code> — integer, currently <code>1</code>. Present in every index.</li>
      <li><code>repository</code> — human-readable repository name (e.g. <code>"RadicalPackages RADPx Package Repository"</code>). The <code>radpm</code> tool reads this into the repository <em>provider</em> field (default <code>"unknown"</code>), which then supplies each package's default provider.</li>
      <li><code>suite</code> — the suite the index belongs to (<code>"stable"</code> or <code>"experimental"</code>). Informational in the file; the tool takes the active suite from its <code>--suite</code> option rather than this field.</li>
      <li><code>component</code> — component name, currently always <code>"main"</code>. Present in the file; not consumed by the tool.</li>
      <li><code>packages</code> — array of package records (see below). Empty arrays are valid; the stable index currently ships <code>"packages": []</code>.</li>
      <li><code>signing_key</code> — <em>optional/observed</em>, index level. A GPG key fingerprint for the index as a whole. Present in the experimental index; the tool parses <code>signing_key</code> only on individual package records, not at index level, so at index level it is descriptive metadata.</li>
      <li><code>signature</code> — <em>optional/observed</em>, index level. URL of a detached ASCII-armored signature over the index file (e.g. <code>packages.json.asc</code>). Present in the experimental index; not consumed by the tool.</li>
    </ul>

    <h3>Package Record Fields</h3>
    <p>
      Each entry of <code>packages</code> is an object. The following fields are parsed by
      <code>parsePackage()</code> in <code>radpm.cpp</code>:
    </p>
    <ul>
      <li><code>name</code> — package name (required; the tool errors on a record with no name).</li>
      <li><code>version</code> — package version string, e.g. <code>"0.1.0-crimson"</code>, <code>"0.2.0-radpx"</code> (required).</li>
      <li><code>suite</code> — suite for this package; defaults to the repository suite when omitted.</li>
      <li><code>architecture</code> — target architecture slug. Observed values: <code>radpx-any</code> (architecture-independent) and <code>radpx-x86_64</code>.</li>
      <li><code>summary</code> — one-line human description.</li>
      <li><code>dependencies</code> — array of package names (or provided virtual names) this package requires. Used by <code>resolve</code>/<code>verify</code> to report unmet dependencies.</li>
      <li><code>provides</code> — array of virtual names this package satisfies. A dependency is considered met if some selected package's <code>name</code> or one of its <code>provides</code> entries matches. Example: <code>radpx-ncurses</code> provides <code>libncurses</code>, <code>libtinfo</code>, <code>libradpxc</code>, etc.</li>
      <li><code>archive</code> — location of the <code>.radpm</code> archive: an absolute <code>http(s)</code> URL or a path relative to the index. May be <code>null</code>/absent for pure metadata packages. On resolve the tool computes an absolute <code>archive_location</code> from this.</li>
      <li><code>sha256</code> — hex SHA-256 of the archive. This is the integrity check the tool actually enforces: <code>install</code> runs <code>sha256sum</code> on the downloaded archive and fails on mismatch. May be <code>null</code>/absent when there is no archive.</li>
      <li><code>bytes</code> — integer archive size in bytes (default <code>0</code>).</li>
      <li><code>docs</code> — documentation reference for the package. Observed values are relative doc paths (<code>"docs/radpx-os/0.1.4/api/"</code>, <code>"docs/radlib/0.2.0/api/"</code>) or a portal page (<code>"radpx-os.html"</code>).</li>
      <li><code>signature</code> — <em>optional</em>. URL of a detached ASCII-armored signature over the archive (the archive URL with a <code>.asc</code> suffix). May be <code>null</code>/absent. See GPG Signing below.</li>
      <li><code>signing_key</code> — <em>optional</em>. GPG key fingerprint that signed the archive. May be <code>null</code>/absent. Every signed package in the experimental index uses fingerprint <code>F3731ADBB37AFA120A7D5EBD20B2754CF3894789</code>.</li>
      <li><code>provider</code> — <em>optional</em>. Provider name; defaults to the repository's <code>repository</code> value when omitted (the current records omit it and inherit the default).</li>
      <li><code>repository_url</code> — <em>optional</em>. Provider repository URL; defaults to the repository root when omitted.</li>
      <li><code>supported_kernel_versions</code> — <em>optional/observed</em>. Array of version-range strings, e.g. <code>[">=0.1.0 <0.3.0"]</code>. Present on every current package record but <strong>not</strong> parsed by <code>radpm.cpp</code>; treat it as advisory metadata rather than an enforced constraint.</li>
    </ul>
  </section>

  <section class="card">
    <h2>Packagegroups</h2>
    <p>
      A packagegroup is a named, versioned set of package names that are meant to be selected together.
      RADPx OS images should select packagegroups first and add explicit packages only when needed:
      packagegroups keep terminal, desktop, networking, and SDK selections reproducible while still letting
      the resolver report missing dependencies. Selecting a group adds all of its member package names to
      the resolve set.
    </p>

    <h3>Packagegroup Index (<code>radpm-packagegroup-index</code>)</h3>
    <p>
      <code>radpm/dists/&lt;suite&gt;/main/packagegroups.json</code> is optional (repositories without it still
      load). Top-level fields mirror the package index — <code>schema</code>
      (<code>"radpm-packagegroup-index"</code>), <code>schema_version</code>, <code>repository</code>,
      <code>suite</code>, <code>component</code>, and an index-level <code>signing_key</code> (observed) — plus:
    </p>
    <ul>
      <li><code>packagegroups</code> — array of group entries. Each entry either carries the full group inline, or points to a separate descriptor file via <code>descriptor</code> (a path relative to the index) or <code>url</code>. When a <code>descriptor</code>/<code>url</code> is present the tool loads that file and reads the full group from it; the inline <code>name</code>/<code>version</code>/<code>provider</code>/<code>summary</code> fields in the index entry act as a preview.</li>
    </ul>

    <h3>Packagegroup Descriptor (<code>radpm-packagegroup</code>)</h3>
    <p>
      Each descriptor file (e.g. <code>packagegroups/radpx-terminal-base.json</code>) is parsed by
      <code>parseGroupDescriptor()</code>:
    </p>
    <ul>
      <li><code>schema</code> — <code>"radpm-packagegroup"</code>; <code>schema_version</code> — <code>1</code> (present in file, not parsed).</li>
      <li><code>name</code> — group name (required), e.g. <code>radpx-terminal-base</code>.</li>
      <li><code>version</code> — group version (required), e.g. <code>"0.2.0-beta.1"</code>.</li>
      <li><code>provider</code> — <em>optional</em>. Provider name; defaults to the repository provider.</li>
      <li><code>repository_url</code> — <em>optional</em>. Provider repository URL; defaults to the repository root.</li>
      <li><code>summary</code> — one-line human description.</li>
      <li><code>packages</code> — array of member package names.</li>
      <li><code>docs</code> — documentation reference (observed: <code>"radpx-os.html#packagegroups"</code>).</li>
    </ul>
    <p>
      Published experimental groups: <code>radpx-terminal-base</code>, <code>radpx-desktop-base</code>,
      <code>radpx-networking</code>, and <code>radpx-dev-sdk</code>.
    </p>
  </section>

  <section class="card">
    <h2>GPG Signing</h2>
    <p>
      RADpm artifacts are signed with the RadicalPackages archive key, fingerprint
      <code>F3731ADBB37AFA120A7D5EBD20B2754CF3894789</code>. The public key is committed at
      <code>keys/radical-packages-archive-key.asc</code> (ASCII-armored) and
      <code>keys/radical-packages-archive-key.gpg</code> (dearmored); the private key is never committed.
    </p>
    <p>
      Signatures are detached and ASCII-armored (<code>.asc</code>). Each signed package record carries a
      <code>signature</code> URL alongside its archive — the archive URL with a <code>.asc</code> suffix — and
      a <code>signing_key</code> fingerprint. The experimental package index also carries an index-level
      <code>signature</code> (over <code>packages.json</code>) and <code>signing_key</code>, and each
      packagegroup index carries an index-level <code>signing_key</code>.
    </p>
    <p>
      Note on enforcement: the <code>radpm</code> tool records and passes through these signing fields but does
      not itself invoke GPG. The integrity check it enforces on <code>install</code> is the <code>sha256</code>
      of each downloaded archive. Signature verification with the archive key is therefore a separate,
      operator-driven step against the published <code>.asc</code> files. (The same key also clear-signs and
      detach-signs the parallel Debian/APT channels — <code>InRelease</code> and <code>Release.gpg</code> — via
      <code>scripts/stage_github_release_apt_repo.py</code>.)
    </p>
  </section>

  <section class="card">
    <h2>Resolve Output (<code>radpm-lock</code>)</h2>
    <p>
      <code>radpm resolve</code>/<code>verify</code> emit a lock object that <code>radpm install</code> consumes.
      It is generated output rather than index schema, but documents how the fields above are used. Fields:
      <code>schema</code> (<code>"radpm-lock"</code>), <code>schema_version</code>, <code>repository</code>,
      <code>suite</code>, <code>index</code>, <code>selected_packages</code>,
      <code>selected_packagegroups</code>, <code>packages</code> (each resolved package record plus a computed
      <code>archive_location</code>), <code>diagnostics</code>, and <code>ok</code>. On a missing package or
      unmet dependency the tool instead emits a <code>radpm-error</code> object and exits non-zero.
    </p>
  </section>

  <section class="card">
    <h2>Example: A Real Package Record</h2>
    <p>
      Drawn verbatim from <code>radpm/dists/experimental/main/packages.json</code> (the
      <code>radpx-ncurses</code> record), showing an architecture-specific, signed package with virtual
      <code>provides</code>:
    </p>
    <pre><code>{
  "name": "radpx-ncurses",
  "version": "0.1.0-experimental",
  "suite": "experimental",
  "architecture": "radpx-x86_64",
  "summary": "RADPx ncurses/tinfo shared runtime and development headers for x86_64 terminal applications.",
  "dependencies": [
    "radpx-core"
  ],
  "provides": [
    "libncurses",
    "libncursesw",
    "libtinfo",
    "libradpxc",
    "radpx-terminal-ui-dev"
  ],
  "supported_kernel_versions": [
    ">=0.1.0 <0.3.0"
  ],
  "archive": "https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/radpx-os-0.2.0-beta.1/radpx-ncurses_0.1.0-experimental_radpx-x86_64.radpm",
  "sha256": "853b76699f78622fbe7877e4685128e802a96cd7e371479addbe47ef013ed714",
  "bytes": 607457,
  "docs": "radpx-os.html",
  "signature": "https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/radpx-os-0.2.0-beta.1/radpx-ncurses_0.1.0-experimental_radpx-x86_64.radpm.asc",
  "signing_key": "F3731ADBB37AFA120A7D5EBD20B2754CF3894789"
}</code></pre>
    <p>
      The enclosing index adds the object header and, in the experimental suite, index-level
      <code>signing_key</code> and <code>signature</code> fields:
    </p>
    <pre><code>{
  "schema": "radpm-package-index",
  "schema_version": 1,
  "repository": "RadicalPackages RADPx Package Repository",
  "suite": "experimental",
  "component": "main",
  "packages": [ /* ...records... */ ],
  "signing_key": "F3731ADBB37AFA120A7D5EBD20B2754CF3894789",
  "signature": "https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/radpx-os-0.2.0-beta.1/packages.json.asc"
}</code></pre>

    <h3>Example: A Packagegroup Descriptor</h3>
    <p>From <code>radpm/dists/experimental/main/packagegroups/radpx-terminal-base.json</code>:</p>
    <pre><code>{
  "schema": "radpm-packagegroup",
  "schema_version": 1,
  "name": "radpx-terminal-base",
  "version": "0.2.0-beta.1",
  "provider": "RadicalPackages",
  "repository_url": "https://github.com/Radical-Computer-Technologies/RadicalPackages",
  "summary": "Core RADPx terminal image package set with RADLib, ncurses, and vim-tiny.",
  "packages": [
    "radpx-core",
    "radlib",
    "radpx-ncurses",
    "radpx-vim-tiny"
  ],
  "docs": "radpx-os.html#packagegroups"
}</code></pre>
  </section>

  <section class="card">
    <h2>Related</h2>
    <div class="links">
      <a class="link-card" href="radpx-os.html"><strong>RADPx OS Hub</strong><span>Build profiles, packagegroups, and repository notes.</span></a>
      <a class="link-card" href="radpm/dists/experimental/main/packages.json"><strong>Experimental .radpm Index</strong><span>Machine-readable package records.</span></a>
      <a class="link-card" href="radpm/dists/experimental/main/packagegroups.json"><strong>Experimental Packagegroups</strong><span>Machine-readable group records.</span></a>
      <a class="link-card" href="keys/radical-packages-archive-key.asc"><strong>Archive Signing Key</strong><span>Public GPG key for verifying signatures.</span></a>
    </div>
  </section>
</main>
