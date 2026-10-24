# AI Incident Playbook

## What counts as an AI incident
Any event where an AI system, or an agent's actions, causes or could cause harm, breaches policy or law, or behaves outside its approved scope. Examples:
- Harmful, biased or unlawful outputs or decisions
- Confidential or personal data exposed through prompts, outputs, logs or a vendor
- Prompt injection or jailbreak leading to unauthorised behaviour
- Agent takes an unapproved or irreversible action
- Material model drift or accuracy failure
- Vendor model change that alters behaviour
- Misuse by users, or unapproved ("shadow") AI use

## Roles
| Role | Duty |
|---|---|
| **Incident Commander** (AI Governance Lead or delegate) | Runs the response, owns decisions and communication |
| **Technical Lead** | Contains, diagnoses and fixes |
| **Business Owner** | Assesses impact; owns customer and stakeholder decisions |
| **Legal / DPO** | Determines notification duties across all clocks; advises on regulators |
| **InfoSec** | Security forensics, access revocation, threat assessment |
| **Communications** | Internal and external messaging |

## Response phases

### 1. Detect and report
Sources: monitoring alerts, user complaints, staff reports, vendor notices, audit, red-team. **Anyone can report**; log it immediately in the [incident log](incident-log-template.csv).

### 2. Triage (target: 4 hours for Sev 1-2)
- Confirm it is real; identify the system in the [register](../02-inventory/ai-system-register.csv)
- Assign severity per the [matrix](severity-matrix.md)
- Appoint the Incident Commander; open a war room for Sev 1-2

### 3. Contain
Pick the least disruptive action that stops harm:
- Switch to human-only / fallback process
- **Pause the agent or trigger the kill switch**; revoke tool credentials
- Disable the affected feature, tighten guardrails, roll back model / prompt / data version
- Block a malicious input source
- **Preserve evidence first:** logs, prompts, outputs, model and prompt versions, configuration

### 4. Investigate
- Reconstruct the timeline from traces (inputs → plan → tool calls → outputs → actions)
- Identify root cause: data, model, prompt, tool, permission, process, vendor, misuse
- Determine **who and what was affected**, over what period, and whether decisions need to be reviewed or reversed

### 5. Notify
Legal/DPO decides, using the clocks below. Notify affected individuals when required or appropriate.

### 6. Recover
- Fix and test; run regression and relevant red-team cases
- Return to service through an expedited **G2** check
- Remediate affected people (correct decisions, restore data, apologise where appropriate)
- Update monitoring so the same failure is detected sooner

### 7. Learn
Complete a [blameless post-incident review](post-incident-review-template.md) within 10 business days (Sev 1-2). Update controls, tests, the risk register and training. Re-tier the system if needed.

## Notification clocks (check with Legal; indicative, last reviewed October 2026)

| Regime | Trigger | Indicative clock |
|---|---|---|
| **India DPDPA** s.8(6) and Rule 7 | Personal data breach | Inform affected Data Principals and give the Data Protection Board an **initial intimation without delay**; **detailed report to the Board within 72 hours** of becoming aware (extendable by the Board on written request) |
| **CERT-In** (India) | Specified cyber incidents, including data breaches | Report within **6 hours** of noticing, under CERT-In directions (check current directions and scope) |
| **Sector regulators** (e.g., RBI for banks and NBFCs) | Cyber incidents, outsourcing / third-party failures, model failures with customer impact | Per applicable circulars; confirm with the compliance function |
| **GDPR** Art. 33 / 34 | Personal data breach (EU data subjects) | Supervisory authority within **72 hours** of awareness where required; data subjects without undue delay if high risk |
| **EU AI Act** Art. 73 / Art. 26(5) | Serious incident involving a high-risk AI system (providers report; deployers inform the provider first) | Generally within **15 days** of awareness; 2 days for widespread infringement or critical-infrastructure disruption; 10 days in the event of death. **Note:** high-risk obligations were postponed by the Digital Omnibus on AI (Regulation (EU) 2026/1744) to 2 December 2027 (Annex III) and 2 August 2028 (Annex I); confirm the date that applies to you |
| **Contracts** | Customer, bank-partner and vendor terms | Per contract; vendors should be required to notify you promptly |

Run these clocks **in parallel**. The earliest deadline (often CERT-In's 6 hours) drives the first call to Legal. These are indicative and not legal advice. Verify against current official texts.

## Agent-specific containment checklist
- [ ] Kill switch executed and confirmed
- [ ] Agent credentials and API keys revoked / rotated
- [ ] In-flight tasks listed; actions already taken enumerated from the trace
- [ ] Irreversible actions identified and compensating actions planned
- [ ] Memory / vector store checked for poisoned content; quarantined if needed
- [ ] Downstream systems and data stores reviewed for unwanted changes

## Exercises
Run a tabletop at least twice a year. Suggested scenarios: a prompt-injection leak via a retrieved document; an agent sending an unapproved external message; a vendor silently changing model behaviour; bias detected in a Tier 1 decision model.
