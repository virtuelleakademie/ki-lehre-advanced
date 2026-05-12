"""The bundled example for the marimo "Beispiel laden" button must parse."""

from workshop_tool.examples import EXAMPLE_SPEC_MD, EXAMPLE_STUDENT_ANSWER
from workshop_tool.spec_parser import parse_spec


def test_example_spec_parses():
    spec = parse_spec(EXAMPLE_SPEC_MD)
    assert spec.lernaufgabe
    assert len(spec.skills_and_knowledge) >= 3
    assert len(spec.misconceptions) >= 2


def test_example_student_answer_is_non_empty():
    assert EXAMPLE_STUDENT_ANSWER.strip()
