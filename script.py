#!/usr/bin/env python3
"""
Organize files in a directory by their file extensions.

Usage:
    python script.py /path/to/directory

The script will create subdirectories named after each file extension
(e.g., .txt, .py) and move the corresponding files into them.
"""

import os
import sys
import shutil
from pathlib import Path

def organize_by_extension(target_dir: Path) -> None:
    if not target_dir.is_dir():
        raise NotADirectoryError(f"{target_dir} is not a directory")

    for entry in target_dir.iterdir():
        if entry.is_file():
            ext = entry.suffix or "no_extension"
            dest_dir = target_dir / ext.lstrip(".")
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(entry), dest_dir / entry.name)

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
        sys.exit(1)

    target = Path(sys.argv[1]).resolve()
    organize_by_extension(target)
    print(f"Organized files in {target}")

if __name__ == "__main__":
    main()
