# Sprint 06 Contract: Theme Mode Standards

## Goal

Add lightweight standards for light and dark display modes so future frontend and UI work supports theme switching consistently without overbuilding a design system.

## In Scope

- Add frontend implementation guidance for light/dark mode.
- Add UI interaction guidance for theme switching behavior.
- Require readable contrast and semantic color usage across modes.
- Update progress and QA handoff files.

## Out of Scope

- Adding a concrete theme implementation or dependency.
- Defining brand-specific palettes.
- Requiring a full token platform before a real frontend project exists.

## Deliverables

- Updated `docs/standards/frontend.md`.
- Updated `docs/standards/ui-interaction.md`.
- Updated `docs/progress.md`.
- QA report for this documentation sprint.

## Done Means

- Future Codex sessions know where theme implementation rules live.
- Future UI work knows how users should switch and persist display mode.
- Verification has been run through `./scripts/check.sh`.

## Verification

```bash
./scripts/check.sh
```

Manual or QA checks:

- Confirm frontend rules cover semantic tokens, system preference, persistence, and contrast.
- Confirm UI rules cover where the mode switch appears and how it behaves.

## Risks / Notes

- Real projects should adapt the exact theme mechanism to the selected frontend stack.
- Theme support should not justify adding a heavy design system before the project needs one.

## Handoff

- Next likely step: add framework-specific theme implementation examples after a real frontend stack is selected.
