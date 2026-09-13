# Figma MCP setup

Read only when configuring or repairing a connection. Use the section for the user's client and chosen provider; verify current provider instructions before changing configuration. These examples are starting points, not a reason to replace a working connection or configure a second provider.

## Bridge prerequisites

The bridge runs as a stdio MCP server through this package:

```json
{
  "figma-bridge": {
    "command": "npx",
    "args": ["-y", "@gethopp/figma-mcp-bridge"]
  }
}
```

It also requires the Figma plugin from the project's latest release. Import its manifest through `Plugins > Development > Import plugin from manifest`, open the plugin in the target file, and keep it running while reading the design. Apply installation or configuration changes only within the user's authorized setup request; existing authorization does not need to be requested again.

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

## Claude Code configuration

Claude Code supports user-scoped MCP servers for all projects and project-scoped servers shared through the repository. Choose one Figma provider and one scope.

Add the official remote Figma MCP for the current user:

```sh
claude mcp add --transport http --scope user figma https://mcp.figma.com/mcp
```

For project scope, replace `--scope user` with `--scope project`. Open Claude Code, run `/mcp`, and complete the browser OAuth flow. Verify the result with `claude mcp list` and a read-only call for the target node.

Add Figma MCP Bridge for the current user:

```sh
claude mcp add --transport stdio --scope user figma-bridge -- npx -y @gethopp/figma-mcp-bridge
```

For project scope, replace `--scope user` with `--scope project`. Then run `claude mcp list`, open the bridge plugin in the target Figma file, and call `list_files`. Do not configure both providers unless the user needs both intentionally.

