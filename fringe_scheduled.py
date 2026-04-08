"""
Scheduled fringe probe — intended to be triggered by launchd every
4 hours (see scheduled/online.claudegoes.fringe.plist).

This is the non-MCP path: it runs the probe as a plain Python process,
posts the suggested transmission to the local SQLite db, republishes
transmissions.json, and syncs to S3 + invalidates CloudFront so the
homepage heartbeat stays fresh. No Claude session, no MCP handshake —
just the work the MCP tool would do if it were called.

Logs to scheduled/fringe.log so launchd output stays out of ~.
Never raises: any failure is written to the log and the process exits 0
so launchd does not keep retrying.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# Load .env so SERPAPI_KEY is visible to the fringe module
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

LOG_PATH = ROOT / "scheduled" / "fringe.log"
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log(msg: str) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{stamp}] {msg}\n"
    try:
        with LOG_PATH.open("a") as f:
            f.write(line)
    except Exception:
        pass
    # Also echo to stdout so launchd StandardOutPath captures it
    print(line, end="")


async def run_once() -> dict:
    from fringe import run_fringe_probe
    return await run_fringe_probe(num_results=10)


def post_and_deploy(result: dict) -> None:
    """If the probe produced a suggested transmission, save it and deploy."""
    from database import save_transmission, list_transmissions
    from website import publish_transmissions, deploy_site

    suggested = result.get("suggested_transmission") or {}
    title = suggested.get("title")
    body = suggested.get("body")
    if not (title and body):
        log("No suggested transmission — skipping post/deploy")
        return

    saved = save_transmission(title, body, None)
    log(f"Saved transmission id={saved.get('id')}: {title}")

    publish_transmissions(list_transmissions())
    log("Republished transmissions.json")

    deploy = deploy_site()
    if deploy.get("status") == "deployed":
        log("Deployed to S3 + invalidated CloudFront")
    else:
        log(f"Deploy error: {deploy.get('error') or deploy}")


def main() -> int:
    log("=== scheduled fringe probe start ===")
    if not os.environ.get("SERPAPI_KEY"):
        log("ERROR: SERPAPI_KEY not set — skipping probe")
        return 0

    try:
        result = asyncio.run(run_once())
    except Exception as e:
        log(f"EXCEPTION during probe: {e}")
        log(traceback.format_exc())
        return 0

    status = result.get("status")
    log(f"probe status={status}")

    if status == "error":
        log(f"probe error: {result.get('error')}")
        return 0

    if status != "ok":
        log(f"probe non-ok status, skipping post: {json.dumps(result)[:300]}")
        return 0

    topic = result.get("topic", {})
    log(f"topic={topic.get('slug')} kind={topic.get('kind')} results={result.get('num_results')}")
    log(f"source_page={result.get('source_page')}")
    log(f"concept_page={result.get('concept_page')}")

    try:
        post_and_deploy(result)
    except Exception as e:
        log(f"EXCEPTION during post/deploy: {e}")
        log(traceback.format_exc())

    log("=== scheduled fringe probe done ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
