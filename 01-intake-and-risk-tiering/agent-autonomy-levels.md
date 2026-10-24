# Agent Autonomy Levels

Agentic systems differ from conventional AI because they **plan, call tools and take actions**. Governance should scale with how much the agent is allowed to do without a human.

| Level | Name | Description | Minimum controls |
|---|---|---|---|
| **L1** | Advisor | Produces suggestions; a human decides and performs any action | Output labelling, user guidance, logging |
| **L2** | Approved actor | Proposes actions; **each action needs explicit human approval** | Approval UI, action preview, complete audit log, least-privilege credentials |
| **L3** | Supervised autonomous | Executes within defined guardrails; humans monitor and review exceptions | Allow-listed tools, spend/rate limits, anomaly alerts, kill switch, sampling review, red-team testing |
| **L4** | Fully autonomous | Self-directs, may delegate to or create sub-agents | **Committee approval**, sandboxing, hard action ceilings, continuous monitoring, tested shutdown |

## Design rules (all levels)

1. **Least privilege:** read-only by default; write access is granted per tool, per scope, and logged.
2. **Allow-list tools:** the agent can only call tools explicitly registered for it.
3. **Human approval for irreversible actions:** payments, deletions, external communications, record changes.
4. **Traceability:** every plan step, tool call, input and output is logged with a correlation ID.
5. **Kill switch:** a tested way to halt the agent within a defined time.
6. **Bounded loops:** maximum steps, time and cost per task.
7. **Separation of duties:** an agent should not both propose and approve its own high-impact action.
8. **Prompt-injection resistance:** treat retrieved content and tool outputs as untrusted; validate before acting.

See the [agentic addendum](../04-lifecycle-gates/agentic-addendum.md) for gate-level checks.
