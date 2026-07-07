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
| `radbard` | RADBard music and audio composition suite. | `sudo apt install radbard` |

## Links

- [RADLib API Documentation](docs/radlib/api/)
- [Debian package index](debian/dists/stable/main/binary-amd64/Packages)
- [RADBard package pool](debian/pool/main/r/radbard/)
