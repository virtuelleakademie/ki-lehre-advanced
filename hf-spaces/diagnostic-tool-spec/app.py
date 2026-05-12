"""Marimo app entry point for the diagnostic workshop tool.

This file lives at the sub-project root because HF Spaces marimo convention
expects `app.py`. Run locally with:
    cd hf-spaces/diagnostic-tool-spec && uv run marimo run app.py

The UI is organised into five visible stages (intro, input, parsed spec,
API call, structured response) so a workshop participant can see what
"schema-constrained output" looks like at each step of the pipeline.
"""

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import json

    import marimo as mo

    from workshop_tool.agent import (
        MODEL,
        SYSTEM_PROMPT,
        build_user_prompt,
        diagnose_with_meta,
    )
    from workshop_tool.examples import EXAMPLE_SPEC_MD, EXAMPLE_STUDENT_ANSWER
    from workshop_tool.models import DiagnosticResponse
    from workshop_tool.spec_parser import parse_spec

    return (
        DiagnosticResponse,
        EXAMPLE_SPEC_MD,
        EXAMPLE_STUDENT_ANSWER,
        MODEL,
        SYSTEM_PROMPT,
        build_user_prompt,
        diagnose_with_meta,
        json,
        mo,
        parse_spec,
    )


@app.cell
def _(mo):
    mo.md(
        """
        # Diagnostisches Werkzeug

        **Was dir dieses Werkzeug gibt:** eine strukturierte Diagnose einer
        Lernenden-Antwort durch die Brille deines eigenen Specs. Du beschreibst,
        welche Skills und Misconceptions in deiner Aufgabe relevant sind; das
        Werkzeug liest die Antwort durch dein Spec und zeigt, was demonstriert
        ist, was fehlt und welche Misconceptions sichtbar sind, jeweils mit
        Zitaten aus der Antwort als Evidenz.

        **Wozu das gut ist:** das Werkzeug ist ein Test deines Specs. Scharfer,
        spezifischer Output bedeutet, dass dein Spec an dieser Stelle gut
        spezifiziert war. Generischer Output bedeutet meist, dass dein Spec dort
        zu vage ist: schärfe es und lass es erneut laufen.

        Die Stufen unten machen die Pipeline sichtbar (Markdown parsen → an die
        API senden → strukturiert zurückbekommen), damit der Mechanismus
        *Output bedürfnissgemäss einschränken* an deinem eigenen Spec
        nachvollziehbar wird.

        Klick **Beispiel laden** und dann **Diagnose erstellen**, um zu starten.
        """
    )
    return


@app.cell
def _(mo):
    get_seed, set_seed = mo.state({"spec": "", "answer": ""})
    return get_seed, set_seed


@app.cell
def _(EXAMPLE_SPEC_MD, EXAMPLE_STUDENT_ANSWER, mo, set_seed):
    def _load_example(_value):
        set_seed({"spec": EXAMPLE_SPEC_MD, "answer": EXAMPLE_STUDENT_ANSWER})

    example_button = mo.ui.button(
        label="Beispiel laden",
        on_click=_load_example,
        kind="neutral",
        tooltip="Füllt beide Felder mit dem Statistik-Beispiel aus Block 1.",
    )
    return (example_button,)


@app.cell
def _(get_seed, mo):
    seed = get_seed()
    spec_input = mo.ui.text_area(
        value=seed["spec"],
        placeholder=(
            "## Lernaufgabe (Kontext und Ziel)\n"
            "Wortlaut, Rahmen, intendiertes Ergebnis.\n\n"
            "## Erforderliche Skills und Knowledge\n"
            "- Skill 1.\n"
            "- Skill 2.\n\n"
            "## Antizipierte Misconceptions\n"
            "- Misconception 1.\n"
        ),
        full_width=True,
        rows=18,
        label="**Markdown-Spec** (aus deinem Block-2-Spec-Sheet)",
    )
    answer_input = mo.ui.text_area(
        value=seed["answer"],
        placeholder="Antwort der Lernenden hier einfügen...",
        full_width=True,
        rows=18,
        label="**Antwort der Lernenden** (echt oder konstruiert)",
    )
    return answer_input, spec_input


@app.cell
def _(mo):
    diagnose_button = mo.ui.run_button(
        label="Diagnose erstellen",
        kind="success",
    )
    return (diagnose_button,)


@app.cell
def _(mo):
    mo.md("## Stufe 1: Eingabe")
    return


@app.cell
def _(answer_input, mo, spec_input):
    mo.hstack([spec_input, answer_input], widths="equal")
    return


@app.cell
def _(diagnose_button, example_button, mo):
    mo.hstack([example_button, diagnose_button], justify="start", gap=1)
    return


@app.cell
def _(diagnose_button, mo):
    mo.stop(
        not diagnose_button.value,
        mo.md(
            "*Spec und Antwort einfügen (oder Beispiel laden), dann auf "
            "**Diagnose erstellen** klicken. Die Pipeline-Stufen darunter werden "
            "erst nach dem Klick gefüllt.*"
        ),
    )
    return


@app.cell
def _(answer_input, mo, parse_spec, spec_input):
    mo.stop(not spec_input.value.strip(), mo.md("*Bitte einen Spec einfügen.*"))
    mo.stop(not answer_input.value.strip(), mo.md("*Bitte eine Antwort einfügen.*"))

    try:
        spec = parse_spec(spec_input.value)
    except ValueError as exc:
        mo.stop(
            True,
            mo.vstack([
                mo.md("## Stufe 2: Markdown wird zu strukturierten Daten"),
                mo.callout(
                    mo.md(
                        f"**Spec-Parsing fehlgeschlagen:** {exc}\n\n"
                        "Der Parser sucht drei Level-2-Überschriften: "
                        "`## Lernaufgabe (Kontext und Ziel)`, "
                        "`## Erforderliche Skills und Knowledge`, "
                        "`## Antizipierte Misconceptions`. Prüfe deine Überschriften."
                    ),
                    kind="danger",
                ),
            ]),
        )
    return (spec,)


@app.cell
def _(mo, spec):
    def _bullets(items):
        if not items:
            return "*(keine)*"
        return "\n".join(f"- {item}" for item in items)

    mo.vstack([
        mo.md("## Stufe 2: Markdown wird zu strukturierten Daten"),
        mo.md(
            "*Dein Markdown wurde von `parse_spec()` in ein `Spec`-Pydantic-Objekt "
            "mit drei Feldern überführt. Falls hier ein Eintrag fehlt oder falsch "
            "zugeordnet ist, hat das Markdown-Format das Parsing verwirrt.*"
        ),
        mo.callout(
            mo.md(
                f"**`lernaufgabe`** *(str)*\n\n{spec.lernaufgabe}\n\n"
                f"**`skills_and_knowledge`** *(list[str], {len(spec.skills_and_knowledge)} Einträge)*\n\n"
                f"{_bullets(spec.skills_and_knowledge)}\n\n"
                f"**`misconceptions`** *(list[str], {len(spec.misconceptions)} Einträge)*\n\n"
                f"{_bullets(spec.misconceptions)}"
            ),
            kind="info",
        ),
    ])
    return


@app.cell
def _(
    DiagnosticResponse,
    SYSTEM_PROMPT,
    answer_input,
    build_user_prompt,
    json,
    mo,
    spec,
):
    user_prompt = build_user_prompt(spec, answer_input.value)

    def _field_lines(model):
        rows = []
        for name, info in model.model_fields.items():
            annotation = info.annotation
            type_label = getattr(annotation, "__name__", None) or str(annotation)
            description = (info.description or "").strip()
            rows.append(
                f"- **`{name}`** *({type_label})* — {description}"
                if description
                else f"- **`{name}`** *({type_label})*"
            )
        return "\n".join(rows)

    schema_fields_md = _field_lines(DiagnosticResponse)
    schema_json = json.dumps(DiagnosticResponse.model_json_schema(), indent=2)

    mo.vstack([
        mo.md("## Stufe 3: Was an die API gesendet wird"),
        mo.md(
            "*Klick die Abschnitte auf. Du siehst den exakten Text, der an die "
            "Anthropic-API geht, plus das Pydantic-Schema, das die Form der "
            "Antwort erzwingt.*"
        ),
        mo.accordion({
            "System Prompt": mo.md(f"```text\n{SYSTEM_PROMPT}\n```"),
            "User Prompt (Spec + Antwort)": mo.md(
                f"```text\n{user_prompt}\n```"
            ),
            "Pydantic-Schema (`DiagnosticResponse`)": mo.vstack([
                mo.md(
                    "Die Felder, die das Modell zurückgeben muss:\n\n"
                    f"{schema_fields_md}"
                ),
                mo.accordion({
                    "JSON-Schema (Rohformat)": mo.md(
                        f"```json\n{schema_json}\n```"
                    ),
                }),
            ]),
        }),
    ])
    return


@app.cell
def _(answer_input, diagnose_with_meta, mo, spec):
    with mo.status.spinner("Diagnose wird erstellt..."):
        result = diagnose_with_meta(spec, answer_input.value)
    return (result,)


@app.cell
def _(mo, result):
    def _bullets_or_none(items):
        if not items:
            return "*(keine)*"
        return "\n".join(f"- {item}" for item in items)

    diagnosis = result.response
    meta_bits = [f"Modell: `{result.model}`", f"Latenz: {result.latency_seconds:.1f} s"]
    if result.input_tokens is not None and result.output_tokens is not None:
        meta_bits.append(
            f"Tokens: {result.input_tokens} in, {result.output_tokens} out"
        )
    meta_strip = "  ·  ".join(meta_bits)

    mo.vstack([
        mo.md("## Stufe 4: Strukturierte Antwort"),
        mo.md(
            "*Jedes der folgenden Felder wurde vom Modell befüllt und entspricht "
            "exakt dem Pydantic-Schema aus Stufe 3. Vergleiche jedes Feld mit "
            "deiner Erwartung: generischer Output an einer Stelle bedeutet meist, "
            "dass dein Spec dort zu vage ist.*"
        ),
        mo.md(f"<small>{meta_strip}</small>"),
        mo.md(f"**Gesamteindruck:** {diagnosis.overall_assessment}"),
        mo.callout(
            mo.md(f"### Skills demonstriert\n{_bullets_or_none(diagnosis.skills_present)}"),
            kind="success",
        ),
        mo.callout(
            mo.md(f"### Skills fehlen\n{_bullets_or_none(diagnosis.skills_missing)}"),
            kind="warn",
        ),
        mo.callout(
            mo.md(
                "### Misconceptions erkannt\n"
                f"{_bullets_or_none(diagnosis.misconceptions_detected)}"
            ),
            kind="danger",
        ),
        mo.md(f"### Evidenz\n{_bullets_or_none(diagnosis.evidence)}"),
    ])
    return


if __name__ == "__main__":
    app.run()
