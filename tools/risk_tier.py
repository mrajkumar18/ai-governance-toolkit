#!/usr/bin/env python3
"""AI use-case risk tier calculator.

Implements the logic in 01-intake-and-risk-tiering/risk-tiering-questionnaire.md.

Usage:
    python risk_tier.py answers.json

answers.json format:
{
  "A": [],                   # stop checks answered Yes, e.g. ["A3"] (A1-A9)
  "B": ["B5"],               # high-risk domains answered Yes (B1-B9)
  "C": ["C1", "C2"],         # impact factors answered Yes (C1-C9)
  "autonomy": "L2",          # L1 | L2 | L3 | L4
  "production_write_access": false
}

This is an internal triage aid, not a legal determination. Legal should confirm
any Tier 0 or Tier 1 outcome and any borderline EU AI Act classification.
"""
import json
import sys

A_CODES = {f"A{i}" for i in range(1, 10)}
B_CODES = {f"B{i}" for i in range(1, 10)}
C_POINTS = {"C1": 3, "C2": 1, "C3": 2, "C4": 1, "C5": 1, "C6": 1, "C7": 1, "C8": 2, "C9": 1}
D_POINTS = {"L1": 0, "L2": 1, "L3": 2, "L4": 4}
TIER_NAMES = {0: "Prohibited / Stop", 1: "High", 2: "Medium", 3: "Low"}


def _check_codes(name, given, allowed):
    unknown = sorted(set(given) - set(allowed))
    if unknown:
        raise ValueError(f"unknown {name} codes: {unknown}")


def assess(ans: dict) -> dict:
    a = list(ans.get("A", []))
    b = list(ans.get("B", []))
    c = list(ans.get("C", []))
    level = ans.get("autonomy", "L1")
    if level not in D_POINTS:
        raise ValueError(f"autonomy must be one of {sorted(D_POINTS)}")
    _check_codes("A", a, A_CODES)
    _check_codes("B", b, B_CODES)
    _check_codes("C", c, C_POINTS)

    reasons = []
    l4 = level == "L4"

    if a:
        reasons.append(f"Stop checks triggered: {', '.join(sorted(a))}")
        reasons.append("Do not proceed. Escalate to Legal.")
        return {"tier": 0, "name": TIER_NAMES[0], "score": None, "reasons": reasons,
                "committee_approval_required": False, "legal_escalation": True}

    score = sum(C_POINTS[k] for k in set(c)) + D_POINTS[level]

    if b:
        tier = 1
        reasons.append(f"High-risk domain(s): {', '.join(sorted(b))}")
    elif score >= 8:
        tier = 1
        reasons.append(f"Score {score} >= 8")
    elif score >= 4:
        tier = 2
        reasons.append(f"Score {score} in 4-7")
    else:
        tier = 3
        reasons.append(f"Score {score} in 0-3")

    if level in ("L3", "L4") and ans.get("production_write_access") and tier > 2:
        tier = 2
        reasons.append("Agent floor: L3/L4 with production write access -> minimum Tier 2")

    if l4:
        reasons.append("L4 autonomy requires AI Governance Committee approval "
                       "(L4 scores 4 points on its own, so it is never Tier 3)")

    # Legal confirms every Tier 0 and Tier 1 outcome, however Tier 1 was reached
    # (high-risk domain OR score >= 8). Tier 0 returns early above.
    legal = tier == 1
    if legal and not b:
        reasons.append("Tier 1 reached by score: Legal to confirm classification")

    return {"tier": tier, "name": TIER_NAMES[tier], "score": score, "reasons": reasons,
            "committee_approval_required": l4 or tier == 1, "legal_escalation": legal}


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        result = assess(json.load(f))
    print(f"Tier {result['tier']} - {result['name']}")
    if result["score"] is not None:
        print(f"Score: {result['score']}")
    for r in result["reasons"]:
        print(f"  - {r}")
    print(f"Committee approval required: {'Yes' if result['committee_approval_required'] else 'No'}")
    print(f"Legal confirmation required: {'Yes' if result['legal_escalation'] else 'No'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
