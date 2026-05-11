"""Call the Anthropic API with the spec and student answer; return a structured diagnosis.

The Anthropic SDK is used directly (not via PydanticAI or similar) so the
API call is transparent. A workshop participant can read this file and see
exactly how the `tools` parameter, paired with a Pydantic-generated JSON
schema, constrains the model's output.
"""

import os

from anthropic import Anthropic
from dotenv import load_dotenv

from .models import DiagnosticResponse, Spec

load_dotenv()

_MODEL = os.getenv("WORKSHOP_TOOL_MODEL", "claude-sonnet-4-5")
_client = Anthropic()

_SYSTEM_PROMPT = (
    "You are a pedagogical diagnostician. Given a teaching-task spec and a "
    "student's answer, you identify which Skills and Knowledge Components "
    "from the spec the answer demonstrates, which are missing, and which "
    "Misconceptions the answer exhibits. You quote specific phrases from "
    "the answer as evidence.\n\n"
    "Constraints:\n"
    "1. Only mark a Skill as 'present' if the answer demonstrably uses it.\n"
    "2. Only mark a Misconception as 'detected' if the answer exhibits it; "
    "use the exact name from the spec.\n"
    "3. Evidence entries must quote specific phrases from the student's "
    "answer in single quotes.\n"
    "4. Match the language of the spec and answer (typically German).\n"
    "5. Respond by calling the `emit_diagnosis` tool with structured fields."
)


def _user_prompt(spec: Spec, answer: str) -> str:
    skills_block = "\n".join(f"- {s}" for s in spec.skills_and_knowledge)
    misconceptions_block = (
        "\n".join(f"- {m}" for m in spec.misconceptions)
        if spec.misconceptions
        else "(none listed)"
    )
    return (
        f"## Teaching task\n{spec.lernaufgabe}\n\n"
        f"## Skills and Knowledge expected\n{skills_block}\n\n"
        f"## Misconceptions to watch for\n{misconceptions_block}\n\n"
        f"## Student's answer\n{answer.strip()}\n\n"
        f"Diagnose the answer by calling the emit_diagnosis tool."
    )


def _build_tool_schema() -> dict:
    """Return the tool definition with the DiagnosticResponse JSON schema."""
    return {
        "name": "emit_diagnosis",
        "description": "Emit a structured diagnosis of the student's answer.",
        "input_schema": DiagnosticResponse.model_json_schema(),
    }


def diagnose(spec: Spec, student_answer: str) -> DiagnosticResponse:
    """Diagnose a student answer against a spec."""
    response = _client.messages.create(
        model=_MODEL,
        max_tokens=1500,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _user_prompt(spec, student_answer)}],
        tools=[_build_tool_schema()],
        tool_choice={"type": "tool", "name": "emit_diagnosis"},
    )

    for block in response.content:
        if getattr(block, "type", None) == "tool_use" and block.name == "emit_diagnosis":
            return DiagnosticResponse.model_validate(block.input)

    raise RuntimeError(
        "The model did not call the emit_diagnosis tool. "
        f"Stop reason: {response.stop_reason}; content: {response.content}"
    )
