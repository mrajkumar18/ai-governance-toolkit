# Exceptions and Risk Acceptance

Sometimes a control cannot be met on time. Exceptions are allowed, but **visible, time-bound and owned**.

## Rules
1. Only the **risk owner** (a named business leader) may accept residual risk, within their authority.
2. **Tier 1** exceptions need AI Governance Committee approval. **Tier 2** needs Risk & Compliance plus the Governance Lead. **Tier 3** needs the Governance Lead.
3. **No exceptions** for Tier 0 (prohibited) uses, or for legal obligations. Legal decides what is a legal obligation.
4. Every exception has an **expiry date** (default 90 days) and a **remediation plan**.
5. Exceptions are logged in the register and reported to the Committee.

## Rating bands and acceptance authority (example)
Rate each risk as **likelihood (1-5) × impact (1-5)**, as in the [risk register](risk-register-template.csv). Record an **inherent** score (before controls) and a **residual** score (after controls that are implemented and evidenced). Residual must not exceed inherent, and a control that is planned but not yet working does not reduce the residual score.

| Residual score | Band | Who may accept | Conditions |
|---|---|---|---|
| 1-4 | Low | Risk owner | Review at the normal cycle |
| 5-9 | Medium | Risk owner + AI Governance Lead | Tier 1 systems also need Risk & Compliance |
| 10-14 | High | Risk owner + Risk & Compliance; Committee informed (Committee approves for Tier 1) | Time-bound (default 90 days) with a funded remediation plan |
| 15-25 | Critical | AI Governance Committee only | Do not go live unless compensating controls bring it below 15, or the Committee records a time-bound exception |

*Bands and authorities are examples. Set them with the Committee and your enterprise risk framework, and keep the two aligned.*

## Exception record
| Field | |
|---|---|
| Exception ID / system | |
| Control (TK-xx) not met | |
| Reason | |
| Risk if not mitigated | |
| Compensating controls | |
| Residual risk rating | |
| Expiry date | |
| Remediation plan and owner | |
| Risk owner (accepting) | |
| Approver(s) | |

## Review
A system whose residual risk in any category sits in the High or Critical band is reviewed at every G3, regardless of tier cadence. Expired exceptions automatically trigger a gate re-review. Repeated renewals are escalated.
