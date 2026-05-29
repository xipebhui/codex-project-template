# Sprint 05 Contract: List Query Standards

## Goal

Add explicit frontend and backend rules for list-page data loading so Codex does not generate full-table fetches, client-side pagination over unbounded data, or list queries that include full detail payloads.

## In Scope

- Add frontend data-fetching rules for list pages.
- Add backend/database query rules for paginated list endpoints.
- Require list responses to use summary payloads and detail views to load details separately.
- Require backend-owned pagination limits and stable ordering.
- Update progress and QA handoff files.

## Out of Scope

- Implementing a specific API framework, ORM, or pagination helper.
- Adding automated static analysis for list query violations.
- Choosing cursor pagination for every project regardless of scale.

## Deliverables

- Updated `docs/standards/frontend.md`.
- Updated `docs/standards/database.md`.
- Updated `docs/progress.md`.
- QA report for this documentation sprint.

## Done Means

- Future Codex sessions have explicit rules against fetching all list data by default.
- List and detail payload boundaries are documented.
- Backend pagination responsibility is documented.
- Verification has been run through `./scripts/check.sh`.

## Verification

```bash
./scripts/check.sh
```

Manual or QA checks:

- Confirm frontend standard forbids unbounded list fetches.
- Confirm backend/database standard requires bounded list queries.
- Confirm detail payloads are separated from list payloads.

## Risks / Notes

- Real implementation should choose offset or cursor pagination based on project scale and query shape.
- A tiny static lookup list can still be loaded all at once only when there is a documented small upper bound.

## Handoff

- Next likely step: add API-specific examples once the first real backend stack is selected.
