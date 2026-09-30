---
name: changed-contract-verification
description: "Verify changed callback, persistence, replication or integration contracts across real consumer boundaries."
---

# Verify a changed cross-boundary contract

Use when a change crosses a callback, persistence, replication or integration boundary, not for every edit. Do the smallest useful thing: prove the changed consumer-visible contract using the existing runner and entrypoint; leave unrelated surfaces, infrastructure and frameworks alone.

1. Name the producer, consumer and boundary. Write a concrete observable invariant: a callback settles once, an acknowledged save survives a reload, or a replicated update reaches the intended consumer. Specify inputs, output/error, ordering and ownership relevant to the change. Trace the actual entrypoint to the boundary; testing a private helper alone can miss a bypass.
2. For a regression, run the reproducer against the broken implementation and retain its observed failure, then run the same assertions against the fix. A green test without a failing control does not establish regression coverage. Include one unchanged valid case. For new behavior, exercise success and the changed rejection/error boundary.
3. Reuse existing fixtures and runner. Assert consumer-visible outcomes rather than private call counts, unless call count is itself the contract. Run the full affected test file/module and applicable syntax/type/build checks. A mock returning success cannot prove durable storage or delivery.
4. Select only gates reached by the changed path:
   - UI callbacks: actual UI response, focus release, close during pending async work, and relevant console/network errors.
   - Replication: direction, absent consumer/entity, resynchronization and lifecycle cleanup.
   - Persistence: reload/readback, failure rollback, retry/idempotency if applicable; exercise a direct-save route separately if it can bypass changed validation.
   - Authorization: valid and denied inputs through the same boundary, not merely validator unit tests.
5. Smoke the changed path through the actual application entrypoint in an authorized local/test runtime. Confirm which artifact/configuration that runtime loaded. A file on disk or a live process does not prove the changed code is active.

Report static/build, behavioral/mock, disk and actual-runtime evidence separately, with commands and observed results. Stop only when the changed contract and unchanged case are verified; if runtime or activation is unresolved, report that blocker and do not claim the fix is runtime-verified.
