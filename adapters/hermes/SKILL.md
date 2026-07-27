---
name: app-builder
description: Run an APP_Builder project — plan it, execute it unit by unit, review it, and iterate. Use when working inside a repository governed by APP_Builder's AGENTS.md, when starting or resuming a project session, when a Deliverable Unit needs to be produced or reviewed, or when the user asks to bootstrap, plan, build, review, or iterate on a digital asset.
---

# APP_Builder — Hermes adapter

**Governance is not here.** It lives in `AGENTS.md` at the repository root — the single, platform-neutral source. Hermes auto-injects `AGENTS.md` from the working directory, so it is already loaded before this skill runs. Read it and follow it. This file only exposes the command surface; it never restates a rule.

> Unlike the Claude Code adapter, this one carries no governance pointer. `CLAUDE.md` exists because Claude Code auto-loads that filename; Hermes loads `AGENTS.md` natively and needs no redirect. What Hermes lacks is a slash-command surface — that is what this skill provides.

## The six playbooks

Neutral procedures in `commands/`. Read the one that applies, when it applies. Do not preload them all: each is read when its moment arrives.

| Playbook | When to read it |
|---|---|
| `commands/bootstrap.md` | First contact with the repo. One-time platform check |
| `commands/init-project.md` | A new project starts. Produces the plan that Rule 1 requires |
| `commands/session-start.md` | Every new session, without exception. Establishes the resumption point |
| `commands/start-execution.md` | The plan is approved and a unit is about to be produced |
| `commands/review.md` | A unit is finished and needs its quality gate |
| `commands/iterate.md` | Review found something, or the user asks for changes |

## How a session runs

1. **`session-start` first.** Always. Before producing anything, before reading design docs. It tells you where the work stopped.
2. **No deliverable before the plan is approved** — Rule 1, the Planning Gate. If no approved plan exists, run `init-project` and stop at the gate.
3. **Produce one unit at a time**, following `start-execution` and the active Asset Profile.
4. **Every unit passes `review`** before it counts as done. Completeness is defined by the active profile, not by your judgement.
5. **Update `task_tracker` and `work_log` after each unit; `project_memory` at end of session.** Rule 6 says now, not later and not in batches.

## Hermes-specific mechanics

These are platform mechanics, not governance. They exist here because this is the platform layer.

- **Delegating a unit or a review.** `delegate_task` subagents know nothing of the conversation: put the full unit spec, file paths, and the active profile's quality gate into `goal` and `context`. Leaf subagents cannot use `clarify`, `memory` or `execute_code` — a stuck subagent will not ask, it will guess. Specify completely or do not delegate.
- **A reviewer must not be the builder.** If a subagent produced the unit, a different one reviews it. Subagent summaries are self-reports: ask for verifiable handles — file paths, line numbers, the exact fragment that supports each finding — and check at least one before accepting a verdict.
- **Delegation is not durable.** If the parent session closes before a child returns, the work is discarded silently. Wait for the verdict; a review that never returned is not a pass.
- **Model per invocation, not per task.** `-m MODEL` applies to the whole invocation and subagents inherit the parent's model. Route by cost with separate invocations, not with delegation.
- **`--usage-file PATH`** writes cost, tokens, model and API calls after a run, even on failure. Use it when a project needs per-project cost accounting.

## What not to do

- **Never restate governance here.** If a rule needs changing, it changes in `AGENTS.md`. This file and the core must never disagree, and the way to guarantee that is to keep the rules in one place.
- **Do not copy the playbooks into this skill.** Read them from `commands/` at the moment of use. Two copies drift.
- **Do not name commercial products** where the core names categories — Rule 7. "LLM provider", not a brand.
- **Do not add scope** because it seems useful. Rule 4: stop and ask.
