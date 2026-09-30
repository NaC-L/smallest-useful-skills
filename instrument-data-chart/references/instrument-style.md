# Instrument chart style

A compact, independently written recipe derived from the supplied design study of stencil.so. These are styling recommendations, not an assertion that every source chart shares these settings. Use values as a starting point; readability at the actual output size wins. This is a data-chart theme, not a mandate for application UI.

## Palette and typography

- Background: `#000000`; primary text: `#ededed`; secondary: `#a1a1a1`; small muted labels no darker than `#757575` on opaque black. Verify actual contrast after opacity/background compositing.
- Main series/accent: cyan `#44cfff`; baseline: neutral grey. Purple `#a86af4` for another highlighted series; green `#4ade80`, amber `#f5b04a`, red `#f4644a` only for warranted status/deltas. At most four hues; distinguish series with text and outlined/filled marks as well.
- Numbers, axes and captions: a licensed monospace font, tabular numerals. Free options include Geist Mono, JetBrains Mono and IBM Plex Mono; do not assume Berkeley Mono is licensed. Titles/prose: a restrained sans-serif such as Geist or the project's existing font.
- Starting sizes: axes 11px, data labels 11-13px, captions 10-11px. Increase these for delivery-scale readability; never bake unreadable miniature labels into an export. Uppercase/tracking is optional for compact metadata, not long content.

## Frame and marks

- A simple figure with subtle 1px border, no decorative shadow or gradient. Allow label gutters; a desktop 760px-wide chart is a reference, not a fixed required viewport.
- Dashed grid: 1px white at about 6% opacity, dash pattern `[2,4]`. Avoid an unnecessary second axis border. Pixel-align hairlines in the renderer's coordinate system; account for device pixel ratio and stroke width rather than blindly adding 0.5 at every scale.
- Square points, about 6-8px; optional outlined square halo for emphasis. Lines about 1.5px; dashed secondary/projection lines must have a legend. Bars may be solid or lightly tinted with a 1px outline. No bevels or glossy gradients.
- Prefer a visible data label or concise derived-delta annotation to decorative badges. Keep precision consistent with input accuracy; do not hide important differences with rounded tick labels.

## Selective ordered dithering

Use a flat or wire treatment for dense charts. Dither selected area fills, composition wedges or highlighted tiles; do not texture every mark or text background.

For a Bayer 8x8 ordered threshold matrix with entries 0-63, a cell at `(x,y)` is painted when normalized intensity exceeds `(B[y % 8][x % 8] + 0.5) / 64`. Start with 2px cells, or 4px for a large poster. Generate the standard matrix independently; do not copy shipped site implementations. Keep the data boundary and mark geometry crisp. If texture/noise is used, seed it deterministically so redraw/export does not flicker or suggest changed data.

## Output and accessibility

- A caption contains the supported finding and compact method/sample limitations. Include units and denominators; an arrow suggesting 'better' needs a defined metric direction.
- For canvas, set backing dimensions from CSS dimensions times device pixel ratio, transform once, and redraw on resize rather than stretching the bitmap. Disconnect observers and cancel animation on unmount. SVG or a DOM grid is equally valid.
- Static is the default. If animation serves the task, the original style suggests 12fps stepped motion; respect `prefers-reduced-motion` with a static equivalent. Do not animate merely to reproduce branding.
- Provide a text/table equivalent for canvas data and keyboard/touch access to any information otherwise confined to hover. Non-color signs or shapes retain meaning without hue discrimination.
- Render the final artifact and inspect desktop/narrow layouts where applicable. Test zero/missing values and long labels when present; verify the caption, visible values and underlying data agree.
