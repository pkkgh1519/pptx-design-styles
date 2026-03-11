# 🎨 PPTX Modern Design Styles Skill

> A Claude.ai skill for creating visually stunning presentations — 30 modern design styles included

---

## Overview

This skill enables Claude.ai to apply **30 curated modern design styles** when generating PPTX presentations. Each style includes precise **HEX color values, font pairings, layout rules, and signature elements** so every deck looks intentionally designed.

---

## 🚀 How to Use (사용 방법)

이 섹션에서는 각 AI 플랫폼에서 이 디자인 스킬을 설정하고 사용하는 방법을 안내합니다.

### 1. Claude.ai (Projects)
Claude의 프로젝트 기능을 활용하여 디자인 전문가로 만들 수 있습니다.
- **설치**: 
  1. Claude.ai에서 새로운 **Project**를 생성합니다.
  2. **Project Knowledge**에 `SKILL.md`와 `references/styles.md` 파일을 업로드합니다.
- **사용**: 프로젝트 채팅에서 "PPTX 내용을 구성해줘"라고 요청하면, Claude가 지식 베이스의 스타일 가이드를 바탕으로 30가지 테마 중 최적의 디자인을 적용합니다.

### 2. Gemini Antigravity (Local Skill)
Antigravity 에이전트의 로컬 스킬 시스템에 등록하여 사용합니다.
- **설치**: 
  1. 이 저장소를 로컬의 스킬 디렉토리(`~/.gemini/antigravity/skills/`)로 복사하거나 심볼릭 링크를 생성합니다.
  ```bash
  ln -s $(pwd) ~/.gemini/antigravity/skills/pptx-design-styles
  ```
- **사용**: Antigravity가 자동으로 스킬을 감지하며, "현대적인 느낌의 발표 자료를 만들어줘"와 같은 요청 시 `SKILL.md`의 트리거 조건에 따라 디자인 프로세스가 활성화됩니다.

### 3. Codex (Agent Skill)
Codex 에이전트 환경에서 디자인 가이드라인을 통합합니다.
- **설치**: 
  1. Codex 워크스페이스의 스킬 폴더(`.codex/skills/` 또는 지정된 경로)에 이 프로젝트를 추가합니다.
- **사용**: 에이전트가 코딩 및 문서 작업 중 PPTX 관련 컨텍스트를 감지하면 `SKILL.md`에 정의된 30가지 스타일 규격에 맞춰 슬라이드 구성과 스타일 코드를 생성합니다.

---

## Visual Gallery

Explore a few of the **30 distinct styles** available in this collection.

### ✨ Highlights
<p align="center">
  <img src="assets/images/style_glass.png" width="45%" alt="Glassmorphism">
  <img src="assets/images/style_brutal.png" width="45%" alt="Neo-Brutalism">
</p>
<p align="center">
  <img src="assets/images/style_cyber.png" width="45%" alt="Cyberpunk">
  <img src="assets/images/style_riso.png" width="45%" alt="Risograph">
</p>

### 📱 Full Collection Preview
<p align="center">
  <img src="assets/images/full_preview.png" width="100%" alt="Full Collection Preview">
</p>

---

## 30 Design Styles

| # | Style | Mood | Best For |
|---|-------|------|----------|
| 01 | Glassmorphism | Premium · Tech | SaaS, AI |
| 02 | Neo-Brutalism | Bold · Startup | Pitch decks |
| 03 | Bento Grid | Modular · Structured | Product features |
| 04 | Dark Academia | Scholarly · Refined | Education, research |
| 05 | Gradient Mesh | Artistic · Vibrant | Brand launches |
| 06 | Claymorphism | Friendly · 3D | Apps, education |
| 07 | Swiss International | Functional · Corporate | Consulting, finance |
| 08 | Aurora Neon Glow | Futuristic · AI | AI, cybersecurity |
| 09 | Retro Y2K | Nostalgic · Pop | Events, marketing |
| 10 | Nordic Minimalism | Calm · Natural | Wellness, non-profit |
| 11 | Typographic Bold | Editorial · Impact | Brand statements |
| 12 | Duotone Color Split | Dramatic · Contrast | Strategy decks |
| 13 | Monochrome Minimal | Restrained · Luxury | Luxury brands |
| 14 | Cyberpunk Outline | HUD · Sci-Fi | Gaming, infra |
| 15 | Editorial Magazine | Magazine · Story | Annual reviews |
| 16 | Pastel Soft UI | Soft · App-like | Healthcare, beauty |
| 17 | Dark Neon Miami | Synthwave · 80s | Entertainment |
| 18 | Hand-crafted Organic | Natural · Eco | Eco brands |
| 19 | Isometric 3D Flat | Technical · Structured | IT architecture |
| 20 | Vaporwave | Dreamy · Subculture | Creative agencies |
| 21 | Art Deco Luxe | Gold · Geometric | Luxury, gala events |
| 22 | Brutalist Newspaper | Editorial · Raw | Media, research |
| 23 | Stained Glass Mosaic | Colorful · Artistic | Culture, museums |
| 24 | Liquid Blob Morphing | Fluid · Organic Tech | Biotech, innovation |
| 25 | Memphis Pop Pattern | 80s · Geometric | Fashion, lifestyle |
| 26 | Dark Forest Nature | Mysterious · Atmospheric | Eco premium |
| 27 | Architectural Blueprint | Technical · Precise | Architecture |
| 28 | Maximalist Collage | Energetic · Layered | Advertising, fashion |
| 29 | SciFi Holographic Data | Hologram · HUD | AI, quantum |
| 30 | Risograph Print | CMYK · Indie | Publishing, art |

---

## File Structure

```
pptx-design-styles/
├── SKILL.md              # Skill trigger + recommendation matrix
├── README.md             # This file
├── preview/
│   └── modern-pptx-designs-30.html
└── references/
    └── styles.md         # Full specs: HEX, fonts, layout, signature elements
```

---

## Style Selection Guide

| Goal | Recommended |
|------|-------------|
| Tech / AI / Startup | Glassmorphism, Aurora Neon, Cyberpunk, SciFi Holographic |
| Corporate / Finance | Swiss International, Monochrome, Editorial Magazine |
| Brand / Marketing | Gradient Mesh, Typographic Bold, Duotone Split |
| Product / App / UX | Bento Grid, Claymorphism, Pastel Soft UI |
| Entertainment / Gaming | Retro Y2K, Dark Neon Miami, Vaporwave, Memphis Pop |
| Eco / Wellness | Hand-crafted Organic, Nordic Minimalism, Dark Forest |
| Luxury / Premium | Art Deco Luxe, Monochrome Minimal, Dark Academia |
| Science / Biotech | Liquid Blob, SciFi Holographic, Aurora Neon |

---

## Created By

**TodayCode (오늘코드)** — [YouTube](https://youtube.com/@todaycode) · Python & AI education in Korean

---

## License

MIT License — free to use, modify, and distribute.
