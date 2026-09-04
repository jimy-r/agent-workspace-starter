# Before your first session: how context works

Most first-week trouble with an agent workspace is not the agent. It is context, which means what the model can see, how that changes as a session runs, and what happens when it fills up. Five minutes here saves a lost afternoon.

## What the agent can see

The model has no memory between requests. Every time it takes a step (a reply, a file read, a command), the whole conversation so far is sent again. That includes your instructions file, every message, every file it opened and every result it got back. That growing pile is the context. A session that has read forty files is carrying all forty on every step, whether the current step needs them or not.

Between sessions, nothing carries over except what is on disk. That is why this template keeps state in files (`tasks/todo.md`, `tasks/notes.md`, `tasks/lessons.md`) and why the first word of every session is `orient`. The agent rebuilds its picture from those files, not from a chat that no longer exists.

## Why long sessions go wrong

Three things happen as context fills.

- **The thread gets harder to hold.** Material from an earlier, unrelated task is still in the room, and the model weighs it. Answers drift, old constraints resurface, and the agent starts solving the wrong problem well.
- **Compaction happens to you.** Near the limit, Claude Code replaces the transcript with a summary. The summary is good at the gist and bad at detail: a decision and its reason, a half-finished edit, a rule you stated an hour ago. If it fires mid-task, the agent continues from the summary and does not know what it lost.
- **Every step costs more.** Each step re-reads the pile, so a big session is slow and expensive on every step that follows, whatever made it big. The reference repo's Pattern 18 has the measurements.

## Five habits

1. **One task per session.** When the next thing does not need this conversation, say `wrap`, then `/clear`, then `orient`. The test is whether the next task needs this history. Same project does not count. A fresh session that reads the state files knows everything that matters and nothing that does not.

2. **Ask for several things at once.** Each message is at least one full re-read. "Rename the function, update the two callers and run the tests" is one step of carry. The same three requests one at a time are three, and the later ones carry the earlier ones' output. Separate requests only when the second genuinely depends on the answer to the first.

3. **Compact on purpose, not by surprise.** If a task is long enough that the window will fill, compact at a clean point. `/compact` takes a note on what to keep ("keep the plan, the files in flight and the open questions"). Do it before the limit, at a moment when nothing is half done, so the summary is made of finished thoughts.

4. **Never restructure the workspace at high context.** Edits to `CLAUDE.md`, the skills, the hooks or `protected-paths.txt` change how every future session behaves. Make them in a fresh session, with a small context and a clear head, and check them in the session after. A workspace edit made at the end of a long, tired session is the most common way to break the loop.

5. **Put the memory in files.** Decisions, plans and open questions belong in the task files, and `wrap` puts them there. If it exists only in the scrollback, it is gone at `/clear`, and it is gone at compaction too.

## How this fits the loop

`orient` reads the state files so a session can start small. Work happens in a scoped session. `wrap` writes the outcome back to disk. `/clear` closes the room. The loop is the habit list in ritual form, which is why the template makes three words do the work.

## When you are ready for more

The reference repo goes deeper. [Pattern 9, "Context is a budget, not a constant"](https://github.com/jimy-r/agent-workspace-architecture/blob/main/PATTERNS.md?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter#9-context-is-a-budget-not-a-constant) covers ceilings and what must survive a compaction. [Pattern 18, "Position is price"](https://github.com/jimy-r/agent-workspace-architecture/blob/main/PATTERNS.md?utm_source=github&utm_medium=repo&utm_campaign=agent-workspace-starter#18-position-is-price--a-token-costs-more-the-earlier-you-add-it) has the numbers behind why an early file read is the expensive one.
