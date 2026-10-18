"""Join blinded critic scores + clusters back to arms and print the pilot summary."""
import json, glob, statistics as st, collections, pathlib, math
root = pathlib.Path(__file__).resolve().parent.parent
key = json.loads((root / "critic/key.json").read_text())
ideas = {i["id"]: i for i in json.loads((root / "ideas/all.json").read_text())}
rev = {}
for f in sorted(glob.glob(str(root / "critic/out_*.json"))):
    for r in json.load(open(f)): rev[key[r["review_id"]]] = r
print(f"reviewed {len(rev)}/96")
arms = "ABCD"
def per(arm): return [i for i in ideas if ideas[i]["arm"] == arm and i in rev]
def mean_ci(v):
    if len(v) < 2: return (round(st.mean(v), 2), 0)
    return round(st.mean(v), 2), round(1.96 * st.stdev(v) / math.sqrt(len(v)), 2)
print("\nmean score (±95% CI half-width)")
print("arm  n  rubric        validity      coherence     novelty")
for a in arms:
    ids = per(a)
    row = [mean_ci([rev[i][m] for i in ids]) for m in ("rubric_score", "validity", "coherence", "novelty")]
    print(a, f"{len(ids):>3}", "  ".join(f"{m:.2f}±{c:.2f}" for m, c in row))
print("\nkill-test survival (no 'fails') and per-test fail rate; provenance abandonment")
for a in arms:
    ids = per(a); T = ["retention_law", "linkability", "issuer_unwilling", "no_wallet"]
    surv = sum(all(rev[i]["kill_tests"][t] != "fails" for t in T) for i in ids) / len(ids)
    fr = {t: round(sum(rev[i]["kill_tests"][t] == "fails" for i in ids) / len(ids), 2) for t in T}
    pf = [rev[i]["provenance_faithful"] for i in ids if rev[i]["provenance_faithful"] != "NA"]
    ab = f"{pf.count('no')}/{len(pf)}" if pf else "n/a"
    print(a, f"survive={surv:.2f}", fr, "abandoned", ab)
print("\nvalid & novel (validity>=3 and novelty>=3) per arm; cells covered with >=1 such idea")
for a in arms:
    ids = [i for i in per(a) if rev[i]["validity"] >= 3 and rev[i]["novelty"] >= 3]
    print(a, len(ids), "ideas;", len({ideas[i]["cell"] for i in ids}), "/8 cells")
cf = root / "critic/clusters.json"
if cf.exists():
    ck = json.loads((root / "critic/cluster_key.json").read_text())
    cl = json.loads(cf.read_text())["clusters"]
    print(f"\nclusters overall: {len(cl)} for 96 ideas")
    c_of = {ck[x]: n for n, c in enumerate(cl) for x in c}
    for a in arms:
        ids = [i for i in ideas if ideas[i]["arm"] == a]
        print(a, "distinct clusters", len({c_of[i] for i in ids}), "of", len(ids),
              "| clusters unique to this arm", sum(1 for n in {c_of[i] for i in ids}
                  if all(ideas[j]["arm"] == a for j in c_of if c_of[j] == n)))
    cross = sum(1 for c in cl if len({ideas[ck[x]]["cell"] for x in c}) > 1)
    print("clusters spanning >1 cell:", cross)
