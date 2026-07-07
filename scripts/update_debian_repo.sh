#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACKAGE_PATH="${1:-}"

if [ -z "$PACKAGE_PATH" ]; then
    echo "usage: $0 /path/to/package.deb" >&2
    exit 2
fi

if [ ! -f "$PACKAGE_PATH" ]; then
    echo "package not found: $PACKAGE_PATH" >&2
    exit 2
fi

PACKAGE_NAME="$(dpkg-deb -f "$PACKAGE_PATH" Package)"
ARCH="$(dpkg-deb -f "$PACKAGE_PATH" Architecture)"
POOL_DIR="$ROOT/debian/pool/main/${PACKAGE_NAME:0:1}/$PACKAGE_NAME"
DIST_DIR="$ROOT/debian/dists/stable/main/binary-$ARCH"

mkdir -p "$POOL_DIR" "$DIST_DIR"
cp "$PACKAGE_PATH" "$POOL_DIR/"

(
    cd "$ROOT/debian"
    dpkg-scanpackages pool /dev/null > "dists/stable/main/binary-$ARCH/Packages"
    gzip -kf "dists/stable/main/binary-$ARCH/Packages"
    apt-ftparchive release dists/stable > dists/stable/Release
)

echo "Updated Debian repository for $PACKAGE_NAME ($ARCH)."
