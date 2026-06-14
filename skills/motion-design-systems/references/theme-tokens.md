# Theme Tokens Reference

Use this when a user requests brand cleanup, color consistency, or replacement of blue/green/purple/etc. accents.

## Tokenize First

Prefer named tokens:

```css
:root {
  --color-bg: #f7f3ec;
  --color-ink: #111111;
  --color-muted: rgba(17, 17, 17, 0.62);
  --color-accent: #ef6f22;
  --glass-fill: rgba(255, 255, 255, 0.52);
  --glass-border: rgba(255, 255, 255, 0.72);
}
```

## Search Targets

- CSS variables.
- Raw hex colors.
- RGB/RGBA values.
- SVG `fill` and `stroke`.
- Canvas/WebGL constants.
- Inline HTML styles.
- Duplicated start/carryover frames.

## Exclusions

Do not recolor unless explicitly requested:

- Logo artwork.
- Product demo recordings.
- Screenshots of real products.
- User-provided reference images.

## Proof

Check at least one proof frame per affected scene and one proof frame from the next scene if it carries over the same visual.

