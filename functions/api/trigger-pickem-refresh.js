// Cloudflare Pages Function — Session 6.11.
//
// Lives at repo-root functions/, NOT frontend/functions/ -- confirmed the
// hard way (real 405s in production) that Cloudflare Pages Functions must
// sit alongside the build command's own working directory, which for this
// project's Pages build command (`mkdir -p frontend/data && cp ...`,
// referencing "frontend/data" as a relative path) is the repo root, even
// though "frontend" is the configured build OUTPUT directory. Moving this
// file into frontend/functions/ put it inside the output dir instead of
// the project root, so Cloudflare fell back to normal static routing and
// 405'd every POST instead of ever running this code.
//
// Backs the Pick'em tab's "Force new pull" button. A static page cannot
// safely call GitHub's Actions API itself (that would mean embedding a
// GitHub token in client-side JS, readable by anyone), so this function
// runs server-side, on Cloudflare's edge, holding the real token as a
// Pages secret the browser never sees. It does exactly two things:
//   1. Checks whether pickem_pipeline.yml is already queued or running,
//      so a click doesn't stack duplicate runs on top of one already in
//      flight.
//   2. If not, fires a workflow_dispatch to start a brand-new run right
//      now, instead of waiting for GitHub's own hourly cron trigger --
//      confirmed (2026-09-16) to actually fire several hours apart on
//      this repo, not hourly as scheduled; GitHub deprioritizes scheduled
//      triggers on low-activity repos and gives no way to fix that from
//      the workflow file itself.
//
// Requires one Pages secret, set in the Cloudflare dashboard (Pages
// project -> Settings -> Environment variables -> Production, encrypted):
//   GH_ACTIONS_TOKEN — a GitHub fine-grained personal access token scoped
//   to ONLY this repo, with "Actions: Read and write" permission and
//   nothing else. Never reuse a broader token here.

const OWNER = "drgregmscott-tech";
const REPO = "Market_Betting";
const WORKFLOW_FILE = "pickem_pipeline.yml";
const GITHUB_API = `https://api.github.com/repos/${OWNER}/${REPO}/actions/workflows/${WORKFLOW_FILE}`;

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json" },
  });
}

export async function onRequestPost({ env }) {
  const token = env.GH_ACTIONS_TOKEN;
  if (!token) {
    return json(
      { ok: false, reason: "not_configured", message: "GH_ACTIONS_TOKEN secret is not set on this Pages project." },
      500
    );
  }

  const ghHeaders = {
    Authorization: `Bearer ${token}`,
    Accept: "application/vnd.github+json",
    "User-Agent": "market-betting-pickem-refresh-button",
  };

  // Step 1: refuse to pile a new run on top of one already in flight.
  let runsRes;
  try {
    runsRes = await fetch(`${GITHUB_API}/runs?per_page=5`, { headers: ghHeaders });
  } catch (err) {
    return json({ ok: false, reason: "network_error", message: String(err) }, 502);
  }
  if (!runsRes.ok) {
    return json(
      { ok: false, reason: "github_error", message: `GitHub API returned HTTP ${runsRes.status} while checking run status.` },
      502
    );
  }
  const runsData = await runsRes.json();
  const inFlight = (runsData.workflow_runs || []).find(
    (r) => r.status === "queued" || r.status === "in_progress"
  );
  if (inFlight) {
    return json({
      ok: false,
      reason: "already_running",
      message: "A pick'em pipeline run is already in progress.",
      run_url: inFlight.html_url,
      started_at: inFlight.run_started_at,
    });
  }

  // Step 2: fire a brand-new run.
  const dispatchRes = await fetch(`${GITHUB_API}/dispatches`, {
    method: "POST",
    headers: { ...ghHeaders, "content-type": "application/json" },
    body: JSON.stringify({ ref: "main" }),
  });

  if (dispatchRes.status !== 204) {
    const bodyText = await dispatchRes.text().catch(() => "");
    return json(
      { ok: false, reason: "dispatch_failed", message: `GitHub API returned HTTP ${dispatchRes.status}: ${bodyText}` },
      502
    );
  }

  return json({ ok: true, message: "New pick'em pipeline run triggered." });
}
