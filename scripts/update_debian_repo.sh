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

TARGET_SUITES=()
PACKAGE_PATHS=()
while [ "$#" -gt 0 ]; do
    case "$1" in
        --suite)
            if [ "$#" -lt 2 ]; then
                echo "--suite requires a suite name" >&2
                exit 2
            fi
            TARGET_SUITES+=("$2")
            shift 2
            ;;
        --)
            shift
            while [ "$#" -gt 0 ]; do
                PACKAGE_PATHS+=("$1")
                shift
            done
            ;;
        -*)
            echo "unknown option: $1" >&2
            exit 2
            ;;
        *)
            PACKAGE_PATHS+=("$1")
            shift
            ;;
    esac
done

if [ "${#PACKAGE_PATHS[@]}" -lt 1 ]; then
    echo "usage: $0 [--suite stable|experimental] /path/to/package.deb [/path/to/another-package.deb ...]" >&2
    exit 2
fi

if [ "${#TARGET_SUITES[@]}" -eq 0 ]; then
    for SUITE_MANIFEST in "$SUITES_DIR"/*.packages; do
        TARGET_SUITES+=("$(basename "$SUITE_MANIFEST" .packages)")
    done
fi

for PACKAGE_PATH in "${PACKAGE_PATHS[@]}"; do
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
    for SUITE_NAME in "${TARGET_SUITES[@]}"; do
        SUITE_MANIFEST="$SUITES_DIR/$SUITE_NAME.packages"
        if [ ! -f "$SUITE_MANIFEST" ]; then
            echo "missing suite manifest: $SUITE_MANIFEST" >&2
            exit 2
        fi
        mkdir -p "$ROOT/debian/dists/$SUITE_NAME/main/binary-$ARCH"
    done
    cp "$PACKAGE_PATH" "$POOL_FILE"
    echo "Copied $PACKAGE_NAME ($ARCH)."
done

(
    cd "$ROOT/debian"
    ALL_PACKAGES="$(mktemp)"
    dpkg-scanpackages -m pool /dev/null > "$ALL_PACKAGES"
    for SUITE_NAME in "${TARGET_SUITES[@]}"; do
        SUITE_MANIFEST="suites/$SUITE_NAME.packages"
        if [ ! -f "$SUITE_MANIFEST" ]; then
            echo "missing suite manifest: $SUITE_MANIFEST" >&2
            exit 2
        fi
        for DIST_DIR in "dists/$SUITE_NAME/main/binary-"*; do
            [ -d "$DIST_DIR" ] || continue
            ARCH_NAME="${DIST_DIR##*-}"
            filter_packages_for_suite "$SUITE_NAME" "$ALL_PACKAGES" "$ARCH_NAME" > "$DIST_DIR/Packages"
            gzip -knf "$DIST_DIR/Packages"
        done
        apt-ftparchive release "dists/$SUITE_NAME" > "dists/$SUITE_NAME/Release"
    done
    rm -f "$ALL_PACKAGES"
)

echo "Updated Debian repository metadata."
