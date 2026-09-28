"""N2 token dashboard: one self-contained static HTML (no server, no external libraries).

Design follows the ABM dataviz method: KPI row first, magnitude as single-hue bars
(4px rounded data-end, square at the baseline, 2px gap), trend as a 2px line with a
crosshair, budgets as status label + icon (never color alone), and a table view.
"""
from __future__ import annotations

import html
import json
from collections import defaultdict

from .common import emit, now_iso, write_text
from . import tokens as T

PAGE = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tokens · __NAME__</title>
<style>
.viz-root{color-scheme:light;--surface-0:#f5f4f1;--surface-1:#fcfcfb;--text-primary:#0b0b0b;--text-secondary:#52514e;--text-muted:#7a7974;--grid:#e4e3df;--series-1:#2a78d6;--series-1-hover:#1c5cab;--good:#0ca30c;--warning:#fab219;--critical:#d03b3b;}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])) .viz-root{color-scheme:dark;--surface-0:#111110;--surface-1:#1a1a19;--text-primary:#ffffff;--text-secondary:#c3c2b7;--text-muted:#8f8e86;--grid:#2c2c2a;--series-1:#3987e5;--series-1-hover:#6da7ec;}}
:root[data-theme="dark"] .viz-root{color-scheme:dark;--surface-0:#111110;--surface-1:#1a1a19;--text-primary:#ffffff;--text-secondary:#c3c2b7;--text-muted:#8f8e86;--grid:#2c2c2a;--series-1:#3987e5;--series-1-hover:#6da7ec;}
*{box-sizing:border-box}body{margin:0}
.viz-root{background:var(--surface-0);color:var(--text-primary);font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;min-height:100vh;padding:16px}
main{max-width:1100px;margin:0 auto}
h1{font-size:20px;margin:0 0 4px}h2{font-size:15px;margin:0 0 12px}
.sub{color:var(--text-secondary);margin:0 0 16px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:12px;margin-bottom:16px}
.card{background:var(--surface-1);border-radius:10px;padding:16px;min-width:0;overflow-x:auto}
.kpi{min-width:0}.kpi .v{font-size:clamp(22px,2.6vw,32px);font-weight:650;letter-spacing:-.01em;overflow-wrap:anywhere;line-height:1.15}.kpi .l{color:var(--text-secondary)}
.hero{grid-column:span 2}.hero .v{font-size:clamp(34px,5vw,48px)}
.kpi .v .st{font-size:18px;font-weight:600}
@media (max-width:640px){.hero{grid-column:auto}}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:12px;margin-bottom:12px}
svg{display:block;width:100%;height:auto;overflow:visible}
.axis{fill:var(--text-muted);font-size:12px}.lbl{fill:var(--text-secondary);font-size:12px}.val{fill:var(--text-primary);font-size:12px}
.bar{fill:var(--series-1);cursor:default}.bar:hover,.bar:focus{fill:var(--series-1-hover);outline:none}
.gl{stroke:var(--grid);stroke-width:1}
.line{fill:none;stroke:var(--series-1);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.area{fill:var(--series-1);opacity:.1}.dot{fill:var(--series-1);stroke:var(--surface-1);stroke-width:2}
.xh{stroke:var(--text-muted);stroke-width:1;stroke-dasharray:3 3}
#tip{position:fixed;pointer-events:none;background:var(--surface-1);color:var(--text-primary);border-radius:8px;padding:8px 10px;box-shadow:0 4px 16px rgba(0,0,0,.18);font-size:12px;display:none;z-index:9}
#tip b{font-size:14px;display:block}#tip span{color:var(--text-secondary)}
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--grid)}th{color:var(--text-secondary);font-weight:600}td.n{text-align:right}
.st{display:inline-flex;gap:6px;align-items:center;font-weight:600}.st i{font-style:normal;display:inline-block;width:10px;height:10px;border-radius:50%}
.st.ok i{background:var(--good)}.st.soft i{background:var(--warning)}.st.hard i{background:var(--critical)}
details summary{cursor:pointer;color:var(--text-secondary)}
.empty{color:var(--text-secondary);padding:24px 0}
</style>
</head>
<body class="viz-root">
<main>
<h1>Espacio de tokens · __NAME__</h1>
<p class="sub">Generado __NOW__ desde el ledger. Construcción + operación. Los eventos "estimado" usan caracteres/4.</p>
<section class="kpis" id="kpis"></section>
<section class="grid2"><div class="card"><h2>Tokens por unidad (FU/DU/WU)</h2><div id="byUnit"></div></div><div class="card"><h2>Tokens por modelo</h2><div id="byModel"></div></div></section>
<section class="card" style="margin-bottom:12px"><h2>Tokens por día</h2><div id="byDay"></div></section>
<section class="card" style="margin-bottom:12px"><h2>Presupuestos</h2><div id="budgets"></div></section>
<section class="card"><details><summary>Vista de tabla (todos los agregados)</summary><div id="table"></div></details></section>
</main>
<div id="tip" role="status" aria-live="polite"></div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
const D=JSON.parse(document.getElementById('data').textContent);
const fmt=n=>n==null?'n/d':Number(n).toLocaleString('es');
const tip=document.getElementById('tip');
function showTip(e,val,label){tip.replaceChildren();const b=document.createElement('b');b.textContent=val;const s=document.createElement('span');s.textContent=label;tip.append(b,s);tip.style.display='block';const x=(e.clientX||e.target.getBoundingClientRect().right)+12,y=(e.clientY||e.target.getBoundingClientRect().top)+12;tip.style.left=Math.min(x,innerWidth-200)+'px';tip.style.top=y+'px';}
function hideTip(){tip.style.display='none';}
const NS='http://www.w3.org/2000/svg';
function el(n,a,p){const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e;}
function kpi(label,value,hero){const c=document.createElement('div');c.className='card kpi'+(hero?' hero':'');const v=document.createElement('div');v.className='v';v.textContent=value;const l=document.createElement('div');l.className='l';l.textContent=label;c.append(v,l);return c;}
const K=document.getElementById('kpis');
K.append(kpi('tokens totales',fmt(D.total),true),kpi(D.cost_lower_bound?'costo USD (cota inferior, según pricing.yaml)':'costo USD (según pricing.yaml)',(D.cost_known&&!D.cost_lower_bound)?('$'+D.cost.toFixed(2)):(D.cost?('≥ $'+D.cost.toFixed(2)):'n/d')),kpi('eventos estimados',D.estimated+' de '+D.events));
const worst=D.budgets.reduce((w,b)=>({ok:0,soft:1,hard:2}[b.state]>{ok:0,soft:1,hard:2}[w]?b.state:w),'ok');
const bc=kpi('presupuestos','');const lab={ok:'✔ dentro',soft:'⚠ umbral blando',hard:'✖ tope duro superado'};const st=document.createElement('span');st.className='st '+worst;const dot=document.createElement('i');st.append(dot,document.createTextNode(lab[worst]));bc.querySelector('.v').replaceChildren(st);K.append(bc);
function hbar(id,rows){const host=document.getElementById(id);if(!rows.length){host.innerHTML='<p class="empty">Sin datos todavía.</p>';return;}
 const W=520,rowH=28,bar=18,labW=150,valW=70,H=rows.length*rowH+8,max=Math.max(...rows.map(r=>r.v))||1;
 const s=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'barras horizontales'},host);
 const x0=labW,span=W-labW-valW;
 rows.forEach((r,i)=>{const y=i*rowH+4,w=Math.max(2,r.v/max*span),rr=Math.min(4,w);
  const t=el('text',{x:labW-8,y:y+bar/2+4,'text-anchor':'end',class:'lbl'},s);t.textContent=r.k.length>22?r.k.slice(0,21)+'…':r.k;
  const p=el('path',{class:'bar',tabindex:0,d:`M${x0},${y}h${w-rr}a${rr},${rr} 0 0 1 ${rr},${rr}v${bar-2*rr}a${rr},${rr} 0 0 1 -${rr},${rr}h-${w-rr}z`},s);
  const v=el('text',{x:x0+w+6,y:y+bar/2+4,class:'val'},s);v.textContent=fmt(r.v);
  const h=el('rect',{x:0,y:y-4,width:W,height:rowH,fill:'transparent'},s);
  [p,h].forEach(n=>{n.addEventListener('pointermove',e=>showTip(e,fmt(r.v)+' tokens',r.k));n.addEventListener('pointerleave',hideTip);});
  p.addEventListener('focus',e=>showTip(e,fmt(r.v)+' tokens',r.k));p.addEventListener('blur',hideTip);});}
hbar('byUnit',D.by_unit);hbar('byModel',D.by_model);
(function(){const host=document.getElementById('byDay'),rows=D.by_day;if(rows.length<2){host.innerHTML='<p class="empty">Se necesita más de un día de datos para la tendencia.</p>';return;}
 const W=1000,H=220,L=60,R=16,T=12,B=28,max=Math.max(...rows.map(r=>r.v))||1,n=rows.length;
 const X=i=>L+i*(W-L-R)/(n-1),Y=v=>T+(H-T-B)*(1-v/max);
 const s=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'tokens por día'},host);
 [0,.5,1].forEach(f=>{el('line',{x1:L,x2:W-R,y1:Y(max*f),y2:Y(max*f),class:'gl'},s);const t=el('text',{x:L-8,y:Y(max*f)+4,'text-anchor':'end',class:'axis'},s);t.textContent=fmt(Math.round(max*f));});
 const pts=rows.map((r,i)=>[X(i),Y(r.v)]);
 el('path',{class:'area',d:`M${pts[0][0]},${Y(0)}L${pts.map(p=>p.join(',')).join('L')}L${pts[n-1][0]},${Y(0)}Z`},s);
 el('path',{class:'line',d:'M'+pts.map(p=>p.join(',')).join('L')},s);
 [0,n-1].forEach(i=>{const t=el('text',{x:X(i),y:H-8,'text-anchor':i?'end':'start',class:'axis'},s);t.textContent=rows[i].k;});
 const xh=el('line',{class:'xh',y1:T,y2:H-B,x1:-10,x2:-10},s),dot=el('circle',{class:'dot',r:4,cx:-10,cy:-10},s);
 const hit=el('rect',{x:L,y:T,width:W-L-R,height:H-T-B,fill:'transparent'},s);
 hit.addEventListener('pointermove',e=>{const b=s.getBoundingClientRect(),px=(e.clientX-b.left)*W/b.width;const i=Math.max(0,Math.min(n-1,Math.round((px-L)/((W-L-R)/(n-1)))));xh.setAttribute('x1',X(i));xh.setAttribute('x2',X(i));dot.setAttribute('cx',X(i));dot.setAttribute('cy',Y(rows[i].v));showTip(e,fmt(rows[i].v)+' tokens',rows[i].k);});
 hit.addEventListener('pointerleave',()=>{hideTip();xh.setAttribute('x1',-10);xh.setAttribute('x2',-10);dot.setAttribute('cx',-10);});})();
function table(host,head,rows){const t=document.createElement('table');const tr=document.createElement('tr');head.forEach(h=>{const th=document.createElement('th');th.textContent=h;tr.append(th);});t.append(tr);rows.forEach(r=>{const tr=document.createElement('tr');r.forEach((c,i)=>{const td=document.createElement('td');if(c instanceof Node)td.append(c);else td.textContent=c;if(i&&typeof c!=='object')td.className='n';tr.append(td);});t.append(tr);});host.append(t);}
const B=document.getElementById('budgets');if(!D.budgets.length){B.innerHTML='<p class="empty">Sin presupuestos declarados en ads.yaml → tokens.budgets.</p>';}else{table(B,['Alcance','Usado','Blando','Duro','Estado'],D.budgets.map(b=>{const s=document.createElement('span');s.className='st '+b.state;const i=document.createElement('i');s.append(i,document.createTextNode(lab[b.state]));return[b.scope,fmt(b.used),fmt(b.soft),fmt(b.hard),s];}));}
table(document.getElementById('table'),['Dimensión','Clave','Entrada','Salida','Costo USD'],D.rows.map(r=>[r.dim,r.k,fmt(r.in),fmt(r.out),r.cost==null?'n/d':r.cost.toFixed(4)]));
})();
</script>
</body>
</html>
"""


def build(ctx):
    events = [e for e in T.read_ledger(ctx) if "_invalid_line" not in e]
    pricing = T.load_pricing(ctx)
    name = (T._manifest(ctx).get("name")) or ctx.root.name

    def rows(by):
        agg = T.aggregate(events, pricing, by)
        return sorted(({"k": k, "v": a["input_tokens"] + a["output_tokens"]} for k, a in agg.items()), key=lambda r: -r["v"])[:12]

    day = defaultdict(int)
    for e in events:
        day[str(e.get("ts", ""))[:10]] += int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0))
    table = []
    for dim in ("phase", "unit", "model", "feature"):
        for k, a in T.aggregate(events, pricing, dim).items():
            table.append({"dim": dim, "k": k, "in": a["input_tokens"], "out": a["output_tokens"], "cost": round(a["cost_usd"], 6) if a["cost_known"] else None})
    costs = [T.cost(e, pricing) for e in events]
    data = {"total": sum(int(e.get("input_tokens", 0)) + int(e.get("output_tokens", 0)) for e in events),
            "events": len(events), "estimated": sum(1 for e in events if e.get("source") == "estimate"),
            "cost": round(sum(c for c in costs if c is not None), 6), "cost_known": bool(costs) and all(c is not None for c in costs),
            "cost_lower_bound": any(e.get("cost_lower_bound") for e in events),
            "by_unit": rows("unit"), "by_model": rows("model"),
            "by_day": [{"k": k, "v": v} for k, v in sorted(day.items())], "budgets": T.budgets_status(ctx, events), "rows": table}
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return PAGE.replace("__DATA__", blob).replace("__NAME__", html.escape(str(name))).replace("__NOW__", now_iso())


def cmd_dashboard(ctx, args):
    tok = T._manifest(ctx).get("tokens") or {}
    target = ctx.root / (args.out or tok.get("dashboard") or "ops/tokens/dashboard.html")
    state = write_text(ctx, target, build(ctx))
    return emit(ctx, {"dashboard": str(target.relative_to(ctx.root)), "state": state}, [f"Dashboard N2 {state}: {target.relative_to(ctx.root)}"])


def register(sub):
    d = sub.add_parser("dashboard", help="Genera el dashboard N2 (HTML estático)")
    d.add_argument("--out")
    d.set_defaults(func=cmd_dashboard)
