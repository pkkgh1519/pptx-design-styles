# Scenario-Based Image Slot Workflow

Use this reference when a deck should combine a native PPT template with scenario-specific raster visuals generated or selected from prompts. The goal is to make decks feel custom without turning text, labels, diagrams, or controls into uneditable images.

## When to Use

- The user asks for generated illustrations, GPT/image-model visuals, visual-metaphor prompts, image slots, or image-placeholder templates.
- The selected style uses large raster visuals, hero illustrations, abstract AI/process metaphors, or scenario-specific background art.
- A slide needs a custom visual scene that would take too long to build as native PPT shapes, while the message hierarchy remains editable.

## Template Registration 30% Gate

For every PPTX template registration request, measure whether image components are structural enough to require slots.

1. Calculate deck-level image component area ratio:

   ```text
   deck_image_ratio = sum(min(slide_image_area, slide_area)) / (slide_area * slide_count)
   ```

2. Count picture/raster components by visible area, not by object count. Include PNG/JPEG/bitmap pictures, non-editable EMF/WMF/SVG picture shapes, and picture placeholders that carry layout meaning. Use the visible intersection with the slide bounds when possible; ignore fully hidden or fully off-slide items.
3. Cap each slide's counted image area at that slide's full area so overlapping images cannot push the deck above 100%.
4. Report the measured percentage and the most image-heavy slide types or slide numbers before stating the decision.

Decision rule:

- If `deck_image_ratio >= 30%`, automatically define image slots during style registration. Add image structure analysis, repeated placement patterns, slot contracts, and prompt-manifest guidance to the style reference.
- If `deck_image_ratio < 30%`, do not auto-define slots. Tell the user the measured ratio, explain that the style can be registered as native PPT styling only, and define slots only if the user explicitly requests them.
- If the user explicitly asks for image slots, define them regardless of the measured ratio.

## Do Not Use

- Do not use generated images for text-heavy diagrams, tables, legends, captions, security labels, slide numbers, or anything that must remain editable.
- Do not send confidential labels, internal system names, customer data, source code, screenshots, credentials, PII, or security markings into an image-generation prompt.
- Do not rely on generated images for exact architecture, process, or compliance details unless the exact labels and connectors are overlaid as native PPT elements.

## Workflow

1. Read the selected style in `references/styles.md` first.
2. Build the slide plan with native PPT structure: title, message, hierarchy, footer, badges, diagrams, labels, and callouts.
3. Add image slots only where raster visuals improve comprehension or atmosphere.
4. Define a slot contract for every generated/replaceable image.
5. Convert slot contracts into a prompt manifest. Keep prompts sanitized and reusable.
6. Generate or select images with the available image-generation tool/model. If generation is unavailable, create native placeholders and deliver the prompt manifest.
7. Insert images into reserved areas, crop to the declared aspect ratio, and overlay all real text and precise labels as native PPT elements.
8. Render the deck and inspect readability, safe margins, palette fit, and unwanted generated text/logos.

## Slot Contract

Use this compact schema when planning each image slot:

```yaml
image_slot:
  id: hero_visual
  slide_type: cover
  purpose: scenario-specific metaphor
  aspect_ratio: "16:9-safe"
  placement: "right half, behind native title block"
  output_role: "decorative_or_metaphor"
  text_in_image: false
  overlay_native_text: true
  style_tokens:
    palette: ["#00C73C", "#253E93", "#F2F8FE"]
    mood: "clean Korean corporate training"
    motif: "AI workflow, connected nodes, soft blue-green glow"
  prompt_inputs:
    - topic
    - audience
    - metaphor
  forbidden_content:
    - confidential labels
    - company-internal system names
    - real people
    - readable Korean or English text
  fallback:
    - reuse template asset
    - build native PPT icon-card layout
```

Required fields: `id`, `slide_type`, `purpose`, `aspect_ratio`, `placement`, `output_role`, `text_in_image`, `overlay_native_text`, `style_tokens`, `forbidden_content`, and `fallback`.

## Prompt Rules

- Include the slide purpose, visual metaphor, composition, palette, lighting, camera/illustration style, and negative constraints.
- Add `no readable text, no logos, no UI screenshots, no watermarks` unless the user explicitly supplies approved safe source material.
- Keep generated images language-neutral. Add Korean/English wording later as native PPT text.
- Avoid exact model-specific parameters in the skill. Use the currently available image-generation tool/model and record model, size, and date in working notes when relevant.
- Cache generated assets by a stable hash of style name, slot id, sanitized prompt, model, size, and revision. Regenerate only when the scenario or style changes.

## Native Overlay Rules

Always keep these as PPT-native elements:

- Titles, subtitles, body text, bullets, captions, and speaker notes
- Security labels such as `대외비`, `기밀`, `Confidential`
- Company logos, product logos, and brand marks
- Architecture node labels, arrows, step numbers, legends, and data labels
- Tables, charts, compliance mappings, and source references
- Footer, page number, document name, author/team names, and dates

## QA Checklist

- The generated image fits the slot aspect ratio and has safe margins for overlays.
- Native text remains readable at final slide size.
- The image contains no accidental readable text, logo, watermark, PII, customer data, or confidential/security marking.
- The image palette matches the selected style's exact HEX colors closely enough to feel intentional.
- Important meaning is not trapped inside pixels; the slide still works if the image is replaced by a placeholder.
- A rendered slide inspection confirms crop, layering, footer, badges, and contrast.

## Starter Slot Types

General reusable slots:

- `hero_visual`: cover or section opener visual metaphor
- `process_visual`: non-text background for a sequence or workflow
- `concept_metaphor`: abstract scene explaining a theme
- `architecture_backdrop`: safe decorative environment behind native architecture labels
- `role_enablement_visual`: people/process illustration without real faces or labels
- `closing_motif`: simple branded closing image

For `NCP Cloud Security Training`:

- `architecture_context_visual`: sanitized cloud architecture backdrop, native labels overlaid
- `attack_chain_backdrop`: abstract threat-flow visual, no exploit specifics or readable labels
- `security_control_icon_set`: consistent non-branded icon-like visuals for controls
- `mitre_flow_visual`: abstract matrix/flow background, native ATT&CK/D3FEND labels overlaid

For a future `AX Mindset`-style template:

- `hero_ai_orchestration`: AI transformation metaphor for cover slides
- `dx_to_ax_bridge`: transition visual from digital transformation to AI transformation
- `step_process_visual`: scenario-specific process scene behind native step cards
- `learning_curve_visual`: conceptual upskilling curve with native axis/labels
- `role_enablement_visual`: role-based enablement illustration without real people
- `barrier_matrix_visual`: abstract friction/opportunity background for native matrix content
