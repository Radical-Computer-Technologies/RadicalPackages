#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUITES_DIR="$ROOT/debian/suites"

filter_packages_for_suite() {
    local suite="$1"
    local source_file="$2"
    local manifest="$SUITES_DIR/$suite.packages"

    if [ ! -f "$manifest" ]; then
        echo "missing suite manifest: $manifest" >&2
        exit 2
    fi

    awk -v manifest="$manifest" '
        BEGIN {
            RS = "\n";
            while ((getline line < manifest) > 0) {
                sub(/[[:space:]]*#.*/, "", line);
                gsub(/^[[:space:]]+|[[:space:]]+$/, "", line);
                if (line != "") allowed[line] = 1;
            }
            close(manifest);
            RS = "";
            ORS = "\n\n";
        }
        {
            package_name = "";
            line_count = split($0, lines, "\n");
            for (idx = 1; idx <= line_count; idx++) {
                if (lines[idx] ~ /^Package: /) {
                    package_name = substr(lines[idx], 10);
                    gsub(/^[[:space:]]+|[[:space:]]+$/, "", package_name);
                    break;
                }
            }
            if (allowed[package_name]) print $0;
        }
    ' "$source_file"
}

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

    mkdir -p "$POOL_DIR"
    for SUITE_MANIFEST in "$SUITES_DIR"/*.packages; do
        SUITE_NAME="$(basename "$SUITE_MANIFEST" .packages)"
        mkdir -p "$ROOT/debian/dists/$SUITE_NAME/main/binary-$ARCH"
    done
    cp "$PACKAGE_PATH" "$POOL_DIR/"
    echo "Copied $PACKAGE_NAME ($ARCH)."
done

(
    cd "$ROOT/debian"
    ALL_PACKAGES="$(mktemp)"
    dpkg-scanpackages pool /dev/null > "$ALL_PACKAGES"
    for SUITE_MANIFEST in suites/*.packages; do
        SUITE_NAME="$(basename "$SUITE_MANIFEST" .packages)"
        for DIST_DIR in "dists/$SUITE_NAME/main/binary-"*; do
            [ -d "$DIST_DIR" ] || continue
            filter_packages_for_suite "$SUITE_NAME" "$ALL_PACKAGES" > "$DIST_DIR/Packages"
            gzip -kf "$DIST_DIR/Packages"
        done
        apt-ftparchive release "dists/$SUITE_NAME" > "dists/$SUITE_NAME/Release"
    done
    rm -f "$ALL_PACKAGES"
)

echo "Updated Debian repository metadata."
