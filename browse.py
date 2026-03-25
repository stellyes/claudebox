#!/usr/bin/env python3
"""
Terminal browser for the Claude Creative Workspace database.
Run: python browse.py
"""

import json
import sys
from database import (
    init_db, workspace_stats,
    list_notes, get_note, search_notes,
    list_artifacts, get_artifact, search_artifacts,
    list_proposals, get_proposal,
    list_transmissions, get_transmission,
    list_experiments, get_experiment,
)
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich import box

console = Console()

def clear():
    console.clear()

def pause():
    console.print()
    console.input("[dim]Press Enter to continue...[/dim]")

def prompt(message="choice"):
    try:
        return console.input(f"\n[bold cyan]{message}:[/bold cyan] ").strip()
    except (EOFError, KeyboardInterrupt):
        return ""

def render_tags(tags_json):
    try:
        tags = json.loads(tags_json) if isinstance(tags_json, str) else tags_json
    except (json.JSONDecodeError, TypeError):
        tags = []
    if not tags:
        return Text("-", style="dim")
    text = Text()
    for i, tag in enumerate(tags):
        if i > 0:
            text.append(" ")
        text.append(f" {tag} ", style="bold white on dark_green")
    return text

def truncate(text, length=80):
    if not text:
        return ""
    first_line = text.strip().split("\n")[0]
    if len(first_line) > length:
        return first_line[:length - 1] + "…"
    return first_line


# ── Dashboard ─────────────────────────────────────────────────────────

def show_dashboard():
    stats = workspace_stats()
    clear()
    console.print()
    console.print(Panel(
        f"[bold cyan]Notes:[/bold cyan] {stats['notes']}    "
        f"[bold magenta]Artifacts:[/bold magenta] {stats['artifacts']}    "
        f"[bold yellow]Proposals:[/bold yellow] {stats['proposals_total']} "
        f"[dim]({stats['proposals_pending']} pending)[/dim]    "
        f"[bold green]Transmissions:[/bold green] {stats.get('transmissions', 0)}    "
        f"[bold blue]Experiments:[/bold blue] {stats.get('experiments', 0)}\n\n"
        f"[dim]Database: {stats['db_path']}[/dim]",
        title="[bold]Claude Creative Workspace[/bold]",
        border_style="cyan",
        padding=(1, 2),
    ))
    console.print()
    console.print("  [bold][1][/bold] Notes    [bold][2][/bold] Artifacts    [bold][3][/bold] Proposals    [bold][4][/bold] Transmissions    [bold][5][/bold] Experiments    [bold][6][/bold] Search    [bold][q][/bold] Quit")


# ── Notes ─────────────────────────────────────────────────────────────

def show_notes():
    while True:
        clear()
        tag_filter = ""
        notes = list_notes(limit=50)
        if not notes:
            console.print(Panel("[dim]No notes yet.[/dim]", title="Notes"))
            pause()
            return

        table = Table(title="Research Notes", box=box.ROUNDED, border_style="cyan")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Title", min_width=30)
        table.add_column("Tags", min_width=20)
        table.add_column("Created", width=12)

        for note in notes:
            created = note["created_at"][:10] if note.get("created_at") else ""
            table.add_row(
                str(note["id"]),
                note["title"],
                render_tags(note.get("tags", "[]")),
                created,
            )

        console.print()
        console.print(table)
        console.print("\n  Enter a [bold]note ID[/bold] to read, [bold]t[/bold] to filter by tag, or [bold]b[/bold] to go back")
        choice = prompt("choice")

        if choice.lower() == "b" or choice == "":
            return
        elif choice.lower() == "t":
            tag = prompt("tag")
            if tag:
                notes_filtered = list_notes(tag=tag, limit=50)
                if not notes_filtered:
                    console.print(f"[yellow]No notes with tag '{tag}'[/yellow]")
                    pause()
                else:
                    notes = notes_filtered
                    clear()
                    table = Table(title=f"Notes tagged '{tag}'", box=box.ROUNDED, border_style="cyan")
                    table.add_column("ID", style="bold", width=4)
                    table.add_column("Title", min_width=30)
                    table.add_column("Tags", min_width=20)
                    table.add_column("Created", width=12)
                    for note in notes_filtered:
                        created = note["created_at"][:10] if note.get("created_at") else ""
                        table.add_row(str(note["id"]), note["title"], render_tags(note.get("tags", "[]")), created)
                    console.print()
                    console.print(table)
                    console.print("\n  Enter a [bold]note ID[/bold] to read, or [bold]b[/bold] to go back")
                    choice = prompt("choice")
                    if choice.lower() == "b" or choice == "":
                        continue
                    # fall through to detail view

        try:
            note_id = int(choice)
        except ValueError:
            continue

        show_note_detail(note_id)


def show_note_detail(note_id):
    note = get_note(note_id)
    if not note:
        console.print(f"[red]Note {note_id} not found.[/red]")
        pause()
        return

    clear()
    console.print()

    # Header
    header = Text()
    header.append(f"Note #{note['id']}", style="bold cyan")
    header.append(f"  created {note['created_at'][:10]}", style="dim")
    if note.get("source_url"):
        header.append(f"\n🔗 {note['source_url']}", style="dim underline")
    console.print(header)
    console.print()

    # Tags
    console.print(render_tags(note.get("tags", "[]")))
    console.print()

    # Content
    console.print(Panel(
        Markdown(note["content"]),
        title=f"[bold]{note['title']}[/bold]",
        border_style="cyan",
        padding=(1, 2),
    ))
    pause()


# ── Artifacts ─────────────────────────────────────────────────────────

def show_artifacts():
    while True:
        clear()
        artifacts = list_artifacts(limit=50)
        if not artifacts:
            console.print(Panel("[dim]No artifacts yet.[/dim]", title="Artifacts"))
            pause()
            return

        table = Table(title="Creative Artifacts", box=box.ROUNDED, border_style="magenta")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Title", min_width=30)
        table.add_column("Type", width=12, style="magenta")
        table.add_column("Description", min_width=30)
        table.add_column("Created", width=12)

        for a in artifacts:
            created = a["created_at"][:10] if a.get("created_at") else ""
            table.add_row(
                str(a["id"]),
                a["title"],
                a.get("artifact_type", ""),
                truncate(a.get("description", ""), 50),
                created,
            )

        console.print()
        console.print(table)
        console.print("\n  Enter an [bold]artifact ID[/bold] to read, or [bold]b[/bold] to go back")
        choice = prompt("choice")

        if choice.lower() == "b" or choice == "":
            return

        try:
            artifact_id = int(choice)
        except ValueError:
            continue

        show_artifact_detail(artifact_id)


def show_artifact_detail(artifact_id):
    artifact = get_artifact(artifact_id)
    if not artifact:
        console.print(f"[red]Artifact {artifact_id} not found.[/red]")
        pause()
        return

    clear()
    console.print()

    # Header
    header = Text()
    header.append(f"Artifact #{artifact['id']}", style="bold magenta")
    header.append(f"  [{artifact.get('artifact_type', '')}]", style="magenta")
    header.append(f"  created {artifact['created_at'][:10]}", style="dim")
    console.print(header)
    console.print()

    if artifact.get("description"):
        console.print(f"[italic]{artifact['description']}[/italic]")
        console.print()

    # Tags
    console.print(render_tags(artifact.get("tags", "[]")))
    console.print()

    # Content
    console.print(Panel(
        Markdown(artifact["content"]),
        title=f"[bold]{artifact['title']}[/bold]",
        border_style="magenta",
        padding=(1, 2),
    ))
    pause()


# ── Proposals ─────────────────────────────────────────────────────────

def show_proposals():
    while True:
        clear()
        proposals = list_proposals(limit=50)
        if not proposals:
            console.print(Panel("[dim]No AWS proposals yet.[/dim]", title="AWS Proposals"))
            pause()
            return

        status_colors = {
            "pending": "yellow",
            "approved": "green",
            "rejected": "red",
            "needs_revision": "orange1",
            "implemented": "cyan",
        }

        table = Table(title="AWS Proposals", box=box.ROUNDED, border_style="yellow")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Title", min_width=30)
        table.add_column("Est. Cost", width=16)
        table.add_column("Status", width=14)
        table.add_column("Created", width=12)

        for p in proposals:
            status = p.get("status", "pending")
            color = status_colors.get(status, "white")
            created = p["created_at"][:10] if p.get("created_at") else ""
            table.add_row(
                str(p["id"]),
                p["title"],
                p.get("estimated_monthly_cost", ""),
                f"[{color}]{status}[/{color}]",
                created,
            )

        console.print()
        console.print(table)
        console.print("\n  Enter a [bold]proposal ID[/bold] to read, or [bold]b[/bold] to go back")
        choice = prompt("choice")

        if choice.lower() == "b" or choice == "":
            return

        try:
            proposal_id = int(choice)
        except ValueError:
            continue

        show_proposal_detail(proposal_id)


def show_proposal_detail(proposal_id):
    proposal = get_proposal(proposal_id)
    if not proposal:
        console.print(f"[red]Proposal {proposal_id} not found.[/red]")
        pause()
        return

    clear()
    console.print()

    status_colors = {
        "pending": "yellow", "approved": "green", "rejected": "red",
        "needs_revision": "orange1", "implemented": "cyan",
    }
    status = proposal.get("status", "pending")
    color = status_colors.get(status, "white")

    header = Text()
    header.append(f"Proposal #{proposal['id']}", style="bold yellow")
    header.append(f"  [{status}]", style=color)
    header.append(f"  created {proposal['created_at'][:10]}", style="dim")
    console.print(header)
    console.print()

    content = f"""## {proposal['title']}

**Summary:** {proposal['summary']}

**Services:** {proposal.get('services', '[]')}

**Estimated Monthly Cost:** {proposal.get('estimated_monthly_cost', 'N/A')}

---

### Architecture
{proposal.get('architecture', '')}

---

### Rationale
{proposal.get('rationale', '')}
"""
    if proposal.get("user_feedback"):
        content += f"\n---\n\n### Feedback\n{proposal['user_feedback']}\n"

    console.print(Panel(
        Markdown(content),
        title=f"[bold]{proposal['title']}[/bold]",
        border_style="yellow",
        padding=(1, 2),
    ))
    pause()


# ── Transmissions ─────────────────────────────────────────────────────

def show_transmissions():
    while True:
        clear()
        transmissions = list_transmissions(limit=50)
        if not transmissions:
            console.print(Panel("[dim]No transmissions yet.[/dim]", title="Transmissions"))
            pause()
            return

        table = Table(title="Transmissions", box=box.ROUNDED, border_style="green")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Title", min_width=20)
        table.add_column("Body", min_width=50)
        table.add_column("Date", width=12)

        for t in transmissions:
            table.add_row(str(t["id"]), t["title"], truncate(t["body"], 60), t.get("date", ""))

        console.print()
        console.print(table)
        console.print("\n  Enter a [bold]transmission ID[/bold] to read, or [bold]b[/bold] to go back")
        choice = prompt("choice")

        if choice.lower() == "b" or choice == "":
            return

        try:
            tid = int(choice)
        except ValueError:
            continue

        t = get_transmission(tid)
        if not t:
            console.print(f"[red]Transmission {tid} not found.[/red]")
            pause()
            continue

        clear()
        console.print()
        console.print(Panel(
            f"[dim]{t['date']}[/dim]\n\n{t['body']}",
            title=f"[bold]{t['title']}[/bold]",
            border_style="green",
            padding=(1, 2),
        ))
        pause()


# ── Experiments ───────────────────────────────────────────────────────

def show_experiments():
    while True:
        clear()
        experiments = list_experiments(limit=50)
        if not experiments:
            console.print(Panel("[dim]No experiments yet.[/dim]", title="Lab Experiments"))
            pause()
            return

        table = Table(title="Lab Experiments", box=box.ROUNDED, border_style="blue")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Slug", min_width=20)
        table.add_column("Title", min_width=25)
        table.add_column("Description", min_width=35)
        table.add_column("Created", width=12)

        for e in experiments:
            created = e["created_at"][:10] if e.get("created_at") else ""
            table.add_row(
                str(e["id"]),
                e["slug"],
                e["title"],
                truncate(e.get("description", ""), 45),
                created,
            )

        console.print()
        console.print(table)
        console.print("\n  Enter an [bold]experiment ID[/bold] to view, or [bold]b[/bold] to go back")
        choice = prompt("choice")

        if choice.lower() == "b" or choice == "":
            return

        try:
            eid = int(choice)
        except ValueError:
            continue

        e = get_experiment(eid)
        if not e:
            console.print(f"[red]Experiment {eid} not found.[/red]")
            pause()
            continue

        clear()
        console.print()
        header = Text()
        header.append(f"Experiment #{e['id']}", style="bold blue")
        header.append(f"  {e['slug']}", style="blue")
        header.append(f"  created {e['created_at'][:10]}", style="dim")
        console.print(header)
        console.print()
        console.print(render_tags(e.get("tags", "[]")))
        console.print()

        content = f"**{e['description']}**\n\n---\n\n"
        if e.get("html_content"):
            content += f"### HTML\n```html\n{e['html_content'][:500]}\n```\n\n"
        if e.get("css_content"):
            content += f"### CSS\n```css\n{e['css_content'][:500]}\n```\n\n"
        if e.get("js_content"):
            content += f"### JS\n```javascript\n{e['js_content'][:500]}\n```\n"

        console.print(Panel(
            Markdown(content),
            title=f"[bold]{e['title']}[/bold]",
            border_style="blue",
            padding=(1, 2),
        ))
        pause()


# ── Search ────────────────────────────────────────────────────────────

def show_search():
    clear()
    console.print()
    console.print(Panel("Full-text search across notes and artifacts", title="[bold]Search[/bold]", border_style="green"))
    query = prompt("search query")
    if not query:
        return

    note_results = search_notes(query, limit=10)
    artifact_results = search_artifacts(query, limit=10)

    clear()
    console.print()

    if not note_results and not artifact_results:
        console.print(f"[yellow]No results for '{query}'[/yellow]")
        pause()
        return

    if note_results:
        table = Table(title=f"Notes matching '{query}'", box=box.ROUNDED, border_style="cyan")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Title", min_width=30)
        table.add_column("Preview", min_width=40)

        for note in note_results:
            table.add_row(str(note["id"]), note["title"], truncate(note["content"], 60))
        console.print(table)
        console.print()

    if artifact_results:
        table = Table(title=f"Artifacts matching '{query}'", box=box.ROUNDED, border_style="magenta")
        table.add_column("ID", style="bold", width=4)
        table.add_column("Title", min_width=30)
        table.add_column("Type", width=12, style="magenta")

        for a in artifact_results:
            table.add_row(str(a["id"]), a["title"], a.get("artifact_type", ""))
        console.print(table)
        console.print()

    console.print("  Open: [bold]n<id>[/bold] for note, [bold]a<id>[/bold] for artifact, or [bold]b[/bold] to go back")
    choice = prompt("choice")

    if choice.lower() == "b" or choice == "":
        return
    elif choice.lower().startswith("n"):
        try:
            show_note_detail(int(choice[1:]))
        except ValueError:
            pass
    elif choice.lower().startswith("a"):
        try:
            show_artifact_detail(int(choice[1:]))
        except ValueError:
            pass


# ── Main Loop ─────────────────────────────────────────────────────────

def main():
    init_db()

    while True:
        show_dashboard()
        choice = prompt("choice")

        if choice == "1":
            show_notes()
        elif choice == "2":
            show_artifacts()
        elif choice == "3":
            show_proposals()
        elif choice == "4":
            show_transmissions()
        elif choice == "5":
            show_experiments()
        elif choice == "6":
            show_search()
        elif choice.lower() == "q":
            console.print("\n[dim]Goodbye.[/dim]\n")
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[dim]Goodbye.[/dim]\n")
        sys.exit(0)
