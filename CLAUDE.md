# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Files

- **CLAUDE.md** (this file) - Quick developer reference and commands
- **marimo-quarto-integration.md** - Detailed technical guide for marimo + Quarto integration
- **workshop-redesign-overview.md** - Comprehensive explanation of the workshop redesign
- **resources/prompt-templates/pedagogical-prompts.qmd** - 14 evidence-based prompt templates

## Project Overview

Educational website and workshop materials for teaching advanced AI/LLM concepts, focusing on the OpenAI API. Built with Quarto, delivered in German, maintained by the Virtual Academy at Bern University of Applied Sciences (BFH). Published at https://virtuelleakademie.github.io/ki-lehre-advanced/

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

**Workshop Modules (3-hour focused workshop):**

- **workshop/00-setup/**: Marimo introduction, environment setup, pedagogical principles
- **workshop/02-prior-knowledge/**: **Main module** - Build prior knowledge diagnostic tool
  - `index.qmd`: Theory, pedagogy, code examples (German)
  - `diagnostic-agent.py`: Full interactive marimo notebook
  - `gradio-demo.qmd`: Deployment guide for HuggingFace Spaces
- **exercises/exercise-01/**: Practice exercise - Socratic questioning agent

**Additional Resources:**

- **workshop/01-retrieval-practice/**: Retrieval practice generators (supplemental)
- **gradio-app/**: Production Gradio app for HuggingFace deployment
  - `app.py`: Web interface for teachers
  - `DEPLOYMENT.md`: Step-by-step deployment guide

**Supporting Directories:**

- **resources/**: Prompt templates library, supporting materials
- **tutorials/**: Optional local setup guides (VS Code, OpenAI)
- **slides/**: RevealJS presentations
- **assets/**: Images, PDFs, logos, backgrounds
- **docs/**: Build output - **DO NOT EDIT** (GitHub Pages, auto-generated)
- **archive/**: Archived legacy content (old workshop modules, exercises)

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
- Current: marimo[mcp], openai, pydantic, python-dotenv, tiktoken
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
- **Language**: Primarily German
- **Bibliography**: Uses bibliography.bib and ai-for-research.bib
- **Search**: Navbar overlay search enabled
- **Comments**: Hypothesis integration for collaborative annotation
- **Current branch**: feature/marimo (adding interactive notebooks)

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

## Workshop Structure (New Design)

The redesigned modular workshop focuses on building pedagogically sound AI tools:

### New Modules (Marimo-based)
- **Module 0** (workshop/00-setup/): Marimo introduction, environment setup, pedagogical principles
- **Module 1** (workshop/01-retrieval-practice/): Build retrieval practice generators
- **Exercise 1** (exercises/exercise-01/): Create Socratic questioning agent (20 min)

### Legacy Content (Being Migrated)
- Setup (OpenAI Platform + Google Colab) - *migrating to marimo*
- Exploring OpenAI Models (parameters) - *migrating to marimo*
- API Tricks: Mixture of Experts patterns - *needs update*
- Structured Output: JSON schema responses - *migrating to marimo*
- Legacy exercises in exercises/ directory

### Resources
- **Prompt Templates** (resources/prompt-templates/pedagogical-prompts.qmd): 14 evidence-based prompt templates for common teaching scenarios

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
