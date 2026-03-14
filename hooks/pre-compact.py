#!/usr/bin/env python3
"""
Pre-Compact State Capture Hook

Fires before context compaction to capture current session state:
- Active TODO items from session logs
- Recent decisions and key context
- Current working directory and modified files

Hook Event: PreCompact
Output: Prints status to stderr (visible to user)
"""

from __future__ import annotations

import json
import os
import sys
import re
import hashlib
from pathlib import Path
from datetime import datetime

CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
NC = "\033[0m"


def get_session_dir() -> Path:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        base = Path.home() / ".claude" / "sessions" / "default"
    else:
        project_hash = hashlib.md5(project_dir.encode()).hexdigest()[:8]
        base = Path.home() / ".claude" / "sessions" / project_hash
    base.mkdir(parents=True, exist_ok=True)
    return base


def find_recent_session_log() -> dict | None:
    logs_dir = Path.home() / ".claude" / "session-logs"
    if not logs_dir.exists():
        return None
    log_files = sorted(logs_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not log_files:
        return None
    return {"log_path": str(log_files[0]), "log_name": log_files[0].name}


def extract_recent_decisions(limit: int = 4) -> list[str]:
    logs_dir = Path.home() / ".claude" / "session-logs"
    if not logs_dir.exists():
        return []
    log_files = sorted(logs_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not log_files:
        return []

    content = log_files[0].read_text()
    decisions = []
    patterns = [r"Decision:\s*(.+)", r"Decided:\s*(.+)", r"→\s*(.+)", r"\*\*Notes?\*\*:\s*(.+)"]

    for line in content.split("\n")[-60:]:
        for pattern in patterns:
            match = re.search(pattern, line.strip())
            if match and len(match.group(1)) > 15:
                decisions.append(match.group(1)[:120])
                if len(decisions) >= limit:
                    return decisions
    return decisions


def append_compaction_marker() -> None:
    logs_dir = Path.home() / ".claude" / "session-logs"
    if not logs_dir.exists():
        return
    log_files = sorted(logs_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not log_files:
        return
    try:
        with open(log_files[0], "a") as f:
            f.write(f"\n\n---\n")
            f.write(f"**Context compaction at {datetime.now().strftime('%H:%M')}**\n")
            f.write(f"Check session log and git status for current state.\n")
    except IOError:
        pass


def save_state(state: dict) -> None:
    state_file = get_session_dir() / "pre-compact-state.json"
    state["timestamp"] = datetime.now().isoformat()
    try:
        state_file.write_text(json.dumps(state, indent=2))
    except IOError as e:
        print(f"Warning: Could not save pre-compact state: {e}", file=sys.stderr)


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, IOError):
        hook_input = {}

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        return 0

    session_log = find_recent_session_log()
    decisions = extract_recent_decisions()

    state = {
        "project_dir": project_dir,
        "session_log": session_log,
        "decisions": decisions,
    }
    save_state(state)
    append_compaction_marker()

    lines = [f"\n{YELLOW}⚡ Context compaction starting — saving state{NC}", ""]

    if session_log:
        lines.append(f"{GREEN}Session log:{NC} {session_log['log_name']}")

    if decisions:
        lines.append(f"{GREEN}Recent decisions captured:{NC}")
        for d in decisions[:3]:
            lines.append(f"  • {d[:100]}")

    lines.append("")
    lines.append(f"{CYAN}Recovery: read session log + git log after compaction.{NC}")
    lines.append("")

    print("\n".join(lines), file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
