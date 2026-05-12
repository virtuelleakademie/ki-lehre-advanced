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

A marimo app that takes a German markdown teaching-task spec and a student's answer, then calls the Anthropic API with a Pydantic schema constraint to produce a structured diagnosis: which Skills the answer demonstrates, which are missing, which Misconceptions it exhibits, with evidence quotes. The UI exposes the full pipeline (parsed spec, prompts sent to the API, JSON schema, structured response) so participants can see what schema-constrained output means at each step.

Used in Block 3 of the BFH workshop "KI in der Lehre: Advanced" as an iframe-embedded interactive demo.

## Architecture

The pipeline, surfaced as four visible stages in the marimo UI:

- **Stage 1: Input.** Two text areas for the markdown spec and the student answer, plus a "Beispiel laden" button that fills both with the Statistik-II multiple-regression example from Block 1.
- **Stage 2: Parsing.** `spec_parser.parse_spec()` converts the markdown spec into a three-field `Spec` Pydantic object (`lernaufgabe`, `skills_and_knowledge`, `misconceptions`). The UI shows the parsed object so participants can verify the markdown→object mapping.
- **Stage 3: API call.** `agent.diagnose_with_meta(spec, answer)` calls the Anthropic API via the SDK's `messages.parse()` helper. The UI shows the verbatim system prompt (`agent.SYSTEM_PROMPT`), the rendered user prompt (`agent.build_user_prompt`), and the `DiagnosticResponse` Pydantic schema (friendly field list plus raw JSON schema).
- **Stage 4: Response.** The five fields of the structured response (skills present, skills missing, misconceptions detected, evidence, overall assessment), each labelled as a Pydantic field, with model name and round-trip latency above.

The Pydantic schema is the "Output bedürfnissgemäss einschränken" mechanism (the workshop's learning objective).

## Local development

From the sub-project directory:

```bash
cd hf-spaces/diagnostic-tool-spec
uv sync                       # install deps into a local .venv
cp .env.example .env          # then paste a real ANTHROPIC_API_KEY into .env
uv run pytest                 # 13 unit tests, no API calls
uv run marimo run app.py      # serves at http://localhost:2718
```

End-to-end smoke test: open the URL, click **Beispiel laden**, then **Diagnose erstellen**. All four UI stages should render and Stage 4 should show a German diagnosis with `model` and `latency` in the metadata strip above the cards.

Environment variables read at startup:

- `ANTHROPIC_API_KEY` (required): your Anthropic API key.
- `WORKSHOP_TOOL_MODEL` (optional, default `claude-sonnet-4-6`): the model passed to `messages.parse()`.

## Deployment to Hugging Face Spaces

This sub-project is deployed as a Docker-SDK Space. The Space repository is separate from the workshop repo: deployment copies the contents of this directory into a Space clone, then `git push`es to Hugging Face. The Space's `README.md` YAML front matter (at the top of this file) is what Hugging Face reads to configure the Space.

### Prerequisites

- A Hugging Face account with write access (the deployed target in this project is `huggingface.co/spaces/awellis/diagnostic-tool-spec`).
- The `hf` CLI installed (`uv tool install huggingface_hub[cli]` or via the project's environment).
- A working local checkout of this sub-project (`uv run pytest` green, `uv run marimo run app.py` produces a diagnosis end-to-end).

### One-time setup

Authenticate the CLI with a token that has write access to the target Space:

```bash
hf auth login                 # paste a write-scope token
hf whoami                     # confirm the active user
```

Create the Space (once). Either via the web UI at `huggingface.co/new-space` (SDK: **Docker**, hardware: **CPU basic**, visibility: **Public**) or via CLI:

```bash
hf repos create diagnostic-tool-spec \
  --repo-type space \
  --space-sdk docker \
  --flavor cpu-basic \
  --public
```

Add the API key. Either through the web UI (the Space's **Settings → Variables and secrets** page → add a secret named `ANTHROPIC_API_KEY`), or inline at create time by adding `--secrets ANTHROPIC_API_KEY=sk-ant-...` to the command above. Optionally also set `WORKSHOP_TOOL_MODEL` as a (non-secret) variable to override the default model — via the UI or via `--env WORKSHOP_TOOL_MODEL=claude-sonnet-4-6`.

### Deploy (each release)

Clone the Space into a sibling directory of the workshop repo, mirror this sub-project's contents into the clone, then push:

```bash
# 1. Clone the Space (do this once, then reuse the clone)
cd ~/GitHub
git clone https://huggingface.co/spaces/awellis/diagnostic-tool-spec hf-space-diagnostic-tool-spec

# 2. Mirror this sub-project's tracked files into the clone
cd hf-space-diagnostic-tool-spec
rsync -av --delete \
  --exclude='.git' --exclude='.venv' --exclude='.env' \
  --exclude='__pycache__' --exclude='.pytest_cache' \
  ~/GitHub/sites/ki-in-der-lehre/ki-lehre-advanced/hf-spaces/diagnostic-tool-spec/ ./

# 3. Commit and push
git add .
git commit -m "Deploy diagnostic-tool-spec"
git push origin main
```

Hugging Face builds the Docker image automatically. The first build takes ~5 minutes; watch progress in the **Logs** tab on the Space page. Subsequent builds reuse cached layers and are faster.

### Verify the deployed Space

```bash
curl -sI https://awellis-diagnostic-tool-spec.hf.space | head -1
```

Expected: `HTTP/2 200`. Then open the URL in a browser and run the **Beispiel laden → Diagnose erstellen** smoke test from the local-dev section.

### Wire the workshop iframe

After the first successful deploy, update [`workshop/block-3-multi-tool/tool.qmd`](../../workshop/block-3-multi-tool/tool.qmd) so the `<iframe src=...>` points at the deployed Space URL (currently a placeholder), re-render Quarto, and commit. This step is needed only once unless the Space URL changes.
