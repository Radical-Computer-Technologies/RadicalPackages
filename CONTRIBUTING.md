# Contributing to RadicalPackages

RadicalPackages is the distribution repository and public documentation portal
for Radical Computer Technologies. It publishes Debian packages as flat APT
repositories stored in GitHub Releases; the Git repository keeps docs, suite
manifests, signing keys, and automation scripts. Package binaries are not
committed.

Published site: <https://radical-computer-technologies.github.io/RadicalPackages/>

## Repository layout

```text
debian/suites/                      APT suite manifests
keys/radical-packages-archive-key.asc   public signing key (private key never committed)
docs/                               published HTML docs by product/version
  radlib/<version>/api/
  radhdl/<version>/
  radbuild/0.2.1/
  radix-os/<version>/api/
docs_src/                           documentation sources
scripts/                            staging/publishing/doc-regeneration helpers
release-staging/                    generated APT channel staging
```

## How docs are organized

Documentation is organized by product, release channel, and major version
family. Use exact version paths such as `docs/radlib/0.1.0/` and
`docs/radhdl/0.2.0/`; newer exact versions supersede older ones without a
`current` alias. The top-level `index.md`, `packages.md`, `RELEASES.md`, and the
per-product pages (`radlib.md`, `radbuild.md`, `radix-os.md`, `radbard.md`) are
the portal's landing content.

## Maintainer workflow

Stage a signed flat APT repository (stable channel):

```bash
export RADICAL_PACKAGE_GPG_KEY=F3731ADBB37AFA120A7D5EBD20B2754CF3894789

scripts/stage_github_release_apt_repo.py \
  --suite stable --version 0.1.0 \
  --out-dir release-staging/apt-stable --force \
  ../RADLib/build/package/deb/out/*.deb \
  ../RadBuild/dist/debian/*.deb
```

Stage an experimental channel with `--suite experimental` and a beta version.
Publish staged assets to GitHub Releases:

```bash
gh auth login
scripts/publish_github_release_assets.py \
  --tag apt-experimental \
  --title "RadicalPackages Experimental APT Channel" \
  --clobber release-staging/apt-experimental
```

Use `--dry-run` on the publish script to inspect the `gh` command without
changing GitHub.

Regenerate documentation from sibling checkouts:

```bash
scripts/update_radlib_docs.sh ../RADLib
scripts/update_radix_docs.sh ../RADPx-OS 0.1.0
scripts/update_radbuild_docs.sh ../RadBuild 0.2.1
```

## Conventions

- Never commit package binaries or private signing keys.
- Keep the public signing key at `keys/radical-packages-archive-key.asc`.
- Keep commits small, incremental, and green; work on a topic branch rather than
  committing directly to `main`. Commits are authored as the maintainer.
