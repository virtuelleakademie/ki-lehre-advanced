# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Files

- **CLAUDE.md** (this file): quick developer reference and commands
- **2026-05-06-advanced-workshop-design.md**: the design doc for the Spec Card workshop (the user's own theoretical design statement; current authoritative source for what the workshop is)
- **2026-05-06-spec-card-redesign.md**: implementation plan for the Spec Card design (load-bearing claims, vocabulary policy, file inventory, sequence)
- **2026-05-07-redesign-comparison.md**: side-by-side comparison of Redesign A (diagnostic-tool-shell) vs. Redesign B (Spec Card). Useful as the historical record of the design choice
- **instructor-notes/spec-card-statistics-internal.md**: the worked Statistics-Novice Spec Card in the internal-precise register (architectures named)
- **marimo-quarto-integration.md**: technical guide for marimo + Quarto. Not used by the current workshop's main flow; preserved because the integration remains valid for other content
- **resources/prompt-templates/pedagogical-prompts.qmd**: legacy prompt templates from earlier iterations

## Project Overview

Educational website and workshop materials for the **KI in der Lehre: Advanced** workshop, the third in a three-workshop trilogy on AI in education at the BFH Virtuelle Akademie.

This 3-hour workshop has participants build a **Spec Card**: a 6-section falsifiable specification of a learner in their own discipline. Participants then deploy the spec across four tools (Microsoft Copilot, HuggingChat, a Marimo notebook with structured outputs, a coding agent like Claude Code or pi.dev) and apply four diagnostic roles (clarity stress-test, intervention/observation mapper, misconception probe, performance-learning dissociation detector) to a real assignment from their teaching.

The workshop's central claim is that **AI substitution disables (rather than degrades) the metacognitive update**. Without the learner's first-order action, the second-order metacognitive computation does not run. This is the sharp, falsifiable form of the offloading-vs-outsourcing distinction the intermediate workshop establishes informally.

Built with Quarto, **delivered in German**, maintained by the Virtual Academy at Bern University of Applied Sciences (BFH). Published at https://virtuelleakademie.github.io/ki-lehre-advanced/

Two prior iterations of this workshop have been archived:
- `archive/marimo-iteration/` — the original PydanticAI + Marimo design
- `archive/diagnostic-shell-iteration/` — the simpler Gradio-based diagnostic-tool-shell design (English content)

See `2026-05-06-spec-card-redesign.md` and `2026-05-06-advanced-workshop-design.md` for the design rationale.

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

**Workshop Structure (3-hour workshop, German):**

- **vorbereitung/index.qmd**: pre-workshop reading (~30 min) + the worked Statistics-Novice spec card
- **workshop/index.qmd**: workshop overview, schedule, learning objectives
- **workshop/einstieg/**: Einstieg (10 min): curse-of-knowledge activator
- **workshop/block-1-performanz-lernen/**: Block 1 (35 min): two posteriors, Pearl's intervention vs. observation, action-as-input metacognitive update, performance vs. learning
- **workshop/block-2-spec-card/**: Block 2 (45 min): walkthrough of the worked spec card; participants build their own
  - **workshop/spec-card-statistics/**: the worked Statistics-Novice Spec Card (participant-facing, German)
  - **workshop/spec-card-template/**: fillable 6-section template
- **workshop/block-3-multi-tool/**: Block 3 (30 min): four-tier deployment spectrum
  - `index.qmd`: the block content
  - `copilot-template.md`: tier 1 (chat, BFH-licensed)
  - `huggingchat-template.md`: tier 2 (open-weight)
  - `coding-agent-walkthrough.md`: tier 4 (Claude Code or pi.dev)
- **workshop/block-4-diagnostische-rollen/**: Block 4 (35 min): the four diagnostic roles applied to participant's own assignment
- **workshop/closing/**: Closing (10 min): resource-rational analysis + one concrete commitment
- **workshop/build/scenarios/**: six discipline scenarios (nursing, education, business, social work, engineering, statistics) with three calibrated student responses each. Used in Block 4 as backup assignments and as the Role 3 misconception bank. (The directory name `build/` is a legacy from the previous iteration; the scenarios remain there to keep URLs stable.)

**The Hosted Tools:**

- **hf-spaces/diagnostic-tool-shell-marimo/**: marimo notebook for the **tier-3 demonstration in Block 3**. Same Pydantic schema and Anthropic API call as the Gradio shell, but laid out as reactive cells so the data flow is visible.
- **hf-spaces/diagnostic-tool-shell/**: the Gradio shell from the previous iteration. Stays live as a fallback deployment for participants who prefer a finished tool over a notebook view.
- **hf-spaces/worked-example-weaver-app/**: an older personalized-worked-example tool. Stays deployed. Not linked from the new workshop content.

**Reference / instructor notes:**

- **instructor-notes/spec-card-statistics-internal.md**: the Statistics-Novice Spec Card in the internal-precise register (Marr, ACT-R, Bayesian, Daw & Fleming, Pearl, conceptual change theory all named). For instructor audit; the participant-facing version is at `workshop/spec-card-statistics/`.

**Supporting Directories:**

- **resources/**: legacy prompt templates library
- **tutorials/**: optional local setup guides
- **slides/**: RevealJS presentations (legacy from prior iteration; need updating to match the new design)
- **assets/**: images, PDFs, logos, backgrounds
- **docs/**: build output (GitHub Pages, auto-generated). **Do not edit.**
- **archive/marimo-iteration/**: PydanticAI + Marimo iteration. Not rendered.
- **archive/diagnostic-shell-iteration/**: English-language diagnostic-tool-shell iteration. Not rendered.

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
- **Language**: German (workshop content and materials). Instructor notes and design docs are English. Variable names and code identifiers stay English (programming convention). Archived iterations (under `archive/`) are in their original languages.
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

**Spec Cards bauen, vier diagnostische Rollen** — A 3-hour workshop in which participants build a falsifiable cognitive specification of a learner (a Spec Card) and apply four diagnostic roles to their own assignments.

### Learning Objectives

By the end of this workshop, participants will:

1. **Write** a six-section Spec Card for a novice in their own discipline, with particular focus on Section 4 (misconceptions with intuitive basis) and Section 5 (metacognitive posterior with action-as-input requirement)
2. **Translate** the spec into multiple tools and observe where model defaults diverge from specified behavior
3. **Apply** four diagnostic roles to their own teaching materials (clarity stress-test; intervention-vs-observation mapping; misconception probe; performance-learning dissociation detection)
4. **Justify** why AI substitution disables (rather than degrades) metacognitive update, and what that means for assignment design

### Workshop Flow

| Block | Duration | What Participants Do |
|------|----------|---------------------|
| Einstieg | 10 min | Curse-of-knowledge activator: explain a key concept assuming a specific schema is missing |
| Block 1 | 35 min | Performance vs. learning, two posteriors, Pearl's intervention/observation, paired sketch on own assignment |
| Block 2 | 45 min | Walkthrough of the worked Statistics-Novice Spec Card; participants build their own |
| **Break** | 15 min | |
| Block 3 | 30 min | Four-tier deployment spectrum (instructor demo): Copilot, HuggingChat, Marimo notebook, coding agent |
| Block 4 | 35 min | Four diagnostic roles applied to participant's own assignment |
| Closing | 10 min | Resource-rational analysis applied to institutional adoption + one concrete commitment |

### The Spec Card: 6 Sections

Each section commits to a specific theoretical claim. Internal-precise labels (in `instructor-notes/`) preserve the architecture names; participant-facing labels (in `workshop/`) use accessible German.

| # | Internal label (English) | Participant-facing label (German) | Theoretical commitment |
|---|---|---|---|
| 1 | Role + expertise level | Rolle und Erfahrungsstand | Stable point on novice-expert continuum |
| 2 | What's not yet built (overhypotheses + uncompiled productions) | Was noch nicht aufgebaut ist | Hierarchical priors + ACT-R element interactivity |
| 3 | Schemas held + automatised patterns | Vorhandene Schemata und automatisierte Muster | ACT-R chunks + compiled productions |
| 4 | Misconceptions with intuitive basis | Fehlkonzepte und ihr intuitiver Hintergrund | Conceptual change theory (Vosniadou, diSessa, Chi) |
| 5 | Metacognitive posterior with action-as-input requirement | Selbsteinschätzung und ihre Aktualisierungsbedingungen | Daw & Fleming + active inference |
| 6 | What this novice does when stuck | Was diese Novizin tut, wenn sie nicht weiterkommt | ACT-R production rules under uncertainty |

### Vocabulary Policy

Two registers, kept distinct:

- **Internal docs** (instructor-notes/, design docs, this CLAUDE.md): full theoretical naming preserved
- **Participant materials** (workshop/, vorbereitung/): only Pearl's intervention/observation and Kapur's productive failure are named. Marr's levels, ACT-R, Bayesian framing, Daw & Fleming, active inference, and conceptual change as a tradition are *used as concepts* but not *named as architectures*.

### Four Diagnostic Roles

Applied to participant's own teaching material in Block 4:

1. **Klarheits-Stresstest** (clarity stress-test): hand the Twin your instructional material; where it fails for missing schemas, you've found tacit knowledge
2. **Intervention vs. Beobachtung** (intervention/observation mapper): decompose your assignment into subtasks; ask which generate input to the metacognitive computation
3. **Fehlkonzept-Sonde** (misconception probe): configure Twin to hold a misconception; does the assignment force a visibly failing prediction (productive failure)?
4. **Performanz-Lernen-Detektor** (performance-learning dissociation detector): Twin produces fluent-confident-wrong work; lecturer evaluates and notices what they catch and miss

### Technical Stack

- **Anthropic Claude Haiku 4.5**: structured-output language model used by the marimo notebook (tier 3) and the legacy Gradio shell
- **Pydantic**: defines the `Diagnosis` and `Response` schema (the load_signal taxonomy from the previous iteration is reused as concrete content for Section 4 of the Statistics-Novice spec)
- **Gradio**: legacy shell, fallback deployment
- **Marimo**: tier-3 demonstration notebook (visible code, reactive cells)
- **HuggingFace Spaces**: free deployment platform
- **Coding agents** (Claude Code or pi.dev): tier-4 demonstration

### Six Backup Scenarios

Located at `workshop/build/scenarios/` and mirrored in `hf-spaces/diagnostic-tool-shell/scenarios.json` and `hf-spaces/diagnostic-tool-shell-marimo/scenarios.json`:

1. Nursing: Warfarin and INR
2. Education: Critique a quiz question
3. Business: Bakery pricing
4. Social work: Missed appointments
5. Engineering: Stale-data bug
6. Statistics: Interpreting r = 0.3

Each scenario provides three calibrated student responses. In the new design these serve as backup assignments for Block 4 (for participants without their own material) and as Role 3's misconception bank.

### Pedagogical Grounding

Layered on top of the intermediate workshop's CLT framing. The new design adds:

- **Computational vs. algorithmic levels** (Marr): used implicitly; not named in participant materials
- **Bayesian framing of belief revision**: priors, posteriors, conditioning variables; named as concepts (Posteriore, Aktualisierungsbedingungen) but not as a framework
- **ACT-R-style decomposition**: chunks and compiled productions as schemas + automatised patterns; named as concepts only
- **Pearl's intervention vs. observation**: named explicitly in participant materials. Mechanises the offloading-vs-outsourcing distinction
- **Daw & Fleming second-order metacognition**: the action-as-input claim is the workshop's strongest claim. The citation lives in instructor notes; the claim is stated in plain German for participants
- **Productive failure (Kapur)**: named in Block 4, Role 3
- **Conceptual change theory** (Vosniadou, diSessa, Chi): used in Section 4's "intuitive basis" requirement

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
