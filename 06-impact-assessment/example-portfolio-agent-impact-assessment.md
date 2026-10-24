# AI Impact Assessment (Short Form): Portfolio Risk Monitoring Agent

> **Fictional example** for "Example Bank" (short form for Tier 2: sections marked ◐ in the template, plus transfer and oversight notes). Figures and thresholds are illustrative.

| Field | |
|---|---|
| Assessment ID | IA-003 |
| System (register ID) | AI-003 (agents AG-003-1 to AG-003-3) |
| Risk tier | **Tier 2 (Medium):** score 4 = C2 personal data (staff names in status notes) 1 + C6 vendor LLM 1 + C9 external model provider 1 + L2 autonomy 1. No Section A or B answer; not customer-facing. No agent floor (L2). |
| Assessor(s) | AI Engineering Lead; AI Governance Lead |
| Date / version | 2026-10-01 / v1.0 |
| Reviewers | Risk & Compliance, Legal/DPO, InfoSec |

## 1. System description ◐
- **Purpose:** Read programme status data, detect RAG-status drift against agreed criteria, and draft escalation notes for programme managers.
- **Out of scope:** Sending any message, changing any status field, assessing individual staff performance, use on projects containing customer data.
- **Model and autonomy:** Three orchestrated LLM agents (LangGraph) using a vendor LLM; each agent is **L2** (acts only after human approval of each outward action). Registered in the agent register as AG-003-1 (Status Collector, read-only), AG-003-2 (Drift Analyst, read-only), AG-003-3 (Escalation Drafter, drafts only).
- **How outputs are used:** Drafts appear in a review queue. A programme manager edits and sends, or discards.
- **Context:** Internal PMO, India; about 60 programmes; roughly 100 drafts per week (illustrative).
- **Legal role:** Built in-house on a third-party LLM API: provider and deployer of the system; the vendor is the GPAI model provider. No EU nexus, so the EU AI Act is a benchmark only (Art. 50 transparency logic applied to drafts voluntarily).

## 2. Necessity and proportionality ◐
- **Why AI:** Status drift is found late because reports are read manually; drafts of routine escalation notes consume programme-manager time.
- **Alternatives considered:** Rules-only RAG thresholds (cannot read free-text status notes); more reporting meetings (cost, delay).
- **Proportionality:** Read-only data access, human approval of every outbound message, and no personal or customer data in prompts.
- **Minimisation:** Only status fields and free-text status notes are read. The system does process staff names internally (register: `personal_data = Y`), but names and e-mail addresses are replaced by programme-role tokens **before** any text is sent to the vendor LLM, so no personal data leaves the organisation. Legal/DPO to re-confirm if tokenisation changes.

## 3. Stakeholders and affected people ◐
| Group | How affected | Vulnerability considerations |
|---|---|---|
| Programme managers | Receive AI-drafted escalations; may over-trust drafts | Automation bias; blame if an inaccurate draft is sent |
| Delivery teams named in status notes | May be implicated by an inaccurate escalation | No performance or HR use permitted |
| Executives reading escalations | Decisions on programme support | Misleading summaries |

## 4A. Cross-border transfer assessment (TK-25)
| Item | Response |
|---|---|
| Destinations / processing | Vendor LLM endpoint in a regional data centre outside India (per vendor terms); orchestration and logs in private cloud, India |
| Data transferred | Tokenised status text and RAG criteria; no names, e-mail addresses or customer data |
| DPDPA s.16 | Personal data is tokenised before leaving, so none is transferred; destination not restricted by current notifications (Legal to recheck each review) |
| GDPR Chapter V | Not applicable (no EU data subjects; no personal data transferred) |
| Sector localisation | No regulated customer or payment data in scope; confirmed with Compliance |
| Provider terms | No training on our data; 30-day retention with zero-retention option requested (condition below) |
| Supplementary measures | Tokenisation before send; encrypted transit; API keys per agent, rotated |
| **Result** | ☒ Permitted with conditions. Sign-off: Legal/DPO |

## 6. Controls and mitigations ◐
| Risk | Control (TK-xx) | Owner | Status | Evidence |
|---|---|---|---|---|
| Prompt injection via status notes (R-003) | TK-12 / TK-21 Treat notes as untrusted data; instructions only from system prompt; output validation; injection tests in G2 | AI Engineering Lead | Done | Red-team report 2026-09-20 |
| Excessive agency | TK-21 Tool allow-list per agent; read-only except draft tools; sending is not a tool | AI Engineering Lead | Done | Agent register; permission matrix |
| Wrong or invented escalation | TK-10 Groundedness test against source status; drafts show the source fields they used | AI Engineering Lead | Done | Eval suite EVAL-003-C |
| Automation bias | TK-09 Programme manager edits every draft; monitor draft acceptance-without-edit rate and review time | Head of PMO | In progress | Monitoring plan v1.0 |
| Unlabelled AI content | TK-08 / TK-24 Each draft carries an "AI-drafted, review before sending" label; final sender is the named human | AI Engineering Lead | Done | Screenshot; label text |
| Vendor model change (R-004 pattern) | TK-15 / TK-16 Pin model version; daily canary question set; significant-change checklist on any vendor notice | AI Engineering Lead | Done | Canary results; change log |
| Data transfer | TK-25 Tokenisation and provider terms per section 4A | DPO | Done | Section 4A |
| Runaway cost / loops | TK-21 Step, rate and spend limits; kill switch tested and timed | AI Engineering Lead | Done | Kill-switch record |

## 7. Human oversight (effectiveness metrics)
- **Overseer:** the programme manager who owns the programme, with authority to discard or edit any draft; sending is manual.
- **Effectiveness thresholds (illustrative):** draft acceptance-without-edit rate between 20% and 80% (outside the range triggers review); median review time above 20 seconds; reviewer miss rate on monthly seeded drafts (known-wrong escalations) below 10%.

## 10. Residual risk and decision ◐
| Residual score (L × I) and band | Accepted by | Conditions |
|---|---|---|
| 4 (Low) for prompt injection (R-003); highest other residual 6 (Medium) | Head of PMO; AI Governance Lead | Zero-retention option confirmed with vendor before moving from Pilot to Live; first monthly oversight-metrics review to Risk & Compliance |

**Decision:** ☒ Proceed with conditions (Pilot)

## 11. Review and sign-off
Next review date: 2027-01-01 (quarterly), on any significant change, and on any vendor model-change notice.

| Role | Name | Date |
|---|---|---|
| Business owner | Head of PMO | 2026-10-01 |
| Risk & Compliance | (name) | 2026-10-01 |
| Legal / DPO | (name) | 2026-10-01 |
| InfoSec | (name) | 2026-10-01 |
