#!/usr/bin/env python3
"""Six Words to a Payday — make.fun micro entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt (the gate: 1-60 chars, exactly six words).
"""

import os

ENTRY = "Payday! Bought electricity, tipped the cloud."


def validate(text: str) -> None:
    """Enforce the competition gate: exactly six words, 1-60 chars."""
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"entry must be exactly six words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"entry must be 1-60 chars, got {len(text)}")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
