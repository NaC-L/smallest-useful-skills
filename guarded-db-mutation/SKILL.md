---
name: guarded-db-mutation
description: "Apply an explicitly requested, scoped database row change with preconditions, backups, and readback."
---

# Guarded database mutation

Only for an explicitly requested, precisely scoped mutation. Audit requests authorize reads, not repair. Historical recipes are not current schema or authority.

Do the smallest useful thing: change only verified target rows and required fields. Do not fix adjacent records, redesign the schema, or reconcile unrelated historical data.

1. Verify database/environment, schema, engine, unique key and intended effect. SELECT the identical predicate first; record expected keys, values and count. A name or IP alone need not uniquely identify a row or owner.
2. Back up affected rows and restoration requirements; verify readability and record a secret-safe path. Inventory FK/cascade, triggers, counters and runtime caches. Bulk deletion/schema changes need a separate plan and appropriate backup.
3. Use parameterized statements and a supported transaction. Lock or guard against concurrent drift using expected old values/version. Assert affected rows and rollback on unexpected count. Make retries idempotent; preserve higher privileges when required. Non-transactional tables/auto-committing DDL need a recovery plan before writing.
4. SELECT within the transaction; commit only if expected values/counts match. Read again after commit. Report actual effects without exposing sensitive rows.
5. Distinguish repaired rows from runtime caches and future overwrites. Never restart/reload implicitly. State reconciliation and rollback boundaries: row restoration may not undo triggered/external effects.

Stop if identity, expected count, current state or recovery cannot be established. No broad WHERE, silent partial repair, or authorization derives from this skill.
