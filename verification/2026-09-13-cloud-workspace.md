# Chembridge cloud workspace verification - 13 September 2026

## Configured scope

The whole Chembridge initiative now has a public hub repository and four saved Codex Web environments. The hub supports shared standards, project discovery, planning and new-plugin onboarding. Origin, ChemDraw and UoE each keep an independent repository, dependency environment and acceptance record.

| Environment | Repository | Verified configuration |
| --- | --- | --- |
| Chembridge | `saigyujikingyo-png/chembridge` | Standard-library-only hub check for setup and maintenance |
| Chembridge / Origin Companion | `saigyujikingyo-png/origin-agent-bridge` | Reused original environment; renamed, saved and read back |
| Chembridge / ChemDraw Companion | `saigyujikingyo-png/chemdraw-companion` | Architecture-contract setup and maintenance saved |
| Chembridge / UoE Companion | `saigyujikingyo-png/edinburgh-study-agent` | Locked virtual environment setup and maintenance saved |

All use the universal container image with Python 3.12 and caching. Agent internet access uses the common-dependencies preset, GET/HEAD/OPTIONS and task-relevant official documentation domains. No new API key, project secret, campus session or vendor licence was added. Configuration alone does not establish every network route.

The desktop Chembridge project was changed by the user to the public hub checkout as its primary source. The project-list API then confirmed that path and `isGitRepository: true`. Small private OneDrive entrypoint documents were backed up, updated and read back locally. No large archive was hydrated and no cloud-sync server verification or disk cleanup was performed.

## Actual cloud-container results

All Python versions below were observed as **3.12.13**. Commits identify the source tested before later documentation-only receipts.

| Scope | Tested commit | Observed result |
| --- | --- | --- |
| Chembridge hub | `cb488d012dab140f227aeaf57371818d53263ca0` | Setup and maintenance passed: 3 product profiles and 6 local documentation links |
| Origin portable core | `d536599b7e90cbfa42f8c60cc94446dfbf447964` | Ruff passed; 81 files formatted; **175 tests passed in 19.52 s**; setup and maintenance passed |
| ChemDraw architecture contracts | `c9070b4fe6dbf670057dd5021521842291814340` | **5 JSON Schemas** passed; the bounded M2 mechanism fixture passed graph/flow accounting and logical snake topology; setup and maintenance passed |
| UoE portable core | `18d76f7ff053f91ffbb395574c6017ce453361a2` | **112 passed, 4 skipped in 5.28 s**; setup and maintenance passed |
| UoE real stdio MCP | Same UoE commit | Initialize/list/call passed with 31 tools, structured results, a synthetic local task round trip and rejection of an invalid request |
| UoE publication audit | Same UoE commit | 75 exact Git-index files checked; no issues |

The initial UoE cloud run at `2fcd88f67ab1ec6b9a363021794c33ad8f1bf2a7` had 110 passes, one failure and four browser setup errors. The failure exposed an interpreter-symlink bug: resolving the selected virtual-environment Python path launched the base interpreter without the package. The fix preserves the selected executable path and adds a regression that launches a real temporary virtual environment.

Chrome's sandboxed test fixture cannot run as root in this container. Those four checks now report explicit skips; the sandbox remains enabled. Root setup also avoids downloading an unused Chrome installation. These are cloud skips, not browser passes. The existing non-root CI matrix below supplies separate evidence for the full synthetic DOM suite. The new public configuration files are included in the exact publication allowlist; all existing credential/content checks remain active.

The UoE verification commands ran once through a temporary maintenance test sequence because interactive terminal input was unreliable. After the check, maintenance was restored to `bash scripts/setup_codex_cloud.sh`, so every ordinary task does not rerun the full test suite.

## UoE full cross-platform CI

[CI run 34753380958](https://github.com/saigyujikingyo-png/edinburgh-study-agent/actions/runs/34753380958) completed successfully at `18d76f7ff053f91ffbb395574c6017ce453361a2`.

| Runner | Python | Regression result |
| --- | --- | --- |
| Ubuntu | 3.11 | **116 passed in 4.37 s** |
| Ubuntu | 3.12 | **116 passed in 5.13 s** |
| Windows | 3.11 | **116 passed in 34.30 s** |
| Windows | 3.12 | **116 passed in 42.12 s** |

Each job also passed the real stdio smoke test, exact publication audit and source-archive build. These runs exercised the four sandboxed synthetic DOM tests without skips. They did not access a real campus account.

## Remaining evidence boundaries

No model-based cloud task was launched. Desktop source registration and saved Web environments were verified, but an actual desktop-to-cloud task dispatch was not exercised. This configuration is not a Terra max benchmark, native Origin/ChemDraw acceptance, campus login test or end-user attachment-delivery test. Existing product release labels and native limitations remain in force.

Native software remains on an authorised licensed execution device. Cloud development dependencies do not make Windows professional software run natively in the Linux development container. The known OpenAI local Work project-sync frontend bug was not investigated or modified.

Shared baseline 2026-09-13.1 and cloud entrypoints were carried into the known product repositories and the materials entrypoint. Independent product tasks were not messaged or synchronised. Future products can reuse the templates but still require their own environment creation and verification.
