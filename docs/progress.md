# Progress Log

## Current Baseline

- Branch: `main`
- Harness status: `active`
- Last verified state: `Sprint 07 backend workflow standards verified with ./scripts/check.sh`

## Active Contract

- `docs/contracts/sprint-07-backend-workflow-standards.md`

## Latest Completed Work

- Added source-backed development standards for Python, Java, database design, and frontend development.
- Updated project rules so future Codex sessions read relevant standards before technology-specific work.
- Added scale-based database design guidance to avoid premature architecture.
- Added lightweight reusable module guidance for personal/small projects, with email-first authentication as the default.
- Added UI interaction guidance for list, create, detail, edit, button, feedback, loading, error, and smoothness behavior.
- Added frontend and backend list-query rules requiring bounded pagination, summary list payloads, and separate detail loading.
- Added light/dark display mode guidance for frontend implementation and UI interaction behavior.
- Added backend workflow guidance for lightweight in-process queues, database-backed task state, graceful shutdown, retries, cancellation, and escalation rules.

## Verification Evidence

- `./scripts/check.sh` passed. Output:

```text
[check] repository root: /Users/pengfei.shi/workspace/tmp-project/codex-project-template
[check] done
```

## Known Gaps

- Standards are documentation-only in this sprint; automated enforcement should be added only after a real project selects a stack.
- Java, Python, database, and frontend checks are not yet active because this template does not contain application code for those stacks.
- Reusable module choices still need to be rechecked at implementation time because auth/payment packages change quickly.
- UI interaction guidance is documentation-only; real frontend projects still need browser-based QA for actual screens.
- List-query rules are documentation-only; real projects should add API or integration tests once a backend stack exists.
- Theme mode rules are documentation-only; real projects should verify both modes in browser QA.
- Backend workflow rules are documentation-only; real projects should add worker recovery and shutdown checks once a backend stack exists.

## Recommended Next Steps

1. Add framework-specific workflow examples after the first real backend stack is selected.
2. Consider adding example schemas for `image_generation_tasks`, `image_generation_steps`, and `generated_images` when a real story-image service is implemented.
