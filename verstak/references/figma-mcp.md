# Verifying Figma MCP

Support two provider types. Discover the tools that are actually available, then verify them with a read-only call. Do not require a particular MCP server name when its tool set identifies the provider unambiguously.

## Official or base Figma MCP

Look for the following capabilities; exact tool names may vary:

- `get_design_context` — structured context for an exact node;
- `get_metadata` — a lightweight map of a large node;
- `get_screenshot` — the visual reference;
- `get_variable_defs` — variables and styles;
- `get_code_connect_map` — mappings between Figma components and code;
- `whoami` — remote authentication verification, when available.

Verify the connection with `whoami`, metadata, or a screenshot call for the Figma URL/node supplied by the user. A successful `whoami` confirms authentication but not access to a particular file, so verify the target node as well.

Use this implementation sequence:

1. Call `get_design_context` for the exact node.
2. If the response is too large, call `get_metadata`, then request the relevant child nodes.
3. Call `get_screenshot` for the same node and variant.
4. Fetch `get_variable_defs`, Code Connect mappings, and asset exports as needed.

Do not begin implementation until both structure and a visual reference are available.

## `@gethopp/figma-mcp-bridge`

Recognize the bridge by tools such as:

- `list_files`, `get_document`, `get_selection`, `get_node`;
- `get_design_context`, `get_metadata`, `get_screenshot`, `save_screenshots`;
- `get_styles`, `get_variable_defs`;
- `get_motion_styles`, `get_node_motion`.

Verify the bridge as follows:

1. Call `list_files` and confirm that the target Figma file is connected.
2. If the list is empty, ask the user to open the target file in Figma and run the installed bridge plugin inside that file.
3. Fetch `get_metadata`, `get_selection`, or a specific `get_node` with the correct `fileKey`.
4. Fetch a screenshot of the same node.

The bridge runs as a stdio MCP server through this package:

```json
{
  "figma-bridge": {
    "command": "npx",
    "args": ["-y", "@gethopp/figma-mcp-bridge"]
  }
}
```

It also requires the Figma plugin from the project's latest release. Import its manifest through `Plugins > Development > Import plugin from manifest`, open the plugin in the target file, and keep it running while reading the design. Do not install software or modify the user's MCP configuration without permission.

Current source: <https://github.com/gethopp/figma-mcp-bridge>.

## OpenCode configuration

OpenCode reads MCP servers from `opencode.json` or `opencode.jsonc`. Choose one appropriate Figma provider to avoid inflating context with duplicate tool sets.

Official remote Figma MCP:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "figma": {
      "type": "remote",
      "url": "https://mcp.figma.com/mcp",
      "enabled": true
    }
  }
}
```

After adding it, run `opencode mcp auth figma` and complete the browser OAuth flow. Then verify the status with `opencode mcp list` and read the target Figma node.

Figma MCP Bridge:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "figma-bridge": {
      "type": "local",
      "command": ["npx", "-y", "@gethopp/figma-mcp-bridge"],
      "enabled": true
    }
  }
}
```

After starting OpenCode, check the server with `opencode mcp list`, open the bridge plugin in the target Figma file, and call `list_files`. Never store tokens directly in the repository; use OAuth or OpenCode environment variables.

## Connection failures

When verification fails, report:

1. which provider and tools were discovered;
2. which read-only call failed;
3. whether the cause is missing MCP configuration, authentication, file access, an exact node ID, a running bridge plugin, or connectivity;
4. the minimum action required from the user.

Repeat the verification call after the fix. Do not continue from a screenshot preview or memory when structured Figma data is unavailable.
