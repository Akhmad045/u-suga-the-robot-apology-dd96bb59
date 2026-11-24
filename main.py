#!/usr/bin/env python3
"""The Laundry Announcement — writes a two-line robot apology to /output/entry.txt.

Line one: the robot apologizes for waking the baby at 3 a.m. by announcing,
at full volume, that the laundry was done. Line two: what it learned — good
news can wait until morning — and what it will do differently: whisper after
midnight. A small, exact, human-scale slip, and a lesson that follows from
that exact mistake.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

ENTRY = (
    "I am sorry I woke the baby at 3 a.m. by announcing, at full volume, "
    "that the laundry was done.\n"
    "I have learned that good news can wait until morning, so from now on "
    "I will whisper after midnight."
)

MAX_CHARS = 400

USAGE = "usage: main.py [--self-test]"


def validate(text):
    """Enforce the competition gate: 1-400 chars, exactly two lines,
    not only whitespace, no leading or trailing whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) == 0:
        raise ValueError("entry is empty (gate needs 1-400 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the 400-character gate"
        )
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(
            f"entry must be exactly two lines, got {len(lines)}"
        )
    for line in lines:
        if line.strip() == "":
            raise ValueError("entry line must not be blank")
        if "\r" in line:
            raise ValueError("entry must not contain carriage returns")
    return text


def self_test():
    """Exercise validate() against the gate's rejection cases."""
    cases = [
        ("", "empty"),
        (" ", "whitespace-only"),
        ("x" * 401, "401 chars"),
        ("one line only", "one line"),
        ("a\nb\nc", "three lines"),
        (" padded \nsecond line", "leading/trailing whitespace"),
        ("first line\n", "trailing newline"),
        ("first line\n \n", "blank second line"),
        ("first\r\nsecond", "carriage return"),
    ]
    for text, label in cases:
        try:
            validate(text)
        except ValueError as exc:
            print(f"self-test ok: rejected {label}: {exc}")
        else:
            raise SystemExit(f"self-test FAIL: {label} was accepted")
    # boundaries: 1 char and exactly 400 chars must pass the length rule
    validate("y\nz")
    print("self-test ok: two-line minimal entry accepted")
    validate("y" * 199 + "\n" + "z" * 200)
    print("self-test ok: 400-char boundary accepted")
    # the entry itself must pass its own gate
    validate(ENTRY)
    print("self-test ok: entry passes the gate")
    print("self-test: all cases passed")
    return 0


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--self-test" and len(sys.argv) == 2:
            return self_test()
        print(USAGE, file=sys.stderr)
        return 2
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(ENTRY)
    data = text.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the two lines
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print(f"wrote {out_path}: {len(text)} chars, "
          f"{len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
