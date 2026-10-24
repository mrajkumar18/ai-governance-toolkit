# Shadow AI Discovery Guide

Shadow AI is any AI use that has not gone through intake: personal accounts on public chatbots, browser extensions with AI features, AI switched on inside an existing SaaS product, scripts calling a model API, or a team's own agent. You cannot tier or govern what you have not found. Use several of the methods below together; no single one finds everything.

> **Before you monitor:** involve Legal / the DPO (and HR or employee representatives where required). Monitoring staff activity has privacy and employment-law implications. Prefer category-level and application-level signals over reading content, and say in the policy what is monitored.

## 1. Detection methods

| Method | What it reveals | Typical owner | Limits |
|---|---|---|---|
| **Web / DNS / proxy / CASB logs** filtered by an "AI / generative AI" category or a maintained domain list | Which AI sites and APIs are reached, by which teams, how often | InfoSec / Network | Misses personal devices and mobile data; list needs regular updates |
| **Identity-provider and OAuth review**: sign-ins with company SSO and third-party app consents that include AI tools | Sanctioned-looking tools users connected to mail, drive or chat | IT / IAM | Only covers tools using company identity |
| **Browser-extension and software inventory** via endpoint management | AI extensions, desktop assistants, local model runners | IT / Endpoint | Unmanaged devices are invisible |
| **Procurement, card and expense data**: AI subscriptions, API credits, free-trial sign-ups to work emails | Paid or trialled tools outside purchasing | Finance / Procurement | Free tiers leave no spend trail |
| **Embedded-AI review of existing SaaS**: release notes, admin consoles, contract renewals, vendor questionnaires | AI features enabled by default inside CRM, HR, collaboration, security and ITSM tools | Procurement / Vendor risk | Needs a recurring review, not a one-off |
| **DLP and endpoint alerts** for uploads or pastes of classified data to AI domains | Data-leak risk and the teams behind it | InfoSec | Detects the leak, not always the tool |
| **Code and CI scanning**: AI SDK imports, model-API keys in repositories, pipeline calls to model endpoints | Engineering-built AI and agents | Engineering / AppSec | Only covers code you can scan |
| **Cloud billing and API-gateway logs** for model-hosting and inference services | Self-hosted models and unregistered pilots | Cloud / FinOps | Needs tagging discipline |
| **Survey and amnesty**: ask every business unit and offer a no-blame window to register existing use | Use that no log shows; the context behind it | AI Governance Lead | Relies on honesty; pair with the technical methods |

## 2. Process

1. **Baseline** (week 1 of the [adoption plan](adoption-guide.md)): run the survey and amnesty, pull the first reports from the methods above, and seed the [register](../02-inventory/ai-system-register.csv).
2. **Triage each finding** within 10 business days: *Sanction* (register, tier, onboard through the gates), *Replace* (move users to an approved equivalent) or *Stop* (block and instruct).
3. **Escalate immediately** if personal, customer or regulated data was entered into a non-approved tool: treat it as an incident under the [playbook](../05-incident-response/ai-incident-playbook.md).
4. **Repeat** at least quarterly, and whenever the AI domain list or vendor features change materially.
5. **Report** register coverage (registered systems ÷ systems discovered) to the Committee as a [KPI](../07-policy-and-templates/governance-kpis.md).

## 3. Policy language (add to the AI policy and acceptable-use standard)

> **Discovery and monitoring.** The organisation may use network, identity, endpoint, procurement and code-scanning data to identify the use of AI tools. Monitoring focuses on which tools are used and what categories of data leave the organisation, and is carried out under the applicable privacy and employment rules.
>
> **Registration duty.** Anyone who uses, builds or enables an AI tool, feature, plugin or agent for work must register it through intake, including free tools, pilots and AI features inside existing software.
>
> **Amnesty.** For [30 days from the policy launch], AI use declared voluntarily is assessed through the gates without disciplinary action, unless it involved deliberate disregard of data-protection or confidentiality rules.

## 4. Embedded and vendor AI checklist (ask at every renewal)
- [ ] Has the vendor added or enabled AI features since the last review?
- [ ] Is our data used to train or improve the vendor's models, and can we opt out?
- [ ] Can AI features be switched off by an administrator, per team?
- [ ] Is the feature in the register, tiered, and covered by the vendor assessment?
