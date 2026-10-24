# Third-Party AI Assessment (Vendor / Model Provider)

Complete at G1 and keep current through section 6. Attach to the register entry. Ratings: ✅ Satisfactory · ⚠ Gap (action) · ❌ Unacceptable.

| Vendor | | Product / model | | Assessor | | Date | |
|---|---|---|---|---|---|---|---|

## 1. Governance and compliance
| # | Question | Rating | Notes |
|---|---|---|---|
| 1.1 | Does the vendor have an AI governance program and named accountable owner? | | |
| 1.2 | Certifications / attestations (e.g., ISO 27001, SOC 2, ISO/IEC 42001)? Scope covers this service? | | |
| 1.3 | Which regulations does the vendor state compliance with (e.g., EU AI Act role, DPDPA, GDPR)? | | |
| 1.4 | Is the vendor a regulated entity's outsourcing partner (sector rules apply)? | | |

## 2. Data
| # | Question | Rating | Notes |
|---|---|---|---|
| 2.1 | Is our data (prompts, files, outputs) used to **train or improve** models? Can this be disabled contractually? | | |
| 2.2 | Retention period and deletion process for prompts, outputs and logs? | | |
| 2.3 | Where is data processed and stored (inference, storage, logs, backups, support access)? Which sub-processors? | | |
| 2.6 | Transfer route for personal data (DPDPA s.16 position, GDPR Chapter V mechanism), region pinning available, and answers recorded in section 4A of the impact assessment? | | |
| 2.4 | Tenant isolation and encryption in transit and at rest? | | |
| 2.5 | Data-processing agreement covering our DPDPA / GDPR obligations? | | |

## 3. Model and system
| # | Question | Rating | Notes |
|---|---|---|---|
| 3.1 | Model documentation available (model card, limitations, intended use, evaluation results)? | | |
| 3.2 | Training-data provenance, copyright and licensing posture? IP indemnity offered? | | |
| 3.3 | Safety and bias testing performed; red-team results shared? | | |
| 3.4 | Model **change notification**: advance notice and version pinning for updates or deprecation? | | |
| 3.5 | For agents / tool use: permission model, audit logging, action controls? | | |
| 3.6 | **If a general-purpose AI model:** technical documentation for downstream users provided (capabilities, limits, restricted uses)? Public summary of training content and copyright policy available? | | |
| 3.7 | **If a general-purpose AI model:** is it designated or treated as presenting systemic risk? Does the provider follow a recognised code of practice, and will it share relevant evaluation and incident information? | | |

## 4. Security and resilience
| # | Question | Rating | Notes |
|---|---|---|---|
| 4.1 | Access control, SSO, role-based permissions, key management? | | |
| 4.2 | Prompt-injection and data-leakage protections? | | |
| 4.3 | Logging available to us (inputs, outputs, tool calls) and exportable? | | |
| 4.4 | Incident response: notification time, contacts, and cooperation with our playbook? | | |
| 4.5 | Availability SLAs, business continuity, and exit / portability plan? | | |

## 5. Contract essentials
- [ ] Data use and no-training clause
- [ ] Retention and deletion obligations
- [ ] Audit and assurance rights (**Tier 1: right to audit, or to receive independent assurance reports, is mandatory**)
- [ ] Incident-notification timeframe aligned to our regulatory clocks
- [ ] IP indemnity and output ownership
- [ ] Sub-processor approval and change notice
- [ ] Model-change notice and version control
- [ ] Exit assistance and data return

## 6. Ongoing monitoring (after approval)
Set the cadence at G1 and review it at each G3.

| # | Activity | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|
| 6.1 | Full reassessment of this questionnaire | Annually | Annually | At contract renewal |
| 6.2 | Check certifications / attestations are still valid and in scope | Annually | Annually | At renewal |
| 6.3 | Model-change notices logged in a version register; each one triaged against the [significant-change checklist](../04-lifecycle-gates/significant-change-checklist.md) | Every notice | Every notice | Every notice |
| 6.4 | Regression / canary tests run to detect silent model changes | Daily or per release | Weekly | Monthly |
| 6.5 | Sub-processor and region changes reviewed against transfer assessment | Every change | Every change | At renewal |
| 6.6 | Vendor incident notices reviewed; notification SLA tested at least once (tabletop or test notice). The SLA must let you meet your earliest regulatory clock | Annually | Every two years | - |
| 6.7 | Audit rights exercised, or independent assurance reports (e.g., SOC 2, ISO 27001 / 42001) obtained and reviewed | Annually | Annually | - |
| 6.8 | Exit and data-return plan tested or walked through | Every two years | At renewal | - |

## 7. Decision
☐ Approve ☐ Approve with conditions ☐ Reject. Conditions: __________ Residual risk owner: __________
