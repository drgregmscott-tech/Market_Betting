"""
Session 3.2 - Liquidity Check (Arbitrage Detection Logic)

WHAT THIS FILE IS
------------------
Answers one narrow question for detector.py: if a price gap is real and
clears fees, how much of it can actually be traded? Per Session 0.1's own
five per-venue evaluation criteria, a price gap that can't be filled at
meaningful size isn't a real arbitrage - it's a headline number nobody can
actually collect.

REAL BUG FOUND AND FIXED THIS SESSION, AGAINST LIVE DATA
-----------------------------------------------------------
The first version of this file used each venue's own reported `liquidity`
field (Kalshi: `liquidity_dollars`; Polymarket: `liquidity`) as the
fillable-size proxy for both venues. Pulling real, live data to validate
Session 3.2 (multiple real Kalshi weather markets - KXHIGHPHIL's several
strikes - and the real KXHOUSEMO5 down-ballot race) found that Kalshi's
`liquidity_dollars` field reads `"0.0000"` on every single real market
checked, even ones with substantial real size resting on the book (one
real KXHOUSEMO5 leg had 116.02 contracts resting at its best ask, and real
volume in the tens of thousands of contracts). This was not one stale
market - it was consistent and systematic across every Kalshi ticker
pulled. Using that field as-is would have made this function report every
Kalshi-involving opportunity as illiquid, regardless of how real or
fillable it actually was - the check itself wasn't wrong, but the input it
depended on for Kalshi was dead.

Polymarket's `liquidity` field, checked against the same real pull, is NOT
dead - real Polymarket markets return real, populated, non-zero liquidity
figures (e.g. $9,746.02 on the real MO-05 Republican market). So this fix
is asymmetric on purpose: Kalshi and Polymarket need genuinely different
treatment because they expose genuinely different real data, not because
of a stylistic preference for consistency.

THE FIX: USE KALSHI'S REAL ORDER-BOOK SIZE FIELDS INSTEAD
-----------------------------------------------------------
Kalshi's real market payload does carry usable size information -
`yes_ask_size_fp` and `yes_bid_size_fp` - confirmed live and populated
(non-zero) on every real market pulled this session. `schema_exchange.py`
and `ingest_kalshi.py` were extended this session (see those files' own
Session 3.2 notes) to capture these as `yes_ask_size` and `yes_bid_size`
on every normalized Kalshi row.

Which field applies depends on which SIDE of the market a leg is buying,
confirmed directly against real numbers (KXHOUSEMO5-26-R: yes_bid=0.19,
yes_ask=0.20, no_bid=0.80, no_ask=0.81 - and 0.80 = 1 - 0.20, 0.81 = 1 -
0.19, exactly the complementary relationship Kalshi's API produces for a
single binary market with one real order book):
- Buying YES at the quoted yes_ask consumes the resting size at that
  price - `yes_ask_size`.
- Buying NO at the quoted no_ask is mechanically the same action as
  SELLING YES at the complementary price (1 - no_ask, which equals
  yes_bid) - so the size actually available to a NO buyer is
  `yes_bid_size`, not a separate "no_ask_size" field, because Kalshi's
  API does not publish one; there is only one real order book per
  market, not two.

Polymarket does not expose an equivalent top-of-book size field in its
Gamma API market summary (only bid/ask price and a `liquidity` dollar
figure for the market as a whole). Since that `liquidity` figure IS real
for Polymarket, this function keeps using it there, converted to an
approximate contract count by dividing by the leg's own price - a named
approximation, not a precise order-book read, since Polymarket's own
reported number is itself a summary statistic, not a literal "contracts
resting at this exact price" count the way Kalshi's fields are.

WHY CONTRACTS, NOT DOLLARS, IS THE RIGHT UNIT TO COMPARE ACROSS LEGS
-----------------------------------------------------------------------
Both legs of a two-legged arbitrage must be filled 1-for-1 - buying 100
YES contracts on one venue and only 20 NO contracts on the other leaves
80 contracts unhedged, which is a directional bet, not an arbitrage.
Since every contract on both venues pays exactly $1.00 at settlement (the
whole point of a binary event contract), a contract count IS a dollar
notional amount (100 contracts = $100 of locked-in payout), so comparing
the two legs' fillable CONTRACT counts and taking the smaller one gives
the real fillable size of the position directly, in dollars, with no unit
conversion needed.

WHAT COUNTS AS "SUFFICIENT"
------------------------------
MIN_SUFFICIENT_LIQUIDITY_DOLLARS is a floor below which a flagged
opportunity is real but not worth the operational overhead of executing
two simultaneous trades across two venues for. This is a named, starting
value - not yet validated against a real filled trade - flagged here so
Greg can recalibrate it once a real trade's actual execution experience
exists to check it against, the same "no silent adjustments" pattern used
elsewhere in this project.
"""

from __future__ import annotations

from typing import Optional

MIN_SUFFICIENT_LIQUIDITY_DOLLARS = 50.0


def _to_float(value) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _kalshi_leg_contracts(row: dict, side: str) -> Optional[float]:
    """Real, precise fillable-contract count for a Kalshi leg, using the
    real size field that actually gets consumed by the trade - see this
    module's docstring for why NO uses yes_bid_size, not a separate
    no-side field Kalshi doesn't publish."""
    if side == "YES":
        return _to_float(row.get("yes_ask_size"))
    if side == "NO":
        return _to_float(row.get("yes_bid_size"))
    return None


def _polymarket_leg_contracts(row: dict, price: Optional[float]) -> Optional[float]:
    """Approximate fillable-contract count for a Polymarket leg. Real
    `liquidity` field (confirmed live and populated, unlike Kalshi's dead
    `liquidity_dollars`), divided by the leg's own price to estimate a
    contract count on the same footing as Kalshi's real per-contract
    figures. Named as an approximation, not a literal order-book read -
    Polymarket's Gamma API does not expose per-price-level size the way
    Kalshi's market object does."""
    liquidity = _to_float(row.get("liquidity"))
    if liquidity is None or price is None or price <= 0:
        return None
    return liquidity / price


def _leg_fillable_contracts(
    row: Optional[dict], side: Optional[str], platform: Optional[str], price
) -> tuple[Optional[float], str]:
    if row is None or side is None or platform is None:
        return None, "unknown_missing_leg_data"

    price_f = _to_float(price)

    if platform == "kalshi":
        return _kalshi_leg_contracts(row, side), "kalshi_real_order_book_size_field"
    if platform == "polymarket":
        return (
            _polymarket_leg_contracts(row, price_f),
            "polymarket_liquidity_dollars_divided_by_price_approximation",
        )
    return None, f"unknown_platform_{platform}"


def estimate_fillable_size(
    row_a: Optional[dict],
    side_a: Optional[str],
    platform_a: Optional[str],
    price_a,
    row_b: Optional[dict],
    side_b: Optional[str],
    platform_b: Optional[str],
    price_b,
) -> dict:
    """Returns a dict with the estimated fillable size (in dollars, which
    equals contracts for a $1-notional binary contract - see module
    docstring) for a two-legged position, which basis each leg's number
    came from, and whether the pair clears MIN_SUFFICIENT_LIQUIDITY_DOLLARS.

    `side_a`/`side_b` must be "YES" or "NO" - which side of that leg's
    market is actually being bought, not which venue is "leg A" in some
    other sense. `platform_a`/`platform_b` must be "kalshi" or
    "polymarket".

    If either leg's fillable count can't be determined at all (missing
    row, missing size field, unrecognized platform), this returns a
    fillable size of 0.0 and marks it explicitly UNKNOWN rather than
    assuming either "fully liquid" or "fully illiquid" - a missing number
    is not the same claim as a small number, and detector.py's output
    should not blur the two together.
    """
    contracts_a, basis_a = _leg_fillable_contracts(row_a, side_a, platform_a, price_a)
    contracts_b, basis_b = _leg_fillable_contracts(row_b, side_b, platform_b, price_b)

    if contracts_a is None or contracts_b is None:
        return {
            "fillable_size_dollars": 0.0,
            "basis": f"unknown_leg_a={basis_a}_leg_b={basis_b}",
            "sufficient": False,
        }

    fillable = min(contracts_a, contracts_b)
    binding_leg = "leg_a" if contracts_a <= contracts_b else "leg_b"

    return {
        "fillable_size_dollars": round(fillable, 2),
        "basis": f"leg_a={basis_a}_leg_b={basis_b}_min_{binding_leg}_binding",
        "sufficient": fillable >= MIN_SUFFICIENT_LIQUIDITY_DOLLARS,
    }
