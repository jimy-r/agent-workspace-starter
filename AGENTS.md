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

Before you commit, run what CI runs locally: `python -m json.tool` over every
JSON file under `.claude/`, and a `py_compile` pass over each hook in
`.claude/hooks/`. Python 3.12 is the version CI uses.

CI also runs each hook exactly as `.claude/settings.json` wires it, from a
directory outside the repo, and asserts exit 2 on a known-bad payload and 0 on
a benign one. That check is an inline script in the last `validate` step of
[`.github/workflows/ci.yml`](.github/workflows/ci.yml), so there is no local
command to run. It runs in CI on every pull request and push to main.
