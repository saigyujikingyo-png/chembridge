# Add a Chembridge plugin

1. Create a dedicated public GitHub repository with an explicit source licence. Keep restricted software and private data out of the repository.
2. Copy the current DEVELOPMENT_PRINCIPLES.md and adapt templates/AGENTS.md with the product's real scope, setup and checks. Add the repository to project-catalog.json and cloud/profiles.json.
3. Keep the development checkout outside cloud sync. Prefer one source tree and execution core across supported agent hosts and models.
4. Define meaningful output schemas and server-side validation for every public tool and dispatched operation, following shared principles section 12. Include lifecycle/error branches, media metadata, backward compatibility, a per-operation coverage record and focused contract checks in the product plan. Keep detailed schemas discoverable on demand.
5. Create a Codex Web environment named `Chembridge / Product Name`, using the existing GitHub connection. Select the actual repository, pin the runtime, install the locked dependencies, and enable caching with an idempotent maintenance command.
6. Run the repository's real portable tests in the cloud terminal. Record commit, platform, runtime, timings and results. Use a separate authorised device for native licensed software and account-specific acceptance.
7. Save the environment and verify it appears in the cloud selector. Record model-based tasks and desktop dispatch only when separately exercised. Publish evidence and keep preview/stable claims accurate.

Do not add a second paid model layer, a central database or a resident service merely to adopt these conventions. Keep each environment limited to the dependencies needed by that product.

Before implementation, classify runtime components under [the lifecycle contract](../RUNTIME_LIFECYCLE.md) and complete [a lifecycle record](LIFECYCLE_RECORD.md). Define startup/shutdown/crash ownership, profile/session cardinality, readiness, retry cleanup, native/job lifetime, OS-event behavior and lifecycle-preserving installation/upgrade/removal. Record local and remote host acceptance separately; autostart is required only by the product's declared lifecycle.

Assign one Product Max owner under [the ownership policy](../governance/OWNERSHIP.md), retain Governance High review of shared gaps, and use Ultra only for bounded expert questions. Copy all referenced shared contracts with the principles, or use explicit versioned references that remain resolvable in the product checkout. Existing-product migration requires a safe checkpoint, handoff and verified takeover receipt.
