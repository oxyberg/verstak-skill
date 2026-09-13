---
name: verstak
description: Implement screens and components from Figma with pixel-perfect fidelity. Use for Figma-to-code work («сверстай по Figma», «сверстай экран по макету») or explicit requests for Верстак / $verstak; not for generic UI redesign.
---

# Verstak

Deliver working UI that reproduces the requested Figma design in the project's existing stack. Preserve its design system, assets, meaningful containers, states, and responsive behavior. The user's explicit choices take precedence over this skill's defaults.

## Source and scope

Use the exact frame, component, or variant requested. Obtain structured Figma context and a screenshot of the same target, including its reference dimensions. Reuse context already verified in the task; a small follow-up does not require rediscovering the file or design system. Read [references/figma-mcp.md](references/figma-mcp.md) when provider selection, missing context, or connection errors need guidance. Setup instructions are needed only for setup or repair.

Inspect the relevant repository components, tokens, fonts, assets, and conventions. Resolve routine choices from the source and code. Ask only when an unresolved choice materially changes the result, such as conflicting design-system mappings with no reliable evidence. Continue independent work while missing input is pending. If Figma is unavailable, distinguish supported work from design details that remain unverified; a user-requested screenshot approximation has a different fidelity limit.

## Fidelity constraints

- Reuse matching code components and design tokens, including available Code Connect mappings. When no design system exists, use measured Figma values; local names for those values are fine, but do not invent a replacement visual system.
- Preserve containers that control sizing, alignment, clipping, and responsiveness. Translate Auto Layout and constraints into an appropriate layout model; use absolute positioning for actual overlaps or positioned elements. Extract repeated components where useful, without forcing an atomic-design hierarchy.
- Match geometry, spacing, typography, line height, letter spacing, colors, borders, effects, and opacity. Preserve asset aspect ratios and fill/fit/crop behavior. Use original SVG or raster assets; do not substitute similar icons, emoji, or CSS drawings for available originals.
- Exclude presentation-only platform chrome such as browser bars and system indicators unless it belongs to the requested product.
- Implement specified variants, interaction states, and motion using their source values. Where absent, infer necessary accessible control behavior, including keyboard focus and disabled feedback, within the design language. Respect reduced motion; do not add animation solely to fill missing specifications.
- Follow supplied responsive frames and resizing constraints. Infer missing behavior from containers and content, preserving hierarchy, readability, touch targets, and freedom from unintended overflow. Identify inferred behavior separately from extracted specifications.

## Verify and finish

For UI implementation, run the project and inspect a capture at the reference dimensions. Compare it with the Figma screenshot; use an overlay or pixel diff when useful to locate discrepancies. Correct observable mismatches, especially container geometry, text wrapping, baselines, clipping, and assets. Do not claim visual fidelity from code inspection alone.

Check affected interactive states and responsive behavior at supplied sizes and representative nearby widths when resizing applies. Scale checks to the change: a spacing correction needs focused visual verification; changed layout or behavior needs broader relevant coverage. Run required project checks and relevant existing tests. Repeat or broaden verification only after a change, failure, or unresolved concern warrants it.

Continue through implementation, local execution, inspection, and fixes within the authorized task. Finish when the requested UI is implemented, observable discrepancies are resolved, and relevant checks pass. If access, tooling, or a platform limitation prevents verification or exact reproduction, complete unaffected work and state the precise remaining limitation instead of claiming a perfect match or looping indefinitely.

Respond briefly in the user's language with the result and verification performed. Include assumptions, remaining deviations, or blockers only when present.
