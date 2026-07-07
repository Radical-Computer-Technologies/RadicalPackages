#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ "$#" -lt 1 ]; then
    echo "usage: $0 /path/to/package.deb [/path/to/another-package.deb ...]" >&2
    exit 2
fi

for PACKAGE_PATH in "$@"; do
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
    echo "Copied $PACKAGE_NAME ($ARCH)."
done

(
    cd "$ROOT/debian"
    for DIST_DIR in dists/stable/main/binary-*; do
        [ -d "$DIST_DIR" ] || continue
        dpkg-scanpackages pool /dev/null > "$DIST_DIR/Packages"
        gzip -kf "$DIST_DIR/Packages"
    done
    apt-ftparchive release dists/stable > dists/stable/Release
)

echo "Updated Debian repository metadata."
