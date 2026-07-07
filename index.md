# Radical Packages

Radical Computer Technologies package repository and documentation hub.

## Package Repositories

### Debian Systems / Ubuntu

Add the Radical Computer Technologies package repository:

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

Install a package:

```bash
sudo apt install <package>
```

`Trusted: yes` is temporary for the unsigned beta repository. The repository should be signed before broad public release.

## Packages

| Package | Description | Install |
| --- | --- | --- |
| `radlib-runtime` | RADLib shared runtime libraries required by RADLib-based apps. | `sudo apt install radlib-runtime` |
| `radlib-dev` | RADLib public headers and CMake package files. | `sudo apt install radlib-dev` |
| `radlib-doc` | RADLib generated API documentation package. | `sudo apt install radlib-doc` |
| `radlib-examples` | RADLib example applications and sample projects. | `sudo apt install radlib-examples` |
| `radlib-tools` | RADLib SDK tools and protocol generator. | `sudo apt install radlib-tools` |
| `radlib` | Aggregate RADLib package that installs runtime, development files, docs, examples, and tools. | `sudo apt install radlib` |
| `radbard` | RADBard music and audio composition suite. | `sudo apt install radbard` |

## Links

- [RADLib API Documentation](docs/radlib/api/)
- [Debian package index](debian/dists/stable/main/binary-amd64/Packages)
- [Debian package pool](debian/pool/main/)
