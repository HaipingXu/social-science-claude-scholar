#!/usr/bin/env python3
"""
Post-Compact Context Restoration Hook

Fires after context compaction (SessionStart with source="compact") to
restore session context: recent decisions, active session log, git status.

Hook Event: SessionStart (matcher: "compact|resume")
Output: Prints restoration context to stdout (shown to Claude)
"""

from __future__ import annotations

import json
import os
import sys
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


def read_pre_compact_state() -> dict | None:
    state_file = get_session_dir() / "pre-compact-state.json"
    if not state_file.exists():
        return None
    try:
        state = json.loads(state_file.read_text())
        state_file.unlink()
        return state
    except (json.JSONDecodeError, IOError):
        return None


def find_recent_session_log() -> dict | None:
    logs_dir = Path.home() / ".claude" / "session-logs"
    if not logs_dir.exists():
        return None
    log_files = sorted(logs_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not log_files:
        return None
    return {"log_path": str(log_files[0]), "log_name": log_files[0].name}


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, IOError):
        hook_input = {}

    source = hook_input.get("source", "")
    if source not in ("compact", "resume"):
        return 0

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if not project_dir:
        return 0

    pre_compact_state = read_pre_compact_state()
    session_log = find_recent_session_log()

    if not pre_compact_state and not session_log:
        return 0

    lines = [f"\n{CYAN}[Context Restored After Compaction]{NC}", ""]

    if pre_compact_state and pre_compact_state.get("decisions"):
        lines.append(f"{GREEN}Pre-Compaction Decisions:{NC}")
        for d in pre_compact_state["decisions"][-3:]:
            lines.append(f"  - {d}")
        lines.append("")

    if session_log:
        lines.append(f"{GREEN}Active Session Log:{NC}")
        lines.append(f"  {session_log['log_path']}")
        lines.append("")

    lines.append(f"{YELLOW}Recovery Actions:{NC}")
    lines.append("  1. Read the session log above to understand current objectives")
    lines.append("  2. Run: git log --oneline -5 && git diff --stat")
    lines.append("  3. Continue from where you left off")
    lines.append("")

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
