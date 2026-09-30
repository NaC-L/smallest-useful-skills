---
name: bounded-log-triage
description: "Diagnose a reported incident with bounded read-only log or database evidence, without performing repairs."
---

# Bounded evidence triage

For an incident, access failure or disputed event where logs/rows must distinguish causes. Read-only; diagnosis is not permission to repair data or services.

Do the smallest useful thing: answer the reported failure using the narrowest reliable observation. Start with available evidence; widen the window or sources only when a specific hypothesis requires it.

1. Establish target identity, reproduction, event time/timezone, query window and authoritative surface. Record retention/gaps. Distinguish live runtime, stored rows and historical transcripts.
2. If the cause is ambiguous, write 2-3 competing hypotheses. Collect the smallest falsifying observation: active build/config for activation, changed-path output for logic, exact row for data. If an earlier fix failed, measure activation before another patch.
3. Query narrowly with read-only access and bounded results. Correlate primary events with stable identifiers/timestamps. IPs, names, nearby events and slow-query warnings are leads, not proof of ownership or causality.
4. Compare a matched healthy baseline when available. No log hit means "not observed in retained/queried evidence," not "never happened." A present file does not prove a process loaded it.
5. Report observation -> inference -> confidence; alternatives ruled out, missing evidence and next discriminating check. Redact secrets/unnecessary personal data. Stop when the question is answered or the exact missing observation is identified. Keep later authorized repair separate.
