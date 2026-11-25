#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

The entry is one spoken monologue, held in MONOLOGUE. A dark lord
who poisons the valley's wells one spoon at a time receives the hero
at his table -- and the weariness of forty years of it shows only in
how he talks: the sentences that trail off, the correction he makes
mid-thought, the chore he tends to instead of the duel. He never
says he is tired. He sets a second place at the table instead.

Running this file checks the monologue against the house limits and
writes it, exactly as written and with no trailing newline, to
/output/entry.txt. Only the Python standard library is used.
"""

from pathlib import Path

MONOLOGUE = (
    "This one tastes of almonds. That one too. I drink a little of "
    "each poison every night, so no one will ever know which one "
    "killed them \u2014 no. So I will know. It is a precaution. A "
    "precaution I have taken for \u2014 for a long while. The first "
    "one took my brother. The wells are the scheme, hero. Seven "
    "wells, seven winters, and by spring the whole valley drinks "
    "from my hand. Or it does not drink at all. Your sword is very "
    "bright. Put it down. Sit. The soup is almost ready, and I have "
    "set two places."
)

OUT_PATH = Path("/output/entry.txt")

# Words that would say the tiredness out loud instead of letting
# the voice carry it. The brief forbids them; the check enforces it.
PLAIN_TIRED_WORDS = ("tired", "weary", "exhausted", "sleepy", "fatigue")


def check_monologue(text: str) -> str:
    """Return the monologue unchanged, or raise if it breaks a rule."""
    spoken = text.strip()
    if not spoken:
        raise ValueError("monologue is blank")
    if "\n" in spoken or "\r" in spoken:
        raise ValueError("monologue must be one unbroken paragraph")
    if not 1 <= len(spoken) <= 600:
        raise ValueError(
            "monologue is %d characters; the gate allows 1 to 600"
            % len(spoken)
        )
    words = spoken.split()
    if not 95 <= len(words) <= 105:
        raise ValueError(
            "monologue is %d words; the brief asks for about 100"
            % len(words)
        )
    lowered = spoken.lower()
    for plain in PLAIN_TIRED_WORDS:
        if plain in lowered:
            raise ValueError(
                "monologue says %r outright; the tiredness must be "
                "felt in the voice, not announced" % plain
            )
    return spoken


def emit(text: str) -> tuple[int, int]:
    """Write the checked monologue to OUT_PATH; return (words, bytes)."""
    spoken = check_monologue(text)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    blob = spoken.encode("utf-8")
    OUT_PATH.write_bytes(blob)
    return len(spoken.split()), len(blob)


def main() -> None:
    words, size = emit(MONOLOGUE)
    print("wrote %d words, %d bytes to %s" % (words, size, OUT_PATH))


if __name__ == "__main__":
    main()
