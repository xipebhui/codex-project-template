# Sprint 09 Contract: Distinctive Product Design Skill

## Implementation-plan link

- Milestone: `M5 Reusable Skills`
- Task: `M5-T01`

## Goal

Add a remotely installable Skill that guides compatible coding agents from product-design ideation through seeded variation, native image generation, implementation, independent screenshot critique, reduction, and verification.

## In scope

- Add `design-distinctive-product` under `.agents/skills/`.
- Keep image generation provider-neutral and require the current environment's native capability.
- Follow an existing frontend stack; default new lightweight prototypes to semantic HTML, CSS, and JavaScript.
- Include a design-seed generator and concise workflow references.
- Document the GitHub installation source.
- Validate the Skill and repository.

## Out of scope

- Video generation and video APIs.
- External image-provider configuration.
- A fixed React, Vue, or other framework template.
- Publishing the repository or installing the Skill into a remote environment.

## Done means

- The Skill passes the standard Skill validator.
- The seed generator runs and rejects undersized seeds.
- The workflow defines explicit ideation, image generation, critique, reduction, and delivery gates.
- No required capability is silently replaced with a fallback.
- `./scripts/check.sh` passes.

## Verification

```bash
python3 /Users/pengfei.shi/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/design-distinctive-product
python3 .agents/skills/design-distinctive-product/scripts/generate_design_seed.py
./scripts/check.sh
```
