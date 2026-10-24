# 04 · Lifecycle Gates

Five stage gates take an AI use case from idea to retirement. Each gate has entry criteria, a checklist, required evidence, approvers and three possible outcomes: **Approve**, **Approve with conditions**, **Reject / rework**.

| Gate | File | Question it answers |
|---|---|---|
| **G0** | [`gate-0-intake.md`](gate-0-intake.md) | Is this use case allowed, classified and registered? |
| **G1** | [`gate-1-design-approval.md`](gate-1-design-approval.md) | Is the design sound, lawful and risk-assessed? |
| **G2** | [`gate-2-pre-deployment.md`](gate-2-pre-deployment.md) | Is it tested, secured and ready to release? |
| **G3** | [`gate-3-operate-and-monitor.md`](gate-3-operate-and-monitor.md) | Is it still performing safely in production? |
| **G4** | [`gate-4-retirement.md`](gate-4-retirement.md) | Is it being retired cleanly? |
| + | [`agentic-addendum.md`](agentic-addendum.md) | Extra checks for agents (L2-L4) |
| + | [`significant-change-checklist.md`](significant-change-checklist.md) | When a change to a live system needs re-assessment, and which gate it re-enters |

## Approver matrix

| Gate | Tier 3 | Tier 2 | Tier 1 |
|---|---|---|---|
| G0 | Gov. Lead | Gov. Lead + Risk | Committee |
| G1 | Self-attest | Risk + Legal/DPO + InfoSec | Committee |
| G2 | Self-attest + Gov. Lead | Risk + InfoSec | Committee |
| G3 (review) | Annual | Quarterly | Monthly |
| G4 | Gov. Lead | Gov. Lead + Legal/DPO | Committee |

Record every decision in [`gate-tracker.csv`](gate-tracker.csv). Use `CHG` in the gate column for decisions taken under the [significant-change checklist](significant-change-checklist.md).

Control IDs (TK-xx) refer to the [control mapping matrix](../03-control-mapping/control-mapping-matrix.csv).
