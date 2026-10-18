"""Pilot-2 analysis: C (banded) vs D (random), critic v2, embedding diversity and distance from pilot 1."""
import json, glob, math, hashlib, statistics as st, collections, itertools, pathlib, urllib.request, yaml
root = pathlib.Path(__file__).resolve().parent.parent
ideas = {i["id"]: i for i in json.loads((root / "ideas2/all.json").read_text())}
key = json.loads((root / "critic_p2/key.json").read_text())
rev = {}
for f in glob.glob(str(root / "critic_p2/out_*.json")):
    for r in json.load(open(f)): rev[key[r["review_id"]]] = r
cells = {c["id"]: c for c in yaml.safe_load(open(root / "config/pilot2_cells.yaml"))}
print("reviewed", len(rev), "/", len(ideas))
C = collections.Counter; arm = lambda i: ideas[i]["arm"]
def ci(v): return f"{st.mean(v):.2f}±{(1.96*st.stdev(v)/math.sqrt(len(v))) if len(v)>1 else 0:.2f}"
real = lambda i: (rev[i]["norm_violation_today"]["violated"] == "yes" and rev[i]["purpose_sufficiency"]["rating"] == "sufficient" and rev[i]["transmission_check"]["permits_minimal_flow"] != "blocks")
print("\narm  n  rubric       novelty      real-opp  sufficient  violated  blocks  prov-yes/no/NA")
for a in "CD":
    ids = [i for i in rev if arm(i) == a]
    pr = C(rev[i]["provenance_faithful"] for i in ids)
    print(a, len(ids), ci([rev[i]["rubric_score"] for i in ids]), ci([rev[i]["novelty"] for i in ids]), sum(map(real, ids)), sum(rev[i]["purpose_sufficiency"]["rating"] == "sufficient" for i in ids),
          sum(rev[i]["norm_violation_today"]["violated"] == "yes" for i in ids), sum(rev[i]["transmission_check"]["permits_minimal_flow"] == "blocks" for i in ids), f"{pr['yes']}/{pr['no']}/{pr['NA']}")
print("\nreal opportunities per cell (of 6 ideas):")
for c in cells: print(f"  {c:18}", sum(real(i) for i in rev if ideas[i]["cell"] == c), "  C:", sum(real(i) for i in rev if ideas[i]["cell"] == c and arm(i) == "C"), " D:", sum(real(i) for i in rev if ideas[i]["cell"] == c and arm(i) == "D"))
print("\nrubric dist:", dict(sorted(C(r["rubric_score"] for r in rev.values()).items())), " norm violated:", C(r["norm_violation_today"]["violated"] for r in rev.values()), " violated parameter:", C(r["norm_violation_today"]["parameter"] for r in rev.values()))
print("transmission today (critic):", C(r["transmission_check"]["principle_today"] for r in rev.values()), "| cell-assigned:", C(c["tp"] for c in cells.values()))
print("permits:", C(r["transmission_check"]["permits_minimal_flow"] for r in rev.values()), " aggregation:", C(r["aggregation"] for r in rev.values()), " issuer_willing:", C(r["adoption"]["issuer_willing"] for r in rev.values()))
print("\nby attribute family (cell-assigned): n, mean rubric, real-opp")
fam = collections.defaultdict(list)
for i in rev: fam[cells[ideas[i]["cell"]]["family"]].append(i)
for f, ids in sorted(fam.items()): print(f"  {f:24} n={len(ids):2} rubric {st.mean(rev[i]['rubric_score'] for i in ids):.2f} real {sum(map(real, ids))}")
print("by transmission principle (cell-assigned): n, mean rubric, real-opp, permits/unclear/blocks")
tp = collections.defaultdict(list)
for i in rev: tp[cells[ideas[i]["cell"]]["tp"]].append(i)
for f, ids in sorted(tp.items()): print(f"  {f:24} n={len(ids):2} rubric {st.mean(rev[i]['rubric_score'] for i in ids):.2f} real {sum(map(real, ids))}", dict(C(rev[i]["transmission_check"]["permits_minimal_flow"] for i in ids)))
# embeddings
cache_f = root / "cache/embeddings.json"; cache = json.loads(cache_f.read_text()) if cache_f.exists() else {}
def emb(texts):
    todo = [t for t in dict.fromkeys(texts) if hashlib.md5(t.encode()).hexdigest() not in cache]
    for i in range(0, len(todo), 32):
        b = todo[i:i + 32]; req = urllib.request.Request("http://localhost:1234/v1/embeddings", json.dumps({"model": "text-embedding-qwen3-embedding-0.6b", "input": b}).encode(), {"Content-Type": "application/json"})
        for t, d in zip(b, json.load(urllib.request.urlopen(req, timeout=300))["data"]):
            v = d["embedding"]; n = math.sqrt(sum(x * x for x in v)); cache[hashlib.md5(t.encode()).hexdigest()] = [x / n for x in v]
    cache_f.write_text(json.dumps(cache)); return [cache[hashlib.md5(t.encode()).hexdigest()] for t in texts]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
tx = lambda i: f"{i['title']}. {i['moment']} Verifier: {i['verifier']}. Predicate: {i['predicate']}"
p1 = json.loads((root / "ideas/all.json").read_text())
E2 = dict(zip(ideas, emb([tx(ideas[i]) for i in ideas]))); E1 = emb([tx(i) for i in p1])
print("\n== embedding diversity (1-cos), pilot 2")
for a in "CD":
    pd = []
    for c in cells:
        V = [E2[i] for i in ideas if ideas[i]["cell"] == c and arm(i) == a]; pd.append(st.mean(1 - dot(x, y) for x, y in itertools.combinations(V, 2)))
    print(f"  within-cell pairwise distance, arm {a}: {st.mean(pd):.3f} (sd over cells {st.stdev(pd):.3f})")
dC = [st.mean(1 - dot(x, y) for x, y in itertools.combinations([E2[i] for i in ideas if ideas[i]['cell'] == c and arm(i) == 'C'], 2)) - st.mean(1 - dot(x, y) for x, y in itertools.combinations([E2[i] for i in ideas if ideas[i]['cell'] == c and arm(i) == 'D'], 2)) for c in cells]
print(f"  C minus D paired by cell: {st.mean(dC):+.3f}, C higher in {sum(x>0 for x in dC)}/{len(dC)} cells")
nov = {a: [1 - max(dot(E2[i], e) for e in E1) for i in ideas if arm(i) == a] for a in "CD"}
allp1 = [1 - max(dot(E2[i], e) for e in E1) for i in ideas]
print("  distance of pilot-2 ideas from nearest pilot-1 idea (1-max cos): C %.3f  D %.3f ; overall mean %.3f, p10 %.3f" % (st.mean(nov["C"]), st.mean(nov["D"]), st.mean(allp1), sorted(allp1)[len(allp1) // 10]))
# within pilot 2: cross-cell duplicates
pairs = [(dot(E2[a], E2[b]), a, b) for a, b in itertools.combinations(ideas, 2) if ideas[a]["cell"] != ideas[b]["cell"]]
print("  cross-cell pairs with cos>=0.85:", sum(p[0] >= 0.85 for p in pairs), "of", len(pairs), "; max cos", round(max(p[0] for p in pairs), 3))
