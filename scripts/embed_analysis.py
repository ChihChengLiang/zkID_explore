"""Re-run pilot distance/diversity metrics with Qwen3-Embedding-0.6B served by LM Studio (localhost:1234).
Needs PYTHONPATH with openpyxl, numpy-free implementation (pure python)."""
import json, glob, math, yaml, pathlib, urllib.request, statistics as st, collections, itertools, hashlib
import openpyxl

root = pathlib.Path(__file__).resolve().parent.parent
MODEL = "text-embedding-qwen3-embedding-0.6b"
cache_f = root / "cache/embeddings.json"
cache = json.loads(cache_f.read_text()) if cache_f.exists() else {}

def embed(texts):
    todo = [t for t in dict.fromkeys(texts) if hashlib.md5(t.encode()).hexdigest() not in cache]
    for i in range(0, len(todo), 32):
        b = todo[i:i + 32]
        req = urllib.request.Request("http://localhost:1234/v1/embeddings",
            json.dumps({"model": MODEL, "input": b}).encode(), {"Content-Type": "application/json"})
        for t, d in zip(b, json.load(urllib.request.urlopen(req, timeout=300))["data"]):
            v = d["embedding"]; n = math.sqrt(sum(x * x for x in v))
            cache[hashlib.md5(t.encode()).hexdigest()] = [x / n for x in v]
    cache_f.write_text(json.dumps(cache))
    return [cache[hashlib.md5(t.encode()).hexdigest()] for t in texts]

dot = lambda a, b: sum(x * y for x, y in zip(a, b))
def vendi(V):                       # exp(entropy of eigenvalues of K/n); K = cosine kernel
    n = len(V); K = [[dot(a, b) for b in V] for a in V]
    # eigenvalues via power-free route: n is tiny (3), use numpy-free Jacobi
    A = [[K[i][j] / n for j in range(n)] for i in range(n)]
    for _ in range(60):
        for p in range(n):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-12: continue
                th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p]); c, s = math.cos(th), math.sin(th)
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]; A[k][p] = c * akp - s * akq; A[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]; A[p][k] = c * apk - s * aqk; A[q][k] = s * apk + c * aqk
    ev = [max(A[i][i], 1e-12) for i in range(n)]
    return math.exp(-sum(e * math.log(e) for e in ev))

ideas = json.loads((root / "ideas/all.json").read_text())
cells = {c["id"]: c for c in yaml.safe_load((root / "config/pilot_cells.yaml").read_text())}
seeds = {s["id"]: s for f in glob.glob(str(root / "seeds/*.yaml")) for s in yaml.safe_load(open(f))}
man = json.loads((root / "prompts/manifest.json").read_text())
hd = json.loads((root / "config/distance.json").read_text())
wb = openpyxl.load_workbook(root / "zkID_Taiwan_MyData_Use_Cases.xlsx", data_only=True)
known = [f"{r[1]}. Predicate: {r[3]}" for r in list(wb["Use Case Matrix"].iter_rows(values_only=True))[1:16]]

itext = [f"{i['title']}. {i['moment']} Verifier: {i['verifier']}. Predicate: {i['predicate']}" for i in ideas]
IE = embed(itext); KE = embed(known)
SE = dict(zip(seeds, embed([s["abstract_problem"] for s in seeds.values()])))
TE = dict(zip(cells, embed([c["target"] for c in cells.values()])))
for i, e in zip(ideas, IE): i["e"] = e

print("== 1. Do Haiku distance ratings agree with embedding distance? (Spearman per cell)")
def rank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
    for k, i in enumerate(o): r[i] = k
    return r
def spearman(a, b):
    ra, rb = rank(a), rank(b); ma = mb = (len(a) - 1) / 2
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    return num / math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
rs = []
for c in cells:
    ids = list(seeds); r = spearman([hd[c][i] for i in ids], [1 - dot(SE[i], TE[c]) for i in ids]); rs.append(r)
print("  rho per cell:", [round(r, 2) for r in rs], " mean", round(st.mean(rs), 2))

print("\n== 2. Mean embedding distance (1-cos) of each arm's seed set to the cell target")
for a in "BCD":
    d = [st.mean(1 - dot(SE[s], TE[c]) for s in man[f"{c}__{a}"]["seeds"]) for c in cells]
    print(" ", a, round(st.mean(d), 3), " per-cell min/max", round(min(d), 3), round(max(d), 3))

print("\n== 3. Within-cell diversity of each arm's 3 ideas (mean over 8 cells)")
print("  arm  pairwise-dist   vendi(3)   novelty-vs-workbook(1-max cos)   dist-to-cell-target")
res = {}
for a in "ABCD":
    pd, vd, nv, tg = [], [], [], []
    for c in cells:
        V = [i for i in ideas if i["cell"] == c and i["arm"] == a]; E = [i["e"] for i in V]
        pd.append(st.mean(1 - dot(x, y) for x, y in itertools.combinations(E, 2)))
        vd.append(vendi(E))
        nv += [1 - max(dot(e, k) for k in KE) for e in E]
        tg += [1 - dot(e, TE[c]) for e in E]
    res[a] = (pd, vd)
    print(f"  {a}   {st.mean(pd):.3f}±{1.96*st.stdev(pd)/math.sqrt(8):.3f}   {st.mean(vd):.2f}±{1.96*st.stdev(vd)/math.sqrt(8):.2f}"
          f"   {st.mean(nv):.3f}   {st.mean(tg):.3f}")

print("\n== 4. Paired by cell (arm minus A), mean diff in pairwise distance, and #cells where arm > A")
for a in "BCD":
    d = [x - y for x, y in zip(res[a][0], res["A"][0])]
    print(f"  {a}-A: {st.mean(d):+.3f}  (sd {st.stdev(d):.3f}, {sum(x>0 for x in d)}/8 cells higher)")
d = [x - y for x, y in zip(res["C"][0], res["D"][0])]
print(f"  C-D: {st.mean(d):+.3f}  (sd {st.stdev(d):.3f}, {sum(x>0 for x in d)}/8 cells higher)")

print("\n== 5. Cross-arm convergence: per cell, 12 ideas, greedy clusters at cos>=T")
for T in (0.80, 0.85, 0.90):
    nclu, conv = [], collections.Counter()
    for c in cells:
        V = [i for i in ideas if i["cell"] == c]; lab = {}
        for i, x in enumerate(V):
            for j in range(i):
                if dot(x["e"], V[j]["e"]) >= T: lab[i] = lab.get(j, j); break
            else: lab[i] = i
        nclu.append(len(set(lab.values())))
        for i, x in enumerate(V):
            if any(lab[j] == lab[i] and V[j]["arm"] != x["arm"] for j in range(len(V)) if j != i): conv[x["arm"]] += 1
    print(f"  T={T}: distinct clusters/cell mean {st.mean(nclu):.1f} of 12; ideas sharing cluster with another arm: " + " ".join(f"{a}={conv[a]}/24" for a in "ABCD"))
print("\ncos pairwise distribution (all same-cell pairs): ", end="")
allp = sorted(dot(x["e"], y["e"]) for c in cells for x, y in itertools.combinations([i for i in ideas if i["cell"] == c], 2))
print("p50 %.2f p75 %.2f p90 %.2f max %.2f" % (allp[len(allp)//2], allp[int(len(allp)*.75)], allp[int(len(allp)*.9)], allp[-1]))
