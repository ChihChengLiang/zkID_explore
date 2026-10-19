"""Build viz/whiteboard.html with both pilots' ideas (96 + 150), placed by t-SNE of Qwen3 embeddings
(title + moment + verifier + issuer + predicate). Reviews are critic v2 for both pilots.
Needs numpy + scikit-learn on PYTHONPATH and LM Studio serving the embedding model."""
import json, glob, pathlib, urllib.request, yaml
import numpy as np
from sklearn.manifold import TSNE
root = pathlib.Path(__file__).resolve().parent.parent
def load_rev(pattern, keyfile):
    key = json.load(open(root / keyfile)); out = {}
    for f in glob.glob(str(root / pattern)):
        for r in json.load(open(f)): out[key[r["review_id"]]] = r
    return out
rev1 = load_rev("critic2/out_*.json", "critic2/key.json"); rev2 = load_rev("critic_p2/out_*.json", "critic_p2/key.json")
fam1 = {}; ci1 = {}
ck = json.load(open(root / "classify/key.json"))
for r in json.load(open(root / "classify/out_sonnet.json")): fam1[ck[r["id"]]] = r["family"]
for r in json.load(open(root / "classify/ci_sonnet.json")): ci1[ck[r["id"]]] = r
cells2 = {c["id"]: c for c in yaml.safe_load(open(root / "config/pilot2_cells.yaml"))}
ADJ = {frozenset(p) for p in [("healthcare","government_admin"),("employment","finance"),("education","government_admin"),("housing","government_admin"),("family_social","government_admin"),("family_social","healthcare"),("family_social","education"),("finance","government_admin"),("housing","civic_community"),("civic_community","government_admin"),("justice_security","government_admin"),("employment","civic_community"),("education","employment"),("education","civic_community"),("government_admin","commerce"),("justice_security","civic_community"),("housing","employment"),("civic_community","religion"),("family_social","civic_community")]}
def dist2(c): return "same" if c["origin"] == c["use"] else ("adjacent" if frozenset((c["origin"], c["use"])) in ADJ else "different")
items = []
for i in json.load(open(root / "ideas/all.json")):
    r = rev1[i["id"]]; c = ci1[i["id"]]
    items.append(dict(i, pilot=1, rid="p1:" + i["id"], rv=r, family=fam1[i["id"]], tp=c["transmission_principle"], dist=c["context_distance"], origin=c["origin_context"], use=c["use_context"], setting="", fact=""))
for i in json.load(open(root / "ideas2/all.json")):
    r = rev2[i["id"]]; c = cells2[i["cell"]]
    items.append(dict(i, pilot=2, rid="p2:" + i["id"], rv=r, family=c["family"], tp=c["tp"], dist=dist2(c), origin=c["origin"], use=c["use"], setting=c["setting"], fact=c["fact"]))
texts = [f"{i['title']}. {i['moment']} Verifier: {i['verifier']}. Issuer: {i['issuer']}. Predicate: {i['predicate']}" for i in items]
E = []
for k in range(0, len(texts), 32):
    req = urllib.request.Request("http://localhost:1234/v1/embeddings", json.dumps({"model": "text-embedding-qwen3-embedding-0.6b", "input": texts[k:k + 32]}).encode(), {"Content-Type": "application/json"})
    E += [d["embedding"] for d in json.load(urllib.request.urlopen(req, timeout=300))["data"]]
E = np.array(E); E /= np.linalg.norm(E, axis=1, keepdims=True); S = E @ E.T
xy = TSNE(n_components=2, perplexity=15, metric="cosine", init="pca", random_state=3).fit_transform(E)
xy -= xy.min(0); xy /= xy.max(0)
data = []
for n, i in enumerate(items):
    r = i["rv"]; nb = [j for j in np.argsort(-S[n]) if j != n][:3]
    real = r["norm_violation_today"]["violated"] == "yes" and r["purpose_sufficiency"]["rating"] == "sufficient" and r["transmission_check"]["permits_minimal_flow"] != "blocks"
    data.append({
        "id": i["rid"], "pilot": i["pilot"], "cell": i["cell"], "arm": i["arm"], "title": i["title"], "moment": i["moment"], "verifier": i["verifier"],
        "predicate": i["predicate"], "issuer": i["issuer"], "disclosed": i["disclosed_today"], "why": i["why_zk"], "borrowed": i["inspired_by"],
        "family": i["family"], "tp": i["tp"], "dist": i["dist"], "origin": i["origin"], "use": i["use"], "setting": i["setting"], "fact": i["fact"],
        "x": round(float(xy[n, 0]), 4), "y": round(float(xy[n, 1]), 4), "real": bool(real),
        "nb": [{"id": items[j]["rid"], "sim": round(float(S[n, j]), 2)} for j in nb],
        "rv": {"rubric": r["rubric_score"], "novelty": r["novelty"], "prov": r["provenance_faithful"], "purpose": r.get("context_purpose", ""),
               "viol": r["norm_violation_today"], "suff": r["purpose_sufficiency"], "tc": r["transmission_check"], "agg": r["aggregation"], "adopt": r["adoption"]},
    })
tpl = (root / "scripts/whiteboard_template.html").read_text()
(root / "viz/whiteboard.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(len(data), "stickers;", sum(d["real"] for d in data), "real opportunities")
