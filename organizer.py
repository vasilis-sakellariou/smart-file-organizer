import argparse
import json
import shutil
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"


def get_unique_path(path):
    if not path.exists():
        return path

    counter = 1
    while True:
        new_path = path.with_name(f"{path.stem} ({counter}){path.suffix}")
        if not new_path.exists():
            return new_path
        counter += 1


with open(CONFIG_FILE, encoding="utf-8") as file:
    config = json.load(file)

extension_to_category = {}
for category, extensions in config["categories"].items():
    for extension in extensions:
        extension_to_category[extension.lower()] = category

ignored_files = config["ignore"]["files"]
ignored_prefixes = tuple(config["ignore"]["prefixes"])

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
    if not item.is_file():
        continue

    if item.name.lower() in ignored_files or item.name.startswith(ignored_prefixes):
        print(f"Skipped: {item.name}")
        continue

    extension = item.suffix.lower()
    category = extension_to_category.get(extension, "Others")
    destination_folder = folder / category
    destination = get_unique_path(destination_folder / item.name)

    note = ""
    if destination.name != item.name:
        note = f" (renamed to '{destination.name}')"

    if dry_run:
        print(f"[DRY RUN] Would move: {item.name} -> {category}/{note}")
    else:
        destination_folder.mkdir(exist_ok=True)
        shutil.move(item, destination)
        print(f"Moved: {item.name} -> {category}/{note}")