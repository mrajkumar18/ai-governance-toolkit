# Gate 3: Operate and Monitor

**Purpose:** Keep the system safe and in scope **after** release. This is a recurring review, not a one-time approval.
**Cadence:** Tier 1 monthly · Tier 2 quarterly · Tier 3 annual.

## Review checklist
- [ ] Performance, accuracy and drift within thresholds (TK-17)
- [ ] Fairness metrics monitored; no adverse trend (TK-11, TK-17)
- [ ] Complaints, overrides and user feedback reviewed (TK-19)
- [ ] Human-oversight effectiveness reviewed: override rate, review time or time-to-override, and reviewer miss rate from sampled or seeded cases are inside the thresholds in the monitoring plan. Very low override rates with short review times are treated as a possible rubber-stamping signal (TK-09, TK-17)
- [ ] Incidents and near misses reviewed; actions on track (TK-18)
- [ ] Changes since last review passed change control; every change that meets the [significant-change criteria](significant-change-checklist.md) has a completed checklist, re-tiering decision and register update (TK-16)
- [ ] Vendor / model-provider changes assessed (new model version, terms, sub-processors) (TK-15)
- [ ] Access and permission review completed (TK-12)
- [ ] Logs retained and sampled (TK-13)
- [ ] Impact assessment still valid; refresh if scope changed (TK-05)
- [ ] Independent assurance: Tier 1 reviewed by Internal Audit or an independent party in the last 12 months; Tier 2 sampled (TK-22)
- [ ] Open exceptions reviewed; none past expiry ([exceptions process](../07-policy-and-templates/exception-and-risk-acceptance.md))
- [ ] Register current; next review date set (TK-02)
- [ ] For agents: permission, tool and action-ceiling review; kill-switch re-tested (TK-21)

## Triggers for an unscheduled review
Severity 1-2 incident · significant change (see [checklist](significant-change-checklist.md)) · new user population · regulatory change · sustained metric breach · significant complaint cluster.

## Outcomes
Continue · Continue with actions · Suspend (status = Suspended; tracked to resolution) · Retire (→ G4)
