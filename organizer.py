import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".py": "Code",
    ".zip": "Archives",
}

parser = argparse.ArgumentParser(description="Organize files into folders by type.")
parser.add_argument("--folder", default="test_folder", help="Folder to organize (default: test_folder)")
parser.add_argument("--dry-run", action="store_true", help="Show what would happen without moving any files")
args = parser.parse_args()

folder = Path(args.folder).expanduser()
dry_run = args.dry_run

if not folder.is_dir():
    print(f"Error: '{folder}' is not a valid folder.")
    raise SystemExit(1)

for item in list(folder.iterdir()):
    if item.is_file():
        extension = item.suffix.lower()
        category = CATEGORIES.get(extension, "Others")
        destination_folder = folder / category

        if dry_run:
            print(f"[DRY RUN] Would move: {item.name} -> {category}/")
        else:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(item, destination_folder / item.name)
            print(f"Moved: {item.name} -> {category}/")