"""Validate the small Chembridge catalog and local documentation links."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "project-catalog.json").read_text(encoding="utf-8"))
profiles = json.loads((root / "cloud/profiles.json").read_text(encoding="utf-8"))
ids = [item["id"] for item in catalog["projects"]]
assert len(ids) == len(set(ids)), "Duplicate project IDs"
assert set(ids) == set(profiles), "Catalog/profile mismatch"
for item in catalog["projects"]:
    assert item["repository"].startswith("https://github.com/saigyujikingyo-png/")
    assert item["default_branch"] and item["cloud_environment"]
    assert profiles[item["id"]]["setup"] and profiles[item["id"]]["checks"]
    assert profiles[item["id"]]["scope"]
assert "2026-09-13.2" in (root / "DEVELOPMENT_PRINCIPLES.md").read_text(encoding="utf-8")
links = 0
for doc in [*root.glob("*.md"), *root.glob("templates/*.md")]:
    for target in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        if path:
            assert (doc.parent / path).exists(), f"Broken local link: {doc.name}: {path}"
            links += 1
print(f"PASS: {len(ids)} Chembridge project profiles and {links} local documentation links.")
print("Scope: hub configuration only; product and native acceptance remain separate.")
