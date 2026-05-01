import argparse
import sys
from pathlib import Path

from lorepages import __version__
from lorepages.constants import DEFAULT_BASE_URL, DEFAULT_MODE, DEFAULT_THEME


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lorepages",
        description="Static site generator for lorewright D&D campaign content",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command")

    build = subparsers.add_parser("build", help="Build a static site from a campaign directory")
    build.add_argument(
        "campaign_dir",
        type=Path,
        help="Path to the campaign directory",
    )
    build.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: <campaign-dir>/_site/)",
    )
    build.add_argument(
        "--mode",
        choices=["dm", "player"],
        default=DEFAULT_MODE,
        help=f"Build mode (default: {DEFAULT_MODE})",
    )
    build.add_argument(
        "--theme",
        default=DEFAULT_THEME,
        help=f"Theme name or path to custom theme directory (default: {DEFAULT_THEME})",
    )
    build.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Base URL for links (default: {DEFAULT_BASE_URL})",
    )
    build.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 1

    if args.command == "build":
        campaign_dir = args.campaign_dir.resolve()
        if not campaign_dir.is_dir():
            print(f"Error: {campaign_dir} is not a directory", file=sys.stderr)
            return 1

        output_dir = args.output_dir
        if output_dir is None:
            output_dir = campaign_dir / "_site"
        else:
            output_dir = output_dir.resolve()

        base_url = args.base_url
        if base_url and not base_url.endswith("/"):
            base_url += "/"

        from lorepages.builder import SiteBuilder

        builder = SiteBuilder(
            campaign_dir=campaign_dir,
            output_dir=output_dir,
            mode=args.mode,
            theme=args.theme,
            base_url=base_url,
            verbose=args.verbose,
        )
        builder.build()

    return 0


if __name__ == "__main__":
    sys.exit(main())
