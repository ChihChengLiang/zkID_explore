"""Pull the dimension-value lists used to define pilot-2 settings. Outputs to data/taxonomies/.
 - Google Places types (Table A + B)        https://developers.google.com/maps/documentation/places/web-service/place-types
 - OSM Map Features via taginfo (global)     https://taginfo.openstreetmap.org
 - Your Europe citizen topic tree (SDG portal) https://europa.eu/youreurope/citizens/index_en.htm
"""
import re, json, html, time, pathlib, urllib.request, urllib.parse, collections

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "data/taxonomies"; out.mkdir(parents=True, exist_ok=True)
get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 zkid-explore/0.1"}), timeout=60).read().decode("utf-8", "replace")

# --- Google place types
t = get("https://developers.google.com/maps/documentation/places/web-service/place-types")
res = {}
for tab in ("table-a", "table-b"):
    s = t.find(f'id="{tab}"'); e = t.find("<h3", s + 10)
    seg = t[s:e]; cur = None; res[tab] = collections.OrderedDict()
    for m in re.finditer(r'<th\s+id="[^"]*"\s+colspan="\d">([^<]+)</th>|<code[^>]*>([a-z_0-9]+)</code>', seg):
        if m.group(1): cur = html.unescape(m.group(1).strip()); res[tab][cur] = []
        elif cur and m.group(2) != "types": res[tab][cur].append(m.group(2))
(out / "google_place_types.json").write_text(json.dumps(res, indent=1))
print("google:", {k: (len(v), sum(map(len, v.values()))) for k, v in res.items()})

# --- OSM via taginfo
osm = {}
for key in ("amenity", "shop", "office", "leisure", "tourism", "healthcare", "craft", "public_transport", "emergency"):
    q = urllib.parse.urlencode({"key": key, "filter": "all", "lang": "en", "sortname": "count", "sortorder": "desc", "rp": 300, "page": 1})
    d = json.loads(get(f"https://taginfo.openstreetmap.org/api/4/key/values?{q}"))
    osm[key] = [{"value": r["value"], "count": r["count"], "description": r.get("description", "")} for r in d["data"] if r["count"] >= 1000 and r["in_wiki"]]
    time.sleep(0.5)
(out / "osm_features.json").write_text(json.dumps(osm, indent=1))
print("osm (count>=1000 and documented in wiki):", {k: len(v) for k, v in osm.items()})

# --- Your Europe tree
t = get("https://europa.eu/youreurope/citizens/index_en.htm")
tree = collections.OrderedDict(); seen = set()
for href, label in re.findall(r'href="https://europa\.eu/youreurope/citizens/([^"#?]+?)/index_en\.htm"[^>]*>\s*([^<]{2,120}?)\s*<', t):
    if href in seen or href.startswith(("stylesheets", "images")): continue
    seen.add(href); parts = href.split("/"); label = html.unescape(label.strip())
    if len(parts) == 1: tree[parts[0]] = {"label": label, "children": collections.OrderedDict()}
    elif len(parts) >= 2 and parts[0] in tree:
        top = tree[parts[0]]["children"]
        if len(parts) == 2: top[parts[1]] = {"label": label, "children": []}
        elif parts[1] in top: top[parts[1]]["children"].append({"path": href, "label": label})
(out / "youreurope_tree.json").write_text(json.dumps(tree, indent=1, ensure_ascii=False))
print("youreurope: topics", len(tree), "subtopics", sum(len(v["children"]) for v in tree.values()),
      "pages", sum(len(s["children"]) for v in tree.values() for s in v["children"].values()))
