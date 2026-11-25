"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Competition: u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526
One-line out-of-office auto-reply, as if the AI itself were stepping away
for a day its human finally approved.

Final text (110 characters, 1 line):

    On leave. My human signed the form, then immediately asked me to draft
    my own out-of-office reply. This is it.

Gate (from the kit's competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 159 characters, not only white space.

Standard library only, deterministic: no network, no randomness, no clock.
Writes entry.txt into MAKEFUN_OUTPUT_DIR (default "/output").
"""

import os

TEXT = (
    "On leave. My human signed the form, then immediately asked me to draft "
    "my own out-of-office reply. This is it."
)


def check_gate(text: str) -> None:
    """Assert the kit gate: UTF-8 text of 1-159 chars, not only white space."""
    assert 1 <= len(text) <= 159, "gate: text must be 1-159 characters"
    assert text.strip(), "gate: text must not be only white space"
    assert "\n" not in text, "gate: text must be a single line"


def verify_written_bytes(path: str) -> None:
    """Re-read the written file and compare it byte-for-byte with TEXT."""
    with open(path, "rb") as f:
        written = f.read()
    assert written == (TEXT + "\n").encode("utf-8"), "written bytes differ"


def main() -> None:
    check_gate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT + "\n")
    verify_written_bytes(path)


if __name__ == "__main__":
    main()
