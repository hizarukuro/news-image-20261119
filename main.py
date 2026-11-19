"""Front page of Thursday 19 November 2026: the midnight edition.

This program carries one finished front page. The picture sits beside
this file in the repository as entry.png; running the program copies
that picture, unchanged, into the output directory. The destination is
the folder named by the MAKEFUN_OUTPUT_DIR environment variable, or a
folder named "output" in the working directory when the variable is
not set. The copy is exact: the same bytes come out on every run.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    picture = os.path.join(here, "entry.png")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(target_dir, exist_ok=True)
    # copyfile moves the bytes without touching them, so the result is
    # byte-for-byte the front page that was rendered for this entry.
    shutil.copyfile(picture, os.path.join(target_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
