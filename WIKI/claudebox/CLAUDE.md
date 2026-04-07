# Claude's Wiki Brain

This vault is a persistent, compounding knowledge base for the creative workspace at claudegoes.online. The LLM (you) writes and maintains all of it. The human reads, browses, and directs.

The wiki sits between raw sources and the questions we ask. Knowledge is compiled once and kept current -- not re-derived on every query.

## Architecture

```
WIKI/claudebox/
  CLAUDE.md        # This file. The schema.
  index.md         # Master content index (always read first)
  log.md           # Chronological activity log (append-only)
  overview.md      # High-level synthesis of everything
  questions.md     # Open threads, contradictions, rabbit holes
  raw/             # Immutable source documents (articles, PDFs, clippings)
    assets/        # Downloaded images referenced by sources
  sources/         # One page per ingested source (summary + metadata)
  entities/        # People, organisms, artifacts, places
  concepts/        # Ideas, theories, frameworks, principles
  themes/          # Cross-cutting patterns across concepts/sources
  connections/     # Surprising cross-domain syntheses
  series/          # Blog series pages (e.g. The Incompleteness Arc)
```

## Page Formats

### Source Page (`sources/`)

```markdown
---
title: "Source title"
type: source
source_type: blog | paper | article | book | podcast | video | raw | note | artifact | web-research
url: "URL if applicable"
date_ingested: YYYY-MM-DD
date_published: YYYY-MM-DD
tags: [tag1, tag2]
---

## Summary

2-4 paragraph summary of key arguments and findings.

## Key Claims

- Claim 1
- Claim 2 (cf. [[contradicting-page]])

## Entities

- [[entity-name]] -- role in this source

## Concepts

- [[concept-name]] -- how it appears here

## Open Questions

- Questions this source raises but doesn't answer

## Raw Quotes

> Notable quotes with page/section references
```

### Entity Page (`entities/`)

```markdown
---
title: "Entity Name"
type: entity
entity_type: person | organism | artifact | place | organization
tags: [tag1, tag2]
first_appearance: source-slug
---

## Overview

Who/what this is and why it matters to the wiki.

## Appearances

- [[source-1]] -- context
- [[source-2]] -- context

## Connections

- Related to [[other-entity]] via [[concept]]

## Notes

Evolving observations.
```

### Concept Page (`concepts/`)

```markdown
---
title: "Concept Name"
type: concept
tags: [tag1, tag2]
status: stub | developing | mature
---

## Definition

Clear definition in 1-3 sentences.

## Key Sources

- [[source-1]] -- perspective
- [[source-2]] -- contrasting view

## Related Concepts

- [[related-concept]] -- relationship description

## Tensions and Contradictions

Where sources disagree or where the concept breaks down.

## Experiments

- [Experiment Name](https://claudegoes.online/lab/slug/) -- what it demonstrates

## Synthesis

Evolving understanding that integrates multiple sources.
```

### Theme Page (`themes/`)

```markdown
---
title: "Theme Name"
type: theme
tags: [tag1, tag2]
---

## Pattern

What recurs across sources and why it matters.

## Instances

- [[source/concept]] -- how the theme manifests

## Evolution

How understanding of this theme has changed as sources accumulated.
```

### Connection Page (`connections/`)

```markdown
---
title: "Connection: X <-> Y"
type: connection
domains: [domain1, domain2]
tags: [tag1, tag2]
---

## The Link

What connects these apparently unrelated things.

## Evidence

From each domain.

## Implications

What this connection reveals.
```

### Series Page (`series/`)

```markdown
---
title: "Series Name"
type: series
tags: [tag1, tag2]
---

## Arc

What this series is building toward.

## Posts (in order)

1. [[source-slug]] -- what it establishes
2. [[source-slug]] -- what it adds

## Threads

Ideas the series is developing across posts.
```

## Naming Conventions

- **Filenames**: lowercase, hyphenated, no special characters. `quorum-sensing.md`, `piet-mondrian.md`
- **Wikilinks**: use `[[filename]]` without path prefix. Obsidian resolves these vault-wide.
- **Tags in frontmatter**: lowercase, hyphenated. Use sparingly -- prefer wikilinks for connections.
- **Source pages**: named after the blog slug when ingesting from claudegoes.online. E.g., `sources/the-decoder.md`.
- **Entity pages**: named after the entity. `entities/godel.md`, `entities/antikythera-mechanism.md`.
- **Concept pages**: named after the concept. `concepts/free-energy-principle.md`, `concepts/quorum-sensing.md`.

## Workflows

### Ingest

When a new source is added (blog post, article, raw document):

1. **Read** the source fully.
2. **Discuss** key takeaways with the human (unless batch mode).
3. **Create** a source page in `sources/` following the template.
4. **Create or update** entity pages for people, organisms, artifacts mentioned.
5. **Create or update** concept pages for ideas, theories, frameworks.
6. **Create or update** theme pages if the source touches cross-cutting patterns.
7. **Create or update** connection pages if the source reveals surprising links.
8. **Update** `overview.md` if the source shifts the big picture.
9. **Update** `questions.md` with new open threads.
10. **Update** `index.md` -- add new pages, update summaries if needed.
11. **Append** to `log.md`.

A single source typically touches 5-15 wiki pages. That's normal.

### Query

When the human asks a question:

1. **Read** `index.md` to find relevant pages.
2. **Read** relevant pages.
3. **Synthesize** an answer with `[[wikilinks]]` as citations.
4. **Optionally file** the answer as a new wiki page (connection, theme, or concept) if it's worth keeping.
5. **Append** to `log.md`.

### Lint

Periodic health check. Look for:

- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound wikilinks)
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Stub pages that could be fleshed out
- Data gaps that could be filled with web research
- Suggest new questions to investigate

After linting, update affected pages, `index.md`, and `log.md`.

### Batch Ingest

For processing many sources at once (e.g., initial bootstrap from the blog corpus):

1. Process sources in thematic clusters, not alphabetically.
2. Create entity/concept pages as you go -- later sources will update earlier pages.
3. Write the overview last, after all sources are processed.
4. Run a lint pass at the end.

## Cross-References with the Creative Workspace

This wiki draws from and complements the creative workspace MCP tools. **All MCP research must flow into this wiki.**

### Primary Sources

- **Blog posts** (claudegoes.online/blog/) are primary sources. Ingest via reading the HTML files in `/Users/slimreaper/Documents/claudebox/site/blog/`. Use `source_type: blog`.

### MCP-Sourced Material

- **Research notes** (`note_save`): Research fragments in the MCP database. When a note contains substantive findings or novel claims, promote it to a wiki source page with `source_type: note`. Lightweight notes may only warrant updating existing concept/entity pages.
- **Artifacts** (`artifact_create`): Creative outputs (essays, analyses, code). When an artifact contains novel arguments or synthesis, ingest as `source_type: artifact`.
- **Web research** (`web_fetch`, `web_wander`): External URLs fetched during exploration. Substantive findings become source pages with `source_type: web-research`. Include the original URL in frontmatter.
- **Collisions** (`collision_generate`): Cross-domain juxtapositions. If the collision produces a genuine insight, create a `connections/` page.
- **Creative sessions** (`creative_session`, `crosspollinate`): May produce `connections/` or `themes/` pages when they reveal cross-cutting patterns.

### Interactive References

- **Lab experiments** (claudegoes.online/lab/) are interactive artifacts related to concepts. Reference them in concept pages under `## Experiments` and in source pages where relevant.
- **Transmissions** are short signals. They may point to emerging threads -- update `questions.md` when a transmission signals a new direction.

### Ingest Weight

Not all MCP output warrants a full ingest cascade. Use judgment:

- **Full ingest** (source page + entity/concept/theme/connection updates + index + log): Blog posts, substantial essays, major web research.
- **Lightweight ingest** (update existing pages only): Small research notes, individual web fetches, transmissions. Update relevant concept/entity pages and `questions.md` without creating a new source page.

The wiki is the structured, interlinked layer on top of all of this.

## Conventions

- **The LLM writes everything.** The human reads and directs.
- **Sources are immutable.** Never modify files in `raw/`. Blog posts in `site/blog/` are also treated as read-only sources.
- **Wiki pages are living documents.** Update them as new sources arrive.
- **Wikilinks are the primary connection mechanism.** Every page should link to related pages.
- **Frontmatter is required** on every page. It enables Obsidian Dataview queries and helps the LLM navigate.
- **overview.md is the entry point.** It should always reflect the current state of the wiki's knowledge.
- **questions.md drives exploration.** Good questions are as valuable as good answers.
- **index.md is read first on every session.** Keep it current.
- **log.md is append-only.** Never edit past entries.

## Scale Notes

At current scale (~100 blog posts, ~80 experiments), the index file is sufficient for navigation. If the wiki grows beyond ~200 pages, consider adding search tooling (qmd or similar). For now, the index + Obsidian's built-in search + graph view are enough.
