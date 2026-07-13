# Scenario-Based Image Slot Workflow

Use this reference when a deck combines native PPT structure with scenario-specific raster visuals. Generated assets may support atmosphere or comprehension, but text, exact diagrams, evidence, controls, and brand/security markings stay editable and verifiable.

## Contents

1. [When to Use](#when-to-use)
2. [Image-Area Review Gate](#image-area-review-gate)
3. [Asset Role Classification](#asset-role-classification)
4. [Workflow](#workflow)
5. [Slot Catalog and Instances](#slot-catalog-and-instances)
6. [Executable Manifest](#executable-manifest)
7. [Prompt, Safety, and Brand Rules](#prompt-safety-and-brand-rules)
8. [Model Capabilities and Failure Handling](#model-capabilities-and-failure-handling)
9. [Quantitative QA](#quantitative-qa)

## When to Use

- The user asks for generated illustrations, image-model visuals, visual-metaphor prompts, image slots, or image-placeholder templates.
- The selected style uses large raster visuals, hero illustrations, abstract process metaphors, or scenario-specific background art.
- A custom scene would be costly to build with native shapes, while all meaning-bearing content can remain native.

Do not use generated images for text-heavy diagrams, tables, charts, legends, screenshots used as evidence, security labels, slide numbers, exact architecture/process/compliance details, or brand assets.

## Image-Area Review Gate

For template registration, measure image use as a **review gate**, not an automatic generation condition. A high ratio means the template needs asset-role review and possibly a slot catalog; it never means every image should be regenerated.

Calculate visible image area as the union of clipped visible image polygons on each slide:

```text
slide_visible_image_area = area(union(clip(each_visible_image_polygon, slide_bounds)))
deck_image_ratio = sum(slide_visible_image_area) / sum(slide_area)
```

Measurement rules:

- Use one coordinate system throughout the calculation, preferably EMU; convert only for reporting.
- Apply crop and rotation before clipping to slide bounds. Use geometric union so overlapping pictures are counted once.
- Include PNG/JPEG/bitmap pictures, non-editable EMF/WMF/SVG picture shapes, picture fills, and meaningful picture placeholders.
- Exclude fully hidden/off-slide items and non-rendering placeholders. Report master/background images separately when they repeat across slides.
- Record tool/version, deck hash, slide size, slide ID, source shape ID, role, clipped area, per-slide union area, ratio, exclusions, and rounding precision.
- Report the deck ratio and most image-heavy slides before the review decision.

Decision rule:

- `deck_image_ratio >= 30%`: perform role classification and document recurring placements. Define catalog entries only for recurring replaceable assets.
- `deck_image_ratio < 30%`: native PPT styling is normally sufficient; define slots only when the user requests them or a recurring replaceable asset warrants one.
- User-requested slots still require role classification, safety review, and an explicit conditional instance.

## Asset Role Classification

Classify every candidate before generation:

| Role | Treatment |
|---|---|
| `generative/decorative` | May be generated after sanitization; must not carry essential meaning. |
| `native-rebuild` | Rebuild with PPT shapes/text; do not generate. |
| `preserve/reuse` | Reuse only an approved, licensed source asset with provenance; do not synthesize a replacement by default. |
| `screenshot/evidence` | Preserve the verified source capture and attribution; never fabricate or visually alter evidence. |
| `brand-protected` | Use only an approved brand asset as a native PPT element in `origin_compat_mode`; never generate it. |

Only `generative/decorative` assets may enter image generation. When classification is uncertain, default to `native-rebuild` or a neutral placeholder.

## Workflow

1. Read the selected style in `references/styles.md`.
2. Build the native slide plan first: title, message, hierarchy, footer, badges, diagrams, labels, data, and callouts.
3. Measure template image area when registering a template, then classify candidate assets.
4. Define reusable entries in the slot catalog; instantiate only the slots needed by the actual slide plan.
5. Create and validate a sanitized prompt manifest for each `generative/decorative` instance.
6. Check model capabilities, generate once, and run slot-level QA. Retry once only for a correctable generation/QA failure.
7. Embed approved assets, apply the declared fit/focal point, and keep all real text and precise labels native.
8. Render the deck and inspect crop, layering, contrast, badges, footer, and fallback output.

If generation is unavailable or blocked, use the declared native fallback and retain the prompt manifest. Never block deck delivery on a decorative asset.

## Slot Catalog and Instances

A catalog describes reusable possibilities; it does not require every new deck to use every slot. The slide plan creates conditional instances only when the relevant slide and content exist.

Catalog entries define: stable catalog ID, eligible slide types, purpose, role, style tokens, allowed content, forbidden content, and native fallback. Instance IDs must be unique deck-wide and stable across revisions, for example `s01.hero_ai_orchestration`.

Every instance must identify its slide and exact placement. Use either EMU, inches, or normalized slide fractions; do not mix units inside one bounds object. `aspect_ratio` is the physical slot width divided by height, not a phrase such as “wide row.”

## Executable Manifest

```yaml
manifest_version: 1
style_id: ai-transformation-playbook
mode: public_default
deck:
  sha256: "<deck-sha256>"
  slide_size: {width: 10, height: 7.5, unit: in}
slots:
  - id: s01.hero_ai_orchestration
    catalog_slot_id: hero_ai_orchestration
    slide_id: 1
    slide_type: cover
    role: generative/decorative
    purpose: abstract AI-enabled work orchestration atmosphere
    bounds: {x: 5.10, y: 0.70, w: 4.30, h: 4.30, unit: in}
    aspect_ratio: "1:1"
    fit: cover
    focal_point: {x: 0.65, y: 0.50, unit: fraction}
    z_order:
      above: [background]
      below: [title, author, footer, security_badge]
    safe_overlay_regions: []
    prompt:
      template_id: style36.hero.v1
      positive: "Clean corporate AI enablement illustration; abstract workflow nodes; white, signal green, deep blue, and pale-blue palette; generous whitespace."
      negative: "no readable text, no logos, no people, no UI screenshots, no watermarks, no confidential or customer data"
      sanitized_inputs:
        topic: AI-enabled work orchestration
        audience: corporate learners
        metaphor: connected abstract workflow nodes
      sanitization:
        ruleset: image-prompt-v1
        status: passed
        prohibited_matches: []
    generation:
      provider: "<record-actual-provider>"
      model: "<record-actual-model>"
      model_version: "<record-when-available>"
      size_px: {width: 1536, height: 1536}
      seed: null
      reproducibility: approved_asset_hash
      capability_check:
        aspect_ratio: passed
        requested_size: passed
        reference_images: not_used
        transparency: not_required
    output:
      path: assets/generated/s01.hero_ai_orchestration.png
      sha256: "<asset-sha256>"
      mime: image/png
      embedded: true
    fallback:
      on: [tool_unavailable, policy_block, capability_mismatch, generation_error, qa_fail]
      action: native_ai_tile
    qa:
      status: passed
      render_path: renders/slide-01.png
    status: embedded
    attempts: 1
```

For models without deterministic seeds, preserve the approved output path and SHA-256; do not claim prompt-only reproducibility. A cache key must include style ID, instance ID, manifest/template revision, sanitized prompt, model and version, size, seed when supported, and reference-asset hashes.

## Prompt, Safety, and Brand Rules

- Include purpose, metaphor, composition, palette, lighting/illustration style, whitespace, and negative constraints.
- Keep prompts language-neutral and use sanitized, generic concepts only. Never send confidential labels, internal system/team/customer names, source code, credentials, PII, screenshots, unpublished data, or security markings.
- Add all Korean/English wording later as native PPT text. Generated output must contain no readable text, logos, UI screenshots, or watermarks.
- Keep titles, captions, notes, security labels, logos, architecture labels/connectors, charts, tables, references, footer, page number, author/team, and dates native.
- Public default mode must use neutral styling and omit copied company/product marks. `origin_compat_mode` is allowed only when the user explicitly requests faithful reproduction and supplies or identifies approved source assets. Record approval/provenance; brand assets remain native and are never prompt inputs.

## Model Capabilities and Failure Handling

Before generation, verify requested aspect ratio/size, crop tolerance, seed support, transparency need, reference-image policy, and applicable content-policy limits. Adapt the output size or use fallback rather than silently changing slot geometry.

State flow:

```text
planned -> classified -> sanitized -> generated -> qa_passed -> embedded
                       \-> fallback
generated -> qa_failed -> retry_once -> qa_passed | fallback
```

- Do not retry policy or safety blocks.
- Retry at most once for a correctable generation or QA failure, recording both attempts.
- `preserve/reuse`, `screenshot/evidence`, and `brand-protected` assets require provenance and approval rather than generation.
- A fallback must preserve slide meaning and layout without the image.

## Quantitative QA

- Instance IDs are unique; every instance resolves to one existing slide and one catalog entry.
- Bounds and rendered aspect-ratio error are at most 1%; crop retains the declared focal point and does not enter protected overlay regions.
- Effective embedded resolution at placed size is at least 150 PPI; linked external images: 0.
- Generated readable text, logos, watermarks, PII, customer data, confidential/security markings: 0.
- Native text remains readable at final slide size; text/image collisions and unintended occlusion: 0.
- Meaning-bearing labels, lines, axes, cells, arrows, data, and evidence remain native or preserved, never generated.
- Output path and SHA-256 match the embedded asset; model/version/size and seed-or-approved-hash are recorded.
- A final rendered-slide inspection confirms palette, contrast, crop, layering, footer, badges, and the native fallback. Record pass/fail per instance and keep the render path as evidence.

## Starter Catalog

- `hero_visual` — `generative/decorative`; cover or section-opener atmosphere.
- `concept_metaphor` — `generative/decorative`; abstract, non-text visual metaphor.
- `architecture_backdrop` — normally `native-rebuild`; decorative generation only when it contains no topology or evidence.
- `process_visual`, `learning_curve_visual`, `role_enablement_visual`, `barrier_matrix_visual` — `native-rebuild` unless an approved source asset is explicitly preserved.
- `architecture_screenshot`, `attack_chain_evidence` — `screenshot/evidence`.
- `company_logo`, `security_badge` — `brand-protected` and native-only in `origin_compat_mode`.
