# Implementation Plan

## Purpose

This file is the global delivery plan for a project that uses this template. It exists to lock product direction, architecture decisions, implementation sequence, and acceptance expectations before sprint execution begins.

When this file is present and marked `locked`, Codex must not replace it with a new plan in chat or Plan mode. Sprint contracts should take the next unfinished slice from this file.

## Planning Status

- Status: `draft`
- Last updated: `2026-09-04`
- Product target: `codex-project-template`
- Current milestone: `M5`
- Current task: `M5-T01`

Status values:

- `draft`: still being discussed; implementation should not start unless the user explicitly asks for a prototype or spike.
- `locked`: approved as the global execution plan; sprint contracts must derive from this plan.
- `needs-update`: implementation revealed a conflict; update this file before continuing.

## Source Documents

List the documents that this plan is based on.

- Product spec: `docs/spec.md`
- Standards:
  - `docs/standards/python.md`
  - `docs/standards/java.md`
  - `docs/standards/database.md`
  - `docs/standards/backend-workflows.md`
  - `docs/standards/frontend.md`
  - `docs/standards/ui-interaction.md`
  - `docs/standards/reusable-modules.md`
- Design notes: `<path>`
- API notes: `<path>`
- User decisions: `<path or summary>`

## Non-Negotiable Decisions

Record decisions that should not be re-planned during implementation.

### Product Scope

- `<decision>`

### UI And Interaction

- `<decision>`

### Architecture

- `<decision>`

### Data And Persistence

- `<decision>`

### Background Workflows

- `<decision>`

### Auth And Reusable Modules

- `<decision>`

### Out Of Scope

- `<explicit non-goal>`

## Delivery Strategy

Use a hybrid strategy by default:

1. Build enough product shell and UI to validate the full experience.
2. Implement one core vertical slice end to end.
3. Complete modules incrementally after the core slice proves the architecture and interaction model.
4. Harden with QA, edge states, recovery behavior, and production checks.

Avoid pure horizontal delivery unless the user only needs a visual prototype. Avoid pure module-by-module delivery until the core product loop has been proven.

## Milestones

### M1 Product Shell And UI Flow

Goal:

- `<what should be visible and reviewable>`

Deliverables:

- `<deliverable>`

Acceptance:

- `<observable acceptance condition>`

### M2 Core Vertical Slice

Goal:

- `<end-to-end workflow to prove first>`

Deliverables:

- `<deliverable>`

Acceptance:

- `<observable acceptance condition>`

### M3 Module Completion

Goal:

- `<modules to complete after the core slice>`

Deliverables:

- `<deliverable>`

Acceptance:

- `<observable acceptance condition>`

### M4 Reliability And QA Hardening

Goal:

- `<checks, recovery, performance, accessibility, and workflow hardening>`

Deliverables:

- `<deliverable>`

Acceptance:

- `<observable acceptance condition>`

### M5 Reusable Skills

Goal:

- Add small, installable Skills after a workflow proves reusable.

Deliverables:

- A provider-neutral product-design Skill with native image generation and visual QA.

Acceptance:

- The Skill passes validation, its deterministic utilities are tested, and repository checks pass.

## Task Queue

Each task should be small enough to become one sprint contract or part of one sprint contract.

| ID | Milestone | Status | Task | Depends On | Verification |
| --- | --- | --- | --- | --- | --- |
| M1-T01 | M1 | `todo` | `<task>` | `<none>` | `<check>` |
| M1-T02 | M1 | `todo` | `<task>` | `M1-T01` | `<check>` |
| M2-T01 | M2 | `todo` | `<task>` | `M1-T02` | `<check>` |
| M5-T01 | M5 | `done` | Add the distinctive product-design Skill | `none` | Skill validation, seed script test, and `./scripts/check.sh` |

Status values:

- `todo`
- `in-progress`
- `blocked`
- `done`
- `deferred`

## Execution Rules

1. Do not skip ahead unless dependencies are marked done or the user explicitly changes the plan.
2. Do not create a sprint contract that conflicts with this file.
3. Every sprint contract must cite the milestone and task ID it implements.
4. If implementation reveals missing requirements, architecture conflict, or scope mismatch, mark this plan `needs-update` and update it before continuing.
5. Do not introduce new frameworks, services, data models, or workflow infrastructure unless they fit the non-negotiable decisions or this file is updated.
6. Keep sprint changes small and reviewable.
7. Update this file when a task is started, completed, blocked, or deferred.
8. Keep `docs/progress.md` aligned with the current milestone and task.

## Change Control

When the plan changes, record:

- Date
- Reason
- Changed sections
- Impact on existing sprint contracts
- Verification or QA implications

### Change Log

| Date | Change | Reason | Impact |
| --- | --- | --- | --- |
| `<YYYY-MM-DD>` | `<change>` | `<reason>` | `<impact>` |
| `2026-09-04` | Added M5 and completed M5-T01 | Package the validated AI product-design workflow as an installable Skill | Adds a reusable design workflow without changing application architecture |

## QA Strategy

Define how the project will be checked across milestones.

- Automated checks: `./scripts/check.sh`
- Manual UI checks: `<screens or flows>`
- Data checks: `<database/API checks>`
- Workflow checks: `<background task checks>`
- Accessibility checks: `<keyboard/focus/contrast checks>`

## Open Questions

- `<question>`

## Handoff

- Next milestone: `<milestone id>`
- Next task: `<task id>`
- Known blockers: `<blocker or none>`
