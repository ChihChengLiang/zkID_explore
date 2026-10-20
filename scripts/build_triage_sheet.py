"""Build labeling/triage.html: a correction sheet for the 37 triaged ideas (channel fields)."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
ins = {r["id"]: r for r in json.load(open(root / "triage/in.json"))}
S = {r["id"]: r for r in json.load(open(root / "triage/out_sonnet.json"))}; H = {r["id"]: r for r in json.load(open(root / "triage/out_haiku.json"))}
FIELDS = ["interaction_mode", "current_evidence", "verifier_reader"]
rows = []
for i, r in ins.items():
    dis = [f for f in FIELDS if S[i][f] != H[i][f]]
    rows.append({"id": i, "title": r["title"], "moment": r["moment"], "verifier": r["verifier"], "issuer": r["issuer"], "disclosed": r["disclosed_today"], "predicate": r["predicate"],
                 "model": {f: S[i][f] for f in FIELDS}, "other": {f: H[i][f] for f in FIELDS}, "disagree": dis, "rationale": S[i]["rationale"]})
tpl = (root / "scripts/triage_sheet_template.html").read_text()
(root / "labeling/triage.html").write_text(tpl.replace("__DATA__", json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")))
print(len(rows), "ideas;", sum(bool(r["disagree"]) for r in rows), "with a model disagreement")
