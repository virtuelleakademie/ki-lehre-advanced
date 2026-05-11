"""Marimo app entry point for the diagnostic workshop tool.

This file lives at the sub-project root because HF Spaces marimo convention
expects `app.py`. Run locally with:
    cd hf-spaces/diagnostic-tool-spec && uv run marimo run app.py
"""

import marimo

__generated_with = "0.19.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    from workshop_tool.agent import diagnose
    from workshop_tool.spec_parser import parse_spec

    return diagnose, mo, parse_spec


@app.cell
def _(mo):
    mo.md(
        """
        # Diagnostisches Werkzeug

        Füge dein Markdown-Spec links ein. Füge die Antwort einer Studentin
        rechts ein. Das Werkzeug ruft die Anthropic-API mit einem
        Pydantic-Schema-Constraint auf und gibt eine strukturierte Diagnose
        zurück.
        """
    )
    return


@app.cell
def _(mo):
    spec_input = mo.ui.text_area(
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
        rows=15,
        label="Markdown-Spec",
    )
    answer_input = mo.ui.text_area(
        placeholder="Antwort der Studentin hier einfügen...",
        full_width=True,
        rows=15,
        label="Antwort der Studentin",
    )
    diagnose_button = mo.ui.run_button(label="Diagnose erstellen")
    mo.hstack([spec_input, answer_input], widths="equal")
    return answer_input, diagnose_button, spec_input


@app.cell
def _(diagnose_button, mo):
    diagnose_button
    return


@app.cell
def _(answer_input, diagnose, diagnose_button, mo, parse_spec, spec_input):
    mo.stop(
        not diagnose_button.value,
        mo.md("*Spec und Antwort einfügen, dann auf 'Diagnose erstellen' klicken.*"),
    )
    mo.stop(not spec_input.value.strip(), mo.md("*Bitte einen Spec einfügen.*"))
    mo.stop(not answer_input.value.strip(), mo.md("*Bitte eine Antwort einfügen.*"))

    try:
        spec = parse_spec(spec_input.value)
    except ValueError as exc:
        mo.stop(
            True,
            mo.callout(mo.md(f"**Spec-Parsing fehlgeschlagen:** {exc}"), kind="danger"),
        )

    with mo.status.spinner("Diagnose wird erstellt..."):
        result = diagnose(spec, answer_input.value)

    def _list_or_none(items: list[str]) -> str:
        if not items:
            return "*(keine)*"
        return "\n".join(f"- {item}" for item in items)

    mo.vstack([
        mo.md("## Diagnose"),
        mo.md(f"**Gesamteindruck:** {result.overall_assessment}"),
        mo.callout(
            mo.md(f"### Skills demonstriert\n{_list_or_none(result.skills_present)}"),
            kind="success",
        ),
        mo.callout(
            mo.md(f"### Skills fehlen\n{_list_or_none(result.skills_missing)}"),
            kind="warn",
        ),
        mo.callout(
            mo.md(f"### Misconceptions erkannt\n{_list_or_none(result.misconceptions_detected)}"),
            kind="danger",
        ),
        mo.md(f"### Evidenz\n{_list_or_none(result.evidence)}"),
    ])
    return


if __name__ == "__main__":
    app.run()
