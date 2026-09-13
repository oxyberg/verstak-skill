# Reading Figma through MCP

Read when choosing provider calls or diagnosing missing Figma context. Use tools actually exposed by the environment; names below describe capabilities, not a required server name or call sequence. Reuse successful reads from the current task when the target and design have not changed.

## Official or base Figma MCP

- `get_design_context`: structured context for the target node.
- `get_metadata`: a lightweight structural map when a target is large or a response is truncated.
- `get_screenshot`: the visual reference for the same node and variant.
- `get_variable_defs`, `get_code_connect_map`: styles and component mappings when relevant.

A successful target-node read verifies file access. `whoami` verifies authentication only and is unnecessary when the target read succeeds. Fetch child nodes selectively if the complete target is too large; retrieve variables, mappings, and assets as needed.

## `@gethopp/figma-mcp-bridge`

The bridge requires its Figma plugin to be running in the target file. Use `list_files` to resolve connected files when needed, then pass the correct `fileKey` to target reads. An empty file list usually requires opening the target file and running its bridge plugin.

Use `get_node` or `get_design_context` for structure, `get_screenshot` or `save_screenshots` for the reference, and `get_styles` or `get_variable_defs` for design-system information. Inspect `get_node_motion` or `get_motion_styles` when implementing specified animation. Use selection or document metadata only when the target cannot be resolved directly.

## Missing context or failed reads

Report the failed call and distinguish observed errors from suspected causes: configuration, authentication, file access, node selection, plugin state, or connectivity. Use an available equivalent read or request the minimum missing input. Retry after a relevant fix, rather than repeating the same failing call.

Continue repository inspection and work supported by verified context. Keep design-dependent decisions pending when their source is unavailable; do not present guesses as extracted values or claim an unverified match. If the user explicitly requests an approximation from a screenshot, honor that scope and explain its fidelity limits.

For an authorized setup or repair task, read the applicable section of [mcp-setup.md](mcp-setup.md).
