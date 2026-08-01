# Changelog

All notable changes to RadicalPackages are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project aims to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- 2026-08-01: Published **RADPx-OS 0.1.5-beta.1** x86 release documentation and
  regenerated the Doxygen API reference. The Crimson 0.1.5 line moves the desktop
  shell's Terminal, File Explorer, and Text Editor out of the kernel into separate
  userland processes (`/bin/radterm`, `/bin/radfiles`, `/bin/radedit`) driven over
  the compositor client path — the Terminal runs `radsh` over a real pty — and
  hardens the SMP scheduler so the multi-window desktop is crash-free under `-smp 4`.
  Bumped the portal version labels (`0.1.4` -> `0.1.5`) and repointed the current
  x86 release-bundle links to `radpx-os-0.1.5-beta.1`.
- 2026-07-22: Refreshed the RADPx-OS narrative docs and regenerated the Doxygen
  API reference so the published pages describe the shipped multi-window desktop
  shell (compositor, status, mainpage, getting-started) instead of the older
  single desktop+terminal surface state. Updated the portal summary and the
  window-manager profile description to match.
- 2026-07-22: Published **RADPx-OS 0.1.4-beta.2** release documentation and
  regenerated the Doxygen API reference. This release adds the multi-window
  RADCompositor desktop shell (Terminal, File Explorer, and Text Editor) with
  dynamic Slint UIs running in the freestanding kernel. Corrected the RADPx-OS
  portal version labels (`0.2.0` -> `0.1.4`).
- 2026-07-18: Updated branding and published documentation for the **RADPx-OS**
  / **RADKernel** rename across the portal and package descriptions.
