# Tools

Small, dependency-free Python (3.8+) helpers.

| Script | What it does |
|---|---|
| `risk_tier.py` | Calculates the risk tier from questionnaire answers (JSON), plus whether Committee approval and Legal confirmation are required. Mirrors the logic in the questionnaire |
| `validate_register.py` | Checks the system register (and optionally the agent register) for missing fields, invalid values, missing impact assessments / committee approvals, agent-to-parent consistency and overdue reviews |
| `test_risk_tier.py` | Unit tests for the tier logic, including the L4 floor and Legal-escalation rules (`python -m unittest test_risk_tier -v`) |

```bash
python risk_tier.py example_answers.json
python risk_tier.py example_answers_high_risk.json
python validate_register.py ../02-inventory/ai-system-register.csv ../02-inventory/agent-register.csv

# Evaluate overdue reviews as of a fixed date (CI uses this for the sample data)
REGISTER_AS_OF=2026-10-24 python validate_register.py ../02-inventory/ai-system-register.csv ../02-inventory/agent-register.csv
```
