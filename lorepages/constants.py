from enum import Enum


class PageType(Enum):
    OVERVIEW = "overview"
    CHAPTER = "chapter"
    NPC_ROSTER = "npcs"
    LOCATIONS = "locations"
    FACTIONS = "factions"
    TIMELINE = "timeline"
    SUMMARY = "summary"
    BRIEFING = "briefing"
    OTHER = "other"


SORT_KEYS: dict[PageType, int] = {
    PageType.OVERVIEW: 0,
    PageType.BRIEFING: 1,
    PageType.SUMMARY: 2,
    PageType.NPC_ROSTER: 200,
    PageType.LOCATIONS: 201,
    PageType.FACTIONS: 202,
    PageType.TIMELINE: 203,
    PageType.OTHER: 300,
}

CHAPTER_SORT_BASE = 100

SKIP_DIRS = {"changelog", "art", "references", "_site"}

PLAYER_VISIBLE_TYPES = {
    PageType.BRIEFING,
    PageType.NPC_ROSTER,
    PageType.LOCATIONS,
    PageType.FACTIONS,
}

DM_ONLY_HEADING_PATTERNS = [
    "dm information",
    "dm notes",
    "dm notes & tips",
    "dm resources",
    "secrets",
    "secrets & hidden elements",
    "secrets & intrigue",
    "hidden details",
    "hidden elements",
    "stat block",
    "potential outcomes",
    "roleplaying tips",
    "roleplaying notes",
    "running this location",
    "faction quests",
    "faction events timeline",
    "npc stat block references",
    "modifying npc stats",
    "tracking npc relationships",
    "story role",
]

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}

DEFAULT_THEME = "parchment"
DEFAULT_MODE = "dm"
DEFAULT_BASE_URL = ""
