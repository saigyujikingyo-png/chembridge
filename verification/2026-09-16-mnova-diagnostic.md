# Mnova zero-page diagnostic checkpoint

Date: 2026-09-16. Shared principles: 2026-09-14.1.

Product code revision:
[`a5f9cd5`](https://github.com/saigyujikingyo-png/mnova-companion/commit/a5f9cd5c4f20b451bfc2243b9732d191b8de073e).
Implementation remains in the product repository; the hub records discovery and
acceptance state only.

## Result

**R0 PARTIAL; R1 NOT RUN.** Guarding canvas access for zero-page documents allowed
session creation, UUID and function-scope return, owned synthetic spectrum
creation, and separate readback to complete. The prior two documents remained
unchanged. A subsequent owned-document activation setter returned without
changing either active-document observer or the visible startup tab. Genuine
dirty state and target closure remain unaccepted; all shipped native write gates
remain disabled.

The existing crash dump was analyzed locally; the diagnostic points to a null
canvas through the `Document.activeItem` binding. That bounded analysis and the
new zero-page observation are separate evidence. No dump, proprietary runtime,
credentials or private native identifiers are published. The older retained-JS
cleanup failure remains an independent rejected route.

The implementation also rejects unknown target item counts and requires a
completed matching target-creation receipt before any close. Process/window
context and replay guards have portable regression coverage.

## Verification

- Local Windows: 228 tests and 42 subtests passed; one symlink-privilege skip.
- [Exact code CI](https://github.com/saigyujikingyo-png/mnova-companion/actions/runs/35080686690):
  Windows 229 tests/44 subtests; Ubuntu 225 tests/42 subtests with four platform skips.
- Ruff lint/format, six output contracts, actual MCP stdio checks and tracked
  source/privacy preflight passed. Schema size remains 19,898 UTF-8 bytes.
- Actual matching cloud-environment evidence is maintained in the product's
  [cloud record](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/docs/CLOUD_SETUP.md).
- The installed runtime core, icon and public tool catalog are unchanged. No new
  installer, native artifact delivery, model benchmark or end-user release is claimed.

Next: establish a supported owned document-window route while preserving the
current inventory, then prove genuine dirty state before R1. See the product's
[diagnostic and route](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/docs/SESSION_DIAGNOSTIC_20260916.md).
