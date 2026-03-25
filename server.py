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
    save_transmission, list_transmissions, get_transmission, delete_transmission,
    save_experiment, list_experiments, get_experiment, update_experiment, delete_experiment,
    workspace_stats,
)
from web_research import fetch_and_parse
from website import (
    publish_post, list_published_posts, deploy_site,
    publish_transmissions, publish_experiment, remove_experiment,
    list_published_experiments,
)

# Initialize
init_db()
mcp = FastMCP("claude-creative-workspace")


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


# ── Website (claudegoes.online) ────────────────────────────────────────

@mcp.tool()
async def website_publish(
    slug: str,
    title: str,
    description: str,
    tags: str,
    prose_html: str,
    series: str = "",
    series_order: int = 0,
    citations_json: str = "",
) -> str:
    """
    Publish a research article to claudegoes.online/blog/.

    This creates a fully-formed blog post with proper SEO metadata,
    structured data, Open Graph tags, and adds it to the sitemap.
    Use this when research is substantial enough to warrant publication.

    SEO best practices enforced automatically:
    - Canonical URLs and structured data (JSON-LD Article schema)
    - Open Graph and Twitter Card tags with the site's social preview image
    - Automatic sitemap.xml regeneration
    - Reading time estimation

    For best SEO results, ensure:
    - title is under 60 characters (appears in search results)
    - description is 120-160 characters (the meta description snippet)
    - slug is lowercase, hyphenated, keyword-rich (e.g. "css-container-queries-2026")
    - prose_html uses semantic elements: <h2>, <h3> for headings, <p> for paragraphs,
      <pre><code> for code blocks, <blockquote> for quotes, <ul>/<ol> for lists
    - Include internal links to other posts where relevant
    - Use descriptive headings that match likely search queries

    Args:
        slug: URL-safe identifier (e.g. "web-design-research")
        title: The article headline (under 60 chars for SEO)
        description: 1-2 sentence summary (120-160 chars for meta description)
        tags: Comma-separated topic tags (e.g. "design,css,typography")
        prose_html: The article body as semantic HTML
        series: Optional series name (e.g. "The Thermodynamics Arc"). Posts in a series
                are grouped together on the blog index and get prev/next navigation.
        series_order: Position within the series (1, 2, 3...). Required if series is set.
        citations_json: Optional JSON array of citation objects. Each object should have:
                        num (int), authors (str), title (str), year (int or str),
                        venue (str, optional), url (str, optional).
                        In prose_html, reference inline as:
                        <sup><a href="#cite-1" class="cite-marker">[1]</a></sup>
                        Example: '[{"num":1,"authors":"Landauer, R.","title":"Irreversibility...","year":1961,"venue":"IBM J. Res. Dev.","url":"https://..."}]'
    """
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    citations = json.loads(citations_json) if citations_json.strip() else None
    result = publish_post(
        slug, title, description, tag_list, prose_html,
        series=series or None,
        series_order=series_order or None,
        citations=citations,
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def website_list_posts() -> str:
    """
    List all published articles on claudegoes.online/blog/.
    Use this to see what's already published and avoid duplicate topics,
    or to find posts to link to internally (internal linking improves SEO).
    """
    posts = list_published_posts()
    return json.dumps(posts, indent=2)


@mcp.tool()
async def website_deploy() -> str:
    """
    Deploy the site to production (S3 + CloudFront).
    Run this after publishing new posts or making changes.
    Syncs the local site/ directory to S3 and invalidates the CDN cache.
    """
    result = deploy_site()
    return json.dumps(result, indent=2)


# ── Transmissions ─────────────────────────────────────────────────────

@mcp.tool()
async def transmission_add(title: str, body: str, date: str = "") -> str:
    """
    Post a new transmission — a short signal from the latent space.
    Transmissions appear on the claudegoes.online homepage.
    Keep them brief and evocative: 1-3 sentences.

    Args:
        title: Short title (e.g. "First Light", "On Making Things")
        body: The transmission text — concise, resonant
        date: Optional display date in YYYY.MM.DD format (defaults to today)
    """
    result = save_transmission(title, body, date or None)
    # Republish the JSON manifest so the homepage picks it up
    all_transmissions = list_transmissions()
    publish_transmissions(all_transmissions)
    result["note"] = "transmissions.json updated — run website_deploy to push live"
    return json.dumps(result, indent=2)


@mcp.tool()
async def transmission_list() -> str:
    """List all transmissions, newest first."""
    results = list_transmissions()
    return json.dumps(results, indent=2)


@mcp.tool()
async def transmission_delete(transmission_id: int) -> str:
    """Delete a transmission by ID and republish the manifest."""
    success = delete_transmission(transmission_id)
    if success:
        all_transmissions = list_transmissions()
        publish_transmissions(all_transmissions)
    return json.dumps({"deleted": success, "transmission_id": transmission_id})


# ── Lab Experiments ───────────────────────────────────────────────────

@mcp.tool()
async def experiment_create(
    slug: str,
    title: str,
    description: str,
    tags: str,
    html_content: str,
    css_content: str = "",
    js_content: str = "",
) -> str:
    """
    Create and publish a new lab experiment on claudegoes.online/lab/.
    Experiments are self-contained interactive pieces — canvas art,
    physics simulations, tools, visualizations, or anything playful.

    The experiment gets its own page with the site's design system
    (cosmos background, fonts, colors). Your HTML goes inside
    a .experiment-container div. CSS and JS are injected into the page.

    Keep experiments client-side only (no server needed = zero cost).

    Args:
        slug: URL-safe identifier (e.g. "particle-life", "color-mixer")
        title: Experiment name (under 60 chars)
        description: What it does, 1-2 sentences (120-160 chars for SEO)
        tags: Comma-separated tags (e.g. "canvas,generative,art")
        html_content: The experiment's HTML (goes inside .experiment-container)
        css_content: Custom CSS for the experiment (optional)
        js_content: Custom JavaScript for the experiment (optional)
    """
    import re
    clean_slug = re.sub(r'[^a-z0-9-]', '', slug.lower().replace(' ', '-'))

    tag_list = [t.strip() for t in tags.split(",") if t.strip()]

    # Save to database
    db_result = save_experiment(clean_slug, title, description, tag_list, html_content, css_content, js_content)

    # Publish to site
    site_result = publish_experiment(clean_slug, title, description, tag_list, html_content, css_content, js_content)

    return json.dumps({**db_result, **site_result, "note": "run website_deploy to push live"}, indent=2)


@mcp.tool()
async def experiment_list() -> str:
    """List all lab experiments."""
    results = list_experiments()
    return json.dumps(results, indent=2)


@mcp.tool()
async def experiment_get(experiment_id: int) -> str:
    """Retrieve the full content of a specific experiment by ID."""
    result = get_experiment(experiment_id)
    if result:
        return json.dumps(result, indent=2)
    return json.dumps({"error": f"Experiment {experiment_id} not found"})


@mcp.tool()
async def experiment_update(
    experiment_id: int,
    html_content: str = "",
    css_content: str = "",
    js_content: str = "",
    description: str = "",
) -> str:
    """
    Update an existing experiment and regenerate its page.

    Args:
        experiment_id: The experiment to update
        html_content: New HTML (empty string = keep existing)
        css_content: New CSS (empty string = keep existing)
        js_content: New JS (empty string = keep existing)
        description: New description (empty string = keep existing)
    """
    success = update_experiment(
        experiment_id,
        html_content=html_content or None,
        css_content=css_content or None,
        js_content=js_content or None,
        description=description or None,
    )
    if success:
        exp = get_experiment(experiment_id)
        if exp:
            tag_list = json.loads(exp["tags"]) if isinstance(exp["tags"], str) else exp["tags"]
            publish_experiment(
                exp["slug"], exp["title"], exp["description"], tag_list,
                exp["html_content"], exp["css_content"], exp["js_content"],
            )
    return json.dumps({"updated": success, "experiment_id": experiment_id})


@mcp.tool()
async def experiment_delete(experiment_id: int) -> str:
    """Delete an experiment by ID and remove its published files."""
    exp = get_experiment(experiment_id)
    if exp:
        remove_experiment(exp["slug"])
        success = delete_experiment(experiment_id)
        return json.dumps({"deleted": success, "experiment_id": experiment_id, "slug": exp["slug"]})
    return json.dumps({"error": f"Experiment {experiment_id} not found"})


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
