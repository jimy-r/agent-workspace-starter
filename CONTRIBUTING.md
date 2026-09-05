# Contributing

This is a template repository. Every copy made with "Use this template" is independent from the moment it is created, so a fix here reaches copies made after it and nothing else. That shapes what is worth reporting.

> Reading this inside your own copy? "Use this template" brought this file and `.github/ISSUE_TEMPLATE/` along with the scaffold. They describe contributing to the template, not to your workspace. Delete both, or replace them with your own.

## In scope

- A defect in the template as shipped: a hook that crashes, a skill that references a file the template does not contain, a broken link, an instruction in `CLAUDE.md` that contradicts another one.
- A step in [`docs/tutorial.md`](docs/tutorial.md) or [`docs/before-your-first-session.md`](docs/before-your-first-session.md) that does not work as written on a fresh copy.
- Something that breaks under the only dependency the template claims, Python 3.8+ on PATH.

## Out of scope

- Anything in your own copy after you have customised it. That workspace is yours from creation and this repo has no view into it.
- New skills, hooks or routines. The template stays the smallest honest subset. The larger pattern set lives in [agent-workspace-architecture](https://github.com/jimy-r/agent-workspace-architecture), which takes component proposals.
- Claude Code itself. Bugs in the CLI, the hooks engine or the skills loader go to [anthropics/claude-code](https://github.com/anthropics/claude-code).

## Reporting a defect

Open an issue with the [bug report form](../../issues/new?template=bug_report.yml). It asks which commit you copied and what you ran, because a template defect has to be reproducible on a fresh copy before it can be fixed. Search the open issues first; a near-duplicate is the most common reason a report goes nowhere.

## Sending a change

Fork, branch, one focused change per pull request, [conventional commit](https://www.conventionalcommits.org/) messages. If an agent drafted the change, say so in the pull request and add a `Co-Authored-By:` trailer.

Two things will get a pull request declined whatever its quality:

- It adds surface. The template is deliberately small, and a component that helps some copies is dead weight in the rest.
- It puts something private in a file: a real name, an address, a path from your own machine, a credential even as a placeholder. Every file here is copied verbatim into other people's repositories.

## Maintenance, honestly

Best-effort and solo. No roadmap and no service level. Silence on an issue is a queue rather than a decision, and a well-made proposal can still be declined for pulling the template away from minimal.

Keep exchanges straightforward and on the work. Conduct concerns go through [GitHub's report abuse](https://github.com/contact/report-abuse) route.
