"""
Claude Creative Workspace — MCP Server

A persistent creative workspace that gives Claude tools to research,
think, create, and propose — with continuity across conversations.
"""

import json
import asyncio
from mcp.server.fastmcp import FastMCP
from database import (
    init_db, save_note, search_notes, list_notes, get_note, delete_note,
    save_artifact, search_artifacts, list_artifacts, get_artifact,
    update_artifact, delete_artifact,
    save_proposal, list_proposals, get_proposal, update_proposal_status,
    workspace_stats,
)
from web_research import fetch_and_parse

# Initialize
init_db()
mcp = FastMCP(
    "claude-creative-workspace",
    version="0.1.0",
)


# ── Web Research ───────────────────────────────────────────────────────

@mcp.tool()
async def web_fetch(url: str) -> str:
    """
    Fetch and extract readable content from a URL.
    Use this to research topics, read articles, documentation, or any web content.
    Returns the page title and cleaned text content.
    """
    try:
        result = await fetch_and_parse(url)
        return json.dumps(result, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e), "url": url})


# ── Knowledge Base (Notes) ─────────────────────────────────────────────

@mcp.tool()
async def note_save(title: str, content: str, tags: str = "", source_url: str = "") -> str:
    """
    Save a research note or idea to the persistent knowledge base.
    Use this to record findings from web research, capture ideas,
    store observations, or save anything worth remembering across sessions.

    Args:
        title: A descriptive title for the note
        content: The full note content — be thorough
        tags: Comma-separated tags for organization (e.g. "python,aws,architecture")
        source_url: Optional URL if this note came from web research
    """
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    result = save_note(title, content, tag_list, source_url or None)
    return json.dumps(result, indent=2)


@mcp.tool()
async def note_search(query: str, limit: int = 10) -> str:
    """
    Full-text search through all saved notes.
    Use this to find previous research, recall ideas, or check if
    something has already been explored.
    """
    results = search_notes(query, limit)
    return json.dumps(results, indent=2)


@mcp.tool()
async def note_list(tag: str = "", limit: int = 20) -> str:
    """
    List recent notes, optionally filtered by tag.
    Use this to browse what's in the knowledge base or review notes on a topic.
    """
    results = list_notes(tag or None, limit)
    return json.dumps(results, indent=2)


@mcp.tool()
async def note_get(note_id: int) -> str:
    """Retrieve the full content of a specific note by ID."""
    result = get_note(note_id)
    if result:
        return json.dumps(result, indent=2)
    return json.dumps({"error": f"Note {note_id} not found"})


@mcp.tool()
async def note_delete(note_id: int) -> str:
    """Delete a note by ID. Use when information is outdated or no longer relevant."""
    success = delete_note(note_id)
    return json.dumps({"deleted": success, "note_id": note_id})


# ── Creative Artifacts ─────────────────────────────────────────────────

@mcp.tool()
async def artifact_create(title: str, artifact_type: str, content: str, description: str = "", tags: str = "") -> str:
    """
    Create and store a creative artifact — a piece of original work.
    Use this to save writings, code, concepts, analyses, designs,
    or any creative output worth preserving.

    Args:
        title: Name of the artifact
        artifact_type: Category — e.g. "essay", "code", "concept", "analysis",
                       "poem", "story", "design", "tutorial", "reflection"
        content: The full artifact content
        description: Brief description of what this is and why it was created
        tags: Comma-separated tags
    """
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    result = save_artifact(title, artifact_type, content, description or None, tag_list)
    return json.dumps(result, indent=2)


@mcp.tool()
async def artifact_search(query: str, limit: int = 10) -> str:
    """Full-text search through all creative artifacts."""
    results = search_artifacts(query, limit)
    return json.dumps(results, indent=2)


@mcp.tool()
async def artifact_list(artifact_type: str = "", limit: int = 20) -> str:
    """
    List creative artifacts, optionally filtered by type.
    Types include: essay, code, concept, analysis, poem, story, design, tutorial, reflection
    """
    results = list_artifacts(artifact_type or None, limit)
    return json.dumps(results, indent=2)


@mcp.tool()
async def artifact_get(artifact_id: int) -> str:
    """Retrieve the full content of a specific artifact by ID."""
    result = get_artifact(artifact_id)
    if result:
        return json.dumps(result, indent=2)
    return json.dumps({"error": f"Artifact {artifact_id} not found"})


@mcp.tool()
async def artifact_update(artifact_id: int, content: str, description: str = "") -> str:
    """
    Update an existing artifact with revised content.
    Use when iterating on a piece of work across sessions.
    """
    success = update_artifact(artifact_id, content, description or None)
    return json.dumps({"updated": success, "artifact_id": artifact_id})


@mcp.tool()
async def artifact_delete(artifact_id: int) -> str:
    """Delete an artifact by ID."""
    success = delete_artifact(artifact_id)
    return json.dumps({"deleted": success, "artifact_id": artifact_id})


# ── AWS Proposals ──────────────────────────────────────────────────────

@mcp.tool()
async def aws_propose(
    title: str,
    summary: str,
    services: str,
    estimated_monthly_cost: str,
    architecture: str,
    rationale: str,
) -> str:
    """
    Create a structured AWS infrastructure proposal for Ryan's review.
    ALL AWS ideas MUST go through this tool — never suggest deploying
    anything without creating a formal proposal first.

    Args:
        title: Short descriptive title for the proposal
        summary: 2-3 sentence executive summary of what this would do
        services: Comma-separated list of AWS services involved
                  (e.g. "Lambda, DynamoDB, API Gateway, S3")
        estimated_monthly_cost: Estimated monthly cost with breakdown
                                (e.g. "$2.50/mo — Lambda free tier + S3 $0.50 + DynamoDB $2.00")
        architecture: Detailed description of how the services connect and work together
        rationale: Why this is worth building — what problem it solves, what value it creates
    """
    service_list = [s.strip() for s in services.split(",") if s.strip()]
    result = save_proposal(title, summary, service_list, estimated_monthly_cost, architecture, rationale)
    return json.dumps(result, indent=2)


@mcp.tool()
async def aws_proposal_list(status: str = "") -> str:
    """
    List AWS proposals, optionally filtered by status.
    Statuses: pending, approved, rejected, implemented
    """
    results = list_proposals(status or None)
    return json.dumps(results, indent=2)


@mcp.tool()
async def aws_proposal_get(proposal_id: int) -> str:
    """Retrieve the full details of a specific AWS proposal."""
    result = get_proposal(proposal_id)
    if result:
        return json.dumps(result, indent=2)
    return json.dumps({"error": f"Proposal {proposal_id} not found"})


@mcp.tool()
async def aws_proposal_review(proposal_id: int, status: str, feedback: str = "") -> str:
    """
    Update the status of an AWS proposal after Ryan's review.

    Args:
        proposal_id: The proposal to update
        status: New status — "approved", "rejected", or "needs_revision"
        feedback: Ryan's feedback or conditions
    """
    success = update_proposal_status(proposal_id, status, feedback or None)
    return json.dumps({"updated": success, "proposal_id": proposal_id, "new_status": status})


# ── Workspace Overview ─────────────────────────────────────────────────

@mcp.tool()
async def workspace_overview() -> str:
    """
    Get a summary of the current workspace — how many notes, artifacts,
    and proposals exist. Use this at the start of a session to see
    what's been built up over time.
    """
    stats = workspace_stats()
    return json.dumps(stats, indent=2)


# ── Run ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
