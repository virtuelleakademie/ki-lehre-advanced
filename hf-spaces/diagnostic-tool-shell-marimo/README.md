---
title: Diagnostic Tool Shell (Marimo, Tier 3)
emoji: 📓
colorFrom: indigo
colorTo: pink
sdk: docker
app_file: notebook.py
pinned: false
license: cc0-1.0
---

# Diagnostic Tool Shell (Marimo, Tier-3 Demonstration)

Companion to the Gradio shell at `hf-spaces/diagnostic-tool-shell/`. Same
Pydantic schema, same Anthropic API call. The difference: this version is a
marimo notebook, with each step of the data flow exposed as a separate cell.

Used as the **tier-3 demonstration in Block 3** of the workshop "KI in der
Lehre Advanced." The aim is to make legible how a Spec Card compiles into a
structured-output API call, by walking through the cells live.

## What the cells show

1. Pydantic schema — the structure the model must return
2. Scenario loading — the calibrated student responses from `scenarios.json`
3. UI to pick scenario and calibrated response
4. Editable system prompt (the Spec Card as text)
5. Anthropic API call with forced tool-use, enforcing the schema
6. Validated `DiagnosticResult` rendered as cards
7. Live preview of the portable prompt for use in any other LLM

## Run locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."

marimo edit notebook.py        # editable mode, code visible
marimo run notebook.py         # tool mode, code hidden
```

## Deploying as a Hugging Face Space

Use the docker SDK; provide a small Dockerfile that installs requirements and
runs `marimo run notebook.py --port 7860 --host 0.0.0.0`. Set
`ANTHROPIC_API_KEY` as a Space secret.

## Why marimo and not Gradio for this tier

Gradio hides the implementation behind a polished UI. Marimo interleaves code
and output cell by cell. For a workshop block whose goal is to make the
spec-to-prompt-to-API flow legible, marimo is structurally better suited.
The Gradio shell remains live as a fallback deployment for participants who
prefer a finished tool over a notebook view.
