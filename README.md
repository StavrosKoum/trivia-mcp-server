# Trivia MCP Server

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server, written in Python, that lets Claude host a trivia game.

> 🚧 Work in progress

## Planned features

- Get a random trivia question
- Check answers
- Track and show your score
- Choose a category

## Tech stack

- Python 3.12
- [`mcp`](https://pypi.org/project/mcp/) Python SDK (v2, `MCPServer`)

## Setup

```powershell
git clone https://github.com/StavrosKoum/trivia-mcp-server.git
cd trivia-mcp-server
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## License

MIT
