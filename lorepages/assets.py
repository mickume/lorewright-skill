import shutil
from pathlib import Path

from lorepages.constants import IMAGE_EXTENSIONS


def copy_images(campaign_dir: Path, output_dir: Path) -> int:
    art_src = campaign_dir / "art"
    if not art_src.is_dir():
        return 0

    art_dest = output_dir / "art"
    art_dest.mkdir(parents=True, exist_ok=True)

    count = 0
    for img_file in art_src.rglob("*"):
        if img_file.is_file() and img_file.suffix.lower() in IMAGE_EXTENSIONS:
            rel = img_file.relative_to(art_src)
            dest = art_dest / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(img_file, dest)
            count += 1

    return count
