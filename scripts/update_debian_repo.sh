#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUITES_DIR="$ROOT/debian/suites"

filter_packages_for_suite() {
    local suite="$1"
    local source_file="$2"
    local target_arch="$3"
    local manifest="$SUITES_DIR/$suite.packages"

    if [ ! -f "$manifest" ]; then
        echo "missing suite manifest: $manifest" >&2
        exit 2
    fi

    awk -v manifest="$manifest" -v target_arch="$target_arch" '
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
            package_arch = "";
            line_count = split($0, lines, "\n");
            for (idx = 1; idx <= line_count; idx++) {
                if (lines[idx] ~ /^Package: /) {
                    package_name = substr(lines[idx], 10);
                    gsub(/^[[:space:]]+|[[:space:]]+$/, "", package_name);
                } else if (lines[idx] ~ /^Architecture: /) {
                    package_arch = substr(lines[idx], 15);
                    gsub(/^[[:space:]]+|[[:space:]]+$/, "", package_arch);
                }
            }
            if (!allowed[package_name]) next;
            if (target_arch == "all") {
                if (package_arch == "all") print $0;
            } else if (package_arch == target_arch || package_arch == "all") {
                print $0;
            }
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
    PACKAGE_VERSION="$(dpkg-deb -f "$PACKAGE_PATH" Version)"
    ARCH="$(dpkg-deb -f "$PACKAGE_PATH" Architecture)"
    POOL_DIR="$ROOT/debian/pool/main/${PACKAGE_NAME:0:1}/$PACKAGE_NAME"
    POOL_FILE="$POOL_DIR/${PACKAGE_NAME}_${PACKAGE_VERSION}_${ARCH}.deb"

    mkdir -p "$POOL_DIR"
    for SUITE_MANIFEST in "$SUITES_DIR"/*.packages; do
        SUITE_NAME="$(basename "$SUITE_MANIFEST" .packages)"
        mkdir -p "$ROOT/debian/dists/$SUITE_NAME/main/binary-$ARCH"
    done
    cp "$PACKAGE_PATH" "$POOL_FILE"
    echo "Copied $PACKAGE_NAME ($ARCH)."
done

(
    cd "$ROOT/debian"
    ALL_PACKAGES="$(mktemp)"
    dpkg-scanpackages -m pool /dev/null > "$ALL_PACKAGES"
    for SUITE_MANIFEST in suites/*.packages; do
        SUITE_NAME="$(basename "$SUITE_MANIFEST" .packages)"
        for DIST_DIR in "dists/$SUITE_NAME/main/binary-"*; do
            [ -d "$DIST_DIR" ] || continue
            ARCH_NAME="${DIST_DIR##*-}"
            filter_packages_for_suite "$SUITE_NAME" "$ALL_PACKAGES" "$ARCH_NAME" > "$DIST_DIR/Packages"
            gzip -kf "$DIST_DIR/Packages"
        done
        apt-ftparchive release "dists/$SUITE_NAME" > "dists/$SUITE_NAME/Release"
    done
    rm -f "$ALL_PACKAGES"
)

echo "Updated Debian repository metadata."
