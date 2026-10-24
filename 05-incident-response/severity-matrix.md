# Severity Matrix

| Severity | Definition | Examples | Response target | Escalate to |
|---|---|---|---|---|
| **Sev 1 Critical** | Serious harm to people, major legal/regulatory breach, or large-scale compromise | Discriminatory credit decisions at scale; agent makes unauthorised payments; large personal-data leak via model | Immediate; contain within 1 hour | Committee, Legal/DPO, executive sponsor |
| **Sev 2 High** | Material harm or breach contained to limited scope; high-risk system malfunction | Tier 1 model accuracy collapse; confirmed prompt-injection exploit with limited impact | Triage within 4 hours; contain within 1 business day | AI Governance Lead, Legal/DPO, InfoSec |
| **Sev 3 Medium** | Control failure or quality issue with minor harm | Repeated hallucinations in internal copilot; missing logs for a period | Triage within 1 business day | System owners, Risk |
| **Sev 4 Low / Near miss** | No harm; potential for harm identified | Guardrail blocked an injection attempt; override rate rising | Log and review at next gate | System owner |

**Upgrade rule:** raise severity one level if the system is Tier 1, if vulnerable groups are affected, or if the issue is repeated.
