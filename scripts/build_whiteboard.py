"""Build viz/whiteboard.html: stickers for all ideas, placed by t-SNE of Qwen3 embeddings
(text = title + moment + verifier + issuer + predicate), with critic scores in the side panel.
Needs numpy+scikit-learn on PYTHONPATH and LM Studio serving the embedding model."""
import json, glob, pathlib, urllib.request, math
import numpy as np
from sklearn.manifold import TSNE

root = pathlib.Path(__file__).resolve().parent.parent
ideas = json.loads((root / "ideas/all.json").read_text())
key = json.loads((root / "critic/key.json").read_text())
rev = {}
for f in glob.glob(str(root / "critic/out_*.json")):
    for r in json.load(open(f)): rev[key[r["review_id"]]] = r

texts = [f"{i['title']}. {i['moment']} Verifier: {i['verifier']}. Issuer: {i['issuer']}. Predicate: {i['predicate']}" for i in ideas]
E = []
for k in range(0, len(texts), 32):
    req = urllib.request.Request("http://localhost:1234/v1/embeddings",
        json.dumps({"model": "text-embedding-qwen3-embedding-0.6b", "input": texts[k:k + 32]}).encode(),
        {"Content-Type": "application/json"})
    E += [d["embedding"] for d in json.load(urllib.request.urlopen(req, timeout=300))["data"]]
E = np.array(E); E /= np.linalg.norm(E, axis=1, keepdims=True)
S = E @ E.T
xy = TSNE(n_components=2, perplexity=12, metric="cosine", init="pca", random_state=3).fit_transform(E)
xy -= xy.min(0); xy /= xy.max(0)

data = []
for n, i in enumerate(ideas):
    r = rev[i["id"]]
    nb = [j for j in np.argsort(-S[n]) if j != n][:3]
    data.append({
        "id": i["id"], "cell": i["cell"], "arm": i["arm"], "title": i["title"], "moment": i["moment"],
        "verifier": i["verifier"], "predicate": i["predicate"], "issuer": i["issuer"],
        "disclosed": i["disclosed_today"], "why": i["why_zk"], "borrowed": i["inspired_by"],
        "x": round(float(xy[n, 0]), 4), "y": round(float(xy[n, 1]), 4),
        "nb": [{"id": ideas[j]["id"], "sim": round(float(S[n, j]), 2)} for j in nb],
        "rev": {k: r[k] for k in ("rubric_score", "validity", "coherence", "novelty", "provenance_faithful", "kill_tests", "reasons")},
    })
tpl = (root / "scripts/whiteboard_template.html").read_text()
(root / "viz/whiteboard.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(len(data), "stickers")
