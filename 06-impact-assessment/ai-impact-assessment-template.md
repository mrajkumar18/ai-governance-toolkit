# AI Impact Assessment

| Field | |
|---|---|
| Assessment ID | IA-### |
| System (register ID) | AI-### |
| Risk tier | |
| Assessor(s) | |
| Date / version | |
| Reviewers (Risk, Legal/DPO, InfoSec) | |

*◐ = required for Tier 2 short form. All sections required for Tier 1.*

## 1. System description ◐
- Purpose and intended use:
- Out-of-scope / prohibited uses:
- Model type, provider, version; autonomy level:
- How outputs are used in a decision or process:
- Deployment context (channels, geography, volume):

## 2. Necessity and proportionality ◐
- Why is AI needed? What alternatives were considered?
- Is the AI use proportionate to the benefit?
- Data minimisation: what is the least data needed?

## 3. Stakeholders and affected people ◐
| Group | How affected | Vulnerability considerations |
|---|---|---|
| | | |

## 4. Data
- Sources, lawful basis / consent, special-category data:
- Quality, representativeness, known gaps and bias risks:
- Retention, third-party sharing:
- Cross-border transfer or external model provider? ☐ No ☐ Yes → complete section 4A

### 4A. Cross-border transfer assessment (TK-25)
*Complete whenever personal data (including prompts, files, embeddings or logs) leaves the home jurisdiction or goes to an external model provider. **Tier 3 systems that transfer personal data complete this section only** and use an IA-### reference in the register.*

| Item | Response |
|---|---|
| Destinations and processing locations (model inference, storage, logs, backups, support access, sub-processors) | |
| Data transferred (categories; prompts, uploads, outputs, embeddings, logs) and whether it is minimised or pseudonymised first | |
| Legal route, India (DPDPA s.16): is the destination restricted by Central Government notification? Does any stricter sectoral or other law apply? | |
| Legal route, EU / GDPR Chapter V (if EU data subjects): adequacy decision, standard contractual clauses, BCRs or an Art. 49 derogation; transfer impact assessment where SCCs are used | |
| Sector localisation rules (e.g., RBI payment-data storage, other regulator circulars) | |
| Provider terms: training on our data, retention, deletion, region pinning, zero-retention option | |
| Risk of access by foreign authorities and the supplementary measures chosen (encryption, key control, tokenisation, regional endpoint) | |
| **Result** | ☐ Permitted ☐ Permitted with conditions ☐ Not permitted. Legal / DPO sign-off: |

## 5. Potential impacts
Rate each: **Likelihood** (Low / Med / High) × **Severity** (Low / Med / High).

| Impact area | Description of potential impact | Likelihood | Severity | Rating |
|---|---|---|---|---|
| Fairness and discrimination | | | | |
| Privacy and data protection | | | | |
| Safety and physical / mental wellbeing | | | | |
| Economic / financial harm | | | | |
| Autonomy, dignity, manipulation | | | | |
| Access to services / rights | | | | |
| Transparency and ability to contest | | | | |
| Security and misuse | | | | |
| Societal / environmental | | | | |

## 6. Controls and mitigations ◐
| Risk | Control (TK-xx) | Owner | Status | Evidence |
|---|---|---|---|---|
| | | | | |

## 7. Human oversight
- Who oversees, with what competence and authority?
- What information does the overseer see? Can they override? Is override tested?
- Safeguards against automation bias:
- Effectiveness metrics and thresholds (override rate, review time or time-to-override, reviewer miss rate on seeded or sampled cases):

## 8. Transparency and redress
- How are people informed about AI use?
- How can they request explanation, human review or complaint resolution?

## 9. Monitoring plan
Summarise here, and attach the full [monitoring plan](../07-policy-and-templates/monitoring-plan-template.md) (Tier 1-2): metrics, thresholds, frequency, owners, triggers for suspension.

## 10. Residual risk and decision ◐
| Residual score (L × I) and band | Accepted by | Conditions |
|---|---|---|
| | | |

*Bands and acceptance authority: see [exceptions and risk acceptance](../07-policy-and-templates/exception-and-risk-acceptance.md).*

**Decision:** ☐ Proceed  ☐ Proceed with conditions  ☐ Redesign  ☐ Do not proceed

## 11. Review and sign-off
Next review date: ________

| Role | Name | Date |
|---|---|---|
| Business owner | | |
| Risk & Compliance | | |
| Legal / DPO | | |
| InfoSec | | |
| AI Governance Committee (Tier 1) | | |
