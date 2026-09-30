---
name: omp-ttsr-rule-calibration
description: "Calibrate one noisy OMP TTSR rule or one repeated user correction using labeled episodes and held-out CLI checks."
---

# Calibrate one TTSR rule

Deliver one candidate and verification report. Scope: one noisy rule or repeated correction, using the smallest relevant sample. No full-history scan, mandatory parallel agents, active rules/settings changes, or unrelated cleanup. Stop if evidence cannot distinguish useful matches from noise.

Do the smallest useful thing: adjust only the evidenced condition and scope in a candidate copy; do not build a mining pipeline or rewrite the rule library.

## Label before matching

Read relevant JSONL user/assistant/toolResult messages, tool_execution_start arguments, and TTSR injections. Episode: user follow-up plus preceding assistant text, recent tool calls/results, and fired rules; retain session ID and ordering. Expand context only for unclear attribution.

Label correction, ordinary follow-up, or ambiguous; separately record failure evidence. Correction wording is a proxy, not proven failure. Adapt vocabulary to the sessions' language; no universal regex.

Reserve held-out sessions with known positives and plausible negatives before drafting. Include read-only commands, quoted examples, helper code, and unrelated tools. Compare old/new hits, preserved positives, false positives, correction-proxy precision, sampled base rate/lift when defined, and session coverage. Report denominators/uncertainty; no historical thresholds or holdout tuning.

## Draft narrowly

Back up an existing rule before editing its working copy; retain rollback path. Serialize regex strings using JSON escaping (`json.dumps`) into YAML; inspect parsed values. Use explicit `scope: ["text"]` for prose or evidence-supported tool scopes such as `["tool:bash", "tool:eval"]`. Claim-interruption rules may require `interruptMode: always`; leave global repeat/interrupt settings unchanged.

## Verify with the installed CLI

Run `omp --version` and `omp ttsr --help` first. For every positive and negative snippet, run:

```sh
omp ttsr test --json --rule candidate.md --source text --file snippet.txt
omp ttsr test --json --rule candidate.md --source tool --tool bash --file snippet.txt
```

Select the actual tool; supply `--path`/`--agent` when scoped. Explicit sources avoid file-extension inference. Assert expected entries in `triggered`/`notTriggered`, not just exit success. Test wrong-source/tool negatives too.

Run `omp ttsr list --json` in a disposable project discovering the candidate locally; confirm its name, path, conditions, and scope. Listing is not isolated by `--rule` and does not prove triggering. Stop on registration errors or lost positives. Report commands/results, remaining uncertainty, and backup path; leave activation separate.
