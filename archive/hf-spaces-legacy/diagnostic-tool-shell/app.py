"""
Diagnostic Tool Shell - Gradio App

A workshop tool that takes a student response and returns a CLT-grounded
diagnosis plus a targeted intervention. The output schema is fixed (it IS
the cognitive-load-theory taxonomy); workshop participants iterate the
system prompt to apply that taxonomy in their discipline.

Built by the Virtual Academy at Bern University of Applied Sciences for the
"KI in der Lehre: Advanced" workshop.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import anthropic
import gradio as gr
from dotenv import load_dotenv

from models import DiagnosticResult, SCHEMA_DOCS

load_dotenv()

MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")
SCENARIOS_PATH = Path(__file__).parent / "scenarios.json"

STARTER_SYSTEM_PROMPT = """You are a teacher analyzing a student's written response.

Your job is to apply Cognitive Load Theory to identify what the response reveals
about the student's cognitive state, and to recommend a targeted intervention.

How to choose `load_signal`:
- intrinsic_overload: the student is tracking many interacting pieces and losing
  the thread. Look for partial reasoning that breaks down mid-explanation.
- extrinsic_distractor: the student fixates on irrelevant surface features of
  the task or material. Look for effort spent in the wrong place.
- germane_disengagement: the answer is technically correct but rote. Look for
  retrieval without elaboration, transfer, or self-explanation.
- schema_gap: a foundational concept needed for this task is simply absent.
  Look for confident-sounding answers that miss the prerequisite.
- active_misconception: the student is reasoning consistently from a wrong
  model. Look for systematic errors that fit a coherent (but wrong) theory.

How to choose `intervention`:
- segment_intrinsic_load -> address intrinsic_overload by chunking
- reduce_extrinsic_load -> address extrinsic_distractor by decluttering
- prompt_germane_processing -> address germane_disengagement with a probe
- activate_prior_schema -> address schema_gap with a bridging analogy
- replace_misconception -> address active_misconception with a worked example
  that contrasts the wrong model with the right one

Severity guides how much of an intervention is needed:
- mild: a brief nudge will suffice
- moderate: needs a focused mini-lesson before the student can move on
- fundamental: blocks the whole topic; rebuild before continuing

The `evidence` field must quote or paraphrase the student's actual words.
The `content` field must be specific text you would say to this student, not
generic advice.
"""


def _load_scenarios() -> list[dict]:
    if not SCENARIOS_PATH.exists():
        return [
            {
                "id": "starter",
                "label": "Starter (placeholder)",
                "domain": "general",
                "instruction": "Replace with real scenarios in Phase B1.",
                "responses": [
                    {
                        "label": "Sample response",
                        "text": "I just multiplied them together because that's what you usually do.",
                        "expected_load_signal": "germane_disengagement",
                    }
                ],
            }
        ]
    return json.loads(SCENARIOS_PATH.read_text())


SCENARIOS = _load_scenarios()


def _client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def _diagnostic_tool() -> dict:
    schema = DiagnosticResult.model_json_schema()
    return {
        "name": "report_diagnostic",
        "description": "Report the CLT-grounded diagnosis and targeted intervention for the student response.",
        "input_schema": schema,
    }


def run_diagnostic(system_prompt: str, student_response: str) -> str:
    """Call Claude with the participant's system prompt; force structured output."""
    if not student_response.strip():
        return "_Paste a student response above and press Run._"
    if not os.getenv("ANTHROPIC_API_KEY"):
        return (
            "**ANTHROPIC_API_KEY is not set.** Set the env var (locally in `.env` "
            "or as a Hugging Face Space secret) and reload."
        )

    try:
        message = _client().messages.create(
            model=MODEL,
            max_tokens=2048,
            system=system_prompt,
            tools=[_diagnostic_tool()],
            tool_choice={"type": "tool", "name": "report_diagnostic"},
            messages=[{"role": "user", "content": student_response}],
        )
    except anthropic.APIError as exc:
        return f"**Anthropic API error:** {exc}"

    tool_use = next((b for b in message.content if b.type == "tool_use"), None)
    if tool_use is None:
        return "**The model did not return a structured result.** Try again or refine the prompt."

    try:
        result = DiagnosticResult.model_validate(tool_use.input)
    except Exception as exc:
        return f"**The model returned invalid structured output:** {exc}"

    return _render_result(result)


def _render_result(result: DiagnosticResult) -> str:
    d = result.diagnosis
    r = result.response
    return f"""### Diagnosis

| field | value |
| --- | --- |
| **load_signal** | `{d.load_signal}` |
| **severity** | `{d.severity}` |
| **evidence** | {d.evidence} |
| **domain_notes** | {d.domain_notes} |

### Response

| field | value |
| --- | --- |
| **intervention** | `{r.intervention}` |
| **content** | {r.content} |
"""


def build_portable_prompt(system_prompt: str) -> str:
    """Generate the markdown recipe participants paste into Copilot/ChatGPT/Claude."""
    load_lines = "\n".join(f"- `{k}`: {v}" for k, v in SCHEMA_DOCS["load_signal"].items())
    intervention_lines = "\n".join(
        f"- `{k}`: {v}" for k, v in SCHEMA_DOCS["intervention"].items()
    )
    return f"""# Diagnostic prompt (portable)

Paste this into ChatGPT, Claude, Microsoft Copilot, or any other LLM chat.
Replace the `<<student response>>` marker with the response you want to
analyse.

---

You are a teacher analysing a student's written response. Apply the criteria
in the SYSTEM section below, then return ONLY a JSON object in exactly the
shape specified. Do not add prose around the JSON.

## SYSTEM

{system_prompt.strip()}

## Categories (do not redefine)

**load_signal**:
{load_lines}

**intervention**:
{intervention_lines}

**severity**: mild | moderate | fundamental

## Output shape (JSON only, no prose)

```json
{{
  "diagnosis": {{
    "load_signal": "<one of the load_signal values>",
    "evidence": "<short quote or paraphrase from the student>",
    "severity": "<mild | moderate | fundamental>",
    "domain_notes": "<1-2 sentences of discipline-specific observations>"
  }},
  "response": {{
    "intervention": "<one of the intervention values>",
    "content": "<concrete text to say to the student>"
  }}
}}
```

## Student response

<<student response>>
"""


def _scenario_labels() -> list[str]:
    return [s["label"] for s in SCENARIOS]


def _scenario_response_labels(scenario_label: str) -> list[str]:
    scenario = next((s for s in SCENARIOS if s["label"] == scenario_label), None)
    if scenario is None:
        return []
    return [r["label"] for r in scenario["responses"]]


def _scenario_response_text(scenario_label: str, response_label: str) -> str:
    scenario = next((s for s in SCENARIOS if s["label"] == scenario_label), None)
    if scenario is None:
        return ""
    response = next(
        (r for r in scenario["responses"] if r["label"] == response_label), None
    )
    if response is None:
        return ""
    return response["text"]


def _scenario_brief(scenario_label: str) -> str:
    scenario = next((s for s in SCENARIOS if s["label"] == scenario_label), None)
    if scenario is None:
        return ""
    return f"**Domain:** {scenario['domain']}\n\n**Task:** {scenario['instruction']}"


SCHEMA_DOCS_MARKDOWN = f"""**load_signal** (fixed enum):

{chr(10).join(f"- `{k}`: {v}" for k, v in SCHEMA_DOCS["load_signal"].items())}

**intervention** (fixed enum):

{chr(10).join(f"- `{k}`: {v}" for k, v in SCHEMA_DOCS["intervention"].items())}

**severity** (fixed enum): `mild`, `moderate`, `fundamental`
"""


with gr.Blocks(title="Diagnostic Tool Shell", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
# Diagnostic Tool Shell

Build a CLT-grounded diagnostic tool by iterating the system prompt below.
The output schema is fixed: it is the cognitive-load-theory taxonomy. Your
job is to instruct the model how to apply it in your discipline.
        """
    )

    with gr.Row():
        with gr.Column(scale=3):
            gr.Markdown("### 1. System prompt (edit this)")
            system_prompt = gr.Textbox(
                value=STARTER_SYSTEM_PROMPT,
                lines=20,
                show_label=False,
            )
            with gr.Accordion("Output schema (fixed, not editable)", open=False):
                gr.Markdown(SCHEMA_DOCS_MARKDOWN)

        with gr.Column(scale=2):
            gr.Markdown("### 2. Test on a student response")
            scenario = gr.Dropdown(
                choices=_scenario_labels(),
                value=_scenario_labels()[0] if SCENARIOS else None,
                label="Scenario",
            )
            scenario_brief = gr.Markdown(
                _scenario_brief(_scenario_labels()[0]) if SCENARIOS else ""
            )
            response_label = gr.Dropdown(
                choices=_scenario_response_labels(_scenario_labels()[0])
                if SCENARIOS
                else [],
                value=_scenario_response_labels(_scenario_labels()[0])[0]
                if SCENARIOS and _scenario_response_labels(_scenario_labels()[0])
                else None,
                label="Calibrated response",
            )
            student_response = gr.Textbox(
                value=_scenario_response_text(
                    _scenario_labels()[0],
                    _scenario_response_labels(_scenario_labels()[0])[0],
                )
                if SCENARIOS and _scenario_response_labels(_scenario_labels()[0])
                else "",
                lines=6,
                label="Student response (paste your own or use the calibrated one above)",
            )
            run_button = gr.Button("Run diagnostic", variant="primary")
            output = gr.Markdown(label="Result")

    with gr.Accordion("3. Export portable prompt", open=False):
        gr.Markdown(
            "Copy this and paste it into Copilot, ChatGPT, Claude, or any other LLM."
        )
        portable = gr.Code(
            value=build_portable_prompt(STARTER_SYSTEM_PROMPT),
            language="markdown",
            label="Portable prompt (live preview)",
        )

    def _on_scenario_change(scenario_label: str):
        labels = _scenario_response_labels(scenario_label)
        first_label = labels[0] if labels else None
        first_text = _scenario_response_text(scenario_label, first_label) if first_label else ""
        return (
            _scenario_brief(scenario_label),
            gr.Dropdown(choices=labels, value=first_label),
            first_text,
        )

    def _on_response_change(scenario_label: str, response_label: str):
        return _scenario_response_text(scenario_label, response_label)

    scenario.change(
        _on_scenario_change,
        inputs=[scenario],
        outputs=[scenario_brief, response_label, student_response],
    )
    response_label.change(
        _on_response_change,
        inputs=[scenario, response_label],
        outputs=[student_response],
    )
    system_prompt.change(
        build_portable_prompt,
        inputs=[system_prompt],
        outputs=[portable],
    )
    run_button.click(
        run_diagnostic,
        inputs=[system_prompt, student_response],
        outputs=[output],
    )


if __name__ == "__main__":
    demo.launch()
