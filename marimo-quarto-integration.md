# Marimo + Quarto Integration Guide

## Overview

This project integrates **marimo** (reactive Python notebooks) with **Quarto** (publishing system) using the **quarto-marimo extension**. This gives us the best of both worlds:

- **Marimo's interactivity**: Reactive cells, UI elements, reproducible execution
- **Quarto's publishing**: Beautiful websites, custom callouts, multi-format output

## ⚠️ Critical Limitation: Islands Are Isolated

**Each marimo code block in Quarto runs in isolation.** Variables defined in one `{.marimo}` block are NOT available in other blocks.

**This won't work:**
```markdown
\`\`\`python {.marimo}
slider = mo.ui.slider(1, 10)
\`\`\`

\`\`\`python {.marimo}
# ERROR: NameError - 'slider' is undefined!
mo.md(f"Value: {slider.value}")
\`\`\`
```

**Solution:** Keep all related code in a single marimo island, or use a full marimo notebook for multi-cell reactivity.

## How It Works

### Marimo Islands

The quarto-marimo extension uses a technique called "marimo islands" where interactive Python code cells are embedded directly into Quarto documents (`.qmd` files) alongside regular markdown content.

```markdown
---
title: "My Interactive Tutorial"
filters:
  - marimo-team/marimo
external-env: true
---

## Introduction

Some explanatory text here.

\`\`\`{.marimo}
#| echo: true
#| editor: true

import marimo as mo
slider = mo.ui.slider(1, 10, label="Value")
slider
\`\`\`

The slider is interactive in the browser!
```

## Architecture

### Extension Installation

The extension is already installed at:
```
_extensions/marimo-team/marimo/
```

Files:
- `marimo-execute.lua`: Pandoc filter that intercepts `{.marimo}` blocks
- `extract.py`: Python script that executes marimo code
- `_extension.yml`: Configuration (v0.4.3)

### Execution Pipeline

1. Quarto finds code blocks with `{.marimo}` class
2. Lua filter extracts these blocks
3. Python script (`extract.py`) executes code using `MarimoIslandGenerator`
4. For HTML: Outputs interactive WASM islands
5. For PDF: Extracts static outputs (images, text)

### Environment Management

Two modes:

**1. Sandboxed (Default)**
```yaml
pyproject: |
  [project]
  dependencies = ["openai", "pydantic"]
```
Creates isolated `uv` environment per notebook.

**2. External Environment (Our Choice)**
```yaml
external-env: true
```
Uses the existing `.venv` directory with all project dependencies.

## Development Workflows

### Workflow A: Marimo-First (Recommended for Complex Interactions)

**Best for**: Modules with lots of interactivity and UI elements

```bash
# 1. Develop in marimo
marimo edit workshop/01-new-module/notebook.py

# Test interactivity, refine UI
# Save when satisfied

# 2. Export to .qmd
source .venv/bin/activate
marimo export md workshop/01-new-module/notebook.py -o workshop/01-new-module/index-temp.qmd

# 3. Refine the .qmd manually:
#    - Add German text between sections
#    - Insert custom callouts (:::{.callout-try})
#    - Configure cell editability
#    - Add front matter

# 4. Preview
quarto preview

# 5. Cleanup
rm workshop/01-new-module/index-temp.qmd
```

**Example refinements:**
- Change `#| editor: false` for demo cells
- Change `#| editor: true` for practice cells
- Add `:::{.callout-reflect}` before complex sections
- Translate English to German
- Add pedagogical context

### Workflow B: Quarto-First (Recommended for Documentation-Heavy Content)

**Best for**: Content with lots of explanation and minimal interactivity

```bash
# 1. Create .qmd directly
vim workshop/02-new-topic/index.qmd

# 2. Add front matter
# ---
# title: "Topic Title"
# filters:
#   - marimo-team/marimo
# external-env: true
# ---

# 3. Write content with embedded marimo cells
# Use {.marimo} code blocks

# 4. Preview
quarto preview

# Optional: Open .qmd in marimo for testing
marimo edit workshop/02-new-topic/index.qmd
```

**Unique feature**: You can open `.qmd` files directly in marimo! This enables round-trip editing.

## Cell Configuration

### Front Matter (Document Level)

```yaml
---
title: "Module Title"
subtitle: "Description"
filters:
  - marimo-team/marimo  # Required!
external-env: true       # Use project .venv
---
```

### Cell Options

```python
{.marimo}
#| echo: true       # Show source code
#| editor: true     # Allow editing in browser
#| eval: true       # Execute the code
#| output: true     # Show output
```

**Common patterns:**

**Demo/Explanation Cells** (read-only):
```python
{.marimo}
#| echo: true
#| editor: false

# Code students observe but don't edit
```

**Practice Cells** (editable):
```python
{.marimo}
#| echo: true
#| editor: true

# Code students can modify and experiment with
```

**Setup Cells** (hidden):
```python
{.marimo}
#| echo: false
#| editor: false

# Imports and setup, hidden from students
```

## Integration with Custom Callouts

Marimo islands work seamlessly with Quarto's custom callouts:

```markdown
::: {.callout-try}
## Ausprobieren

Try modifying the slider value!
:::

\`\`\`{.marimo}
#| editor: true

import marimo as mo
slider = mo.ui.slider(1, 10)
slider
\`\`\`

::: {.callout-reflect}
## Reflection

What happened when you changed the value?
:::
```

All 20+ custom callouts defined in `_quarto.yml` work with marimo islands.

## Project Structure

### Current Setup

```
workshop/
├── 00-setup/
│   ├── marimo-intro.py      # Source (develop here)
│   └── index.qmd             # Published page (embeds + text)
├── 01-retrieval-practice/
│   ├── retrieval-practice-generator.py
│   └── index.qmd
└── [legacy content...]

exercises/
├── exercise-01/
│   ├── socratic-tutor-starter.py      # Starter template
│   ├── socratic-tutor-solution.py     # Reference solution
│   └── index.qmd                       # Exercise description
```

### File Patterns

**Source Files** (.py):
- Stored as pure Python
- Edit in marimo: `marimo edit file.py`
- Version controlled easily
- Full marimo features

**Published Files** (.qmd):
- Embed marimo code as islands
- Add explanatory text
- Include custom callouts
- Render to HTML: `quarto render`

## Navigation Setup

In `_quarto.yml`:

```yaml
sidebar:
  - title: "Workshop"
    contents:
      - workshop/index.qmd
      - section: "Neue Module (Marimo-basiert)"
        contents:
          - workshop/00-setup/index.qmd
          - workshop/01-retrieval-practice/index.qmd
      - section: "Legacy Content"
        contents:
          - workshop/setup-openai/index.qmd
          # ...
```

## Benefits of This Approach

### 1. Pedagogical
- **Reactive execution**: Demonstrates cause-effect relationships
- **Immediate feedback**: Students see results instantly
- **Experimentation**: Safe environment to try changes

### 2. Technical
- **No server needed**: Runs entirely in browser via WASM
- **Git-friendly**: Source as Python, not JSON
- **Reproducible**: No hidden state or execution order issues
- **Maintainable**: Single source of truth

### 3. User Experience
- **Dual workflow**: Use in browser OR download and run locally
- **Progressive disclosure**: Hide complex code, show practice cells
- **Integrated**: Works with existing Quarto features

## Common Tasks

### Adding a New Module

```bash
# 1. Create marimo source
marimo edit workshop/03-new-module/module.py

# 2. Develop content (code + mo.md cells)

# 3. Export and refine
marimo export md workshop/03-new-module/module.py -o workshop/03-new-module/index.qmd
# Edit index.qmd to add German text and callouts

# 4. Add to _quarto.yml navigation

# 5. Render and test
quarto preview
```

### Converting Jupyter to Marimo

```bash
# 1. Convert notebook
marimo convert workshop/old-module/notebook.ipynb > workshop/old-module/converted.py

# 2. Refactor for reactivity
marimo edit workshop/old-module/converted.py
# Fix any cell dependencies, add UI elements

# 3. Export to .qmd
marimo export md workshop/old-module/converted.py -o workshop/old-module/index.qmd

# 4. Refine and test
```

### Testing Locally

**View in marimo editor**:
```bash
marimo edit workshop/module/notebook.py
```

**View as Quarto site**:
```bash
quarto preview
# Opens http://localhost:8800
```

**View specific page**:
```bash
quarto render workshop/module/index.qmd
# Output: docs/workshop/module/index.html
open docs/workshop/module/index.html
```

## Troubleshooting

### Issue: "marimo: command not found"

**Solution**: Activate virtual environment
```bash
source .venv/bin/activate
```

### Issue: API key errors during render

**Expected behavior**: Marimo cells will error during `quarto render` if they need API keys that aren't set. This is fine - the cells will execute interactively when users load the page in their browser with their own API keys.

**To suppress errors during development**:
Add error handling in cells:
```python
try:
    response = client.chat.completions.create(...)
except:
    mo.md("*API key not configured*")
```

### Issue: Cells not interactive in browser

**Check**:
1. Front matter includes `filters: - marimo-team/marimo`
2. Code blocks use `{.marimo}` not just `{python}`
3. `external-env: true` is set (or dependencies specified)

### Issue: Changes not showing in preview

**Solution**:
- Quarto caches by default (`freeze: auto`)
- Delete `_freeze/` directory to force re-render
- Or: `quarto render --no-cache`

### Issue: Import errors in marimo cells

**Solution**:
```bash
# Ensure package is installed
uv add <package>
uv sync

# Restart quarto preview
```

## Best Practices

### 1. Cell Organization

**Do**:
- One logical concept per cell
- Keep cells small and focused
- Use `mo.md()` for rich markdown output
- Group related variables in same cell

**Don't**:
- Put all code in one cell
- Create complex cross-cell dependencies
- Mutate objects across cells (marimo doesn't track mutations)

### 2. UI Elements

**Do**:
- Use `mo.ui` for interactive elements
- Label all inputs clearly
- Provide sensible defaults
- Use German labels for consistency

**Don't**:
- Overload with too many inputs
- Use English labels in German workshop
- Forget to display the UI element (must return or display it)

### 3. Editor Configuration

**Practice cells** (students edit):
```python
{.marimo}
#| echo: true
#| editor: true
```

**Demo cells** (show but don't edit):
```python
{.marimo}
#| echo: true
#| editor: false
```

**Setup cells** (hide completely):
```python
{.marimo}
#| echo: false
#| editor: false
```

### 4. Pedagogical Integration

**Always**:
- Explain WHY before showing code
- Use callouts to highlight key concepts
- Provide reflection prompts after interactions
- Connect to learning principles (Make it Stick)

**Pattern**:
```markdown
::: {.callout-reflect}
## Why this works
[Explanation of cognitive science principle]
:::

[Marimo cell with interactive demo]

::: {.callout-try}
## Your turn
[Practice prompt]
:::

[Marimo cell with editor: true]
```

## Migration Plan

### Completed
- ✅ Module 0: Setup & Marimo Introduction
- ✅ Module 1: Retrieval Practice Generator
- ✅ Exercise 1: Socratic Tutor

### Remaining
- ⏳ Module 2: Metacognitive Prompts
- ⏳ Module 3: Adaptive Difficulty
- ⏳ Exercise 2: Study Assistant
- ⏳ Exercise 3: Adaptive Practice System

### Legacy (Lower Priority)
- Jupyter: exploring-openai-models
- Jupyter: structured-output
- QMD: api-tricks (needs fixes)
- QMD: setup-openai, setup-colab

## Resources

- [Marimo Documentation](https://docs.marimo.io/)
- [Quarto Marimo Extension](https://github.com/marimo-team/quarto-marimo)
- [Make it Stick Principles](https://virtuelleakademie.github.io/ki-lehre-intermediate/03-lernumgebungen/)
- [Project CLAUDE.md](../CLAUDE.md)

## Questions?

Check `CLAUDE.md` for development commands and workflow patterns, or see the pedagogical prompt templates in `resources/prompt-templates/`.
