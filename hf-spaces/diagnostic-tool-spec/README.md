---
title: Diagnostic Workshop Tool
emoji: 🔬
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
license: cc0-1.0
---

# diagnostic-tool-spec

A marimo app that takes a German markdown teaching-task spec and a student's answer, then calls the Anthropic API with a Pydantic schema constraint to produce a structured diagnosis: which Skills the answer demonstrates, which are missing, which Misconceptions it exhibits, with evidence quotes.

Used in Block 3 of the BFH workshop "KI in der Lehre: Advanced" as an iframe-embedded interactive demo.

## Architecture

The pipeline:

- `spec_parser.parse_spec()` converts the markdown spec into a three-field `Spec` Pydantic object.
- `agent.diagnose(spec, answer)` calls the Anthropic API with the spec content and the student answer, using the SDK's `messages.parse()` helper (which sends the `DiagnosticResponse` Pydantic schema via `output_config.format`) to constrain the model's output to that schema.
- The marimo UI displays the five fields of the diagnosis.

The Pydantic schema is the "Output bedürfnissgemäss einschränken" mechanism (the workshop's learning objective).

## Local development

```bash
cd hf-spaces/diagnostic-tool-spec
uv sync
cp .env.example .env  # then add your ANTHROPIC_API_KEY
uv run pytest
uv run marimo run app.py
```

## Deployment

This sub-project deploys to a HuggingFace Space. The Space is a separate git repo; deployment is a `git push` from a Space clone to which the sub-project files are copied. See the implementation plan at `notes/2026-05-12-diagnostic-tool-plan.md` for the deployment steps.

The `ANTHROPIC_API_KEY` is configured as a Space secret in the HF Space settings (not committed).
