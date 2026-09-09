// Market_Betting frontend — Session 4.6
//
// This page now reads FOUR independent data files:
//   1. data/clv_log.csv               — Track 1 (pick'em), unchanged since
//      Session 2.8. A copy of data/pickem/clv_log.csv placed here by the
//      Cloudflare Pages build step.
//   2. data/arbitrage_flags_latest.csv — Track 2 (arbitrage), Session 3.5.
//      A copy of data/arbitrage/flags/arbitrage_flags_latest.csv.
//   3. data/weather_clv_log.csv        — Track 3 (weather), new this
//      session. A copy of data/weather/clv_log.csv.
//   4. data/politics_clv_log.csv       — Track 4 (down-ballot politics),
//      Session 5.6. A copy of data/politics/clv_log.csv.
//
//      The Cloudflare Pages build command must be updated to copy this
//      third file too, same one-time dashboard edit Sessions 3.5/5.6
//      needed for their own tracks — see this session's handoff notes for
//      the exact command.
//
// All tracks are loaded and rendered independently: if one file fails to
// load, the other tracks' sections still render normally. No track's
// failure should ever hide another track's real data.
//
// No framework, no build tool, no external libraries — matches the DFS
// sibling repos' static-file pattern. The chart is hand-drawn SVG.

(function () {
"use strict";

const DATA_URL = "data/clv_log.csv";
const ARB_DATA_URL = "data/arbitrage_flags_latest.csv";
const WEATHER_DATA_URL = "data/weather_clv_log.csv";
const POLITICS_DATA_URL = "data/politics_clv_log.csv";
const PROPS_DATA_URL = "data/props_clv_log.csv";

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

// ---------------------------------------------------------------------
// Overview tab -- each track's init function stashes its own currently-
// open, still-actionable rows here so the Overview tab can pool them
// into one ranked list without re-fetching anything. A track that fails
// to load simply leaves its array empty; the Overview never blocks on
// one track's failure, same rule as every other part of this page.
// ---------------------------------------------------------------------
const overviewData = {
  pickem: { loaded: false, rows: [] },
  arb: { loaded: false, rows: [] },
  weather: { loaded: false, rows: [] },
  politics: { loaded: false, rows: [] },
  props: { loaded: false, rows: [] },
};

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
        // End of row for LF-only files, and the second half of a CRLF
        // pair (the \r just before this was already handled below).
        row.push(field); field = ""; rows.push(row); row = [];
      }
      else if (c === "\r") {
        // Only end the row here for a lone CR. If this CR is followed
        // by LF (a CRLF pair -- what Python's csv module writes by
        // default, e.g. detector.py's output), let the "\n" branch
        // above end the row instead, so the row isn't ended twice and,
        // more importantly, so it gets ended at all: the previous
        // version of this check only fired when the PRECEDING
        // character was not "\r", which is backwards and silently
        // dropped every row in any CRLF file. Confirmed via Session
        // 3.5's own live-site check: arbitrage_flags_latest.csv (CRLF,
        // from Python's csv.writer) parsed to zero rows under the old
        // logic despite loading successfully over the network; pick'em's
        // clv_log.csv (LF-only) was never affected, which is why this
        // went unnoticed for five prior sessions.
        if (text[i + 1] !== "\n") { row.push(field); field = ""; rows.push(row); row = []; }
      }
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

// A row counts as "actionable" for the Overview tab if its own timing
// field is either unknown (never filter out a row just because we can't
// parse its timestamp) or genuinely still in the future. Used for
// game_start_time (pick'em/props) and target_date (weather); politics
// uses hours_to_resolution directly instead (see initPolitics).
function isFutureOrUnknown(iso) {
  if (!iso) return true;
  const t = new Date(iso).getTime();
  if (isNaN(t)) return true;
  return t > Date.now();
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

    overviewData.pickem.loaded = true;
    overviewData.pickem.rows = open.filter((r) => isFutureOrUnknown(r.game_start_time));
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

    overviewData.arb.loaded = true;
    overviewData.arb.rows = rows.filter(
      (r) => String(r.liquidity_sufficient).trim().toLowerCase() === "true"
    );
  } catch (err) {
    const el = document.getElementById("arbLoadError");
    if (el) el.hidden = false;
    console.error("Market_Betting frontend: failed to load arbitrage data.", err);
  }
}

// =======================================================================
// TRACK 3 — Weather/climate markets (new this session)
//
// weather_clv_log.csv shares the same open/closed lifecycle shape as
// pick'em's clv_log.csv (Session 4.3 built this track on the same shared
// CLV structure, per clv_logger.py). Two real differences from the other
// tracks, both handled explicitly rather than by reusing another track's
// code unchanged: (1) consensus_available is always false here — Kalshi
// is the only venue this track ingests (Session 4.1), so there is no
// cross-venue benchmark to show, unlike pick'em/politics; (2) each row
// carries real forecast context (city, target date, strike threshold,
// forecast value) instead of a player/team or a candidate/race — shown
// directly in the open/closed tables so a flagged contract reads as a
// real weather bet, not an anonymous ticker.
// =======================================================================

function fmtStrike(r) {
  const kind = escapeHtml(r.strike_type) || "";
  const floor = r.floor_strike, cap = r.cap_strike;
  if (floor && cap) return `${escapeHtml(floor)}–${escapeHtml(cap)}°F`;
  if (floor) return `≥${escapeHtml(floor)}°F`;
  if (cap) return `≤${escapeHtml(cap)}°F`;
  return kind || "—";
}

function renderWeatherStats(rows) {
  const open = rows.filter((r) => r.status === "open");
  const closed = rows.filter((r) => r.status === "closed" && toNum(r.clv_edge_at_close) !== null);

  const avgEdge = closed.length
    ? closed.reduce((sum, r) => sum + toNum(r.clv_edge_at_close), 0) / closed.length
    : null;
  const positive = closed.filter((r) => toNum(r.clv_edge_at_close) > 0).length;
  const hitRate = closed.length ? (positive / closed.length) * 100 : null;

  setText("weatherStatOpen", String(open.length));
  setText("weatherStatClosed", String(closed.length));

  const cumEl = document.getElementById("weatherStatCumEdge");
  if (cumEl) {
    cumEl.textContent = avgEdge === null ? "—" : fmtEdge(avgEdge);
    cumEl.className = "stat-value " + (avgEdge === null ? "" : edgeClass(avgEdge).replace("edge-", ""));
  }

  setText("weatherStatHitRate", hitRate === null ? "—" : hitRate.toFixed(0) + "%");

  return { open, closed };
}

function renderWeatherOpenTable(open) {
  const tbody = document.getElementById("weatherOpenTableBody");
  const emptyNote = document.getElementById("weatherOpenEmpty");
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
      return `
        <tr>
          <td class="name-cell">${escapeHtml(r.city_label) || "—"}</td>
          <td>${fmtDate(r.target_date)}</td>
          <td>${escapeHtml(r.forecast_kind) || "—"}${r.forecast_value_f ? " " + escapeHtml(r.forecast_value_f) + "°F" : ""}</td>
          <td>${fmtStrike(r)}</td>
          <td>${escapeHtml(r.flagged_side) || "—"}</td>
          <td>${escapeHtml(r.first_flagged_market_price) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${escapeHtml(r.lead_days) || "—"}d</td>
        </tr>`;
    })
    .join("");
}

function renderWeatherClosedTable(closed) {
  const tbody = document.getElementById("weatherClosedTableBody");
  const emptyNote = document.getElementById("weatherClosedEmpty");
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
          <td class="name-cell">${escapeHtml(r.city_label) || "—"}</td>
          <td>${fmtDate(r.target_date)}</td>
          <td>${escapeHtml(r.flagged_side) || "—"}</td>
          <td>${escapeHtml(r.closing_market_price) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.closing_pulled_at)}</td>
        </tr>`;
    })
    .join("");
}

async function initWeather() {
  try {
    const res = await fetch(WEATHER_DATA_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const text = await res.text();
    const rows = parseCSV(text);

    const { open, closed } = renderWeatherStats(rows);
    renderWeatherOpenTable(open);
    renderWeatherClosedTable(closed);

    overviewData.weather.loaded = true;
    overviewData.weather.rows = open.filter((r) => isFutureOrUnknown(r.target_date));
  } catch (err) {
    const el = document.getElementById("weatherLoadError");
    if (el) el.hidden = false;
    console.error("Market_Betting frontend: failed to load weather data.", err);
  }
}

// =======================================================================
// TRACK 4 — Down-ballot politics (Session 5.6)
//
// politics_clv_log.csv shares the same open/closed lifecycle shape as
// pick'em's clv_log.csv (Session 4.3/5.3 built the politics track on the
// same shared CLV structure, per clv_logger.py). The one real difference
// this track's own roadmap card calls out explicitly: these are
// long-dated positions — races can sit open for weeks or months — so
// every flagged row here shows real resolution-date context
// (hours_to_resolution, converted to a human "time to resolution" string)
// rather than a game-time column the way pick'em/arbitrage do.
// =======================================================================

function fmtHoursToResolution(h) {
  const n = toNum(h);
  if (n === null) return "—";
  if (n < 0) return "past due";
  if (n < 24) return Math.round(n) + "h";
  const days = n / 24;
  if (days < 60) return Math.round(days) + "d";
  const months = days / 30.44;
  return months.toFixed(1) + "mo";
}

function renderPoliticsStats(rows) {
  const open = rows.filter((r) => r.status === "open");
  const closed = rows.filter((r) => r.status === "closed" && toNum(r.clv_edge_at_close) !== null);

  const avgEdge = closed.length
    ? closed.reduce((sum, r) => sum + toNum(r.clv_edge_at_close), 0) / closed.length
    : null;
  const avgHours = open.length
    ? open.reduce((sum, r) => sum + (toNum(r.hours_to_resolution) || 0), 0) / open.length
    : null;

  setText("politicsStatOpen", String(open.length));
  setText("politicsStatClosed", String(closed.length));

  const cumEl = document.getElementById("politicsStatCumEdge");
  if (cumEl) {
    cumEl.textContent = avgEdge === null ? "—" : fmtEdge(avgEdge);
    cumEl.className = "stat-value " + (avgEdge === null ? "" : edgeClass(avgEdge).replace("edge-", ""));
  }

  setText("politicsStatAvgWait", avgHours === null ? "—" : fmtHoursToResolution(avgHours) + " avg");

  return { open, closed };
}

function renderPoliticsOpenTable(open) {
  const tbody = document.getElementById("politicsOpenTableBody");
  const emptyNote = document.getElementById("politicsOpenEmpty");
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
      const hours = toNum(r.hours_to_resolution);
      const waitClass = hours !== null && hours > 24 * 60 ? "wait-long" : "";
      return `
        <tr>
          <td class="name-cell" title="${escapeAttr(r.candidate_name)}">${escapeHtml(r.candidate_name) || "—"}</td>
          <td>${escapeHtml(r.party) || "—"}</td>
          <td>${escapeHtml(r.state) || "—"}</td>
          <td>${escapeHtml(r.chamber) || "—"}${r.district ? " " + escapeHtml(r.district) : ""}</td>
          <td>${escapeHtml(r.venue) || "—"}</td>
          <td>${escapeHtml(r.first_flagged_market_price) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td class="${waitClass}">${fmtHoursToResolution(hours)}</td>
        </tr>`;
    })
    .join("");
}

function renderPoliticsClosedTable(closed) {
  const tbody = document.getElementById("politicsClosedTableBody");
  const emptyNote = document.getElementById("politicsClosedEmpty");
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
          <td class="name-cell">${escapeHtml(r.candidate_name) || "—"}</td>
          <td>${escapeHtml(r.party) || "—"}</td>
          <td>${escapeHtml(r.state) || "—"}</td>
          <td>${escapeHtml(r.venue) || "—"}</td>
          <td>${escapeHtml(r.closing_market_price) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.closing_pulled_at)}</td>
        </tr>`;
    })
    .join("");
}

async function initPolitics() {
  try {
    const res = await fetch(POLITICS_DATA_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const text = await res.text();
    const rows = parseCSV(text);

    const { open, closed } = renderPoliticsStats(rows);
    renderPoliticsOpenTable(open);
    renderPoliticsClosedTable(closed);

    overviewData.politics.loaded = true;
    overviewData.politics.rows = open.filter((r) => {
      const hours = toNum(r.hours_to_resolution);
      return hours === null || hours > 0;
    });
  } catch (err) {
    const el = document.getElementById("politicsLoadError");
    if (el) el.hidden = false;
    console.error("Market_Betting frontend: failed to load politics data.", err);
  }
}

// =======================================================================
// TRACK 5 — Sportsbook player props, DraftKings + FanDuel (Session 6.6)
//
// props_clv_log.csv shares the same open/closed lifecycle shape as
// pick'em's clv_log.csv (Session 6.3 built this track on the same shared
// CLV structure, per clv_logger.py's CLV_LOG_COLUMNS_PROPS). This
// session's own validation requirement is the account-limiting-risk
// indicator, shown per row via renderRiskBadges() below — the real point
// of this track's frontend card, per ROADMAP.md's Session 6.6 entry.
// =======================================================================

function renderRiskBadges(r) {
  // Every DK/FD row carries the same PROPS_PLATFORM_RISK_MULTIPLIER
  // (0.50, sizing_engine.py) -- this badge is intentionally shown on
  // every row rather than only on "risky" ones, since sportsbook
  // account-limiting is this track's own best-corroborated risk for the
  // whole venue type, not a per-row condition.
  let badges = `<span class="risk-badge" title="DraftKings/FanDuel positions carry this project's highest account-limiting-risk dampener (PROPS_PLATFORM_RISK_MULTIPLIER = 0.50), applied equally to both platforms.">Acct. limit risk</span>`;

  const fieldVig = String(r.implied_prob_includes_field_vig).trim().toLowerCase() === "true";
  if (fieldVig) {
    badges += `<span class="risk-badge" title="This row's own price still includes DraftKings' one-sided field vig (implied_prob_includes_field_vig = True) -- sizing_engine.py applies an extra PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER (0.60) dampener to it.">Field vig</span>`;
  }
  return badges;
}

function renderPropsStats(rows) {
  const open = rows.filter((r) => r.status === "open");
  const closed = rows.filter((r) => r.status === "closed" && toNum(r.clv_edge_at_close) !== null);

  const avgEdge = closed.length
    ? closed.reduce((sum, r) => sum + toNum(r.clv_edge_at_close), 0) / closed.length
    : null;
  const positive = closed.filter((r) => toNum(r.clv_edge_at_close) > 0).length;
  const hitRate = closed.length ? (positive / closed.length) * 100 : null;

  setText("propsStatOpen", String(open.length));
  setText("propsStatClosed", String(closed.length));

  const cumEl = document.getElementById("propsStatCumEdge");
  if (cumEl) {
    cumEl.textContent = avgEdge === null ? "—" : fmtEdge(avgEdge);
    cumEl.className = "stat-value " + (avgEdge === null ? "" : edgeClass(avgEdge).replace("edge-", ""));
  }

  setText("propsStatHitRate", hitRate === null ? "—" : hitRate.toFixed(0) + "%");

  return { open, closed };
}

function renderPropsOpenTable(open) {
  const tbody = document.getElementById("propsOpenTableBody");
  const emptyNote = document.getElementById("propsOpenEmpty");
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
      return `
        <tr>
          <td class="name-cell">${escapeHtml(r.player_name) || "—"}</td>
          <td>${escapeHtml(r.team) || "—"}</td>
          <td>${escapeHtml(r.stat_type) || "—"}</td>
          <td>${escapeHtml(r.flagged_side) || "—"}</td>
          <td>${escapeHtml(r.platform) || "—"}</td>
          <td>${escapeHtml(r.line) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.game_start_time)}</td>
          <td>${renderRiskBadges(r)}</td>
        </tr>`;
    })
    .join("");
}

function renderPropsClosedTable(closed) {
  const tbody = document.getElementById("propsClosedTableBody");
  const emptyNote = document.getElementById("propsClosedEmpty");
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
          <td>${escapeHtml(r.closing_market_price) || "—"}</td>
          <td class="${edgeClass(edge)}">${fmtEdge(edge)}</td>
          <td>${fmtDate(r.closing_pulled_at)}</td>
        </tr>`;
    })
    .join("");
}

async function initProps() {
  try {
    const res = await fetch(PROPS_DATA_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const text = await res.text();
    const rows = parseCSV(text);

    const { open, closed } = renderPropsStats(rows);
    renderPropsOpenTable(open);
    renderPropsClosedTable(closed);

    overviewData.props.loaded = true;
    overviewData.props.rows = open.filter((r) => isFutureOrUnknown(r.game_start_time));
  } catch (err) {
    const el = document.getElementById("propsLoadError");
    if (el) el.hidden = false;
    console.error("Market_Betting frontend: failed to load props data.", err);
  }
}

// =======================================================================
// OVERVIEW — pools each track's currently-open, still-actionable rows
// (stashed into `overviewData` by each track's own init function above)
// into one ranked list. Each track's "edge" already lives on its own
// comparable scale (a model-probability edge as a fraction of $1, or
// arbitrage's net profit per $1 risked) — pooling and sorting on that
// raw number is a real, if imperfect, cross-track ranking, not a claim
// that the tracks carry identical risk per unit of edge. See the
// Overview tab's own panel note for that caveat, shown to the user
// directly rather than only in this comment.
// =======================================================================

const TRACK_META = {
  pickem: { label: "Pick'em", tagClass: "track-tag-pickem" },
  arb: { label: "Arbitrage", tagClass: "track-tag-arb" },
  weather: { label: "Weather", tagClass: "track-tag-weather" },
  politics: { label: "Politics", tagClass: "track-tag-politics" },
  props: { label: "Props", tagClass: "track-tag-props" },
};

function mapPickemForOverview(r) {
  return {
    track: "pickem",
    opportunity: [r.player_name, r.stat_type].filter(Boolean).join(" — ") || "—",
    side: r.flagged_side || "—",
    venue: r.platform || "—",
    edge: toNum(r.first_flagged_edge),
    edgeDisplay: fmtEdge(toNum(r.first_flagged_edge)),
    timing: fmtDate(r.game_start_time),
    longDated: false,
  };
}

function mapArbForOverview(r) {
  return {
    track: "arb",
    opportunity: r.title_a || r.opportunity_type || "—",
    side: r.opportunity_type || "—",
    venue: [r.platform_a, r.platform_b].filter(Boolean).join(" / ") || "—",
    edge: toNum(r.net_profit_per_dollar),
    edgeDisplay: fmtNetProfit(toNum(r.net_profit_per_dollar)) + "/$1",
    timing: "Live snapshot",
    longDated: false,
  };
}

function mapWeatherForOverview(r) {
  return {
    track: "weather",
    opportunity: [r.city_label, r.forecast_kind].filter(Boolean).join(" — ") || "—",
    side: r.flagged_side || "—",
    venue: "Kalshi",
    edge: toNum(r.first_flagged_edge),
    edgeDisplay: fmtEdge(toNum(r.first_flagged_edge)),
    timing: r.lead_days ? r.lead_days + "d out" : "—",
    longDated: false,
  };
}

function mapPoliticsForOverview(r) {
  const hours = toNum(r.hours_to_resolution);
  return {
    track: "politics",
    opportunity: [r.candidate_name, r.chamber].filter(Boolean).join(" — ") || "—",
    side: r.party || "—",
    venue: r.venue || "—",
    edge: toNum(r.first_flagged_edge),
    edgeDisplay: fmtEdge(toNum(r.first_flagged_edge)),
    timing: fmtHoursToResolution(hours),
    longDated: hours !== null && hours > 24 * 60,
  };
}

function mapPropsForOverview(r) {
  return {
    track: "props",
    opportunity: [r.player_name, r.stat_type].filter(Boolean).join(" — ") || "—",
    side: r.flagged_side || "—",
    venue: r.platform || "—",
    edge: toNum(r.first_flagged_edge),
    edgeDisplay: fmtEdge(toNum(r.first_flagged_edge)),
    timing: fmtDate(r.game_start_time),
    longDated: false,
  };
}

const OVERVIEW_MAPPERS = {
  pickem: mapPickemForOverview,
  arb: mapArbForOverview,
  weather: mapWeatherForOverview,
  politics: mapPoliticsForOverview,
  props: mapPropsForOverview,
};

const OVERVIEW_TOP_N = 10;

// Maps each track to the DOM ids of its own top-10 table on the Overview
// tab. Each track is ranked and rendered independently -- per the user's
// explicit correction, this replaced an earlier version that pooled all
// five tracks into one cross-ranked list.
const OVERVIEW_TABLES = {
  pickem: { body: "overviewPickemTableBody", empty: "overviewPickemEmpty" },
  arb: { body: "overviewArbTableBody", empty: "overviewArbEmpty" },
  weather: { body: "overviewWeatherTableBody", empty: "overviewWeatherEmpty" },
  politics: { body: "overviewPoliticsTableBody", empty: "overviewPoliticsEmpty" },
  props: { body: "overviewPropsTableBody", empty: "overviewPropsEmpty" },
};

function renderOverviewTrackTable(track, mapped) {
  const ids = OVERVIEW_TABLES[track];
  const tbody = document.getElementById(ids.body);
  const emptyNote = document.getElementById(ids.empty);
  if (!tbody || !emptyNote) return;

  const top = mapped.slice().sort((a, b) => b.edge - a.edge).slice(0, OVERVIEW_TOP_N);

  if (!top.length) {
    emptyNote.hidden = false;
    tbody.innerHTML = "";
    return;
  }
  emptyNote.hidden = true;

  tbody.innerHTML = top
    .map(
      (r) => `
        <tr>
          <td class="name-cell" title="${escapeAttr(r.opportunity)}">${escapeHtml(r.opportunity)}${
            r.longDated ? '<span class="long-dated-badge">Long-dated</span>' : ""
          }</td>
          <td>${escapeHtml(r.side)}</td>
          <td>${escapeHtml(r.venue)}</td>
          <td class="${edgeClass(r.edge)}">${r.edgeDisplay}</td>
          <td>${escapeHtml(r.timing)}</td>
        </tr>`
    )
    .join("");
}

function renderOverview() {
  const loadErrorEl = document.getElementById("overviewLoadError");

  const tracksLoaded = Object.values(overviewData).filter((t) => t.loaded);
  if (loadErrorEl) loadErrorEl.hidden = tracksLoaded.length > 0;

  let totalActionable = 0;
  let bestEdgeOverall = null;
  let bestEdgeDisplay = "—";
  let longDatedShown = 0;

  for (const [track, mapper] of Object.entries(OVERVIEW_MAPPERS)) {
    const rows = overviewData[track].rows || [];
    totalActionable += rows.length;

    const mapped = rows.map(mapper).filter((r) => r.edge !== null);
    renderOverviewTrackTable(track, mapped);

    const top = mapped.slice().sort((a, b) => b.edge - a.edge).slice(0, OVERVIEW_TOP_N);
    if (top.length && (bestEdgeOverall === null || top[0].edge > bestEdgeOverall)) {
      bestEdgeOverall = top[0].edge;
      bestEdgeDisplay = top[0].edgeDisplay;
    }
    longDatedShown += top.filter((r) => r.longDated).length;
  }

  setText("overviewStatTotal", String(totalActionable));
  setText("overviewStatTracksLive", `${tracksLoaded.length}/5`);
  setText("overviewStatTopEdge", bestEdgeDisplay);
  setText("overviewStatLongDated", String(longDatedShown));
}

// =======================================================================
// Tab navigation — plain show/hide, single page, no routing. Runs
// immediately since this script tag sits at the end of <body>, so the
// nav/tab-panel markup already exists in the DOM by the time this file
// executes.
// =======================================================================

function initTabs() {
  const buttons = document.querySelectorAll(".tab-btn");
  const panels = document.querySelectorAll(".tab-panel");

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const target = btn.getAttribute("data-tab");

      buttons.forEach((b) => b.classList.toggle("active", b === btn));
      panels.forEach((p) => {
        p.hidden = p.getAttribute("data-tab") !== target;
      });
    });
  });
}

async function init() {
  initTabs();

  // All tracks load independently and in parallel: a failure or an empty
  // result in one must never block or hide another track's real data.
  await Promise.allSettled([initPickem(), initArbitrage(), initWeather(), initPolitics(), initProps()]);

  renderOverview();

  setText("asOf", new Date().toLocaleString(undefined, {
    month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
  }));
}

init();
})();
