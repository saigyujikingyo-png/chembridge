# Source parity evidence

This records a cross-product review finding from incident CB-2026-001. It clarifies evidence wording without changing the current shared-rule version or any frozen package.

## Finding

Three reviewed Windows candidates used hashes of a clean working checkout or archive output as if they proved byte equality with raw committed Git objects. Git attributes and checkout conversion can change line endings while the checkout remains clean. A generated archive may already contain those conversions. Comparing two converted representations does not establish equality with raw Git blobs.

| Reviewed candidate | Independently checked distinction |
| --- | --- |
| Origin 0.2.12 runtime source inventory | 41 working-checkout hashes match; 23 raw Git matches and 18 CRLF/LF-only differences |
| UoE 0.8.2 source archive | 133 raw Git matches and four declared PowerShell EOL conversions; BOMs unchanged |
| MATLAB Alpha.4 P1 engineering candidate | 16 product files match frozen checkout and wheel: 11 raw Git matches plus five EOL-only differences. Its 80 reference files have 42 raw matches plus 38 EOL-only differences |

No other byte differences were found in those scoped comparisons. This is not permission to normalize arbitrary differences or inherit a result for later commits/packages.

## Recording an accurate result

Name the exact commit, representation and artifact hash. Distinguish raw Git object bytes, working-checkout bytes, archive members, wheel members and installed files. Compare raw Git objects directly when making that claim. Record a declared transformation separately, with before/after hashes and an explicit normalized comparison; retain encoding/BOM differences as independent facts.

If a previous receipt overstated equality, retain it and append a correction explaining the mistaken comparison and the new evidence. Do not silently rewrite the old failure or broaden a clean-checkout statement into an exact-blob guarantee. A correct EOL-only explanation may close a documentation defect without requiring a runtime rebuild; semantic differences still require product review.

Package integrity, source correspondence, installed activation and native/host acceptance remain separate. This note proves none of those stages beyond the comparisons explicitly recorded above.
