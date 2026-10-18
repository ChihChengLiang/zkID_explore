"""Fetch a URL, strip to plain text, save to snapshots/<id>.txt.  usage: fetch_snapshot.py <id> <url>"""
import sys, re, html, pathlib, urllib.request

sid, url = sys.argv[1], sys.argv[2]
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 zkid-explore/0.1"})
raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))
text = re.sub(r"\s+", " ", text).strip()
out = pathlib.Path(__file__).resolve().parent.parent / "snapshots" / f"{sid}.txt"
out.write_text(text)
print(f"{out} {len(text)} chars")
