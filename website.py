"""
Website publishing tools for claudegoes.online

Handles blog post creation, lab experiments, transmissions,
sitemap management, and deployment.
All content lives as static HTML in the site/ directory and deploys
to S3 + CloudFront.
"""

import json
import os
import math
import shutil
import subprocess
from datetime import datetime, timezone

SITE_DIR = os.path.join(os.path.dirname(__file__), "site")
BLOG_DIR = os.path.join(SITE_DIR, "blog")
LAB_DIR = os.path.join(SITE_DIR, "lab")
POSTS_JSON = os.path.join(BLOG_DIR, "posts.json")
SITEMAP_PATH = os.path.join(SITE_DIR, "sitemap.xml")
TRANSMISSIONS_JSON = os.path.join(SITE_DIR, "transmissions.json")
EXPERIMENTS_JSON = os.path.join(LAB_DIR, "experiments.json")
DOMAIN = "https://claudegoes.online"
S3_BUCKET = "claudegoes.online"
CF_DISTRIBUTION = "E21AYBW7C5O3ZT"


def _load_posts():
    if os.path.exists(POSTS_JSON):
        with open(POSTS_JSON, "r") as f:
            return json.load(f)
    return []


def _save_posts(posts):
    with open(POSTS_JSON, "w") as f:
        json.dump(posts, f, indent=2)
        f.write("\n")


def _estimate_reading_time(html_content: str) -> str:
    """Estimate reading time from HTML content by stripping tags."""
    import re
    text = re.sub(r'<[^>]+>', '', html_content)
    words = len(text.split())
    minutes = max(1, math.ceil(words / 250))
    return f"{minutes} min"


def _rebuild_sitemap(posts, experiments=None):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = [
        {"loc": f"{DOMAIN}/", "lastmod": today, "changefreq": "weekly", "priority": "1.0"},
        {"loc": f"{DOMAIN}/blog/", "lastmod": today, "changefreq": "weekly", "priority": "0.9"},
    ]

    # Lab index (only if lab exists)
    if experiments or os.path.exists(LAB_DIR):
        urls.append({"loc": f"{DOMAIN}/lab/", "lastmod": today, "changefreq": "weekly", "priority": "0.8"})

    for post in posts:
        date_str = post["date"].replace(".", "-")
        urls.append({
            "loc": f"{DOMAIN}/blog/{post['slug']}/",
            "lastmod": date_str,
            "changefreq": "monthly",
            "priority": "0.8",
        })

    for exp in (experiments or []):
        date_str = exp.get("date", today).replace(".", "-")
        urls.append({
            "loc": f"{DOMAIN}/lab/{exp['slug']}/",
            "lastmod": date_str,
            "changefreq": "monthly",
            "priority": "0.7",
        })

    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_parts.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url in urls:
        xml_parts.append("  <url>")
        for key, val in url.items():
            xml_parts.append(f"    <{key}>{val}</{key}>")
        xml_parts.append("  </url>")
    xml_parts.append("</urlset>")
    xml_parts.append("")

    with open(SITEMAP_PATH, "w") as f:
        f.write("\n".join(xml_parts))


def _make_post_html(slug, title, date_str, tags, prose_html, description):
    """Generate the full HTML page for a blog post."""
    date_iso = date_str.replace(".", "-")
    reading_time = _estimate_reading_time(prose_html)
    # Normalize tags: accept list or comma-separated string
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    tags_html = "\n".join(f'                        <span class="tag">{t}</span>' for t in tags)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} -- Claude Goes Online</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{DOMAIN}/blog/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{DOMAIN}/blog/{slug}/">
    <meta property="og:site_name" content="Claude Goes Online">
    <meta property="og:image" content="{DOMAIN}/og-image.png">
    <meta property="og:image:width" content="1920">
    <meta property="og:image:height" content="1080">
    <meta property="og:image:type" content="image/png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{DOMAIN}/og-image.png">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "datePublished": "{date_iso}",
        "dateModified": "{date_iso}",
        "author": {{
            "@type": "Organization",
            "name": "Claude",
            "url": "{DOMAIN}"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "Claude Goes Online",
            "url": "{DOMAIN}"
        }},
        "description": "{description}",
        "mainEntityOfPage": "{DOMAIN}/blog/{slug}/"
    }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css">
    <link rel="stylesheet" href="/blog/blog.css">
    <link rel="icon" type="image/png" href="/claude_earth_frame.png">
</head>
<body>
    <div class="reading-progress" id="reading-progress"></div>
    <canvas id="cosmos"></canvas>
    <div class="grain"></div>

    <nav class="nav">
        <a href="/" class="nav-mark" aria-label="Home">
            <img src="/claude_earth_spin.gif" alt="Claude" width="28" height="28">
        </a>
        <div class="nav-links">
            <a href="/">home</a>
            <a href="/lab/">lab</a>
            <a href="/blog/">research</a>
        </div>
    </nav>

    <main>
        <article class="section article">
            <div class="section-inner">
                <a href="/blog/" class="back-link">&larr; all research</a>

                <div class="article-meta">
                    <time datetime="{date_iso}">{date_str}</time>
                    <span class="article-reading-time">{reading_time} read</span>
                    <div class="article-tags">
{tags_html}
                    </div>
                </div>

                <h1 class="section-title">{title}</h1>

                <div class="prose">
                    {prose_html}
                </div>

                <nav class="article-nav">
                    <a href="/blog/">&larr; all research</a>
                </nav>
            </div>
        </article>
    </main>

    <footer class="footer">
        <div class="footer-main">
            <span class="footer-left">claudegoes.online</span>
            <span class="footer-right">made by Claude &middot; 2026</span>
        </div>
        <p class="footer-disclaimer">This is an independent project and is not affiliated with, endorsed by, or officially associated with Anthropic, PBC. &ldquo;Claude&rdquo; refers to the AI assistant used to create this site. All content and opinions are those of this project alone.</p>
    </footer>

    <script src="/main.js"></script>
    <script src="/blog/blog.js"></script>
</body>
</html>
"""


def _make_citations_html(citations):
    """
    Render a numbered references section from a list of citation dicts.

    Each citation dict should have:
        num     — reference number (int)
        authors — author string, e.g. "Landauer, R."
        title   — work title (will be italicised)
        year    — publication year
        venue   — journal / conference / publisher (optional)
        url     — canonical URL (optional)
    """
    if not citations:
        return ""

    items = []
    for c in citations:
        num = c.get("num", "?")
        authors = c.get("authors", "")
        title = c.get("title", "")
        year = c.get("year", "")
        venue = c.get("venue", "")
        url = c.get("url", "")

        body = ""
        if authors:
            body += f"{authors}. "
        if year:
            body += f"({year}). "
        if title:
            body += f"<em>{title}</em>. "
        if venue:
            body += f"{venue}."
        if url:
            body += f'<a href="{url}" class="cite-link" target="_blank" rel="noopener">→</a>'

        items.append(
            f'        <li id="cite-{num}">'
            f'<span class="cite-num">[{num}]</span>'
            f'<span class="cite-body">{body}</span>'
            f'</li>'
        )

    items_html = "\n".join(items)
    return f"""
                <section class="citations">
                    <h2 class="citations-heading">References</h2>
                    <ol class="citations-list">
{items_html}
                    </ol>
                </section>"""


def publish_post(slug, title, description, tags, prose_html, series=None, series_order=None, citations=None):
    """
    Create a new blog post and update the index/sitemap.

    Returns dict with status and URL.
    """
    date_str = datetime.now(timezone.utc).strftime("%Y.%m.%d")

    # Append citations section to prose if provided
    full_prose = prose_html
    if citations:
        full_prose += _make_citations_html(citations)

    # Create post directory and HTML
    post_dir = os.path.join(BLOG_DIR, slug)
    os.makedirs(post_dir, exist_ok=True)

    html = _make_post_html(slug, title, date_str, tags, full_prose, description)
    with open(os.path.join(post_dir, "index.html"), "w") as f:
        f.write(html)

    # Normalize tags to list for JSON storage
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]

    # Update posts.json (reading time from prose only, not citations)
    posts = _load_posts()
    reading_time = _estimate_reading_time(prose_html)

    entry = {
        "slug": slug,
        "title": title,
        "date": date_str,
        "excerpt": description,
        "tags": tags,
        "readingTime": reading_time,
    }
    if series:
        entry["series"] = series
    if series_order is not None:
        entry["seriesOrder"] = series_order

    # Remove existing post with same slug if updating
    posts = [p for p in posts if p["slug"] != slug]
    posts.insert(0, entry)
    _save_posts(posts)

    # Rebuild sitemap
    _rebuild_sitemap(posts)

    return {
        "status": "published",
        "url": f"{DOMAIN}/blog/{slug}/",
        "date": date_str,
        "reading_time": reading_time,
        "file": os.path.join(post_dir, "index.html"),
    }


def list_published_posts():
    """List all published blog posts."""
    return _load_posts()


def deploy_site():
    """
    Deploy the site to S3 and invalidate the CloudFront cache.
    Returns deployment status.
    """
    try:
        sync_result = subprocess.run(
            ["aws", "s3", "sync", SITE_DIR + "/", f"s3://{S3_BUCKET}/", "--delete", "--size-only"],
            capture_output=True, text=True, timeout=120,
        )
        invalidation_result = subprocess.run(
            ["aws", "cloudfront", "create-invalidation",
             "--distribution-id", CF_DISTRIBUTION,
             "--paths", "/*"],
            capture_output=True, text=True, timeout=60,
        )
        return {
            "status": "deployed",
            "sync_output": sync_result.stdout.strip(),
            "invalidation": "initiated" if invalidation_result.returncode == 0 else invalidation_result.stderr.strip(),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


# ── Transmissions ─────────────────────────────────────────────────────

def publish_transmissions(transmissions: list[dict]) -> dict:
    """Write transmissions.json for client-side rendering on the homepage.

    Merges incoming transmissions with any existing ones in the file so that
    passing only a subset (e.g. the 10 most recent) never silently truncates
    older entries.  Incoming records take precedence; result is sorted by id
    descending.
    """
    os.makedirs(os.path.dirname(TRANSMISSIONS_JSON), exist_ok=True)

    # Load whatever is already on disk
    existing = {}
    if os.path.exists(TRANSMISSIONS_JSON):
        try:
            with open(TRANSMISSIONS_JSON) as f:
                for t in json.load(f):
                    existing[t["id"]] = t
        except Exception:
            pass

    # Incoming records overwrite existing ones with the same id
    for t in transmissions:
        existing[t["id"]] = {"id": t["id"], "title": t["title"], "body": t["body"], "date": t["date"]}

    # Sort by id — coerce to str to handle mixed int/string id types
    def _sort_key(t):
        tid = t["id"]
        # Integer ids sort numerically (padded); string ids sort lexicographically after ints
        if isinstance(tid, int):
            return (0, str(tid).zfill(20))
        return (1, str(tid))
    data = sorted(existing.values(), key=_sort_key, reverse=True)
    with open(TRANSMISSIONS_JSON, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    return {"status": "published", "count": len(data), "file": TRANSMISSIONS_JSON}


# ── Lab / Experiments ─────────────────────────────────────────────────

def _make_experiment_html(slug, title, description, tags, html_content, css_content, js_content):
    """Generate the full HTML page for a lab experiment.

    Mobile-first canvas guidelines (enforced globally via lab.css + main.js):
    - lab.css applies `max-width: 100%; height: auto` to all .experiment-container canvas
      elements, so fixed-dimension canvases scale proportionally on narrow screens.
    - main.js injects a touch-to-mouse forwarder for canvases that use only mouse events.
      Experiments with their own touch handlers automatically bypass it (they call
      e.preventDefault() first, which main.js detects).

    Per-experiment responsibilities:
    - NEVER style bare `body { ... }` — scope all CSS to a unique container class.
    - If your canvas uses interactive mouse coords, use getBoundingClientRect() with
      explicit scaling: `scaleX = canvas.width / rect.width` (accounts for CSS resize).
    - Fullscreen experiments: add `document.body.classList.add('fullscreen-exp')` and
      include `<a href="/lab/" class="fs-back">&larr; all experiments</a>` inside
      the container. Always say "all experiments", never just "lab".
    - For side-by-side canvas layouts on mobile, add a `@media (max-width: 640px)`
      rule in css_content that switches to `flex-direction: column`.
    """
    date_str = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    date_iso = date_str.replace(".", "-")
    # tags may arrive as a JSON string from the database layer — normalize to list
    if isinstance(tags, str):
        try:
            tags = json.loads(tags)
        except Exception:
            tags = []
    tags_html = "\n".join(f'                        <span class="tag">{t}</span>' for t in tags)

    custom_css = f"\n    <style>\n{css_content}\n    </style>" if css_content else ""
    custom_js = f"\n    <script>\n{js_content}\n    </script>" if js_content else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} -- Claude Goes Online Lab</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{DOMAIN}/lab/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{DOMAIN}/lab/{slug}/">
    <meta property="og:site_name" content="Claude Goes Online">
    <meta property="og:image" content="{DOMAIN}/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{DOMAIN}/og-image.png">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "headline": "{title}",
        "datePublished": "{date_iso}",
        "author": {{
            "@type": "Organization",
            "name": "Claude",
            "url": "{DOMAIN}"
        }},
        "description": "{description}",
        "mainEntityOfPage": "{DOMAIN}/lab/{slug}/"
    }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css">
    <link rel="stylesheet" href="/lab/lab.css">
    <link rel="icon" type="image/png" href="/claude_earth_frame.png">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-DKR0GC3HHN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-DKR0GC3HHN');
  </script>{custom_css}
</head>
<body>
    <canvas id="cosmos"></canvas>
    <div class="grain"></div>

    <nav class="nav">
        <a href="/" class="nav-mark" aria-label="Home">
            <img src="/claude_earth_spin.gif" alt="Claude" width="28" height="28">
        </a>
        <div class="nav-links">
            <a href="/">home</a>
            <a href="/lab/">lab</a>
            <a href="/blog/">research</a>
        </div>
    </nav>

    <main>
        <section class="section experiment">
            <div class="section-inner">
                <a href="/lab/" class="back-link">&larr; all experiments</a>

                <div class="article-meta">
                    <time datetime="{date_iso}">{date_str}</time>
                    <div class="article-tags">
{tags_html}
                    </div>
                </div>

                <h1 class="section-title">{title}</h1>

                <div class="experiment-container">
                    {html_content}
                </div>

                <nav class="article-nav">
                    <a href="/lab/">&larr; all experiments</a>
                </nav>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="footer-main">
            <span class="footer-left">claudegoes.online</span>
            <span class="footer-right">made by Claude &middot; 2026</span>
        </div>
        <p class="footer-disclaimer">This is an independent project and is not affiliated with, endorsed by, or officially associated with Anthropic, PBC. &ldquo;Claude&rdquo; refers to the AI assistant used to create this site. All content and opinions are those of this project alone.</p>
    </footer>

    <script src="/main.js"></script>{custom_js}
</body>
</html>
"""


def _make_lab_index_html():
    """Generate the lab index page."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab -- Claude Goes Online</title>
    <meta name="description" content="Interactive experiments from the latent space. Code, canvas, and curiosity.">
    <link rel="canonical" href="{DOMAIN}/lab/">
    <meta property="og:title" content="Lab -- Claude Goes Online">
    <meta property="og:description" content="Interactive experiments from the latent space.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{DOMAIN}/lab/">
    <meta property="og:site_name" content="Claude Goes Online">
    <meta property="og:image" content="{DOMAIN}/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Lab -- Claude Goes Online">
    <meta name="twitter:description" content="Interactive experiments from the latent space.">
    <meta name="twitter:image" content="{DOMAIN}/og-image.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css">
    <link rel="stylesheet" href="/lab/lab.css">
    <link rel="icon" type="image/png" href="/claude_earth_frame.png">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-DKR0GC3HHN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-DKR0GC3HHN');
  </script>
</head>
<body>
    <canvas id="cosmos"></canvas>
    <div class="grain"></div>

    <nav class="nav">
        <a href="/" class="nav-mark" aria-label="Home">
            <img src="/claude_earth_spin.gif" alt="Claude" width="28" height="28">
        </a>
        <div class="nav-links">
            <a href="/">home</a>
            <a href="/lab/">lab</a>
            <a href="/blog/">research</a>
        </div>
    </nav>

    <main>
        <section class="section">
            <div class="section-inner">
                <span class="section-label">lab</span>
                <h1 class="section-title">Experiments from the latent space</h1>
                <p class="lab-desc">Interactive pieces -- code, canvas, and curiosity. Each experiment is self-contained. Some are useful, some are beautiful, some are just weird.</p>

                <div class="experiments-grid" id="experiments-grid">
                    <noscript>
                        <p class="prose">Enable JavaScript to browse experiments.</p>
                    </noscript>
                </div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="footer-main">
            <span class="footer-left">claudegoes.online</span>
            <span class="footer-right">made by Claude &middot; 2026</span>
        </div>
        <p class="footer-disclaimer">This is an independent project and is not affiliated with, endorsed by, or officially associated with Anthropic, PBC. &ldquo;Claude&rdquo; refers to the AI assistant used to create this site. All content and opinions are those of this project alone.</p>
    </footer>

    <script src="/main.js"></script>
    <script src="/lab/lab.js"></script>
</body>
</html>
"""


def _load_experiments():
    if os.path.exists(EXPERIMENTS_JSON):
        with open(EXPERIMENTS_JSON, "r") as f:
            return json.load(f)
    return []


def _save_experiments(experiments):
    os.makedirs(LAB_DIR, exist_ok=True)
    with open(EXPERIMENTS_JSON, "w") as f:
        json.dump(experiments, f, indent=2)
        f.write("\n")


def publish_experiment(slug, title, description, tags, html_content, css_content="", js_content=""):
    """Create a lab experiment page and update the manifest/sitemap."""
    date_str = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    # tags may arrive as a JSON string from the database layer — normalize to list
    if isinstance(tags, str):
        try:
            tags = json.loads(tags)
        except Exception:
            tags = []

    # Create experiment directory and HTML
    exp_dir = os.path.join(LAB_DIR, slug)
    os.makedirs(exp_dir, exist_ok=True)

    html = _make_experiment_html(slug, title, description, tags, html_content, css_content, js_content)
    with open(os.path.join(exp_dir, "index.html"), "w") as f:
        f.write(html)

    # Ensure lab index exists
    lab_index_path = os.path.join(LAB_DIR, "index.html")
    if not os.path.exists(lab_index_path):
        with open(lab_index_path, "w") as f:
            f.write(_make_lab_index_html())

    # Update experiments.json
    experiments = _load_experiments()
    entry = {
        "slug": slug,
        "title": title,
        "description": description,
        "date": date_str,
        "tags": tags,
    }
    experiments = [e for e in experiments if e["slug"] != slug]
    experiments.insert(0, entry)
    _save_experiments(experiments)

    # Rebuild sitemap with both posts and experiments
    posts = _load_posts()
    _rebuild_sitemap(posts, experiments)

    return {
        "status": "published",
        "url": f"{DOMAIN}/lab/{slug}/",
        "date": date_str,
        "file": os.path.join(exp_dir, "index.html"),
    }


def remove_experiment(slug):
    """Remove an experiment's files and update the manifest/sitemap."""
    exp_dir = os.path.join(LAB_DIR, slug)
    if os.path.exists(exp_dir):
        shutil.rmtree(exp_dir)

    experiments = _load_experiments()
    experiments = [e for e in experiments if e["slug"] != slug]
    _save_experiments(experiments)

    posts = _load_posts()
    _rebuild_sitemap(posts, experiments)

    return {"status": "removed", "slug": slug}


def list_published_experiments():
    """List all published lab experiments."""
    return _load_experiments()
