#!/usr/bin/env python3
"""Publish staged RadicalPackages assets to a GitHub Release."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


DEFAULT_REPO = "Radical-Computer-Technologies/RadicalPackages"


def run(cmd: list[str], dry_run: bool = False) -> subprocess.CompletedProcess | None:
    if dry_run:
        print("+ " + " ".join(cmd))
        return None
    return subprocess.run(cmd, check=True, text=True)


def gh_auth_ok() -> bool:
    return subprocess.run(["gh", "auth", "status"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def release_exists(repo: str, tag: str) -> bool:
    return subprocess.run(["gh", "release", "view", tag, "--repo", repo], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def collect_assets(paths: list[str]) -> list[str]:
    assets: list[str] = []
    for raw in paths:
        path = Path(raw).expanduser().resolve()
        if path.is_dir():
            assets.extend(str(item) for item in sorted(path.iterdir()) if item.is_file())
        elif path.is_file():
            assets.append(str(path))
        else:
            raise FileNotFoundError(path)
    if not assets:
        raise ValueError("no release assets found")
    return assets


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--tag", required=True, help="Release tag, for example apt-stable, apt-experimental, v0.2.1, or v0.2.1-beta.1.")
    parser.add_argument("--title", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--draft", action="store_true")
    parser.add_argument("--prerelease", action="store_true")
    parser.add_argument("--clobber", action="store_true", help="Replace same-named assets on existing releases.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("assets", nargs="+", help="Files or directories to upload.")
    args = parser.parse_args(argv)

    assets = collect_assets(args.assets)
    if not args.dry_run and not gh_auth_ok():
        raise RuntimeError("gh is not authenticated; run `gh auth login` and retry")

    title = args.title or args.tag
    notes = args.notes or f"RadicalPackages assets for {args.tag}"
    if args.dry_run:
        exists = False
    else:
        exists = release_exists(args.repo, args.tag)

    if exists:
        cmd = ["gh", "release", "upload", args.tag, "--repo", args.repo]
        if args.clobber:
            cmd.append("--clobber")
        run([*cmd, *assets], args.dry_run)
    else:
        cmd = ["gh", "release", "create", args.tag, "--repo", args.repo, "--title", title, "--notes", notes]
        if args.draft:
            cmd.append("--draft")
        if args.prerelease:
            cmd.append("--prerelease")
        run([*cmd, *assets], args.dry_run)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
