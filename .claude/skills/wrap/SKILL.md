---
name: wrap
description: Use when closing out a completed task to integrate it into the required files. Updates the task list, review section, and any registry/index the change belongs in. Invoke via "wrap", "/wrap", "wrap this up", or "close out".
---

## Purpose

Stop rediscovering the integration checklist every time a task finishes. `wrap` is the canonical close-out ritual: it turns "done in the code" into "done across all the places that need to know about it."

## Iron Law

**If the task added, renamed, or removed something that lives in a registry, the registry must be updated in the same turn.** A shortcut without a row in the Command shortcuts table is invisible next session. No exceptions.

## Procedure

### 1. Summarize what was done

One or two lines. Name the files touched and the outcome. If nothing material changed, stop here and tell the user — don't fabricate a close-out.

### 2. Update the active plan — `tasks/todo.md`

- Mark plan items complete (`[ ]` → `[x]`).
- Append or fill a `## Review` section: what was built, files created/modified, any open follow-ups.

### 3. Strike through the bullet in `tasks/notes.md`

Find the matching bullet under the correct `##` section. Wrap it in `~~...~~` and append `*(Done YYYY-MM-DD — <one-line summary with key file paths>)*`.

If the task was not on the notes list, skip this step — don't invent an entry retroactively.

### 4. Registry / index sweep — THE STEP PEOPLE FORGET

For each row, ask: *did this task add, rename, or remove something that belongs here?* If yes, update that file in this turn.

| Change type | Registry to update |
|---|---|
| New / removed verbal shortcut | **Command shortcuts** table in `CLAUDE.md` |
| New protected path | `.claude/protected-paths.txt` |
| New / removed skill or hook | the "What's inside" table in `README.md`, if you keep one |
| Stack / deployment / constraint change on a project | that project's `CONTEXT.md` |

### 5. Lessons check

If this task surfaced a mistake pattern worth preventing in future sessions, prepend a `## YYYY-MM-DD — <short title>` block to `tasks/lessons.md`. Skip if nothing was learned — don't pad the file with platitudes.

### 6. Report

End with a tight summary:

- **Touched:** file list with one-line reason each
- **Skipped:** registries/files considered and deliberately not updated, with reason
- **Needs user confirmation:** anything requiring a user decision before it can be closed

## Rules

- **Do not invent history.** If a step doesn't apply, say so and skip it.
- **Don't overwrite another agent's work.** If you see evidence of concurrent edits (unexpected diffs, new files you didn't make), stop and ask before overwriting.
- **Don't mark tasks complete that aren't verified.** `wrap` assumes the task is already done and verified.
- **Strike-through, don't delete.** Historical bullets in `tasks/notes.md` stay visible with a done date — they're the audit trail.
