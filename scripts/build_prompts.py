"""Build prompts/<cell>__<arm>.md for arms A (none), B (near), C (distance-banded), D (random diverse).
Needs config/distance.json (cell -> seed -> 0..10)."""
import json, random, glob, yaml, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
cells = yaml.safe_load((root / "config/pilot_cells.yaml").read_text())
seeds = {s["id"]: s for f in sorted(glob.glob(str(root / "seeds/*.yaml"))) for s in yaml.safe_load(open(f))}
dist = json.loads((root / "config/distance.json").read_text())
K = 6
group_of = {}
for g, leaves in yaml.safe_load((root / "config/domains.yaml").read_text()).items():
    for l in leaves: group_of[l] = g
grp = lambda s: group_of.get(s["domain"], s["domain"])
CENTRAL = {"identity-credentials", "government-admin", "finance"}

def pick_near(c):
    return sorted(seeds, key=lambda i: (dist[c][i], i))[:K]

def pick_banded(c, rng):
    d = dist[c]
    ranked = sorted(seeds, key=lambda i: (d[i], i))
    n = len(ranked)
    pool = ranked[n // 10:]                     # drop nearest decile
    mid = [i for i in pool if n * 0.4 <= ranked.index(i) < n * 0.6]
    far = [i for i in pool if ranked.index(i) >= n * 0.7]
    for _ in range(2000):
        chosen = rng.sample(mid, 1) + rng.sample(far, K - 1)
        S = [seeds[i] for i in chosen]
        if (len({s["domain"] for s in S}) == K
                and sum(grp(s) not in CENTRAL for s in S) >= 2
                and any(s.get("mechanism_outcome") in ("fails", "blocked-by-law") for s in S)
                and sum(s["distance_class"] == "distant-analog" for s in S) >= 2):
            return chosen
    raise SystemExit(f"no valid banded draw for {c}")

def pick_random(rng):
    for _ in range(2000):
        chosen = rng.sample(sorted(seeds), K)
        if len({seeds[i]["domain"] for i in chosen}) == K:
            return chosen

def seed_block(ids):
    out = []
    for i in ids:
        s = seeds[i]
        out.append(f"- id: {i}\n  situation: {s['abstract_problem']}\n  original setting: {s['problem']}\n"
                   f"  mechanism: {s['mechanism']} (outcome: {s.get('mechanism_outcome','unknown')})\n"
                   f"  evidence: \"{s['evidence']['quote']}\"")
    return "\n".join(out)

TEMPLATE = open(root / "docs/generator_prompt.md").read()
manifest = {}
for c in cells:
    rng = random.Random(f"{c['id']}")
    picks = {"A": [], "B": pick_near(c["id"]), "C": pick_banded(c["id"], rng), "D": pick_random(random.Random("D" + c["id"]))}
    for arm, ids in picks.items():
        seed_part = ("" if arm == "A" else
                     "\nINSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):\n" + seed_block(ids) + "\n")
        prov = ("Set inspired_by to [] (no material was given)." if arm == "A" else
                "For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.")
        text = (TEMPLATE.replace("{{ISSUER}}", c["issuer"]).replace("{{PREDICATE}}", c["predicate"])
                .replace("{{TARGET}}", c["target"]).replace("{{SEEDS}}", seed_part).replace("{{PROVENANCE}}", prov)
                .replace("{{OUT}}", f"ideas/{c['id']}__{arm}.yaml"))
        (root / "prompts" / f"{c['id']}__{arm}.md").write_text(text)
        manifest[f"{c['id']}__{arm}"] = {"seeds": ids, "domains": [seeds[i]["domain"] for i in ids]}
(root / "prompts/manifest.json").write_text(json.dumps(manifest, indent=1))
print(len(manifest), "prompts")
