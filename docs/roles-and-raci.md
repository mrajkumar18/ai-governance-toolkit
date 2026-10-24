# Roles and RACI

## Roles

| Role | Responsibility |
|---|---|
| **AI Governance Committee** | Owns AI policy and risk appetite; approves Tier 1 use cases and any L4 agent; reviews incident trends |
| **AI Governance Lead** (PMO/GRC) | Runs the intake process, keeps the register, chairs gate reviews, reports to the committee |
| **Business Owner** | Accountable for the use case, its outcomes and residual risk |
| **Technical Owner** | Builds and operates the system; produces technical evidence (testing, logs, documentation) |
| **Risk & Compliance** | Challenges risk assessments; maps obligations; owns control testing |
| **Legal / Data Protection Officer** | Legal classification, lawful basis, DPIA / impact assessment review |
| **Information Security** | Security review, access control, logging, red-team and incident support |
| **Internal Audit** | Independent assurance over the toolkit's operation |

## RACI by activity

R = Responsible, A = Accountable, C = Consulted, I = Informed

| Activity | Business Owner | Technical Owner | Gov. Lead | Risk & Compliance | Legal / DPO | InfoSec | Committee |
|---|---|---|---|---|---|---|---|
| Submit intake form | A/R | C | I | I | I | I | - |
| Assign risk tier | C | C | R / A (Tier 2-3) | C | C | C | A (Tier 1) |
| Maintain AI register | C | R | A | I | I | I | I |
| Impact assessment | A | R | C | C | C | C | I |
| Gate approvals | A (Tier 2-3) | R | R | C | C | C | A (Tier 1) |
| Monitoring and drift review | A | R | I | C | I | C | I |
| Incident response | A | R | R | C | C | R | A for Sev 1-2; I otherwise |
| Retirement | A | R | R | I | C | C | I |
