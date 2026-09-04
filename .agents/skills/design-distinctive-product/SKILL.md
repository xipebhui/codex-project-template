---
name: design-distinctive-product
description: Design or redesign distinctive product interfaces through a checkpointed human-in-the-loop workflow covering idea exploration, seeded visual variation, native image generation, implementation, screenshot-based independent critique, reduction, and final UI verification. Use for landing pages, web apps, mobile-style interfaces, product prototypes, or existing UI redesigns when Codex should produce a polished implementation through staged user approvals rather than generic AI-looking design.
---

# Design Distinctive Product

Create a usable, visually distinctive product interface through a fixed explore-build-critique-reduce workflow. Preserve product clarity while pushing beyond familiar AI design defaults.

## Core rules

- Follow the existing project's stack, conventions, and design system when they exist.
- For a new standalone lightweight design prototype with no selected stack, use semantic HTML, CSS, and JavaScript. Do not add a framework only to render a design.
- Build the real product workflow first. Build a marketing landing page only when requested.
- Treat image generation as a required exploration stage, but retain generated assets in the final interface only when they add value.
- Use the current environment's native image-generation capability. Do not assume a particular tool name, vendor, or API.
- Do not silently replace unavailable image generation or independent critique with placeholders, CSS decoration, mocks, or self-review. Report the missing capability and pause.
- Do not add video generation unless the user explicitly requests an expanded workflow.

## Interaction contract

Use checkpointed mode by default.

- Advance at most one checkpoint stage per assistant turn.
- At the end of each stage, present only that stage's compact output, ask for the named approval, and end the turn immediately.
- Do not start the next stage, call its tools, generate its assets, or edit its files in the same turn as the approval request.
- Continue only after a new user message explicitly approves the current checkpoint. Treat `continue` as approval for the current checkpoint only, not the rest of the workflow.
- Incorporate requested changes and present the same checkpoint again when the user does not approve.
- Resume from the last approved checkpoint. Do not restart completed stages.
- Do not write product code before the user explicitly approves the design brief at Checkpoint 3.
- Bypass checkpoints only when the user explicitly requests autonomous or end-to-end execution. Tool permission modes such as auto or always-approve do not count as user approval for design checkpoints.

Label every pause exactly as `Checkpoint N — <name>` so the user can see the current state.

## Workflow

### 1. Establish design intent

Inspect the product request, repository instructions, existing UI, technical stack, and brand assets. Capture the product, primary user, primary action, desired feeling, surfaces, constraints, and explicit dislikes.

Make minor assumptions explicit. Do not ask a long discovery questionnaire.

**Checkpoint 1 — Design intent:** Present the product, primary user, primary action, desired feeling, surfaces, constraints, and assumptions. Ask the user to approve or correct them, then stop.

### 2. Explore ideas

Generate 5-8 brief, meaningfully different design directions. Describe each direction through its central metaphor, intended feeling, interaction character, visual language, product fit, and main risk. Do not reduce directions to color palettes or generic adjectives.

Shortlist 2-3 directions and recommend one without selecting it for the user.

**Checkpoint 2 — Direction selection:** Present the shortlist, recommendation, and tradeoffs. Ask the user to select or combine a direction, then stop. Do not generate a seed yet.

### 3. Inject seeded variation and write the design brief

Run `scripts/generate_design_seed.py` once for each concrete variation. Use the random string to inspire layout rhythm, spatial ratios, typography, color relationships, shape language, material, imagery, and motion. Do not expose the string in the interface or let it override usability.

Record the chosen seed so the design decision trail is reproducible.

Read `references/design-brief.md` and create a concise brief before implementation. Include explicit anti-patterns to avoid. Keep product requirements separate from visual invention.

Define the intended image asset and its job in the interface, but do not generate it yet.

**Checkpoint 3 — Design brief:** Present the seed-derived decisions, concise brief, image-generation plan, and implementation stack. Ask the user to approve the brief and authorize image generation, then stop. Do not generate images or write product code yet.

### 4. Generate visual assets

Read `references/image-generation.md`. Discover and use the native image-generation capability available in the current environment. Generate at least one purposeful visual exploration, inspect the output, and iterate or edit it when needed before integration.

Never place uninspected generated output into the product. Never expose credentials or introduce an external image provider without explicit user authorization.

**Checkpoint 4 — Visual selection:** Present the inspected candidates with a recommendation. Ask the user to select, request revisions, or approve the recommendation, then stop. Do not write product code yet.

### 5. Implement the first complete version

Implement a coherent, runnable interface in the selected stack. Include the primary workflow and relevant loading, empty, error, success, focus, and responsive states. Avoid invented product capabilities and meaningless placeholder content.

Render the result in a real browser and capture screenshots at representative viewport sizes.

**Checkpoint 5 — First implementation:** Present the screenshots, implemented interactions, and checks run. Ask the user to approve the direction or request changes, then stop. Do not begin independent critique yet.

### 6. Run independent critique

Read `references/critic-rubric.md`. Give a fresh critic context only the screenshots, design intent, selected direction, and optional reference images. Withhold source code, implementation effort, earlier scores, and the implementer's rationale.

Present the highest-impact findings and proposed changes before applying them.

**Checkpoint 6 — Critique:** Ask the user to approve or edit the proposed changes, then stop. After approval, apply them, recapture screenshots, and run the critic again. Repeat Checkpoint 6 for at most three full critique rounds. When all gates pass, report that result at Checkpoint 6 and ask permission to proceed to reduction, then stop. Do not reveal a desired score to the critic.

### 7. Perform the reduction pass

Read `references/reduction-audit.md`. Identify elements that do not support comprehension, action, identity, or feedback.

Before removing material elements, present the keep/remove/simplify decisions.

**Checkpoint 7 — Reduction:** Ask the user to approve or edit the reduction decisions, then stop. Apply only the approved decisions on the next turn.

After approval, remove or simplify only the approved elements. Recheck the interface so restraint does not create missing context or broken composition.

### 8. Verify and deliver

Read `references/delivery-checklist.md`. Run the project's checks and perform browser verification. Report the selected direction, image-generation usage, major critique-driven changes, removed elements, verification evidence, and any unresolved issue.

Label the final response `Complete — Delivery`; it is not an approval checkpoint.

## Output artifacts

Keep artifacts in the project's existing documentation structure when one exists. Otherwise create a small `design/` working directory only when the artifacts need to persist:

- `design-intent.md`
- `design-brief.md`
- `critique-01.md` through `critique-03.md`
- screenshots and selected generated assets

Do not create persistent process files for a disposable one-off exploration unless the user asks for them.
