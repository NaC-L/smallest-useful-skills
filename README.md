# Smallest Useful Skills

Focused, English-language Markdown skills for coding assistants. Each has a specific trigger, one bounded outcome, and a verification gate. Use only the relevant skill; this is not an always-read checklist.

**Smallest useful thing:** solve the requested problem completely with the smallest justified change. Reuse existing tools, preserve unrelated work, and stop when the outcome is verified. Smaller does not mean skipping backups, regression checks or runtime evidence.

**Status: release candidate.** Collection tests validate packaging and documented safeguards, not guaranteed agent performance. Validate the skills on your own representative tasks before relying on them.

## Skills

### General engineering and interfaces

| Skill | Use when |
|---|---|
| [`instrument-data-chart`](instrument-data-chart/SKILL.md) | Create one evidence-backed chart in the black/cyan Instrument visual style. |
| [`ui-surface-acceptance`](ui-surface-acceptance/SKILL.md) | Check the actual changed UI for responsive readability, contrast and relevant visual states. |
| [`ui-interaction-lifecycle`](ui-interaction-lifecycle/SKILL.md) | Verify panel/dialog save, cancel, focus, close and cleanup behavior. |
| [`changed-contract-verification`](changed-contract-verification/SKILL.md) | A change crosses callbacks, persistence, replication or integration boundaries. |
| [`measured-performance-fix`](measured-performance-fix/SKILL.md) | A reproducible slow path needs a measured, behavior-preserving fix. |
| [`authoritative-write-boundary`](authoritative-write-boundary/SKILL.md) | Untrusted input reaches protected state or persistent writes. |

### Documents and guarded operations

| Skill | Use when |
|---|---|
| [`bounded-log-triage`](bounded-log-triage/SKILL.md) | A reported incident needs read-only evidence. |
| [`docx-stdlib-workflows`](docx-stdlib-workflows/SKILL.md) | Create/fill DOCX without python-docx. |
| [`guarded-db-mutation`](guarded-db-mutation/SKILL.md) | An exact database row change is requested. |
| [`verified-file-deploy`](verified-file-deploy/SKILL.md) | Remote file deployment is explicitly requested. |

### OMP-specific workflows

These four skills target [oh-my-pi](https://github.com/can1357/oh-my-pi); the rest are framework-independent.

| Skill | Use when |
|---|---|
| [`omp-memory-budget`](omp-memory-budget/SKILL.md) | Project memory overflows its verified injection budget. |
| [`omp-session-usage-audit`](omp-session-usage-audit/SKILL.md) | Recorded OMP tokens, costs or timing need analysis. |
| [`omp-ttsr-rule-calibration`](omp-ttsr-rule-calibration/SKILL.md) | One OMP rule is noisy or one correction keeps recurring. |
| [`omp-plugin-verification`](omp-plugin-verification/SKILL.md) | A plugin change needs tests and actual host verification. |

OMP workflows check the installed version instead of assuming historical defaults. No private scripts are required. Skills never grant permission to publish, mutate production, send messages or restart services.

The chart skill includes a compact Instrument style reference; it does not copy third-party implementation code. UI, verification, performance and authority skills are framework-independent, not game-server API guides. Visual acceptance and interaction lifecycle are separate checks, not mandatory companions. No routing skill is required: choose directly from each description.

## Use

```sh
git clone https://github.com/NaC-L/smallest-useful-skills.git
cd smallest-useful-skills
```

For a skill-aware assistant, copy only the selected skill directory into the skill search path documented by that assistant. Keep any bundled `references/` directory with it. Loading/reloading behavior is host-specific; this repository does not install itself.

Alternatively, ask an assistant with file access to read the chosen `SKILL.md` as task context:

> Read `ui-interaction-lifecycle/SKILL.md`. Fix the settings dialog so Cancel discards its preview and a late request cannot reopen it or steal focus. Preserve the shared fetch used by other views. Use existing tests and check the changed dialog in the local application.

The prompt names a bounded task; the skill supplies technical checks. No routing skill or blanket loading of all skills is needed.

## Check the collection

Requires Python 3.10 or newer; collection tests use only the standard library:

```sh
python -B -m unittest discover -s tests -v
```

These are document/package checks, not application integration tests, security certification or a benchmark of model quality.

## Sources and license

The Instrument chart recipe is independently written from a visual study of [stencil.so](https://stencil.so/). No third-party JavaScript, screenshots, font files or other site assets are distributed. Mentioned fonts retain their own licenses; inclusion in the recipe does not grant a font license. This collection is not affiliated with stencil.so or oh-my-pi.

The original skill text and collection code are available under the [MIT License](LICENSE).
