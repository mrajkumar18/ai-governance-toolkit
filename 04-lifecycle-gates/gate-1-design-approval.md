# Gate 1: Design Approval

**Purpose:** Confirm the design is sound, lawful and its risks are understood **before significant build effort**.
**Applies to:** Tier 1-2 (Tier 3: self-attest items marked ★).

## Entry criteria
- [ ] G0 approved
- [ ] Architecture and data-flow diagram available

## Checklist
- [ ] ★ Intended purpose and limits of use documented (TK-14)
- [ ] AI risk assessment completed; risks have owners and treatments (TK-04)
- [ ] [Impact assessment](../06-impact-assessment/ai-impact-assessment-template.md) completed (full for Tier 1, short for Tier 2) (TK-05)
- [ ] Lawful basis / consent and notice defined for personal data (TK-07)
- [ ] ★ Data sources assessed for quality, representativeness, minimisation, licensing (TK-06)
- [ ] Human oversight designed: who reviews, with what authority and information (TK-09)
- [ ] ★ Vendor / model provider assessed; contract covers data use, retention, audit rights, incident notice (TK-15)
- [ ] ★ Cross-border transfers and external model-provider data flows assessed using section 4A of the [impact assessment template](../06-impact-assessment/ai-impact-assessment-template.md) (Tier 3: complete 4A only); localisation rules checked (TK-25)
- [ ] ★ **If built on a general-purpose AI (GPAI) model:** provider's technical documentation for downstream users obtained and reviewed (capabilities, limitations, intended and restricted uses); training-content summary and copyright policy confirmed; systemic-risk designation and Code of Practice status recorded; provider's usage terms checked against our use case. Gaps are logged as conditions (TK-15, TK-26)
- [ ] ★ Children's data identified; verifiable parental consent and tracking / targeting restrictions addressed where relevant (TK-07)
- [ ] ★ IP, copyright and licensing of data, models and outputs reviewed (TK-26)
- [ ] Legal role (provider / deployer) and applicable regimes confirmed by Legal; sector-regulator expectations reviewed (e.g., RBI)
- [ ] Security architecture reviewed: access control, secrets, network, data protection (TK-12)
- [ ] Logging and traceability design defined (TK-13)
- [ ] For agents: complete the [agentic addendum](agentic-addendum.md) design section (TK-21)
- [ ] Success metrics and acceptance thresholds defined, including fairness metrics where relevant (TK-10, TK-11)

## Required evidence
Design document · GPAI provider documentation and status record (if applicable) · [Risk register](../07-policy-and-templates/risk-register-template.csv) · [Model card (draft)](../07-policy-and-templates/model-card-template.md) · [Test plan](../07-policy-and-templates/evaluation-and-test-plan-template.md) · Impact assessment · Vendor assessment · Security review note · Metrics definition

## Outcomes
Approve · Approve with conditions · Rework
