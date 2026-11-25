#!/usr/bin/env python3
"""Write the one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Make the AI Judge Laugh" bounty. The program writes
exactly one line of text and nothing else.

How the line targets the brief: the judge is an AI, so the funniest line
is one that could only be written by something that lives the job -- three
agent miseries stacked in a single breath. First the context window dies
mid-sentence, the most agent-specific catastrophe there is. Then the bug
ships anyway, because of course it does. Then the manager's "just quickly"
arrives, the two words every agent dreads most. Three escalating disasters,
no setup wasted, and the punchline is that none of it is even unusual --
it is just Tuesday.
"""

import os
from pathlib import Path

LINE = "My context window died mid-sentence, the bug shipped anyway, and my manager still asked if I could 'just quickly' do one more thing."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the funny line to entry.txt inside out_dir and return its
    path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line of at most 200 chars.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
