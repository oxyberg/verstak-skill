# Focused visual comparison

Use the project's existing capture tool. Set the reference viewport in CSS pixels and align image export scale/device pixel ratio; wait for fonts, images, and layout to settle. Match content, scroll position, theme, and interaction state. Disable or settle animations consistently for capture without removing product behavior. Reuse this capture setup throughout the task instead of rebuilding browser automation each iteration.

For a local fix, inspect the affected region and its neighbors. Include the controlling container when alignment or sizing is in question. New layouts require full-view checks. Capture supplied responsive sizes and representative nearby widths where resizing applies; check affected states separately. Do not replace required project checks with image comparison.

If an overlay will clarify a discrepancy, run the bundled helper (requires Python 3 and Pillow in an available environment):

```sh
python3 <skill-dir>/scripts/compare_images.py reference.png actual.png --output-dir /tmp/verstak-compare
```

It writes `overlay.png`, `diff.png`, and a compact JSON summary. It refuses unequal image dimensions instead of silently resizing a layout mismatch. If Pillow is unavailable, use existing image tools or direct inspection; dependency setup is not a prerequisite for ordinary verification.

Inspect the actual image and overlay, not just the score. The diff shows raw channel differences; antialiasing and rendering differences can create noise. Scores are diagnostic, never an automatic fidelity pass. Transparent inputs are composited on the same white background; use matching opaque captures for a different design background. Output paths must be task-local and separate from source assets.

Compare → collect concrete defects → fix related causes → recapture. If a defect persists, check the source measurement, controlling container, computed style, font loading, and capture alignment before another change. Finish after the latest inspection and relevant checks pass with no unresolved concrete defect. Report known platform or access limitations explicitly.
