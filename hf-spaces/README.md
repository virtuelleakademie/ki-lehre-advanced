# HuggingFace Spaces deployments

Active tool used by Block 3 of the workshop.

## diagnostic-tool-spec

The current Block-3 tool. A marimo app that takes a German markdown teaching-task spec and a student's answer, then calls the Anthropic API with `output_config.format` (via the SDK's Pydantic-aware `messages.parse()` helper) to constrain the response to the `DiagnosticResponse` schema. Returns which Skills the answer demonstrates, which are missing, which Misconceptions it exhibits, and evidence quotes.

See [diagnostic-tool-spec/README.md](diagnostic-tool-spec/README.md) for local development and deployment details.

## Archived tools

Earlier iterations live under [archive/hf-spaces-legacy/](../archive/hf-spaces-legacy/):

- **diagnostic-tool-shell** — Gradio shell from the previous iteration. Used forced `tool_use` for structured output. Stays deployed as a legacy HF Space; source archived here.
- **diagnostic-tool-shell-marimo** — marimo notebook variant of diagnostic-tool-shell. Same forced `tool_use` mechanism.
- **worked-example-weaver** / **worked-example-weaver-app** — earlier personalized-worked-example tools (marimo and Gradio). Not part of the current workshop flow.
