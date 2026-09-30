---
name: verified-file-deploy
description: "Verify backups, drift, byte integrity, and activation for an explicitly requested remote file deployment."
---

# Verified file deploy

This skill grants no permission. Deploy, push and restart/reload require separate explicit authorization; do not use it for ordinary local edits.

Do the smallest useful thing: transfer only files required for the requested change using the existing deploy runner. Do not introduce deployment infrastructure, migrate services, or widen the release.

1. Verify exact environment, host, destination and permitted actions. Read current target and reconcile drift. Validate and deduplicate all destinations before writing; exclude secrets and unrelated changes.
2. Run the changed path's full relevant test module and syntax/build checks. Review generated artifacts for unintended behavior. Record local byte hashes; preserve target encoding/EOL.
3. Back up original target bytes before overwrite and verify backup hashes. Use unique temporary paths. Bound concurrency for independent destinations; order each backup -> transfer -> verify chain. Serialize shared targets, migrations and activation.
4. Verify every deployed file by readback or trustworthy target-side SHA256. A successful transfer or hash-looking filename is insufficient. Stop on mismatch; list partial writes and backups. Multiple transfers are not automatically atomic.
5. Activate only if separately authorized. Verify an ordinary functional request, relevant logs and actual UI where applicable, not just process liveness. Rollback requires permission unless already covered by the approved plan.

Report files, tests, backups, hash results and one accurate state: staged / synchronized on disk / activated / runtime-verified. Disk parity does not prove running behavior. Archived commands/hosts need fresh verification.
