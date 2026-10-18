"""Coverage report for config/pilot2_cells.yaml against config/axes.yaml."""
import yaml, collections, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
cells = yaml.safe_load(open(root / "config/pilot2_cells.yaml")); ax = yaml.safe_load(open(root / "config/axes.yaml"))
adj = {frozenset(p) for p in [("healthcare","government_admin"),("employment","finance"),("education","government_admin"),("housing","government_admin"),("family_social","government_admin"),("family_social","healthcare"),("family_social","education"),("finance","government_admin"),("housing","civic_community"),("civic_community","government_admin"),("justice_security","government_admin"),("employment","civic_community"),("education","employment"),("education","civic_community"),("government_admin","commerce"),("justice_security","civic_community"),("housing","employment"),("civic_community","religion"),("family_social","civic_community")]}
def dist(c): return "same" if c["origin"] == c["use"] else ("adjacent" if frozenset((c["origin"], c["use"])) in adj else "different")
def show(name, vals, universe):
    n = collections.Counter(vals); miss = [u for u in universe if n[u] == 0]
    print(f"{name:22}", dict(n.most_common()), "| MISSING:", miss or "none")
print(len(cells), "cells; ids unique:", len({c["id"] for c in cells}) == len(cells))
show("attribute_family", [c["family"] for c in cells], ax["attribute_family"])
show("predicate", [c["predicate"] for c in cells], ax["predicate"])
show("transmission_principle", [c["tp"] for c in cells], list(ax["transmission_principle"]))
show("use context", [c["use"] for c in cells], ax["context"])
show("origin context", [c["origin"] for c in cells], ax["context"])
show("context distance", [dist(c) for c in cells], ["same", "adjacent", "different"])
print("cells needing a Taiwan-law check:", sum(c["check"] for c in cells), "of", len(cells))
bad = [c["id"] for c in cells if c["family"] not in ax["attribute_family"] or c["predicate"] not in ax["predicate"] or c["tp"] not in ax["transmission_principle"] or c["use"] not in ax["context"] or c["origin"] not in ax["context"]]
print("invalid labels:", bad or "none")
