#!/usr/bin/env python3
"""Validate that the style registry, reference headings, and preview stay aligned."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNT = 36
IDENTITY_CONTRACTS = (
    (35, "cloud-security-briefing", "클라우드 보안 브리핑", "녹빛 클라우드 감시자", "16:9"),
    (36, "ai-transformation-playbook", "AI 전환 플레이북", "인지 궤도 플레이북", "4:3"),
)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def style_registry(skill_text: str) -> list[tuple[int, str]]:
    try:
        table = skill_text.split("## Full Style List", 1)[1].split("## Core Production Principles", 1)[0]
    except IndexError as exc:
        raise ValueError("SKILL.md is missing the Full Style List section") from exc

    rows = re.findall(r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|", table, re.MULTILINE)
    return [(int(number), name.strip()) for number, name in rows]


def markdown_style_registry(text: str, start_heading: str, end_heading: str) -> list[tuple[int, str]]:
    try:
        table = text.split(start_heading, 1)[1].split(end_heading, 1)[0]
    except IndexError as exc:
        raise ValueError(f"missing style table section {start_heading}") from exc

    rows = re.findall(r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|", table, re.MULTILINE)
    return [(int(number), name.strip()) for number, name in rows]


def reference_registry(reference_text: str) -> list[tuple[int, str]]:
    rows = re.findall(r"^##\s+(\d{2})\.\s+(.+?)\s*$", reference_text, re.MULTILINE)
    return [(int(number), name.strip()) for number, name in rows]


def preview_registry(preview_text: str) -> list[tuple[int, str]]:
    rows = re.findall(
        r'class="card-num">\s*(\d{2})\s*[—-]\s*([^<]+?)\s*</',
        preview_text,
        re.IGNORECASE,
    )
    return [(int(number), name.strip()) for number, name in rows]


def validate_sequence(label: str, rows: list[tuple[int, str]], errors: list[str]) -> None:
    numbers = [number for number, _ in rows]
    names = [name.casefold() for _, name in rows]
    expected = list(range(1, EXPECTED_COUNT + 1))

    if numbers != expected:
        errors.append(f"{label}: expected numbers 01-{EXPECTED_COUNT:02d}, got {numbers}")
    if len(names) != len(set(names)):
        errors.append(f"{label}: duplicate style names found")


def validate_recommendations(
    label: str,
    text: str,
    heading: str,
    canonical_names: set[str],
    errors: list[str],
) -> None:
    try:
        section = text.split(heading, 1)[1].split("---", 1)[0]
    except IndexError:
        errors.append(f"{label}: missing recommendation section {heading}")
        return

    rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", section, re.MULTILINE)
    for goal, recommendation_list in rows:
        if "---" in goal or "Recommended" in recommendation_list or "추천" in recommendation_list:
            continue
        for name in (item.strip() for item in recommendation_list.split(",")):
            if name and name.casefold() not in canonical_names:
                errors.append(f"{label}: non-canonical recommendation {name!r} in {goal.strip()!r}")


def main() -> int:
    skill_text = read("SKILL.md")
    reference_text = read("references/styles.md")
    preview_text = read("preview/modern-pptx-designs.html")
    readmes = [read("README.md"), read("README_ko.md")]
    workflow_text = read("references/image-slot-workflow.md")
    ci_text = read(".github/workflows/validate.yml")

    canonical = style_registry(skill_text)
    references = reference_registry(reference_text)
    previews = preview_registry(preview_text)
    readme_registries = (
        markdown_style_registry(readmes[0], "## 36 Design Styles", "## File Structure"),
        markdown_style_registry(readmes[1], "## 36가지 디자인 스타일", "## 파일 구조"),
    )
    errors: list[str] = []

    for label, rows in (
        ("SKILL.md", canonical),
        ("references/styles.md", references),
        ("preview HTML", previews),
        ("README.md", readme_registries[0]),
        ("README_ko.md", readme_registries[1]),
    ):
        validate_sequence(label, rows, errors)

    if references != canonical:
        errors.append("references/styles.md headings do not exactly match the SKILL.md registry")

    normalized_previews = [(number, name.casefold()) for number, name in previews]
    normalized_canonical = [(number, name.casefold()) for number, name in canonical]
    if normalized_previews != normalized_canonical:
        errors.append("preview card labels do not exactly match the SKILL.md registry")

    for label, registry in zip(("README.md", "README_ko.md"), readme_registries):
        if registry != canonical:
            errors.append(f"{label}: style table does not exactly match the SKILL.md registry")

    card_count = len(re.findall(r'class="card"', preview_text))
    if card_count != EXPECTED_COUNT:
        errors.append(f"preview HTML: expected {EXPECTED_COUNT} cards, got {card_count}")

    if not re.search(rf"트렌드\s+{EXPECTED_COUNT}\b", preview_text):
        errors.append(f"preview HTML: header does not advertise {EXPECTED_COUNT} styles")

    canonical_names = {name.casefold() for _, name in canonical}
    validate_recommendations(
        "SKILL.md",
        skill_text,
        "## Style Recommendation Matrix",
        canonical_names,
        errors,
    )
    validate_recommendations(
        "README.md",
        readmes[0],
        "## Style Selection Guide",
        canonical_names,
        errors,
    )
    validate_recommendations(
        "README_ko.md",
        readmes[1],
        "## 스타일 선택 가이드",
        canonical_names,
        errors,
    )

    local_preview = "preview/modern-pptx-designs.html"
    for filename, content in zip(("README.md", "README_ko.md"), readmes, strict=True):
        if local_preview not in content:
            errors.append(f"{filename}: missing local preview link {local_preview}")
        if "github.io" in content:
            errors.append(f"{filename}: stale GitHub Pages link remains")
        if "assets/images/full_preview.png" not in content:
            errors.append(f"{filename}: missing generated full-preview image")
        if "scripts/" not in content or "validate_style_registry.py" not in content:
            errors.append(f"{filename}: missing validator from file tree")

    if not (ROOT / "assets/images/full_preview.png").is_file():
        errors.append("assets/images/full_preview.png is missing")

    for number, style_id, display_name, legacy_alias, ratio in IDENTITY_CONTRACTS:
        identity_line = (
            f"- `{style_id}`: display `{display_name}`; deprecated alias `{legacy_alias}`; "
            f"native ratio **{ratio}**."
        )
        if identity_line not in skill_text:
            errors.append(f"SKILL.md: missing identity contract for style {number:02d}")

        section_match = re.search(
            rf"^## {number:02d}\. {re.escape(display_name)}\s*$([\s\S]*?)(?=^## \d{{2}}\.|\Z)",
            reference_text,
            re.MULTILINE,
        )
        if not section_match:
            errors.append(f"references/styles.md: missing section for style {number:02d}")
            continue
        section = section_match.group(1)
        if f"**Style ID**: `{style_id}`" not in section:
            errors.append(f"references/styles.md: wrong style_id for style {number:02d}")
        if f"**Legacy Alias**: `{legacy_alias}`" not in section:
            errors.append(f"references/styles.md: wrong legacy alias for style {number:02d}")
        for mode in ("`public_default`", "`origin_compat_mode`"):
            if mode not in section:
                errors.append(f"references/styles.md: style {number:02d} missing {mode} contract")

    for requirement in (
        "public mode is the default",
        "presentation subject may remain as native text",
        "origin compatibility mode",
    ):
        if requirement not in skill_text:
            errors.append(f"SKILL.md: missing compatibility rule {requirement!r}")

    for filename, content in zip(("README.md", "README_ko.md"), readmes, strict=True):
        if "origin compatibility mode" not in content:
            errors.append(f"{filename}: missing origin compatibility policy")

    workflow_requirements = (
        "area(union(clip(each_visible_image_polygon, slide_bounds)))",
        "generative/decorative",
        "native-rebuild",
        "preserve/reuse",
        "screenshot/evidence",
        "brand-protected",
        "style_id: ai-transformation-playbook",
        "status: embedded",
        "attempts: 1",
    )
    for requirement in workflow_requirements:
        if requirement not in workflow_text:
            errors.append(f"image-slot workflow: missing contract token {requirement!r}")

    if "pull_request:" not in ci_text:
        errors.append("CI workflow: validator is not triggered for pull requests")
    if "python3 scripts/validate_style_registry.py" not in ci_text:
        errors.append("CI workflow: style registry validator is not invoked")
    if not re.search(
        r"(?ms)^  validate:\s*$.*?^    permissions:\s*$\n      contents: read\s*$",
        ci_text,
    ):
        errors.append("CI workflow: pull-request validator is not pinned to contents: read")
    if (ROOT / ".github/workflows/static.yml").exists():
        errors.append("CI workflow: legacy Pages deployment workflow still exists")
    for pages_token in (
        "pages: write",
        "actions/configure-pages",
        "actions/upload-pages-artifact",
        "actions/deploy-pages",
        "github-pages",
    ):
        if pages_token in ci_text:
            errors.append(f"CI workflow: Pages deployment token remains: {pages_token}")

    if errors:
        print("Style registry validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Style registry validation passed: {EXPECTED_COUNT} canonical styles are aligned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
