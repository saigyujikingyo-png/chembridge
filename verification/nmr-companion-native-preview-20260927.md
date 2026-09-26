# NMR Companion native Windows preview - 2026-09-27

This is a product-owner registration checkpoint. It records bounded source, package, installed-runtime and host evidence separately; it does not close shared incidents or claim full experimental acceptance.

- [Repository](https://github.com/saigyujikingyo-png/nmr-companion), default branch `main`.
- [v0.2.0-alpha.2 prerelease](https://github.com/saigyujikingyo-png/nmr-companion/releases/tag/v0.2.0-alpha.2), built from `3168f34660054b663b96d58a0b9f809c82522f31`; native UI correction merged through [PR 3](https://github.com/saigyujikingyo-png/nmr-companion/pull/3).
- [Exact-source CI 36278519479](https://github.com/saigyujikingyo-png/nmr-companion/actions/runs/36278519479): Windows **364 passed**, Ubuntu **343 passed and 21 Windows-only skips**; Ruff, 12 retained frontend checks per platform, Qt offscreen checks and builds passed.
- The versioned `release-evidence.json` and `SHA256SUMS` attached to the release are the subsequent package/installation/host evidence. The [earlier developer checkpoint](nmr-companion-developer-preview-20260924.md) remains historical.

## Native workbench and joint scope

The primary Windows frontend is a Qt Widgets application with a native executable, menus, dialogs and dockable project, properties and result panels. It does not need a browser, WebView or HTTP listener. The readable visual design uses restrained colors, text status, visible focus, contextual guidance and integral details below the spectrum to avoid overlapping labels.

Organic ORG-01 through ORG-12 and relaxation REL-01 through REL-14 remain one first batch. Native forms and the host-neutral MCP share the same revisioned scientific core, editable evidence, explicit mappings, stale state, reconciliation and reopenable exports. Qualified processed 2D, structures, reference annotations and condition comparisons are implemented with bounded fixture evidence; curated interpretation remains separate. See the product's [case-level acceptance](https://github.com/saigyujikingyo-png/nmr-companion/blob/v0.2.0-alpha.2/docs/ACCEPTANCE.md).

## Distribution and current device

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `nmr-companion-0.2.0a2-windows-x64.zip` | 172309954 | `42d7b4e326259e9e92480680c4f4096f2d0d0a426d0bb08c73a65f44a0817639` |
| `nmr_companion-0.2.0a2-py3-none-any.whl` | 515620 | `b7ff9c409a07abdcf33ce7bc13271a45c96f595b3f0b25375f92e5e4a33b6176` |
| `nmr_companion-0.2.0a2.tar.gz` | 888069 | `ccad2069e6435cc2a57cdff08ea332701aecc9b4d13739770016d27aef8f0f20` |

The Windows archive bundles Python, scientific dependencies, Qt, required third-party notices and guarded per-user installation/upgrade/rollback tools. All 9,635 payload files passed archive and relocated-file verification. This is unsigned and uses a console installer; it has no graphical setup wizard, Start Menu registration, file association or automatic updater.

A qualified native candidate at `67e4a1c` passed an actual alpha.1 upgrade, Verify, reinstall and rollback in both directions on one Windows device. Final `3168f34` passed installation and Verify, a real Windows Qt backend with an owned hidden window, installed offscreen spectrum/fit/candidate rendering, structured MCP reads and prior-artifact resource readback. The previous in-use installation and project originals were retained. Hidden-window and offscreen checks do not establish physical user interaction or fresh-device/OS-event acceptance.

## Installed host and artifact delivery

The supported Codex plugin commands registered alpha.2 against the installed native runtime; adapter and skill bytes were read back. A real Codex CLI 0.158.0-alpha.2.1 workflow on the qualified `67e4a1c` candidate performed a single reconciled edit, nine MCP calls and a 4,280,350-byte archive delivery, then independently reopened revision 15. Source arrays were unchanged and dependent interpretations became stale. The final wheel differs only in two UI modules and RECORD; scientific, persistence and MCP members are byte-identical, and the final installed runtime read back the original delivered bytes without replaying the edit.

GPT-5.6 Terra with max reasoning was requested. Resolved model/effort metadata and charges were unavailable, so this is not a confirmed Terra-max result. The successful attempt took 92.721 seconds; prior configuration/project-binding failures and token use are retained in the release evidence. First-attempt success is false.

## Separate remaining gates

- One authorized private NOMAD 1H Bruker archive passed explicit processing-profile import, original-byte preservation and export/reopen. This does not provide the required real benchtop DX/CSV pair or qualify broader 13C/2D profiles and chemistry.
- Physical usability, curated chemical/experimental review, new-device, reboot, sleep/resume, crash and actual clean-removal acceptance remain open.
- The matching `Chembridge / NMR Companion` cloud profile is prepared. Product setup installs the Python dependencies; its Qt checks additionally need the EGL/OpenGL libraries and fonts declared by product CI, and retained frontend checks need Node 22. A saved dedicated environment, interactive container and cloud model task have not been verified. An earlier accessible settings route did not expose environment creation; no application internals or caches were changed.
- Other agent hosts and native Mnova acceptance retain their own gates. This independent NMR core does not inherit their evidence or modify their restrictions.

Hub check: `python scripts/check_workspace.py` validates seven profiles and local documentation links only. It is not a product or cloud-environment acceptance test.
