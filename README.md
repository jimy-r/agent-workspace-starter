# agent-workspace-starter

A minimal, working scaffold for a **governed agent workspace** in [Claude Code](https://claude.com/claude-code). Click "Use this template", open a terminal in your copy, and you have session discipline (orient → work → wrap), a self-improvement loop, and two safety hooks running on day one.

This is the runnable companion to **[agent-workspace-architecture](https://github.com/jimy-r/agent-workspace-architecture?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter)** — a documented production workspace published as a reference. The reference explains the patterns and the reasoning; this template is the smallest honest subset you can actually start from. **[Take the interactive tour](https://jimy-r.github.io/agent-workspace-architecture/?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter)** of the full system to see where a workspace like this can go.

## Quickstart

```bash
# 1. Scaffold your workspace from this template
gh repo create my-workspace --template jimy-r/agent-workspace-starter --private --clone
cd my-workspace

# 2. Open Claude Code
claude

# 3. Say:
#    "orient"        → briefing on workspace state + recommended next action
#    "add to tasks: <thing>"  → captured in tasks/notes.md
#    "wrap"          → close-out ritual when a task finishes
```

No build step, no dependencies beyond Python 3.8+ on PATH (for the optional hooks — delete the `hooks` block in `.claude/settings.json` if you don't want them).

## What's inside

| Path | What it does |
|---|---|
| `CLAUDE.md` | Always-loaded context: working principles, command shortcuts, credential law. Edit the placeholders first. |
| `.claude/skills/orient/` | Session-start briefing: reads a fixed file set, reports state, recommends one next action. Read-only by design. |
| `.claude/skills/wrap/` | Close-out ritual: updates the plan, strikes the task bullet, sweeps registries, captures lessons. |
| `.claude/skills/tasks/` | Quick task-queue readout, lighter than orient. |
| `.claude/hooks/protect_files.py` | PreToolUse guard: blocks agent edits to protected paths (`.env`, credentials, anything you list). |
| `.claude/hooks/check_bash_command.py` | PreToolUse guard: blocks shell-level writes to the same paths, plus force-pushes and pushes to main. |
| `.claude/protected-paths.txt` | One place to declare what the agent must never write to. |
| `tasks/todo.md` | The active implementation plan (plan first, then build). |
| `tasks/notes.md` | Your running task list, grouped by topic. |
| `tasks/lessons.md` | The self-improvement loop: every correction becomes a rule the next session reads. |

## The loop this scaffolds

1. **Orient at session start.** The agent reads a small fixed file set and tells you where things stand. No wandering, no speculative exploration.
2. **Plan before building.** Work gets a checklist in `tasks/todo.md`; you approve it before implementation.
3. **Capture corrections as lessons.** When you correct the agent, the correction is written to `tasks/lessons.md` before work continues. Sessions start by reading it. The mistake rate drops because the rules accumulate.
4. **Wrap when done.** Completed work is integrated everywhere it needs to be recorded, not just left in the diff.

That loop is the smallest version of the governance patterns documented in the reference repo — see [PATTERNS.md](https://github.com/jimy-r/agent-workspace-architecture/blob/main/PATTERNS.md?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter) for the full set (scheduled agents, review queues, audits, memory hygiene) and what each one costs.

## The hooks, honestly

The two guards are **mistake-catchers, not security boundaries**. They block the casual failure modes — an agent redirecting output over your `.env`, a well-meaning force-push — by string-matching tool calls before they run. A determined process writing files from inside Python is out of scope. They fail open: a bug in a hook will never brick your session.

Declare what's off-limits in `.claude/protected-paths.txt` (one substring per line). Both hooks read it; sensible defaults apply if it's missing.

Two known sharp edges, inherited from real use: the bash guard matches command *text*, so a commit message containing "push" near "main" can false-positive (run commit and push as separate commands), and any path containing a protected substring is blocked even in quoted strings. Loosen the list rather than fighting it.

## Customising

- `CLAUDE.md` — replace the placeholders, trim what you don't use. Every line costs tokens on every turn; short is correct.
- Add project folders, each with its own `CONTEXT.md` (entity facts) — orient's freshness scan picks them up automatically.
- New verbal shortcut? Add a row to the Command shortcuts table in `CLAUDE.md` so it works next session.
- Outgrowing the starter? The reference repo documents the next pieces in adoption order: [ADOPTION.md](https://github.com/jimy-r/agent-workspace-architecture/blob/main/ADOPTION.md?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter).

## Who built this

James Ross. I design agent workspaces and AI-orchestration systems; this template is extracted from the workspace I run daily, published in full (redacted) at [agent-workspace-architecture](https://github.com/jimy-r/agent-workspace-architecture?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter). If you're standing up something similar inside an organisation, the practice site is **[jamesross.ai](https://jamesross.ai)**.

Maintained best-effort as a curated artifact: no roadmap, no SLA. Issues for real defects welcome.

## License

[MIT](LICENSE). Fork freely; that's what it's for.
