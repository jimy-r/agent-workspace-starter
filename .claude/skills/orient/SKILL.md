---
name: orient
description: Use at the start of a new session when the user says "orient", "/orient", or asks to get up to speed on the workspace. Produces a briefing of active state, in-flight work, staleness flags, and a recommended next action.
---

## Purpose

Bring Claude up to speed on this workspace quickly and deterministically at session start, without burning context on speculative exploration. Output is a concise briefing the user can redirect.

## Iron Law

**Read the fixed file set below. Do not wander.** If a file listed here doesn't exist, note it and move on — don't improvise replacements.

## Procedure

### 1. Read (in parallel)

- `CLAUDE.md` — workspace working context (includes the Command shortcuts table)
- `tasks/todo.md` — current implementation plan
- `tasks/lessons.md` — self-improvement rules to apply this session
- `tasks/notes.md` — master task list (scan active sections; skip the `## Completed` table)

### 2. Freshness scan

Glob for `*/CONTEXT.md` and `*/PLAN.md` across project folders and check mtime. Flag any older than 30 days as potentially stale. Do NOT read the files — just check mtime.

### 3. Produce the briefing

Output under 300 words, structured as:

**Active state** — one line on where the workspace is right now.

**In-flight work** — anything with an open plan or checklist that isn't closed. Cite file paths.

**Staleness flags** — any CONTEXT.md / PLAN.md older than 30 days.

**Lessons active this session** — one-line summary per entry in `lessons.md`.

**Recommended next action** — one task with a one-sentence tradeoff. Present as "I'd pick X because Y; alternatives are Z" — something the user can redirect, not a decided plan.

## Rules

- Do NOT read project source code or docs beyond the file set above. The user can ask for depth on a specific project after orienting.
- Do NOT fire subagents during orient — the file set is small and bounded.
- Do NOT write to any file during orient — this is read-only.
- Do NOT include the `## Completed` historical tables in what you summarize.
- If a listed file is missing, note it in the briefing as a structural flag — don't skip silently.
- End with one question offering direction: "Want depth on any of these, or start on the recommended next action?"
