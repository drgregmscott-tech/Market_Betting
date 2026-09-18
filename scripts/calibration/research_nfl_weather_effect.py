"""
Session 2.46 -- Does weather move NFL player stats beyond the player's own norm?

WHAT: For every player-week 2020-2025 (REG), computes RESIDUAL = actual stat
minus the player's mean over his previous games that season (>= 3 games).
Then compares residuals by weather bucket, for OUTDOOR games only (roof ==
"outdoors" in nflverse's schedule file; dome/closed/open games are excluded
because weather cannot be trusted to act there).
Weather = nflverse `temp` (F) and `wind` (mph) columns (game-time observed).
HELD-OUT: buckets/slopes fit on seasons 2020-2023, checked on 2024-2025.
Research-only; writes nothing.
USAGE: python scripts/calibration/research_nfl_weather_effect.py
"""
from __future__ import annotations

import numpy as np
import pandas as pd

SCHEDULE_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
STATS_URL = "https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_{s}.parquet"
STATS = ["passing_yards", "completions", "attempts", "rushing_yards", "receiving_yards", "receptions", "fg_made", "passing_tds"]
MIN_PRIOR_MEAN = {"passing_yards": 60, "completions": 8, "attempts": 15, "rushing_yards": 10, "receiving_yards": 10,
                  "receptions": 1.5, "fg_made": 0.3, "passing_tds": 0.5}
WIND_BINS = [(0, 10), (10, 15), (15, 100)]
TEMP_BINS = [(-50, 32), (32, 50), (50, 120)]


def load() -> pd.DataFrame:
    sched = pd.read_csv(SCHEDULE_URL)
    sched = sched[(sched.season.between(2020, 2025)) & (sched.game_type == "REG")]
    sched = sched[sched.roof == "outdoors"][["season", "week", "home_team", "away_team", "temp", "wind"]].dropna(subset=["temp", "wind"])
    rows = []
    for s in range(2020, 2026):
        d = pd.read_parquet(STATS_URL.format(s=s))
        d = d[d.season_type == "REG"]
        rows.append(d)
    st = pd.concat(rows)
    st["team"] = st["team"].replace({"LAR": "LA", "LVR": "LV"})
    sched = sched.replace({"LAR": "LA"})
    keys = pd.concat([
        sched.rename(columns={"home_team": "team"}).drop(columns="away_team"),
        sched.rename(columns={"away_team": "team"}).drop(columns="home_team"),
    ])
    return st.merge(keys, on=["season", "week", "team"], how="inner")


def residuals(df: pd.DataFrame, stat: str, min_prior: int = 3) -> pd.DataFrame:
    d = df[["player_id", "season", "week", "temp", "wind", stat]].dropna().sort_values(["player_id", "season", "week"])
    g = d.groupby(["player_id", "season"])[stat]
    d["prior_mean"] = g.transform(lambda x: x.shift().expanding().mean())
    d["n_prior"] = g.cumcount()
    d = d[d.n_prior >= min_prior]
    d["resid"] = d[stat] - d["prior_mean"]
    return d


def main() -> None:
    df = load()
    print(f"outdoor player-weeks: {len(df)}")
    for stat in STATS:
        d = residuals(df, stat)
        d = d[d.prior_mean > MIN_PRIOR_MEAN[stat]]
        train, test = d[d.season <= 2023], d[d.season >= 2024]
        print(f"\n== {stat}  (train n={len(train)}, test n={len(test)}; mean resid by bucket, share of prior mean)")
        for name, col, bins in (("wind", "wind", WIND_BINS), ("temp", "temp", TEMP_BINS)):
            out = []
            for lo, hi in bins:
                cells = []
                for part in (train, test):
                    s = part[(part[col] >= lo) & (part[col] < hi)]
                    cells.append(f"{s.resid.sum()/s.prior_mean.sum():+.3f} (n={len(s)})" if len(s) else "n/a")
                out.append(f"[{lo},{hi}) train {cells[0]} | test {cells[1]}")
            print(f"  {name}: " + "  ;  ".join(out))
        for name, col in (("wind", "wind"), ("temp", "temp")):
            for lab, part in (("train", train), ("test", test)):
                x = part[col].to_numpy(float); y = (part.resid / part.prior_mean).to_numpy(float)
                slope = np.polyfit(x, y, 1)[0]
                se = np.std(y - np.polyval(np.polyfit(x, y, 1), x)) / (np.std(x) * np.sqrt(len(x)))
                print(f"  slope {name} {lab}: {slope:+.4f} per unit (t={slope/se:+.1f})")


if __name__ == "__main__":
    main()
