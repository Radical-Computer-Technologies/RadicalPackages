# RadicalPackages Release Hosting

RadicalPackages uses GitHub Releases for binary artifacts and GitHub Pages for human documentation.

## Required Local Setup

```bash
sudo apt install gh dpkg-dev apt-utils gnupg jq tar zstd xz-utils
gh auth login
gh auth status
export RADICAL_PACKAGE_GPG_KEY=F3731ADBB37AFA120A7D5EBD20B2754CF3894789
```

The public APT key is committed under `keys/`. The private key and revocation certificate must remain outside this repository.

For unattended signing, either unlock the key in your local GPG agent first or use one of the script's loopback options:

```bash
scripts/stage_github_release_apt_repo.py ... --gpg-passphrase-file /path/to/local/passphrase-file
```

The script also accepts `RADICAL_PACKAGE_GPG_PASSPHRASE` for CI-style environments. Do not commit passphrase files or private key exports.

## Version Rules

- Stable release-set versions use `x.y.z`, such as `0.2.1`.
- Experimental release-set versions use `x.y.z-beta` or `x.y.z-beta.N`, such as `0.2.1-beta.1`.
- Mutable APT channel release tags are `apt-stable` and `apt-experimental`.
- Immutable archive tags should use `v0.2.1` or `v0.2.1-beta.1`.

## Stage APT Assets

```bash
scripts/stage_github_release_apt_repo.py \
  --suite experimental \
  --version 0.2.1-beta.1 \
  --out-dir release-staging/apt-experimental \
  --force \
  ../RadBuild/dist/debian/*.deb
```

The staged directory contains:

- package `.deb` files
- `Packages`
- `Packages.gz`
- `Release`
- `InRelease`
- `Release.gpg`
- `SHA256SUMS`
- `release-manifest.json`

## Publish APT Assets

Dry run:

```bash
scripts/publish_github_release_assets.py \
  --tag apt-experimental \
  --title "RadicalPackages Experimental APT Channel" \
  --clobber \
  --dry-run \
  release-staging/apt-experimental
```

Publish:

```bash
scripts/publish_github_release_assets.py \
  --tag apt-experimental \
  --title "RadicalPackages Experimental APT Channel" \
  --clobber \
  release-staging/apt-experimental
```

For immutable archive releases, use a versioned tag and `--prerelease` for beta releases:

```bash
scripts/publish_github_release_assets.py \
  --tag v0.2.1-beta.1 \
  --title "RadicalPackages 0.2.1 beta 1" \
  --prerelease \
  release-staging/apt-experimental
```

## RADPx OS Images

RADPx OS images should be uploaded as compressed release bundles, not committed:

```bash
tar --sparse -czf radix-os-crimson_0.1.3-beta.1_x86_64-grub-terminal-interactive.tar.gz \
  -C ../RADPx-OS/artifacts/radix/x86_64-grub-terminal \
  radixkernel-x86-64-grub-terminal.iso \
  radix-rootfs.ext4 \
  radix-fat32.img \
  make-radix-rootfs-ext4.sh \
  run-radix-vm.sh \
  SHA256SUMS
```

Upload these bundles and any `.radpm` archives with `scripts/publish_github_release_assets.py` to the matching immutable release, such as `radix-os-0.2.0-beta.1`.
