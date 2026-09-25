# AGENTS.md

Instructions for any coding agent working in this repository, in the
[agents.md](https://agents.md/) format.

This repo is a template: the smallest working scaffold for a governed agent
workspace in Claude Code. Everything here is copied verbatim into someone
else's repository by "Use this template", so nothing private, machine-specific
or personal ever belongs in a file.

[`CLAUDE.md`](CLAUDE.md) carries the working rules and is the file to read
first; it is the same content Claude Code loads automatically. Humans start at
[`README.md`](README.md), contributors at [`CONTRIBUTING.md`](CONTRIBUTING.md).

Before you commit, run what CI runs: `python -m json.tool` over every JSON file
under `.claude/`, a `py_compile` pass over each hook in `.claude/hooks/`, and
the hook payload check (each hook, run as `.claude/settings.json` wires it, must
exit 2 on a known-bad payload and 0 on a benign one).
Python 3.12 is the version CI uses.
