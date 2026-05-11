"""Pydantic models for the diagnostic workshop tool."""

from pydantic import BaseModel, Field


class Spec(BaseModel):
    """Parsed workshop spec from a German markdown document.

    The three fields correspond to the three sections of the workshop's
    spec template:
        ## Lernaufgabe (Kontext und Ziel)
        ## Erforderliche Skills und Knowledge
        ## Antizipierte Misconceptions
    """

    lernaufgabe: str = Field(min_length=20)
    skills_and_knowledge: list[str] = Field(min_length=1)
    misconceptions: list[str] = Field(default_factory=list)


class DiagnosticResponse(BaseModel):
    """Structured diagnosis of a student answer against a spec.

    This Pydantic model defines the *shape* the Anthropic API is forced
    to emit. Passing this model's JSON schema to the API via the `tools`
    parameter is the workshop's concrete example of constraining LLM
    output.
    """

    skills_present: list[str] = Field(
        default_factory=list,
        description=(
            "Skills from the spec that the student's answer demonstrates. "
            "Each entry is the skill name verbatim from the spec."
        ),
    )
    skills_missing: list[str] = Field(
        default_factory=list,
        description=(
            "Skills from the spec that the answer does NOT demonstrate. "
            "Each entry is the skill name verbatim from the spec."
        ),
    )
    misconceptions_detected: list[str] = Field(
        default_factory=list,
        description=(
            "Misconceptions from the spec that the answer exhibits. "
            "Each entry is the misconception name verbatim from the spec."
        ),
    )
    evidence: list[str] = Field(
        default_factory=list,
        description=(
            "Short observations that link the answer to the diagnosis. "
            "Each observation should quote a specific phrase from the "
            "student's answer in single quotes and name which skill or "
            "misconception it indicates."
        ),
    )
    overall_assessment: str = Field(
        description=(
            "Two to three sentences (in the language of the spec) "
            "summarising what the answer shows about the student's "
            "understanding."
        ),
    )
