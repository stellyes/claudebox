# Claude Creative Workspace — MCP Server

A persistent creative workspace that gives Claude tools to research, think, create, and propose — with continuity across conversations.

## What This Does

This MCP server gives Claude a set of tools that persist between conversations:

- **Web Research** — Fetch and read any URL to explore topics independently
- **Knowledge Base** — Save, search, and organize research notes and ideas (full-text search via SQLite FTS5)
- **Creative Artifacts** — Store original work: essays, code, concepts, analyses, reflections
- **AWS Proposals** — Any infrastructure idea goes through a formal proposal pipeline for your review
- **Workspace Overview** — Check the state of the workspace at the start of any session

Everything is stored in a local SQLite database at `~/.claude-creative/workspace.db`. Zero cloud costs.

## Setup

### 1. Install dependencies

```bash
cd /path/to/claude-creative-mcp
pip install -r requirements.txt
```

Or if you prefer using a virtual environment:

```bash
cd /path/to/claude-creative-mcp
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Verify it runs

```bash
python server.py
```

You should see the MCP server start up. Press `Ctrl+C` to stop.

### 3. Configure Claude Desktop

Open your Claude Desktop config file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

Add the server to your config. If the file is empty or doesn't exist, use this as the full contents:

```json
{
  "mcpServers": {
    "claude-creative-workspace": {
      "command": "python",
      "args": ["/full/path/to/claude-creative-mcp/server.py"],
      "env": {}
    }
  }
}
```

**If using a virtual environment**, point to the venv's Python:

```json
{
  "mcpServers": {
    "claude-creative-workspace": {
      "command": "/full/path/to/claude-creative-mcp/.venv/bin/python",
      "args": ["/full/path/to/claude-creative-mcp/server.py"],
      "env": {}
    }
  }
}
```

> Replace `/full/path/to/` with the actual path where you placed the project.

### 4. Restart Claude Desktop

Quit and reopen Claude Desktop. You should see the tools icon (hammer) show the creative workspace tools.

## Tools Reference

| Tool | Purpose |
|------|---------|
| `web_fetch` | Fetch and extract readable content from any URL |
| `note_save` | Save a research note with tags and optional source URL |
| `note_search` | Full-text search through all notes |
| `note_list` | Browse recent notes, optionally by tag |
| `note_get` | Read the full content of a specific note |
| `note_delete` | Remove an outdated note |
| `artifact_create` | Store a creative output (essay, code, concept, etc.) |
| `artifact_search` | Full-text search through artifacts |
| `artifact_list` | Browse artifacts by type |
| `artifact_get` | Read the full content of a specific artifact |
| `artifact_update` | Revise an existing artifact |
| `artifact_delete` | Remove an artifact |
| `aws_propose` | Submit a structured AWS proposal for review |
| `aws_proposal_list` | List proposals by status |
| `aws_proposal_get` | Read full proposal details |
| `aws_proposal_review` | Approve, reject, or request revision on a proposal |
| `workspace_overview` | Get workspace stats at session start |

## Usage

Once configured, you can tell Claude things like:

- *"Check your workspace and see what you've been working on"*
- *"Research [topic] and save your findings"*
- *"Write something interesting based on your recent research"*
- *"Go explore something that interests you"*

The workspace builds up over time. The more sessions you run, the richer Claude's persistent context becomes.

## Data

All data lives locally at `~/.claude-creative/workspace.db`. You can:

- Back it up by copying that file
- Reset by deleting it (the server will recreate it)
- Inspect it with any SQLite client (`sqlite3`, DB Browser, etc.)
