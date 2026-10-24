# Mapping Notes

## How to read the matrix
- References are at **clause / article / category** level, not sub-requirement level, so they stay stable and readable.
- A "-" means no direct equivalent, not that the topic is irrelevant. Often another framework covers it indirectly.
- `gate` shows where the control is normally verified (G0-G4; see [lifecycle gates](../04-lifecycle-gates/)).
- `applies_to` shows when the control is mandatory. Tier 3 uses a lighter subset. It follows one grammar: a **tier scope** (`All`, `Tier 1-2`, or `Agents`), then an optional **qualifier in square brackets** that narrows it (e.g., `All [personal data]`, `Tier 1-2 [L1-L3]`), and `+` to add a second scope (`Tier 1-2 + Agents` = Tier 1-2 systems plus every agent).
- Rows TK-25 (cross-border transfer) and TK-26 (IP and licensing) cover obligations that are easy to miss in AI programs.

## Framework notes
- **NIST AI RMF 1.0:** referenced by function and category (GOVERN, MAP, MEASURE, MANAGE). Agentic and generative specifics are in NIST AI 600-1 (Generative AI Profile).
- **ISO/IEC 42001:2023:** clauses 4-10 for the management system; Annex A control groups A.2-A.10 (policies, internal organisation, resources, impact assessment, life cycle, data, information for interested parties, use of AI, third parties).
- **EU AI Act (Regulation (EU) 2024/1689):** high-risk obligations (Arts. 9-15, 17, 26, 27, 43, 49, 72, 73), transparency (Art. 50), AI literacy (Art. 4) and GPAI provider obligations (Arts. 51-55, relevant to deployers through the information they are entitled to receive). Obligations differ for **providers** and **deployers**; check which you are. **Dates:** as amended by the Digital Omnibus on AI (Regulation (EU) 2026/1744, in force 27 July 2026), Annex III high-risk obligations apply from 2 December 2027 and Annex I from 2 August 2028; see the [applicability guide](../docs/applicability-guide.md) for the full list and verify against the Official Journal.
- **ISO/IEC 27001:2022:** Annex A control numbering (e.g., A 5.9 inventory, A 8.15 logging, A 8.32 change management).
- **GDPR:** Articles on principles (5), lawful basis (6), transparency (13-15), automated decisions (22), design (25), security (32), breach (33-34), DPIA (35).
- **India DPDPA 2023:** section references for notice and consent (s.4-7), fiduciary obligations (s.8), significant data fiduciaries (s.10) and data principal rights (s.11-14). The DPDP Rules 2025 (notified 13 November 2025) phase in obligations over roughly 18 months and set the breach-reporting procedure (Rule 7); **check the commencement date for each obligation.**
- **RBI FREE-AI (Aug 2025):** an advisory expert-committee report with 7 guiding principles ("sutras"), 6 pillars (Infrastructure, Policy, Capacity, Governance, Protection, Assurance) and 26 recommendations. The matrix maps to **pillars only**, because the recommendations are advisory until RBI adopts them through directions.

## Caveats
- Indicative mapping for practitioners, **not legal advice**.
- A single clause rarely satisfies a regulation by itself; use the matrix to find coverage and gaps, then read the source.
- Authorities' guidance, harmonised standards and implementation dates evolve. Review the matrix at least twice a year.

## Extending the matrix
Add a column for your own policy IDs, or for sector rules (e.g., banking supervisory guidance, healthcare). Keep one row per control theme.
