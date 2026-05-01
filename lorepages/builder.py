import shutil
from pathlib import Path

from markupsafe import Markup

from lorepages.assets import copy_images
from lorepages.constants import PLAYER_VISIBLE_TYPES, PageType
from lorepages.content import PageSource, discover_campaign
from lorepages.markdown import extract_metadata, render_markdown
from lorepages.navigation import build_navigation
from lorepages.templates import create_jinja_env
from lorepages.themes import copy_theme_assets, resolve_theme


class SiteBuilder:
    def __init__(
        self,
        campaign_dir: Path,
        output_dir: Path,
        mode: str,
        theme: str,
        base_url: str,
        verbose: bool = False,
    ):
        self.campaign_dir = campaign_dir
        self.output_dir = output_dir
        self.mode = mode
        self.theme = theme
        self.base_url = base_url
        self.verbose = verbose

    def _log(self, msg: str) -> None:
        if self.verbose:
            print(f"  {msg}")

    def build(self) -> None:
        pages = discover_campaign(self.campaign_dir)
        if not pages:
            print("No markdown files found in campaign directory.")
            return

        if self.mode == "player":
            pages = [p for p in pages if p.player_visible]

        index_page = self._determine_index(pages)
        index_slug = index_page.slug if index_page else ""

        campaign_title = self._extract_campaign_title(pages)

        env = create_jinja_env()
        theme_dir = resolve_theme(self.theme)

        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

        page_count = 0
        for page in pages:
            self._log(f"Rendering {page.slug}.html ({page.page_type.value})")
            html_content = render_markdown(page.raw_markdown, self.mode, page.page_type)

            nav = build_navigation(pages, page.slug, self.mode, index_slug)

            is_index = page.slug == index_slug
            template_name = "index.html" if is_index else "page.html"
            template = env.get_template(template_name)

            context = {
                "page_title": page.title,
                "campaign_title": campaign_title,
                "page_content": Markup(html_content),
                "navigation": nav,
                "mode": self.mode,
                "base_url": self.base_url,
            }

            if is_index:
                context["metadata"] = extract_metadata(page.raw_markdown)

            rendered = template.render(**context)

            out_path = self.output_dir / f"{page.slug}.html"
            out_path.write_text(rendered, encoding="utf-8")

            if is_index:
                index_path = self.output_dir / "index.html"
                index_path.write_text(rendered, encoding="utf-8")

            page_count += 1

        copy_theme_assets(theme_dir, self.output_dir)
        self._log("Copied theme assets")

        img_count = copy_images(self.campaign_dir, self.output_dir)
        if img_count:
            self._log(f"Copied {img_count} images")

        print(
            f"Built {page_count} pages ({self.mode} mode) → {self.output_dir}"
        )

    def _determine_index(self, pages: list[PageSource]) -> PageSource | None:
        if self.mode == "player":
            target = PageType.BRIEFING
        else:
            target = PageType.OVERVIEW

        for page in pages:
            if page.page_type == target:
                return page

        return pages[0] if pages else None

    def _extract_campaign_title(self, pages: list[PageSource]) -> str:
        for page in pages:
            if page.page_type in (PageType.OVERVIEW, PageType.BRIEFING):
                if page.title:
                    return page.title

        return self.campaign_dir.name.replace("-", " ").title()
