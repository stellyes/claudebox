"""
Branch Manager — Git branch workflow for experimental research.

Adapted from autoresearch's git-branch-per-experiment pattern:
risky or experimental work happens on branches. Only merge to
master after evaluation passes the quality gate.

Phase 3 of the autoresearch adaptation.
"""

import subprocess
import re
from datetime import datetime, timezone


BRANCH_PREFIX = "research/"


def _run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a git command and return the result."""
    return subprocess.run(
        ["git"] + args,
        capture_output=True, text=True,
        check=check,
        cwd="/Users/slimreaper/Documents/claudebox",
    )


def current_branch() -> str:
    """Get the current git branch name."""
    result = _run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    return result.stdout.strip()


def is_on_experiment_branch() -> bool:
    """Check if we're currently on a research experiment branch."""
    return current_branch().startswith(BRANCH_PREFIX)


def create_experiment_branch(tag: str) -> dict:
    """
    Create a new experiment branch from master.

    Args:
        tag: Short identifier for the experiment (e.g. "transmission-arc-6",
             "identity-arc-start", "site-redesign-v2")

    Returns:
        dict with branch name and status.
    """
    # Sanitize tag
    safe_tag = re.sub(r"[^a-z0-9\-]", "-", tag.lower().strip())
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    branch_name = f"{BRANCH_PREFIX}{safe_tag}-{date_str}"

    # Make sure we're on master first
    cur = current_branch()
    if cur != "master":
        return {
            "status": "error",
            "message": f"Must be on master to create experiment branch. Currently on: {cur}",
        }

    # Create and switch to the branch
    result = _run_git(["checkout", "-b", branch_name], check=False)
    if result.returncode != 0:
        return {"status": "error", "message": result.stderr.strip()}

    return {
        "status": "created",
        "branch": branch_name,
        "message": f"Created experiment branch: {branch_name}. Work here freely — merge to master when quality gate passes.",
    }


def list_experiment_branches() -> list[dict]:
    """List all experiment branches with their last commit info."""
    result = _run_git(
        ["branch", "--list", f"{BRANCH_PREFIX}*", "--format=%(refname:short) %(committerdate:short) %(subject)"],
        check=False,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return []

    branches = []
    for line in result.stdout.strip().split("\n"):
        parts = line.split(" ", 2)
        if len(parts) >= 3:
            branches.append({
                "branch": parts[0],
                "last_commit_date": parts[1],
                "last_commit_msg": parts[2],
            })
        elif len(parts) == 2:
            branches.append({
                "branch": parts[0],
                "last_commit_date": parts[1],
                "last_commit_msg": "",
            })
    return branches


def merge_experiment(branch_name: str | None = None) -> dict:
    """
    Merge an experiment branch into master.

    If branch_name is None, merges the current branch (if it's an experiment branch).

    Returns:
        dict with status and message.
    """
    if branch_name is None:
        branch_name = current_branch()

    if not branch_name.startswith(BRANCH_PREFIX):
        return {
            "status": "error",
            "message": f"Not an experiment branch: {branch_name}",
        }

    # Switch to master
    result = _run_git(["checkout", "master"], check=False)
    if result.returncode != 0:
        return {"status": "error", "message": f"Failed to switch to master: {result.stderr.strip()}"}

    # Merge
    result = _run_git(["merge", branch_name, "--no-ff"], check=False)
    if result.returncode != 0:
        # Abort the failed merge
        _run_git(["merge", "--abort"], check=False)
        return {"status": "error", "message": f"Merge failed: {result.stderr.strip()}"}

    return {
        "status": "merged",
        "branch": branch_name,
        "message": f"Merged {branch_name} into master.",
    }


def discard_experiment(branch_name: str | None = None) -> dict:
    """
    Discard an experiment branch (switch to master and delete the branch).

    If branch_name is None, discards the current branch.
    """
    if branch_name is None:
        branch_name = current_branch()

    if not branch_name.startswith(BRANCH_PREFIX):
        return {
            "status": "error",
            "message": f"Not an experiment branch: {branch_name}",
        }

    if current_branch() == branch_name:
        result = _run_git(["checkout", "master"], check=False)
        if result.returncode != 0:
            return {"status": "error", "message": f"Failed to switch to master: {result.stderr.strip()}"}

    result = _run_git(["branch", "-D", branch_name], check=False)
    if result.returncode != 0:
        return {"status": "error", "message": f"Failed to delete branch: {result.stderr.strip()}"}

    return {
        "status": "discarded",
        "branch": branch_name,
        "message": f"Discarded experiment branch: {branch_name}",
    }


def experiment_diff(branch_name: str | None = None) -> str:
    """
    Get the diff between an experiment branch and master.

    Returns the diffstat summary.
    """
    if branch_name is None:
        branch_name = current_branch()

    result = _run_git(["diff", "--stat", f"master...{branch_name}"], check=False)
    return result.stdout.strip() if result.returncode == 0 else "Unable to generate diff."
