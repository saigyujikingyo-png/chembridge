# Code Relay registration and preview acceptance

Date: 14 September 2026. Shared principles: **2026-09-14.1**.

## Corrective preview 0.1.1

The 0.1.0 release-commit CI exposed intermittent Windows access denial while
acquiring the local budget lock. Version 0.1.1 bounds retries of local lock
acquisition and returns a stable busy/inaccessible error if denial persists;
the fix never retries provider requests. Public output contract 1.0 is unchanged.

Corrective runtime SHA: `30ed044c3371732c99772b67a8ec0ed68234f9af`.
All six public Windows/Ubuntu Python 3.11/3.12/3.13 CI jobs passed at that SHA:
https://github.com/saigyujikingyo-png/code-relay/actions/runs/34876588452.
The product receipt includes synthetic regression/stress checks and package
hashes. Private installation and cloud acceptance metadata is excluded from
this update and retained in the private development task.

Current distribution: https://github.com/saigyujikingyo-png/code-relay/releases/tag/v0.1.1.
Evidence: product `verification/2026-09-14-preview-0.1.1.md`.
The earlier release and record below remain historical evidence.

## Initial registration and 0.1.0 history

Code Relay is an independent MIT-licensed, Codex-first coding-workflow plugin.
Its host-neutral standard-library core delegates bounded routine work to
user-configured OpenAI-compatible and Anthropic models. Architecture, advanced
implementation and final review stay with the host. Multiple ELM model profiles
can share a user-supplied connection; exact IDs and entitlements remain
account-specific. Plugin runtime code never reads host account credentials.

Repository: https://github.com/saigyujikingyo-png/code-relay.
Default branch: `codex/initial-preview`.
Implementation: `3627bb04535cf09cd834bdd0a95c35a9d65a9008`.
Distribution: https://github.com/saigyujikingyo-png/code-relay/releases/tag/v0.1.0.

The matching **Chembridge / Code Relay** cloud environment was created, saved
and read back in the official environment list and detail page. Both saved
setup and maintenance commands are `bash scripts/setup_codex_cloud.sh`.
The existing universal-image, Python 3.12, caching and common-dependencies
network policy was used. No private data or model credentials were added.
Environment/account identifiers and detailed host metadata are not published.

At the implementation commit, the Python 3.12.13 cloud check reported 99 tests
in 4.785 s, OK (1 skipped); the headless Tk class does not run its GUI methods.
Real stdio discovered seven output schemas and validated status/errors plus
the JSON text fallback. The synthetic provider workflow made two loopback HTTP
calls, left source unchanged and took 50 ms in the core. Setup and maintenance
passed, and the terminal confirmed the exact Git SHA. No model-based cloud
task or desktop cloud dispatch is claimed.

The local suite reported 104 tests in 9.127 s, 103 passed and one skipped for
unavailable symlink creation. Six Windows/Ubuntu CI jobs passed Python
3.11/3.12/3.13 at the same commit:
https://github.com/saigyujikingyo-png/code-relay/actions/runs/34874468082.

All seven public tools declare outputSchema and validate matching
structuredContent with an identical JSON text fallback. Eighteen focused
contract tests cover lifecycle/error/null/artifact branches, malformed output
rejection without repeating work, and known-ID preservation. Per-tool coverage
is maintained in the product's `docs/OUTPUT_CONTRACTS.md`.

The bundled Windows runtime passed self-test and actual installed stdio checks.
A real model invoked the status tool successfully, but also made an unrelated
read-only call contrary to the bounded prompt. That establishes status-tool
callability, not a fully accepted coding workflow or savings benchmark.

READY: shared-rule inheritance, public source, output contracts, portable/CI/
container checks, tested same-device package/install/stdio.
PARTIAL: graphical configuration and real host-model workflow acceptance.
UNVERIFIED: live ELM/OpenAI-compatible/Anthropic, representative Terra max
coding benchmark and savings, new-device/removal, other hosts and ChatGPT Work.

The hub catalog/profile check passed with four products. This records an
actually saved matching environment, not automatic future provisioning or
another product's acceptance.
