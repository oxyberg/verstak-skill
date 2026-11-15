---
name: verstak
description: Implement screens and components from Figma with pixel-perfect fidelity. Use for Figma-to-code work («сверстай по Figma», «сверстай экран по макету») or explicit requests for Верстак / $verstak; not for generic UI redesign.
---

# Verstak

Deliver working UI that reproduces the requested Figma design in the project's existing stack. Preserve its design system, assets, meaningful containers, states, and responsive behavior. The user's explicit choices take precedence over this skill's defaults.

## Choose the smallest sufficient scope

- Local correction: inspect the affected node, its controlling container, matching code, and nearby dependencies. Reuse verified context; expand only when inherited styles, layout, or shared components require it. Verify the changed area and affected neighbors.
- Component or state change: inspect the component, relevant variants, and its integration. Verify affected states, keyboard behavior, and resizing where applicable.
- New screen or structural layout change: inspect the target frame, reusable components, and supplied responsive frames. Verify the full composition and affected responsive behavior.

Choose scope silently from the request; all scopes retain the fidelity constraints below. Do not perform a full-file or design-system audit for a local change.

## Source and implementation

Use the exact frame, component, or variant requested. Obtain structured Figma context and a screenshot of the same target, including its reference dimensions. Reuse context already verified in the task; a small follow-up does not require rediscovering the file or design system. Read [references/figma-mcp.md](references/figma-mcp.md) when provider selection, missing context, or connection errors need guidance. Setup instructions are needed only for setup or repair.

Use one working Figma provider; switch only for a specific failure or missing capability. Request only needed nodes and fields; avoid duplicate structural reads and whole-file dumps. Batch independent reads where supported. Load supporting references only for the applicable operation, while honoring required tool prerequisites.

Inspect relevant repository components, tokens, fonts, assets, and conventions. Before coding dependent UI, resolve font families/weights, original assets, controlling dimensions, and existing component mappings to prevent rework. Ask only when an unresolved choice materially changes the result; continue independent work meanwhile. If Figma is unavailable, separate supported work from unverified design details; honor a user-requested screenshot approximation without claiming extracted specifications.

For long or multi-screen tasks, keep a compact task-local evidence note: target IDs and source revision if available, reference dimensions, controlling layout/type/token values, mappings, asset paths, inferences, and unresolved questions. Reuse it after context loss. Refresh affected evidence when the target, design, or implementation changes; never treat an old note as proof of an unchanged source. Skip the note for a small self-contained correction.

## Fidelity constraints

- Reuse matching code components and design tokens, including available Code Connect mappings. When no design system exists, use measured Figma values; local names for those values are fine, but do not invent a replacement visual system.
- Preserve containers that control sizing, alignment, clipping, and responsiveness. Translate Auto Layout and constraints into an appropriate layout model; use absolute positioning for actual overlaps or positioned elements. Extract repeated components where useful, without forcing an atomic-design hierarchy.
- Match geometry, spacing, typography, line height, letter spacing, colors, borders, effects, and opacity. Preserve asset aspect ratios and fill/fit/crop behavior. Use original SVG or raster assets; do not substitute similar icons, emoji, or CSS drawings for available originals.
- Exclude presentation-only platform chrome such as browser bars and system indicators unless it belongs to the requested product.
- Implement specified variants, interaction states, and motion using their source values. Where absent, infer necessary accessible control behavior, including keyboard focus and disabled feedback, within the design language. Respect reduced motion; do not add animation solely to fill missing specifications.
- Follow supplied responsive frames and resizing constraints. Infer missing behavior from containers and content, preserving hierarchy, readability, touch targets, and freedom from unintended overflow. Identify inferred behavior separately from extracted specifications.

## Verify and finish

Run the project and inspect a capture at the reference dimensions. Compare the same state, scale, and crop with the Figma screenshot. From each comparison, collect concrete discrepancies and fix a related batch, prioritizing container geometry, fonts/text wrapping, and assets before decoration. Recapture affected views after changes; avoid a screenshot for every CSS property. Do not claim fidelity from code inspection alone. For overlay/diff assistance or persistent comparison noise, read [references/visual-check.md](references/visual-check.md).

Check affected interactive states and responsive behavior at supplied sizes and representative nearby widths when resizing applies. Scale checks to the change: a spacing correction needs focused visual verification; changed layout or behavior needs broader relevant coverage. Run required project checks and relevant existing tests. Repeat or broaden verification only after a change, failure, or unresolved concern warrants it.

Finish when the requested UI is implemented, relevant checks pass, and the latest comparison leaves no concrete unresolved defect. Do not invent polish work after that point. For a persistent discrepancy, diagnose its cause before another edit; do not repeat speculative tweaks. A fixed iteration or token cap must not silently waive a defect. If access, tooling, or a platform limitation prevents verification or reproduction, complete unaffected work and report the precise remaining limitation instead of claiming a perfect match or looping indefinitely.

Respond briefly in the user's language with the result and verification performed. Include assumptions, remaining deviations, or blockers only when present.
