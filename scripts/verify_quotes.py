"""For each seed, check evidence.quote appears verbatim (whitespace-normalised) in its snapshot.
Sets quote_verified accordingly and rewrites the YAML. Exit 1 if any seed fails."""
import sys, re, pathlib, yaml, json
from jsonschema import Draft202012Validator

root = pathlib.Path(__file__).resolve().parent.parent
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
validator = Draft202012Validator(json.loads((root / "schema/seed.schema.json").read_text()))
bad = total = 0
for f in sorted((root / "seeds").glob("*.yaml")):
    seeds = yaml.safe_load(f.read_text()) or []
    for s in seeds:
        total += 1
        errs = [e.message for e in validator.iter_errors(s)]
        snap = root / s["evidence"].get("snapshot", "") if s.get("evidence", {}).get("snapshot") else None
        ok = False
        if snap and snap.exists():
            ok = norm(s["evidence"]["quote"]) in norm(snap.read_text())
            s["evidence"]["quote_verified"] = ok
        elif s.get("evidence", {}).get("quote_verified"):
            ok = True  # hand-verified example without snapshot
        if errs or not ok:
            bad += 1
            print(f"FAIL {s.get('id')}: schema={errs} quote_found={ok}")
    f.write_text(yaml.safe_dump(seeds, sort_keys=False, allow_unicode=True, width=100))
print(f"{total} seeds, {bad} failing")
sys.exit(1 if bad else 0)
