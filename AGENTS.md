# Chembridge contributor entrypoint

Read DEVELOPMENT_PRINCIPLES.md (shared rule version 2026-09-13.2), then CLOUD_DEVELOPMENT.md and project-catalog.json before work. Chembridge is the umbrella for university convenience plugins, professional-software plugins, and agent workflows; it is not another name for Origin Companion.

Use this repository for shared standards, new-plugin planning, project discovery and cloud setup templates. Implement a product in its own repository and matching cloud environment. Preserve its own native, safety, compatibility, ownership and acceptance requirements. Routine messages between existing user-owned Chembridge tasks are preauthorised under DEVELOPMENT_PRINCIPLES.md section 11; no per-message confirmation is needed within that scope. Preserve each task's objective, source ownership and separate acceptance evidence.

Shared targets are ChatGPT Chat, local Work, cloud Work, Codex, Claude, WorkBuddy and other suitable agents. Use one identity and host-neutral core per plugin with thin adapters. Codex is both a development tool and a target user host. Ordinary plugin users do not need a coding project. Public content is English, open-source and suitable for GitHub Releases. GPT-5.6 Terra with max reasoning is the benchmark, subject to actual availability and evidence.

Use the lightest applicable setup. This hub requires only Python's standard library. Run `python scripts/check_workspace.py`. Install only the dependencies for the selected product. Do not aggregate incompatible product environments or add paid model services by default.

Private university OneDrive is a materials/archive entrypoint, not a Git checkout or required runtime output location. Keep accounts, licences, private coursework, tokens and installed runtimes outside public source and cloud development containers. Download only authorised data needed for the current task.

Configuration checks, portable tests, model-based cloud tasks, desktop handoff and native-software acceptance are separate evidence. Do not claim one from another. The confirmed OpenAI local Work project-sync frontend bug remains out of scope; do not change caches, registrations or application internals to repair it.

When adding a new plugin, follow templates/NEW_PLUGIN.md and register its repository, setup and checks. Existing GitHub authorisation may cover a new repository, but a matching Codex cloud environment must still be created and verified. Do not claim automatic future environment creation.
