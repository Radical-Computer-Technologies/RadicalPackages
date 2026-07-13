#!/usr/bin/env python3
"""Stage a flat APT repository for publication as GitHub Release assets."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any


ASSET_LIMIT_BYTES = 2 * 1024 * 1024 * 1024
STABLE_VERSION = re.compile(r"^\d+\.\d+\.\d+$")
EXPERIMENTAL_VERSION = re.compile(r"^\d+\.\d+\.\d+-beta(?:\.\d+)?$")


def run(cmd: list[str], cwd: Path | None = None, stdout: Any = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=True, text=True, stdout=stdout)


def read_cmd(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_suite_packages(root: Path, suite: str) -> set[str]:
    manifest = root / "debian" / "suites" / f"{suite}.packages"
    if not manifest.exists():
        raise FileNotFoundError(f"missing suite manifest: {manifest}")
    packages: set[str] = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        clean = line.split("#", 1)[0].strip()
        if clean:
            packages.add(clean)
    return packages


def package_field(path: Path, field: str) -> str:
    return read_cmd(["dpkg-deb", "-f", str(path), field])


def copy_package(path: Path, out_dir: Path, allowed: set[str], include_unlisted: bool) -> dict[str, Any] | None:
    name = package_field(path, "Package")
    version = package_field(path, "Version")
    arch = package_field(path, "Architecture")
    if name not in allowed and not include_unlisted:
        print(f"skip {path}: package {name} is not in suite manifest", file=sys.stderr)
        return None
    dest = out_dir / f"{name}_{version}_{arch}.deb"
    if dest.exists() and sha256(dest) != sha256(path):
        raise FileExistsError(f"asset name collision with different content: {dest.name}")
    shutil.copy2(path, dest)
    size = dest.stat().st_size
    if size >= ASSET_LIMIT_BYTES:
        raise ValueError(f"GitHub Release asset exceeds 2 GiB limit: {dest}")
    return {
        "package": name,
        "version": version,
        "architecture": arch,
        "asset": dest.name,
        "bytes": size,
        "sha256": sha256(dest),
    }


def validate_release_version(suite: str, version: str) -> None:
    if suite == "stable" and not STABLE_VERSION.fullmatch(version):
        raise ValueError("stable release versions must look like x.y.z")
    if suite == "experimental" and not EXPERIMENTAL_VERSION.fullmatch(version):
        raise ValueError("experimental release versions must look like x.y.z-beta or x.y.z-beta.N")


def gzip_packages(packages_path: Path) -> None:
    with packages_path.open("rb") as source, gzip.GzipFile(filename="", mode="wb", fileobj=(packages_path.with_suffix(packages_path.suffix + ".gz")).open("wb"), mtime=0) as target:
        shutil.copyfileobj(source, target)


def write_sha256sums(out_dir: Path) -> None:
    lines = []
    for path in sorted(item for item in out_dir.iterdir() if item.is_file() and item.name != "SHA256SUMS"):
        lines.append(f"{sha256(path)}  {path.name}")
    (out_dir / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def gpg_command(args: argparse.Namespace, output: Path, input_path: Path, detached: bool = False) -> list[str]:
    cmd = ["gpg", "--yes", "--default-key", args.gpg_key or os.environ.get("RADICAL_PACKAGE_GPG_KEY", ""), "--digest-algo", "SHA256"]
    passphrase = os.environ.get("RADICAL_PACKAGE_GPG_PASSPHRASE", "")
    if args.gpg_passphrase_file:
        cmd.extend(["--batch", "--pinentry-mode", "loopback", "--passphrase-file", str(args.gpg_passphrase_file)])
    elif passphrase:
        cmd.extend(["--batch", "--pinentry-mode", "loopback", "--passphrase", passphrase])
    if detached:
        cmd.extend(["-abs", "-o", str(output), str(input_path)])
    else:
        cmd.extend(["--clearsign", "-o", str(output), str(input_path)])
    return cmd


def sign_release(out_dir: Path, args: argparse.Namespace) -> None:
    if args.unsigned:
        return
    key = args.gpg_key or os.environ.get("RADICAL_PACKAGE_GPG_KEY", "")
    if not key:
        raise ValueError("GPG signing key required; set --gpg-key or RADICAL_PACKAGE_GPG_KEY, or pass --unsigned for local tests")
    release = out_dir / "Release"
    run(gpg_command(args, out_dir / "InRelease", release))
    run(gpg_command(args, out_dir / "Release.gpg", release, detached=True))


def stage_repo(args: argparse.Namespace) -> Path:
    root = Path(__file__).resolve().parents[1]
    validate_release_version(args.suite, args.version)
    out_dir = args.out_dir.resolve()
    if out_dir.exists():
        if not args.force:
            raise FileExistsError(f"output directory exists; pass --force to replace it: {out_dir}")
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    allowed = load_suite_packages(root, args.suite)
    packages = []
    for raw in args.packages:
        path = Path(raw).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(path)
        if path.suffix != ".deb":
            raise ValueError(f"expected a .deb package: {path}")
        record = copy_package(path, out_dir, allowed, args.include_unlisted)
        if record:
            packages.append(record)
    if not packages:
        raise ValueError("no packages were staged")

    all_arches = sorted({record["architecture"] for record in packages})
    release_conf = out_dir / "apt-ftparchive-release.conf"
    release_conf.write_text(
        "\n".join(
            [
                f'APT::FTPArchive::Release::Origin "Radical Computer Technologies";',
                f'APT::FTPArchive::Release::Label "RadicalPackages";',
                f'APT::FTPArchive::Release::Suite "{args.suite}";',
                f'APT::FTPArchive::Release::Codename "{args.suite}";',
                f'APT::FTPArchive::Release::Architectures "{" ".join(all_arches)}";',
                'APT::FTPArchive::Release::Components ".";',
                f'APT::FTPArchive::Release::Description "RadicalPackages {args.suite} GitHub Release flat APT repository";',
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    with (out_dir / "Packages").open("w", encoding="utf-8") as handle:
        run(["dpkg-scanpackages", "-m", "."], cwd=out_dir, stdout=handle)
    gzip_packages(out_dir / "Packages")
    with (out_dir / "Release").open("w", encoding="utf-8") as handle:
        run(["apt-ftparchive", "-c", str(release_conf), "release", "."], cwd=out_dir, stdout=handle)
    release_conf.unlink()
    sign_release(out_dir, args)
    write_sha256sums(out_dir)

    manifest = {
        "schema": "radicalpackages-github-release-apt",
        "schema_version": 1,
        "suite": args.suite,
        "release_version": args.version,
        "channel_tag": f"apt-{args.suite}",
        "signed": not args.unsigned,
        "architectures": all_arches,
        "packages": sorted(packages, key=lambda item: (item["package"], item["version"], item["architecture"])),
        "assets": [
            {
                "name": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in sorted(out_dir.iterdir())
            if path.is_file()
        ],
    }
    (out_dir / "release-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_sha256sums(out_dir)
    return out_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", choices=("stable", "experimental"), required=True)
    parser.add_argument("--version", required=True, help="Release-set version: x.y.z for stable, x.y.z-beta[.N] for experimental.")
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--gpg-key", default="")
    parser.add_argument("--gpg-passphrase-file", type=Path, default=None, help="Optional file for non-interactive GPG signing.")
    parser.add_argument("--unsigned", action="store_true", help="Generate unsigned metadata for local tests only.")
    parser.add_argument("--force", action="store_true", help="Replace an existing output directory.")
    parser.add_argument("--include-unlisted", action="store_true", help="Stage packages not present in debian/suites/<suite>.packages.")
    parser.add_argument("packages", nargs="+", help=".deb package files to stage.")
    args = parser.parse_args(argv)
    out_dir = stage_repo(args)
    print(out_dir)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
