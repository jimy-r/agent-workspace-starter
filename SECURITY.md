# Security policy

## Supported versions

This is a template repository. There's no running service and no version to track. Each fork or "Use this template" copy becomes its own independent workspace from the moment it's created, and a fix made here only reaches copies made afterward.

## What to report, and where

### 1. A pattern here that would weaken a copy's security

An unsafe hook configuration, a credential-handling gap, a permissive default in `.claude/settings.json`. Use GitHub's [private security advisories](https://github.com/jimy-r/agent-workspace-starter/security/advisories/new) so the fix lands before it propagates into someone's fork.

### 2. Privacy leaks in committed content

Open a public Issue. The content is already public, so speed matters more than privacy here. Do not include the leaked content in the report; link to the file and line.

## Out of scope

- Vulnerabilities in **Claude Code itself**: report to [anthropics/claude-code](https://github.com/anthropics/claude-code).
- Issues in your own fork after you've customised it — that's your workspace to secure from there.

## Maintainer response

Private security advisories get a first response within a week. If you don't hear back in two weeks, open a new private advisory as a ping.

---

*Last verified against the repo structure on **2026-08-28**.*
