# Radical Packages

Radical Computer Technologies package repository and documentation hub.

## Package Repositories

### Debian Systems / Ubuntu Stable

Add the stable Radical Computer Technologies package repository:

```bash
sudo tee /etc/apt/sources.list.d/radical-computer-technologies.sources >/dev/null <<'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: stable
Components: main
Architectures: amd64
Trusted: yes
EOF

sudo apt update
```

### Debian Systems / Ubuntu Experimental

Add the experimental repository when you want beta applications such as RADBard:

```bash
sudo tee /etc/apt/sources.list.d/radical-computer-technologies-experimental.sources >/dev/null <<'EOF'
Types: deb
URIs: https://radical-computer-technologies.github.io/RadicalPackages/debian/
Suites: experimental
Components: main
Architectures: amd64
Trusted: yes
EOF

sudo apt update
```

Install a package:

```bash
sudo apt install <package>
```

`Trusted: yes` is temporary for the unsigned beta repository. The repository should be signed before broad public release.

## Stable Packages

| Package | Description | Install |
| --- | --- | --- |
| `radlib` | Aggregate RADLib package that installs runtime, development files, docs, examples, and tools. | `sudo apt install radlib` |
| `radlib-runtime` | Latest RADLib runtime meta-package. | `sudo apt install radlib-runtime` |
| `radlib-runtime-0-1` | RADLib ABI 0.1 runtime meta-package. | `sudo apt install radlib-runtime-0-1` |
| `radlib-dev` | Latest RADLib public headers and CMake package files. | `sudo apt install radlib-dev` |
| `radlib-dev-0-1` | RADLib ABI 0.1 public headers and CMake package files. | `sudo apt install radlib-dev-0-1` |
| `radlib-doc` | RADLib generated API documentation package. | `sudo apt install radlib-doc` |
| `radlib-examples` | RADLib example applications and sample projects. | `sudo apt install radlib-examples` |
| `radlib-tools` | RADLib SDK tools and protocol generator. | `sudo apt install radlib-tools` |

Targeted module installs are available for lean deployments:

```bash
sudo apt install radlib-core
sudo apt install radlib-ui
sudo apt install radlib-media
sudo apt install radlib-dsp
sudo apt install radlib-fpga
sudo apt install radlib-web
```

Use packages such as `radlib-core-0-1` directly when an application should pin the RADLib 0.1 ABI runtime line.

## Experimental Packages

| Package | Description | Install |
| --- | --- | --- |
| `radbard` | RADBard music and audio composition suite beta. | `sudo apt install radbard` |

## Links

- [RADLib API Documentation](docs/radlib/api/)
- [Stable Debian package index](debian/dists/stable/main/binary-amd64/Packages)
- [Experimental Debian package index](debian/dists/experimental/main/binary-amd64/Packages)
- [Debian package pool](debian/pool/main/)
