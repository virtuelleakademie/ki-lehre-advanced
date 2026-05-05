# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Files

- **CLAUDE.md** (this file) - Quick developer reference and commands
- **marimo-quarto-integration.md** - Detailed technical guide for marimo + Quarto integration
- **workshop-redesign-overview.md** - Comprehensive explanation of the workshop redesign
- **resources/prompt-templates/pedagogical-prompts.qmd** - 14 evidence-based prompt templates

## Project Overview

Educational website and workshop materials for the **KI in der Lehre: Advanced** workshop, the third in a three-workshop trilogy on AI in education at the BFH Virtuelle Akademie.

This 3-hour workshop has participants build a CLT-grounded **diagnostic AI tool** for their own discipline, **without writing code**. The output schema is fixed (it IS the cognitive-load-theory taxonomy: five `load_signal` and five `intervention` enum categories); participants iterate the system prompt against a hosted Gradio shell. They leave with a configured tool URL and a portable prompt recipe usable in Microsoft Copilot, ChatGPT, or Claude.

Built with Quarto, delivered in English, maintained by the Virtual Academy at Bern University of Applied Sciences (BFH). Published at https://virtuelleakademie.github.io/ki-lehre-advanced/

The marimo + PydanticAI iteration of this workshop has been moved to `archive/marimo-iteration/`. See `workshop-redesign-overview.md` for the redesign rationale.

## Development Commands

### Quarto Commands
```bash
quarto preview          # Live preview on port 8800
quarto render          # Build the entire site to docs/
quarto render <file>   # Render specific file
```

### Python Environment
```bash
source .venv/bin/activate    # Activate virtual environment
uv sync                      # Install/sync dependencies from pyproject.toml
uv add <package>            # Add new dependency
marimo edit <file.py>       # Open marimo notebook
```

### Git Workflow (Makefile)
```bash
make branch name=<name>     # Create feature branch from main
make commit msg="message"   # Stage and commit all changes
make push                   # Push current branch
make merge                  # Merge current branch into main (admin only)
make status                 # Show git status
make diff                   # Show word-level diff
```

## Architecture

### Content Organization

**Workshop Structure (3-hour workshop, English):**

- **workshop/index.qmd**: Main workshop overview, schedule, learning objectives
- **workshop/opening/**: Opening (10 min): think-pair-share on a misdiagnosis you remember
- **workshop/theory/**: Theory (30 min): the CLT-grounded diagnostic taxonomy (five `load_signal` and five `intervention` categories)
- **workshop/demo/**: Demo (15 min): walkthrough of the diagnostic shell on a calibrated nursing example
- **workshop/build/**: Build (115 min, includes break): the four CLT-anchored labs against the hosted shell
  - **workshop/build/scenarios/**: six discipline scenarios (nursing, education, business, social work, engineering, statistics), each with three calibrated student responses tagged to `load_signal` categories
- **workshop/extend/**: Extend (15 min): tool-vs-recipe and most-diagnostic-load-signal reflection
- **workshop/diskussion/**: Closing (5-10 min): one Monday commitment + the meta-lesson

**The Hosted Shell:**

- **hf-spaces/diagnostic-tool-shell/**: the Gradio app participants use during the Build block
  - `models.py`: fixed Pydantic schema (Diagnosis, Response, DiagnosticResult)
  - `app.py`: three surfaces (system prompt editor, test pane, export portable prompt). Uses Anthropic Claude Haiku 4.5 with structured output via tool-use.
  - `scenarios.json`: source of truth for the scenario pack (mirrored as .qmd files under workshop/build/scenarios/)
- **hf-spaces/worked-example-weaver-app/**: the older personalized-worked-example tool. Stays deployed and is linked from the closing as optional further exploration. Not used in the workshop's main flow.

**Supporting Directories:**

- **resources/**: Prompt templates library, supporting materials
- **tutorials/**: Optional local setup guides
- **slides/**: RevealJS presentations
- **assets/**: Images, PDFs, logos, backgrounds
- **docs/**: Build output (GitHub Pages, auto-generated). **Do not edit.**
- **archive/marimo-iteration/**: prior iteration of the workshop (marimo + PydanticAI). Not in the live render. See `archive/marimo-iteration/README.md` for context.

### Key Configuration Files

**_quarto.yml**: Main site configuration
- Preview port: 8800
- Output dir: docs/
- Defines navigation (navbar, sidebars)
- Configures custom callouts (20+ types for pedagogy)
- RevealJS settings for slides
- Execution directory: "project"
- Freeze: auto (caching enabled)

**_brand.yml**: Visual branding
- Colors, typography (Jura font)
- Brand identity elements

**pyproject.toml**: Python dependencies for any local marimo work that may still happen on this repo (not used by the main workshop flow).
- Package manager: uv
- Requires Python >=3.10

**hf-spaces/diagnostic-tool-shell/requirements.txt**: dependencies for the hosted shell (gradio, anthropic, pydantic, python-dotenv). Self-contained; not installed via the project venv.

**_metadata.yml files**: Per-directory defaults
- Located in exercises/, slides/, tutorials/, workshop/
- Define common format settings for that section

### Quarto Extensions

10+ custom extensions in _extensions/:
- **custom-callout**: Pedagogical callouts (activities, tips, timing)
- **timer**: Workshop timing components
- **pyodide**: Run Python in browser
- **flashcards**: Interactive learning cards
- **embedio**, **embedpdf**: Embed external content
- **qrcode**: Generate QR codes for links
- **reveal-header**: Custom RevealJS headers
- And more (fontawesome, bsicons, attribution, social-embeds, simplemenu)

### Custom Callouts

20+ specialized callout types for teaching (defined in _quarto.yml):
- **Activities**: `activity-individual`, `activity-pair`, `activity-group`, `activity-screens-down`, `activity-screens-up`
- **Learning**: `try`, `reflect`, `feedback`, `caution`, `pro-tip`
- **Technical**: `prompt-example`, `testing`, `export`
- **Workshop flow**: `setup`, `timing`, `break`, `checkpoint`, `schedule`

Use with: `:::{.callout-activity-individual}` in QMD files

### File Types

- **.qmd**: Quarto markdown (main content format)
- **.ipynb**: Jupyter notebooks (interactive tutorials)
- **.py**: Python scripts, marimo notebooks
- **.scss**: Custom styles in styles/

## Workflow Patterns

### Adding Content
1. Create/edit .qmd or .ipynb files in appropriate directory
2. Run `quarto preview` for live development
3. Auto-renders on save (editor.render-on-save: true)
4. Commit with `make commit msg="description"`

### Adding Python Dependencies
```bash
uv add <package>    # Adds to pyproject.toml and installs
uv sync            # Syncs all dependencies
```

### Working with Marimo + Quarto Integration

**Note**: The current workshop (diagnose-then-respond redesign) does **not** use marimo. The hosted Gradio shell at `hf-spaces/diagnostic-tool-shell/` is the only interactive surface participants encounter. The marimo + Quarto integration documented below is preserved because it remains a valid technique for OTHER content (and the archived marimo iteration uses it), but it is not exercised by the main workshop flow.

The project supports **marimo islands** - interactive Python cells embedded in Quarto documents.

#### Development Workflow (Option A: Marimo-First)
```bash
# 1. Create/edit marimo notebook
marimo edit workshop/module-name/notebook.py

# 2. Test interactivity in marimo editor

# 3. Export to .qmd
source .venv/bin/activate
marimo export md workshop/module-name/notebook.py -o workshop/module-name/index-temp.qmd

# 4. Refine the .qmd:
#    - Add German explanatory text
#    - Insert custom callouts
#    - Configure cell editability (#| editor: true/false)
#    - Add front matter with filters

# 5. Preview in Quarto
quarto preview
```

#### Development Workflow (Option B: Direct .qmd Editing)
```bash
# 1. Create .qmd with marimo code blocks
# 2. Add front matter:
#    ---
#    filters:
#      - marimo-team/marimo
#    external-env: true
#    ---
# 3. Use {.marimo} code blocks with configuration:
#    {.marimo}
#    #| echo: true
#    #| editor: true   # Make editable in browser
```

#### Marimo Cell Configuration
- `#| echo: true` - Show source code
- `#| editor: true` - Allow editing in browser (for practice)
- `#| editor: false` - Read-only (for demos)
- `external-env: true` - Use project .venv instead of isolated env

#### File Structure Pattern
```
workshop/01-module-name/
├── source-notebook.py    # Source of truth (edit in marimo)
├── index.qmd             # Quarto page (embeds islands + text)
└── images/               # Supporting files
```

#### Key Benefits
- **Reactive**: Changes propagate automatically
- **Interactive**: Students edit cells in browser
- **Git-friendly**: Source as Python files
- **Integrated**: Works with custom callouts

#### Editing Marimo Notebooks

**IMPORTANT**: When editing Marimo notebooks:

1. **Preferred Method - Use the marimo editor**:
   ```bash
   marimo edit path/to/notebook.py
   ```
   The editor handles validation and saves cells in the correct format automatically.

2. **If editing .py files directly**: Use Python syntax validation only:
   ```bash
   python3 -m py_compile path/to/notebook.py
   ```

3. **AVOID `marimo check` for programmatic edits**: The `marimo check` command triggers a linter that can convert properly formatted cells into unparsable format when editing files programmatically. Only use it for validation, not as part of automated workflows.

**Best Practice**: Add/edit cells using the marimo editor's UI (click + button) rather than editing the .py file directly. This ensures cells are saved in the format marimo expects.

### Publishing
1. Render: `quarto render` (outputs to docs/)
2. Push to main branch
3. GitHub Pages automatically deploys from docs/

## Important Context

- **License**: CC0 1.0 Universal (public domain)
- **Language**: English (workshop content and materials)
- **Bibliography**: Uses bibliography.bib and ai-for-research.bib
- **Search**: Navbar overlay search enabled
- **Comments**: Hypothesis integration for collaborative annotation
- **Main branch**: main

## Pedagogical Framework

This workshop is grounded in cognitive science principles from "Make it Stick" and educational research:

### Core Principles
1. **Active Retrieval** - Students recall information from memory (not re-reading)
2. **Desirable Difficulties** - Productive struggle that deepens understanding
3. **Distributed Practice** - Spacing learning over time
4. **Metacognition** - Reflection on one's own learning process
5. **Transfer** - Practice concepts in varied contexts
6. **AI as Scaffolding** - Tools support cognitive work, don't replace it

### Design Philosophy
**Critical**: AI tools should promote thinking, not give direct answers. The best educational AI tools:
- Create "desirable difficulties" that enhance learning
- Use Socratic questioning to guide discovery
- Provide formative feedback that promotes reflection
- Support retrieval practice over recognition
- Adapt to student needs while maintaining challenge

**Reference**: See https://virtuelleakademie.github.io/ki-lehre-intermediate/03-lernumgebungen/ for detailed pedagogical principles.

## Workshop Structure

**Building Diagnostic AI Tools, Grounded in Cognitive Load Theory** - A 3-hour workshop in which participants build a working diagnostic tool for their discipline without writing code.

### Learning Objectives

By the end of this workshop, participants will:

1. **Identify** five CLT-grounded diagnostic signals in student work
2. **Match** each diagnostic signal to a corresponding intervention strategy
3. **Write** a system prompt that instructs an LLM to apply those categories in their discipline
4. **Calibrate** the prompt against tagged student responses
5. **Produce** a portable prompt recipe usable in any LLM interface (Microsoft Copilot, ChatGPT, Claude.ai)

### Workshop Flow

| Block | Duration | What Participants Do |
|------|----------|---------------------|
| Opening | 10 min | Think-pair-share: a misdiagnosis you remember |
| Theory | 30 min | The five `load_signal` categories grounded in CLT and schema research |
| Demo | 15 min | Walkthrough of the shell on a calibrated nursing example |
| Build: Pick scenario | 10 min | Choose one of six discipline scenarios |
| Build: Lab 1 | 15 min | Domain examples of each load type |
| **Break** | 10 min | |
| Build: Lab 2 | 15 min | Map diagnosis to intervention |
| Build: Lab 3 | 25 min | Write the diagnostic system prompt for your discipline |
| Build: Lab 4 | 25 min | Test on calibrated responses, refine, export portable prompt |
| Build: Pair-test + gallery | 15 min | Run a partner's tool against your scenario |
| Extend | 15 min | Tool-vs-recipe and most-diagnostic-load-signal reflection |
| Closing | 5-10 min | One Monday commitment |

### Technical Stack

- **Anthropic Claude Haiku 4.5**: structured-output language model used by the diagnostic shell
- **Pydantic**: defines the fixed `Diagnosis` and `Response` schema
- **Gradio**: hosts the three-surface shell UI
- **HuggingFace Spaces**: free deployment platform

### The Fixed Schema (CLT Load Taxonomy)

The schema is the workshop's central object. Participants never edit it; they iterate the system prompt that uses it.

`load_signal` (diagnostic categories):

1. `intrinsic_overload`: too much element interactivity for the learner's current schema
2. `extrinsic_distractor`: irrelevant complexity in material or task design
3. `germane_disengagement`: going through motions without effortful processing
4. `schema_gap`: relevant prior knowledge is missing
5. `active_misconception`: a wrong schema is in place and being applied

`intervention` (response strategies, default mapping to load signals above):

1. `segment_intrinsic_load`
2. `reduce_extrinsic_load`
3. `prompt_germane_processing`
4. `activate_prior_schema`
5. `replace_misconception`

`severity`: `mild`, `moderate`, `fundamental`.

### Six Discipline Scenarios

Located at `workshop/build/scenarios/` and mirrored in `hf-spaces/diagnostic-tool-shell/scenarios.json`:

1. Nursing: Warfarin and INR
2. Education: Critique a quiz question
3. Business: Bakery pricing
4. Social work: Missed appointments
5. Engineering: Stale-data bug
6. Statistics: Interpreting r = 0.3

Each scenario provides three calibrated student responses tagged with the `load_signal` they exemplify, used as the answer key for Lab 4.

### Pedagogical Grounding

Based on **Cognitive Load Theory** [@swellerCognitiveLoadProblem1988] (with the updated germane-processing framing in Sweller, Ayres and Kalyuga 2019) and schema-acquisition research:

- **Three classical load types**: intrinsic, extraneous, germane (the latter reframed as germane *processing* in 2019)
- **Diagnostic taxonomy extension**: schema_gap and active_misconception add two distinct schema-acquisition failure modes (absent vs. wrong schema)
- **Workshop design principle**: theory provides structure (the fixed schema); practitioners provide cues (the system prompt)

## Notes for Development

### General

- Site renders from project root, not individual directories
- Freezing enabled: computed results cached in _freeze/
- Preview doesn't auto-open browser (browser: false in config)
- GitHub Pages deployment URL: https://virtuelleakademie.github.io/ki-lehre-advanced/
- Main branch is `main` (not master)
- **docs/ directory**: Contains generated HTML output - **DO NOT edit files here** (they get overwritten on render)

### Markdown Formatting

**IMPORTANT**: Always include a blank line before markdown lists. This ensures proper rendering in Quarto.

**Correct:**
```markdown
Here is some text.

- List item 1
- List item 2
```

**Incorrect:**
```markdown
Here is some text.
- List item 1
- List item 2
```

This applies to all list types (unordered `-`, ordered `1.`, and nested lists).

**Writing Style - Avoid Hyphens and Em-Dashes:**

Do not use hyphens (-) or em-dashes (—) as separators in content. Instead, use:

- **Colons** for list items with labels: `**Label:** Description here`
- **Parentheses** for clarifications: `Link text (additional context)`
- **Full sentences** when appropriate

**Correct:**
```markdown
- **Programming (Python):** For loops, list comprehensions, functions
- **Study the code:** Understand how structured outputs work
```

**Incorrect:**
```markdown
- **Programming (Python)** - For loops, list comprehensions, functions
- **Study the code** - Understand how structured outputs work
```
