# Radical Packages

Distribution repository for Radical Computer Technologies packages and public documentation.

GitHub Pages URL:

<https://radical-computer-technologies.github.io/RadicalPackages/>

## Package Repositories

### Debian Systems / Ubuntu Stable

This repository currently publishes x86_64 / amd64 Debian packages.

Add the stable repository:

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

### Debian Systems / Ubuntu Experimental

Add the experimental repository when you want beta applications such as RADBard:

```bash
sudo tee /etc/apt/sources.list.d/radical-computer-technologies-experimental.sources >/dev/null <<'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: experimental
Components: main
Architectures: amd64
Trusted: yes
EOF

sudo apt update
```

Install a package:

```bash
sudo apt install <package>
```

`Trusted: yes` is used while the repository is in early unsigned beta form. Replace this with a signed repository key before broad public release.

## Stable Packages

| Package | Description | Install |
| --- | --- | --- |
| `radlib-runtime` | RADLib shared runtime libraries required by RADLib-based apps. | `sudo apt install radlib-runtime` |
| `radlib-dev` | RADLib public headers and CMake package files. | `sudo apt install radlib-dev` |
| `radlib-doc` | RADLib generated API documentation package. | `sudo apt install radlib-doc` |
| `radlib-examples` | RADLib example applications and sample projects. | `sudo apt install radlib-examples` |
| `radlib-tools` | RADLib SDK tools and protocol generator. | `sudo apt install radlib-tools` |
| `radlib` | Aggregate RADLib package that installs runtime, development files, docs, examples, and tools. | `sudo apt install radlib` |

## Experimental Packages

| Package | Description | Install |
| --- | --- | --- |
| `radbard` | RADBard music and audio composition suite beta. | `sudo apt install radbard` |

## Documentation

- [RADLib API Documentation](docs/radlib/api/)

## Repository Layout

```text
debian/
  dists/stable/main/binary-amd64/
  dists/experimental/main/binary-amd64/
  pool/main/
  suites/
docs/
  radlib/api/
scripts/
  update_debian_repo.sh
  update_radlib_docs.sh
```

## Maintainer Workflow

Publish Debian packages:

```bash
scripts/update_debian_repo.sh \
  ../RADLib/build/package/deb/out/*.deb \
  ../RADBard/release/radbard-0.1.0-x86_64.deb
```

Regenerate RADLib Doxygen documentation:

```bash
scripts/update_radlib_docs.sh ../RADLib
```
