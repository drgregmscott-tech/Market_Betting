// Market_Betting frontend — Session 3.5
//
// This page now reads TWO independent data files:
//   1. data/clv_log.csv               — Track 1 (pick'em), unchanged since
//      Session 2.8. A copy of data/pickem/clv_log.csv placed here by the
//      Cloudflare Pages build step.
//   2. data/arbitrage_flags_latest.csv — Track 2 (arbitrage), new this
//      session. A copy of data/arbitrage/flags/arbitrage_flags_latest.csv,
//      itself a new file this session's detector.py change writes on every
//      run (a stable, always-overwritten name) alongside the existing
//      timestamped arbitrage_flags_<timestamp>.csv files, so this page has
//      one predictable filename to fetch instead of guessing the latest
//      timestamp. The Cloudflare Pages build command must copy this second
//      file too — see Session 3.5's notes if this section shows a load
//      error in every deploy.
//
// The two tracks are loaded and rendered independently: if one file fails
// to load, the other track's section still renders normally. Neither
// track's failure should ever hide the other track's real data.
//
// No framework, no build tool, no external libraries — matches the DFS
// sibling repos' static-file pattern. The chart is hand-drawn SVG.

(function () {
"use strict";

const DATA_URL = "data/clv_log.csv";
const ARB_DATA_URL = "data/arbitrage_flags_latest.csv";

// ---------------------------------------------------------------------
// Sizing constants -- ported exactly from scripts/sizing/sizing_engine.py.
// Any change to the Python script's constants must be mirrored here by
// hand; there is no shared source of truth between the two, so this
// block should be checked against the script whenever either changes.
// ---------------------------------------------------------------------
const SUPPORTED_LEG_COUNT = 2;
const SUPPORTED_PLATFORMS = new Set(["prizepicks"]);
const ENTRY_PAYOUT_MULTIPLIER = 3.0;
const ENTRY_NET_ODDS_B = ENTRY_PAYOUT_MULTIPLIER - 1.0;
const KELLY_FRACTION = 0.25;
const PLATFORM_RISK_MULTIPLIER = { prizepicks: 0.70, underdog: 0.85 };
const MAX_SINGLE_POSITION_PCT = 0.05;
const MIN_BANKROLL = 1.0;
const SAME_GAME_CAUTION_MULTIPLIER = 0.85;

// Selected legs for the sizing calculator: Map<flag_id, row>
const selectedLegs = new Map();

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
  if (!header) return [];
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
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function escapeAttr(s) {
  return String(s == null ? "" : s).replace(/"/g, "&quot;");
}

function escapeHtml(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

// =======================================================================
// TRACK 1 — Pick'em (unchanged from Session 2.8, aside from small
// null-safety additions so a missing element never throws and blocks
// Track 2 from rendering).
// =======================================================================

function renderStats(rows) {
  const open = rows.filter((r) => r.status === "open");
  const closed = rows.filter((r) => r.status === "closed" && toNum(r.clv_edge_at_close) !== null);

  const avgEdge = closed.length
    ? closed.reduce((sum, r) => sum + toNum(r.clv_edge_at_close), 0) / closed.length
    : null;
  const positive = closed.filter((r) => toNum(r.clv_edge_at_close) > 0).length;
  const hitRate = closed.length ? (positive / closed.length) * 100 : null;

  setText("statOpen", String(open.length));
  setText("statClosed", String(closed.length));

  const cumEl = document.getElementById("statCumEdge");
  if (cumEl) {
    cumEl.textContent = avgEdge === null ? "—" : fmtEdge(avgEdge);
    cumEl.className = "stat-value " + (avgEdge === null ? "" : edgeClass(avgEdge).replace("edge-", ""));
  }

  setText("statHitRate", hitRate === null ? "—" : hitRate.toFixed(0) + "%");

  return { open, closed };
}

function renderChart(closed) {
  const svg = document.getElementById("trendChart");
  const emptyNote = document.getElementById("chartEmpty");
  if (!svg || !emptyNote) return;

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
  if (!tbody || !emptyNote) return;

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
      const checked = selectedLegs.has(r.flag_id) ? "checked" : "";
      return `
        <tr>
          <td class="checkbox-cell">
            <input type="checkbox" data-flag-id="${escapeAttr(r.flag_id)}" ${checked} />
          </td>
          <td class="name-cell">${escapeHtml(r.player_name) || "—"}</td>
          <td>${escapeHtml(r.team) || "—"}</td>
          <td>${escapeHtml(r.stat_type) || "—"}</td>
          <td>${escapeHtml(r.flagged_side) || "—"}</td>
          <td>${escapeHtml(r.platform) || "—"}</td>
          <td>${escapeHtml(r.last_seen_line || r.first_flagged_line) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.game_start_time)}</td>
        </tr>`;
    })
    .join("");

  tbody.querySelectorAll("input[type=checkbox]").forEach((cb) => {
    cb.addEventListener("change", (e) => onLegToggle(e, sorted));
  });
}

function onLegToggle(e, currentOpenRows) {
  const flagId = e.target.getAttribute("data-flag-id");
  const row = currentOpenRows.find((r) => r.flag_id === flagId);
  if (!row) return;

  if (e.target.checked) {
    if (selectedLegs.size >= SUPPORTED_LEG_COUNT && !selectedLegs.has(flagId)) {
      const oldestKey = selectedLegs.keys().next().value;
      selectedLegs.delete(oldestKey);
    }
    selectedLegs.set(flagId, row);
  } else {
    selectedLegs.delete(flagId);
  }

  renderSelectedLegs();
  renderSizingResult();
  syncCheckboxes();
}

function syncCheckboxes() {
  document.querySelectorAll("#openTableBody input[type=checkbox]").forEach((cb) => {
    cb.checked = selectedLegs.has(cb.getAttribute("data-flag-id"));
  });
}

function renderSelectedLegs() {
  const wrap = document.getElementById("sizingSelectedLegs");
  if (!wrap) return;
  if (!selectedLegs.size) {
    wrap.innerHTML = `<p class="empty-note">None selected. Check two PrizePicks flags in the table above.</p>`;
    return;
  }
  wrap.innerHTML = Array.from(selectedLegs.values())
    .map(
      (r) => `
      <div class="leg-chip">
        <div class="leg-chip-info">
          <span class="leg-chip-name">${escapeHtml(r.player_name) || "—"} &mdash; ${escapeHtml(r.stat_type) || "—"} ${escapeHtml(r.flagged_side) || ""}</span>
          <span class="leg-chip-detail">${escapeHtml(r.platform) || "—"} · line ${escapeHtml(r.last_seen_line || r.first_flagged_line) || "—"} · model prob ${
            toNum(r.first_flagged_model_prob) !== null ? (toNum(r.first_flagged_model_prob) * 100).toFixed(1) + "%" : "—"
          }</span>
        </div>
        <button class="leg-chip-remove" data-remove-flag-id="${escapeAttr(r.flag_id)}">Remove</button>
      </div>`
    )
    .join("");

  wrap.querySelectorAll("[data-remove-flag-id]").forEach((btn) => {
    btn.addEventListener("click", () => {
      selectedLegs.delete(btn.getAttribute("data-remove-flag-id"));
      renderSelectedLegs();
      renderSizingResult();
      syncCheckboxes();
    });
  });
}

function sizeEntry(legs, bankroll) {
  const platforms = new Set(legs.map((l) => l.platform));

  if (legs.length !== SUPPORTED_LEG_COUNT) {
    return { status: "rejected", reason: `Select exactly ${SUPPORTED_LEG_COUNT} legs (2-pick Power Play) — currently ${legs.length} selected.` };
  }
  if (platforms.size !== 1 || !SUPPORTED_PLATFORMS.has([...platforms][0])) {
    return {
      status: "rejected",
      reason: `Only platform(s) ${[...SUPPORTED_PLATFORMS].join(", ")} are supported — selected leg(s) are from ${[...platforms].join(", ")}. No sourced payout multiplier exists yet for any other platform.`,
    };
  }
  for (const leg of legs) {
    if (toNum(leg.first_flagged_model_prob) === null) {
      return { status: "rejected", reason: `Flag ${leg.flag_id} has no model probability logged — cannot size it.` };
    }
    if (!leg.game_id) {
      return { status: "rejected", reason: `Flag ${leg.flag_id} has no game_id logged — required for the same-game caution check.` };
    }
  }
  if (!(bankroll >= MIN_BANKROLL)) {
    return { status: "rejected", reason: `Bankroll must be at least $${MIN_BANKROLL}.` };
  }

  const pCombined = legs.reduce((p, l) => p * toNum(l.first_flagged_model_prob), 1.0);
  const fRaw = (pCombined * (ENTRY_NET_ODDS_B + 1.0) - 1.0) / ENTRY_NET_ODDS_B;
  const fQuarter = Math.max(fRaw, 0) * KELLY_FRACTION;

  const platform = legs[0].platform;
  const dampener = PLATFORM_RISK_MULTIPLIER[platform];

  const gameIds = new Set(legs.map((l) => l.game_id));
  const sameGamePair = gameIds.size === 1;
  const sameGameMultiplier = sameGamePair ? SAME_GAME_CAUTION_MULTIPLIER : 1.0;

  const fDampened = fQuarter * dampener * sameGameMultiplier;

  const uncappedStake = bankroll * fDampened;
  const capAmount = bankroll * MAX_SINGLE_POSITION_PCT;
  const capped = uncappedStake > capAmount;
  let finalStake = Math.min(uncappedStake, capAmount);

  let status;
  if (fRaw <= 0) {
    status = "no_bet_negative_edge";
    finalStake = 0;
  } else if (capped) {
    status = "sized_capped_at_max_position";
  } else {
    status = "sized";
  }

  return {
    status,
    platform,
    combinedEntryProbability: pCombined,
    rawKellyFraction: fRaw,
    quarterKellyFraction: fQuarter,
    platformRiskMultiplier: dampener,
    sameGamePair,
    sameGameMultiplier,
    dampenedKellyFraction: fDampened,
    bankroll,
    uncappedStake,
    capAmount,
    finalStake,
  };
}

function statusLabel(status) {
  switch (status) {
    case "sized": return "Sized";
    case "sized_capped_at_max_position": return "Sized — capped at 5% of bankroll";
    case "no_bet_negative_edge": return "No bet — combined edge is not positive";
    default: return status;
  }
}

function renderSizingResult() {
  const el = document.getElementById("sizingResult");
  const bankrollInput = document.getElementById("bankrollInput");
  if (!el || !bankrollInput) return;
  const bankroll = toNum(bankrollInput.value);

  if (selectedLegs.size === 0) {
    el.hidden = true;
    return;
  }

  if (bankroll === null) {
    el.hidden = false;
    el.className = "sizing-result rejected";
    el.innerHTML = `<p class="sizing-reject-text">Enter a current bankroll above to size this entry.</p>`;
    return;
  }

  const legs = Array.from(selectedLegs.values());
  const result = sizeEntry(legs, bankroll);
  el.hidden = false;

  if (result.status === "rejected") {
    el.className = "sizing-result rejected";
    el.innerHTML = `<p class="sizing-reject-text">${escapeHtml(result.reason)}</p>`;
    return;
  }

  el.className = "sizing-result";
  el.innerHTML = `
    <div class="sizing-stake-line">
      <span class="sizing-stake-value">$${result.finalStake.toFixed(2)}</span>
      <span class="sizing-stake-status">${statusLabel(result.status)}</span>
    </div>
    <div class="sizing-breakdown">
      <div><span>Combined entry probability</span><span>${(result.combinedEntryProbability * 100).toFixed(1)}%</span></div>
      <div><span>Raw Kelly fraction</span><span>${(result.rawKellyFraction * 100).toFixed(2)}%</span></div>
      <div><span>Quarter-Kelly fraction</span><span>${(result.quarterKellyFraction * 100).toFixed(2)}%</span></div>
      <div><span>Platform risk multiplier</span><span>${result.platformRiskMultiplier.toFixed(2)}×</span></div>
      <div><span>Same-game pair</span><span>${result.sameGamePair ? "Yes (0.85× caution applied)" : "No"}</span></div>
      <div><span>Dampened Kelly fraction</span><span>${(result.dampenedKellyFraction * 100).toFixed(2)}%</span></div>
      <div><span>Bankroll entered</span><span>$${result.bankroll.toFixed(2)}</span></div>
      <div><span>Uncapped suggested stake</span><span>$${result.uncappedStake.toFixed(2)}</span></div>
      <div><span>5% bankroll cap</span><span>$${result.capAmount.toFixed(2)}</span></div>
    </div>
  `;
}

function renderClosedTable(closed) {
  const tbody = document.getElementById("closedTableBody");
  const emptyNote = document.getElementById("closedEmpty");
  if (!tbody || !emptyNote) return;

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
          <td class="name-cell">${escapeHtml(r.player_name) || "—"}</td>
          <td>${escapeHtml(r.stat_type) || "—"}</td>
          <td>${escapeHtml(r.flagged_side) || "—"}</td>
          <td>${escapeHtml(r.platform) || "—"}</td>
          <td>${escapeHtml(r.closing_line) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.closing_pulled_at)}</td>
        </tr>`;
    })
    .join("");
}

async function initPickem() {
  try {
    const res = await fetch(DATA_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const text = await res.text();
    const rows = parseCSV(text);

    const { open, closed } = renderStats(rows);
    renderChart(closed);
    renderOpenTable(open);
    renderClosedTable(closed);
    renderSelectedLegs();

    const bankrollInput = document.getElementById("bankrollInput");
    if (bankrollInput) bankrollInput.addEventListener("input", renderSizingResult);
  } catch (err) {
    const el = document.getElementById("loadError");
    if (el) el.hidden = false;
    console.error("Market_Betting frontend: failed to load pick'em data.", err);
  }
}

// =======================================================================
// TRACK 2 — Arbitrage (new this session)
//
// arbitrage_flags_latest.csv is a full replace on every pipeline run, not
// an append-only log the way clv_log.csv is (see detector.py's Session 3.5
// change). There is therefore no "open vs. closed" distinction here and no
// trend chart: every row in this file is this run's current snapshot.
// =======================================================================

function fmtNetProfit(n) {
  if (n === null) return "—";
  return "$" + n.toFixed(4);
}

function fmtBool(v) {
  const s = String(v).trim().toLowerCase();
  if (s === "true") return "Yes";
  if (s === "false") return "No";
  return v || "—";
}

function renderArbStats(rows) {
  const singleTypes = new Set(["kalshi_yes_no", "polymarket_yes_no"]);
  const single = rows.filter((r) => singleTypes.has(r.opportunity_type));
  const cross = rows.filter((r) => r.opportunity_type === "cross_venue");
  const fillable = rows.filter((r) => String(r.liquidity_sufficient).trim().toLowerCase() === "true");

  setText("arbStatTotal", String(rows.length));
  setText("arbStatSingle", String(single.length));
  setText("arbStatCross", String(cross.length));
  setText("arbStatFillable", String(fillable.length));
}

function renderArbTable(rows) {
  const tbody = document.getElementById("arbTableBody");
  const emptyNote = document.getElementById("arbEmpty");
  if (!tbody || !emptyNote) return;

  const sorted = rows
    .slice()
    .sort((a, b) => (toNum(b.net_profit_per_dollar) || -1) - (toNum(a.net_profit_per_dollar) || -1));

  if (!sorted.length) {
    emptyNote.hidden = false;
    tbody.innerHTML = "";
    return;
  }
  emptyNote.hidden = true;

  tbody.innerHTML = sorted
    .map((r) => {
      const netProfit = toNum(r.net_profit_per_dollar);
      return `
        <tr>
          <td>${escapeHtml(r.opportunity_type) || "—"}</td>
          <td>${escapeHtml(r.platform_a) || "—"}</td>
          <td class="name-cell" title="${escapeAttr(r.title_a)}">${escapeHtml(r.title_a) || "—"}</td>
          <td>${escapeHtml(r.leg_a_ask) || "—"}</td>
          <td>${escapeHtml(r.platform_b) || "—"}</td>
          <td class="name-cell" title="${escapeAttr(r.title_b)}">${escapeHtml(r.title_b) || "—"}</td>
          <td>${escapeHtml(r.leg_b_ask) || "—"}</td>
          <td class="${edgeClass(netProfit)}">${fmtNetProfit(netProfit)}</td>
          <td>${fmtBool(r.liquidity_sufficient)}</td>
          <td>${escapeHtml(r.legal_footprint_status) || "—"}</td>
        </tr>`;
    })
    .join("");
}

async function initArbitrage() {
  try {
    const res = await fetch(ARB_DATA_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const text = await res.text();
    const rows = parseCSV(text);

    renderArbStats(rows);
    renderArbTable(rows);
  } catch (err) {
    const el = document.getElementById("arbLoadError");
    if (el) el.hidden = false;
    console.error("Market_Betting frontend: failed to load arbitrage data.", err);
  }
}

async function init() {
  // Both tracks load independently and in parallel: a failure or an
  // empty result in one must never block or hide the other track's
  // real data on the page.
  await Promise.allSettled([initPickem(), initArbitrage()]);

  setText("asOf", new Date().toLocaleString(undefined, {
    month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
  }));
}

init();
})();
