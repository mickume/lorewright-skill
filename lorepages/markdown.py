import re

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

from lorepages.constants import DM_ONLY_HEADING_PATTERNS, PageType


class _BlockquoteClassProcessor(Treeprocessor):
    def run(self, root):
        for bq in root.iter("blockquote"):
            existing = bq.get("class", "")
            bq.set("class", f"{existing} read-aloud".strip())


class _BlockquoteClassExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            _BlockquoteClassProcessor(md), "blockquote_class", 15
        )


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")


def filter_dm_content(source: str, page_type: PageType) -> str:
    lines = source.splitlines(keepends=True)
    out: list[str] = []
    skip_level: int | None = None

    for line in lines:
        m = _HEADING_RE.match(line.rstrip())
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip().lower()

            if skip_level is not None:
                if level <= skip_level:
                    skip_level = None
                else:
                    continue

            if any(heading_text == p or heading_text.startswith(p) for p in DM_ONLY_HEADING_PATTERNS):
                skip_level = level
                continue
        elif skip_level is not None:
            continue

        out.append(line)

    return "".join(out)


_MD_LINK_RE = re.compile(r'href="([^"]*?)\.md(#[^"]*?)?"')


def _rewrite_link(m: re.Match) -> str:
    anchor = m.group(2) or ""
    return f'href="{m.group(1)}.html{anchor}"'


def rewrite_links(html: str) -> str:
    return _MD_LINK_RE.sub(_rewrite_link, html)


_METADATA_RE = re.compile(r"^\*\*(.+?):\*\*\s*(.+)$")


def extract_metadata(source: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in source.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        m = _METADATA_RE.match(line)
        if m:
            metadata[m.group(1).strip()] = m.group(2).strip()
        elif metadata:
            break
    return metadata


def render_markdown(source: str, mode: str, page_type: PageType) -> str:
    if mode == "player" and page_type in (
        PageType.NPC_ROSTER,
        PageType.LOCATIONS,
        PageType.FACTIONS,
    ):
        source = filter_dm_content(source, page_type)

    md = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "toc",
            "attr_list",
            _BlockquoteClassExtension(),
        ],
        extension_configs={
            "toc": {"permalink": True, "toc_depth": "2-4"},
        },
    )

    html = md.convert(source)
    html = rewrite_links(html)

    return html
