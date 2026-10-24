# Changelog

Versioning: MAJOR for structural changes to the tiering method or control set, MINOR for new or materially changed content, PATCH for corrections.

## 1.1.0 · 2026-10-24

### Fixed
- **`tools/risk_tier.py`:** `legal_escalation` now covers every Tier 0 and Tier 1 outcome, including a Tier 1 reached by score (8 or more) with no Section B domain. Added tests, including the L4-never-Tier-3 rule.
- **Decision flow:** the diagram and the questionnaire now state that L4 is never Tier 3 (4 points on its own) and always needs Committee approval, and that Legal confirms every Tier 0 / Tier 1 outcome.
- **Regulatory status:** the Digital Omnibus on AI is now cited as adopted law (Regulation (EU) 2026/1744, in force 27 July 2026) instead of a political agreement. A9 (non-consensual intimate imagery and CSAM) is now an EU prohibition from 2 December 2026, and remains an internal prohibition regardless.
- **Sample data:** AI-003 now records `personal_data = Y` (staff names in status notes), which is what makes it Tier 2 under the toolkit's own scoring.
- **Control matrix:** `applies_to` values follow one documented grammar (see mapping notes).

### Added
- G1 check for general-purpose AI (GPAI) provider documentation, training-content summary and systemic-risk status; matching vendor-assessment questions 3.6-3.7; TK-15 now maps Arts. 51-55.
- [`significant-change-checklist.md`](04-lifecycle-gates/significant-change-checklist.md): what counts as a significant change and which gate it re-enters.
- Section 4A (cross-border transfer assessment) in the impact assessment template; vendor-assessment question 2.6.
- [`monitoring-plan-template.md`](07-policy-and-templates/monitoring-plan-template.md) and G2 / G3 checks for it.
- Human-oversight effectiveness measures (override rate, review time, reviewer miss rate) in G2, G3, the impact assessment, KPIs and TK-09 evidence.
- Explicit GenAI disclosure and labelling check and evidence at G2.
- Vendor ongoing-monitoring section (tiered cadence, audit-right requirement for Tier 1).
- Rating bands and acceptance authority for residual risk (example) in the exceptions process.
- [`docs/shadow-ai-discovery.md`](docs/shadow-ai-discovery.md) and registration / discovery language in the acceptable-use standard.
- Second impact-assessment example: short-form Tier 2 multi-agent GenAI system.
- Cross-reference table for registers and artefacts in the field definitions.
- Repo hygiene: `.gitignore`, GitHub Actions CI (tests, register validation, link check), `CONTRIBUTING.md`; `REGISTER_AS_OF` option for the validator.
- [`docs/showcase-walkthrough.md`](docs/showcase-walkthrough.md): a 20-30 minute demo script with commands, expected outputs and talking points.

## 1.0.0 · October 2026
Initial baseline.
