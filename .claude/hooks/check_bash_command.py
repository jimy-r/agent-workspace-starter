"""
PreToolUse Bash hook -- close the Bash gap in Edit/Write file protection
and block dangerous git operations.

The Edit/Write hook (protect_files.py) gates direct file-tool calls
against the protected-path list, but shell-level filesystem operations
(`mv`, `cp`, `sed -i`, `rm`, output redirection `>` / `>>`) bypass it
because they arrive through the `Bash` tool. This hook covers that gap.

It refuses two categories of command:

    1. File writes to protected paths -- any write-intent verb (`>` /
       `>>` / `rm` / `mv <dest>` / `cp <dest>` / `sed -i` / `tee` /
       `touch` / `chmod` / `chown` / `truncate`) whose target contains a
       protected substring (case-insensitive, normalised to forward
       slashes). The list comes from `.claude/protected-paths.txt`,
       shared with protect_files.py; DEFAULTS apply if it's missing.

    2. Dangerous git operations -- `git push` targeting `main` or
       `master`, any force push, `git reset --hard` against main/master.

This is *defence-in-depth*, not paranoia. The bar is "catch casual
mistakes," not "stop a determined adversary." Processes that open files
internally (`open(path, 'w')`) are out of scope -- the hook can't
inspect process behaviour.

Known sharp edge: the hook matches command TEXT, not parsed intent. A
commit message containing "main" near a `git push` in the same command
string can false-positive. Run `git commit` and `git push` as separate
commands rather than bypassing the hook.

Claude Code hook protocol:
    - stdin: JSON payload {"tool_name": "Bash", "tool_input": {"command": "..."}}
    - exit 0: allow
    - exit 2: block (stderr message is surfaced to the agent; JSON on
      stdout with {"decision": "block", "reason": "..."} is the
      structured form)

If the hook script itself errors, it fails open (exit 0, no block) so a
bug here does NOT brick the agent's ability to run Bash.
"""

from __future__ import annotations

import json
import os
import re
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


# ---------------------------------------------------------------------------
# Write-intent patterns. Each captures the target path as group(2).
# The path token is terminated by whitespace, pipe, semicolon, ampersand,
# or end of string. Single and double quotes optionally wrap the target.
# ---------------------------------------------------------------------------

_PATH = r"(['\"]?)([^\s'\"|&;<>]+)\1"

WRITE_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(rf"(?<![2&])>\s*{_PATH}"), "shell redirection '>'"),
    (re.compile(rf">>\s*{_PATH}"), "shell append '>>'"),
    (re.compile(rf"2>\s*{_PATH}"), "stderr redirection '2>'"),
    (re.compile(rf"\brm\s+(?:-[rRfv]+\s+)*{_PATH}"), "rm"),
    (re.compile(rf"\bmv\s+\S+\s+{_PATH}"), "mv (destination)"),
    (re.compile(rf"\bcp\s+(?:-\S+\s+)*\S+\s+{_PATH}"), "cp (destination)"),
    (re.compile(rf"\bsed\s+-i\S*\s+.+?\s+{_PATH}"), "sed -i (in-place edit)"),
    (re.compile(rf"\btee\s+(?:-[aA]\s+)?{_PATH}"), "tee"),
    (re.compile(rf"\btouch\s+{_PATH}"), "touch"),
    (re.compile(rf"\bchmod\s+\S+\s+{_PATH}"), "chmod"),
    (re.compile(rf"\bchown\s+\S+\s+{_PATH}"), "chown"),
    (re.compile(rf"\btruncate\s+\S+\s+{_PATH}"), "truncate"),
]

# ---------------------------------------------------------------------------
# Dangerous git operations -- blocked regardless of target path.
# ---------------------------------------------------------------------------

DANGEROUS_GIT: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"\bgit\s+push\s+(?:\S+\s+)*(?:origin\s+)?main(?:\s|:|$)"),
        "git push to 'main' is forbidden -- use a feature branch + PR",
    ),
    (
        re.compile(r"\bgit\s+push\s+(?:\S+\s+)*(?:origin\s+)?master(?:\s|:|$)"),
        "git push to 'master' is forbidden -- use a feature branch + PR",
    ),
    (
        re.compile(
            r"\bgit\s+push\s+(?:\S+\s+)*(?:-f\b|--force\b|--force-with-lease\b)"
        ),
        "git force-push is forbidden",
    ),
    (
        re.compile(r"\bgit\s+reset\s+--hard\s+(?:origin/)?(?:main|master)\b"),
        "git reset --hard on main/master is forbidden",
    ),
]


def _normalise_target(target: str) -> str:
    return target.replace("\\", "/").lower()


def check_protected_writes(command: str, protected: list[str]) -> tuple[bool, str]:
    """Return (blocked, reason) if the command writes to a protected path."""
    for pattern, verb in WRITE_PATTERNS:
        for match in pattern.finditer(command):
            normalised = _normalise_target(match.group(2))
            for entry in protected:
                if entry in normalised:
                    return True, (
                        f"{verb} targets protected path '{match.group(2)}' "
                        f"(matches '{entry}' in .claude/protected-paths.txt). "
                        f"If legitimate, narrow the entry deliberately -- "
                        f"don't bypass the hook."
                    )
    return False, ""


def check_dangerous_git(command: str) -> tuple[bool, str]:
    """Return (blocked, reason) if the command is a dangerous git op."""
    for pattern, reason in DANGEROUS_GIT:
        if pattern.search(command):
            return True, reason
    return False, ""


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    command = payload.get("tool_input", {}).get("command", "")
    if not isinstance(command, str) or not command:
        return 0

    blocked, reason = check_protected_writes(command, load_protected())
    if not blocked:
        blocked, reason = check_dangerous_git(command)

    if blocked:
        print(json.dumps({"decision": "block", "reason": f"[bash-guard] {reason}"}))
        print(f"[bash-guard] BLOCKED: {reason}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # intentional fail-open
        print(f"[bash-guard] hook error (failing open): {exc}", file=sys.stderr)
        sys.exit(0)
