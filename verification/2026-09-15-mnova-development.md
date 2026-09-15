# Mnova Companion development checkpoint

Date: 15 September 2026. Shared principles: **2026-09-14.1**.

The user approved implementation after the [architecture review](../plans/MNOVA_COMPANION_PLAN.md).
The independent MIT-licensed product repository is
[mnova-companion](https://github.com/saigyujikingyo-png/mnova-companion), on default
branch `codex/initial-preview`. This is source version `0.1.0.dev1`, not an
end-user release. No installer, stable tag or installed host integration is claimed.

Verified implementation: `026024275f0af5021b3f62f708f389020f0c7a52`.

## Implemented scope

The external Python 3.12 core exposes six typed MCP tools with meaningful
`outputSchema`, runtime-validated `structuredContent`, matching JSON text and
separate media content. It implements installation metadata, on-demand contracts,
owner-selected input staging, hash-verified original file access, durable job
records and single-writer primitives. `mnova_open` stages files only; native import
is explicitly `not_run`. `mnova_run` returns `CAPABILITY_UNVERIFIED` without starting
a job or native process. Native reconciliation and destination-specific delivery
are not yet implemented.

The locked dependencies and idempotent setup are in the product repository.
Licensed desktop software, private data and licences remain outside source and
cloud containers. No additional model service was added.

## Evidence ledger

| Gate | State | Evidence and limits |
| --- | --- | --- |
| Local portable verification | READY | Windows, Python 3.12.14: 55 tests passed, 1 ordinary-symlink privilege skip, 42 subtests passed, 1.96 s. A real directory junction rejection passed. Actual Win32 short-path regressions passed. Ruff, format, six output contracts, real MCP stdio and tracked-source checks passed. |
| Corrective commit CI | READY | [Windows/Ubuntu run](https://github.com/saigyujikingyo-png/mnova-companion/actions/runs/34998988183) passed at the exact implementation SHA above. Windows: 56 passed, 44 subtests, 2.93 s. Ubuntu: 52 passed, 4 Windows-only skips, 42 subtests, 1.35 s. Both also passed Ruff, formatting, schemas, real MCP stdio and source preflight. |
| Native bootstrap and bounded readback | PARTIAL | Embedded Python 3.11.15 on Mnova 17.0.1-41952 executed the metadata probe and constructed/read an original synthetic 1D spectrum. Licence/modules and real raw-data processing remain unverified. |
| Native lifetime and scientific workflow | FAILED / WRITES DISABLED | A guarded cross-language standalone-document release experiment crashed Mnova with Windows exception c0000409. No native save, fresh disk reopen or PDF/PNG/CSV export was reached. The session held only a task-owned synthetic sentinel. Mnova was not restarted after the failure. |
| Matching Codex environment | CREATED / PARTIAL | `Chembridge / Mnova Companion` was saved and selector-verified. Initial e03deb0 setup and maintenance passed. The current implementation's interactive container checks could not run after access to the original browser/account session was lost. CI is separate evidence. |
| Model, host and artifact receipt | UNVERIFIED | No real model benchmark, installed-host workflow or destination-supported original-file receipt. |

The first implementation CI found a Windows 8.3 short-path normalization failure.
It was reproduced using real `GetShortPathNameW` aliases and fixed with path
canonicalization after symlink/reparse rejection. The corrective commit adds
regressions for staged inputs, registered outputs, restart readback and rejecting
an input containing the store itself. Earlier Linux success was not reused as
Windows acceptance.

## Evidence and next gate

- [Product status](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/docs/STATUS.md)
- [Output contract coverage](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/docs/CONTRACT_COVERAGE.md)
- [Native investigation](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/docs/NATIVE_API.md)
- [Privacy-minimized native receipt](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/acceptance/native_20260915.json)
- [Cloud configuration and its separate checks](https://github.com/saigyujikingyo-png/mnova-companion/blob/codex/initial-preview/docs/CLOUD_SETUP.md)

The next native gate needs an explicit supported Python document-lifetime contract
or a separately verified isolated executor. The inspected API describes document
construction and lock/unlock, but provides no sufficient ownership/automatic
destruction guarantee for the failed cross-language route. Console download
availability alone does not establish licence or isolated-session behavior.
Do not repeat the known crash or enable writes based on metadata success.
Genuinely dirty-document preservation is also still unverified.

Cloud follow-up must regain access to the existing saved environment and run the
documented checks on the actual implementation checkout. Environment creation,
portable tests, native work, model execution and host delivery remain independent.
Private account/environment identifiers, machine paths, document identifiers and
raw experimental receipts are excluded from this public record.
