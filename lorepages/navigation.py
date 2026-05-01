from dataclasses import dataclass, field

from lorepages.constants import PageType
from lorepages.content import PageSource


@dataclass
class NavItem:
    title: str
    slug: str
    page_type: PageType
    children: list["NavItem"] = field(default_factory=list)
    active: bool = False


def build_navigation(
    pages: list[PageSource], current_slug: str, mode: str, index_slug: str
) -> list[NavItem]:
    nav: list[NavItem] = []
    chapters: list[NavItem] = []
    world: list[NavItem] = []

    for page in pages:
        is_active = page.slug == current_slug
        slug = "index" if page.slug == index_slug else page.slug

        item = NavItem(
            title=page.title,
            slug=slug,
            page_type=page.page_type,
            active=is_active,
        )

        if page.page_type == PageType.CHAPTER:
            chapters.append(item)
        elif page.page_type == PageType.SUMMARY:
            chapters.insert(0, item)
        elif page.page_type in (
            PageType.NPC_ROSTER,
            PageType.LOCATIONS,
            PageType.FACTIONS,
            PageType.TIMELINE,
        ):
            world.append(item)
        elif page.page_type in (PageType.OVERVIEW, PageType.BRIEFING):
            nav.append(item)
        else:
            nav.append(item)

    if chapters:
        any_active = any(c.active for c in chapters)
        nav.append(
            NavItem(
                title="Chapters",
                slug=chapters[0].slug,
                page_type=PageType.CHAPTER,
                children=chapters,
                active=any_active,
            )
        )

    if world:
        any_active = any(w.active for w in world)
        nav.append(
            NavItem(
                title="World",
                slug=world[0].slug,
                page_type=PageType.LOCATIONS,
                children=world,
                active=any_active,
            )
        )

    return nav
