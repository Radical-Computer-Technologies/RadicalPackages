#!/usr/bin/env python3
"""Cut a RADPx-OS signed release: build the x86 image profiles, package the
crimson image bundles, collect the (unchanged) .radpm package set + package-group
metadata from a prior release, generate SHA256SUMS + a release manifest, GPG-sign
every asset, and (optionally) publish the GitHub Release.

This is the repeatable replacement for the manual beta.1 assembly. Typical use:

  # stage locally (no publish), reusing the .radpm/package metadata from beta.1
  scripts/cut_radpx_os_release.py --version 0.1.4-beta.2 \
      --radpm-from-release radpx-os-0.1.4-beta.1

  # then, after eyeballing the staged assets, publish:
  scripts/cut_radpx_os_release.py --version 0.1.4-beta.2 \
      --radpm-from-release radpx-os-0.1.4-beta.1 --skip-build --publish

Prereqs: radbuild + cmake for the builds; gh authenticated; the RADPx package GPG
signing key unlocked in the agent (RADICAL_PACKAGE_GPG_KEY, default below).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

REPO = "Radical-Computer-Technologies/RadicalPackages"
GPG_KEY = os.environ.get("RADICAL_PACKAGE_GPG_KEY", "F3731ADBB37AFA120A7D5EBD20B2754CF3894789")

# Each profile: bundle suffix, artifact dir under the OS repo, and the image file
# basenames produced by the build for that target.
PROFILES = {
    "terminal-interactive": {
        "dir": "x86_64-grub-terminal",
        "build_dir": "build/embedded/x86_64_grub_terminal_interactive",
        "iso": "radkernel-x86-64-grub-terminal-interactive.iso",
        "ext4": "rad-rootfs-interactive.ext4",
        "fat": "rad-fat32-interactive.img",
        "kind": "terminal",
        "desc": "x86_64 GRUB framebuffer terminal (interactive login)",
    },
    "terminal-smoke": {
        "dir": "x86_64-grub-terminal",
        "build_dir": "build/embedded/x86_64_grub_terminal_smoke",
        "iso": "radkernel-x86-64-grub-terminal-smoke.iso",
        "ext4": "rad-rootfs-smoke.ext4",
        "fat": "rad-fat32-smoke.img",
        "kind": "terminal",
        "desc": "x86_64 GRUB framebuffer terminal (autologin/autotest smoke)",
    },
    "wm": {
        "dir": "x86_64-grub-wm",
        "build_dir": "build/embedded/x86_64_grub_slint",
        "iso": "radkernel-x86-64-grub-wm.iso",
        "ext4": "rad-rootfs.ext4",
        "fat": "rad-fat32.img",
        "kind": "wm",
        "desc": "x86_64 GRUB RADCompositor/Slint window-manager image",
    },
}


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"  $ {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_profiles(os_repo: Path, jobs: int) -> None:
    print("== building image profiles ==")
    # Terminal interactive + smoke via the variants script (produces
    # artifacts/rad/x86_64-grub-terminal-<name>/).
    run(["bash", "tools/embedded/build_x86_64_grub_terminal_variants.sh"], cwd=os_repo)
    # WM (RADCompositor) profile: configure the Slint build for the wm UI profile with
    # vim-tiny, then build the ISO target (leaves images in build/embedded/x86_64_grub_slint/).
    wm_build = "build/embedded/x86_64_grub_slint"
    run(["cmake", "-S", "tools/embedded/x86_64_grub_slint", "-B", wm_build,
         "-DRAD_X86_UI_PROFILE=wm",
         "-DRAD_X86_TERMINAL_AUTOTEST_NANO=false", "-DRAD_X86_TERMINAL_AUTOLOGIN=false",
         "-DRAD_RKCONFIG_TERMINAL_NANO=false", "-DRAD_RKCONFIG_TERMINAL_NANO_VARIANT=none",
         "-DRAD_RKCONFIG_TERMINAL_VIM=true", "-DRAD_RKCONFIG_TERMINAL_VIM_VARIANT=tiny",
         "-DRAD_X86_MAX_USER_PROCESSES=128", "-DRAD_RKCONFIG_KERNEL_MAX_TASKS=128",
         "-DRAD_RKCONFIG_KERNEL_MAX_PROCESSES=128",
         "-DRAD_RKCONFIG_KERNEL_TASK_STACK_BYTES=524288",
         "-DRAD_RKCONFIG_KERNEL_TASK_STACK_POLICY=dynamic"], cwd=os_repo)
    run(["cmake", "--build", wm_build, "--target", "radkernel_x86_64_grub_slint_iso",
         "-j", str(jobs)], cwd=os_repo)


def stage_bundle(os_repo: Path, version: str, name: str, spec: dict, out: Path) -> Path:
    """Assemble the x86_64-grub-<profile>/ dir (image files + README + run script +
    SHA256SUMS) and tar it as radpx-os-crimson_<version>_x86_64-grub-<name>.tar.gz."""
    bundle_dirname = f"x86_64-grub-{name}"
    staging = out / "bundle-staging" / bundle_dirname
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bd = os_repo / spec["build_dir"]
    # Terminal variants copy their images to artifacts/rad/x86_64-grub-terminal-<name>/;
    # the wm build leaves them in the build dir. Resolve either source.
    art = os_repo / "artifacts" / "rad" / f"x86_64-grub-terminal-{name.split('-', 1)[1]}" if spec["kind"] == "terminal" else bd
    def find(cands: list[Path]) -> Path:
        for c in cands:
            if c.exists():
                return c
        raise FileNotFoundError(f"missing image for {name}: tried {cands}")

    iso_src = find([art / spec["iso"], bd / spec["iso"], bd / "radkernel-x86-64-grub-terminal.iso", bd / "radkernel-x86-64-grub-wm.iso"])
    ext4_src = find([art / spec["ext4"], bd / spec["ext4"], bd / "rad-rootfs.ext4"])
    fat_src = find([art / spec["fat"], bd / spec["fat"], bd / "rad-fat32.img"])

    iso = staging / spec["iso"]
    ext4 = staging / spec["ext4"]
    fat = staging / spec["fat"]
    shutil.copy2(iso_src, iso)
    shutil.copy2(ext4_src, ext4)
    shutil.copy2(fat_src, fat)

    run_sh = staging / f"run-rad-vm-{name}.sh"
    run_sh.write_text(
        "#!/usr/bin/env bash\nset -euo pipefail\ncd \"$(dirname \"$0\")\"\n"
        "qemu-system-x86_64 -m 4G -smp 4 -enable-kvm -cpu host -vga std \\\n"
        f"  -cdrom {iso.name} \\\n"
        f"  -drive if=none,id=raddisk,format=raw,file={ext4.name} -device virtio-blk-pci,drive=raddisk,disable-modern=on \\\n"
        f"  -drive if=none,id=radfat,format=raw,file={fat.name} -device virtio-blk-pci,drive=radfat,disable-modern=on \\\n"
        "  -serial file:rad-vm-serial.log -display gtk -no-reboot\n"
    )
    run_sh.chmod(0o755)

    readme = staging / "README.txt"
    readme.write_text(
        f"RADPx-OS {spec['desc']}\nRADPx-OS Crimson {version}\n\n"
        f"Run with QEMU from this directory (KVM recommended):\n\n"
        f"  ./{run_sh.name}\n\n"
        "Default login is root using the rkconfig-staged password for this image.\n"
    )

    # per-bundle SHA256SUMS
    sums = staging / "SHA256SUMS"
    lines = []
    for p in sorted(staging.iterdir(), key=lambda x: x.name):
        if p.name == "SHA256SUMS":
            continue
        lines.append(f"{sha256(p)}  {p.name}")
    sums.write_text("\n".join(lines) + "\n")

    tar_name = f"radpx-os-crimson_{version}_x86_64-grub-{name}.tar.gz"
    tar_path = out / tar_name
    with tarfile.open(tar_path, "w:gz") as tf:
        tf.add(staging, arcname=bundle_dirname)
    print(f"  bundled {tar_name}  ({tar_path.stat().st_size} bytes)")
    return tar_path


def collect_radpm(out: Path, from_release: str) -> list[Path]:
    """Download the unchanged .radpm packages + package-group JSONs from a prior
    release (userland package metadata does not change with the OS image)."""
    print(f"== collecting .radpm/package metadata from {from_release} ==")
    dl = out / "radpm-src"
    if dl.exists():
        shutil.rmtree(dl)
    dl.mkdir(parents=True, exist_ok=True)
    run(["gh", "release", "download", from_release, "--repo", REPO, "-D", str(dl)])
    keep: list[Path] = []
    for p in sorted(dl.iterdir()):
        n = p.name
        if n.endswith(".asc") or n.endswith(".tar.gz"):
            continue
        if "release-manifest" in n or n == "SHA256SUMS":
            continue
        keep.append(p)
    return keep


def gpg_sign(path: Path) -> Path:
    asc = path.with_name(path.name + ".asc")
    if asc.exists():
        asc.unlink()
    run(["gpg", "--batch", "--yes", "--local-user", GPG_KEY,
         "--armor", "--detach-sign", "--output", str(asc), str(path)])
    return asc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--version", required=True, help="Release version, e.g. 0.1.4-beta.2")
    ap.add_argument("--os-repo", type=Path, default=Path(__file__).resolve().parents[2] / "RADPx-OS")
    ap.add_argument("--radpm-from-release", required=True, help="Prior release tag to reuse .radpm/package metadata from")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--skip-build", action="store_true", help="Reuse existing build artifacts")
    ap.add_argument("--publish", action="store_true", help="Create/upload the GitHub Release (omit to stage only)")
    ap.add_argument("--prerelease", action="store_true", default=True)
    args = ap.parse_args()

    version = args.version
    tag = f"radpx-os-{version}"
    os_repo = args.os_repo.resolve()
    out = Path(__file__).resolve().parents[1] / "release-staging" / tag
    out.mkdir(parents=True, exist_ok=True)
    print(f"== staging {tag} in {out} ==")

    if not args.skip_build:
        build_profiles(os_repo, args.jobs)

    assets: list[Path] = []
    for name, spec in PROFILES.items():
        assets.append(stage_bundle(os_repo, version, name, spec, out))

    for p in collect_radpm(out, args.radpm_from_release):
        dst = out / p.name
        shutil.copy2(p, dst)
        assets.append(dst)

    # top-level SHA256SUMS over all assets
    sums = out / "SHA256SUMS"
    sums.write_text("\n".join(f"{sha256(a)}  {a.name}" for a in sorted(assets, key=lambda x: x.name)) + "\n")
    assets.append(sums)

    # sign every asset
    print("== GPG-signing assets ==")
    for a in list(assets):
        if not a.name.endswith(".asc"):
            assets.append(gpg_sign(a))

    # release manifest (asset catalog with sha256)
    manifest = out / f"{tag}-release-manifest.json"
    manifest.write_text(json.dumps({
        "release": tag,
        "version": version,
        "assets": [{"name": a.name, "bytes": a.stat().st_size, "sha256": sha256(a)}
                   for a in sorted(assets, key=lambda x: x.name)],
    }, indent=2) + "\n")
    assets.append(manifest)

    print(f"\n== staged {len(assets)} assets in {out} ==")
    for a in sorted(assets, key=lambda x: x.name):
        print(f"   {a.name}")

    if args.publish:
        print(f"\n== publishing GitHub Release {tag} ==")
        create = ["gh", "release", "create", tag, "--repo", REPO,
                  "--title", f"RADPx-OS Crimson {version}",
                  "--notes", f"RADPx-OS Crimson {version} — see the RADPx-OS CHANGELOG.",
                  "--target", "main"]
        if args.prerelease:
            create.append("--prerelease")
        create += [str(a) for a in sorted(assets, key=lambda x: x.name)]
        run(create)
        print(f"published: https://github.com/{REPO}/releases/tag/{tag}")
    else:
        print("\n(staged only; re-run with --publish to create the GitHub Release)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
