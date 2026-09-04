# codex-project-template

[中文](README.zh-CN.md) | [English](README.en.md)

A minimal repository template for building a development harness for Codex-driven coding.

一个用于构建 Codex 开发 harness 的最小仓库模板。

## Quick Links

- [中文说明](README.zh-CN.md)
- [English Guide](README.en.md)
- [Implementation Plan](docs/implementation-plan.md)
- [Development Standards](docs/standards/)
- [Reference: Harness design: Building long-running applications with LLMs](docs/references/harness-design-long-running-apps.md)
- [Skill: Distinctive Product Design](.agents/skills/design-distinctive-product/SKILL.md)

## Distinctive Product Design Skill

`design-distinctive-product` turns a product request into a distinctive, usable interface through this workflow:

```text
Design intent → Idea exploration → Seeded variation → Design brief
→ Native image generation → Implementation → Screenshot critique
→ Reduction pass → Delivery verification
```

It follows an existing frontend stack. For a standalone lightweight prototype with no selected stack, it uses semantic HTML, CSS, and JavaScript. Image generation uses the current agent environment's native capability; video generation is intentionally out of scope.

Install for the current project:

```bash
npx skills add https://github.com/xipebhui/codex-project-template/tree/main/.agents/skills/design-distinctive-product --agent codex --yes
```

Install globally for the current user:

```bash
npx skills add https://github.com/xipebhui/codex-project-template/tree/main/.agents/skills/design-distinctive-product --global --agent codex --yes
```

If this repository is already the current project, no installation is needed: Codex discovers the Skill directly under `.agents/skills/`.
