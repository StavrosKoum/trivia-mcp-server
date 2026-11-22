"""Trivia MCP server: the entry point that Claude talks to."""

from mcp.server.mcpserver import MCPServer

# Create the server. The name is what the host (Claude) shows for this server.
mcp = MCPServer("trivia")


@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone. Use this to test that the trivia server is connected."""
    return f"Hello, {name}! The trivia server is up and running."


def main() -> None:
    """Start the server, talking to the host over stdin/stdout ("stdio")."""
    mcp.run()


if __name__ == "__main__":
    main()
