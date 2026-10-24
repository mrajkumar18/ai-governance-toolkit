# Significant-Change Checklist

**Purpose:** Stop live (or piloted) AI systems drifting out of the scope they were approved for. A change is either a **standard change** (normal change control) or a **significant change** (this checklist, plus gate re-entry).
**Applies to:** every registered system in Pilot or Live status, all tiers. **Owner:** Technical owner. **Control:** TK-16.

## 1. Is it a significant change?

Answer for the **proposed** state versus the state last approved at G1 / G2. **Any "Yes" = significant change.**

| # | Question | Yes / No |
|---|---|---|
| S1 | Model, model version or model provider changed, including a **vendor-side update, deprecation or silent version change** you have been notified of or have detected? | |
| S2 | System prompt, retrieval sources, guardrails or output filters changed in a way that alters behaviour, scope or tone? | |
| S3 | Agent tool allow-list, permissions, write access, spend or step limits changed, or a new agent added? | |
| S4 | Autonomy level increased (e.g., L1 to L2)? | |
| S5 | New data source or data category added (especially personal, special-category or children's data)? | |
| S6 | New user population, channel, business process, geography or volume band (e.g., crossing 10,000 individuals per year)? | |
| S7 | Hosting region, sub-processor or external model-provider data flow changed? | |
| S8 | Decision thresholds, score cut-offs or human-review rules changed? | |
| S9 | Retraining or fine-tuning on new data? | |
| S10 | Any Section A, B or C answer in the [questionnaire](../01-intake-and-risk-tiering/risk-tiering-questionnaire.md) would now change? | |

Cosmetic UI changes, bug fixes that do not alter model behaviour, and infrastructure patching are **standard changes**. If unsure, treat it as significant and let the Governance Lead downgrade it in writing.

## 2. Required steps for a significant change

- [ ] Re-run the questionnaire; record the new tier or confirm the old one (re-tiering decision) (TK-03)
- [ ] Update the register entry, [model card](../07-policy-and-templates/model-card-template.md) and, for agents, the agent register (TK-02, TK-14)
- [ ] Re-run the regression and evaluation suite tied to the new model / prompt / tool versions; compare with the baseline (TK-10, TK-16)
- [ ] Re-test what the change touches: bias (S5, S6, S8, S9), security and prompt-injection (S2, S3), kill switch and permissions (S3, S4), oversight effectiveness (S6, S8) (TK-09, TK-11, TK-12, TK-21)
- [ ] Refresh the impact assessment sections affected; refresh the transfer assessment (section 4A) for S5 or S7 (TK-05, TK-25)
- [ ] Re-check vendor terms for S1 or S7 (data use, retention, sub-processors) (TK-15)
- [ ] Update the monitoring plan thresholds if baselines moved (TK-17)
- [ ] Rollback plan and fallback confirmed before release (TK-16)
- [ ] Approval obtained at the level in section 3; logged in the [gate tracker](gate-tracker.csv) with gate = `CHG`

## 3. Which gate does it re-enter, and who approves?

| Situation | Re-enter | Approver |
|---|---|---|
| Tier increases, S4 (autonomy up), a new Section B domain, or a new special-category / children's data use (S5) | **G1 then G2** (full re-entry) | As for the new tier |
| Any other significant change (S1-S3, S5-S10) at Tier 1 | **G2** (targeted: only the checks the change touches) | Committee |
| Any other significant change at Tier 2 | **G2** (targeted) | Risk + InfoSec |
| Any other significant change at Tier 3 | Self-attested checklist | Governance Lead |

A change that raises autonomy to **L4** always needs Committee approval, whatever the tier.

## 4. Vendor-driven changes

Vendors may change models without your request. Treat a received change notice, or a detected behaviour shift, as S1 and start this checklist at once. Pin model versions where the provider allows it, and record in the monitoring plan how you will detect silent changes (for example, a canary question set run daily).

## Required evidence
Completed checklist · Re-tiering decision · Regression results (before / after) · Updated register and model card · Approval record · Rollback plan
