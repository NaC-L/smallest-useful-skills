---
name: measured-performance-fix
description: "Fix a measured slow path by removing unnecessary work, preserving behavior, and comparing equivalent runtime measurements."
---

# Measured performance fix

Use for a reproducible, measured slow path, not a blanket audit or speculative optimization.

Do the smallest useful thing: isolate one costly path, remove its demonstrated unnecessary work, and verify that scenario. Reuse existing profiling, query-plan and regression tools; do not mandate a profiler or new infrastructure.

## Measure and reduce

- Record the baseline scenario, inputs, load, build/configuration and capture window. Compare equivalent before/after windows, documenting build differences and warmup/cache state. Choose relevant latency, throughput, total time, call count and per-call cost; use tail percentiles/max and call chains for spikes. Distinguish self from inclusive time: serialization or boundary copying may be charged to the caller. Scheduler cadence is not frame presentation; CPU, GPU and asset claims need corresponding measurements.
- Remove repeated reads, N+1 queries, excess payloads, allocations and conversions before introducing cache or scheduling. Hoist only values invariant within the intended scope. Reuse a narrow accessor when only one field is needed instead of copying a whole object.
- If residual spikes justify batching or yielding, preserve operation order, values frozen at the original snapshot boundary, and targeted delivery. After await/yield, revalidate stable target identity and operation preconditions; a recycled handle or array position is not identity. Do not slow required interactions by blindly increasing waits.

## Checks only for changed mechanisms

- SQL: inspect EXPLAIN on representative data for query/index changes. Fewer selected columns reduce transferred data, not necessarily scanned rows.
- Cache: only if introduced or changed, define invalidation/lifetime and derived-state updates. Provider errors are not empty results. Reject stale bulk results when state changes during reads; late snapshots must not resurrect deleted records. Check failure, duplicate/out-of-order updates and reconnection where affected.
- Delivery/UI: retain intended recipients; send changes rather than full snapshots when appropriate. Stop unnecessary hidden-view work and batch DOM reads/writes only when that path changed.

Preserve authority, guarded updates, transactions and idempotency. Failed operations must not be published as successes.

## Verify and stop

Run affected behavior checks and actual before/after runtime measurements. Report work removed, comparable metric changes and correctness evidence. Static checks, CI or disk parity alone do not prove improvement; source changes are not runtime activation. Stop when the measured target is resolved without regression. If comparable runtime evidence is unavailable, report improvement as unverified; do not expand into a broad audit or activate services implicitly.
