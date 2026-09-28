// Panel de ventas — dashboard en el cliente: datos por fetch, gráficos SVG propios, sin librerías.
// Todo texto que viene de datos se inserta con textContent (nunca innerHTML).
"use strict";
(function () {
  const $ = (s) => document.querySelector(s);
  const meta = (n) => (document.querySelector(`meta[name="${n}"]`) || {}).content || "";
  const CSRF = meta("csrf-token"), ROL = meta("rol"), MONEDA = meta("moneda") || "USD";
  const SVG = "http://www.w3.org/2000/svg";
  const money = new Intl.NumberFormat("es", { style: "currency", currency: MONEDA, maximumFractionDigits: 0 });
  const money2 = new Intl.NumberFormat("es", { style: "currency", currency: MONEDA });
  const compact = new Intl.NumberFormat("es", { notation: "compact", maximumFractionDigits: 1 });
  const monthFmt = new Intl.DateTimeFormat("es", { month: "short", year: "2-digit", timeZone: "UTC" });
  const monthLong = new Intl.DateTimeFormat("es", { month: "long", year: "numeric", timeZone: "UTC" });
  const iso = (d) => d.toISOString().slice(0, 10);
  const today = () => iso(new Date(Date.now() - new Date().getTimezoneOffset() * 60000)); // fecha local
  const mesLabel = (m, f) => (f || monthFmt).format(new Date(m + "-01T00:00:00Z"));
  const state = { desde: "", hasta: "", preset: "12m", last: null };

  // ---------------------------------------------------------------- red
  async function api(path, opts) {
    const res = await fetch(path, Object.assign({ credentials: "same-origin", headers: { Accept: "application/json" } }, opts));
    if (res.status === 401) { window.location.assign("/login"); throw new Error("Sesión expirada"); }
    if (res.status === 204) return null;
    const body = await res.json().catch(() => ({}));
    if (!res.ok) { const e = new Error(body.detail || body.title || `Error ${res.status}`); e.problem = body; throw e; }
    return body;
  }

  // ---------------------------------------------------------------- rango
  function presetRange(p) {
    const h = today(), hoy = new Date(h + "T00:00:00Z");
    if (p === "ytd") return [`${hoy.getUTCFullYear()}-01-01`, h];
    if (p === "90d") return [iso(new Date(hoy.getTime() - 89 * 864e5)), h];
    if (p === "12m") return [iso(new Date(Date.UTC(hoy.getUTCFullYear(), hoy.getUTCMonth() - 11, 1))), h];
    return ["", ""];
  }
  function setPreset(p) {
    state.preset = p;
    [state.desde, state.hasta] = presetRange(p);
    $("#desde").value = state.desde; $("#hasta").value = state.hasta;
    document.querySelectorAll("[data-preset]").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.preset === p)));
  }
  const qs = () => new URLSearchParams(Object.entries({ desde: state.desde, hasta: state.hasta }).filter(([, v]) => v)).toString();

  // ---------------------------------------------------------------- estados
  function setStatus(text, kind, retry) {
    const box = $("#status");
    box.textContent = text || "";
    box.className = "status" + (kind ? " " + kind : "");
    box.setAttribute("role", kind === "error" ? "alert" : "status");
    if (retry) {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = "Reintentar"; b.addEventListener("click", () => load());
      box.append(" ", b);
    }
  }
  function message(container, text, cls) {
    container.replaceChildren();
    const p = document.createElement("p");
    p.className = cls; p.textContent = text;
    container.append(p);
  }

  async function load(okMsg) {
    const content = $("#content");
    content.classList.add("is-loading");
    content.setAttribute("aria-busy", "true");
    setStatus("Cargando datos…");
    try {
      const q = qs();
      const [res, ventas] = await Promise.all([api(`/api/resumen?${q}`), api(`/api/ventas?${q}&limit=25`)]);
      state.last = [res, ventas];
      render(res, ventas);
      if (!res.n_ventas) setStatus("Sin ventas en el rango seleccionado. Registra la primera venta abajo.");
      else setStatus(typeof okMsg === "string" ? okMsg : "", typeof okMsg === "string" ? "ok" : "");
    } catch (e) {
      setStatus(`No se pudieron cargar los datos: ${e.message}`, "error", true);
      ["#chart-mes", "#chart-vendedor"].forEach((s) => message($(s), "Error al cargar el gráfico.", "error"));
    } finally {
      content.classList.remove("is-loading");
      content.removeAttribute("aria-busy");
    }
  }

  // ---------------------------------------------------------------- render
  function render(res, ventas) {
    const n = res.n_ventas;
    $("#kpi-total").textContent = n ? money.format(res.total_centavos / 100) : "—";
    $("#kpi-n").textContent = n ? String(n) : "—";
    $("#kpi-ticket").textContent = n ? money.format(res.ticket_promedio_centavos / 100) : "—";
    const best = res.por_mes.reduce((a, b) => (b.total_centavos > (a ? a.total_centavos : -1) ? b : a), null);
    $("#kpi-mejor").textContent = n && best ? mesLabel(best.mes, monthLong) : "—";
    const meses = res.por_mes.map((m) => ({ label: mesLabel(m.mes), long: mesLabel(m.mes, monthLong), value: m.total_centavos / 100, n: m.n }));
    const vend = res.por_vendedor.map((v) => ({ label: v.vendedor, long: v.vendedor, value: v.total_centavos / 100, n: v.n }));
    drawChart("#chart-mes", meses, columns);
    drawChart("#chart-vendedor", vend, hbars);
    renderTable(ventas);
  }
  function drawChart(sel, data, fn) {
    const box = $(sel);
    if (!data.length) return message(box, "Sin datos en este rango.", "empty");
    box.replaceChildren(fn(data, Math.max(300, box.clientWidth || 640)));
  }
  // Escala con ticks redondos: paso 1/2/2,5/5 × 10^k y tope = múltiplo del paso.
  function niceScale(v) {
    if (v <= 0) return { max: 1, step: 1, n: 1 };
    const raw = v / 5, p = Math.pow(10, Math.floor(Math.log10(raw))), f = raw / p;
    const step = (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * p, n = Math.ceil(v / step);
    return { max: step * n, step, n };
  }
  function el(tag, attrs, text) {
    const e = document.createElementNS(SVG, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    return e;
  }
  function svgRoot(w, h, label) {
    return el("svg", { viewBox: `0 0 ${w} ${h}`, width: w, height: h, role: "group", "aria-label": label });
  }
  // Barra con extremo de datos redondeado (4px) y base recta, según orientación.
  function barPath(x, y, w, h, vertical) {
    const r = Math.min(4, vertical ? w / 2 : h / 2, vertical ? h : w);
    if (vertical) return `M${x},${y + h}V${y + r}Q${x},${y} ${x + r},${y}H${x + w - r}Q${x + w},${y} ${x + w},${y + r}V${y + h}Z`;
    return `M${x},${y}H${x + w - r}Q${x + w},${y} ${x + w},${y + r}V${y + h - r}Q${x + w},${y + h} ${x + w - r},${y + h}H${x}Z`;
  }
  function bar(d, hit, path) {
    const g = el("g", { class: "bar", tabindex: "0", role: "img",
      "aria-label": `${d.long}: ${money.format(d.value)}, ${d.n} ventas` });
    g.append(el("rect", Object.assign({ class: "hit" }, hit)), el("path", { class: "mark", d: path }));
    const show = (ev) => tooltip(d, ev, g), hide = () => ($("#tooltip").hidden = true);
    g.addEventListener("pointermove", show); g.addEventListener("pointerleave", hide);
    g.addEventListener("focus", show); g.addEventListener("blur", hide);
    return g;
  }
  function columns(data, W) {
    const H = 260, m = { t: 20, r: 8, b: 28, l: 56 }, iw = W - m.l - m.r, ih = H - m.t - m.b;
    const sc = niceScale(Math.max(...data.map((d) => d.value))), max = sc.max, band = iw / data.length;
    const bw = Math.min(24, band * 0.7), s = svgRoot(W, H, "Gráfico de columnas: ventas por mes");
    for (let i = 0; i <= sc.n; i++) {
      const y = m.t + ih - (ih * i) / sc.n;
      s.append(el("line", { class: i ? "gridline" : "baseline", x1: m.l, x2: W - m.r, y1: y, y2: y }),
        el("text", { class: "tick", x: m.l - 8, y: y + 4, "text-anchor": "end" }, compact.format(sc.step * i)));
    }
    const step = Math.ceil(data.length / Math.max(1, Math.floor(iw / 52)));
    const top = data.reduce((a, b) => (b.value > a.value ? b : a), data[0]);
    data.forEach((d, i) => {
      const cx = m.l + band * i + band / 2, h = (ih * d.value) / max, y = m.t + ih - h;
      s.append(bar(d, { x: m.l + band * i, y: m.t, width: band, height: ih }, barPath(cx - bw / 2, y, bw, h, true)));
      if (i % step === 0) s.append(el("text", { class: "tick", x: cx, y: H - 8, "text-anchor": "middle" }, d.label));
      if (d === top && d.value > 0) s.append(el("text", { class: "label", x: cx, y: y - 6, "text-anchor": "middle" }, compact.format(d.value)));
    });
    return s;
  }
  function hbars(data, W) {
    const row = 36, m = { t: 8, r: 64, b: 8, l: Math.min(140, W * 0.35) }, H = m.t + m.b + row * data.length;
    const iw = W - m.l - m.r, max = niceScale(Math.max(...data.map((d) => d.value))).max;
    const s = svgRoot(W, H, "Gráfico de barras: ventas por vendedor");
    s.append(el("line", { class: "baseline", x1: m.l, x2: m.l, y1: m.t, y2: H - m.b }));
    data.forEach((d, i) => {
      const y = m.t + row * i, w = (iw * d.value) / max, bh = Math.min(24, row - 12), by = y + (row - bh) / 2;
      s.append(bar(d, { x: 0, y, width: W, height: row }, barPath(m.l, by, w, bh, false)),
        el("text", { class: "tick", x: m.l - 8, y: by + bh / 2 + 4, "text-anchor": "end" }, d.label),
        el("text", { class: "label", x: m.l + w + 6, y: by + bh / 2 + 4 }, compact.format(d.value)));
    });
    return s;
  }
  function tooltip(d, ev, g) {
    const t = $("#tooltip"), strong = document.createElement("strong"), span = document.createElement("span");
    strong.textContent = money.format(d.value);
    span.textContent = `${d.long} · ${d.n} ventas`;
    t.replaceChildren(strong, span);
    t.hidden = false;
    const r = ev && ev.clientX != null ? { x: ev.clientX, y: ev.clientY } : (() => { const b = g.getBoundingClientRect(); return { x: b.left + b.width / 2, y: b.top }; })();
    const tw = t.offsetWidth, th = t.offsetHeight;
    t.style.left = Math.max(8, Math.min(window.innerWidth - tw - 8, r.x - tw / 2)) + "px";
    t.style.top = Math.max(8, r.y - th - 12) + "px";
  }

  // ---------------------------------------------------------------- tabla
  function renderTable(ventas) {
    const tbody = $("#tabla tbody");
    tbody.replaceChildren();
    $("#tabla-info").textContent = ventas.total
      ? `Mostrando ${ventas.items.length} de ${ventas.total} ventas (más recientes primero).` : "Sin ventas en este rango.";
    for (const v of ventas.items) {
      const tr = document.createElement("tr");
      [v.fecha, v.vendedor, v.cliente, v.producto, money2.format(v.monto_centavos / 100)].forEach((txt, i) => {
        const td = document.createElement("td");
        td.textContent = txt;
        if (i === 4) td.className = "num";
        tr.append(td);
      });
      const td = document.createElement("td");
      if (ROL === "admin") {
        const b = document.createElement("button");
        b.type = "button"; b.textContent = "Borrar";
        b.setAttribute("aria-label", `Borrar venta ${v.id} de ${v.cliente}`);
        b.addEventListener("click", () => borrar(v));
        td.append(b);
      }
      tr.append(td);
      tbody.append(tr);
    }
  }
  async function borrar(v) {
    if (!window.confirm(`¿Borrar la venta a ${v.cliente} del ${v.fecha}? Esta acción no se puede deshacer.`)) return;
    try {
      await api(`/api/ventas/${v.id}`, { method: "DELETE", headers: { "X-CSRF-Token": CSRF, Accept: "application/json" } });
      load("Venta borrada.");
    } catch (e) { setStatus(`No se pudo borrar: ${e.message}`, "error"); }
  }

  // ---------------------------------------------------------------- formulario
  const FIELDS = ["fecha", "cliente", "producto", "monto", "vendedor"];
  function fieldError(name, msg) {
    const input = document.getElementById(`f-${name}`), out = document.getElementById(`err-${name}`);
    if (!input || !out) return false;
    out.textContent = msg || "";
    if (msg) input.setAttribute("aria-invalid", "true"); else input.removeAttribute("aria-invalid");
    return true;
  }
  function validate(f) {
    const errs = {};
    if (!f.fecha.value) errs.fecha = "Indica la fecha."; else if (f.fecha.value > today()) errs.fecha = "No puede ser futura.";
    if (!f.cliente.value.trim()) errs.cliente = "Indica el cliente.";
    if (!f.producto.value.trim()) errs.producto = "Indica el producto.";
    const n = Number(String(f.monto.value).replace(",", "."));
    if (!(n > 0)) errs.monto = "Debe ser un número mayor que 0.";
    return errs;
  }
  async function submitVenta(ev) {
    ev.preventDefault();
    const f = ev.target, btn = f.querySelector("button[type=submit]");
    FIELDS.forEach((k) => fieldError(k, ""));
    const errs = validate(f);
    if (Object.keys(errs).length) {
      Object.entries(errs).forEach(([k, m]) => fieldError(k, m));
      f.querySelector("[aria-invalid=true]").focus();
      return;
    }
    const body = { fecha: f.fecha.value, cliente: f.cliente.value.trim(), producto: f.producto.value.trim(), monto: f.monto.value };
    if (f.vendedor_id) body.vendedor_id = Number(f.vendedor_id.value);
    btn.disabled = true;
    try {
      await api("/api/ventas", { method: "POST", body: JSON.stringify(body), headers: {
        "Content-Type": "application/json", Accept: "application/json", "X-CSRF-Token": CSRF,
        "Idempotency-Key": (window.crypto && crypto.randomUUID) ? crypto.randomUUID() : String(Date.now()) } });
      ["cliente", "producto", "monto"].forEach((k) => (f[k].value = ""));
      await load("Venta guardada.");
    } catch (e) {
      const errors = (e.problem && e.problem.errors) || [];
      errors.forEach((x) => fieldError(String(x.pointer || "").replace("#/", "").replace("vendedor_id", "vendedor"), x.detail));
      setStatus(`No se pudo guardar: ${e.message}`, "error");
    } finally { btn.disabled = false; }
  }

  // ---------------------------------------------------------------- tema
  function initTheme() {
    const b = $("#theme-toggle");
    let saved = null;
    try { saved = localStorage.getItem("pv-theme"); } catch (e) { /* almacenamiento no disponible */ }
    const apply = (t) => {
      if (t) document.documentElement.setAttribute("data-theme", t);
      const dark = t ? t === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
      b.setAttribute("aria-pressed", String(dark));
    };
    apply(saved);
    b.addEventListener("click", () => {
      const next = b.getAttribute("aria-pressed") === "true" ? "light" : "dark";
      try { localStorage.setItem("pv-theme", next); } catch (e) { /* sin persistencia */ }
      apply(next);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initTheme();
    setPreset("12m");
    $("#f-fecha").value = today();
    document.querySelectorAll("[data-preset]").forEach((b) => b.addEventListener("click", () => { setPreset(b.dataset.preset); load(); }));
    $("#form-rango").addEventListener("submit", (ev) => {
      ev.preventDefault();
      state.desde = $("#desde").value; state.hasta = $("#hasta").value; state.preset = "custom";
      document.querySelectorAll("[data-preset]").forEach((b) => b.setAttribute("aria-pressed", "false"));
      load();
    });
    $("#form-venta").addEventListener("submit", submitVenta);
    let t;
    window.addEventListener("resize", () => { clearTimeout(t); t = setTimeout(() => state.last && render(...state.last), 200); });
    load();
  });
})();
