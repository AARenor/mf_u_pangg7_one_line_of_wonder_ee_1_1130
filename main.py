#!/usr/bin/env python3
"""Write one short line of text for the make.fun bounty.

The entry is a single line of text meant to make a reader feel wonder. It is
written verbatim, with no trailing newline, into the output folder.
"""

import os
import sys

TEXT = "In the margin of the library book on tides: returned late, still wet."


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
