"""Build prompts2/<cell>__<arm>.md for arms C (embedding-banded seeds) and D (random distinct-domain seeds).
Distances use Qwen3-Embedding-0.6B (LM Studio). Writes prompts2/manifest.json."""
import json, glob, yaml, math, random, hashlib, pathlib, urllib.request
root = pathlib.Path(__file__).resolve().parent.parent
cells = yaml.safe_load(open(root / "config/pilot2_cells.yaml")); ax = yaml.safe_load(open(root / "config/axes.yaml"))
seeds = {s["id"]: s for f in sorted(glob.glob(str(root / "seeds/*.yaml"))) for s in yaml.safe_load(open(f))}
cache_f = root / "cache/embeddings.json"; cache = json.loads(cache_f.read_text()) if cache_f.exists() else {}
def embed(texts):
    todo = [t for t in dict.fromkeys(texts) if hashlib.md5(t.encode()).hexdigest() not in cache]
    for i in range(0, len(todo), 32):
        b = todo[i:i + 32]
        req = urllib.request.Request("http://localhost:1234/v1/embeddings", json.dumps({"model": "text-embedding-qwen3-embedding-0.6b", "input": b}).encode(), {"Content-Type": "application/json"})
        for t, d in zip(b, json.load(urllib.request.urlopen(req, timeout=300))["data"]):
            v = d["embedding"]; n = math.sqrt(sum(x * x for x in v)); cache[hashlib.md5(t.encode()).hexdigest()] = [x / n for x in v]
    cache_f.write_text(json.dumps(cache)); return [cache[hashlib.md5(t.encode()).hexdigest()] for t in texts]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
tp_text = {k: v for k, v in ax["transmission_principle"].items()}
def target(c): return f"At {c['setting']}, a verifier needs to establish that the person {c['fact']}. Claim type: {c['predicate']}. Collected today under: {c['tp'].replace('_',' ')}."
SE = dict(zip(seeds, embed([s["abstract_problem"] for s in seeds.values()])))
TE = dict(zip([c["id"] for c in cells], embed([target(c) for c in cells])))
group_of = {l: g for g, ls in yaml.safe_load(open(root / "config/domains.yaml")).items() for l in ls}
grp = lambda s: group_of.get(s["domain"], s["domain"]); CENTRAL = {"identity-credentials", "government-admin", "finance"}
K = 6
def banded(cid, rng):
    d = {i: 1 - dot(SE[i], TE[cid]) for i in seeds}; ranked = sorted(seeds, key=lambda i: (d[i], i)); n = len(ranked)
    pos = {i: r for r, i in enumerate(ranked)}
    mid = [i for i in ranked if n * .4 <= pos[i] < n * .6]; far = [i for i in ranked if pos[i] >= n * .7]
    for _ in range(5000):
        ch = rng.sample(mid, 1) + rng.sample(far, K - 1); S = [seeds[i] for i in ch]
        if (len({s["domain"] for s in S}) == K and sum(grp(s) not in CENTRAL for s in S) >= 2
                and any(s.get("mechanism_outcome") in ("fails", "blocked-by-law") for s in S)
                and sum(s["distance_class"] == "distant-analog" for s in S) >= 2): return ch
    raise SystemExit("no banded draw " + cid)
def rand(rng):
    for _ in range(5000):
        ch = rng.sample(sorted(seeds), K)
        if len({seeds[i]["domain"] for i in ch}) == K: return ch
def block(ids):
    return "\n".join(f"- id: {i}\n  situation: {seeds[i]['abstract_problem']}\n  original setting: {seeds[i]['problem']}\n  mechanism: {seeds[i]['mechanism']} (outcome: {seeds[i].get('mechanism_outcome','unknown')})\n  evidence: \"{seeds[i]['evidence']['quote']}\"" for i in ids)
T = open(root / "docs/generator_prompt2.md").read(); man = {}
for c in cells:
    for arm, ids in (("C", banded(c["id"], random.Random("p2C" + c["id"]))), ("D", rand(random.Random("p2D" + c["id"])))):
        txt = (T.replace("{{SETTING}}", c["setting"]).replace("{{FACT}}", c["fact"]).replace("{{PREDICATE}}", c["predicate"])
               .replace("{{TP}}", c["tp"].replace("_", " ") + ": " + tp_text[c["tp"]]).replace("{{ORIGIN}}", c["origin"]).replace("{{USE}}", c["use"])
               .replace("{{SEEDS}}", block(ids)).replace("{{OUT}}", f"ideas2/{c['id']}__{arm}.json"))
        (root / "prompts2" / f"{c['id']}__{arm}.md").write_text(txt)
        man[f"{c['id']}__{arm}"] = {"seeds": ids, "dist": [round(1 - dot(SE[i], TE[c["id"]]), 3) for i in ids], "domains": [seeds[i]["domain"] for i in ids]}
(root / "prompts2/manifest.json").write_text(json.dumps(man, indent=1))
import statistics as st
for a in "CD": print(a, "mean seed distance", round(st.mean(x for k, v in man.items() if k.endswith("__" + a) for x in v["dist"]), 3))
print(len(man), "prompts")
