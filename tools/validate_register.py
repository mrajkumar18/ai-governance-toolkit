#!/usr/bin/env python3
"""Validate the AI system register (and optionally the agent register).

Usage:
    python validate_register.py ai-system-register.csv [agent-register.csv]
Exit code 0 = clean, 1 = findings.

Set REGISTER_AS_OF=YYYY-MM-DD to evaluate overdue reviews as of a fixed date
(used by CI so the fictional sample data stays valid). Defaults to today.
"""
import csv
import os
import sys
from datetime import date

REQUIRED = ["system_id", "name", "type", "business_owner", "technical_owner", "status",
            "risk_tier", "eu_ai_act_role", "autonomy_level", "personal_data",
            "cross_border_transfer", "last_review_date", "next_review_date"]
STATUSES = {"Idea", "Design", "Pilot", "Live", "Suspended", "Retired"}
ACTIVE = {"Pilot", "Live"}
TIERS = {"0", "1", "2", "3"}
LEVELS = {"L1", "L2", "L3", "L4"}
YN = {"Y", "N"}
ROLES = {"Provider", "Deployer", "Provider+Deployer", "Importer/Distributor",
         "Benchmark only (no EU nexus)"}
LEVEL_NUM = {"L1": 1, "L2": 2, "L3": 3, "L4": 4}


def today():
    as_of = os.environ.get("REGISTER_AS_OF", "").strip()
    return date.fromisoformat(as_of) if as_of else date.today()


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_date(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def check_systems(rows):
    out, seen = [], set()
    for i, r in enumerate(rows, start=2):
        sid = r.get("system_id") or f"row{i}"
        for k in REQUIRED:
            if not (r.get(k) or "").strip():
                out.append(f"{sid}: missing required field '{k}'")
        if sid in seen:
            out.append(f"{sid}: duplicate system_id")
        seen.add(sid)
        for field, allowed in (("status", STATUSES), ("risk_tier", TIERS), ("autonomy_level", LEVELS),
                               ("eu_ai_act_role", ROLES), ("personal_data", YN), ("cross_border_transfer", YN)):
            v = (r.get(field) or "").strip()
            if v and v not in allowed:
                out.append(f"{sid}: invalid {field} '{v}'")
        tier, status, level = r.get("risk_tier"), r.get("status"), r.get("autonomy_level")
        if tier in ("1", "2") and not (r.get("impact_assessment_ref") or "").strip():
            out.append(f"{sid}: Tier {tier} requires impact_assessment_ref")
        if (tier == "1" or level == "L4") and status in ACTIVE and not (r.get("committee_approval_ref") or "").strip():
            out.append(f"{sid}: Tier 1 / L4 system in {status} requires committee_approval_ref")
        if tier == "0" and status in ACTIVE:
            out.append(f"{sid}: Tier 0 system must not be Pilot/Live")
        if r.get("personal_data") == "Y" and r.get("cross_border_transfer") == "Y" and not (r.get("impact_assessment_ref") or "").strip():
            out.append(f"{sid}: personal data crossing borders needs an impact/transfer assessment reference")
        last, nxt = parse_date(r.get("last_review_date", "")), parse_date(r.get("next_review_date", ""))
        for name, d in (("last_review_date", last), ("next_review_date", nxt)):
            if (r.get(name) or "").strip() and d is None:
                out.append(f"{sid}: {name} is not YYYY-MM-DD")
        if last and nxt and nxt <= last:
            out.append(f"{sid}: next_review_date is not after last_review_date")
        if nxt and nxt < today() and status in ACTIVE:
            out.append(f"{sid}: review overdue (next_review_date {nxt})")
    return out, {r.get("system_id"): r for r in rows}


def check_agents(agents, systems):
    out = []
    parents_with_agents = set()
    for i, a in enumerate(agents, start=2):
        aid = a.get("agent_id") or f"row{i}"
        for k in ("agent_id", "parent_system_id", "autonomy_level", "tools_allowed", "permissions",
                  "max_steps_per_task", "kill_switch_owner", "log_location"):
            if not (a.get(k) or "").strip():
                out.append(f"{aid}: missing required field '{k}'")
        pid = a.get("parent_system_id")
        parents_with_agents.add(pid)
        parent = systems.get(pid)
        if not parent:
            out.append(f"{aid}: parent_system_id '{pid}' not in system register")
            continue
        al, pl = a.get("autonomy_level"), parent.get("autonomy_level")
        if al in LEVEL_NUM and pl in LEVEL_NUM and LEVEL_NUM[al] > LEVEL_NUM[pl]:
            out.append(f"{aid}: autonomy {al} exceeds parent system level {pl}")
        if al in ("L2", "L3", "L4") and not (a.get("actions_requiring_approval") or "").strip():
            out.append(f"{aid}: define actions_requiring_approval (use 'None (read-only)' if applicable)")
        if al in ("L3", "L4") and not (a.get("last_red_team_date") or "").strip():
            out.append(f"{aid}: L3/L4 agent requires a red-team date")
    for sid, s in systems.items():
        if (s.get("type") or "").startswith("Agent") and s.get("status") in ACTIVE and sid not in parents_with_agents:
            out.append(f"{sid}: agent-type system has no entries in the agent register")
    return out


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__)
        return 2
    systems_rows = read(argv[1])
    findings, systems = check_systems(systems_rows)
    if len(argv) == 3:
        findings += check_agents(read(argv[2]), systems)
    if findings:
        print(f"{len(findings)} finding(s):")
        for x in findings:
            print(" -", x)
        return 1
    print(f"OK: {len(systems_rows)} system(s) validated, no findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
