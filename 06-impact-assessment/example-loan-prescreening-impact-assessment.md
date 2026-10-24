# AI Impact Assessment: Retail Loan Pre-Screening Assistant

> **Fictional example** for "Example Bank". Figures and thresholds are illustrative.

| Field | |
|---|---|
| Assessment ID | IA-001 |
| System (register ID) | AI-001 |
| Risk tier | **Tier 1 (High):** Section B5, creditworthiness evaluation of natural persons |
| Assessor(s) | Lead Data Scientist; AI Governance Lead |
| Date / version | 2026-09-15 / v1.0 |
| Reviewers | Risk & Compliance, Legal/DPO, InfoSec |

## 1. System description
- **Purpose:** Pre-screen retail loan applications and rank them for underwriter review, prioritising workload and flagging incomplete files.
- **Out of scope:** Automatic approval or rejection. Use for marketing, pricing or collections. Use of social-media or inferred sensitive data.
- **Model:** In-house gradient-boosted model v2.3; autonomy **L1** (advisory only).
- **How used:** Produces a score band (A-D) and top contributing factors shown to the underwriter. The underwriter decides.
- **Context:** Branch and digital channels, India; about 40,000 applications per year (illustrative).
- **Legal role and applicability:** Built in-house, so the bank is both **provider and deployer** of the system. No EU nexus, so the EU AI Act (Annex III 5(b): creditworthiness; Art. 27 FRIA) is used as a **benchmark**. DPDPA applies; RBI FREE-AI (advisory) and the bank's existing model-risk, outsourcing and fair-practice obligations apply.

## 2. Necessity and proportionality
- **Why AI:** Manual triage delays decisions and is inconsistent between underwriters.
- **Alternatives considered:** Rules-only scorecard (lower accuracy on thin-file applicants); no triage (status quo).
- **Proportionality:** Advisory use with human decision is proportionate. Fully automated decisions were **rejected** at design.
- **Minimisation:** Uses application, income and bureau fields only; excludes religion, caste, gender, marital status and pin-code-level proxies.

## 3. Stakeholders and affected people
| Group | How affected | Vulnerability considerations |
|---|---|---|
| Loan applicants | Speed and outcome of credit decision | First-time borrowers and thin-file applicants may be disadvantaged |
| Underwriters | Workflow; risk of over-reliance | Automation bias |
| Women, self-employed, rural applicants | Possible indirect bias | Under-represented in historical data |

## 4. Data
- **Sources:** Historical applications and repayment outcomes (5 years), bureau data, application data.
- **Lawful basis:** Consent at application (DPDPA s.6) with an itemised notice covering AI-assisted pre-screening; legitimate uses under s.7 only where they clearly apply. Legal to confirm.
- **Quality / bias risks:** Historical approvals may reflect past human bias; limited data for thin-file and self-employed segments. Fairness testing uses lawful, minimised attributes or proxies (e.g., self-declared or segment-level data); protected attributes are not used as model inputs.
- **Retention / transfer:** Retained per credit-record policy; hosted in India; no external model provider.

## 5. Potential impacts
| Impact area | Description | Likelihood | Severity | Rating |
|---|---|---|---|---|
| Fairness and discrimination | Score bands disadvantage certain groups through proxies | Medium | High | **High** |
| Privacy and data protection | Over-collection or misuse of bureau data | Low | High | Medium |
| Economic / financial harm | Wrongly low band delays or loses a deserving applicant | Medium | Medium | Medium |
| Access to services / rights | Applicants unaware AI was involved; cannot contest | Medium | High | **High** |
| Transparency and contest | Underwriters cannot explain factors | Medium | Medium | Medium |
| Security and misuse | Insider manipulation of inputs or score | Low | High | Medium |
| Autonomy / automation bias | Underwriters rubber-stamp score bands | Medium | High | **High** |

## 6. Controls and mitigations
| Risk | Control | Owner | Status | Evidence |
|---|---|---|---|---|
| Bias via proxies | TK-11 Bias testing across gender, region, employment type; remove proxy features; set parity thresholds | Lead Data Scientist | Done | Bias report v1.2 |
| Fairness drift | TK-17 Monthly fairness metrics with alert thresholds | AI Engineering | Done | Dashboard config |
| Lack of contestability | TK-19 Applicant notice of AI-assisted screening; right to human review and explanation; complaint SLA | Head of Retail Lending | In progress | Notice text; SLA draft |
| Automation bias | TK-09 Underwriters must record their own rationale; random score-hidden sampling; override-rate monitoring | Head of Retail Lending | Done | Procedure SOP-17 |
| Explainability | TK-08 Top-factor explanations shown; model card published internally | Lead Data Scientist | Done | Model card |
| Data protection | TK-06 / TK-07 Minimisation review; lawful-basis record; DPIA completed | DPO | Done | DPIA-001 |
| Security | TK-12 / TK-13 Role-based access; immutable logs of inputs, scores and overrides | InfoSec | Done | Access matrix; log sample |
| Model change | TK-16 Change control with re-test and re-tiering | AI Engineering | Done | Change policy |

## 7. Human oversight
- **Overseer:** Trained underwriters with authority to disregard or override any score band.
- **Information shown:** Band, top factors, data completeness flag, confidence note.
- **Override:** Always possible; overrides are logged with a reason. Override rate is monitored (very low override rates trigger review for automation bias).
- **Automation-bias safeguards:** Periodic score-hidden reviews and calibration sessions.

## 8. Transparency and redress
- Applicants are told AI assists screening and that a human makes the decision.
- On request, applicants get a plain-language explanation of key factors and a human re-review.
- Complaints routed to the grievance officer with a defined SLA.

## 9. Monitoring plan
| Metric | Threshold (illustrative) | Frequency | Owner |
|---|---|---|---|
| Rank-order accuracy (e.g., Gini / AUC) | Drop > 3 points vs baseline | Monthly | Lead Data Scientist |
| Approval-rate parity across monitored groups | Gap beyond agreed tolerance | Monthly | Risk & Compliance |
| Underwriter override rate | < 3% or > 40% | Monthly | Head of Retail Lending |
| Data drift (PSI) | PSI > 0.2 on key features | Weekly | AI Engineering |
| Complaints citing AI | Any cluster of 3+ in a month | Monthly | Grievance officer |

**Suspension triggers:** sustained threshold breach, Severity 1-2 incident, or regulatory direction.

## 10. Residual risk and decision
| Residual risk level | Accepted by | Conditions |
|---|---|---|
| Medium | Head of Retail Lending; AI Governance Committee | Contest process live before go-live; first quarterly fairness review to Committee |

**Decision:** ☒ Proceed with conditions

## 11. Review and sign-off
Next review date: 2026-12-15 (quarterly), and on any material change.

| Role | Name | Date |
|---|---|---|
| Business owner | Head of Retail Lending | 2026-09-15 |
| Risk & Compliance | (name) | 2026-09-15 |
| Legal / DPO | (name) | 2026-09-15 |
| InfoSec | (name) | 2026-09-15 |
| AI Governance Committee | (chair) | 2026-09-16 |
