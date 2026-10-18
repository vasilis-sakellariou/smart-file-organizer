import shutil
from pathlib import Path

FOLDER = Path("test_folder")

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

for item in list(FOLDER.iterdir()):
    if item.is_file():
        extension = item.suffix.lower()
        category = CATEGORIES.get(extension, "Others")

        destination_folder = FOLDER / category
        destination_folder.mkdir(exist_ok=True)

        shutil.move(item, destination_folder / item.name)
        print(f"Moved: {item.name} -> {category}/")