"""Compare Sonnet and Haiku triage labels, summarise zk_need, channel and signals, relate to critic v2 outcomes."""
import json, glob, collections, statistics as st, pathlib, yaml
root = pathlib.Path(__file__).resolve().parent.parent
S = {r["id"]: r for r in json.load(open(root / "triage/out_sonnet.json"))}; H = {r["id"]: r for r in json.load(open(root / "triage/out_haiku.json"))}
cat = {c["id"]: {x["id"] for x in c["claims"]} for c in yaml.safe_load(open(root / "config/certificates.yaml"))["certificates"]}
sch = yaml.safe_load(open(root / "config/triage_schema.yaml"))
def rev(pattern, keyfile, prefix):
    key = json.load(open(root / keyfile)); out = {}
    for f in glob.glob(str(root / pattern)):
        for r in json.load(open(f)): out[prefix + key[r["review_id"]]] = r
    return out
R = rev("critic2/out_*.json", "critic2/key.json", "p1:"); R.update(rev("critic_p2/out_*.json", "critic_p2/key.json", "p2:"))
real = lambda i: R[i]["norm_violation_today"]["violated"] == "yes" and R[i]["purpose_sufficiency"]["rating"] == "sufficient" and R[i]["transmission_check"]["permits_minimal_flow"] != "blocks"
ids = list(S); C = collections.Counter
print(len(ids), "ideas; ids match:", set(S) == set(H))
# validity of enum labels and catalogue references
for name, L in (("Sonnet", S), ("Haiku", H)):
    bad = []
    for i, r in L.items():
        if r["operator"] not in sch["predicate"]["operator"] or r["zk_need"] not in sch["predicate"]["zk_need"]: bad.append((i, "enum"))
        for x in r["inputs"]:
            if x.startswith("MISSING:"): continue
            cid, _, cl = x.partition(".")
            if cid not in cat or cl not in cat[cid]: bad.append((i, x))
    print(name, "invalid enums/inputs:", len(bad), bad[:6])
print("\nagreement Sonnet vs Haiku (of %d):" % len(ids))
for k in ("operator", "zk_need", "unlinkability_needed", "freshness_needed", "current_evidence", "interaction_mode", "verifier_reader", "harm_per_incident", "verifier_incentive", "split_incentive"):
    print(f"  {k:22}", sum(S[i][k] == H[i][k] for i in ids))
print("  reach_log10 within 1  ", sum(abs(S[i]["reach_log10"] - H[i]["reach_log10"]) <= 1 for i in ids), " exact", sum(S[i]["reach_log10"] == H[i]["reach_log10"] for i in ids))
print("  uses same set of certificates", sum({x.split(".")[0] for x in S[i]["inputs"]} == {x.split(".")[0] for x in H[i]["inputs"]} for i in ids))
print("\nSonnet distributions")
for k in ("operator", "zk_need", "current_evidence", "interaction_mode", "verifier_reader", "unlinkability_needed", "harm_per_incident", "verifier_incentive", "split_incentive", "reach_log10"):
    print(f"  {k:22}", dict(C(S[i][k] for i in ids).most_common()))
miss = [x for i in ids for x in S[i]["inputs"] if x.startswith("MISSING")]
print("\nMISSING attributes (Sonnet): %d refs in %d ideas" % (len(miss), sum(any(x.startswith("MISSING") for x in S[i]["inputs"]) for i in ids)), dict(C(miss).most_common(12)))
nin = [len([x for x in S[i]["inputs"] if not x.startswith("MISSING")]) for i in ids]; ncert = [len({x.split(".")[0] for x in S[i]["inputs"] if not x.startswith("MISSING")}) for i in ids]
print("claims per idea: mean %.1f; certificates per idea: %s" % (st.mean(nin), dict(C(ncert))))
print("\nzk_need: share needing real ZK (zk_*) vs not:", {"plain/issuer-precomputed": sum(S[i]["zk_need"] in ("plain_disclosure", "issuer_precomputed") for i in ids), "zk_*": sum(S[i]["zk_need"].startswith("zk_") for i in ids)})
print("\nrelation to critic v2 (Sonnet labels): n, real-opportunity count, mean rubric")
def grp(key, fn=lambda x: x):
    g = collections.defaultdict(list)
    for i in ids: g[fn(S[i][key])].append(i)
    for k, L in sorted(g.items(), key=lambda kv: str(kv[0])): print(f"  {key}={k!s:24} n={len(L):2} real={sum(map(real, L))} rubric={st.mean(R[i]['rubric_score'] for i in L):.2f}")
grp("interaction_mode"); grp("current_evidence"); grp("verifier_reader"); grp("zk_need", lambda v: "zk_*" if v.startswith("zk_") else v)
grp("verifier_incentive"); grp("harm_per_incident"); grp("split_incentive")
g = collections.defaultdict(list)
for i in ids: g["reach>=5" if S[i]["reach_log10"] >= 5 else "reach<=4"].append(i)
for k, L in g.items(): print(f"  {k:30} n={len(L):2} real={sum(map(real, L))} rubric={st.mean(R[i]['rubric_score'] for i in L):.2f}")
print("\n'easy first' cell: interaction already digital (remote_online or machine_mediated or in_person_with_device), no real ZK needed, verifier incentive >= 2:")
for i in ids:
    r = S[i]
    if r["interaction_mode"] in ("remote_online", "machine_mediated", "in_person_with_device") and not r["zk_need"].startswith("zk_") and r["verifier_incentive"] >= 2: print("  ", i, "|", r["zk_need"], "| harm", r["harm_per_incident"], "|", "REAL" if real(i) else "")
print("harm>=3 and photocopy/id-in-person today:")
for i in ids:
    r = S[i]
    if r["harm_per_incident"] >= 3 and r["current_evidence"] in ("paper_copy", "id_shown_in_person", "photo_of_id"): print("  ", i, "|", r["interaction_mode"], "| incentive", r["verifier_incentive"], "|", "REAL" if real(i) else "")
