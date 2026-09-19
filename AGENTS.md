# Chembridge contributor entrypoint

Read DEVELOPMENT_PRINCIPLES.md (shared rule version 2026-09-19.1), then CLOUD_DEVELOPMENT.md and project-catalog.json before work. For lifecycle or ownership work also read RUNTIME_LIFECYCLE.md and governance/OWNERSHIP.md. Chembridge is the umbrella for university convenience plugins, professional-software plugins, and agent workflows; it is not another name for Origin Companion.

Use this repository for shared standards, new-plugin planning, project discovery and cloud setup templates. Implement a product in its own repository and matching cloud environment. Preserve its own native, safety, compatibility, ownership and acceptance requirements. Routine messages between existing user-owned Chembridge tasks are preauthorised under DEVELOPMENT_PRINCIPLES.md section 11; no per-message confirmation is needed within that scope. Preserve each task's objective, source ownership and separate acceptance evidence.

Shared targets are ChatGPT Chat, local Work, cloud Work, Codex, Claude, WorkBuddy and other suitable agents. Use one identity and host-neutral core per plugin with thin adapters. Codex is both a development tool and a target user host. Ordinary plugin users do not need a coding project. Public content is English, open-source and suitable for GitHub Releases. GPT-5.6 Terra with max reasoning is the benchmark, subject to actual availability and evidence.

Use the lightest applicable setup. This hub requires only Python's standard library. Run `python scripts/check_workspace.py`. Install only the dependencies for the selected product. Do not aggregate incompatible product environments or add paid model services by default.

Private university OneDrive is a materials/archive entrypoint, not a Git checkout or required runtime output location. Keep accounts, licences, private coursework, tokens and installed runtimes outside public source and cloud development containers. Download only authorised data needed for the current task.

Configuration checks, portable tests, model-based cloud tasks, desktop handoff and native-software acceptance are separate evidence. Do not claim one from another. The confirmed OpenAI local Work project-sync frontend bug remains out of scope; do not change caches, registrations or application internals to repair it.

When adding a new plugin, follow templates/NEW_PLUGIN.md and register its repository, setup and checks. Existing GitHub authorisation may cover a new repository, but a matching Codex cloud environment must still be created and verified. Do not claim automatic future environment creation.

Every Chembridge plugin must implement and validate meaningful tool output schemas and structured results under DEVELOPMENT_PRINCIPLES.md section 12. Preserve media delivery and host compatibility, keep schemas compact, and record implementation/acceptance gaps separately.

Sections 13–14 require explicit runtime lifecycle semantics and single Product Max ownership. Governance High reviews shared contracts and incidents; Ultra is consultation-only after verified handoff. Recheck current source and applicable installed/remote state. Preserve unresolved incident gates and other owners' uncommitted work.

Current shared-principles conversation scope (explicit user direction, 2026-09-19): this task maintains project-wide principles only. Do not perform or accept code audits, product debugging/testing, runtime/package inspection, installation recovery or product acceptance here. Route technical execution and review to the accountable Product Max or a separately assigned task. See governance/OWNERSHIP.md for the precedence boundary; historical audit workflows do not reactivate that work.
