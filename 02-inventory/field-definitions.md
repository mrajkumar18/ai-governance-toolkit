# Register Field Definitions

## `ai-system-register.csv`

| Field | Definition | Allowed values / format |
|---|---|---|
| `system_id` | Unique ID | `AI-###` |
| `name` | Short name | Text |
| `type` | Kind of AI | Predictive ML; Generative AI; Generative AI (RAG); Agent (multi-agent); Vendor embedded AI |
| `business_owner` / `technical_owner` | Accountable roles | Role or name |
| `business_unit` | Owning unit | Text |
| `purpose` | What it does, in one line | Text |
| `status` | Lifecycle state | Idea; Design; Pilot; Live; Suspended; Retired |
| `risk_tier` | Result of the [questionnaire](../01-intake-and-risk-tiering/risk-tiering-questionnaire.md) | 0, 1, 2, 3 |
| `eu_ai_act_role` | Role under the EU AI Act, or benchmark status | Provider; Deployer; Provider+Deployer; Importer/Distributor; Benchmark only (no EU nexus) |
| `jurisdictions` | Where it operates or affects people | Text |
| `autonomy_level` | [L1-L4](../01-intake-and-risk-tiering/agent-autonomy-levels.md) | L1; L2; L3; L4 |
| `provider_and_model` | Provider, model, version | Text |
| `hosting_region` | Where it runs | Text |
| `data_categories` | Data used | Text |
| `personal_data` | Processes personal data? | Y / N |
| `cross_border_transfer` | Data leaves jurisdiction or goes to external provider? | Y / N |
| `human_oversight_mechanism` | How a human can review or override | Text |
| `impact_assessment_ref` | ID of the impact assessment (required for Tier 1-2) | `IA-###` or blank |
| `committee_approval_ref` | Committee decision reference (required for Tier 1 and any L4 system that is Pilot/Live) | Text or blank |
| `last_review_date` / `next_review_date` | Review cycle | `YYYY-MM-DD` |
| `open_incidents` | Count of open incidents | Integer |

## Cross-references between artefacts

| From | Field | Points to |
|---|---|---|
| `agent-register.csv` | `parent_system_id` | `system_id` in the system register |
| [`risk-register-template.csv`](../07-policy-and-templates/risk-register-template.csv) | `system_id` | `system_id` in the system register (one system, many risks) |
| [`gate-tracker.csv`](../04-lifecycle-gates/gate-tracker.csv) | `system_id` | `system_id` in the system register (use gate `CHG` for significant-change decisions) |
| [`incident-log-template.csv`](../05-incident-response/incident-log-template.csv) | system reference | `system_id` in the system register |
| `ai-system-register.csv` | `impact_assessment_ref` | `IA-###` assessment, which names the register ID back and lists risks and controls (TK-xx) |

A risk's `controls_tk_ids` use the control IDs in the [control matrix](../03-control-mapping/control-mapping-matrix.csv).

## `agent-register.csv`

| Field | Definition |
|---|---|
| `agent_id` | Unique ID (`AG-<system>-<n>`) |
| `parent_system_id` | Links to `system_id` |
| `role` | What the agent is for |
| `tools_allowed` | Allow-list of tools the agent may call |
| `permissions` | read-only / write (scope) |
| `data_scopes` | Data the agent can reach |
| `actions_requiring_approval` | Actions that need human approval |
| `max_steps_per_task` | Loop bound |
| `rate_or_spend_limit` | Daily call or spend ceiling |
| `kill_switch_owner` | Person who can halt the agent |
| `log_location` | Where traces are stored |
| `prompt_version` | Version of system prompt and instructions |
| `eval_suite_ref` | Test suite reference |
| `last_red_team_date` | Most recent adversarial test |
