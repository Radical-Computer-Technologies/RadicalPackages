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

## RadBuild Windows MSI Assets

RadBuild Windows installers are immutable release assets, not APT repository
members. Build them on a Windows host or CI runner, then upload the MSI to the
matching RadBuild prerelease tag:

```powershell
python build_release.py --version 0.2.2-beta.2 `
  --tool-profile radbuild `
  --release-dir $env:RUNNER_TEMP\radbuild-release-windows `
  --no-local-package --no-radtools-publish

python scripts\build_windows_msi.py --version 0.2.2-beta.2 `
  --release-dir $env:RUNNER_TEMP\radbuild-release-windows `
  --out-dir dist\windows
```

Publish with:

```bash
scripts/publish_github_release_assets.py \
  --tag radbuild-0.2.2-beta.2 \
  --title "RadBuild 0.2.2-beta.2" \
  --prerelease \
  dist/windows/radbuild-0.2.2-beta.2-windows-x86_64.msi
```

## RADPx OS Images

RADPx OS images should be uploaded as compressed release bundles, not committed:

```bash
tar --sparse -czf radpx-os-crimson_0.1.3-beta.1_x86_64-grub-terminal-interactive.tar.gz \
  -C ../RADPx-OS/artifacts/radpx/x86_64-grub-terminal \
  radpxkernel-x86-64-grub-terminal.iso \
  radpx-rootfs.ext4 \
  radpx-fat32.img \
  make-radpx-rootfs-ext4.sh \
  run-radpx-vm.sh \
  SHA256SUMS
```

Upload these bundles and any `.radpm` archives with `scripts/publish_github_release_assets.py` to the matching immutable release, such as `radpx-os-0.1.5-beta.1`.

The repeatable way to build, bundle, collect the unchanged `.radpm` metadata, sign, and
(optionally) publish an OS release is `scripts/cut_radpx_os_release.py`. It stages by default
and only creates the GitHub Release when `--publish` is passed:

```bash
# stage locally (build all three x86 profiles, bundle, collect prior .radpm, GPG-sign)
scripts/cut_radpx_os_release.py --version 0.1.5-beta.1 \
  --radpm-from-release radpx-os-0.1.4-beta.1

# then, after eyeballing the staged assets, publish:
scripts/cut_radpx_os_release.py --version 0.1.5-beta.1 \
  --radpm-from-release radpx-os-0.1.4-beta.1 --skip-build --publish
```

Signing uses the passphrase-protected package key, so unlock it in your local GPG agent
before staging (an unattended agent will time out on the detached-signature step).
