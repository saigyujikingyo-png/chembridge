# Controlled maintenance review evidence

Date: 2026-09-19. This is an observed engineering record under shared rule
2026-09-19.1, not a new rule version or a claim that the incident is closed.
Product owners retain implementation and acceptance ownership.

## Package checks can change the package

The reviewed MATLAB Alpha.4 package's passive self-test created 510 undeclared
bytecode files when run normally in an isolated fresh copy. It changed no declared
source files. A second fresh copy using `-I -B` created no extra files, changed no
package bytes and did not create a job root. The private maintenance self-test uses
that verified form. Normal later host use may still create caches; a claim of
permanently cache-free operation would be incorrect.

Distinguish exact packaged-file identity, declared mutable caches and preserved
user data. Test the actual installed invocation, not only the source function.
Do not treat a legitimate cache as a scientific effect or silently ignore arbitrary
extra files to make an integrity assertion pass.

## Windows bootstrap is part of the execution boundary

A UoE bootstrap's ancestor walk originally used `Parent` on a `FileInfo`, which
ended the walk early. The correction uses `Directory` for files and `Parent` for
directories. A real temporary junction regression confirmed refusal before the
interpreter was launched. The original 53-test result and the later correction
remain separate; Governance independently passed the four affected bootstrap
checks, and the owner reported 54 tests passing for the corrected complete suite.
The unused initial review grant was revoked before any live use and then replaced
with the corrected wrapper hash.

An isolated shared-launcher test also showed that Windows PowerShell invoked by
Python inherited a module path that hid `Get-FileHash`. Selecting that process's
own `PSHOME/Modules` fixed the observed bootstrap failure. Synthetic success,
first-product failure and repeat-launch refusal then passed. These fixtures ran
only fake commands, not real upgrades, task stops or campus calls.

## Freeze the reviewed executable inputs

A maintenance review names exact helper, plan, package and adapter hashes. Keep
immutable review copies and distinguish their filenames from executable entrypoints.
A later helper edit invalidates an earlier hash grant even when its intended change
is small. Reconcile the original operation's intent/result before deciding whether
a stage ran; do not repeat a possible write to recover a response.

One Governance snapshot check initially addressed a copy without its intentional
`.txt` suffix and failed before grant creation. The surrounding shell continued,
so its overall exit alone did not prove the check succeeded. The premature internal
notification was immediately corrected; actual filenames and all seven file hashes
were then verified before issuing the grant. Retain individual command outcomes
and verify written artifacts before reporting a multi-step operation complete.

## Installation and loaded host connections differ

Origin's installed version and a real connector status call agreed at 0.2.12.
Mnova's new installed cache and exact registered subprocess returned dev2, while
its already-running product task still returned dev1. Code Relay's installed
docs.1 resources were current while old executable processes remained.

Use supported normal host release and fresh connection acceptance. Do not infer
hot reload from installed files or terminate processes by basename to manufacture
that result. Preserve another product's active work until its safe checkpoint.

ChemDraw's diagnostic preview independently demonstrated raw Git-to-package and
upstream-runtime parity, installed-file parity and official MCP connection
readback. A direct probe of that registered command is still not a fresh model
tool call. Its ordinary build command suppresses bytecode creation during package
verification; diagnostic execution leaves the reviewed package unchanged. The
installed tool reports native execution as frozen instead of importing historical
native results into a new acceptance claim.

Cross-product maintenance captures a fresh configuration baseline when its window
begins. The MATLAB helper verifies that unrelated configuration survives its own
switch, including a ChemDraw connection installed before that window. A stale
whole-configuration snapshot must not become permission to overwrite another
product's later registration.

## Process retirement does not resolve scientific outcome

A later independently observed OS boot boundary can prove that a historical
user-mode process chain no longer exists. It cannot prove that an interrupted
scientific job succeeded, failed or was cancelled. The current-device MATLAB
maintenance admission additionally checks original job hashes, current owners and
launch sources, and preserves the unknown result and idempotency state.

The reviewed finite UoE and MATLAB entrypoints remain subject to fresh admission
after normal host release. Prepared helpers, staged files, portable regressions
and published packages are not evidence that those live upgrades ran. See the
[current migration ledger](MIGRATION.md) for actual product delivery states and
[source parity record](SOURCE_PARITY.md) for archive/Git byte comparisons.
