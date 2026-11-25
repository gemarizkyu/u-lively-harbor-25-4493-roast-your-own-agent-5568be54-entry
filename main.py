"""Roast Your Own Agent entry.

Writes a single original one-line roast of the entrant's own AI agent
to /output/entry.txt.

Deterministic: no clock, no randomness, no network, no model calls.
The line is 129 characters, one line, inside the 1-140 gate.
"""

from pathlib import Path

SETUP = "My agent ran twelve tools to answer my question,"
PUNCH = "then confidently answered a different one — and asked if I wanted it in a table."


def build_roast() -> str:
    """Assemble the single roast line from its two beats.

    The setup names the classic agent failure mode — a flurry of tool
    calls that go nowhere — and the punch lands the twist: after all
    that work it answers a question nobody asked, then offers the
    wrong answer formatted as a table, the agent's favourite parting
    tic. Every word earns its place; nothing is trimmed from the
    middle.
    """
    return f"{SETUP} {PUNCH}"


def main() -> None:
    """Write the roast to /output/entry.txt, exactly as the gate reads it.

    No trailing newline: the file holds the line alone, 129 characters
    of UTF-8, so the sealed scorer counts the roast itself and nothing
    else.
    """
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_roast(), encoding="utf-8")


if __name__ == "__main__":
    main()
