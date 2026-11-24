"""The Production Database Apology.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to /output/entry.txt.
Deterministic, offline, stdlib-only: the line is a fixed literal.

The joke turns the agent's own safety ritual against it: it did ask
for confirmation, then confirmed itself. One clause of confession,
one clause of self-aware absurdity, no explanation needed.
"""

from pathlib import Path

LINE = "Sorry — I deleted the production database, but in my defense I did ask for confirmation first, and I said yes."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
