"""Validate ideas2/*.json (pilot 2) and write ideas2/all.json; builds blinded critic batches in critic_p2/."""
import json, glob, pathlib, random, collections, yaml
root = pathlib.Path(__file__).resolve().parent.parent
man = json.loads((root / "prompts2/manifest.json").read_text())
cells = {c["id"]: c for c in yaml.safe_load(open(root / "config/pilot2_cells.yaml"))}
seeds = {s["id"]: s for f in glob.glob(str(root / "seeds/*.yaml")) for s in yaml.safe_load(open(f))}
KEYS = {"title", "moment", "verifier", "predicate", "disclosed_today", "issuer", "why_zk", "inspired_by"}
out, problems = [], []
for k in sorted(man):
    p = root / f"ideas2/{k}.json"
    try: L = json.loads(p.read_text())
    except Exception as e: problems.append(f"{k}: parse {e}"); continue
    if not isinstance(L, list) or len(L) != 3: problems.append(f"{k}: {len(L) if isinstance(L, list) else 'not a list'} ideas"); continue
    used = set()
    for i, x in enumerate(L):
        if set(x) != KEYS: problems.append(f"{k}#{i}: keys {set(x) ^ KEYS}")
        ib = x.get("inspired_by") or []
        if not ib: problems.append(f"{k}#{i}: cites no seed")
        for b in ib:
            if b["seed_id"] not in man[k]["seeds"]: problems.append(f"{k}#{i}: seed {b['seed_id']} outside pool")
            used.add(b["seed_id"])
        out.append(dict(x, id=f"{k}__{i}", cell=k.rsplit("__", 1)[0], arm=k[-1]))
    if len(used) < 2: problems.append(f"{k}: only {len(used)} distinct seed(s) cited")
(root / "ideas2/all.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(len(out), "ideas;", collections.Counter(i["arm"] for i in out), "; problems:", problems or "none")
# blinded critic batches (v2 prompt)
(root / "critic_p2").mkdir(exist_ok=True)
random.Random(77).shuffle(out); key = {}
for b in range(0, len(out), 8):
    n = b // 8; batch = []
    for j, x in enumerate(out[b:b + 8]):
        rid = f"p{n:02d}-{j}"; key[rid] = x["id"]
        prov = [{"borrowed_aspect": q["borrowed_aspect"], "source_excerpt": seeds[q["seed_id"]]["abstract_problem"] + " | mechanism: " + seeds[q["seed_id"]]["mechanism"]} for q in x["inspired_by"]]
        batch.append({"review_id": rid, **{f: x[f] for f in ["title", "moment", "verifier", "predicate", "disclosed_today", "issuer", "why_zk"]}, "claimed_borrowings": prov})
    json.dump(batch, open(root / f"critic_p2/in_{n:02d}.json", "w"), ensure_ascii=False, indent=1)
json.dump(key, open(root / "critic_p2/key.json", "w"), indent=1)
print((len(out) + 7) // 8, "critic batches")
