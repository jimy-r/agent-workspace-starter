# <Your name>'s workspace

> Always-loaded context that Claude Code reads at session start. Keep it short — every line costs tokens on every turn.

## What this is

<!-- Replace with one paragraph describing this workspace. Example: -->
> Multi-project workspace: personal admin, a side project, and a writing project. Each project folder has its own `CLAUDE.md` and `CONTEXT.md`.

## Working principles

- **Simplicity first** — prefer editing existing files; no new abstractions without clear need.
- **Minimal impact** — only touch what the task requires.
- **Ask before destructive actions** — delete, force-push, mass-rewrite all need confirmation.
- **Honest communication** — no performative agreement, no empty affirmations. When corrected, state what changes and why.

## Self-improvement loop

- After any user correction, append a rule to `tasks/lessons.md` **before** continuing other work. Format: `## YYYY-MM-DD — Short title`, what went wrong, the rule to follow.
- At session start, read `tasks/lessons.md` and apply its rules for the duration of the session.

## Task management

1. Write the plan to `tasks/todo.md` with checkable items.
2. Verify the plan with the user before implementing.
3. Mark items complete as you go.
4. Append a review section on completion (the `wrap` skill does this).

## Command shortcuts

Verbal phrases that map directly to a destination — go there without asking.

| Phrase | Target |
|---|---|
| "add to tasks" / "add to the list" | `tasks/notes.md` (append under the right `##` section) |
| "add a lesson" / "lesson learned: ..." | `tasks/lessons.md` (prepend entry) |
| "orient" / "get me up to speed" | run the `orient` skill |
| "tasks" / "what's on the list" | run the `tasks` skill |
| "wrap" / "close out" | run the `wrap` skill |

Rule: when a new shortcut emerges, ask once, then add it to this table — so the shortcut works next time.

## Credentials

**Iron Law: credentials never live in files.** Passwords, API keys, tokens, recovery codes all live in your password manager. This file references credentials only by their password-manager item name, never their value.

If a credential gets pasted into chat (happens occasionally), refuse to save it, explain why, and recommend regeneration — the transcript has already leaked it.

## Protected paths

The PreToolUse hooks in `.claude/settings.json` block agent writes to anything matching `.claude/protected-paths.txt`. If a legitimate edit is blocked, loosen the list deliberately — don't bypass the hook.
