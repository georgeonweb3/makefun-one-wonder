"""One Line of Wonder — make.fun entry.

Writes one line of text (at most 200 characters) that makes a reader
feel wonder, to /output/entry.txt. Deterministic, no network.
"""

import os

ENTRY = (
    "Voyager still phones home from fifteen billion miles away, on less "
    "power than a fridge light, and nobody out there answers back."
)


MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
