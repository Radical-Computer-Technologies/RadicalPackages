# RadBuild 0.2.1 Graph Framework

RadBuild 0.2.1 continues a graph-based project model while preserving the legacy
Vivado, LiteX, and PetaLinux commands.

## Project Model

Schema v2 settings use:

```json
{
  "radbuild_schema": "2.0",
  "radbuild_version": "0.2.1",
  "project_name": "example",
  "systems": [],
  "connections": [],
  "artifacts": [],
  "deploy": [],
  "packages": {}
}
```

Legacy `projects.vivado`, `projects.litex`, and `projects.petalinux` files can
be migrated in place:

```bash
radbuild project migrate --settings settings.json
```

Migration writes `settings.json.bak` before replacing the file.

## Commands

Project commands:

```bash
radbuild project create /path/to/workspace --non-interactive --project-name demo
radbuild project validate --settings demo/settings.json
radbuild project add-system --settings demo/settings.json --id yocto --type linux.yocto --provider yocto --depends-on vivado
```

Graph and build commands:

```bash
radbuild graph --settings settings.json --json
radbuild generate --settings settings.json
radbuild build fpga --settings settings.json --json-events
radbuild build linux --settings settings.json --dry-run
radbuild build os --settings settings.json --json-events
radbuild build all --settings settings.json --server-profile local
radbuild deploy --settings settings.json --json-events
```

Helper commands:

```bash
radbuild-graph --settings settings.json --json
radbuild-hdlgen catalog
radbuild-package-index --settings settings.json
```

## Providers

Legacy-compatible providers delegate to the current preserved scripts:

- `fpga.vivado`
- `fpga.litex`
- `linux.petalinux`

Graph-native providers generate reproducible project assets:

- `linux.buildroot`: Buildroot external tree, defconfig, rootfs overlay, package definitions.
- `linux.yocto`: `meta-radical` layer, image recipe, package recipes.
- `os.radix`: RADix-OS image build and VM smoke provider. It runs the project-configured smoke script, supports multiple QEMU SMP counts, copies the ISO/disk images/logs into the artifact directory, and writes SHA-256 checksums.
- `software.native`: host software source and Makefile.
- `software.cross`: target software source and Makefile.
- `firmware.generic`: firmware manifest and source directory.
- `package.debian`: Debian packaging metadata and package indexes.

## RadHDL

The HDL commands scan RadHDL JSON manifests and VHDL entities, insert module
instances into an FPGA system, and generate:

- top-level VHDL
- Vivado project TCL
- address-map JSON

```bash
radbuild hdl catalog --json
radbuild hdl add raddsp_axis_gain --system vivado --instance gain0 --generic WIDTH=16
radbuild hdl generate --system vivado
radbuild hdl docs --out docs/radhdl/0.2.1
radbuild hdl docs --theme dark --run-sims --stop-time 100us --out docs/radhdl/0.2.1
```

RadBuild searches for RadHDL in this order:

- `--radhdl <path>`
- `RADBUILD_RADHDL_DIR`
- release-local RadHDL paths
- `/usr/share/radbuild/radhdl`
- source-tree sibling checkouts

The `radbuild-radhdl` Debian package installs the RadHDL catalog, source
assets, and `radhdl-docgen` at `/usr/share/radbuild/radhdl`. `radbuild hdl docs`
invokes that generator, or a source-tree `scripts/radhdl_docgen.py`, to produce
datasheet-style static HTML for module entities. VHDL packages and project
top-level integration files are cataloged for tooling but are not emitted as
datasheet pages. Library pages are indexes that link to module datasheets rather
than pretending that a library is a hardware block.
Generated module pages include source descriptions, use cases, block diagrams,
generic and port tables, register-map bit views when map metadata exists,
richer interface-aware block diagrams, collapsed VHDL include/instantiation
templates, testbench listings, optional GHDL waveform previews, and HDL
snippets. Generated indexes show explicit documentation versions and keep
collapsible sections closed by default. DSP datasheets are organized into
functional packages such as Transform, Matrix, Filter, and Detection. GHDL
runs are evidence-producing rather than all-or-nothing: passing testbenches get
linked VCD artifacts and waveform previews, while failed or simulator-specific
benches get linked status JSON and failure summaries. The same output is
published through the RadicalPackages documentation site. `--theme dark`,
`--theme light`, and `--theme auto` are supported for static HTML output.

## RadicalPackages

RadBuild can sync package names from a local RadicalPackages checkout:

```bash
radbuild packages sync --settings settings.json --radical-packages /path/to/RadicalPackages --suite stable
```

The sync updates `settings.json` and regenerates `packages/package-index.json`
for Debian, Buildroot, and Yocto consumers.

## VSCode

The VSCode extension lives in `vscode/radbuild-vscode`. It invokes the installed
`radbuild` CLI and reads line-delimited JSON events from stdout. It does not
import Python modules. OS builds are exposed through `RadBuild: Build OS`, which
runs `radbuild build os --json-events` and consumes the same artifact manifest as
the other graph systems.

## RADix-OS

RADix-OS repositories can be driven directly by schema v2 JSON project files.
Crimson uses separate project JSONs for independent OS profiles, such as a
terminal-only image and a Slint/RADCompositor window-manager image:

```json
{
  "radbuild_schema": "2.0",
  "radbuild_version": "0.2.1",
  "project_name": "RADix-OS Terminal",
  "systems": [
    {
      "id": "radix-x86-64-grub-terminal",
      "type": "os.radix",
      "provider": "radix-os",
      "depends_on": [],
      "config": {
        "ui_profile": "terminal",
        "feature_chunks": ["kernel.core", "services.base-terminal", "userspace.rash"],
        "build_dir": "build/embedded/x86_64_grub_terminal",
        "smoke_script": "tools/embedded/x86_64_grub_slint_smoke.sh",
        "artifact_dir": "artifacts/radix/x86_64-grub-terminal",
        "qemu_smp": [2, 4],
        "rkconfig": {
          "hostname": "radix",
          "root_password": "radix",
          "rootfs_size_mb": 256,
          "terminal_scale": "auto",
          "terminal_font": "radix-default",
          "terminal_theme": "radix-dark"
        }
      }
    }
  ],
  "connections": [],
  "artifacts": [],
  "deploy": [],
  "packages": {}
}
```

The provider keeps JSON output clean for IDEs by writing CMake/QEMU output to
logs under the configured `.radmeta/radix-os/.../logs` path. The default
artifact set includes:

- `radixkernel-x86-64-grub-<profile>.iso`
- `radixkernel-x86-64-grub-<profile>`
- `radix-rootfs.ext4`
- `radix-fat32.img`
- `run-radix-vm.sh`
- one serial log per configured SMP smoke
- `SHA256SUMS`

The `ui_profile` field selects the compiled OS chunk set. The `terminal`
profile omits Slint/RADCompositor, while the `wm` profile includes the
Slint-backed RADCompositor shell.

The optional `rkconfig` object is passed through to the RADix-OS image
generator and currently supports `hostname`, `root_password`,
`rootfs_size_mb`, `terminal_scale`, `terminal_font`, and `terminal_theme`. The
generated root filesystem follows a Unix-like layout with `/bin`, `/dev`, `/etc`, `/home/root`, `/lib`,
`/lib/radix/modules`, `/mnt/fat`, `/sbin`, `/tmp`, `/usr/bin`, `/usr/lib`, and
`/var/log`. RADix kernel modules use `.rko`; future RADix dynamic shared
objects use `.rso`.

RADix settings can be inspected or edited through the first `menuconfig`
command:

```sh
radbuild menuconfig --settings settings.terminal.json --list
radbuild menuconfig --settings settings.terminal.json --set-rkconfig terminal_theme=radix-dark
radbuild menuconfig --settings settings.terminal.json --enable-chunk fs.ext4
```

When package metadata is generated, RadBuild now emits a RADix package section
beside Debian, Buildroot, and Yocto metadata. RADix packages use the `.radpm`
archive suffix and can carry dependencies plus supported kernel-version ranges
for eventual rootfs installation.

## Debian Packaging

Repository package metadata lives in `packaging/debian` and defines:

- `radbuild`
- `radbuild-radhdl`
- `radbuild-server`
- `radbuild-vscode-support`
- `radbuild-doc`

Generated projects also get local Debian packaging metadata under
`packaging/debian` when `radbuild generate` or `radbuild build packages` is run.

Build local `.deb` packages from the RadBuild repository:

```bash
scripts/build_deb_packages.py --version 0.2.1 --arch all
```

Publish them into a local RadicalPackages checkout and refresh the Debian repo
metadata:

```bash
scripts/publish_deb_to_radicalpackages.py \
  --radical-packages /path/to/RadicalPackages \
  --version 0.2.1 \
  --suite experimental \
  --arch all
```

This writes:

- `radbuild_0.2.1_all.deb`
- `radbuild-server_0.2.1_all.deb`
- `radbuild-vscode-support_0.2.1_all.deb`
- `radbuild-doc_0.2.1_all.deb`
- `radbuild-radhdl_0.2.1_all.deb`
