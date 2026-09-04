# Native image generation

## Capability contract

1. Discover the image-generation capability exposed by the current agent environment.
2. Use the native capability without assuming a Codex, Grok, Gemini, or other vendor-specific tool name.
3. If several native capabilities exist, choose the one best suited to the required asset and state the choice.
4. If no image-generation capability exists, report the missing requirement and pause. Do not silently substitute stock imagery, placeholders, CSS decoration, or an external API.

## Asset workflow

1. Define the asset's job in the product before prompting.
2. Generate a small coherent set of candidates.
3. Inspect composition, artifacts, legibility, crop safety, background treatment, and consistency.
4. Edit or regenerate weak output.
5. Integrate the selected asset at its actual display size.
6. Verify desktop and mobile crops, contrast with surrounding UI, loading behavior, and file weight.

Generated imagery may be removed during the reduction pass when it does not improve comprehension, identity, or emotional effect. Exploration is required; final inclusion is evidence-based.
