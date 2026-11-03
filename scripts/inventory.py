#!/usr/bin/env python3
"""Inventory local screenshots without assigning visual verdicts or changing files."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def inventory(root):
    result = {"schema_version": 1, "root": str(root), "files": [], "skipped": [], "errors": []}

    def record_walk_error(error):
        result["errors"].append({"path": str(error.filename), "reason": str(error)})

    for directory, subdirectories, filenames in os.walk(root, onerror=record_walk_error):
        folder = Path(directory)
        retained = []
        for name in sorted(subdirectories):
            child = folder / name
            if child.is_symlink():
                result["skipped"].append({"path": child.relative_to(root).as_posix(), "reason": "symlink directory"})
            else:
                retained.append(name)
        subdirectories[:] = retained

        for name in sorted(filenames):
            file_path = folder / name
            if file_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue
            relative_path = file_path.relative_to(root).as_posix()
            if file_path.is_symlink():
                result["skipped"].append({"path": relative_path, "reason": "symlink file"})
                continue
            try:
                digest = hashlib.sha256()
                size = 0
                with file_path.open("rb") as source:
                    for chunk in iter(lambda: source.read(1024 * 1024), b""):
                        digest.update(chunk)
                        size += len(chunk)
                result["files"].append({"path": relative_path, "sha256": digest.hexdigest(), "bytes": size})
            except OSError as error:
                result["errors"].append({"path": relative_path, "reason": str(error)})

    result["files"].sort(key=lambda entry: entry["path"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="A folder of store screenshots or current app captures")
    args = parser.parse_args()
    root = args.directory.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Screenshot directory does not exist or is not a directory: {root}")
    result = inventory(root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] or not result["files"] else 0


if __name__ == "__main__":
    sys.exit(main())
