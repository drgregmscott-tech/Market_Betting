// Market_Betting frontend — Session 2.8
//
// This page reads a single data file: data/clv_log.csv, which is a copy of
// data/pickem/clv_log.csv placed there by the Cloudflare Pages build step
// (see the build command in the project's Cloudflare Pages settings).
//
// No framework, no build tool, no external libraries — matches the DFS
// sibling repos' static-file pattern. The chart is hand-drawn SVG.

(function () {
  "use strict";

  const DATA_URL = "data/clv_log.csv";

  function parseCSV(text) {
    // Minimal CSV parser: handles quoted fields containing commas, but this
    // dataset has none observed — kept defensive rather than assuming.
    const rows = [];
    let row = [];
    let field = "";
    let inQuotes = false;

    for (let i = 0; i < text.length; i++) {
      const c = text[i];
      if (inQuotes) {
        if (c === '"') {
          if (text[i + 1] === '"') { field += '"'; i++; }
          else { inQuotes = false; }
        } else {
          field += c;
        }
      } else {
        if (c === '"') { inQuotes = true; }
        else if (c === ",") { row.push(field); field = ""; }
        else if (c === "\n") {
          if (text[i - 1] !== "\r") { row.push(field); field = ""; rows.push(row); row = []; }
        }
        else if (c === "\r") { /* skip, handled with \n */ }
        else { field += c; }
      }
    }
    if (field.length || row.length) { row.push(field); rows.push(row); }

    const header = rows.shift();
    return rows
      .filter((r) => r.length === header.length && r.some((v) => v !== ""))
      .map((r) => {
        const obj = {};
        header.forEach((h, idx) => { obj[h] = r[idx]; });
        return obj;
      });
  }

  function toNum(v) {
    const n = parseFloat(v);
    return Number.isFinite(n) ? n : null;
  }

  function fmtEdge(n) {
    if (n === null) return "—";
    const pct = (n * 100).toFixed(1) + "%";
    return (n > 0 ? "+" : "") + pct;
  }

  function fmtDate(iso) {
    if (!iso) return "—";
    const d = new Date(iso);
    if (isNaN(d.getTime())) return iso;
    return d.toLocaleString(undefined, {
      month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
    });
  }

  function edgeClass(n) {
    if (n === null) return "";
    return n >= 0 ? "edge-pos" : "edge-neg";
  }

  function setText(id, value) {
    document.getElementById(id).textContent = value;
  }

  function renderStats(rows) {
    const open = rows.filter((r) => r.status === "open");
    const closed = rows.filter((r) => r.status === "closed" && toNum(r.clv_edge_at_close) !== null);

    // Average edge per closed flag, not a raw sum. Summing a percentage
    // across hundreds of independent flags produces a number with no real
    // meaning (it grows without bound as more flags close). The average is
    // the honest "is this system right more often than chance" signal.
    const avgEdge = closed.length
      ? closed.reduce((sum, r) => sum + toNum(r.clv_edge_at_close), 0) / closed.length
      : null;
    const positive = closed.filter((r) => toNum(r.clv_edge_at_close) > 0).length;
    const hitRate = closed.length ? (positive / closed.length) * 100 : null;

    setText("statOpen", String(open.length));
    setText("statClosed", String(closed.length));

    const cumEl = document.getElementById("statCumEdge");
    cumEl.textContent = avgEdge === null ? "—" : fmtEdge(avgEdge);
    cumEl.className = "stat-value " + (avgEdge === null ? "" : edgeClass(avgEdge).replace("edge-", ""));

    setText("statHitRate", hitRate === null ? "—" : hitRate.toFixed(0) + "%");

    return { open, closed };
  }

  function renderChart(closed) {
    const svg = document.getElementById("trendChart");
    const emptyNote = document.getElementById("chartEmpty");

    if (!closed.length) {
      emptyNote.hidden = false;
      return;
    }
    emptyNote.hidden = true;

    const sorted = closed.slice().sort((a, b) => {
      const ta = new Date(a.closing_pulled_at || a.last_seen_at || 0).getTime();
      const tb = new Date(b.closing_pulled_at || b.last_seen_at || 0).getTime();
      return ta - tb;
    });

    // Running average edge as each flag closes, not a running sum — a sum
    // grows without bound as more flags close and stops meaning anything.
    // The average is what shows whether the system holds an edge over time,
    // including real losing stretches, the way the project's roadmap asks for.
    let runningSum = 0;
    const points = sorted.map((r, i) => {
      runningSum += toNum(r.clv_edge_at_close) || 0;
      return runningSum / (i + 1);
    });

    const W = 900, H = 320, PAD = 36;
    const minV = Math.min(0, ...points);
    const maxV = Math.max(0, ...points);
    const range = (maxV - minV) || 1;

    const x = (i) => PAD + (i / Math.max(points.length - 1, 1)) * (W - PAD * 2);
    const y = (v) => H - PAD - ((v - minV) / range) * (H - PAD * 2);

    const zeroY = y(0);

    const linePath = points
      .map((v, i) => (i === 0 ? "M" : "L") + x(i).toFixed(1) + "," + y(v).toFixed(1))
      .join(" ");

    const areaPath =
      linePath +
      ` L${x(points.length - 1).toFixed(1)},${zeroY.toFixed(1)} L${x(0).toFixed(1)},${zeroY.toFixed(1)} Z`;

    const finalVal = points[points.length - 1];
    const lineColor = finalVal >= 0 ? "#4fd18b" : "#e2685b";

    svg.innerHTML = `
      <line x1="${PAD}" y1="${zeroY.toFixed(1)}" x2="${W - PAD}" y2="${zeroY.toFixed(1)}"
            stroke="#223129" stroke-width="1" stroke-dasharray="3,4" />
      <path d="${areaPath}" fill="${lineColor}" opacity="0.10" stroke="none" />
      <path d="${linePath}" fill="none" stroke="${lineColor}" stroke-width="2" />
      <text x="${PAD}" y="16" fill="#5c6f66" font-size="11" font-family="monospace">
        ${sorted.length} closed flag${sorted.length === 1 ? "" : "s"}
      </text>
      <text x="${W - PAD}" y="16" fill="${lineColor}" font-size="11" font-family="monospace" text-anchor="end">
        ${fmtEdge(finalVal)} average edge
      </text>
    `;
  }

  function renderOpenTable(open) {
    const tbody = document.getElementById("openTableBody");
    const emptyNote = document.getElementById("openEmpty");

    const sorted = open
      .slice()
      .sort((a, b) => (toNum(b.first_flagged_edge) || -1) - (toNum(a.first_flagged_edge) || -1));

    if (!sorted.length) {
      emptyNote.hidden = false;
      tbody.innerHTML = "";
      return;
    }
    emptyNote.hidden = true;

    tbody.innerHTML = sorted
      .map((r) => {
        const edge = toNum(r.first_flagged_edge);
        return `
        <tr>
          <td class="name-cell">${r.player_name || "—"}</td>
          <td>${r.team || "—"}</td>
          <td>${r.stat_type || "—"}</td>
          <td>${r.flagged_side || "—"}</td>
          <td>${r.platform || "—"}</td>
          <td>${r.last_seen_line || r.first_flagged_line || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.game_start_time)}</td>
        </tr>`;
      })
      .join("");
  }

  function renderClosedTable(closed) {
    const tbody = document.getElementById("closedTableBody");
    const emptyNote = document.getElementById("closedEmpty");

    const sorted = closed
      .slice()
      .sort((a, b) => new Date(b.closing_pulled_at || 0) - new Date(a.closing_pulled_at || 0))
      .slice(0, 25);

    if (!sorted.length) {
      emptyNote.hidden = false;
      tbody.innerHTML = "";
      return;
    }
    emptyNote.hidden = true;

    tbody.innerHTML = sorted
      .map((r) => {
        const edge = toNum(r.clv_edge_at_close);
        return `
        <tr>
          <td class="name-cell">${r.player_name || "—"}</td>
          <td>${r.stat_type || "—"}</td>
          <td>${r.flagged_side || "—"}</td>
          <td>${r.platform || "—"}</td>
          <td>${r.closing_line || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.closing_pulled_at)}</td>
        </tr>`;
      })
      .join("");
  }

  async function init() {
    try {
      const res = await fetch(DATA_URL, { cache: "no-store" });
      if (!res.ok) throw new Error("HTTP " + res.status);
      const text = await res.text();
      const rows = parseCSV(text);

      const { open, closed } = renderStats(rows);
      renderChart(closed);
      renderOpenTable(open);
      renderClosedTable(closed);

      setText("asOf", new Date().toLocaleString(undefined, {
        month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
      }));
    } catch (err) {
      document.getElementById("loadError").hidden = false;
      console.error("Market_Betting frontend: failed to load data.", err);
    }
  }

  init();
})();
