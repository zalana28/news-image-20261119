#!/usr/bin/env python3
"""Publish the repo-held poster to the output directory.

Copies entry.png from beside this script into OUTPUT_DIR (default
"/output") as entry.png. Standard library only, byte-for-byte copy, so
repeated runs produce identical output.

Usage:
    OUTPUT_DIR=/tmp/out1 python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path


def publish() -> Path:
    """Copy entry.png to the output directory and return its path."""
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry.png not found next to main.py: {source}")
    target_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    return target


def main() -> int:
    target = publish()
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    size = target.stat().st_size
    print(f"wrote {target} ({size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
