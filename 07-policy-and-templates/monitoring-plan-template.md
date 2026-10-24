# Monitoring Plan (Template)

Complete at G2 for Tier 1-2 systems; review at every G3. For high-risk systems this doubles as the basis for post-market monitoring (EU AI Act Art. 72 applies to **providers**; deployers monitor under Art. 26(5) and pass findings to the provider). The Commission is due to publish guidance, including a voluntary template, on the post-market monitoring plan by 2 September 2027; align this template with it when it appears. Controls: TK-17, TK-09, TK-18.

| System / ID | | Tier | | Plan owner | | Version / date | |
|---|---|---|---|---|---|---|---|

## 1. Scope and objectives
What harms and failures is this plan designed to detect (accuracy loss, drift, unfair outcomes, misuse, over-reliance, vendor-driven change, agent misbehaviour)? Link to the top risks in the [risk register](risk-register-template.csv).

## 2. Metrics, thresholds and actions
| Area | Metric | Baseline | Alert threshold | Suspension threshold | Frequency | Owner | Action on breach |
|---|---|---|---|---|---|---|---|
| Performance | (e.g., accuracy, groundedness, task success) | | | | | | |
| Data / model drift | (e.g., PSI, embedding drift, input mix) | | | | | | |
| Fairness | (monitored groups; parity gap) | | | | | | |
| Human oversight | Override rate | | below / above range | | | | Review for rubber-stamping or model failure |
| Human oversight | Review time or time-to-override | | | | | | |
| Human oversight | Reviewer miss rate (seeded or sampled cases) | | | | | | |
| Complaints and contests | Count, themes, time to resolve | | | | | | |
| Misuse / safety | Blocked prompts, harmful-output reports | | | | | | |
| Security | Injection attempts, anomalous tool use, access anomalies | | | | | | |
| Vendor / model | Version register; canary-test results for silent change | | | | | | |
| Cost / consumption (agents) | Spend, steps, rate limits | | | | | | |

## 3. Data sources and logging
Where each metric comes from, how long logs are kept, who can access them, and how personal data in logs is protected (TK-13).

## 4. Review cadence and reporting
Tier 1 monthly with automated alerts; Tier 2 quarterly. Who reviews, where results are minuted, and how trends reach the Committee (KPIs).

## 5. Escalation, suspension and incidents
- Who can suspend the system, and how fast (link to the kill switch for agents).
- When a breach becomes an incident under the [playbook](../05-incident-response/ai-incident-playbook.md) and which severity it maps to.
- For high-risk systems: how serious incidents are reported to the provider or authority, and within which clock.

## 6. Feedback loop
How findings update the risk register, the impact assessment, the test suite and the tier. A breach that meets the [significant-change criteria](../04-lifecycle-gates/significant-change-checklist.md) triggers that checklist.

## 7. Provider / deployer information flow
What the deployer shares with the provider (incidents, performance data, complaints) and what the provider shares back (model changes, known issues). Reference the contract clause.

## 8. Sign-off
| Role | Name | Date |
|---|---|---|
| Plan owner | | |
| Risk & Compliance | | |
| Business owner | | |
