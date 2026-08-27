---
name: tasks
description: Use when the user says "tasks", "/tasks", "show me the tasks", or "what's on the list". Produces a concise readout of active items in tasks/notes.md. Lighter and more focused than `orient`.
---

## Purpose

Quick status readout of the task queue. No briefing, no recommendation — just what's on the list. Use when the user wants to see the state of work, not decide what to do next.

## Procedure

### 1. Read

- `tasks/notes.md`

### 2. Parse

**Iron Law: enumerate every `##` section before filtering.** The failure mode this skill exists to prevent is silently skipping a whole section. Do not shortcut by scanning for a subset of sections you remember — list them all first, then decide per-section whether to include.

1. Run a `Grep` for `^## ` across the file to enumerate every section header. Write down the full list.
2. For each section in that list, decide: include or skip. Only `## Completed` (historical table) is always skipped.
3. Within each included section, skip any bullet wrapped in `~~strikethrough~~`.
4. Group the surviving bullets under their `##` section header in the output.

**If a section has zero surviving bullets, omit it from the output — but you must have considered it.**

### 3. Output

**Active tasks** — grouped by section header. One bullet per item, terse. Preserve the user's wording.

**Counts** — at the end: `N active tasks across M sections.`

## Rules

- Do not read any other files. This is a task-queue readout, not a briefing.
- Do not recommend a next action. `orient` does that.
- Do not modify the file. Read-only.
- Keep the whole output under 250 words. If the queue is larger, truncate sections with `...and N more` rather than dumping everything.
