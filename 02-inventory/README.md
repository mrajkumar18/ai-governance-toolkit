# 02 · AI Inventory

You cannot govern what you cannot see. The register is the single source of truth for every AI system and agent.

| File | Purpose |
|---|---|
| [`ai-system-register.csv`](ai-system-register.csv) | One row per AI system or use case (3 fictional examples) |
| [`agent-register.csv`](agent-register.csv) | One row per agent, linked to its parent system via `parent_system_id` |
| [`field-definitions.md`](field-definitions.md) | What each field means and allowed values |

## Rules
1. **Register before build** (G0). Nothing goes live without an entry.
2. **Include vendor-embedded AI** (CRM, HR, security tools) and approved GenAI tools.
3. **One owner per system**, with a named business owner.
4. **Review dates are enforced:** the validator flags overdue reviews.

Validate with: `python ../tools/validate_register.py ai-system-register.csv agent-register.csv`
