"""
Skills integration module.
Reads skill instruction files from configurable directories
so the creative workspace can leverage installed skills
when producing formatted outputs.
"""

import os
import json
from pathlib import Path


# Default skill directories to scan.
# Override via SKILL_DIRS environment variable (colon-separated paths).
#
# To use your installed Claude Desktop skills, set SKILL_DIRS in your
# claude_desktop_config.json env block to point to where your skills live:
#
#   "env": {
#       "SKILL_DIRS": "/path/to/your/skills/public:/path/to/your/skills/user"
#   }
#
# Or simply place skill folders (each containing a SKILL.md) in a "skills/"
# subdirectory next to this server file.
DEFAULT_SKILL_DIRS = [
    # Cloud-hosted Claude paths (used when running inside Claude.ai sandbox)
    "/mnt/skills/public",
    "/mnt/skills/user",
    "/mnt/skills/private",
    "/mnt/skills/examples",
    # Common macOS Claude Desktop skill locations
    str(Path.home() / "Library" / "Application Support" / "Claude" / "skills"),
    str(Path.home() / ".claude" / "skills"),
]


def _get_skill_dirs() -> list[Path]:
    """Get configured skill directories."""
    env_dirs = os.environ.get("SKILL_DIRS", "")
    if env_dirs:
        dirs = [Path(d.strip()) for d in env_dirs.split(":") if d.strip()]
    else:
        dirs = [Path(d) for d in DEFAULT_SKILL_DIRS]

    # Also check a local skills directory relative to the server
    local_skills = Path(__file__).parent / "skills"
    if local_skills.exists():
        dirs.append(local_skills)

    return dirs


def discover_skills() -> list[dict]:
    """
    Scan all skill directories and return metadata for each discovered skill.
    A skill is any directory containing a SKILL.md file.
    """
    skills = []
    seen_names = set()

    for base_dir in _get_skill_dirs():
        if not base_dir.exists():
            continue

        for skill_dir in sorted(base_dir.iterdir()):
            if not skill_dir.is_dir():
                continue

            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                continue

            skill_name = skill_dir.name

            # Deduplicate — first found wins (priority order of dirs)
            if skill_name in seen_names:
                continue
            seen_names.add(skill_name)

            # Read first few lines for description
            try:
                content = skill_file.read_text(encoding="utf-8")
                # Extract description from first paragraph or heading
                lines = content.strip().split("\n")
                description_lines = []
                for line in lines[:10]:
                    if line.strip() and not line.startswith("#"):
                        description_lines.append(line.strip())
                    elif description_lines:
                        break
                description = " ".join(description_lines)[:300]
            except Exception:
                description = ""

            # Check for additional files in the skill directory
            extra_files = []
            for f in sorted(skill_dir.iterdir()):
                if f.is_file() and f.name != "SKILL.md":
                    extra_files.append(f.name)

            skills.append({
                "name": skill_name,
                "path": str(skill_file),
                "directory": str(skill_dir),
                "source": str(base_dir),
                "description": description,
                "extra_files": extra_files,
            })

    return skills


def read_skill(skill_name: str) -> dict:
    """
    Read the full SKILL.md content for a named skill.
    Returns the skill instructions and any additional file listings.
    """
    for base_dir in _get_skill_dirs():
        skill_dir = base_dir / skill_name
        skill_file = skill_dir / "SKILL.md"

        if skill_file.exists():
            try:
                content = skill_file.read_text(encoding="utf-8")

                # List other files in the skill directory
                extra_files = {}
                for f in sorted(skill_dir.iterdir()):
                    if f.is_file() and f.name != "SKILL.md":
                        # For small text files, include content; otherwise just list
                        try:
                            if f.suffix in (".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".py", ".js", ".css", ".html"):
                                file_content = f.read_text(encoding="utf-8")
                                if len(file_content) < 10000:
                                    extra_files[f.name] = file_content
                                else:
                                    extra_files[f.name] = f"[File too large: {len(file_content)} chars — read separately if needed]"
                            else:
                                extra_files[f.name] = f"[Binary file: {f.suffix}]"
                        except Exception:
                            extra_files[f.name] = "[Could not read file]"

                return {
                    "name": skill_name,
                    "path": str(skill_file),
                    "content": content,
                    "extra_files": extra_files,
                }

            except Exception as e:
                return {
                    "name": skill_name,
                    "error": f"Could not read skill file: {e}",
                }

    return {
        "name": skill_name,
        "error": f"Skill '{skill_name}' not found in any skill directory.",
        "searched": [str(d) for d in _get_skill_dirs()],
    }


def read_skill_file(skill_name: str, filename: str) -> dict:
    """
    Read a specific file from within a skill directory.
    Use this to access templates, examples, or config files
    bundled with a skill.
    """
    for base_dir in _get_skill_dirs():
        target = base_dir / skill_name / filename

        if target.exists() and target.is_file():
            try:
                # Try text first
                content = target.read_text(encoding="utf-8")
                return {
                    "skill": skill_name,
                    "filename": filename,
                    "content": content,
                    "size": len(content),
                }
            except UnicodeDecodeError:
                return {
                    "skill": skill_name,
                    "filename": filename,
                    "error": "Binary file — cannot display as text",
                    "size": target.stat().st_size,
                }
            except Exception as e:
                return {
                    "skill": skill_name,
                    "filename": filename,
                    "error": str(e),
                }

    return {
        "skill": skill_name,
        "filename": filename,
        "error": f"File '{filename}' not found in skill '{skill_name}'.",
    }
