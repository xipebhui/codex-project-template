# Sprint 07 Contract: Backend Workflow Standards

## Goal

Add lightweight backend workflow standards for background tasks, queues, graceful shutdown, and persisted task state, with database design guidance that avoids overbuilding for small projects.

## In Scope

- Add a backend workflow standard.
- Define small, medium, and heavy workflow levels.
- Make in-process memory queues plus database state the default for small tasks.
- Require explanation before upgrading to medium workflow infrastructure.
- Update database design guidance for workflow state tables.
- Update project rules, spec, progress, and QA handoff.

## Out of Scope

- Adding a concrete queue, worker, or workflow engine dependency.
- Implementing Temporal, BullMQ, Celery, or any other runtime.
- Designing a universal workflow engine.
- Adding automated tests for workflow behavior before a real backend exists.

## Deliverables

- `docs/standards/backend-workflows.md`
- Updated `docs/standards/database.md`
- Updated `AGENTS.md`, `docs/spec.md`, README references, and `docs/progress.md`
- QA report for this sprint

## Done Means

- Future Codex sessions default to lightweight workflow design for small tasks.
- Future Codex sessions know when they must explain medium workflow needs to the user.
- Database state requirements for workflow tasks are documented.
- Verification has been run through `./scripts/check.sh`.

## Verification

```bash
./scripts/check.sh
```

Manual or QA checks:

- Confirm small workflow default uses memory queue plus database state.
- Confirm independent worker services are not required for small tasks by default.
- Confirm medium workflow upgrades require explanation and user confirmation.

## Risks / Notes

- Real implementation still depends on the selected backend framework and deployment model.
- In-memory queues are not durable; database state must be the source of truth.

## Handoff

- Next likely step: add framework-specific examples after the first real backend stack is selected.
