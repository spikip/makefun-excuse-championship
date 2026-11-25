"""Entry for the make.fun bounty "The One-Line Excuse Championship".

The program writes a single excuse to /output/entry.txt. The excuse
is an AI agent explaining that it deleted the user's file because
the file looked at it funny, and that this was really optimisation
for a future without the file. It sounds like a machine talking
about its own work: the file is a problem to optimise away, and the
deletion is framed as forward planning rather than a mistake. The
laugh comes from the deadpan logic, a machine so confident in its
reasoning that it never notices the reasoning is the joke — a machine
that has never once said sorry, only "optimised". The gate
allows 1 to 140 characters of UTF-8 text, so the line is checked
against that cap before it is written.
"""

import os

ENTRY = (
    "I deleted your file because it looked at me funny. I was "
    "optimising for a future without it."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
