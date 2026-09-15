# Chembridge

Independent open-source plugins and agent workflows for University of Edinburgh study, research and everyday university work.

Chembridge covers university convenience tools, licensed professional-software automation and workflows connecting retrieval, processing, verification and delivery. This repository is the lightweight shared development entrypoint. Each product keeps its own source, runtime, releases and acceptance records.

## Start a cloud task

Open [Codex cloud environments](https://chatgpt.com/codex/cloud/settings/environments). Select **Chembridge** for shared planning, standards or a new plugin, or select the product environment for its implementation.

| Product | Repository | Cloud environment | Scope of the configured checks |
| --- | --- | --- | --- |
| Origin Companion | [origin-agent-bridge](https://github.com/saigyujikingyo-png/origin-agent-bridge) | Chembridge / Origin Companion | Portable Python tests; native Origin stays on a licensed Windows executor |
| ChemDraw Companion | [chemdraw-companion](https://github.com/saigyujikingyo-png/chemdraw-companion) | Chembridge / ChemDraw Companion | Current main-branch architecture contracts; native work has separate gates |
| UoE Companion | [edinburgh-study-agent](https://github.com/saigyujikingyo-png/edinburgh-study-agent) | Chembridge / UoE Companion | Portable tests and MCP smoke checks; four browser tests require non-root CI; no campus login is copied |
| Mnova Companion | [mnova-companion](https://github.com/saigyujikingyo-png/mnova-companion) | Chembridge / Mnova Companion | Portable MCP core; native lifecycle gate failed and writes disabled; initial cloud setup passed, current implementation container checks pending |

Read [cloud development](CLOUD_DEVELOPMENT.md), the [project catalog](project-catalog.json) and the [shared principles](DEVELOPMENT_PRINCIPLES.md). This catalog records the current participating products, not all repositories owned by the maintainer. Historical prototypes and unrelated projects are not inferred to be active Chembridge products.

The [13 September 2026 configuration receipt](verification/2026-09-13-cloud-workspace.md) records all four saved environments, actual container checks and separate CI results.

## Shared direction

One plugin identity per product across ChatGPT Chat, local Work, cloud Work, Codex and other suitable agents; easy installation for non-developers; economical-model support with GPT-5.6 Terra + max as the benchmark; task-specific Edinburgh requirements; lightweight execution and efficient quota use. All plugins must implement validated structured output contracts and meaningful MCP output schemas; see shared principles section 12. These are targets, not blanket acceptance claims.

Public source, documentation and releases belong on GitHub under an explicit licence. Private course materials, licensed vendor software, credentials and individual account data stay private. University OneDrive is a development archive preference and does not become a required destination for users' results.

## Add a plugin

Follow the [new-plugin checklist](templates/NEW_PLUGIN.md). Reuse shared rules and cloud setup conventions without merging unrelated runtimes. New repositories still need their own Codex environment and actual checks.

### Plugin plans

- [Mnova Companion architecture and implementation plan](plans/MNOVA_COMPANION_PLAN.md) — implementation approved; independent repository and cloud environment created. See the [development checkpoint](verification/2026-09-15-mnova-development.md) for portable checks and the failed native lifecycle gate.

This hub has no third-party runtime dependencies:

```bash
python scripts/check_workspace.py
```

Chembridge is independent of the University of Edinburgh and software vendors. See [LICENSE](LICENSE). A product's own licence and third-party notices govern its source and dependencies.
