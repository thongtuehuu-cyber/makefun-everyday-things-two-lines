"""Write the two-line make.fun entry to /output/entry.txt.

Deterministic, no network, no randomness. The entry explains a traffic jam
to a 10-year-old through a stuck-zipper analogy, then says honestly what the
analogy maps and what it leaves out.
"""

import os
import sys

ENTRY = (
    "A traffic jam is a zipper stuck halfway up a giant coat, with the cars "
    "as its teeth jammed tight together so nobody can move until one of them "
    "wiggles free.\n"
    "It maps how cars lock bumper to bumper and block each other, but it "
    "leaves out that a road has many lanes while a zipper has only one row "
    "of teeth, and that you cannot just unzip a road."
)

MAX_CHARS = 400


def validate_entry(text):
    """Return the text if it is a valid entry, else raise ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if text.endswith("\n"):
        raise ValueError("entry must not end with a trailing newline")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly 2 lines, got %d" % len(lines))
    if any(line.strip() == "" for line in lines):
        raise ValueError("entry lines must not be blank")
    return text


def write_entry(output_dir):
    """Validate the entry and write it to <output_dir>/entry.txt."""
    validate_entry(ENTRY)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back gate: what landed on disk must be exactly the winning entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch: entry.txt != ENTRY"
    validate_entry(written)
    return path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
