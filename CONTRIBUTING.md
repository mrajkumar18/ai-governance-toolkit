# Contributing

Corrections and improvements are welcome. This toolkit is a practitioner's starting point, so accuracy and usability matter more than volume.

## Good contributions
- Corrections to regulatory references, dates or clause mappings (please link the official source)
- Gaps in coverage, with the framework clause or real-world scenario that exposes them
- Clearer wording in templates, checklists and the walkthrough
- Bug fixes or tests for the Python helpers

## Ground rules
1. **No real data.** Never include real client, vendor, system, employee or incident information. All examples stay fictional.
2. **Keep it proportionate.** New controls should say who does what, at which gate and with what evidence. If a control cannot name its evidence, it is not ready.
3. **Keep the method deterministic.** Changes to the tiering rules must update the questionnaire, the decision flow, `tools/risk_tier.py` and the tests together.
4. **Mappings are indicative.** Reference at clause, article or category level, and keep the "not legal advice" disclaimer.
5. **Update the changelog** under a new or unreleased version heading.

## Before opening a pull request
```bash
cd tools && python -m unittest test_risk_tier -v && cd ..
REGISTER_AS_OF=2026-10-24 python tools/validate_register.py 02-inventory/ai-system-register.csv 02-inventory/agent-register.csv
```
CI runs the same checks plus a markdown link check.

## Reporting a problem
Open an issue with the file, what is wrong, and (for regulatory points) the source you checked.

By contributing you agree that your contribution is licensed under this repository's license.
