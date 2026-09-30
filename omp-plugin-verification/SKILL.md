---
name: omp-plugin-verification
description: "Verify a changed OMP plugin against the installed host, including the actual event or UI behavior."
---

# Verify an OMP plugin change

Use for a specific plugin change or compatibility failure. Do the smallest useful thing: verify and fix the changed path, reuse the plugin's runner, and leave unrelated hooks, packaging and host configuration alone. This is not a release or installation procedure.

1. Inspect the plugin's source, package scripts, tests, installed OMP version and relevant host API. Identify the event/hook contract and one reproducing scenario before editing. Do not patch the compiled host binary.
2. Add a regression case for the reported behavior and a relevant unchanged case. For message transforms, preserve protected code, paths, URLs and structured/provider content; test those boundaries only when the change touches them. Keep display-only styling out of persisted text.
3. Run the relevant full test file/module and the existing package's applicable type/build checks. Use the lockfile and current dependencies; do not reinstall or upgrade them by habit.
4. Exercise the plugin in an isolated local OMP session using the installed version's supported mechanism; inspect CLI help before using an explicit extension path such as `omp -e <entrypoint>`. Prefer temporary loading over persistent linking. Plugin execution may call external APIs: use mocks/local inputs unless those calls are authorized.
5. Observe the actual changed surface. A stored message is not proof of streamed UI behavior; a finalized hook cannot undo text already displayed. Check the resolved plugin path to distinguish a linked checkout from an installed package.

Stop when the regression, unchanged case and host scenario are verified. If runtime observation is unavailable, report that exact gap. Do not publish, tag, push, install persistently or restart another session without an explicit request.
