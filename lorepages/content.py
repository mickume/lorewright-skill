import re
from dataclasses import dataclass
from pathlib import Path

from lorepages.constants import (
    CHAPTER_SORT_BASE,
    PLAYER_VISIBLE_TYPES,
    SKIP_DIRS,
    SORT_KEYS,
    PageType,
)


@dataclass
class PageSource:
    slug: str
    source_path: Path
    page_type: PageType
    title: str
    raw_markdown: str
    sort_key: int
    player_visible: bool


_CHAPTER_RE = re.compile(r"^chapter-(\d+)", re.IGNORECASE)


def classify_page(filename: str) -> tuple[PageType, int, bool]:
    stem = Path(filename).stem.lower()

    if stem == "campaign-overview":
        return PageType.OVERVIEW, SORT_KEYS[PageType.OVERVIEW], False

    if stem in ("readme", "briefing"):
        return PageType.BRIEFING, SORT_KEYS[PageType.BRIEFING], True

    if stem == "chapters-summary":
        return PageType.SUMMARY, SORT_KEYS[PageType.SUMMARY], False

    m = _CHAPTER_RE.match(stem)
    if m:
        num = int(m.group(1))
        return PageType.CHAPTER, CHAPTER_SORT_BASE + num, False

    if stem == "npcs":
        return PageType.NPC_ROSTER, SORT_KEYS[PageType.NPC_ROSTER], True

    if stem == "locations":
        return PageType.LOCATIONS, SORT_KEYS[PageType.LOCATIONS], True

    if stem == "factions":
        return PageType.FACTIONS, SORT_KEYS[PageType.FACTIONS], True

    if stem == "timeline":
        return PageType.TIMELINE, SORT_KEYS[PageType.TIMELINE], False

    return PageType.OTHER, SORT_KEYS[PageType.OTHER], False


def _extract_title(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return ""


def discover_campaign(campaign_dir: Path) -> list[PageSource]:
    pages: list[PageSource] = []

    for md_file in sorted(campaign_dir.iterdir()):
        if not md_file.is_file() or md_file.suffix.lower() != ".md":
            continue

        rel = md_file.relative_to(campaign_dir)
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue

        page_type, sort_key, player_visible = classify_page(md_file.name)
        raw = md_file.read_text(encoding="utf-8")
        title = _extract_title(raw) or md_file.stem.replace("-", " ").title()

        pages.append(
            PageSource(
                slug=md_file.stem,
                source_path=md_file,
                page_type=page_type,
                title=title,
                raw_markdown=raw,
                sort_key=sort_key,
                player_visible=player_visible,
            )
        )

    pages.sort(key=lambda p: p.sort_key)
    return pages
