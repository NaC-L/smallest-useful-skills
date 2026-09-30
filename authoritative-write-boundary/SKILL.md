---
name: authoritative-write-boundary
description: "Harden an untrusted write or persistence path using canonical backend authority and complete field-level validation coverage."
---

# Intent is not authority

Use when untrusted input can change protected persistent state, prices, ownership or entitlements. Do the smallest useful thing: secure the actual write boundary and its bypass routes, not unrelated services. Reuse existing authorization, transaction and test facilities.

1. Trace input through every writer of the affected state, including generic saves, background sync and alternate paid/free paths. Identify canonical identity/session, permission, ownership/scope, entitlement, price and allowed field values relevant to this operation. Client-provided role, price, ownership and full-object blobs are intent, never authority.
2. Recompute security decisions from trusted backend state. Validate types, ranges and allowed fields before mutation. Bind authorization to the actual target and operation; serialize conflicting writes or use guarded/versioned updates where required. Use transactions, replay protection, rate limits and idempotency only where the operation needs them. Never acknowledge a failed write as success.
3. For client-applied state with protected persistent fields, use exact grant plus clamp: commit payment/entitlement consumption and only the authorized field=value grant atomically, or through a durable idempotent workflow with failure recovery. A balance check alone is not payment; retries must not double-charge or leave a failed grant charged. Never authorize every client difference because one field was purchased. On every untrusted write route, reject or replace protected fields with canonical values; unrelated fields still need their own existing validation.
4. Load the baseline from trusted persistent state. Missing authority for a protected write fails closed; do not invent default values that erase legitimate data. Any explicitly unmanaged fields/entities need a separate documented authorization policy, not automatic pass-through. Compare protected fields and all legitimate paid/free mutation maps in both directions: no protected mutation bypasses authorization, and every valid grant survives synchronization.

## Verification and stop

Test an authorized change and its persistent readback, denied identity/ownership, tampered price/protected fields, and direct-save bypass. Where affected, test authorized free paths, buying one field while injecting another, missing baseline, retries and concurrent updates. Inspect the actual service entrypoint, not only the validator. Keep real secrets and personal data out of logs, fixtures and exception text.

Stop when all affected writers enforce the same authority and valid behavior survives. A forward fix does not repair historical rows: investigate old data separately and preserve evidence. Missing audit entries alone do not prove unauthorized data. Never deploy, reset data or mutate production without explicit authorization.
