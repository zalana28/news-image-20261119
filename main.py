"""News image entry: sum up Thursday 19 November 2026 in one image.

Writes the repository-held poster (entry.png) to /output/entry.png.
Deterministic: the same bytes every run. No network, stdlib only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
