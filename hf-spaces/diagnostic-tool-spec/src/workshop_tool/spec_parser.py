"""Parse a workshop spec from German markdown into a Spec object."""

import re

from .models import Spec

_SECTION_1 = "Lernaufgabe (Kontext und Ziel)"
_SECTION_2 = "Erforderliche Skills und Knowledge"
_SECTION_3 = "Antizipierte Misconceptions"


def _extract_section_body(md: str, heading: str) -> str:
    """Return the body text under a level-2 heading, up to the next level-2
    heading or end of file.
    """
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(md)
    if match is None:
        raise ValueError(f"Spec is missing required section: '{heading}'")
    return match.group(1).strip()


def _extract_top_level_bullets(body: str) -> list[str]:
    """Return top-level bullets (lines starting with '- ').

    Multi-line bullets (the bullet line plus any indented continuation
    lines or italic-annotation lines) are joined into a single string
    per bullet.
    """
    bullets: list[str] = []
    current: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            if current:
                bullets.append(" ".join(current).strip())
            current = [stripped[2:].strip()]
        elif stripped.startswith(("#", ">")):
            if current:
                bullets.append(" ".join(current).strip())
                current = []
        elif stripped and current:
            current.append(stripped)
    if current:
        bullets.append(" ".join(current).strip())
    return [b for b in bullets if b]


def parse_spec(md: str) -> Spec:
    """Parse a markdown spec into a Spec object."""
    section_1 = _extract_section_body(md, _SECTION_1)
    section_2 = _extract_section_body(md, _SECTION_2)
    section_3 = _extract_section_body(md, _SECTION_3)

    lernaufgabe = " ".join(section_1.split())
    skills_and_knowledge = _extract_top_level_bullets(section_2)
    misconceptions = _extract_top_level_bullets(section_3)

    return Spec(
        lernaufgabe=lernaufgabe,
        skills_and_knowledge=skills_and_knowledge,
        misconceptions=misconceptions,
    )
