---
name: ui-interaction-lifecycle
description: "Verify changed dialog or panel states, save/cancel behavior, keyboard focus, close paths and resource cleanup."
---

# Verify UI interaction lifecycle

Use when changing a dialog or panel's state transitions, input ownership or lifetime. Do the smallest useful thing: trace the changed flow's open, action and close paths, reuse existing components and test/runtime tools, and repair only the broken transitions. Do not introduce universal dragging or a new state framework.

1. Read the existing state and input contract. Distinguish loading, empty data, no results, unavailable, failure and success where possible in this flow. Failed loading is not an empty result. Show rejection reasons and meaningful progress; do not substitute an arbitrary timer for actual operation progress. Error text names an available next action, never an invented retry. Prevent misleading repeat submission while an operation is pending.
2. Follow edit, save and cancel paths. Save commits only the intended changes; cancel or Escape must not accidentally commit a preview. Restore the last committed state where previews exist. If cancellation is supported, verify whether it cancels the operation or only dismisses the UI; closing must not imply an in-flight operation was undone.
3. Exercise keyboard and pointer paths. Give controls accessible names and visible focus. Establish sensible opening focus; contain focus only for a modal that owns interaction. Verify the applicable Escape/close behavior, release captured input and restore focus to the opener or a valid fallback. Check close button, cancellation, successful completion, navigation, failure dismissal and component destruction when those branches exist.
4. On close or teardown, stop panel-owned timers, polling and animation loops, and detach listeners and observers no longer needed. Preserve shared or still-required work. Exercise late asynchronous completion: it must not reopen the dismissed panel or steal focus. Repeat open/close to detect duplicated callbacks or stale state using existing instrumentation.
5. Only if persisted layout exists, test save, cancel, reset and reload. Clamp position and size within the viewport on load, resize and scale changes. Recover invalid or non-finite stored layout to defaults without clearing unrelated preferences. Keep reset accessible; do not add persistence to satisfy this check.

Verify relevant transitions on the real surface and with existing targeted tests where available. Screenshots are not interaction evidence. Stop once applicable states, close paths, focus restoration and cleanup are observed; identify any runtime verification gap.
