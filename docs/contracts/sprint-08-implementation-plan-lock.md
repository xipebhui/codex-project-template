# Sprint 08 Contract: Implementation Plan Lock

## Goal

Add a repository-level implementation plan mechanism that locks the global delivery direction before sprint work begins, so Codex does not regenerate incomplete or conflicting plans when switching modes.

## In Scope

- Add `docs/implementation-plan.md` as the global implementation plan template.
- Update project rules so sprint contracts must derive from the implementation plan when it exists.
- Define how to update the implementation plan when reality changes.
- Update spec, README, progress, and QA handoff files.

## Out of Scope

- Creating a real product-specific implementation plan for a concrete app.
- Adding automation that enforces task IDs.
- Changing existing standards content unrelated to planning flow.

## Deliverables

- `docs/implementation-plan.md`
- Updated `AGENTS.md`
- Updated `docs/spec.md`
- Updated README references
- Updated `docs/progress.md`
- QA report for this sprint

## Done Means

- Future Codex sessions know `docs/implementation-plan.md` is the global execution source of truth.
- Sprint contracts must cite implementation plan milestone/task IDs.
- Plan changes require updating the implementation plan before implementation continues.
- Verification has been run through `./scripts/check.sh`.

## Verification

```bash
./scripts/check.sh
```

Manual or QA checks:

- Confirm `AGENTS.md` references the implementation plan in files to read first.
- Confirm operating rules prevent conflicting re-planning.
- Confirm the implementation plan template includes milestones, task queue, execution rules, and change control.

## Risks / Notes

- The template should keep the plan lightweight enough for small projects.
- The implementation plan is a coordination artifact, not a replacement for sprint contracts.

## Handoff

- Next likely step: use `docs/implementation-plan.md` in a real product project and refine the template after one full implementation cycle.
