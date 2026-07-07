# Radical Packages

Distribution repository for Radical Computer Technologies packages and public documentation.

GitHub Pages URL:

<https://radical-computer-technologies.github.io/RadicalPackages/>

## Debian / Ubuntu Repository

This repository currently publishes x86_64 / amd64 Debian packages for RADBard.

Add the repository:

```bash
sudo tee /etc/apt/sources.list.d/radical-computer-technologies.sources >/dev/null <<'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: stable
Components: main
Architectures: amd64
Trusted: yes
EOF

sudo apt update
```

Install RADBard:

```bash
sudo apt install radbard
```

`Trusted: yes` is used while the repository is in early unsigned beta form. Replace this with a signed repository key before broad public release.

## Documentation

- [RADLib API Documentation](docs/radlib/api/)

## Repository Layout

```text
debian/
  dists/stable/main/binary-amd64/
  pool/main/
docs/
  radlib/api/
scripts/
  update_debian_repo.sh
  update_radlib_docs.sh
```

## Maintainer Workflow

Publish a Debian package:

```bash
scripts/update_debian_repo.sh ../RADBard/release/radbard-0.1.0-x86_64.deb
```

Regenerate RADLib Doxygen documentation:

```bash
scripts/update_radlib_docs.sh ../RADLib
```
