"""Build viz/flow.html: source -> attribute family -> consumer diagram for all 246 ideas.
Labels come from classify_sc/out_sonnet.json (primary); Haiku labels are used for an agreement report."""
import json, glob, pathlib, collections, yaml
root = pathlib.Path(__file__).resolve().parent.parent
ft = yaml.safe_load(open(root / "config/flow_types.yaml"))
def load_rev(pattern, keyfile):
    key = json.load(open(root / keyfile)); out = {}
    for f in glob.glob(str(root / pattern)):
        for r in json.load(open(f)): out[key[r["review_id"]]] = r
    return out
rev = {"p1:" + k: v for k, v in load_rev("critic2/out_*.json", "critic2/key.json").items()}
rev.update({"p2:" + k: v for k, v in load_rev("critic_p2/out_*.json", "critic_p2/key.json").items()})
ck = json.load(open(root / "classify/key.json")); fam = {"p1:" + ck[r["id"]]: r["family"] for r in json.load(open(root / "classify/out_sonnet.json"))}
cells2 = {c["id"]: c for c in yaml.safe_load(open(root / "config/pilot2_cells.yaml"))}
ideas = {"p1:" + i["id"]: i for i in json.load(open(root / "ideas/all.json"))}
ideas.update({"p2:" + i["id"]: i for i in json.load(open(root / "ideas2/all.json"))})
for k, i in ideas.items():
    if k.startswith("p2:"): fam[k] = cells2[i["cell"]]["family"]
lab = {r["id"]: r for r in json.load(open(root / "classify_sc/out_sonnet.json"))}
hk = root / "classify_sc/out_haiku.json"
if hk.exists():
    h = {r["id"]: r for r in json.load(open(hk))}
    print("Haiku agreement: source %d/%d, consumer %d/%d" % (sum(lab[i]["source_type"] == h[i]["source_type"] for i in lab), len(lab), sum(lab[i]["consumer_type"] == h[i]["consumer_type"] for i in lab), len(lab)))
bad = [i for i in ideas if i not in lab or lab[i]["source_type"] not in ft["source_types"] or lab[i]["consumer_type"] not in ft["consumer_types"]]
assert not bad, bad[:5]
print("other sources:", [(i, lab[i]["other_note"]) for i in lab if lab[i]["source_type"] == "other"][:10])
print("other consumers:", [(i, lab[i]["other_note"]) for i in lab if lab[i]["consumer_type"] == "other"][:10])
data = []
for k, i in ideas.items():
    r = rev[k]; real = r["norm_violation_today"]["violated"] == "yes" and r["purpose_sufficiency"]["rating"] == "sufficient" and r["transmission_check"]["permits_minimal_flow"] != "blocks"
    data.append({"id": k, "pilot": int(k[1]), "title": i["title"], "issuer": i["issuer"], "verifier": i["verifier"], "family": fam[k], "source": lab[k]["source_type"], "consumer": lab[k]["consumer_type"], "real": bool(real), "rubric": r["rubric_score"], "novelty": r["novelty"]})
tpl = (root / "scripts/flow_template.html").read_text()
meta = {"sources": ft["source_types"], "consumers": ft["consumer_types"]}
(root / "viz/flow.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace("__META__", json.dumps(meta, ensure_ascii=False)))
print(len(data), "ideas;", len({d["source"] for d in data}), "source types,", len({d["consumer"] for d in data}), "consumer types used")
pairs = collections.Counter((d["source"], d["consumer"]) for d in data)
print("distinct (source, consumer) pairs:", len(pairs), "; top:", pairs.most_common(5))
