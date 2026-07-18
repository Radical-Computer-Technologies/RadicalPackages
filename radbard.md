<link rel="stylesheet" href="assets/site.css">

<main class="page">
  <nav class="nav">
    <a class="brand" href="./">Radical Packages</a>
    <div class="nav-links">
      <a href="./">Home</a>
      <a href="packages.html">Packages</a>
      <a href="radix-os.html">RADPx OS</a>
      <a href="docs/">Docs</a>
    </div>
  </nav>

  <section class="hero">
    <div class="eyebrow">Experimental Package</div>
    <h1>RADBard Packages</h1>
    <p class="lead">
      RADBard is the experimental music and audio composition suite. It currently lives in the experimental repository while the editor, notation, mixer, automation, and audio backend stabilize.
    </p>
    <div class="status-row">
      <span class="pill"><strong>Version:</strong> 0.1.0 beta</span>
      <span class="pill"><strong>Suite:</strong> experimental</span>
      <span class="pill"><strong>Architecture:</strong> amd64 currently</span>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>Install RADBard</h2>
      <p>Add the experimental repository from the home page, then install RADBard.</p>
      <div class="command"><code>sudo apt update
sudo apt install radbard</code></div>
    </article>

    <article class="card">
      <h2>Runtime Dependencies</h2>
      <p>RADBard depends on targeted RADLib runtime packages, including UI, media, and DSP modules.</p>
      <div class="package-list">
        <div class="package"><code>radlib-ui-0-1</code><br><span>Editor and UI primitives.</span></div>
        <div class="package"><code>radlib-media-0-1</code><br><span>MIDI, audio, and MusicXML helpers.</span></div>
        <div class="package"><code>radlib-dsp-0-1</code><br><span>EQ, FFT, and DSP primitives.</span></div>
      </div>
    </article>
  </section>

  <section class="card">
    <h2>Published Package</h2>
    <table class="package-table">
      <thead><tr><th>Package</th><th>Purpose</th><th>Install</th></tr></thead>
      <tbody>
        <tr><td><code>radbard</code></td><td>RADBard music and audio composition suite beta.</td><td><code>sudo apt install radbard</code></td></tr>
      </tbody>
    </table>
  </section>

  <details class="doc-group">
    <summary>Repository Metadata</summary>
      <div class="links">
        <a class="link-card" href="debian/dists/experimental/main/binary-amd64/Packages"><strong>Experimental amd64</strong><span>Package index</span></a>
        <a class="link-card" href="debian/pool/main/r/radbard/"><strong>Package Pool</strong><span>Published RADBard .deb files</span></a>
      </div>
  </details>

  <section class="card">
      <h2>Related Packages</h2>
      <div class="links">
        <a class="link-card" href="radlib.html"><strong>RADLib</strong><span>Required runtime package line</span></a>
      </div>
  </section>
</main>
