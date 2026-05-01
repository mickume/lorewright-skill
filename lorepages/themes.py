import shutil
from pathlib import Path

_BUILTIN_THEMES_DIR = Path(__file__).parent / "themes"


def resolve_theme(theme: str) -> Path:
    theme_path = Path(theme)
    if theme_path.is_dir() and (theme_path / "theme.css").exists():
        return theme_path.resolve()

    builtin = _BUILTIN_THEMES_DIR / theme
    if builtin.is_dir() and (builtin / "theme.css").exists():
        return builtin

    available = [d.name for d in _BUILTIN_THEMES_DIR.iterdir() if d.is_dir()]
    raise FileNotFoundError(
        f"Theme '{theme}' not found. Available built-in themes: {', '.join(available)}"
    )


def copy_theme_assets(theme_dir: Path, output_dir: Path) -> None:
    dest = output_dir / "assets" / "theme"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(theme_dir, dest)
