#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The gate allows at most 120 characters.
"""

import os

ENTRY = "The bug you fear most is already in production, quietly passing all its tests."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: one line, within the 120-char gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 120, f"entry is {len(written)} chars, gate is 1-120"
    assert written.strip(), "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"
    print(f"wrote {len(written.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
