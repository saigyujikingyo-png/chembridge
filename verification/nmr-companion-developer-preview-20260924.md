# NMR Companion developer preview - 2026-09-24

This is a product-owner checkpoint and hub registration receipt, not shared-governance technical acceptance or completion of the first laboratory batch.

- Repository: https://github.com/saigyujikingyo-png/nmr-companion
- Source: `bc4b100ca2a271f2cb687070dfa6da1d3bd34fa0` on `main`.
- Release: [v0.1.0-alpha.1](https://github.com/saigyujikingyo-png/nmr-companion/releases/tag/v0.1.0-alpha.1), explicitly a developer prerelease.
- [CI run 36057511607](https://github.com/saigyujikingyo-png/nmr-companion/actions/runs/36057511607): 91 tests passed on Windows and Ubuntu; lint and builds also passed.

## Implemented increment

Organic and physical-chemistry workflows are both in the first batch. This increment provides qualified 1D imports, original-byte preservation, explicit processing and signed integration, internal-standard yield, T1/T2 fitting with diagnostics, and evidence assignments. The editable workbench and MCP frontend share the same revisioned project, conflict handling, idempotent receipts, stale-result semantics, undo and export.

The Windows workbench exercised a labelled synthetic organic/T1 example, explicit trace-to-delay mappings, a conflicting edit from a separate real MCP process, stale-result handling, undo, restart and reopened analysis settings. An exported project was independently reopened with nine spectra and two current analyses. A requested in-app browser download did not produce an observed download event; that browser delivery route remains unaccepted. These observations do not establish an installed AI-host/model workflow.

## Developer packages

The actual GitHub release downloads were read back and matched the local reviewed bytes and published checksums:

| Package | Bytes | SHA-256 |
| --- | ---: | --- |
| `nmr_companion-0.1.0a1-py3-none-any.whl` | 57511 | `2676d1ee938bf45b0d97226b9e36a2a24eba8e584279975264b33c71aa0756aa` |
| `nmr_companion-0.1.0a1.tar.gz` | 116555 | `6e9a762851052b5a5df70e5f60f17c6162dfdd6c800686975a65dab5c484246f` |

The wheel contains the workbench assets. The source archive contains the plugin manifest, skill and dependency lock. These are developer distributions requiring Python and dependencies, not a bundled end-user installer. No private manuals, datasets, accounts or licence material are distributed.

## Separate open gates

- The profile for `Chembridge / NMR Companion` is prepared. Saved Codex cloud-environment creation and execution have not been verified. The accessible legacy settings URL redirected to a workspace home without an environment creation entry; no internal registrations or caches were changed.
- Raw/processed 2D, crosspeak and structure editing, image/PDF evidence, condition comparisons and remaining instrument qualification stay in the joint first batch. The product's [case-level acceptance record](https://github.com/saigyujikingyo-png/nmr-companion/blob/bc4b100ca2a271f2cb687070dfa6da1d3bd34fa0/docs/ACCEPTANCE.md) defines the remaining work.
- Bundled installation, upgrades/removal, named AI hosts and the Terra max benchmark remain open.
- Existing Mnova native gates and other product evidence are unchanged. NMR Companion has its own source, execution core and acceptance record.

Hub validation: `python scripts/check_workspace.py` passed for seven profiles and 22 local documentation links. This validates registration configuration only.
