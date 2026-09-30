---
name: ui-surface-acceptance
description: "Check an explicitly changed UI on its real surface for hierarchy, responsive content, contrast and applicable visual states."
---

# Accept a changed UI surface

Use for visual or accessibility acceptance of an explicitly changed screen or component. Do the smallest useful thing: check that surface and its relevant states, reuse existing components, design tokens and inspection tools, and fix observed defects rather than redesigning the application.

1. Read the changed flow and nearby components. Identify the title, decision-relevant content and primary next action. Keep secondary actions subordinate; danger alone does not make an action primary. Use spacing, grouping and typography before adding decorative emphasis. Reuse established control behavior and sizing conventions.
2. Open the actual application surface. A mockup or isolated preview is a precheck, not acceptance. Select viewports from the supported layout and the changed component's constraints, including a narrow case and relevant aspect-ratio changes. Keep the primary action and close route reachable; shrinking all text is not responsive adaptation.
3. Exercise long labels, supported localized scripts, large formatted values, multiline descriptions and dense lists where applicable. Check wrapping, font coverage, alignment and overflow. Decision-critical information must remain accessible rather than existing only in clipped text. Do not add search or new navigation to small lists by default.
4. Check text against actual rendered backgrounds, including representative light, dark or variable imagery when present. Transparency and blur do not guarantee contrast. Require at least 4.5:1 for normal text and 3:1 for large text: at least 24 CSS px, or approximately 18.7 CSS px when bold. Treat other text as normal. Check permitted themes and opacity settings; meaning must not depend on color alone.
5. Open applicable loading, empty, no-results, unavailable, error and success states. Inspect keyboard focus, hover, pressed, selected and disabled styling where supported. Disabled reasons must not be hover-only; selected and hover states must differ. Check layout stability during loading and overlap with surfaces that actually coexist.

Record viewport, background and state with evidence. A screenshot proves neither keyboard operation nor closing behavior: exercise those separately. Stop after the changed surface's relevant checks pass; report unobserved runtime cases explicitly.
