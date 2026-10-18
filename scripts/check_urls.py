"""HEAD/GET every seed url and print status. Pass --write to record `verified` back into the YAML."""
import sys, pathlib, datetime, urllib.request, yaml

root = pathlib.Path(__file__).resolve().parent.parent
write = "--write" in sys.argv
for f in sorted((root / "sources").glob("*.yaml")):
    seeds = yaml.safe_load(f.read_text())
    for s in seeds:
        req = urllib.request.Request(s["url"], headers={"User-Agent": "zkid-explore/0.1"})
        try:
            code = urllib.request.urlopen(req, timeout=15).status
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:
            code = 0
        print(f"{code:>3} {s['id']}  {s['url']}")
        s["verified"] = {"url_checked_on": datetime.date.today().isoformat(), "http_status": code}
    if write:
        f.write_text(yaml.safe_dump(seeds, sort_keys=False, allow_unicode=True, width=100))
