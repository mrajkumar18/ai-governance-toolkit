# 30-Day Adoption Guide

A pragmatic path to put this toolkit to work in an organisation that has no AI governance today.

## Week 1: Discover
- Run a short survey and ask IT, procurement and business units: "Where is AI used or planned?" Include **embedded vendor AI** and shadow GenAI use.
- Use the methods in the [shadow-AI discovery guide](shadow-ai-discovery.md) (network and identity logs, extension inventory, procurement data, embedded-AI review, amnesty) alongside the survey.
- Seed the [AI system register](../02-inventory/ai-system-register.csv) with whatever you find.
- Name an AI Governance Lead and a sponsor (see [roles](roles-and-raci.md)).
- Issue an interim [GenAI acceptable-use standard](../07-policy-and-templates/genai-acceptable-use-standard.md) immediately; shadow AI is usually the first and largest exposure.
- Work out which regimes apply to you using the [applicability guide](applicability-guide.md).

## Week 2: Classify
- Run every registered item through the [risk-tiering questionnaire](../01-intake-and-risk-tiering/risk-tiering-questionnaire.md).
- Escalate any Tier 0 immediately to Legal.
- Prioritise Tier 1 items for impact assessments.

## Week 3: Control
- Adopt the [gate checklists](../04-lifecycle-gates/). Start with G0 (intake) and G2 (pre-deployment) for all new work.
- Use the [control mapping](../03-control-mapping/control-mapping-matrix.csv) to see which existing ISO 27001 / GDPR controls already cover AI obligations. Avoid duplicating them.
- Publish the [incident playbook](../05-incident-response/ai-incident-playbook.md) and nominate responders.

## Week 4: Operate
- Hold the first AI Governance Committee meeting. Agenda: register review, Tier 1 approvals, open risks.
- Complete one full [impact assessment](../06-impact-assessment/ai-impact-assessment-template.md) for a real Tier 1 or Tier 2 use case.
- Agree 3-5 KPIs from [governance-kpis.md](../07-policy-and-templates/governance-kpis.md).
- Adopt the [AI policy](../07-policy-and-templates/ai-policy-template.md) through your normal policy approval route.

## Common pitfalls
- Making G0 so heavy that teams avoid it. Keep the Tier 3 path to under 30 minutes.
- Treating the register as a one-off exercise. Assign an owner and a quarterly review.
- Ignoring agents. Add autonomy level and tool permissions from day one.
