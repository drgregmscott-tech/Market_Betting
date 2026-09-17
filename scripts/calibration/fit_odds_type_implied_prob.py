"""
Session 2.37/2.38 follow-up -- Re-Deriving PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB
From More Than One Real Observation

WHY THIS EXISTS
----------------
pickem_model.py's PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB (demon 52.83%, goblin
69.51%) is used as the real breakeven for every Demon/Goblin-tagged flag
in this project -- but Session 2.21's own docstring says outright it rests
on exactly ONE real observed entry (a 3-pick Power Play, 2 Standard legs +
1 special leg, re-tagged Demon vs. Goblin, from the user's own PrizePicks
account, 2026-09-14). Session 2.37's full audit found that MLB's demon/
goblin flags carry the track's largest apparent "edges" (30-45 percentage
points) -- but an edge measured against an unvalidated single-anecdote
constant is not distinguishable from "the constant is wrong." This script
exists to make that constant re-derivable the moment more real
observations exist, instead of staying pinned to the one anecdote
indefinitely.

METHOD
------
PrizePicks' own payout for an all-Standard N-leg entry is public and
already sourced (sizing_engine.py's PICKEM_ENTRY_PAYOUT). Treating each
leg's contribution to the entry multiplier as independent (the same
simplifying assumption Session 2.21 already made -- not proven, stated
here again, not hidden):

    M = 1 / (p_std^k_std * p_demon^k_demon * p_goblin^k_goblin)

Taking logs turns this into one linear equation per real observed entry:

    k_demon*log(p_demon) + k_goblin*log(p_goblin) = -log(M) - k_std*log(p_std)

p_std for that leg count is already known exactly (PICKEM_ENTRY_PAYOUT).
Two unknowns (p_demon, p_goblin) means at least 2 real observations are
needed to solve at all -- this project currently has exactly 2 (both from
the SAME real entry, just re-tagged), which is why Session 2.21 could only
solve, not validate, the two numbers. This script uses ordinary least
squares (numpy, no new dependency) so it keeps working, and starts
reporting a real residual/fit-quality check, the moment a 3rd+ genuinely
different observation (a different leg count, a different Standard/
special mix, or an all-special entry) is logged.

DATA SOURCE
-----------
data/pickem/demon_goblin_payout_observations.csv -- append a real row here
every time a real PrizePicks entry with at least one Demon or Goblin leg
is built (does not need to be placed for real money -- PrizePicks' entry
builder shows the live multiplier before an entry is submitted). Columns:
date_observed, platform (always "prizepicks" -- Underdog has no Demon/
Goblin concept), leg_count, standard_legs, demon_legs, goblin_legs,
observed_multiplier, notes.

MOST INFORMATIVE NEW OBSERVATIONS TO ADD (per this script's own
diagnostic below) -- combos NOT yet in the CSV, prioritized by how much
new, independent information they would add over what's already there:
- A leg count other than 3 (e.g. 2-pick 1 Standard + 1 Demon, or 4-pick
  2 Standard + 2 Demon) -- everything logged so far is leg_count=3.
- A mix with 2+ special legs in the same entry (e.g. 1 Demon + 1 Goblin
  together) -- tests whether the two constants combine multiplicatively
  the way this script assumes, not just individually.
- An all-special entry (e.g. 2-pick, both legs Demon) -- the cleanest
  possible read on p_demon alone, no Standard leg in the mix to average
  against.

USAGE
-----
python scripts/calibration/fit_odds_type_implied_prob.py
    Loads the CSV above, fits p_demon/p_goblin by least squares, prints
    the fit alongside the currently-hardcoded PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB
    values and a per-observation residual table, and states plainly
    whether there is yet enough independent data to trust the fit over
    the original anecdote. Writes nothing -- pickem_model.py's constant is
    updated by hand, deliberately, once a fit is judged trustworthy (this
    script does not auto-apply its output, matching this project's "no
    silent recalibration" posture elsewhere, e.g. fit_sigma_recalibration.py).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
OBS_PATH = BASE_DIR / "data" / "pickem" / "demon_goblin_payout_observations.csv"

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sizing"))
from sizing_engine import PICKEM_ENTRY_PAYOUT, breakeven_win_rate_per_leg  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB  # noqa: E402

# A real observation is only useful for the fit if it actually has a
# Demon or Goblin leg AND a known Standard-leg breakeven for its leg
# count. Below this many DISTINCT (leg_count, standard, demon, goblin)
# combos, the system has no redundancy at all -- it can only be solved
# exactly, never checked. 3 is the minimum for a single real residual to
# exist (2 unknowns, so 2 observations solve exactly with zero residual by
# construction; a 3rd is the first one that can actually disagree).
MIN_DISTINCT_COMBOS_FOR_A_REAL_CHECK = 3


def load_observations() -> pd.DataFrame:
    df = pd.read_csv(OBS_PATH)
    df = df.loc[df["platform"] == "prizepicks"].copy()
    df = df.loc[(df["demon_legs"] > 0) | (df["goblin_legs"] > 0)]
    return df


def fit(df: pd.DataFrame) -> dict:
    rows_a = []
    rows_b = []
    used = []
    for _, row in df.iterrows():
        leg_count = int(row["leg_count"])
        if leg_count not in PICKEM_ENTRY_PAYOUT["prizepicks"]:
            continue  # no sourced Standard payout for this leg count -- can't isolate p_std
        p_std = breakeven_win_rate_per_leg("prizepicks", leg_count)
        m = float(row["observed_multiplier"])
        k_std = int(row["standard_legs"])
        k_demon = int(row["demon_legs"])
        k_goblin = int(row["goblin_legs"])
        # k_demon*log(p_demon) + k_goblin*log(p_goblin) = -log(M) - k_std*log(p_std)
        rows_a.append([k_demon, k_goblin])
        rows_b.append(-np.log(m) - k_std * np.log(p_std))
        used.append(row)

    used_df = pd.DataFrame(used)
    A = np.array(rows_a, dtype=float)
    b = np.array(rows_b, dtype=float)

    distinct_combos = used_df[
        ["leg_count", "standard_legs", "demon_legs", "goblin_legs"]
    ].drop_duplicates()

    result = {
        "n_observations": len(used_df),
        "n_distinct_combos": len(distinct_combos),
        "used_df": used_df,
    }

    if len(A) < 2:
        result["status"] = "insufficient"
        result["message"] = (
            f"Only {len(A)} usable real observation(s) -- need at least 2 to solve for "
            "p_demon and p_goblin at all."
        )
        return result

    solution, residuals_sse, rank, _ = np.linalg.lstsq(A, b, rcond=None)
    log_p_demon, log_p_goblin = solution
    p_demon, p_goblin = float(np.exp(log_p_demon)), float(np.exp(log_p_goblin))

    predicted_b = A @ solution
    per_obs_residual = b - predicted_b
    used_df = used_df.assign(
        implied_log_target=b,
        predicted_log_target=predicted_b,
        residual=per_obs_residual,
    )

    result.update({
        "status": "fit",
        "p_demon": p_demon,
        "p_goblin": p_goblin,
        "rank": int(rank),
        "used_df": used_df,
        "trustworthy": len(distinct_combos) >= MIN_DISTINCT_COMBOS_FOR_A_REAL_CHECK,
    })
    return result


def main() -> None:
    df = load_observations()
    print(f"Loaded {len(df)} real Demon/Goblin observation(s) from {OBS_PATH}")
    print()
    print("Currently hardcoded in pickem_model.py (Session 2.21, one real anecdote):")
    for k, v in PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB.items():
        print(f"  {k}: {v:.4f}")
    print()

    result = fit(df)
    if result["status"] == "insufficient":
        print(result["message"])
        return

    print(f"Real observations used in fit: {result['n_observations']} "
          f"({result['n_distinct_combos']} distinct leg_count/mix combo(s))")
    print()
    print("Per-observation detail:")
    show_cols = [
        "date_observed", "leg_count", "standard_legs", "demon_legs", "goblin_legs",
        "observed_multiplier", "residual", "notes",
    ]
    print(result["used_df"][show_cols].to_string(index=False))
    print()

    print(f"Least-squares fit (matrix rank {result['rank']} of 2 unknowns):")
    print(f"  p_demon  = {result['p_demon']:.4f}  (currently hardcoded: "
          f"{PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB['demon']:.4f})")
    print(f"  p_goblin = {result['p_goblin']:.4f}  (currently hardcoded: "
          f"{PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB['goblin']:.4f})")
    print()

    if result["trustworthy"]:
        print(
            f"{result['n_distinct_combos']} distinct combos >= "
            f"{MIN_DISTINCT_COMBOS_FOR_A_REAL_CHECK} -- there is real redundancy here. "
            "Check the residual column above: small, evenly-scattered residuals support "
            "updating pickem_model.py's PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB by hand to this "
            "fit's values; a large or systematic residual on any one combo means the "
            "multiplicative-independence assumption itself may not hold and should be "
            "investigated before trusting this fit."
        )
    else:
        print(
            f"Only {result['n_distinct_combos']} distinct combo(s) logged -- fewer than the "
            f"{MIN_DISTINCT_COMBOS_FOR_A_REAL_CHECK} needed for a real residual check. This fit "
            "exactly reproduces the same 1-anecdote-derived numbers Session 2.21 already has "
            "(2 equations, 2 unknowns, zero redundancy) -- it is NOT yet new evidence. "
            "See this file's own docstring for which new combos to log next for the fastest "
            "real improvement (a different leg count; 2+ special legs together; an "
            "all-special entry)."
        )


if __name__ == "__main__":
    main()
