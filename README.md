# Radical Packages

Distribution repository for Radical Computer Technologies packages and public documentation.

GitHub Pages URL:

<https://radical-computer-technologies.github.io/RadicalPackages/>

## Package Repositories

### Debian Systems / Ubuntu Stable

RadicalPackages publishes Debian packages as flat APT repositories stored in GitHub Releases. The Git repository keeps docs, suite manifests, signing keys, and automation scripts; package binaries are not committed.

Add the stable repository:

```bash
sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://radical-computer-technologies.github.io/RadicalPackages/keys/radical-packages-archive-key.asc \
  | sudo gpg --dearmor -o /etc/apt/keyrings/radical-packages.gpg

sudo tee /etc/apt/sources.list.d/radical-computer-technologies.sources >/dev/null <<'EOF'
Types: deb
URIs: https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/apt-stable
Suites: ./
Signed-By: /etc/apt/keyrings/radical-packages.gpg
Architectures: amd64 arm64
EOF

sudo apt update
```

### Debian Systems / Ubuntu Experimental

Add the experimental repository when you want beta applications such as RADBard or development RADLib releases:

```bash
sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://radical-computer-technologies.github.io/RadicalPackages/keys/radical-packages-archive-key.asc \
  | sudo gpg --dearmor -o /etc/apt/keyrings/radical-packages.gpg

sudo tee /etc/apt/sources.list.d/radical-computer-technologies-experimental.sources >/dev/null <<'EOF'
Types: deb
URIs: https://github.com/Radical-Computer-Technologies/RadicalPackages/releases/download/apt-experimental
Suites: ./
Signed-By: /etc/apt/keyrings/radical-packages.gpg
Architectures: amd64 arm64
EOF

sudo apt update
```

Install a package:

```bash
sudo apt install <package>
```

The public signing key is tracked at `keys/radical-packages-archive-key.asc`. The private signing key is never committed.

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

Experimental packages are allowed to move faster than stable. RADBard, RadBuild, and RADPx-OS documentation live here while they are still beta, and RADLib `0.1.1` development packages should be published here until promoted.

| Package | Description | Install |
| --- | --- | --- |
| `radbard` | RADBard music and audio composition suite beta. | `sudo apt install radbard` |
| `radbuild` | Graph-based embedded-system build framework CLI with RADPx-OS image provider support. | `sudo apt install radbuild` |
| `radbuild-radhdl` | Packaged RadHDL catalog and source assets for RadBuild. | `sudo apt install radbuild-radhdl` |
| `radbuild-server` | Optional RadBuild server, client, worker, and review DB tools. | `sudo apt install radbuild-server` |
| `radbuild-vscode-support` | VSCode extension source and compiled support files for RadBuild. | `sudo apt install radbuild-vscode-support` |
| `radbuild-doc` | RadBuild documentation package. | `sudo apt install radbuild-doc` |
| `radlib-embedded-kernel` | Experimental RADPx-OS kernel service layer for simulator and bare-metal HAL backends. | `sudo apt install radlib-embedded-kernel` |

## Documentation

- [Documentation Index](docs/)
- [RADLib 0.2.0 API Documentation](docs/radlib/0.2.0/api/)
- [RadHDL 0.2.1 Documentation](docs/radhdl/0.2.1/)
- [RadBuild 0.2.1 Documentation](docs/radbuild/0.2.1/)
- [RADPx-OS Crimson 0.2.0 API Documentation](docs/radix-os/0.2.0/api/)

Documentation is organized by product, release channel, and major version family. Use exact version paths such as `docs/radlib/0.1.0/` and `docs/radhdl/0.2.0/`; newer exact versions supersede older versions without a `current` alias.

## Repository Layout

```text
debian/
  suites/
keys/
  radical-packages-archive-key.asc
docs/
  radlib/0.1.0/api/
  radhdl/0.2.1/
  radbuild/0.2.1/
  radix-os/0.1.3/api/
scripts/
  stage_github_release_apt_repo.py
  publish_github_release_assets.py
  update_debian_repo.sh
  update_radlib_docs.sh
```

## Maintainer Workflow

Create a signed flat APT repository for the stable channel:

```bash
export RADICAL_PACKAGE_GPG_KEY=F3731ADBB37AFA120A7D5EBD20B2754CF3894789

scripts/stage_github_release_apt_repo.py \
  --suite stable \
  --version 0.1.0 \
  --out-dir release-staging/apt-stable \
  --force \
  ../RADLib/build/package/deb/out/*.deb \
  ../RadBuild/dist/debian/*.deb
```

Create an experimental channel:

```bash
scripts/stage_github_release_apt_repo.py \
  --suite experimental \
  --version 0.2.1-beta.1 \
  --out-dir release-staging/apt-experimental \
  --force \
  ../RADBard/release/radbard-0.1.0-x86_64.deb \
  ../RadBuild/dist/debian/*.deb
```

Publish the staged assets to GitHub Releases:

```bash
gh auth login

scripts/publish_github_release_assets.py \
  --tag apt-experimental \
  --title "RadicalPackages Experimental APT Channel" \
  --clobber \
  release-staging/apt-experimental
```

Use `--dry-run` on the publish script to inspect the `gh` command without changing GitHub.

Regenerate RADLib Doxygen documentation:

```bash
scripts/update_radlib_docs.sh ../RADLib
scripts/update_radlib_docs.sh ../RADLib 0.1.0
```

Regenerate RADPx-OS and RadBuild documentation:

```bash
scripts/update_radix_docs.sh ../RADPx-OS 0.1.0
scripts/update_radbuild_docs.sh ../RadBuild 0.2.1
```
