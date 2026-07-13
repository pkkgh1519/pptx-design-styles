---
name: pptx-design-styles
description: >
  Create distinctive, production-grade PPTX slide decks using 36 modern design styles, including
  Glassmorphism, Neo-Brutalism, Bento Grid, Workshop Playbook, Terminal Workshop,
  클라우드 보안 브리핑, AI 전환 플레이북, and more. Use for presentations, pitch decks,
  workshop guides, onboarding decks, tutorial slides, visually striking PPTX decks, scenario-based image slots,
  GPT image-assisted slide assets, visual-metaphor prompts, image-placeholder templates, and PPTX 템플릿 등록.
  When registering or updating reusable PPTX templates, measure deck-level visible image area and apply the 30% asset-role review gate.
  Also activate when a presentation/PPTX/slide/deck request mentions NCP, 클라우드 보안, AX,
  AI Transformation, 대외비, 기밀, or Korean corporate/security reporting. Do not activate from
  AX, NCP, NAVER, 대외비, or 기밀 alone without presentation context.
---

# PPTX Modern Design Styles Skill

## How to Use

1. Identify the style the user wants, or recommend a style based on the content/audience
2. Read the detailed spec for that style in `references/styles.md`
3. Apply alongside the core pptx skill to build the slide deck
4. For `Workshop Playbook`, inspect `assets/templates/workshop-playbook-template.pptx` with the core pptx skill when the user wants the same pacing, step badges, and guide-style layout rhythm
5. For `Workshop Playbook (Dark)`, same workflow as Workshop Playbook but apply the dark navy color mapping from Style 33 — structure is identical, only the surface/text/tint colors change
6. For `Terminal Workshop (Dark)`, inspect `assets/templates/terminal-workshop-template.pptx` with the core pptx skill when the user wants coding workshop / vibe-coding training style with terminal-green accent and monospace titles
7. For `클라우드 보안 브리핑`, inspect `assets/templates/ncp-cloud-security-training-template.pptx` with the core pptx skill when the user wants Korean cloud security education, NCP architecture analysis, MITRE ATT&CK/D3FEND mapping, or report-like security training slides. Follow the 16:9 white canvas, NanumSquare font system, green accents (`#00C73C`, `#009F0F`, `#07C63C`), thin report frame, green rounded banners, numbered green callouts, and screenshot-first architecture walkthroughs.
8. For `AI 전환 플레이북`, inspect `assets/templates/ax-mindset-enablement-template.pptx` with the core pptx skill when the user wants Korean AX/AI transformation mindset education, enablement programs, role-based training paths, or image-slot-driven corporate learning decks. Follow the 4:3 white canvas, NanumSquare font system, green (`#00C73C`, `#07C63C`) plus deep blue (`#253E93`), rounded blue-green cards, icon-led process rows, and scenario-based image slots.
9. For Styles 35 and 36, public mode is the default: omit branding and identifiers copied from the source template, including source logos, default `대외비`, original author/team text, and source-company footers. A company or product name explicitly supplied as the presentation subject may remain as native text when relevant and authorized. Use origin compatibility mode only when the user explicitly requests source-faithful branding or classification and confirms they are authorized to use it.
10. When registering a PPTX template as a new or reusable style, measure deck-level visible image area using clipped image polygons and per-slide geometric union. If the ratio is **30% or higher**, read `references/image-slot-workflow.md`, classify every candidate asset, and define conditional slots only for recurring replaceable assets. The ratio triggers review, never automatic image generation. If the ratio is **below 30%**, report it and register native styling unless the user requests slots or a recurring replaceable asset warrants one.
11. For scenario-based image slots, read `references/image-slot-workflow.md` before deck planning when the user asks for generated illustrations, GPT/image-model visuals, custom visual metaphors, or image placeholders. Define native PPT text/layout first, then image slot contracts; use generated images only for backgrounds, illustrations, metaphors, or non-text visual structure. If image generation is unavailable, emit the prompt manifest and native placeholders instead of blocking the deck.
12. After adding, removing, renaming, or renumbering template-backed styles, update the single preview file `preview/modern-pptx-designs.html` as part of the same task. Update the style count, remove stale cards/CSS, add cards for new styles, and verify README/README_ko preview links and file-tree entries point to this file. Do not create numbered preview filenames unless the user explicitly asks.

> **Always** read `references/styles.md` before starting.  
> If the user hasn't chosen a style, use the recommendation matrix below.

---


## Style Naming Standards

- Name styles by **visual mood, generic use, and design metaphor**, not by source file, client, company, or department name.
- Use natural, locale-appropriate public names while keeping established design terms stable. Generic domains such as cloud security or AI transformation may appear when they improve selection.
- Keep company/product names and classification labels such as NCP, NAVER, or `대외비` in triggers and template-origin notes only; do not use them as the public style name.
- Good pattern: `<visual metaphor/material> + <generic use/format>`; avoid raw names like `Company Report Template`.

### Style Identity and Compatibility

- Each template-backed identity record uses an immutable `style_id`; `display_name` is the canonical public name used in lists and recommendations.
- `aliases` accept earlier or alternate names but are never presented as current names.
- `origin_compat_mode` is opt-in and follows the authorization rule in step 9.
- `cloud-security-briefing`: display `클라우드 보안 브리핑`; deprecated alias `녹빛 클라우드 감시자`; native ratio **16:9**.
- `ai-transformation-playbook`: display `AI 전환 플레이북`; deprecated alias `인지 궤도 플레이북`; native ratio **4:3**.

---

## Style Recommendation Matrix

| Presentation Goal | Recommended Styles |
|-------------------|--------------------|
| Tech / AI / Startup | Glassmorphism, Aurora Neon Glow, Cyberpunk Outline, SciFi Holographic Data, Dark Command Dashboard, Workshop Playbook (Dark), Terminal Workshop (Dark) |
| Corporate / Consulting / Finance | Swiss International, Monochrome Minimal, Editorial Magazine, Architectural Blueprint |
| Education / Research / History | Dark Academia, Nordic Minimalism, Brutalist Newspaper |
| Training / Workshop / Onboarding | Workshop Playbook, Workshop Playbook (Dark), Terminal Workshop (Dark), 클라우드 보안 브리핑, AI 전환 플레이북, Swiss International, Bento Grid, Nordic Minimalism |
| AI Transformation / Enablement | AI 전환 플레이북, Workshop Playbook, Bento Grid, Swiss International |
| Korean Corporate / Security Report | 클라우드 보안 브리핑, Swiss International, Monochrome Minimal |
| Brand / Marketing | Gradient Mesh, Typographic Bold, Duotone Color Split, Risograph Print |
| Product / App / UX | Bento Grid, Claymorphism, Pastel Soft UI, Liquid Blob Morphing |
| Entertainment / Gaming | Retro Y2K, Dark Neon Miami, Vaporwave, Memphis Pop Pattern |
| Eco / Wellness / Culture | Hand-crafted Organic, Nordic Minimalism, Dark Forest Nature |
| IT Infrastructure / Architecture | 클라우드 보안 브리핑, Isometric 3D Flat, Cyberpunk Outline, Architectural Blueprint |
| Portfolio / Art / Creative | Monochrome Minimal, Editorial Magazine, Risograph Print, Maximalist Collage |
| Pitch Deck / Strategy | Neo-Brutalism, Duotone Color Split, Bento Grid, Art Deco Luxe, Dark Command Dashboard |
| Luxury / Events / Gala | Art Deco Luxe, Monochrome Minimal, Dark Academia |
| Science / Biotech / Innovation | Liquid Blob Morphing, SciFi Holographic Data, Aurora Neon Glow |

---

## Full Style List

| # | Style Name | Mood | Best For |
|---|------------|------|----------|
| 01 | Glassmorphism | Premium · Tech | SaaS, AI products |
| 02 | Neo-Brutalism | Bold · Startup | Pitch decks, marketing |
| 03 | Bento Grid | Modular · Structured | Feature overviews |
| 04 | Dark Academia | Scholarly · Refined | Education, research |
| 05 | Gradient Mesh | Artistic · Vibrant | Brand launches |
| 06 | Claymorphism | Friendly · 3D | Apps, education |
| 07 | Swiss International | Functional · Corporate | Consulting, finance IR |
| 08 | Aurora Neon Glow | Futuristic · AI | AI, cybersecurity |
| 09 | Retro Y2K | Nostalgic · Pop | Events, marketing |
| 10 | Nordic Minimalism | Calm · Natural | Wellness, non-profit |
| 11 | Typographic Bold | Editorial · Impact | Brand statements |
| 12 | Duotone Color Split | Dramatic · Contrast | Strategy, compare |
| 13 | Monochrome Minimal | Restrained · Luxury | Luxury brands |
| 14 | Cyberpunk Outline | HUD · Sci-Fi | Gaming, infra |
| 15 | Editorial Magazine | Magazine · Story | Annual reviews |
| 16 | Pastel Soft UI | Soft · App-like | Healthcare, beauty |
| 17 | Dark Neon Miami | Synthwave · 80s | Entertainment, music |
| 18 | Hand-crafted Organic | Natural · Eco | Eco brands, food |
| 19 | Isometric 3D Flat | Technical · Structured | IT architecture |
| 20 | Vaporwave | Dreamy · Subculture | Creative agencies |
| 21 | Art Deco Luxe | Gold · Geometric | Luxury, gala events |
| 22 | Brutalist Newspaper | Editorial · Raw | Media, research |
| 23 | Stained Glass Mosaic | Colorful · Artistic | Culture, museums |
| 24 | Liquid Blob Morphing | Fluid · Organic Tech | Biotech, innovation |
| 25 | Memphis Pop Pattern | 80s · Geometric | Fashion, lifestyle |
| 26 | Dark Forest Nature | Mysterious · Atmospheric | Eco premium, adventure |
| 27 | Architectural Blueprint | Technical · Precise | Architecture, planning |
| 28 | Maximalist Collage | Energetic · Layered | Advertising, fashion |
| 29 | SciFi Holographic Data | Hologram · HUD | AI, quantum, defense |
| 30 | Risograph Print | CMYK · Indie | Publishing, art, music |
| 31 | Workshop Playbook | Clear · Trust-building | Workshops, onboarding, tutorials |
| 32 | Dark Command Dashboard | Commanding · Dark-UI | Developer pitches, AI/SaaS overviews |
| 33 | Workshop Playbook (Dark) | Dark · Guided · Trust | Dark workshops, dev onboarding, coding playbooks |
| 34 | Terminal Workshop (Dark) | Hacker · Terminal · Code | Coding workshops, vibe-coding training, dev education |
| 35 | 클라우드 보안 브리핑 | 명료함 · 클라우드 보안 · 교육형 | 16:9 native; cloud security education, architecture walkthroughs, MITRE/D3FEND analysis |
| 36 | AI 전환 플레이북 | 명료함 · AI 전환 · 확산형 | 4:3 native; AI adoption programs, role-based training, generated-image slot decks |

---

## Core Production Principles

- **Always use together with the pptx skill** for actual file generation
- **Strictly follow** each style's background, font, and layout specifications
- Every slide must contain **at least one visual element** (shape, icon, color block)
- **Never use text-only slides** — express design through color, form, and space
- Repeat each style's **signature element** consistently across all slides
- Match **font pairing** exactly as specified — typography drives 50% of the style impression
- Use **exact HEX values** from `references/styles.md` — approximate colors break the aesthetic
- For generated image slots, keep all real text, labels, logos, badges, slide numbers, legends, captions, and security markings as native PPT elements
- Do not include confidential labels, internal system names, real customer data, PII, or security markings in image-generation prompts; sanitize or abstract them before generating assets
- For template registration, use clipped visible-image polygon union, not picture count or summed picture area, for the 30% asset-role review gate

For detailed color, font, and layout specs per style → **[references/styles.md](references/styles.md)**
