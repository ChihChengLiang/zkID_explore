"""Validate seeds/*.yaml against schema/seed.schema.json; check ids and `related` links."""
import json, sys, pathlib, yaml
from jsonschema import Draft202012Validator

root = pathlib.Path(__file__).resolve().parent.parent
schema = json.loads((root / "schema/seed.schema.json").read_text())
validator = Draft202012Validator(schema)

seeds, errors = [], 0
for f in sorted((root / "seeds").glob("*.yaml")):
    for s in yaml.safe_load(f.read_text()) or []:
        seeds.append((f.name, s))
        for e in validator.iter_errors(s):
            errors += 1
            print(f"{f.name}:{s.get('id')}: {'/'.join(map(str, e.path))}: {e.message}")

ids = [s["id"] for _, s in seeds]
for d in {i for i in ids if ids.count(i) > 1}:
    errors += 1; print(f"duplicate id: {d}")
for fn, s in seeds:
    for r in s.get("related", []):
        if r not in ids:
            errors += 1; print(f"{fn}:{s['id']}: related -> unknown id {r}")

print(f"{len(seeds)} seeds, {errors} errors")
sys.exit(1 if errors else 0)
