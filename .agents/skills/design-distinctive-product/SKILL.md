---
name: design-distinctive-product
description: Design or redesign distinctive product interfaces through structured idea exploration, seeded visual variation, native image generation, implementation, screenshot-based independent critique, reduction, and final UI verification. Use for landing pages, web apps, mobile-style interfaces, product prototypes, or existing UI redesigns when Codex should produce a polished implementation rather than generic AI-looking design.
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

## Workflow

### 1. Establish design intent

Inspect the product request, repository instructions, existing UI, technical stack, and brand assets. Capture the product, primary user, primary action, desired feeling, surfaces, constraints, and explicit dislikes.

Ask the user only when a missing choice would materially change the product or design direction. Otherwise make and record a reasonable design assumption.

### 2. Explore ideas

Generate 5-8 brief, meaningfully different design directions. Describe each direction through its central metaphor, intended feeling, interaction character, visual language, product fit, and main risk. Do not reduce directions to color palettes or generic adjectives.

Shortlist 2-3 directions. Ask the user to select when the choice is consequential and they have not delegated end-to-end judgment. Otherwise select one and state why it best fits the product.

### 3. Inject seeded variation

Run `scripts/generate_design_seed.py` once for each concrete variation. Use the random string to inspire layout rhythm, spatial ratios, typography, color relationships, shape language, material, imagery, and motion. Do not expose the string in the interface or let it override usability.

Record the chosen seed so the design decision trail is reproducible.

### 4. Write the design brief

Read `references/design-brief.md` and create a concise brief before implementation. Include explicit anti-patterns to avoid. Keep product requirements separate from visual invention.

### 5. Generate visual assets

Read `references/image-generation.md`. Discover and use the native image-generation capability available in the current environment. Generate at least one purposeful visual exploration, inspect the output, and iterate or edit it when needed before integration.

Never place uninspected generated output into the product. Never expose credentials or introduce an external image provider without explicit user authorization.

### 6. Implement the first complete version

Implement a coherent, runnable interface in the selected stack. Include the primary workflow and relevant loading, empty, error, success, focus, and responsive states. Avoid invented product capabilities and meaningless placeholder content.

Render the result in a real browser and capture screenshots at representative viewport sizes.

### 7. Run independent critique

Read `references/critic-rubric.md`. Give a fresh critic context only the screenshots, design intent, selected direction, and optional reference images. Withhold source code, implementation effort, earlier scores, and the implementer's rationale.

Apply the highest-impact findings, recapture screenshots, and repeat for at most three full critique rounds. Stop earlier when all gates pass. Do not reveal a desired score to the critic.

### 8. Perform the reduction pass

Read `references/reduction-audit.md`. Remove elements that do not support comprehension, action, identity, or feedback. Recheck the interface after removal so restraint does not create missing context or broken composition.

### 9. Verify and deliver

Read `references/delivery-checklist.md`. Run the project's checks and perform browser verification. Report the selected direction, image-generation usage, major critique-driven changes, removed elements, verification evidence, and any unresolved issue.

## Output artifacts

Keep artifacts in the project's existing documentation structure when one exists. Otherwise create a small `design/` working directory only when the artifacts need to persist:

- `design-intent.md`
- `design-brief.md`
- `critique-01.md` through `critique-03.md`
- screenshots and selected generated assets

Do not create persistent process files for a disposable one-off exploration unless the user asks for them.
