# Gate 2: Pre-Deployment

**Purpose:** Prove the system is tested, secured and operable **before** it reaches users.
**Applies to:** All tiers; depth scales with tier.

## Entry criteria
- [ ] G1 approved (Tier 1-2) or G0 approved (Tier 3)
- [ ] Test environment and representative test data available

## Checklist
**Quality and safety**
- [ ] Performance tested against thresholds on representative data (TK-10)
- [ ] Robustness tested: edge cases, adversarial and out-of-distribution inputs (TK-10)
- [ ] Bias / fairness testing performed and results accepted by Risk (TK-11) *(Tier 1-2)*
- [ ] For GenAI: hallucination, groundedness and harmful-output evaluation (TK-10, TK-24)

**Security**
- [ ] Security testing / red-team completed; high findings closed (TK-12)
- [ ] For GenAI and agents: prompt-injection, data-leakage and tool-misuse tests (TK-12, TK-21)
- [ ] Secrets, keys and credentials managed; least privilege verified (TK-12)

**Oversight and transparency**
- [ ] Human override tested end to end (TK-09)
- [ ] Oversight effectiveness baseline set and tested: expected override-rate range and review time defined; reviewers shown to catch known errors in a seeded or score-hidden test (record the miss rate) *(Tier 1-2)* (TK-09)
- [ ] Users are told when they interact with AI, and instructions for use are in place (TK-08)
- [ ] For GenAI and user-facing systems: AI-generated or manipulated content is labelled or marked (machine-readable where Art. 50(2) applies; deepfake disclosure under Art. 50(4)); label text and marking approach recorded (TK-24)
- [ ] Complaint / contest route live (TK-19)

**Operations**
- [ ] Logging verified with a sample audit trail (TK-13)
- [ ] [Monitoring plan](../07-policy-and-templates/monitoring-plan-template.md) approved: metrics, thresholds, frequency, owners, suspension triggers *(Tier 1-2; Tier 3 uses the annual review)* (TK-17)
- [ ] Alert thresholds and on-call owner configured (TK-17)
- [ ] Incident contacts and [playbook](../05-incident-response/ai-incident-playbook.md) linked (TK-18)
- [ ] Rollback / kill-switch tested (TK-21)
- [ ] [Model card](../07-policy-and-templates/model-card-template.md) and technical documentation current (TK-14)
- [ ] Fallback / manual process tested, so the business can run without the AI (TK-17)
- [ ] Open conditions from G0/G1 closed or formally accepted ([exceptions process](../07-policy-and-templates/exception-and-risk-acceptance.md))
- [ ] Operators and users trained (TK-20)
- [ ] Register updated: status, tier, review dates (TK-02)

## Required evidence
Test reports · Red-team report · Bias report · Oversight test record (incl. effectiveness baseline) · Disclosure and labelling evidence (screens, label text, marking or metadata approach) · Log sample · Monitoring plan and config · Training records

## Outcomes
Approve for release · Approve for limited release (pilot) with conditions · Reject
