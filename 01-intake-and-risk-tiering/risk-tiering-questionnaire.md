# Risk-Tiering Questionnaire

Answer Yes / No. The method is deterministic so two assessors reach the same tier. The EU AI Act categories inform the structure, but the output is an **internal** tier, not a legal determination. Have Legal confirm classification for anything near Tier 1 or Tier 0.

## Section A: Stop checks (any "Yes" → Tier 0)

These correspond to practices prohibited under Article 5 of the EU AI Act (summarised). If any apply, **stop and escalate to Legal**.

| # | Question |
|---|---|
| A1 | Does the system use subliminal or purposefully manipulative techniques that materially distort behaviour and are likely to cause significant harm? |
| A2 | Does it exploit vulnerabilities of people due to age, disability or social/economic situation? |
| A3 | Does it score or classify people on social behaviour or personal traits, leading to detrimental treatment? |
| A4 | Does it assess the risk of a person committing a criminal offence based solely on profiling? |
| A5 | Does it build facial-recognition databases through untargeted scraping of images from the internet or CCTV? |
| A6 | Does it infer emotions of people in the workplace or education (other than for medical or safety reasons)? |
| A7 | Does it categorise people biometrically to infer sensitive attributes (e.g., race, political opinions, religion, sexual orientation)? |
| A8 | Does it perform real-time remote biometric identification in public spaces for law enforcement? |
| A9 | Does it generate or manipulate non-consensual sexual / intimate imagery of real, identifiable people ("nudifier" tools) or child sexual abuse material? *(Added to the EU AI Act's prohibited practices by the Digital Omnibus on AI, Regulation (EU) 2026/1744, published in the Official Journal on 24 July 2026; the new prohibitions apply in the EU from 2 December 2026. Prohibited under this toolkit's internal policy now, regardless of EU nexus or date. Legal to confirm scope and exemptions.)* |

## Section B: High-risk domains (any "Yes" → Tier 1)

Aligned to the EU AI Act's high-risk areas (Annex III and Annex I, summarised).

**Notes (Legal to confirm):**
- Systems that **profile natural persons** in these areas are always treated as high-risk. The Article 6(3) derogation (e.g., narrow procedural task, or improving the result of a prior human activity) is a documented **Legal** decision, never a self-assessment by the project team.
- Fraud detection is excluded from the EU credit-scoring category (B5) but is still scored in Sections C-D, and sector regulators (e.g., RBI model-risk and outsourcing expectations) may impose their own governance.
- High-risk **application dates** were postponed by the Digital Omnibus on AI (Regulation (EU) 2026/1744): 2 December 2027 for Annex III and 2 August 2028 for Annex I. The internal tier applies from today regardless of legal dates.

| # | Question |
|---|---|
| B1 | Biometric identification, biometric categorisation or emotion recognition (where permitted)? |
| B2 | Safety component in management of critical infrastructure (digital infrastructure, road traffic, water, gas, heating, electricity)? |
| B3 | Education or vocational training: admissions, evaluating learning outcomes, assigning level, proctoring? |
| B4 | Employment and worker management: recruitment, screening, promotion, termination, task allocation, performance monitoring? |
| B5 | Access to essential services: creditworthiness or credit scoring, life/health insurance risk and pricing, public-benefit eligibility, emergency call triage? |
| B6 | Law enforcement uses (evidence reliability, risk assessment of individuals, profiling)? |
| B7 | Migration, asylum or border control? |
| B8 | Administration of justice or democratic processes? |
| B9 | Safety component of a product covered by EU product-safety legislation (e.g., medical devices, machinery)? |

## Section C: Impact factors (scored)

| # | Question | Points if Yes |
|---|---|---|
| C1 | Does the output make, or materially influence, decisions about individuals with legal or similarly significant effect? | 3 |
| C2 | Does it process personal data? | 1 |
| C3 | Does it process special-category or children's data? | 2 |
| C4 | Is it customer- or public-facing? | 1 |
| C5 | Does it generate content (text, image, audio, video) seen by external parties? | 1 |
| C6 | Does it rely on a third-party or foundation model / vendor AI? | 1 |
| C7 | Does it affect more than 10,000 individuals per year? | 1 |
| C8 | Would errors be hard to reverse, or have material financial or safety consequences? | 2 |
| C9 | Does data cross borders or go to an external model provider? | 1 |

## Section D: Autonomy (scored)

Select one level. See [agent autonomy levels](agent-autonomy-levels.md).

| Level | Description | Points |
|---|---|---|
| L1 | AI suggests; a human decides and acts | 0 |
| L2 | AI acts only after human approval of each action | 1 |
| L3 | AI acts autonomously within guardrails; humans monitor and review exceptions | 2 |
| L4 | Fully autonomous, can delegate to or spawn other agents | 4 |

## Section E: Role and jurisdiction (recorded, not scored)

Record in the register; Legal confirms.

| Item | Question |
|---|---|
| E1 | Is there an EU nexus (placed on the EU market, deployed in the EU, or outputs used in the EU)? If **no**, the EU AI Act is a benchmark only. |
| E2 | Your role: **provider** (develops or has the system developed and places it on the market or puts it into service under its own name), **deployer**, **importer / distributor**, or a combination. |
| E3 | Do you substantially modify a third-party system, or put your name on it? That can make you the **provider** (Art. 25). |
| E4 | Does the system build on a **general-purpose AI** model? Obligations for the model sit with its provider; you remain responsible for your system and use. If yes, record the provider and model, and complete the GPAI checks at [G1](../04-lifecycle-gates/gate-1-design-approval.md) (provider documentation, training-content summary, systemic-risk status). |
| E5 | Which other regimes apply (DPDPA, GDPR, RBI / SEBI / IRDAI or other sector rules)? See [`docs/applicability-guide.md`](../docs/applicability-guide.md). |

## Scoring and result

1. Any **A = Yes** → **Tier 0 (Prohibited / Stop)**.
2. Else any **B = Yes** → **Tier 1 (High)**.
3. Else total = Section C + Section D points:
   - **8 or more → Tier 1 (High)**
   - **4 to 7 → Tier 2 (Medium)**
   - **0 to 3 → Tier 3 (Low)**
4. **Agent floor:** if autonomy is L3 or L4 **and** the agent can write to production systems, the minimum tier is **Tier 2**.
5. **L4 rule:** L4 requires explicit AI Governance Committee approval regardless of tier. L4 scores 4 points by itself, so an L4 system is never below Tier 2, with or without production write access.
6. **Legal confirmation:** Legal confirms every Tier 0 and every Tier 1 outcome, whether Tier 1 came from a Section B domain or from a score of 8 or more, and any borderline classification (`tools/risk_tier.py` reports this as `legal_escalation`).

Record the tier, the triggering answers and the assessor in the [register](../02-inventory/ai-system-register.csv).
