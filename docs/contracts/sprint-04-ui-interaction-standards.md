# Sprint 04 Contract: UI Interaction Standards

## Goal

Add a user-centered UI interaction standard for common product workflows so Codex does not invent awkward interaction patterns when building list, create, detail, edit, button, and feedback flows.

## In Scope

- Add an interaction standard focused on modern CRUD and operational product habits.
- Cover list pages, create flows, detail pages, edit flows, buttons, feedback, loading, errors, empty states, destructive actions, and smoothness.
- Reference established interaction baselines such as NN/g heuristics, GOV.UK, Material Design, Apple HIG, WAI-ARIA APG, and WCAG.
- Update project rules so Codex reads the interaction standard before UI workflow design.
- Update project progress and QA handoff.

## Out of Scope

- Creating a visual design system.
- Adding UI components or framework dependencies.
- Replacing the frontend development standard.
- Defining brand-specific visual style.

## Deliverables

- `docs/standards/ui-interaction.md`
- Updated `AGENTS.md`, `docs/spec.md`, README references, and `docs/progress.md`.
- QA report for this documentation sprint.

## Done Means

- Future Codex sessions have concrete rules for list, create, detail, edit, and button behavior.
- The standard distinguishes interaction behavior from frontend implementation details.
- The standard includes smoothness and feedback expectations.
- Verification has been run through `./scripts/check.sh`.

## Verification

```bash
./scripts/check.sh
```

Manual or QA checks:

- Confirm the standard covers list, create, detail, edit, buttons, feedback, and smoothness.
- Confirm the standard references external interaction baselines.
- Confirm AGENTS points to the new standard for UI workflow work.

## Risks / Notes

- The standard should guide default product behavior while leaving room for project-specific interaction needs.
- Visual style should continue to live in product or design-system decisions, not this interaction standard.

## Handoff

- Next likely step: add stack-specific UI recipes once a real frontend stack and component library are selected.
