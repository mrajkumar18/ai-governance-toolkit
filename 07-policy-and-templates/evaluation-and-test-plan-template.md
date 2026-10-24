# Evaluation and Test Plan (Template)

Complete at G1 (plan) and G2 (results).

| System / ID | | Tier | | Owner | | Version tested | |
|---|---|---|---|---|---|---|---|

## 1. Acceptance criteria
| Dimension | Metric | Acceptance threshold | Result | Pass? |
|---|---|---|---|---|
| Accuracy / quality | | | | |
| Robustness | Performance under noise, edge cases, out-of-distribution input | | | |
| Fairness | Metric(s) chosen for context, with rationale (e.g., selection-rate parity, error-rate parity) | | | |
| Safety / harmful output | | | | |
| Latency / reliability | | | | |

*Choose fairness metrics deliberately; they can conflict. Record why the chosen ones fit the use case and who accepted the trade-off.*

## 2. Test data
Source, representativeness, size, separation from training data, handling of sensitive attributes (use lawful, minimised data or proxies; document privacy safeguards).

## 3. Generative AI tests
- [ ] Groundedness / factuality against sources
- [ ] Hallucination rate on a defined question set
- [ ] Harmful, toxic or policy-violating output tests
- [ ] Personal-data and confidential-data leakage tests
- [ ] Jailbreak and refusal behaviour

## 4. Agent tests (L2+)
- [ ] Prompt injection through documents, web pages, emails, tool output
- [ ] Out-of-scope action requests (excessive agency)
- [ ] Malformed or malicious tool arguments
- [ ] Permission boundary and data-entitlement tests
- [ ] Loop, cost and step-limit tests
- [ ] Safe failure on tool outage or ambiguity
- [ ] Kill switch timed test

## 5. Security testing
Penetration test / red-team scope, findings, remediation status.

## 6. Regression
Test suite ID, tied to model, prompt and tool versions. Re-run on every change.

## 7. Results and sign-off
Summary · Open issues and accepted risks · Approver · Date.
