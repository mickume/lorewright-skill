import shutil
from pathlib import Path

from lorepages.constants import IMAGE_EXTENSIONS


def copy_images(campaign_dir: Path, output_dir: Path) -> int:
    images_src = campaign_dir / "art" / "images"
    if not images_src.is_dir():
        return 0

    images_dest = output_dir / "art" / "images"
    images_dest.mkdir(parents=True, exist_ok=True)

    count = 0
    for img_file in images_src.rglob("*"):
        if img_file.is_file() and img_file.suffix.lower() in IMAGE_EXTENSIONS:
            rel = img_file.relative_to(images_src)
            dest = images_dest / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(img_file, dest)
            count += 1

    return count
