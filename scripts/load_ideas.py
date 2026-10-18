"""Tolerant loader for generator output (values may contain ': ' which breaks strict YAML).
Writes ideas/all.json. Reports count, key and provenance problems."""
import re, glob, json, collections, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
man = json.loads((root / "prompts/manifest.json").read_text())
KEYS = ["title","moment","verifier","predicate","disclosed_today","issuer","why_zk","inspired_by"]
out, problems = [], []
for f in sorted(glob.glob(str(root / "ideas/*.yaml"))):
    k = pathlib.Path(f).stem
    items, cur, sect = [], None, None
    for line in open(f, encoding="utf-8").read().splitlines():
        if not line.strip(): continue
        m = re.match(r"^- (\w+):\s*(.*)$", line)
        if m:
            cur = {"inspired_by": []}; items.append(cur); cur[m[1]] = m[2].strip().strip('"'); sect = m[1]; continue
        m = re.match(r"^  (\w+):\s*(.*)$", line)
        if m and cur is not None and m[1] in KEYS:
            sect = m[1]
            if sect == "inspired_by": cur["inspired_by"] = []
            else: cur[sect] = m[2].strip().strip('"')
            continue
        m = re.match(r"^\s+- seed_id:\s*(\S+)", line)
        if m and cur is not None: cur["inspired_by"].append({"seed_id": m[1], "borrowed_aspect": ""}); continue
        m = re.match(r"^\s+borrowed_aspect:\s*(.*)$", line)
        if m and cur and cur["inspired_by"]: cur["inspired_by"][-1]["borrowed_aspect"] = m[1].strip().strip('"'); continue
        if cur is not None and sect and sect != "inspired_by":   # continuation line
            cur[sect] += " " + line.strip()
    if len(items) != 3: problems.append(f"{k}: {len(items)} ideas")
    for i, x in enumerate(items):
        miss = [q for q in KEYS if q not in x]
        if miss: problems.append(f"{k}#{i}: missing {miss}")
        for p in x["inspired_by"]:
            if p["seed_id"] not in man[k]["seeds"]: problems.append(f"{k}#{i}: seed {p['seed_id']} not in pool")
        if k.endswith("A") and x["inspired_by"]: problems.append(f"{k}#{i}: arm A has provenance")
        out.append(dict(x, id=f"{k}__{i}", cell=k[:-3], arm=k[-1]))
(root / "ideas/all.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(len(out), "ideas;", collections.Counter(i["arm"] for i in out), "; problems:", problems or "none")
