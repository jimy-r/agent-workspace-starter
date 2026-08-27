"""
PreToolUse Edit/Write hook -- block agent modification of protected files.

Reads the Claude Code hook JSON payload from stdin, extracts the target
file_path from tool_input, normalises it, and refuses Edit/Write tool
calls whose target contains any protected substring.

Protected substrings come from `.claude/protected-paths.txt` (one per
line, '#' comments allowed). If that file is missing, the DEFAULTS below
apply. The same list drives check_bash_command.py, so a path blocked at
one tool boundary is blocked at the other.

Claude Code hook protocol:
    - stdin: JSON payload {"tool_name": "Edit"|"Write", "tool_input": {"file_path": "..."}}
    - exit 0: allow
    - exit 2: block (stderr message is surfaced to the agent)

Fails open on parse errors or script bugs -- a buggy hook must not brick
the agent's ability to edit files. This is a mistake-catcher, not a
security boundary: processes that open files internally are out of scope.
"""

from __future__ import annotations

import json
import os
import sys

DEFAULTS: list[str] = [
    ".env",
    "credentials",
    "secrets",
    ".key",
    ".pem",
]

CONFIG_RELPATH = os.path.join(".claude", "protected-paths.txt")


def load_protected() -> list[str]:
    """Read protected substrings from config; fall back to DEFAULTS."""
    root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    config = os.path.join(root, CONFIG_RELPATH)
    try:
        with open(config, encoding="utf-8") as fh:
            entries = [
                line.strip().replace("\\", "/").lower()
                for line in fh
                if line.strip() and not line.strip().startswith("#")
            ]
        return entries or list(DEFAULTS)
    except OSError:
        return list(DEFAULTS)


def _normalise(path: str) -> str:
    return path.replace("\\", "/").lower()


def check(path: str, protected: list[str]) -> tuple[bool, str]:
    if not path:
        return False, ""
    normalised = _normalise(path)
    for entry in protected:
        if entry in normalised:
            return True, (
                f"Edit/Write blocked: '{path}' matches protected substring "
                f"'{entry}' (see .claude/protected-paths.txt). If this edit "
                f"is legitimate, remove or narrow the entry deliberately -- "
                f"don't bypass the hook."
            )
    return False, ""


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read())
    except Exception:
        return 0
    tool_input = payload.get("tool_input", {}) or {}
    path = tool_input.get("file_path") or tool_input.get("path") or ""
    blocked, reason = check(path, load_protected())
    if blocked:
        sys.stderr.write(reason)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # intentional fail-open
        print(f"[protect-files-hook] hook error (failing open): {exc}", file=sys.stderr)
        sys.exit(0)
