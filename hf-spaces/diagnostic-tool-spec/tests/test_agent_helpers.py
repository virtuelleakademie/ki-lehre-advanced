"""Smoke tests for the public agent-module helpers used by the marimo UI.

These tests do not make API calls. They only verify that the public surface
exposed for the UI (SYSTEM_PROMPT, build_user_prompt) behaves predictably.
"""

from workshop_tool.agent import SYSTEM_PROMPT, build_user_prompt
from workshop_tool.models import Spec


def _spec() -> Spec:
    return Spec(
        lernaufgabe="Eine Lernaufgabe lang genug für die Validierung.",
        skills_and_knowledge=["Skill A", "Skill B"],
        misconceptions=["Misconception X"],
    )


def test_system_prompt_mentions_schema():
    assert SYSTEM_PROMPT.strip()
    assert "schema" in SYSTEM_PROMPT.lower()


def test_build_user_prompt_includes_spec_fields():
    prompt = build_user_prompt(_spec(), "Eine Studierenden-Antwort.")
    assert "Eine Lernaufgabe lang genug für die Validierung." in prompt
    assert "Skill A" in prompt
    assert "Skill B" in prompt
    assert "Misconception X" in prompt
    assert "Eine Studierenden-Antwort." in prompt


def test_build_user_prompt_handles_missing_misconceptions():
    spec = Spec(
        lernaufgabe="Eine Lernaufgabe lang genug für die Validierung.",
        skills_and_knowledge=["Skill A"],
        misconceptions=[],
    )
    prompt = build_user_prompt(spec, "Antwort.")
    assert "(none listed)" in prompt
