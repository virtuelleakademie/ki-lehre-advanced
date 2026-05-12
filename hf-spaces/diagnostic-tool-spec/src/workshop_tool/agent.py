"""Call the Anthropic API with the spec and student answer; return a structured diagnosis.

The Anthropic SDK is used directly (not via PydanticAI or similar) so the
API call is transparent. A workshop participant can read this file and see
exactly how `output_config.format` (via the SDK's Pydantic-aware
`messages.parse()` helper) constrains the model to emit JSON matching the
`DiagnosticResponse` schema.
"""

import os
import time
from dataclasses import dataclass

from anthropic import Anthropic
from dotenv import load_dotenv

from .models import DiagnosticResponse, Spec

load_dotenv()

MODEL = os.getenv("WORKSHOP_TOOL_MODEL", "claude-sonnet-4-6")
_client = Anthropic()

SYSTEM_PROMPT = (
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


def build_user_prompt(spec: Spec, answer: str) -> str:
    """Render the spec and student answer into the user-message text sent to the API."""
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


@dataclass
class DiagnosisResult:
    """The diagnosis plus call metadata the UI can display."""

    response: DiagnosticResponse
    model: str
    latency_seconds: float
    input_tokens: int | None
    output_tokens: int | None


def diagnose(spec: Spec, student_answer: str) -> DiagnosticResponse:
    """Diagnose a student answer against a spec.

    Returns only the parsed response. Existing callers and tests rely on this
    shape; the UI calls `diagnose_with_meta` to also surface model/latency.
    """
    return diagnose_with_meta(spec, student_answer).response


def diagnose_with_meta(spec: Spec, student_answer: str) -> DiagnosisResult:
    """Diagnose and return the response wrapped with model name and call timing."""
    user_prompt = build_user_prompt(spec, student_answer)
    start = time.perf_counter()
    response = _client.messages.parse(
        model=MODEL,
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
        output_format=DiagnosticResponse,
    )
    latency = time.perf_counter() - start

    if response.parsed_output is None:
        raise RuntimeError(
            "The model did not return a parseable structured response. "
            f"Stop reason: {response.stop_reason}; content: {response.content}"
        )

    usage = getattr(response, "usage", None)
    input_tokens = getattr(usage, "input_tokens", None) if usage else None
    output_tokens = getattr(usage, "output_tokens", None) if usage else None

    return DiagnosisResult(
        response=response.parsed_output,
        model=MODEL,
        latency_seconds=latency,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
    )
