# Chembridge cloud development

## Scope and environment map

The **Chembridge** environment is the shared entry for the whole initiative, including new plugins. Product implementation uses the matching environment in project-catalog.json so that repository diffs, dependencies and acceptance remain attributable to that product. The shared hub does not nest or bulk-clone every product repository.

Use the universal image with Python 3.12, container caching and a maintenance script. The hub setup and maintenance command is `python scripts/check_workspace.py`. No API key, private account connection, browser profile or vendor licence is needed for hub checks.

For each product, cloud/profiles.json records the setup entrypoint and actual verification commands. Source copies of the two new setup scripts are in cloud/setup. The existing Origin script remains maintained in the Origin repository. Each product's source entrypoint takes precedence for its specific execution and quality constraints.

Enable the common-dependencies network preset and only the extra official documentation domains needed by a task. This baseline uses GET, HEAD and OPTIONS during the agent phase; setup and maintenance have their own dependency-installation access. Native desktop software and campus-account acceptance run separately on authorised execution devices.

The current product scopes differ: Origin has a portable Python suite; ChemDraw main is an architecture preview; UoE includes four synthetic DOM tests requiring sandboxed Chrome on a non-root runner. The root Codex container explicitly skips those four checks and avoids the unused Chrome download; the existing Ubuntu/Windows CI matrix remains the full DOM gate. A cloud setup pass does not turn an architecture preview into a released native plugin or verify a university account workflow.

## Shared rules

DEVELOPMENT_PRINCIPLES.md is the current shared baseline, version 2026-09-13.2. Each participating repository must include that baseline and an AGENTS.md entry requiring it, while retaining product-specific constraints. Update known copies deliberately when the baseline changes; do not assume old tasks have reloaded it.

Keep code and dependency environments outside cloud-synced folders. The private university Chembridge folder remains the materials entrypoint. The hub contains small public documentation, a catalog and setup conventions. Cloud setup is not automatic local disk cleanup.

Routine messages between existing user-owned Chembridge tasks are preauthorised under DEVELOPMENT_PRINCIPLES.md section 11; no per-message confirmation is needed within that scope. Preserve each task's objective, source ownership and separate acceptance evidence. This updates the earlier default against cross-product message relays.

## Desktop and Web

Codex Web selects the cloud environment directly. For the desktop Chembridge project, the code entrypoint is a checkout of this hub; the private OneDrive folder can remain a separate materials folder. Merely selecting OneDrive does not create a GitHub repository or associate a cloud environment. Do not alter the confirmed project-sync frontend bug as part of this setup.

Cloud environment creation, interactive-container tests, an actual model-based task, desktop dispatch, native execution and user artifact delivery are separate verification stages. Record the stage actually exercised in verification/ and do not import another product's pass result.

## Future plugins

Use templates/NEW_PLUGIN.md and templates/AGENTS.md. Register the new repository and its setup/check commands in the catalog and profiles. Create and save its Codex environment through the existing GitHub connection, then run its actual checks. This provides a reusable process; it does not claim an unattended environment-provisioning service.

Official guidance: [Codex cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment) and [network configuration](https://learn.chatgpt.com/docs/cloud/internet-access).
