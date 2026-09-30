---
name: instrument-data-chart
description: "Create a data chart in the black, cyan, pixel-crisp Instrument style, with verifiable values and an evidence-backed caption."
---

# One claim, one chart

Use for a requested data visualization in this visual language, not arbitrary graphs or whole-product redesign. Do the smallest useful thing: create one chart with the existing renderer and data pipeline. Do not add a chart framework or interactions unless needed.

1. Establish the intended comparison, actual data source, units, denominator, time window and uncertainty. Missing is not zero. Never invent benchmark scores; synthetic examples must be unmistakably labeled. If the claim lacks evidence, show an honest comparison instead.
2. Choose marks for the question: bars for category comparisons, paired bars/dumbbells for before-after, scatter for two-metric tradeoffs, lines for ordered progression, composition only for genuine parts of a whole. Use a table when exact values matter more than geometry. State scale/domain explicitly; use a zero baseline for magnitude bars unless a justified alternative is clearly labeled.
3. Apply [the compact style specification](references/instrument-style.md): black, off-white text, restrained cyan, square marks, hairlines, tabular mono numerals, selective Bayer dithering. Preserve an existing chart library; customize its marks/theme rather than replacing it. Prefer static output. Do not copy third-party shipped code or bundle unlicensed fonts.
4. Show meaningful units, labels and a caption stating the supported finding plus methodology. Derive annotations from the same source values as marks; distinguish relative percent from percentage points and handle zero denominators. Do not color a baseline as a loser without evidence.
5. For web charts, provide an accessible name and equivalent data table/text; do not rely on color or hover alone. Resize using actual display dimensions and device pixel ratio when using canvas. Honor reduced motion and clean up resize/animation handlers if added.

## Verification and stop

Reconcile every plotted value, delta and total with the input. Render the actual output at its delivery size and one narrow layout where relevant; inspect clipping, legend/annotation collisions, glyphs, contrast and pattern legibility. Check any added tooltip/keyboard path. Report the artifact and remaining uncertainty. Stop after the requested chart passes; do not claim statistical significance or a general performance win from styling.
