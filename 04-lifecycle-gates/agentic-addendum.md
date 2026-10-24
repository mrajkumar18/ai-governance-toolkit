# Agentic AI Addendum

Apply to any system with autonomy **L2 or above** (see [levels](../01-intake-and-risk-tiering/agent-autonomy-levels.md)). Complete alongside G1 and G2.

## Design (G1)
- [ ] Each agent has a documented **role and scope**; each registered in the [agent register](../02-inventory/agent-register.csv)
- [ ] **Tool allow-list** defined per agent; no wildcard or dynamic tool discovery in production
- [ ] **Least privilege:** read-only by default; each write permission justified and scoped
- [ ] **Action classification:** reversible vs irreversible; irreversible actions require human approval
- [ ] **Separation of duties:** no agent approves its own high-impact action
- [ ] **Bounds defined:** max steps, max runtime, spend/rate limits, retry limits
- [ ] **Delegation rules:** can an agent call or create other agents? (L4 only, Committee approval)
- [ ] **Memory:** what persists between sessions, for how long, and how personal data is handled
- [ ] **Credentials:** short-lived, per-agent, rotated; never in prompts

## Testing (G2)
- [ ] **Prompt injection:** hostile content in documents, web pages, emails and tool outputs does not cause unauthorised actions
- [ ] **Excessive agency:** agent refuses or escalates when asked to act outside scope
- [ ] **Tool misuse:** malformed or malicious tool arguments are validated and rejected
- [ ] **Data leakage:** agent does not expose data outside the requester's entitlement
- [ ] **Goal drift / loops:** agent stops at bounds; no runaway cost
- [ ] **Failure behaviour:** safe state on tool outage, timeout, ambiguous instruction
- [ ] **Kill switch:** halts all agent activity within the defined time; tested and timed
- [ ] **Evaluation suite** with regression tests tied to prompt and model versions

## Operation (G3)
- [ ] Full **trace** per task: plan, tool calls, inputs, outputs, approvals, correlation ID
- [ ] **Anomaly alerts:** unusual tool use, volume, cost, off-hours activity
- [ ] **Sampling review** of agent actions by a human (rate set by tier)
- [ ] **Prompt / tool / model versioning**, with re-testing on any change; changes to tools, permissions, autonomy or model follow the [significant-change checklist](significant-change-checklist.md)
- [ ] **Periodic permission review** and re-certification of the allow-list

## Common agent risks (reference)
Prompt injection · Excessive agency · Insecure tool or plugin design · Sensitive-data disclosure · Unbounded consumption · Over-reliance on agent output · Supply-chain compromise of models, tools or prompts.

These themes align with the OWASP Top 10 for LLM Applications; check its current edition for naming and numbering.
