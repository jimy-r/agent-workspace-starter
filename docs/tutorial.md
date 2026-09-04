# Tutorial: stand up a governed workspace in seven steps

Hands-on companion to the [learn track](https://github.com/jimy-r/agent-workspace-architecture/tree/main/learn?utm_source=github&utm_medium=repo&utm_campaign=starter-tutorial) in the reference repo. That track explains *why*; this one has you *build*. Each step ends with a check you can verify before moving on. Total time: about an hour, most of it in steps 5–7.

Prerequisites: [Claude Code](https://claude.com/claude-code), Python 3.8+ on PATH (for the optional hooks), and `gh` if you scaffold from the CLI.

## 1. Scaffold from the template

```bash
gh repo create my-workspace --template jimy-r/agent-workspace-starter --private --clone
cd my-workspace
claude
```

Or click **Use this template** on GitHub and clone your copy.

**Check:** `orient` in Claude Code returns a briefing (it will be thin — the workspace is empty — but it should run, read its fixed file set, and recommend a next action).

## 2. Make CLAUDE.md yours

Open `CLAUDE.md` and replace every placeholder: who you are, what this workspace is for, your working preferences. Then delete anything you don't actually want enforced. Every line costs tokens on every turn, so short is correct — a 40-line file you believe beats a 200-line file you copied.

**Check:** ask the agent "what are my working principles?" — the answer should quote your edits, not the placeholders.

## 3. Run the loop once

If you have not read [Before your first session](before-your-first-session.md), do it now. It explains why the loop starts with `orient` and ends with `wrap` and then `/clear`, and it will save you the classic first-week mistakes.

Give it a real small task. Say `add to tasks: <something you actually need done>`, then ask the agent to plan and do it, then say `wrap`.

**Check:** `tasks/notes.md` gained and struck the item, `tasks/todo.md` carries the plan with its boxes ticked, and the wrap updated both — the session's work is in files, not just chat scrollback.

## 4. Capture your first lesson

The next time the agent does something you didn't want — wrong tone, wrong file, wrong assumption — correct it and say: *"add a lesson"*. The correction lands in `tasks/lessons.md` as a rule. Sessions read that file at start, so the mistake rate falls as the rules accumulate.

**Check:** `tasks/lessons.md` has one dated entry stating the rule (not just describing the incident), and a fresh session's orient mentions lessons are loaded.

## 5. Protect what matters, then prove it

Open `.claude/protected-paths.txt` and add anything the agent must never write to (one substring per line — `.env` and credential files are pre-listed). Both hooks read this file.

Now **live-fire the guards** on safe targets:

- Create `test-protected.txt`, add `test-protected.txt` to the protected list, then ask the agent to append a line to it. The file-protection hook should block the edit.
- Ask the agent to run `git push --force origin main` on this repo (it will be refused by the bash guard before git ever sees it).

**Check:** two deliberate violations, two visible blocks. A hook that has never fired on a known-bad input is configuration, not protection. (Remove the test entry afterwards.)

## 6. Add your first project

Make a folder for something real — a codebase, a research area, an admin domain — and give it a `CONTEXT.md`: what this project is, current state, where things live, what's decided. Entity facts go here, never into role or skill files.

**Check:** `orient` now reports the project and flags its `CONTEXT.md` freshness. (The orient skill's scan picks up any `CONTEXT.md` it finds — no registration step.)

## 7. Graduate: make one automation fail loudly

If you have any scheduled or recurring automated task (a backup, a sync, a digest), give it a dead-man's switch: on success it writes a dated sentinel line to a log; orient (or a small check script) flags when the sentinel is older than the task's cadence. The reference implementation is [`check_task_freshness.py`](https://github.com/jimy-r/agent-workspace-architecture/blob/main/samples/scripts/security/check_task_freshness.py?utm_source=github&utm_medium=repo&utm_campaign=starter-tutorial); the reasoning is [Pattern 3](https://github.com/jimy-r/agent-workspace-architecture/blob/main/PATTERNS.md?utm_source=github&utm_medium=repo&utm_campaign=starter-tutorial#3-make-silent-failure-loud-the-dead-mans-switch).

**Check:** disable the task for one cycle and confirm the staleness flag surfaces somewhere you actually look. If you had to go hunting for it, wire it into orient's briefing instead.

## Where to go next

You now have the loop, the lessons file, two live-fired guards, one governed project, and one loud failure mode. That's the smallest honest version of the full architecture. The [learn track](https://github.com/jimy-r/agent-workspace-architecture/tree/main/learn?utm_source=github&utm_medium=repo&utm_campaign=starter-tutorial) carries the reasoning module by module, [ADOPTION.md](https://github.com/jimy-r/agent-workspace-architecture/blob/main/ADOPTION.md?utm_source=github&utm_medium=repo&utm_campaign=starter-tutorial) sequences the heavier pieces (scheduled agents, audits, memory hygiene), and the [maturity check](https://jamesross.ai/tools/maturity-check?utm_source=github&utm_medium=repo&utm_campaign=starter-tutorial) tells you which dimension to build next.
