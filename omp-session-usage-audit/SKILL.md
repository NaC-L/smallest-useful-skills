---
name: omp-session-usage-audit
description: "Audit a bounded OMP session window for recorded tokens, cost components, and timing without changing configuration."
---

# Bounded OMP session usage audit

Produce one read-only report for the requested sessions and event-time window. No model/config changes, installations, or injection audits. Preserve verification requirements.

Do the smallest useful thing: answer the requested usage question from the narrowest representative window. Reuse a compliant runner rather than building telemetry or auditing unrelated projects.

## Procedure

1. Fix session root, file/project bounds, timezone, start/end, and scan budget. Inspect the current OMP schema or a programmatically summarized sample first; versions need not share a schema. Stop on unsupported shapes or exhausted bounds. Never load whole transcripts into context.
2. Use an existing trusted runner after checking schema, windowing, and read-only behavior. Otherwise aggregate bounded JSONL line by line. No private runner is required or distributed. Count malformed records, missing timestamps, and exclusions.
3. Read both `message.usage` and top-level `usage`, counting each event once. Parse actual event timestamps as ISO-8601 or documented epoch seconds/milliseconds; never substitute file modification time. Verify naive-timestamp timezone handling. Apply identical event windows to every metric, not whole-session counters.
4. Preserve `input`, `output`, `cacheRead`, `cacheWrite`, and `totalTokens` when present; verify their accounting before deriving totals. Preserve monetary `cost` components (`input`, `output`, `cacheRead`, `cacheWrite`, `total`) or scalar cost with unallocated components. Report currency and missing-field coverage; unknown is not zero. Group by project, verified session kind/role, and model, keeping unknown buckets.
5. Assert unrounded group subtotals equal grand totals within a stated numeric tolerance. Reconcile component costs plus explicitly unallocated amounts to recorded totals; expose mismatches. Derive component unit prices only from matching cost/token coverage.
6. Report recorded request duration, time-to-first-token, and tool wall time only where present, with verified units and coverage. Summed concurrent model/tool durations are work totals, not elapsed or user-active time. Do not invent tool-error rates without recorded error semantics.

## Verification and boundary

Check representative wrapped/unwrapped records and boundary timestamps against aggregates. Report bounds, counts, reconciliation, missing metrics, and limitations. Compare models within comparable roles/time periods; disclose routing, workload, and small-sample confounds.

Only if requested, add a narrow, language-aware user-correction proxy with explicit numerator/denominator and bounded spot-checking; it is not measured accuracy. Stop after reporting, without automatic changes or blanket optimization advice.
