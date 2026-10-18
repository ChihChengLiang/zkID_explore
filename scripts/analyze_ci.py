"""Summarise critic v2 (norm violation, purpose-sufficiency, ...) and the contextual-integrity classification."""
import json, glob, collections, statistics as st, pathlib, os
root = pathlib.Path(__file__).resolve().parent.parent
I = {i["id"]: i for i in json.loads((root / "ideas/all.json").read_text())}
k2 = json.loads((root / "critic2/key.json").read_text()); k1 = json.loads((root / "critic/key.json").read_text())
v2 = {}
for f in glob.glob(str(root / "critic2/out_*.json")):
    for r in json.load(open(f)): v2[k2[r["review_id"]]] = r
v1 = {}
for f in glob.glob(str(root / "critic/out_*.json")):
    for r in json.load(open(f)): v1[k1[r["review_id"]]] = r
print("critic v2 reviewed:", len(v2))
C = collections.Counter
arm = lambda i: I[i]["arm"]
print("\n== norm violation today:", C(v["norm_violation_today"]["violated"] for v in v2.values()))
print("   parameter violated:", C(v["norm_violation_today"]["parameter"] for v in v2.values()))
print("== purpose sufficiency:", C(v["purpose_sufficiency"]["rating"] for v in v2.values()))
print("== transmission principle today:", C(v["transmission_check"]["principle_today"] for v in v2.values()))
print("== permits minimal flow:", C(v["transmission_check"]["permits_minimal_flow"] for v in v2.values()))
print("== aggregation:", C(v["aggregation"] for v in v2.values()))
print("== issuer_willing:", C(v["adoption"]["issuer_willing"] for v in v2.values()), " verifier_can_check:", C(v["adoption"]["verifier_can_check"] for v in v2.values()))
print("== provenance_faithful v2:", C(v["provenance_faithful"] for v in v2.values()), "| v1:", C(v["provenance_faithful"] for v in v1.values()))
print("\n== cross-tab: purpose sufficiency x norm violation")
for s in ("sufficient", "partly", "insufficient"):
    print(f"   {s:13}", dict(C(v["norm_violation_today"]["violated"] for v in v2.values() if v["purpose_sufficiency"]["rating"] == s)))
good = [i for i, v in v2.items() if v["norm_violation_today"]["violated"] == "yes" and v["purpose_sufficiency"]["rating"] == "sufficient" and v["transmission_check"]["permits_minimal_flow"] != "blocks"]
print(f"\n== 'real opportunity' = violated yes AND sufficient AND not blocked: {len(good)}/96")
for a in "ABCD": print("   arm", a, sum(arm(i) == a for i in good), "/24")
print("\n== v1 vs v2 rubric score: mean v1 %.2f, v2 %.2f; exact agreement %d/96; within 1: %d/96" % (
    st.mean(v1[i]["rubric_score"] for i in v2), st.mean(v2[i]["rubric_score"] for i in v2),
    sum(v1[i]["rubric_score"] == v2[i]["rubric_score"] for i in v2), sum(abs(v1[i]["rubric_score"] - v2[i]["rubric_score"]) <= 1 for i in v2)))
print("\n== per arm means (v2): rubric / novelty ; v1 rubric / novelty")
for a in "ABCD":
    ids = [i for i in v2 if arm(i) == a]
    print(a, "%.2f %.2f ; %.2f %.2f" % (st.mean(v2[i]["rubric_score"] for i in ids), st.mean(v2[i]["novelty"] for i in ids),
          st.mean(v1[i]["rubric_score"] for i in ids), st.mean(v1[i]["novelty"] for i in ids)))
print("\n== per arm: sufficiency=sufficient / violated=yes / permits!=blocks counts of 24")
for a in "ABCD":
    ids = [i for i in v2 if arm(i) == a]
    print(a, sum(v2[i]["purpose_sufficiency"]["rating"] == "sufficient" for i in ids), sum(v2[i]["norm_violation_today"]["violated"] == "yes" for i in ids), sum(v2[i]["transmission_check"]["permits_minimal_flow"] != "blocks" for i in ids))

# CI classification
ck = json.loads((root / "classify/key.json").read_text())
def load(p):
    return {ck[r["id"]]: r for r in json.load(open(p))} if os.path.exists(p) else None
S = load(root / "classify/ci_sonnet.json"); H = load(root / "classify/ci_haiku.json")
print("\n== CI classification (Sonnet): context_distance", C(r["context_distance"] for r in S.values()))
print("   transmission principle:", C(r["transmission_principle"] for r in S.values()))
print("   origin ctx:", dict(C(r["origin_context"] for r in S.values()).most_common()))
print("   use ctx:   ", dict(C(r["use_context"] for r in S.values()).most_common()))
unused = set(json.loads(json.dumps(__import__("yaml").safe_load(open(root / "config/axes.yaml"))["context"]))) - {r["use_context"] for r in S.values()} - {r["origin_context"] for r in S.values()}
print("   contexts never used as origin or use:", sorted(unused))
if H:
    print("   Haiku agreement vs Sonnet:", {k: sum(S[i][k] == H[i][k] for i in S) for k in ("transmission_principle", "origin_context", "use_context", "context_distance")})
else: print("   (Haiku classification not in yet)")
print("\n== context_distance x purpose sufficiency / norm violated (Sonnet labels)")
for d in ("same", "adjacent", "different"):
    ids = [i for i in S if S[i]["context_distance"] == d]
    if ids: print(f"   {d:9} n={len(ids):2}  violated=yes {sum(v2[i]['norm_violation_today']['violated']=='yes' for i in ids)}  sufficient {sum(v2[i]['purpose_sufficiency']['rating']=='sufficient' for i in ids)}  mean rubric {st.mean(v2[i]['rubric_score'] for i in ids):.2f}  mean novelty {st.mean(v2[i]['novelty'] for i in ids):.2f}")
print("== transmission principle x permits minimal flow")
for tp in sorted({r["transmission_principle"] for r in S.values()}):
    ids = [i for i in S if S[i]["transmission_principle"] == tp]
    print(f"   {tp:22} n={len(ids):2}", dict(C(v2[i]["transmission_check"]["permits_minimal_flow"] for i in ids)), " mean rubric %.2f" % st.mean(v2[i]["rubric_score"] for i in ids))
print("\n== context distance by cell (Sonnet)")
for ce in sorted({I[i]["cell"] for i in I}):
    print(f"   {ce:16}", dict(C(S[i]["context_distance"] for i in S if I[i]["cell"] == ce)))
