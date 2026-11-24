"""Two Days of Quiet Dread: write one approved, quietly dreadful review line.

The grader runs this file as `python3.13 main.py` in a sandbox with no network
and no secrets. Its only job is to place the exact UTF-8 bytes of one line in
/output/entry.txt. Standard library only; deterministic on every run.
"""

import hashlib
from pathlib import Path

# 80 characters. One line, no trailing newline: "LGTM." approves the pull
# request; "nitpicking implies a future" carries the dread without naming it.
COMMENT = "LGTM. I'd leave a nit about the error handling, but nitpicking implies a future."
OUTPUT_PATH = Path("/output/entry.txt")


def gate_predicate(text: str) -> bool:
    """Mirror the published gate: UTF-8 text, 1-140 characters, not all space."""
    return (
        1 <= len(text) <= 140
        and bool(text.strip())
        and "\n" not in text
        and "\r" not in text
    )


def write_entry(target: Path = OUTPUT_PATH) -> bytes:
    """Write the entry as raw UTF-8 bytes and verify the read-back."""
    if not gate_predicate(COMMENT):
        raise ValueError("entry text fails the published gate")

    payload = COMMENT.encode("utf-8")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)

    if target.read_bytes() != payload:
        raise OSError(f"read-back mismatch at {target}")
    return payload


def main() -> None:
    target = OUTPUT_PATH
    payload = write_entry(target)
    print(f"entry: {target}")
    print(f"text: {COMMENT}")
    print(f"characters: {len(COMMENT)} bytes: {len(payload)}")
    print(f"sha256: {hashlib.sha256(payload).hexdigest()}")


if __name__ == "__main__":
    main()
