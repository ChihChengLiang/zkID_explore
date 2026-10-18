"""After labeling: accuracy of 'same iff cos >= T' against labeling/labels.csv, per T. Skips 'unsure'."""
import csv, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
key = {k["pair"]: k["cos"] for k in json.load(open(root / "labeling/key.json"))}
lab = {int(r["pair"]): r["label"].strip().lower() for r in csv.DictReader(open(root / "labeling/labels.csv")) if r["label"].strip().lower() in ("same", "different")}
print(len(lab), "labelled,", sum(v == "same" for v in lab.values()), "same")
best = []
for T in [x / 100 for x in range(50, 96, 1)]:
    acc = sum((key[p] >= T) == (v == "same") for p, v in lab.items()) / len(lab)
    best.append((acc, T))
top = max(a for a, _ in best)
Ts = [t for a, t in best if a == top]
print(f"best accuracy {top:.2f} for T in [{min(Ts):.2f}, {max(Ts):.2f}]  -> use ~{sum(Ts)/len(Ts):.2f}")
