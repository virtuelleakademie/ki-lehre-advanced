"""
Diagnostic Tool Shell - Marimo Notebook (Tier-3 Demonstration)

This notebook is the tier-3 exhibit in Block 3 of the workshop. It compiles a
Spec Card into a structured-output API call, with each step of the data flow
laid out as a separate cell. The same Pydantic schema and Anthropic tool-use
call as the Gradio shell at hf-spaces/diagnostic-tool-shell/, but legible
cell by cell.

Run locally:
    marimo edit notebook.py        # editable, code visible
    marimo run notebook.py         # tool view, code hidden

Deploy:
    Hugging Face Space (sdk: docker; ANTHROPIC_API_KEY as a secret).
"""

import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _intro():
    import marimo as mo
    mo.md(
        """
        # Tier-3 Demonstration: Spec Card als strukturierter API-Aufruf

        Diese Notebook-Demo zeigt, wie eine Spec Card in einen strukturierten
        API-Aufruf übersetzt wird. Jede Zelle macht einen Schritt des Datenflusses
        sichtbar:

        1. **Schema** definieren (Pydantic): die Struktur, die das Modell zurückgeben muss
        2. **Szenario** auswählen (eine kalibrierte Studierendenantwort)
        3. **System-Prompt** schreiben: deine Spec Card als Text
        4. **API-Aufruf**: Claude Haiku 4.5 mit erzwungenem Tool-Use
        5. **Ergebnis** validieren: aus JSON wird ein typsicheres Pydantic-Objekt
        6. **Export**: portabler Prompt, den du in jeden anderen LLM einfügen kannst
        """
    )
    return (mo,)


@app.cell
def _imports():
    import json
    import os
    from pathlib import Path
    from typing import Literal

    import anthropic
    from pydantic import BaseModel, Field

    return BaseModel, Field, Literal, Path, anthropic, json, os


@app.cell
def _schema(BaseModel, Field, Literal):
    # ---------- Schritt 1: Das Schema ----------
    # Die Diagnose-Sektion einer Spec Card, hier als Pydantic-Modell.

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
        load_signal: LoadSignal = Field(description="Das dominante kognitive Signal.")
        evidence: str = Field(description="Kurzes Zitat oder Paraphrase aus der Antwort.")
        severity: Severity = Field(description="mild | moderate | fundamental")
        domain_notes: str = Field(description="Disziplinspezifische Beobachtungen.")

    class InterventionResponse(BaseModel):
        intervention: Intervention = Field(description="Die passende Interventionskategorie.")
        content: str = Field(description="Konkreter Text, den die Lehrperson sagen würde.")

    class DiagnosticResult(BaseModel):
        diagnosis: Diagnosis
        response: InterventionResponse

    return (DiagnosticResult,)


@app.cell
def _scenarios(Path, json):
    # ---------- Schritt 2: Szenarien laden ----------
    # Sechs disziplinäre Szenarien, je drei kalibrierte Antworten.

    scenarios_path = Path(__file__).parent / "scenarios.json"
    SCENARIOS = json.loads(scenarios_path.read_text())
    f"Geladen: {len(SCENARIOS)} Szenarien mit {sum(len(s['responses']) for s in SCENARIOS)} kalibrierten Antworten."
    return (SCENARIOS,)


@app.cell
def _picker(SCENARIOS, mo):
    # ---------- Schritt 2 (Forts.): UI zum Auswählen ----------

    scenario_picker = mo.ui.dropdown(
        options={s["label"]: s for s in SCENARIOS},
        value=SCENARIOS[0]["label"],
        label="Szenario",
    )
    scenario_picker
    return (scenario_picker,)


@app.cell
def _response_picker(mo, scenario_picker):
    response_picker = mo.ui.dropdown(
        options={r["label"]: r for r in scenario_picker.value["responses"]},
        value=scenario_picker.value["responses"][0]["label"],
        label="Kalibrierte Antwort",
    )
    response_picker
    return (response_picker,)


@app.cell
def _show_response(mo, response_picker, scenario_picker):
    mo.md(f"""
    **Aufgabe ({scenario_picker.value['domain']}):** {scenario_picker.value['instruction']}

    **Studierendenantwort (Tag: `{response_picker.value['expected_load_signal']}`):**

    > {response_picker.value['text']}
    """)
    return


@app.cell
def _system_prompt(mo):
    # ---------- Schritt 3: System-Prompt (deine Spec Card als Text) ----------
    starter_prompt = """Du bist eine Lehrperson, die eine schriftliche Studierendenantwort analysiert.

    Wende kognitive Belastungstheorie an: identifiziere, welches Signal die Antwort
    zeigt, und schlage eine zielgerichtete Intervention vor.

    Wahl des `load_signal`:
    - intrinsic_overload: zu viel Element-Interaktivität für das aktuelle Schema
    - extrinsic_distractor: irrelevante Komplexität fängt die Aufmerksamkeit
    - germane_disengagement: fehlerfreier Abruf ohne Verarbeitung
    - schema_gap: notwendiges Vorwissen fehlt schlicht
    - active_misconception: ein kohärentes, aber falsches Modell ist aktiv

    Das `evidence`-Feld muss aus der Antwort der Studierenden zitieren oder
    paraphrasieren. Das `content`-Feld muss konkreter Text sein, den du dieser
    Studierenden sagen würdest, nicht generische Ratschläge."""

    prompt_editor = mo.ui.text_area(
        value=starter_prompt,
        rows=14,
        label="System-Prompt (deine Spec Card)",
        full_width=True,
    )
    prompt_editor
    return (prompt_editor,)


@app.cell
def _run_button(mo):
    run_button = mo.ui.run_button(label="Diagnose ausführen", kind="success")
    run_button
    return (run_button,)


@app.cell
def _api_call(
    DiagnosticResult,
    anthropic,
    mo,
    os,
    prompt_editor,
    response_picker,
    run_button,
):
    # ---------- Schritt 4: Der API-Aufruf ----------
    # Claude Haiku 4.5 mit erzwungenem Tool-Use, damit das Modell *muss*
    # ein gültiges DiagnosticResult zurückgeben.

    mo.stop(not run_button.value, mo.md("_Drücke den Button oben, um die Diagnose auszuführen._"))
    mo.stop(not os.getenv("ANTHROPIC_API_KEY"),
            mo.md("**ANTHROPIC_API_KEY** ist nicht gesetzt. Setze ihn in `.env` oder als HF-Space-Secret."))

    client = anthropic.Anthropic()
    tool = {
        "name": "report_diagnostic",
        "description": "Liefere die kognitive Diagnose und Intervention.",
        "input_schema": DiagnosticResult.model_json_schema(),
    }

    message = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001"),
        max_tokens=2048,
        system=prompt_editor.value,
        tools=[tool],
        tool_choice={"type": "tool", "name": "report_diagnostic"},
        messages=[{"role": "user", "content": response_picker.value["text"]}],
    )

    tool_use = next(b for b in message.content if b.type == "tool_use")
    result = DiagnosticResult.model_validate(tool_use.input)
    return (result,)


@app.cell
def _show_result(mo, result):
    # ---------- Schritt 5: Validiertes Ergebnis ----------
    d, r = result.diagnosis, result.response
    mo.md(
        f"""
        ### Diagnose

        | Feld | Wert |
        | --- | --- |
        | `load_signal` | `{d.load_signal}` |
        | `severity` | `{d.severity}` |
        | `evidence` | {d.evidence} |
        | `domain_notes` | {d.domain_notes} |

        ### Intervention

        | Feld | Wert |
        | --- | --- |
        | `intervention` | `{r.intervention}` |
        | `content` | {r.content} |
        """
    )
    return


@app.cell
def _portable_prompt(DiagnosticResult, mo, prompt_editor):
    # ---------- Schritt 6: Portabler Prompt ----------
    # Dieselbe Spec Card, aber als Text formatiert, den du in Copilot,
    # ChatGPT oder Claude.ai einfügen kannst.

    schema = DiagnosticResult.model_json_schema()
    portable = f"""# Portabler Prompt

    Du bist eine Lehrperson, die eine schriftliche Studierendenantwort analysiert.
    Antworte AUSSCHLIESSLICH als JSON-Objekt in der unten angegebenen Form. Keine
    Prosa um das JSON.

    ## System

    {prompt_editor.value.strip()}

    ## Erwartete JSON-Struktur

    ```json
    {{
      "diagnosis": {{
    "load_signal": "<intrinsic_overload | extrinsic_distractor | germane_disengagement | schema_gap | active_misconception>",
    "evidence": "<kurzes Zitat aus der Antwort>",
    "severity": "<mild | moderate | fundamental>",
    "domain_notes": "<1-2 Sätze disziplinspezifischer Beobachtungen>"
      }},
      "response": {{
    "intervention": "<segment_intrinsic_load | reduce_extrinsic_load | prompt_germane_processing | activate_prior_schema | replace_misconception>",
    "content": "<konkreter Text für die Studierenden>"
      }}
    }}
    ```

    ## Studierendenantwort

    <<hier einfügen>>
    """
    mo.md(f"```\n{portable}\n```")
    return


if __name__ == "__main__":
    app.run()
