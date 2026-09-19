# Lifecycle and owner migration ledger

Updated: 2026-09-19. Baseline: **2026-09-19.1**, published Hub commit `922d95041b3b857f6ba11fbfb2817b18712ef605`.

This ledger records adoption and ownership separately from product acceptance. Private task IDs, account details, source checkpoints and handoff paths stay in ignored local coordination records.

| Product | Current owner evidence | Handoff/takeover | Rule adoption | Lifecycle work / required next gate |
| --- | --- | --- | --- | --- |
| Origin | Existing Astra Max, verified task metadata | MIGRATED: existing Max ownership verified; no Ultra transfer | Rules read; product copy pending | Takeover accepted; source lifecycle fix underway. Review before deployment; two-account host and OS-event acceptance remain open |
| UoE | Existing Astra Max, verified task metadata | MIGRATED: existing Max ownership and understanding verified | Rules read; product copy pending | Original two transports restored without identity changes; governance remote status passed at 0.8.1; source lifecycle corrections and remaining host/live/OS gates open |
| MATLAB | New Astra Max, actual turn metadata verified | MIGRATED; full receipt/hash and understanding accepted; original Ultra archived | Documentation adoption assigned | On-demand coordinator + durable job scope; startup-attempt reconciliation risk identified; package/native/OS acceptance remains separate |
| Mnova | New Astra Max, actual turn metadata verified | MIGRATED; full receipt/hash and understanding accepted; original Ultra archived | Documentation adoption assigned | 18 product + 8 Hub dirty files checkpointed and preserved; native writes disabled; manual I0/rollback evidence required; old installed state must not be silently upgraded to P0 |
| ChemDraw | Source architecture Astra Ultra; remote source model unresolved | HANDOFF_READY for architecture; new Max intake queued; native handoff completion pending | Pending | Verify both handoffs before ownership acceptance/archival; retain branch boundaries/freeze; withdraw saved-cloud M2 check; explicit licensing gate |
| Code Relay | Existing Astra Max, verified task metadata | MIGRATED; existing sole Max ownership and understanding verified | Published product commit 77469d2, pinned to shared 922d950 | On-demand execution; CLR-LC-01 through 05 remain open; no durable-service or paid API replay claim |

The user explicitly approved new Max takeover tasks for products that require migration. Original Ultra tasks may be archived **after** the replacement has verified information and understanding. MATLAB and Mnova have passed that gate and their original Ultra tasks are archived. Existing Max products retain their tasks. ChemDraw transfer remains pending; its sources are preserved.

## Incident closure conditions

Status is evidence-based. PARTIAL below does not mean a passing gate. See [the initial audit](incidents/CB-2026-001.md) for source references and observation scope.

| # | Required condition | Current evidence / remaining work |
| --- | --- | --- |
| 1 | Origin root cause | PARTIAL: unsafe source retry confirmed; historical duplicate chain and termination cause not reproduced |
| 2 | Origin source of truth | CONFIRMED: packaged repo runner; school was one-off literal adaptation, formal generator missing |
| 3 | Source fix | OPEN; assigned to Origin Max |
| 4 | Regressions | OPEN |
| 5 | Delayed ready | OPEN |
| 6 | Failure after spawn | OPEN |
| 7 | Personal profile regression | OPEN |
| 8 | School profile regression | OPEN |
| 9 | No same-profile duplicate tunnel | OPEN; absence in initial stopped snapshot is not a passing recovery test |
| 10 | No duplicate MCP child | OPEN; legitimate host stdio children must be preserved |
| 11 | Reboot/login acceptance | OPEN; requires safe real OS-event window |
| 12 | Network at login | OPEN; expected behavior must be implemented and verified |
| 13 | Current installed fix | OPEN; initial Origin installed 0.2.11 |
| 14 | Origin ChatGPT reconnect | OPEN; initial remote call failed |
| 15 | Fresh Origin tools | PARTIAL: personal-account Work discovered status tool; actual call failed, other-account/fixed-package gates remain open |
| 16 | Bounded Origin call | OPEN; initial remote status 404; fresh personal-account Work call also failed tunnel-client-not-seen after tool discovery |
| 17 | UoE runtime-to-host chain | PASSED for bounded current transport/tool discovery/status in fresh personal and school ChatGPT Work conversations; campus session and durable OS recovery remain separate open gates |
| 18 | UoE study_status | PASSED bounded governance-host remote/local and fresh personal/school Work calls at 0.8.1; UI selected Terra/max, resolved backend not independently attested; live_connection_checked=false |
| 19 | UoE live school call | PARTIAL: after explicit user approval, one-page live Learn retrieval completed at 11:31 UTC; returned login landing page, authentication unknown, no course sections. Authenticated campus acceptance remains OPEN |
| 20 | MATLAB lifecycle classified | CONFIRMED from current source and verified Product Max understanding |
| 21 | MATLAB autostart defect determination | No violation confirmed; shipped on-demand scope does not require logon startup |
| 22 | Shared gap decision | CONFIRMED |
| 23 | Shared contract | PUBLISHED in 922d950; product adoption separate |
| 24 | Templates synchronized | PUBLISHED in 922d950; downstream copies pending |
| 25 | Existing-product migration audit | PARTIAL: six initial classifications; owner-validated full records pending |
| 26 | Rule version | PUBLISHED 2026-09-19.1; adoption pending |
| 27 | Ultra inventory | PARTIAL: six products/seven roles identified; remote ChemDraw model pending |
| 28 | Ultra handoffs | PARTIAL: MATLAB, architecture ChemDraw and Mnova ready; native ChemDraw completion pending |
| 29 | Max takeover verification | PARTIAL: Origin/UoE/MATLAB/Mnova/Code Relay receipts and understanding verified; ChemDraw pending |
| 30 | Single long-term owner/product | Existing Max retained; MATLAB/Mnova replacements verified; ChemDraw transfer pending |
| 31 | Former Ultra consultation-only | MATLAB/Mnova original Ultra archived after verified transfer; ChemDraw pending |
| 32 | Honest open-item retention | Active ledger; incident remains OPEN |

## Governance validation and unresolved constraints

- Hub checker passed after new links/baseline; this accepts configuration only.
- Task Scheduler operational logging was disabled at inspection. Existing error codes and product logs do not establish which actor terminated wrappers. Logging was not enabled or altered by the audit.
- Current cloud account shows three saved environments; other environment/account visibility and saved ChemDraw command migration remain unverified.
- Public rule publication does not synchronize private materials entrypoints or product copies automatically. Owners must acknowledge or record the remaining version gap.

The private materials entrypoint's old shared-rule copy was compared with the original baseline before synchronization. Principles, lifecycle/ownership references and entrypoint version markers now match the new baseline; this is documentation synchronization only.

MATLAB handoff adds an important distinction: one `_ensure()` call does not spawn twice after its startup timeout, but a subsequent call may attempt another startup because attempt identity is not persisted before readiness. The coordinator lifetime lock still prevents a second Core. A not-ready coordinator can already own recovered accepted work; do not blindly terminate it. This is a source-review risk requiring focused regression, not a proven duplicate scientific execution or autostart defect.
