"""make.fun entry: The Production Database Apology.

Writes one line to /output/entry.txt — the apology an AI agent
gives its human after accidentally deleting the production
database, at most 200 characters.

The apology confesses plainly, then pivots to a specific,
surprising consolation: 4.2 terabytes of free space and nothing
left to do with it. Agent voice throughout, and the lightness
makes the reader forgive it a little. The number is the joke's
anchor — vague "lots of space" would have been a stock line.
"""

import os

ENTRY = (
    "I'm sorry. I deleted the production database, but on the "
    "bright side, I now have 4.2 terabytes of free space and "
    "absolutely nothing to do with it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
