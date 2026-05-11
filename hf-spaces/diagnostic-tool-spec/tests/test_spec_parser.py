"""Tests for the markdown spec parser."""

from pathlib import Path

import pytest

from workshop_tool.models import Spec
from workshop_tool.spec_parser import parse_spec

FIXTURE = Path(__file__).parent / "fixtures" / "example-multiple-regression.md"


def test_parses_example_to_spec_instance():
    spec = parse_spec(FIXTURE.read_text(encoding="utf-8"))
    assert isinstance(spec, Spec)


def test_lernaufgabe_contains_task_keywords():
    spec = parse_spec(FIXTURE.read_text(encoding="utf-8"))
    assert "multiple Regression" in spec.lernaufgabe
    assert "Lernzeit" in spec.lernaufgabe
    assert "Mathenote" in spec.lernaufgabe


def test_skills_section_yields_multiple_entries():
    spec = parse_spec(FIXTURE.read_text(encoding="utf-8"))
    assert len(spec.skills_and_knowledge) >= 4


def test_skills_include_conditional_interpretation():
    spec = parse_spec(FIXTURE.read_text(encoding="utf-8"))
    joined = " ".join(spec.skills_and_knowledge)
    assert "kontrolliert für" in joined or "Konditional" in joined


def test_misconceptions_section_yields_multiple_entries():
    spec = parse_spec(FIXTURE.read_text(encoding="utf-8"))
    assert len(spec.misconceptions) >= 2


def test_handles_german_umlauts():
    spec = parse_spec(FIXTURE.read_text(encoding="utf-8"))
    text = spec.lernaufgabe + " " + " ".join(spec.skills_and_knowledge)
    assert any(ch in text for ch in "äöüÄÖÜ")


def test_missing_lernaufgabe_section_raises():
    md = (
        "## Erforderliche Skills und Knowledge\n- something\n\n"
        "## Antizipierte Misconceptions\n- something\n"
    )
    with pytest.raises(ValueError, match="Lernaufgabe"):
        parse_spec(md)


def test_missing_skills_section_raises():
    md = (
        "## Lernaufgabe (Kontext und Ziel)\nA task description that is long enough.\n\n"
        "## Antizipierte Misconceptions\n- something\n"
    )
    with pytest.raises(ValueError, match="Skills"):
        parse_spec(md)
