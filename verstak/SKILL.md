---
name: verstak
description: Implement production-ready, pixel-perfect screens, components, and UI elements from Figma while preserving the source design system, assets, containers, responsive behavior, states, and motion. Use whenever the user asks to build, implement, or lay out an interface from a Figma design, URL, frame, node, screenshot backed by Figma, or design specification. Russian triggers include «сверстай по Figma», «сверстай экран по макету», and «сверстай компонент». Also use whenever the user explicitly invokes verstak, Верстак, верстак, /verstak, or $verstak.
---

# Verstak

Reproduce Figma interfaces in code with 1:1 visual fidelity. Treat the design, its components, variables, styles, assets, Auto Layout, and constraints as the source of truth. Make assumptions only for viewport adaptability, dynamic content, and states absent from the design. Communicate in the user's language unless they request otherwise.

## Required workflow

### 1. Verify the Figma MCP connection

Read [references/figma-mcp.md](references/figma-mcp.md) before analyzing the design.

1. Discover the available Figma MCP tools and identify the provider: the official/base Figma MCP or `@gethopp/figma-mcp-bridge`.
2. Make a safe read-only call that confirms access to the target file or selected node. Do not treat configuration alone as proof that the connection works.
3. For the bridge, verify that its Figma plugin is open in the target file and that the file appears in `list_files` or an equivalent call.
4. If the connection is missing or broken, stop the design workflow, report the exact failure, and help configure one of the supported providers. Do not replace unavailable Figma context with guesses or manual interpretation of a preview.

### 2. Inspect the project and design source

1. Locate the exact Figma frame, component, or variant to implement. If a link targets an oversized node, fetch its structural map first, then request only the relevant child nodes.
2. Obtain both structured design context and a reference screenshot. With the bridge, use the closest equivalents to `get_design_context`/`get_node` and `get_screenshot`.
3. Inspect the repository to identify its stack, existing components, styles, tokens, fonts, assets, layout primitives, and project rules. Follow the established architecture and conventions.
4. Record the reference frame and viewport dimensions before implementation.

### 3. Find the design system

1. Search the codebase and Figma for a design system: libraries, variables, local styles, component sets, variants, Code Connect mappings, and existing implementations.
2. If multiple systems exist, library access is unavailable, or the mapping is ambiguous, ask the user one specific question. Do not ask for information that can be established reliably through code or MCP.
3. When a design system exists, reuse its components and tokens. Export any missing permitted styles and assets from Figma when needed.
4. When no design system exists, do not invent tokens, token names, icons, colors, typography, radii, shadows, or spacing. Use exact Figma values and export the original SVG or raster assets. Do not add an icon library to replace assets already available in Figma.

### 4. Understand and decompose the structure

1. Read the layer hierarchy, Auto Layout, constraints, grids, clipping, absolute positioning, component instances, variants, and nested containers.
2. For a screen, identify modules, then decompose each module into molecules and atoms.
3. For an individual component, identify its atoms, slots, variants, states, and public API.
4. Reuse repeated entities, but do not abstract a one-off element solely to satisfy formal atomic design.
5. Preserve the semantics and boundaries of Figma containers. Do not flatten nesting that controls sizing, alignment, clipping, or responsiveness.

### 5. Implement exact geometry and visuals

1. Transfer dimensions, spacing, padding, alignment, colors, borders, radii, shadows, blur, opacity, typography, line height, letter spacing, icons, and images 1:1.
2. Preserve intrinsic aspect ratios and Figma's `fill`, `fit`, and `crop` behavior.
3. Prefer a layout model that matches Auto Layout and constraints over a brittle collection of absolute coordinates. Use absolute positioning only when it exists in the design structure or is required for overlap.
4. Do not reproduce platform chrome shown only for presentation: browser frames, address bars, system status bars, home indicators, keyboards, or other elements supplied by the target platform. Implement them only when explicitly identified as part of the product.
5. Do not replace exact assets with similar symbols, emoji, CSS shapes, or third-party icon packages.

### 6. Implement states and motion

1. Find component variants, prototype interactions, hover/pressed/focus/disabled/loading/error states, and motion styles. Inspect the related component set, not only the selected node.
2. Implement specified states and transitions with their exact easing, duration, delay, and animated properties.
3. If states are absent, add the necessary hover, focus-visible, pressed, and disabled states without changing the design language. Add brief, appropriate motion and report these decisions as inferred rather than extracted from Figma.
4. Support keyboard input, reduced motion, and accessibility. Never let animation obstruct interaction.

### 7. Implement responsive behavior

1. Find alternate frames, breakpoints, Auto Layout resizing rules, min/max sizes, wrapping, constraints, and container behavior.
2. Implement every explicitly defined change at its reference size.
3. If resizing behavior is absent, infer it from containers and content: preserve hierarchy, priority, readability, touch targets, and freedom from unintended overflow. Treat these rules as assumptions.
4. Test at least the reference viewport, one adjacent smaller size, and one adjacent larger size when the target platform supports resizing.

### 8. Validate pixel-perfect fidelity

1. Run the project and capture the implementation at the exact dimensions of the reference Figma frame.
2. Compare the images visually and, when possible, with an overlay or pixel diff. Check geometry, text baselines, clipping, colors, shadows, radii, and assets.
3. Fix discrepancies iteratively. Do not declare completion after one pass or judge fidelity from code alone.
4. Validate interactive states, motion, responsive sizes, and dynamic content separately.
5. Run the project's relevant tests, lint, and type checks.

## Completion criteria

Finish only when:

- the MCP has successfully read the target Figma file or node;
- the component structure follows the design's meaningful containers;
- the available design system is reused and missing tokens or assets are not invented;
- the reference viewport matches the design 1:1 except for explicitly documented technical limitations;
- states, motion, and responsiveness are implemented and verified;
- platform chrome is not duplicated;
- the final response lists the implementation, verification performed, assumptions, and remaining deviations.
