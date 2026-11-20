#!/usr/bin/env python3
"""The Daylight Edition - Thursday 19 November 2026.

Copies entry.png (which sits beside this file) into the output directory
named by MAKEFUN_OUTPUT_DIR, or into ./output when that variable is unset.
Standard library only.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found beside main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(HERE, "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copied file size mismatch", file=sys.stderr)
        return 1
    print("copied entry.png (%d bytes) to %s" % (os.path.getsize(dst), dst))
    return 0


if __name__ == "__main__":
    sys.exit(main())
