# Lifecycle and owner migration ledger

Updated: 2026-09-19. Baseline: **2026-09-19.1**, published Hub commit `922d95041b3b857f6ba11fbfb2817b18712ef605`.

This ledger records adoption and ownership separately from product acceptance. Private task IDs, account details, source checkpoints and handoff paths stay in ignored local coordination records.

| Product | Current owner evidence | Handoff/takeover | Rule adoption | Lifecycle work / required next gate |
| --- | --- | --- | --- | --- |
| Origin | Existing Astra Max, verified task metadata | MIGRATED: existing Max ownership verified; no Ultra transfer | Product lifecycle candidate reviewed | 0.2.12 public prerelease and controlled two-account installation accepted; exact release-head Windows/Ubuntu CI passed. A current Governance connector status call returned 0.2.12 on the intended device. Separate account UI, rollback and OS-event gates remain open |
| UoE | Existing Astra Max, verified task metadata | MIGRATED: existing Max ownership and understanding verified | Product lifecycle candidate reviewed | 0.8.2 public prerelease at 88fbf736; PR merged as 01deb3b and six public assets verified. Corrected finite maintenance helper accepted. Installed 0.8.1 connections preserved pending normal host release and controlled upgrade |
| MATLAB | New Astra Max, actual turn metadata verified | MIGRATED; full receipt/hash and understanding accepted; original Ultra archived | Published product commit 34e2cf1, pinned to shared 922d950 | Alpha.4 public engineering prerelease at package source 8dc506c4; four downloaded assets independently verified. Fixture-only validation head 0305bb83 and isolated P2 c92328e0 passed all five Windows/Ubuntu CI runs. P1 staged once with 4,058 files verified; matching Apply review reissued. Alpha.3 remains active pending normal host release and fresh admission; P2 remains source-only |
| Mnova | New Astra Max, actual turn metadata verified | MIGRATED; full receipt/hash and understanding accepted; original Ultra archived | Adopted in isolated candidate 1f24531 | dev2 public prerelease and official installed plugin verified at e22718c; nine raw modules and 65 source/cache files match. Governance's actual status call at 16:19 UTC still returned dev1 through its old connection; normal host pickup remains open. Original product/Hub work preserved; native writes and close disabled |
| ChemDraw | Local Astra Max owns development; source architecture Astra Ultra; remote source model unresolved | MAX_VERIFYING; understanding accepted; historical native materials incomplete | Adopted in reviewed c6cfa3ec source | Diagnostic-only 0.2.0-preview.1 publicly released and locally installed through its reviewed installer and official MCP registration. Independent 51-file installed parity and connection readback passed; 79 focused tests passed, one privilege skip. Fresh host-model acceptance remains open; native execution stays frozen and legacy ChemAIst remains separate |
| Code Relay | Existing Astra Max, verified task metadata | MIGRATED; existing sole Max ownership and understanding verified | Published product commit 77469d2, pinned to shared 922d950 | docs.1 resource-installation repair 52fd007 publicly released and officially installed; 20 raw source/cache resources match. Runtime stays 0.1.1, old sessions await normal pickup; CLR-LC-01 through 05 remain open |

The user explicitly approved new Max takeover tasks for products that require migration. Original Ultra tasks may be archived **after** the replacement has verified information and understanding. MATLAB and Mnova have passed that gate and their original Ultra tasks are archived. Existing Max products retain their tasks. ChemDraw transfer remains pending; its sources are preserved.

ChemDraw's owner explicitly ended the long-term cross-machine development arrangement on 2026-09-19. The existing local Product Max task owns both architecture and native implementation. Its product checkout remains separate from the Hub; preserve the architecture and native branch identities, using a local product worktree when needed. Remote participation is limited to the one-time transfer of required handoff/evidence, with local file/hash readback before retiring the source. Do not retain a remote development owner, recurring remote assignment or dependency on a remote conversation for ordinary work. Preserve original archives; do not migrate credentials, licences or runtime state. Local native/software entitlement and execution acceptance remain separate gates, and the existing runtime/holdout freeze remains in force.

## Incident closure conditions

Status is evidence-based. PARTIAL below does not mean a passing gate. See [the initial audit](incidents/CB-2026-001.md) for source references and observation scope.

| # | Required condition | Current evidence / remaining work |
| --- | --- | --- |
| 1 | Origin root cause | PARTIAL: unsafe source retry confirmed; historical duplicate chain and termination cause not reproduced |
| 2 | Origin source of truth | CONFIRMED: packaged repo runner; school was one-off literal adaptation, formal generator missing |
| 3 | Source fix | PASSED bounded review of Origin 0.2.12 lifecycle/admission/installer source; historical termination cause remains open |
| 4 | Regressions | PASSED exact release-head portable/fixture CI at b717e598; installed/native/OS tests remain separately scoped |
| 5 | Delayed ready | OPEN |
| 6 | Failure after spawn | OPEN |
| 7 | Personal profile regression | OPEN |
| 8 | School profile regression | OPEN |
| 9 | No same-profile duplicate tunnel | PASSED bounded installed observation: one daemon per account after controlled upgrade; persistence across real OS events remains open |
| 10 | No duplicate MCP child | PASSED bounded installed observation: one frontend per account; unrelated host frontends preserved. Real OS-event persistence remains open |
| 11 | Reboot/login acceptance | OPEN; requires safe real OS-event window |
| 12 | Network at login | OPEN; expected behavior must be implemented and verified |
| 13 | Current installed fix | PASSED Origin 0.2.12 controlled upgrade; UoE and MATLAB repaired-version installation remains pending |
| 14 | Origin ChatGPT reconnect | OPEN; initial remote call failed |
| 15 | Fresh Origin tools | PARTIAL: personal-account Work discovered status tool; actual call failed, other-account/fixed-package gates remain open |
| 16 | Bounded Origin call | PASSED current Governance connector status at 0.2.12 on the intended device; earlier 404 and personal Work failure retained. This does not establish both account UI routes |
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
| 29 | Max takeover verification | PARTIAL: Origin/UoE/MATLAB/Mnova/Code Relay receipts and understanding verified; ChemDraw understanding accepted, native material transfer incomplete |
| 30 | Single long-term owner/product | Existing Max retained; MATLAB/Mnova replacements verified; ChemDraw transfer pending |
| 31 | Former Ultra consultation-only | MATLAB/Mnova original Ultra archived after verified transfer; ChemDraw pending |
| 32 | Honest open-item retention | Active ledger; incident remains OPEN |

## Authorized repaired-version rollout

The owner explicitly authorized pushing the repaired versions and installing all of them on 2026-09-19. Product owners must finish publication and installation work within their verified product scope; the earlier missing-consent publication blocker is superseded by this new user instruction, subject to normal platform approval. Technical blockers are recorded separately from permission. Do not repeat an already completed healthy installation just because the authorization was renewed.

Cross-product source-parity reviews found checkout/archive line-ending conversion being described as raw Git byte equality. The exact scope and additive-correction method are recorded in [source parity evidence](SOURCE_PARITY.md); existing frozen packages and the shared-rule version are unchanged.

Origin's installed package was built from `f83f1ca1`; later fixture-only `51be2f09` and documentation-only `1855cde8` commits do not silently change that provenance. The public [v0.2.12 prerelease](https://github.com/saigyujikingyo-png/origin-agent-bridge/releases/tag/v0.2.12) is tagged at documentation-only b717e598; the merged default is ca339def. Exact release-head push and PR checks passed on Windows and Ubuntu, and public asset hashes match the reviewed binaries. The profile command intentionally moved from the old executable to 0.2.12; identity, key references and the remaining complete profile structure were preserved. The failed initial whole-profile byte-equality assertion and additive reconciliation are retained.


The [UoE 0.8.2 prerelease](https://github.com/saigyujikingyo-png/edinburgh-study-agent/releases/tag/v0.8.2), [Mnova dev2 prerelease](https://github.com/saigyujikingyo-png/mnova-companion/releases/tag/v0.1.0-dev.2) and [Code Relay docs.1 revision](https://github.com/saigyujikingyo-png/code-relay/releases/tag/v0.1.1-docs.1) are public. Mnova and Code Relay official installations are verified in their bounded preview scopes; UoE activation remains pending. Code Relay changed installation delivery only, not its provider/runtime version. Installed cache files do not prove that an existing conversation has reloaded a new connection.

The [ChemDraw diagnostic prerelease](https://github.com/saigyujikingyo-png/chemdraw-companion/releases/tag/v0.2.0-preview.1) is tagged at c6cfa3ec and installed locally. Its 51-file package contains 15 raw Git source files, 34 exact upstream CPython files and two build/manifest records. Governance independently verified that mapping, actual installed bytes, the official connection readback and extracted-runtime status/error/EOF behavior. The product owner's registered-command probe also passed; a fresh model-host call remains separate. The bounded source repair is in [draft PR 3](https://github.com/saigyujikingyo-png/chemdraw-companion/pull/3), targeting the existing native implementation branch; historical PRs and native freezes remain untouched. No CI result is claimed from the local tests or package probes.

The [MATLAB Alpha.4 engineering prerelease](https://github.com/saigyujikingyo-png/matlab-companion/releases/tag/v0.1.0-alpha.4) is public at package source 8dc506c4. Governance independently verified all four downloaded assets against the reviewed originals and public digests. The unchanged ZIP remains tied to its original build provenance; the verification asset records later test-only validation at 0305bb83. The isolated P2 branch remains a separate draft source change and is excluded from this package.

UoE and MATLAB require a coordinated normal host release before replacing occupied installed runtimes. A prepared package or read-only maintenance checker is not an installed upgrade. Product-specific native freezes, unresolved job outcomes and licence boundaries remain explicit. ChemDraw work remains local; incomplete remote handoff evidence is not converted into acceptance by installation authorization. Code Relay and Mnova must verify which published fixes are actually present in their installed packages rather than inventing a new runtime version for documentation-only changes.

The owner subsequently explicitly confirmed all pending pushes and version switches. Governance pushed both previously named MATLAB branches and verified their exact remote commits; the historical automatic-approval refusal is no longer an active authorization blocker. UoE's fresh read-only preflight at 16:18 UTC verified 3,337 staged files and preserved all three historical records, but found 16 runtime processes with live external parents. It refused activation with no installed mutation or campus request. Permission to switch does not itself release these occupied runtimes.

The first MATLAB Windows runs (35454412158 and 35454412022) failed because two test fixtures treated terminal-state visibility as completed quarantine publication or required identity rejection within a 100 ms fixture deadline. Governance reviewed the runtime execution lock and active marker, independently passed 31 focused tests, and verified a deterministic two-owner regression: a delayed quarantine write never admits the second backend. Only two test files changed. P1 validation head 0305bb83 and isolated P2 head c92328e0 passed all five new push/PR runs on Windows and Ubuntu. Runtime, packaging inputs, production deadlines and the original package bytes are unchanged. The original failures remain recorded. The matching Apply review was reissued after this technical review; live activation still requires normal host release and fresh admission.

Observed package-cache, Windows bootstrap, immutable review and host-pickup lessons are recorded in [controlled maintenance review evidence](MAINTENANCE_REVIEW.md). These findings do not create new native or OS-event acceptance.

## Governance validation and unresolved constraints

- Hub checker passed after new links/baseline; this accepts configuration only.
- Task Scheduler operational logging was disabled at inspection. Existing error codes and product logs do not establish which actor terminated wrappers. Logging was not enabled or altered by the audit.
- Current cloud account shows three saved environments; other environment/account visibility and saved ChemDraw command migration remain unverified.
- Public rule publication does not synchronize private materials entrypoints or product copies automatically. Owners must acknowledge or record the remaining version gap.

The private materials entrypoint's old shared-rule copy was compared with the original baseline before synchronization. Principles, lifecycle/ownership references and entrypoint version markers now match the new baseline; this is documentation synchronization only.

MATLAB handoff adds an important distinction: one `_ensure()` call does not spawn twice after its startup timeout, but a subsequent call may attempt another startup because attempt identity is not persisted before readiness. The coordinator lifetime lock still prevents a second Core. A not-ready coordinator can already own recovered accepted work; do not blindly terminate it. This is a source-review risk requiring focused regression, not a proven duplicate scientific execution or autostart defect.

Governance's preliminary UoE review required regressions for children born during cleanup and multiple logical MCP child chains. These source-review blockers were corrected and verified in the reviewed 0.8.2 candidate. The still-installed 0.8.1 transport has not been relabelled as that fix; activation requires a reviewed finite maintenance entrypoint and normal release of host-owned frontends.
