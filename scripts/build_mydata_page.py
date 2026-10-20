"""Build docs/mydata.html from data/mydata/*.csv and methodology.txt (replaces the old workbook)."""
import csv, html, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = root / "data/mydata"
e = lambda s: html.escape(s, quote=True)
def table(name):
    with open(d / f"{name}.csv", newline="", encoding="utf-8") as f: r = list(csv.reader(f))
    return r[0], r[1:]
# methodology
lines = [l.rstrip() for l in (d / "methodology.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
title, rest = lines[0], lines[1:]
HEADS = {"Purpose", "How each row was built", "How to reuse this method outside MyData"}
out, mode = [], None
def close():
    global mode
    if mode: out.append(f"</{mode}>"); mode = None
for l in rest:
    if l in HEADS: close(); out.append(f"<h3>{e(l)}</h3>"); continue
    m = re.match(r"^(\d+)\.\s+(.*)", l)
    if m:
        if mode != "ol": close(); out.append("<ol>"); mode = "ol"
        out.append(f"<li>{e(m.group(2))}</li>"); continue
    if l.startswith("- "):
        if mode != "ul": close(); out.append("<ul>"); mode = "ul"
        out.append(f"<li>{e(l[2:])}</li>"); continue
    close(); out.append(f"<p>{e(l)}</p>")
close(); method_html = "\n".join(out)
rh, rr = table("scoring_rubric"); ch, cr = table("data_catalog"); uh, ur = table("use_case_matrix"); dh, dr = table("discovery_matrix")
note = (d / "discovery_matrix_note.txt").read_text(encoding="utf-8").splitlines()
def tbl(h, rows, cls="", score_col=None):
    t = [f'<div class="wrap"><table class="{cls}"><thead><tr>' + "".join(f"<th>{e(x)}</th>" for x in h) + "</tr></thead><tbody>"]
    for r in rows:
        t.append("<tr>" + "".join((f'<td data-s="{e(c)}"><span class="s s{e(c)}">{e(c)}</span></td>' if i == score_col else f"<td>{e(c)}</td>") for i, c in enumerate(r)) + "</tr>")
    t.append("</tbody></table></div>"); return "".join(t)
scores = [int(r[8]) for r in ur if r[8].isdigit()]
themes = sorted({r[0] for r in ur})
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Taiwan MyData use-case worksheet</title>
<style>
:root{{--bg:#fbfbf8;--fg:#14213d;--dim:#4a5568;--panel:#f1f0ea;--line:#d9d6c8;--teal:#0f766e;--amber:#b45309}}
@media(prefers-color-scheme:dark){{:root{{--bg:#14161c;--fg:#e8e6df;--dim:#a8adb8;--panel:#1d2029;--line:#343846;--teal:#5eead4;--amber:#fbbf24}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:28px 18px 80px}}h1{{font-size:28px;margin:0 0 4px}}h2{{font-size:22px;margin:44px 0 6px;border-top:1px solid var(--line);padding-top:24px}}h3{{font-size:16px;margin:22px 0 4px;color:var(--teal)}}
p,li{{max-width:78ch}}.dim{{color:var(--dim)}}nav a{{margin-right:14px}}a{{color:var(--teal)}}
.wrap{{overflow-x:auto;border:1px solid var(--line);border-radius:10px;margin:12px 0}}table{{border-collapse:collapse;width:100%;font-size:14px}}
th,td{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}th{{background:var(--panel);position:sticky;top:0;white-space:nowrap}}
table.use td:nth-child(2){{min-width:260px}}table.use td:nth-child(4),table.use td:nth-child(5),table.use td:nth-child(8),table.use td:nth-child(10){{min-width:240px}}
.s{{display:inline-block;min-width:26px;text-align:center;border-radius:12px;padding:0 8px;font-weight:600;color:#14213d}}.s5{{background:#6ee7b7}}.s4{{background:#bbf7d0}}.s3{{background:#fde68a}}.s2{{background:#fed7aa}}.s1{{background:#fecaca}}
.ctl{{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:10px 0}}select{{font:inherit;padding:4px 8px;border-radius:6px;border:1px solid var(--line);background:var(--bg);color:var(--fg)}}
.dl a{{margin-right:12px}}table.disc td:first-child{{font-weight:600;white-space:nowrap}}
</style></head><body><main>
<h1>Taiwan MyData use-case worksheet</h1>
<p class="dim">Where could zero-knowledge or selective-disclosure proofs replace a document hand-off? The first, hand-built pass of this project, based on Taiwan’s MyData service. Replaces the original spreadsheet; the later AI-assisted exploration is in the <a href="index.html">main project</a>.</p>
<nav><a href="#method">Methodology</a><a href="#rubric">Rubric</a><a href="#catalog">Data catalog</a><a href="#usecases">Use cases</a><a href="#discovery">Discovery matrix</a></nav>
<p class="dl dim">Download the data: <a href="https://github.com/ChihChengLiang/zkID_explore/tree/main/data/mydata">CSV files on GitHub</a></p>
<h2 id="method">{e(title)}</h2>
{method_html}
<h2 id="rubric">Scoring rubric</h2>
{tbl(rh, rr)}
<h2 id="catalog">MyData data catalog</h2>
<p class="dim">The 12 official document categories and who issues them.</p>
{tbl(ch, cr)}
<h2 id="usecases">Use-case matrix</h2>
<p class="dim">{len(ur)} illustrative moments, hand-scored 1–5 against the rubric (average {sum(scores)/len(scores):.2f}; {sum(s == 5 for s in scores)} rated 5). Illustrative, not scraped from real forms.</p>
<div class="ctl"><label>Theme <select id="theme"><option value="">all</option>{"".join(f'<option>{e(t)}</option>' for t in themes)}</select></label><label>Minimum score <select id="min"><option value="0">any</option><option>5</option><option>4</option><option>3</option></select></label><span class="dim" id="count"></span></div>
{tbl(uh, ur, "use", 8)}
<h2 id="discovery">Discovery matrix</h2>
<p class="dim">{e(note[0])}</p><p class="dim">{e(note[1])}</p>
{tbl(dh, dr, "disc")}
</main>
<script>
const rows=[...document.querySelectorAll("table.use tbody tr")];
function f(){{const t=document.querySelector("#theme").value,m=+document.querySelector("#min").value;let n=0;rows.forEach(r=>{{const ok=(!t||r.cells[0].textContent===t)&&(+r.cells[8].dataset.s>=m);r.style.display=ok?"":"none";n+=ok}});document.querySelector("#count").textContent=n+" of "+rows.length+" shown"}}
document.querySelector("#theme").onchange=f;document.querySelector("#min").onchange=f;f();
</script></body></html>"""
(root / "docs/mydata.html").write_text(page, encoding="utf-8")
print("wrote docs/mydata.html;", len(ur), "use cases; avg", round(sum(scores) / len(scores), 2))
