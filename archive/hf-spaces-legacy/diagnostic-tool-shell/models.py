"""
Fixed Pydantic schema for the diagnostic tool shell.

The five `load_signal` and five `intervention` categories ARE the
Cognitive-Load-Theory taxonomy that anchors the workshop. They are NOT
participant-editable. Workshop participants iterate the system prompt; the
schema stays put.

Diagnose-then-respond pipeline: a single LLM call takes a student response
and returns one DiagnosticResult containing both a Diagnosis and a Response.
"""

from typing import Literal
from pydantic import BaseModel, Field


LoadSignal = Literal[
    "intrinsic_overload",
    "extrinsic_distractor",
    "germane_disengagement",
    "schema_gap",
    "active_misconception",
]

Severity = Literal["mild", "moderate", "fundamental"]

Intervention = Literal[
    "segment_intrinsic_load",
    "reduce_extrinsic_load",
    "prompt_germane_processing",
    "activate_prior_schema",
    "replace_misconception",
]


class Diagnosis(BaseModel):
    """What CLT-grounded signal does the student response reveal?"""

    load_signal: LoadSignal = Field(
        description=(
            "The dominant cognitive-load signal in the response. "
            "intrinsic_overload: too much element interactivity for the learner's current schema. "
            "extrinsic_distractor: irrelevant complexity in material or task design. "
            "germane_disengagement: student going through motions without effortful processing. "
            "schema_gap: relevant prior knowledge is missing. "
            "active_misconception: a wrong schema is in place and being applied."
        )
    )
    evidence: str = Field(
        description="A short quote or paraphrase from the student's response that justifies the load_signal classification."
    )
    severity: Severity = Field(
        description="How load-bearing is this signal? mild = minor adjustment, moderate = blocks progress, fundamental = blocks the whole topic."
    )
    domain_notes: str = Field(
        description="Discipline-specific observations the educator should know. One or two sentences."
    )


class Response(BaseModel):
    """A targeted intervention keyed to the diagnosis."""

    intervention: Intervention = Field(
        description=(
            "The intervention category that best addresses the diagnosis. "
            "segment_intrinsic_load: break the task into smaller, less-interactive pieces. "
            "reduce_extrinsic_load: simplify presentation, remove distractors. "
            "prompt_germane_processing: a Socratic probe or reflection question. "
            "activate_prior_schema: an analogy or connection to existing knowledge. "
            "replace_misconception: a corrective explanation paired with a worked example."
        )
    )
    content: str = Field(
        description="The actual text to say to the student. Concrete, specific to the diagnosed signal, and at most a short paragraph."
    )


class DiagnosticResult(BaseModel):
    """One pass of the diagnose-then-respond pipeline."""

    diagnosis: Diagnosis
    response: Response


SCHEMA_DOCS = {
    "load_signal": {
        "intrinsic_overload": "Too much element interactivity for the learner's current schema.",
        "extrinsic_distractor": "Irrelevant complexity in material or task design.",
        "germane_disengagement": "Going through motions without effortful processing.",
        "schema_gap": "Relevant prior knowledge is missing.",
        "active_misconception": "A wrong schema is in place and being applied.",
    },
    "intervention": {
        "segment_intrinsic_load": "Break the task into smaller, less-interactive pieces.",
        "reduce_extrinsic_load": "Simplify presentation, remove distractors.",
        "prompt_germane_processing": "Socratic probe or reflection question.",
        "activate_prior_schema": "Analogy or connection to existing knowledge.",
        "replace_misconception": "Corrective explanation paired with a worked example.",
    },
}
