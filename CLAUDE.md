# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Files

- **CLAUDE.md** (this file) - Quick developer reference and commands
- **marimo-quarto-integration.md** - Detailed technical guide for marimo + Quarto integration
- **workshop-redesign-overview.md** - Comprehensive explanation of the workshop redesign
- **resources/prompt-templates/pedagogical-prompts.qmd** - 14 evidence-based prompt templates

## Project Overview

Educational website and workshop materials for building AI-powered educational tools grounded in Cognitive Load Theory. This 3-hour workshop teaches educators to create personalized worked example generators using PydanticAI and Marimo. Built with Quarto, delivered in English, maintained by the Virtual Academy at Bern University of Applied Sciences (BFH). Published at https://virtuelleakademie.github.io/ki-lehre-advanced/

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

**Workshop Structure (3-hour workshop - English):**

- **workshop/index.qmd**: Main workshop overview with schedule and learning objectives
- **workshop/einstieg/**: Opening activity (10 min) - Activating exercise on learning from examples
- **workshop/part-1-foundation/**: Foundation (30 min) - CLT theory, environment setup, PydanticAI demo
- **workshop/part-2-design/**: Design (30 min) - Data models, domain design, collaborative building
- **workshop/part-3-build/**: Build (50 min) - Concept library, AI agent, generation function
  - `app.py`: **Complete marimo notebook** - The main application participants build
  - `requirements.txt`: Python dependencies for deployment
- **workshop/part-4-interface/**: Interface (40 min) - Marimo UI, reactive forms, display logic
- **workshop/part-5-deploy/**: Deploy (30 min) - HuggingFace Spaces deployment guide
- **workshop/diskussion/**: Closing (10 min) - Reflection, transfer, extensions

**Supporting Directories:**

- **resources/**: Prompt templates library, supporting materials
- **tutorials/**: Optional local setup guides (VS Code, OpenAI)
- **slides/**: RevealJS presentations
- **assets/**: Images, PDFs, logos, backgrounds
- **docs/**: Build output - **DO NOT EDIT** (GitHub Pages, auto-generated)
- **archive/**: Archived legacy content (old workshop modules from previous designs)

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

**pyproject.toml**: Python dependencies
- Current: marimo[mcp], openai, pydantic, pydantic-ai, python-dotenv, tiktoken
- Package manager: uv
- Requires Python >=3.10

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

The project uses **marimo islands** - interactive Python cells embedded in Quarto documents.

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

**Building Personalized Worked Example Generators with AI** - A complete 3-hour workshop

### Learning Objectives

By the end of this workshop, participants will:

1. **Understand** the worked example effect and personalization principle from Cognitive Load Theory
2. **Build** a working personalized example generator using PydanticAI
3. **Deploy** an interactive demo to HuggingFace Spaces
4. **Possess** a template for creating domain-specific educational tools

### Workshop Flow

| Part | Duration | What Participants Do |
|------|----------|---------------------|
| Opening | 10 min | Think-Pair-Share on learning from examples |
| Part 1: Foundation | 30 min | Learn CLT theory, set up environment, see PydanticAI demo |
| Part 2: Design | 30 min | Collaboratively design data models (LearnerProfile, PersonalizedWorkedExample) |
| Part 3: Build | 50 min | Build concept library, create AI agent, test generator |
| Part 4: Interface | 40 min | Build interactive UI with Marimo (forms, buttons, display) |
| Part 5: Deploy | 30 min | Deploy to HuggingFace Spaces, troubleshoot, discuss extensions |
| Closing | 10 min | Reflect on learning, discuss transfer to own teaching |

### Technical Stack

- **PydanticAI**: Type-safe AI agent framework for structured outputs
- **Marimo**: Reactive Python notebooks with built-in UI components
- **OpenAI GPT-4o**: Language model for example generation
- **HuggingFace Spaces**: Free deployment platform

### Three Supported Domains

1. **Programming (Python)**: For loops, list comprehensions, dictionaries, functions, string formatting
2. **Health Sciences (Statistics)**: Correlation, mean/SD, t-tests, confidence intervals, effect size
3. **Agronomy**: Yield prediction, NPK optimization, growing degree days, water efficiency, cost-benefit

### Pedagogical Grounding

Based on **Cognitive Load Theory** (Sweller, 1988):

- **Worked Example Effect**: Novices learn better from studying solutions than solving problems (effect size 0.52)
- **Personalization Effect**: Familiar contexts reduce extraneous cognitive load, improving learning

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
