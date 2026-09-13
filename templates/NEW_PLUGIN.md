# Add a Chembridge plugin

1. Create a dedicated public GitHub repository with an explicit source licence. Keep restricted software and private data out of the repository.
2. Copy the current DEVELOPMENT_PRINCIPLES.md and adapt templates/AGENTS.md with the product's real scope, setup and checks. Add the repository to project-catalog.json and cloud/profiles.json.
3. Keep the development checkout outside cloud sync. Prefer one source tree and execution core across supported agent hosts and models.
4. Create a Codex Web environment named `Chembridge / Product Name`, using the existing GitHub connection. Select the actual repository, pin the runtime, install the locked dependencies, and enable caching with an idempotent maintenance command.
5. Run the repository's real portable tests in the cloud terminal. Record commit, platform, runtime, timings and results. Use a separate authorised device for native licensed software and account-specific acceptance.
6. Save the environment and verify it appears in the cloud selector. Record model-based tasks and desktop dispatch only when separately exercised. Publish evidence and keep preview/stable claims accurate.

Do not add a second paid model layer, a central database or a resident service merely to adopt these conventions. Keep each environment limited to the dependencies needed by that product.
