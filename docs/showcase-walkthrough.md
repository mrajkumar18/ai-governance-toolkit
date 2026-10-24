# Showcase Walkthrough

A step-by-step demo of the toolkit, built for a **20-30 minute** live walkthrough, a screen-share or a recorded video. Each step gives you what to show, what to run, what the output looks like and what to say. Steps 1-4 fit in 10 minutes if you need a short version.

> **Audience:** risk, compliance, audit, PMO, security, engineering and executive sponsors. Adjust the emphasis: executives care about steps 1, 2 and 7; auditors about steps 5 and 6; engineers about steps 3 and 4.

## Before you start

**Setup (2 minutes)**

```bash
git clone <your-repo-url> && cd ai-governance-toolkit
python3 --version          # 3.8 or newer; no packages needed
```

**Have open in tabs:** this repo on GitHub (or your editor), the `README.md` diagram rendered, and a terminal at the repo root.

**Dry-run it once first.** The register validator flags overdue reviews, so if you demo after a sample `next_review_date` has passed (the earliest is **2026-12-15**), step 6 will show findings you did not intend. Either roll the sample dates forward, or run the validator with `REGISTER_AS_OF=2026-10-24` in front of the command.

**One-line pitch:** *"One control set, mapped to many frameworks, applied in proportion to risk, with evidence an auditor can check."*

---

## Step 1. The big picture (3 min)

**Show:** `README.md`, the folder table and the "How it works" diagram.

**Say:**
- Governance only works if it is light enough to use and evidence-based enough to audit.
- Every use case, including pilots, vendor-embedded AI and agents, enters at **G0**, gets a **tier**, goes in the **register**, and passes **gates** in proportion to that tier.
- Tier 0 stops immediately; Tier 3 is a 30-minute path; Tier 1 gets the full path.

**Point at:** the nine top-level folders map to the lifecycle: intake → inventory → controls → gates → incidents → impact assessment → policies.

---

## Step 2. Decide which rules apply (2 min)

**Show:** [`applicability-guide.md`](applicability-guide.md), the quick decision table.

**Say:**
- Not every framework is binding on every organisation. The guide separates **binding law**, **advisory guidance** and **benchmarks**.
- The internal tiers apply from day one, regardless of legal dates, because delay changes legal exposure, not good practice.
- The EU AI Act timeline shown is as amended by the Digital Omnibus on AI (Regulation (EU) 2026/1744); the guide tells readers to verify against the Official Journal.

**Audience question to expect:** "Does the EU AI Act apply to us?" Answer using the EU-nexus row, and show that the register records the role (provider, deployer, benchmark only).

---

## Step 3. Classify use cases live (5 min)

**Show:** [`risk-tiering-questionnaire.md`](../01-intake-and-risk-tiering/risk-tiering-questionnaire.md) briefly, then the decision-flow diagram in [`risk-tiering-decision-flow.md`](../01-intake-and-risk-tiering/risk-tiering-decision-flow.md).

**Say:** The method is deterministic: two assessors reach the same tier. Stop checks first, then high-risk domains, then a score from impact factors and autonomy.

**Run the five scenarios.** Each takes a few seconds and shows a different rule.

**3a. A medium-risk use case**
```bash
python3 tools/risk_tier.py tools/example_answers.json
```
```
Tier 2 - Medium
Score: 5
  - Score 5 in 4-7
Committee approval required: No
Legal confirmation required: No
```

**3b. A high-risk domain (credit scoring)**
```bash
python3 tools/risk_tier.py tools/example_answers_high_risk.json
```
```
Tier 1 - High
Score: 9
  - High-risk domain(s): B5
Committee approval required: Yes
Legal confirmation required: Yes
```
*Point out:* one Section B "Yes" forces Tier 1 whatever the score.

**3c. A prohibited practice (emotion inference at work, A6)**
```bash
echo '{"A":["A6"],"B":[],"C":[],"autonomy":"L1"}' > /tmp/a6.json
python3 tools/risk_tier.py /tmp/a6.json
```
```
Tier 0 - Prohibited / Stop
  - Stop checks triggered: A6
  - Do not proceed. Escalate to Legal.
Committee approval required: No
Legal confirmation required: Yes
```

**3d. A fully autonomous agent with nothing else risky (L4)**
```bash
echo '{"A":[],"B":[],"C":[],"autonomy":"L4","production_write_access":false}' > /tmp/l4.json
python3 tools/risk_tier.py /tmp/l4.json
```
```
Tier 2 - Medium
Score: 4
  - Score 4 in 4-7
  - L4 autonomy requires AI Governance Committee approval (L4 scores 4 points on its own, so it is never Tier 3)
Committee approval required: Yes
Legal confirmation required: No
```
*Point out:* autonomy alone carries weight, and L4 always needs the Committee.

**3e. Tier 1 reached by score, with no high-risk domain**
```bash
echo '{"A":[],"B":[],"C":["C1","C2","C3","C4","C6"],"autonomy":"L1"}' > /tmp/s8.json
python3 tools/risk_tier.py /tmp/s8.json
```
```
Tier 1 - High
Score: 8
  - Score 8 >= 8
  - Tier 1 reached by score: Legal to confirm classification
Committee approval required: Yes
Legal confirmation required: Yes
```
*Point out:* Legal is looped in for every Tier 1, however it was reached.

**Then show the tests** to demonstrate the rules are protected:
```bash
cd tools && python3 -m unittest test_risk_tier -v && cd ..
```
Expect `Ran 10 tests ... OK`.

**Say:** The tool is a triage aid, not a legal determination. Legal confirms every Tier 0 and Tier 1 outcome.

---

## Step 4. Case study A: a high-risk predictive model (5 min)

**Story:** A bank pre-screens retail loan applications. An underwriter makes the final decision. It is Tier 1 because creditworthiness assessment is a high-risk domain.

**Walk the artefacts in order:**

| # | Open | What to point out |
|---|---|---|
| 1 | [`ai-system-register.csv`](../02-inventory/ai-system-register.csv), row **AI-001** | Tier 1, L1, owner roles, `impact_assessment_ref` = IA-001, `committee_approval_ref` = COM-2026-014 |
| 2 | [`gate-tracker.csv`](../04-lifecycle-gates/gate-tracker.csv), AI-001 rows | G1 "Approve with conditions" (conditions closed), then G2 "limited release (pilot)" with open conditions: decisions leave a trail |
| 3 | [`example-loan-prescreening-impact-assessment.md`](../06-impact-assessment/example-loan-prescreening-impact-assessment.md) | Section 5 impact ratings, section 7 oversight (override rate monitored, with thresholds), section 9 monitoring plan |
| 4 | [`risk-register-template.csv`](../07-policy-and-templates/risk-register-template.csv), R-001 and R-002 | Inherent versus residual scores; the risks are the ones the impact assessment named |

**Say:** Notice the golden thread: the same system ID and the same control IDs (TK-xx) run through register, gates, impact assessment and risk register. An auditor can start at any one and reach the others.

---

## Step 5. Case study B: a GenAI multi-agent system (5 min)

**Story:** An internal PMO agent reads programme status, detects drift and drafts escalation notes. It is Tier 2: internal, L2 autonomy, vendor LLM.

**Walk the artefacts:**

| # | Open | What to point out |
|---|---|---|
| 1 | Register row **AI-003** | Type "Agent (multi-agent)", L2, vendor LLM, personal data = Y (staff names), cross-border = Y |
| 2 | [`agent-register.csv`](../02-inventory/agent-register.csv) | Three agents, each with an allow-listed tool set, `read-only` or `write (drafts only)`, step and rate limits, a named kill-switch owner, an eval suite and a red-team date |
| 3 | [`agentic-addendum.md`](../04-lifecycle-gates/agentic-addendum.md) | Design, testing and operation checks that apply from L2 up: tool allow-lists, prompt-injection tests, kill switch |
| 4 | [`example-portfolio-agent-impact-assessment.md`](../06-impact-assessment/example-portfolio-agent-impact-assessment.md) | The short form for Tier 2; the section 4A transfer assessment (tokenise names before they reach the vendor LLM); oversight effectiveness thresholds |
| 5 | [`significant-change-checklist.md`](../04-lifecycle-gates/significant-change-checklist.md) | What happens when the vendor silently changes the model: it triggers re-testing, not a shrug |

**Say:** Agents are first-class here: autonomy levels, tool permissions, kill switches and approval gates are part of the registers and gates, not an afterthought.

---

## Step 6. Show that controls are enforced, not just written (3 min)

**Run the validator on the clean sample data:**
```bash
python3 tools/validate_register.py 02-inventory/ai-system-register.csv 02-inventory/agent-register.csv
```
```
OK: 3 system(s) validated, no findings.
```

**Now break something on purpose.** Clear the Committee approval for AI-001:
```bash
python3 - <<'EOF'
import csv
rows = list(csv.reader(open('02-inventory/ai-system-register.csv', newline='')))
h = rows[0]
for r in rows[1:]:
    if r[0] == 'AI-001':
        r[h.index('committee_approval_ref')] = ''
csv.writer(open('/tmp/bad.csv', 'w', newline=''), lineterminator='\r\n').writerows(rows)
EOF
python3 tools/validate_register.py /tmp/bad.csv 02-inventory/agent-register.csv; echo "exit code: $?"
```
```
1 finding(s):
 - AI-001: Tier 1 / L4 system in Pilot requires committee_approval_ref
exit code: 1
```

**Say:** The register is the single source of truth, and the rules are checked mechanically: Tier 1 needs a Committee reference, Tier 1-2 needs an impact assessment, Tier 0 cannot be live, and overdue reviews are flagged. A non-zero exit code means you can run this in CI.

---

## Step 7. Evidence an auditor would ask for (3 min)

**Show:** [`control-mapping-matrix.csv`](../03-control-mapping/control-mapping-matrix.csv) in a spreadsheet or GitHub's table view.

**Pick one control and trace it, for example TK-09 (human oversight):**

| Column | What it shows |
|---|---|
| Frameworks | NIST AI RMF GOVERN 3 / MAP 3 · ISO 42001 A.6, A.9 · EU AI Act Art. 14, 26(2) · GDPR Art. 22 |
| Typical evidence | Oversight design; override test results; effectiveness metrics (override rate, review time, reviewer miss rate); operator training records |
| Gate | G1 and G2: design, then test |
| Applies to | Tier 1-2 systems at L1-L3 |

**Say:** One control set, mapped to many frameworks, so you do not run parallel compliance programs. Every row names the evidence, and the [gates](../04-lifecycle-gates/) say where that evidence is checked.

**If asked about incidents,** open [`ai-incident-playbook.md`](../05-incident-response/ai-incident-playbook.md): the notification-clocks table (CERT-In, DPDPA, GDPR, EU AI Act) and the agent containment checklist.

---

## Closing (1 min)

**Summarise in three lines:**
1. **Proportionate:** the tier decides the path.
2. **Evidence-first:** every control names its evidence and its gate.
3. **Agent-aware:** autonomy and permissions are part of the model.

**Call to action:** "Start with the 30-day adoption plan. Seed the register in week 1, tier everything in week 2." Link to [`adoption-guide.md`](adoption-guide.md).

**Disclaimer to say out loud:** this is a practitioner's starting point and not legal advice; regulatory references need checking against official texts and your regulators.

---

## Likely questions

| Question | Where to answer from |
|---|---|
| How do we find AI nobody told us about? | [`shadow-ai-discovery.md`](shadow-ai-discovery.md) |
| Who approves what? | Approver matrix in [`04-lifecycle-gates/README.md`](../04-lifecycle-gates/README.md); RACI in [`roles-and-raci.md`](roles-and-raci.md) |
| What if a control cannot be met on time? | [`exception-and-risk-acceptance.md`](../07-policy-and-templates/exception-and-risk-acceptance.md) (time-bound exceptions, rating bands) |
| What do we do when a vendor updates the model? | Significant-change checklist, section 4; vendor assessment section 6 |
| Does this replace our ISO 27001 / GDPR program? | No. The matrix shows where existing controls already cover AI obligations. |
| How do we measure success? | [`governance-kpis.md`](../07-policy-and-templates/governance-kpis.md) |
| Can we adopt only part of it? | Yes. Start with G0 and G2 for all new work; add the rest as maturity grows. |

## Presenter tips

- **Show, then explain.** Run the command, let the output land, then say the one-sentence takeaway.
- **Keep the matrix for last.** It is dense; it lands better after people have seen the artefacts it points to.
- **Stay in the fictional world.** All example data is made up. Do not paste real systems, vendors or incidents into a public demo.
- **Record it.** A 10-minute screen recording of steps 3-6 makes a strong README link.
