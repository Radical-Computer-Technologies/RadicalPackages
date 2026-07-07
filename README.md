# Radical Packages

Distribution repository for Radical Computer Technologies packages and public documentation.

GitHub Pages URL:

<https://radical-computer-technologies.github.io/RadicalPackages/>

## Package Repositories

### Debian Systems / Ubuntu Stable

This repository publishes Debian packages for `amd64` and `arm64` where builds are available.

Add the stable repository:

```bash
sudo tee /etc/apt/sources.list.d/radical-computer-technologies.sources >/dev/null <<'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: stable
Components: main
Architectures: amd64 arm64
Trusted: yes
EOF

sudo apt update
```

### Debian Systems / Ubuntu Experimental

Add the experimental repository when you want beta applications such as RADBard or development RADLib releases:

```bash
sudo tee /etc/apt/sources.list.d/radical-computer-technologies-experimental.sources >/dev/null <<'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: experimental
Components: main
Architectures: amd64 arm64
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

Stable RADLib packages currently track the `0.1.0` release line. ABI-pinned packages use the `-0-1` suffix so applications can depend on a known RADLib ABI line.

| Package | Description | Install |
| --- | --- | --- |
| `radlib` | Aggregate RADLib package that installs runtime, development files, docs, examples, and tools. | `sudo apt install radlib` |
| `radlib-runtime` | Latest RADLib runtime meta-package. | `sudo apt install radlib-runtime` |
| `radlib-runtime-0-1` | RADLib ABI 0.1 runtime meta-package. | `sudo apt install radlib-runtime-0-1` |
| `radlib-dev` | Latest RADLib public headers and CMake package files. | `sudo apt install radlib-dev` |
| `radlib-dev-0-1` | RADLib ABI 0.1 public headers and CMake package files. | `sudo apt install radlib-dev-0-1` |
| `radlib-doc` | RADLib generated API documentation package. | `sudo apt install radlib-doc` |
| `radlib-examples` | RADLib example applications and sample projects. | `sudo apt install radlib-examples` |
| `radlib-tools` | RADLib SDK tools and protocol generator. | `sudo apt install radlib-tools` |

Targeted module installs are also available. Use the unversioned package for the current line or the `-0-1` package when you need to pin the RADLib 0.1 ABI runtime line.

```bash
sudo apt install radlib-core
sudo apt install radlib-ui
sudo apt install radlib-media
sudo apt install radlib-dsp
sudo apt install radlib-fpga
sudo apt install radlib-web
```

Current module package names include `radlib-core`, `radlib-ui`, `radlib-net`, `radlib-dsp`, `radlib-media`, `radlib-database`, `radlib-web`, `radlib-fpga`, `radlib-serial`, `radlib-logging`, `radlib-settings`, `radlib-cli`, `radlib-installer`, `radlib-security`, `radlib-input`, `radlib-display`, `radlib-device`, `radlib-power`, `radlib-service`, `radlib-update`, and `radlib-data-structures`.

## Experimental Packages

Experimental packages are allowed to move faster than stable. RADBard lives here while it is still beta, and RADLib `0.1.1` development packages should be published here until promoted.

| Package | Description | Install |
| --- | --- | --- |
| `radbard` | RADBard music and audio composition suite beta. | `sudo apt install radbard` |

## Documentation

- [RADLib 0.1.0 API Documentation](docs/radlib/0.1.0/api/)
- [Current RADLib API Documentation](docs/radlib/api/)

RADLib Doxygen output is versioned so stable and experimental APIs can be compared directly. Use `docs/radlib/0.1.0/` for stable `0.1.0` and `docs/radlib/0.1.1/` for the experimental `0.1.1` line once published.

## Repository Layout

```text
debian/
  dists/stable/main/binary-amd64/
  dists/stable/main/binary-arm64/
  dists/experimental/main/binary-amd64/
  dists/experimental/main/binary-arm64/
  pool/main/
  suites/
docs/
  radlib/0.1.0/api/
  radlib/0.1.1/api/
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
scripts/update_radlib_docs.sh ../RADLib 0.1.0
```
