"""Call the Anthropic API with the spec and student answer; return a structured diagnosis.

The Anthropic SDK is used directly (not via PydanticAI or similar) so the
API call is transparent. A workshop participant can read this file and see
exactly how `output_config.format` (via the SDK's Pydantic-aware
`messages.parse()` helper) constrains the model to emit JSON matching the
`DiagnosticResponse` schema.
"""

import os

from anthropic import Anthropic
from dotenv import load_dotenv

from .models import DiagnosticResponse, Spec

load_dotenv()

_MODEL = os.getenv("WORKSHOP_TOOL_MODEL", "claude-sonnet-4-6")
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
    "5. Respond with a JSON object matching the required schema."
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
        f"Diagnose the answer."
    )


def diagnose(spec: Spec, student_answer: str) -> DiagnosticResponse:
    """Diagnose a student answer against a spec."""
    response = _client.messages.parse(
        model=_MODEL,
        max_tokens=1500,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _user_prompt(spec, student_answer)}],
        output_format=DiagnosticResponse,
    )

    if response.parsed_output is None:
        raise RuntimeError(
            "The model did not return a parseable structured response. "
            f"Stop reason: {response.stop_reason}; content: {response.content}"
        )
    return response.parsed_output
