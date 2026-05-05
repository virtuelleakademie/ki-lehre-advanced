---
title: Diagnostic Tool Shell
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
license: cc0-1.0
---

# Diagnostic Tool Shell

A workshop tool. Takes a student response and returns a CLT-grounded
diagnosis plus a targeted intervention. The output schema is fixed: it IS
the cognitive-load-theory taxonomy.

Built for the BFH Virtual Academy workshop **KI in der Lehre: Advanced**.

## What workshop participants do

Participants iterate the **system prompt** to apply the fixed schema in
their discipline. They never edit code, never change the schema, and never
deploy anything themselves. They leave with two artifacts:

- A configured tool URL (system prompt encoded in the URL state)
- A portable prompt recipe they paste into Copilot, ChatGPT, or Claude

## Fixed schema

**load_signal** (the diagnostic categories, all CLT-grounded):

- `intrinsic_overload`: too much element interactivity for the learner's current schema
- `extrinsic_distractor`: irrelevant complexity in material or task design
- `germane_disengagement`: going through motions without effortful processing
- `schema_gap`: relevant prior knowledge is missing
- `active_misconception`: a wrong schema is in place and being applied

**intervention** (response strategies):

- `segment_intrinsic_load`
- `reduce_extrinsic_load`
- `prompt_germane_processing`
- `activate_prior_schema`
- `replace_misconception`

**severity**: `mild`, `moderate`, `fundamental`

## Local development

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
python app.py
```

Optionally set `ANTHROPIC_MODEL` to override the default
(`claude-haiku-4-5-20251001`).

## Deploying to Hugging Face Spaces

1. Create a new Space, SDK = Gradio, hardware = CPU basic.
2. Push this directory's contents to the Space's git remote.
3. In Space settings, add `ANTHROPIC_API_KEY` as a secret.

## Structure

- `app.py`: Gradio surfaces (system prompt editor, test pane, export)
- `models.py`: fixed Pydantic schema (Diagnosis, Response, DiagnosticResult)
- `scenarios.json`: discipline scenarios with three calibrated student responses each
- `requirements.txt`: Python dependencies
