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

for item in FOLDER.iterdir():
    if item.is_file():
      extension = item.suffix.lower()
      category = CATEGORIES.get(extension, "Others")
      print(f"{item.name}->{category}")
