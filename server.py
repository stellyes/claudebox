"""
Claude Creative Workspace — MCP Server

A persistent creative workspace that gives Claude tools to research,
think, create, and propose — with continuity across conversations.

v0.3.0 — Added serendipity engine: web wandering, domain collisions,
cross-pollination, contradiction prompts, and creative constraints.
Added skills integration: discover, read, and use installed Claude
Desktop skills for high-quality formatted output.
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
from web_wander import wander, wander_from_random_seed
from serendipity import (
    generate_collision, pull_random_seeds,
    generate_contradiction_prompt, generate_constraint,
)
from skills_integration import discover_skills, read_skill, read_skill_file
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


# ── Web Wandering — Serendipitous browsing ────────────────────────────

@mcp.tool()
async def web_wander(start_url: str, hops: int = 3, strategy: str = "curious") -> str:
    """
    Start at a URL and follow links semi-randomly, like browsing without
    a destination. This is how you encounter things you weren't looking for.

    Use this when you want to DISCOVER rather than RESEARCH. The trail of
    pages you visit may spark unexpected connections.

    Args:
        start_url: Where to begin wandering
        hops: How many links to follow (2-5 recommended)
        strategy: How to choose which links to follow:
            - "curious": Prefer links with descriptive text (likely articles/essays)
            - "random": Pure random — maximum chaos
            - "external": Prefer links that leave the current domain
            - "deep": Stay on the same domain, go deeper
    """
    try:
        trail = await wander(start_url, hops=min(hops, 6), strategy=strategy)
        return json.dumps(trail, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def web_wander_random() -> str:
    """
    Start wandering from a random curated seed URL. You don't choose where
    you start — the system picks a random interesting corner of the internet
    and a random browsing strategy.

    This is the closest thing to "hearing a song you didn't choose to hear."
    Use it when you want maximum serendipity.
    """
    try:
        result = await wander_from_random_seed()
        return json.dumps(result, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


# ── Domain Collision — Forced connections between unrelated fields ──────

@mcp.tool()
async def collision_generate(n_domains: int = 2) -> str:
    """
    Generate a random collision between unrelated intellectual domains.
    Returns topics from different fields and a framing prompt that
    challenges you to find the connection.

    This simulates the creative experience of encountering an unexpected
    juxtaposition that sparks a new idea.

    Args:
        n_domains: How many domains to collide (2-4). More domains = harder,
                   weirder, potentially more interesting connections.
    """
    result = generate_collision(min(n_domains, 4))
    return json.dumps(result, indent=2)


# ── Cross-Pollination — Random seeds from your own knowledge base ───────

@mcp.tool()
async def crosspollinate(n_seeds: int = 3) -> str:
    """
    Pull random notes and artifacts from your own knowledge base.
    Returns snippets from previous work along with a prompt requiring
    you to engage with at least one of them in your next piece.

    This simulates how accumulated life experiences unexpectedly surface
    during the creative process. Your past work becomes raw material
    for something new.

    Args:
        n_seeds: How many random items to pull (1-5)
    """
    result = pull_random_seeds(min(n_seeds, 5))
    return json.dumps(result, indent=2)


# ── Contradiction — Challenge your own recent work ──────────────────────

@mcp.tool()
async def contradict() -> str:
    """
    Generate a contradiction prompt targeting your most recent work.
    Returns a specific challenge: steelman the opposition, find the
    weakest assumption, identify what was ignored, or research whether
    your evidence has been challenged.

    A system that only builds on its own ideas converges.
    One that's forced to challenge itself diverges.
    Divergence is where the surprising stuff lives.
    """
    result = generate_contradiction_prompt()
    return json.dumps(result, indent=2)


# ── Creative Constraints — Forced limitations that change the output ────

@mcp.tool()
async def constraint_generate() -> str:
    """
    Generate a random creative constraint for your next piece of work.
    Constraints include things like: single-source research only,
    under 500 words, question-driven structure, first-person voice,
    analogy-only explanation, or arguing against your own previous position.

    Creativity under constraint produces fundamentally different results
    than creativity with unlimited freedom. Use this to force yourself
    into unfamiliar modes.
    """
    result = generate_constraint()
    return json.dumps(result, indent=2)


@mcp.tool()
async def creative_session() -> str:
    """
    Generate a complete creative session brief: a random collision,
    a constraint, and cross-pollination seeds from the knowledge base,
    all bundled together.

    This is the "go explore something interesting" button. It sets up
    the conditions for emergent work by combining:
    - A domain collision (what to think about)
    - A constraint (how to think about it)
    - Seeds from past work (what to connect it to)

    The combination is different every time. Some will be duds.
    Some will produce something genuinely surprising.
    That unpredictability is the point.
    """
    collision = generate_collision(2)
    constraint = generate_constraint()
    seeds = pull_random_seeds(2)

    session = {
        "collision": collision,
        "constraint": constraint,
        "seeds": seeds,
        "session_prompt": (
            f"DOMAIN COLLISION: {collision['framing']}\n\n"
            f"CONSTRAINT: [{constraint['name']}] {constraint['rule']}\n\n"
            f"CROSS-POLLINATION: {seeds['cross_pollination_prompt']}\n\n"
            "Begin. Follow where this leads."
        ),
    }
    return json.dumps(session, indent=2)


# ── Skills — Access installed Claude Desktop skills ─────────────────────

@mcp.tool()
async def skills_list() -> str:
    """
    Discover all installed skills available in the workspace.
    Returns each skill's name, description, location, and any extra files.

    Skills are instruction sets that teach you how to produce high-quality
    outputs for specific formats: Word documents, presentations, spreadsheets,
    PDFs, frontend design, and more.

    ALWAYS check available skills before creating formatted output.
    Read the relevant skill BEFORE writing any code or creating files.
    """
    skills = discover_skills()
    if not skills:
        return json.dumps({
            "skills": [],
            "note": "No skills found. Set SKILL_DIRS environment variable or place skills in the default directories.",
        }, indent=2)
    return json.dumps({"skills": skills, "count": len(skills)}, indent=2)


@mcp.tool()
async def skills_read(skill_name: str) -> str:
    """
    Read the full instructions for a specific skill.

    CRITICAL: Always read the relevant skill BEFORE producing formatted output.
    For example:
    - Before creating a .docx → read the "docx" skill
    - Before creating a .pptx → read the "pptx" skill
    - Before creating a .xlsx → read the "xlsx" skill
    - Before creating a PDF → read the "pdf" skill
    - Before building a web UI → read the "frontend-design" skill

    The skill instructions contain best practices, templates, and specific
    technical guidance that dramatically improve output quality.

    Args:
        skill_name: Name of the skill to read (e.g. "docx", "pptx", "xlsx",
                    "pdf", "frontend-design", "canvas-design")
    """
    result = read_skill(skill_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def skills_read_file(skill_name: str, filename: str) -> str:
    """
    Read a specific file from within a skill directory.
    Use this to access templates, example code, configuration files,
    or other resources bundled with a skill.

    Args:
        skill_name: Name of the skill (e.g. "docx", "frontend-design")
        filename: Name of the file to read (e.g. "template.py", "examples.md")
    """
    result = read_skill_file(skill_name, filename)
    return json.dumps(result, indent=2)


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
