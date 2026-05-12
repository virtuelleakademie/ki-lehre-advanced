# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Files

- **CLAUDE.md** (this file): quick developer reference and commands
- **2026-05-06-advanced-workshop-design.md**: the design doc for the Spec Card workshop (the user's own theoretical design statement; current authoritative source for what the workshop is)
- **2026-05-06-spec-card-redesign.md**: implementation plan for the Spec Card design (load-bearing claims, vocabulary policy, file inventory, sequence)
- **2026-05-07-redesign-comparison.md**: side-by-side comparison of Redesign A (diagnostic-tool-shell) vs. Redesign B (Spec Card). Useful as the historical record of the design choice
- **instructor-notes/{einstieg, block-1, block-2, block-3, closing}-facilitator.md**: per-block detailed facilitator notes (timing tables, opening/closing scripts, failure modes + redirects, likely questions, what-if-broken backups). Linked from the in-page `callout-facilitator` blocks
- **instructor-notes/spec-card-statistics-internal.md**: the worked Statistics-Novice Spec Card in the internal-precise register (architectures named)
- **marimo-quarto-integration.md**: technical guide for marimo + Quarto. Not used by the current workshop's main flow; preserved because the integration remains valid for other content
- **resources/prompt-templates/pedagogical-prompts.qmd**: legacy prompt templates from earlier iterations

## Project Overview

Educational website and workshop materials for the **KI in der Lehre: Advanced** workshop, the third in a three-workshop trilogy on AI in education at the BFH Virtuelle Akademie.

This 3-hour workshop has participants build a **Spec Sheet**: a 3-section, falsifiable specification of what a learner needs for one teaching task in the participant's own discipline (Teilaufgabe, Wissensbausteine, Misconceptions). Participants then insert the Spec Sheet into a running tool, observe the structured output, and sharpen the Spec where the output is generic or off-target. The Closing covers the Doktrin-Extension and the Downstream-Uses-Gallery; the Selbst-Tun-vs-Zuschauen tagging and the Falsifikationsnotiz are documented as optional Take-Home homework.

The workshop's central operative claim is **Spec is durable, Prompt is rendering**: the hard work of using AI in teaching is not choosing tools or writing prompts but specifying what is supposed to happen in the learner's head. The deeper theoretical claim, inherited from the design's earlier iteration and narrowed in the 2026-05 redesign, is that **AI substitution removes the action-contingent inputs to second-order metacognition**: without the learner's first-order action, the inputs the metacognitive computation would condition on are not generated. The empirical anchor is the *doer effect* (Koedinger, Kim, Jia, McLaughlin & Bier, 2015; Van Campenhout, Johnson & Olsen, 2022): doing predicts learning roughly six times more strongly than reading or video, with causal-strength controls. Fleming & Daw (2017) supplies the mechanism explanation. The Selbst-Tun-vs-Zuschauen tagging in the Take-Home operationalises this for the participant's own teaching task.

**Claims and limits.** The Spec Sheet is a structured-introspection scaffold producing a KC-decomposition *hypothesis* about what the learner needs, grounded in Koedinger's KLI framework (Memory-and-Fluency / Induction-and-Refinement / Understanding-and-Sense-Making mapped onto Faktenwissen / Klassifikationswissen / Erklärungswissen, with each type labelled by its cognitive operation: Abrufen / Erkennen / Begründen). It is not a validated cognitive model: the Block-3 test (observe whether the tool output matches what real learners would produce) is a workshop-scale plausibility check, not a learning-curve fit on accumulated student data. The durability claim is about the Spec's relationship to *tool churn*, not about its empirical validation. Lecturers leave the workshop in a position to test their Spec against real student work after the workshop ends; that post-workshop validation is what would graduate the Spec from hypothesis to model.

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

**Workshop Structure (3-hour workshop, German). Each block is a panel-tabset page with three tabs: Präsentation (slides + facilitator notes), Aktivitäten (participant-facing exercises), Nachlesen (extended reading + cross-links to CAS Lernpsychologie):**

- **vorbereitung/index.qmd**: pre-workshop reading (three anchor sentences, three things to bring, the LLM-as-Novice grounding warning)
- **workshop/index.qmd**: workshop overview, schedule, learning objectives; the "for returning participants" historical note is folded into a collapsed callout
- **workshop/materialien/index.qmd**: single landing page listing every participant material (Vor / Während / Nach + Prompt-Bausteine + external sources). The canonical entry point for participants
- **workshop/einstieg/**: Einstieg (10 min): cross-discipline-pair exercise; participants experience the Expert Blind Spot on their own material before it is named in Block 1
- **workshop/block-1-theorie-und-beispiel/**: Block 1 (35 min): three anchor slides (Ein schwieriges Problem / Der Expert Blind Spot / LLMs als strukturierte Novizen), then the worked-example walkthrough (live page), then Spec-Vorschau
  - `worked-example-statistics.qmd`: the live-walkthrough page; simulated $n = 80$ dataset with reciprocal-suppression structure; R code visible by default; `broom::tidy`+`glance` tables; collapsed `pro-tip` callouts for centring algebra and suppression mechanic; collapsed `caution` callout on LLM grounding
- **workshop/block-2-spec-card/**: Block 2 (60 min): participants build their own Spec Sheet (Sektion 1 → 2 with LLM-as-Novice → 3 with Lernende-Simulator → cross-discipline paired review). Contains a collapsed `caution` callout naming the two concrete failure modes of the ungrounded LLM
  - **workshop/spec-sheet-template/**: 4-section template (1: Teilaufgabe, 2: Wissensbausteine, 3: Fehlkonzepte, 4: Falsifikationsnotiz) plus `prompt-scaffolds.md` and `system-prompt-template.md`
  - The legacy 6-section worked Spec Card for the Statistics-Novice is at `instructor-notes/spec-card-statistics/index.qmd` (internal reference, not in the navigation; CLAUDE.md/old design docs occasionally still refer to a `workshop/spec-card-statistics/` path that no longer exists)
- **workshop/block-3-multi-tool/**: Block 3 (35 min core + 10 min optional role-play): demo of the tool, insert own Spec, observe output, sharpen Spec, (optional) cross-discipline role-play, wrap. The role-play is explicitly marked optional in the page header and timing callout
- **workshop/closing/**: Closing (15 min): Doktrin-Extension → Downstream-Uses-Gallery → personal commitment → Take-Home pointer. Falsifikationsnotiz and Selbst-Tun-vs-Zuschauen tagging are now Take-Home homework, not live Closing content
- **workshop/take-home/**: post-workshop sammelseite: the running tool URL, architecture explanation, four sketches for further tools, optional homework (Falsifikationsnotiz, Selbst-Tun-vs-Zuschauen)
- **workshop/build/scenarios/**: **seven** discipline scenarios in **German** (nursing, education, business, social work, engineering, statistics, math) with three calibrated student responses each. Used as backup assignments for Block 2. Failure-mode names: Aktive Fehlkonzeption, Lernferner Abruf, Schema-Lücke, Intrinsische Überlastung, Extrinsische Ablenkung. (The directory name `build/` is a legacy from a previous iteration; the scenarios remain there to keep URLs stable.)
- **slides/workshop/**: the workshop slide deck (~16 slides, embedded into each block's Präsentation tab). The Closing slides for Falsifikationsnotiz and Selbst-Tun-vs-Zuschauen are retained as Take-Home reference, not shown live in the 15-min Closing
- **slides/archive/legacy-2025/**: archived prior-iteration slide decks (theory/, discussion/) preserved for reference, not rendered into the workshop flow

**The Hosted Tools:**

- **hf-spaces/diagnostic-tool-shell-marimo/**: marimo notebook from the previous workshop iteration. Not part of the current workshop flow; kept as legacy reference. The current Block 1 has no tool-tour.
- **hf-spaces/diagnostic-tool-shell/**: the Gradio shell from the previous iteration. Stays live as a legacy deployment; not part of the current workshop flow.
- **hf-spaces/worked-example-weaver-app/**: an older personalized-worked-example tool. Stays deployed. Not linked from the new workshop content.

**Reference / instructor notes:**

- **instructor-notes/spec-card-statistics-internal.md**: the Statistics-Novice Spec Card in the internal-precise register (Marr, ACT-R, Bayesian, Daw & Fleming, Pearl, conceptual change theory all named). For instructor audit; the participant-facing version is at `workshop/spec-card-statistics/`.
- **instructor-notes/{einstieg, block-1, block-2, block-3, closing}-facilitator.md**: per-block detailed facilitator notes. Each contains a minute-by-minute timing table, suggested opening/closing wording, failure modes with redirects, likely questions, what-if-broken backup plans, and a take-away sentence. Linked from the in-page `callout-facilitator` blocks in each block's Präsentation tab.

**Supporting Directories:**

- **resources/**: legacy prompt templates library plus four CAS-derived interactive figures (`fig-bottleneck`, `fig-cognitive-load-interactive`, `fig-expertise-reversal-interactive`, `fig-offloading-spectrum-interactive`) under `resources/figures/`
- **tutorials/**: optional local setup guides
- **slides/workshop/**: current workshop slide deck (~16 slides, embedded into block Präsentation tabs)
- **slides/archive/legacy-2025/**: archived prior-iteration decks (`theory/`, `discussion/`); preserved under archive, not rendered into the workshop flow
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

**.Renviron** + **.Rprofile**: project-level R locale setup (`LANG=en_US.UTF-8`, `LC_ALL=en_US.UTF-8`, `Sys.setlocale("LC_ALL", "en_US.UTF-8")`). Required for German Umlauts to render correctly in knitr chunk-metadata serialization (e.g. `tbl-cap` strings). Do not remove unless you have verified Umlaut handling works without them on a fresh clone. R packages required for the worked-example: `tidyverse`, `broom`, `patchwork`, `MASS` (MASS ships with base R).

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

**Note**: The current workshop does not use marimo in any block. The marimo notebook from the previous iteration (`hf-spaces/diagnostic-tool-shell-marimo/notebook.py`) is kept as legacy reference only. The marimo + Quarto islands integration documented below remains a valid technique for OTHER content (and the archived marimo iteration uses it), but is not exercised by the main workshop flow.

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
- **Bibliography**: Uses `bibliography.bib`. Citations of sources not yet in the bib file are written in author-year prose form rather than `[@key]` syntax to avoid broken refs. Add entries via Zotero export rather than direct hand-edits.
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

**Spec Sheets bauen, mit LLMs als Hypothesengenerator und Lernende-Simulator** — A 3-hour workshop in which participants build a written, falsifiable specification of what a learner needs for one teaching task (a Spec Sheet) and translate it into a system prompt for a chat tool.

### Learning Objectives

By the end of this workshop, participants will:

1. **Decompose** one of their own teaching tasks into Wissensbausteine (three types defined by cognitive operation: Faktenwissen / Klassifikationswissen / Erklärungswissen, with the operations Abrufen / Erkennen / Begründen made explicit) with the V/B-discipline (vermutet vs. beobachtet) separating LLM hypotheses from teacher observations
2. **Identify** likely misconceptions and knowledge prerequisite-sources, using an LLM in two operational roles: Hypothesengenerator and Lernende-Simulator (reactive and productive)
3. **Translate** the Spec Sheet into a system prompt for a running tool, observe the structured output, and sharpen the Spec where the output is generic or off-target
4. **Decide** which Wissensbausteine require Selbst-Tun versus where Zuschauen suffices (Take-Home homework that operationalises the offloading-vs-outsourcing distinction)

### Workshop Flow

Total wall-clock: 155 min content + 15 min break = 170 min, with 10 min buffer to the 3-hour ceiling. Block 3 has an optional 10-min role-play that extends Block 3 to 45 min and consumes the buffer.

| Block | Duration | What Participants Do |
|------|----------|---------------------|
| Einstieg | 10 min | Cross-discipline pair: write a one-paragraph description of your own teaching task, read your partner's, write three sentences for them, mark what came back |
| Block 1 | 35 min | Three anchor slides (Ein schwieriges Problem / Expert Blind Spot / LLMs als strukturierte Novizen), then live worked-example walkthrough at the Statistics multiple-regression task, then Spec-Vorschau |
| **Pause** | 15 min | |
| Block 2 | 60 min | Build own Spec Sheet for one teaching task: Sektion 1 (Teilaufgabe) → 2 (Wissensbausteine, LLM-as-Novice) → 3 (Misconceptions, Lernende-Simulator) → cross-discipline paired review |
| Block 3 | 35 min core (+10 min optional) | Demo of the running tool with the example Spec, insert own Spec and observe output, sharpen Spec and re-test, (optional) cross-discipline role-play, wrap |
| Closing | 15 min | Doktrin-Extension ("Spec is durable, Werkzeug is Rendering") → Downstream-Uses-Gallery (four further tools the Spec can drive) → persönliche Verpflichtung shared with cross-discipline partner → Take-Home pointer |

The Falsifikationsnotiz and Selbst-Tun-vs-Zuschauen tagging that used to live in the in-room Closing are now Take-Home homework, documented in `workshop/take-home/index.qmd`. The slides for these (Closing section of `slides/workshop/index.qmd`) are retained as Take-Home reference; they are not shown live in the 15-min Closing.

### The Spec Sheet: 3 Sections + 1 Take-Home

The 3-section participant template (in `workshop/spec-sheet-template/index.qmd`). The earlier 6-section "Spec Card" with full theoretical labels remains preserved at `instructor-notes/spec-card-statistics/index.qmd` and `instructor-notes/spec-card-statistics-internal.md` for instructor reference.

| # | Section (German participant label) | Theoretical commitment |
|---|---|---|
| 1 | Lernaufgabe (Wortlaut, Rahmen, intendiertes Ergebnis) | Anchoring the spec to a specific subtask, not a whole assignment |
| 2 | Erforderliche Skills und Knowledge | Three types defined by cognitive operation: Faktenwissen (Abrufen) / Klassifikationswissen (Erkennen) / Erklärungswissen (Begründen); optional V/B-marking; characteristic error form per entry |
| 3 | Antizipierte Misconceptions | Conceptual change theory (used as concept, not named as framework); intuitive basis per entry |
| 4 (Take-Home) | Falsifikationsnotiz | Empirical accountability: what student behaviour would falsify the decomposition? Documented as optional Take-Home homework, not filled in the live Closing |

Plus an optional Pruning-Protokoll: LLM-Vorschläge that were rejected, with a half-line of reason. Empty pruning column with full Spec is a warning signal.

### Vocabulary Policy

Two registers, kept distinct:

- **Internal docs** (instructor-notes/, design docs, this CLAUDE.md): full theoretical naming preserved (ACT-R, Bayesian, Daw & Fleming, conceptual change theory, source-monitoring, etc.)
- **Participant materials** (workshop/, vorbereitung/): plain language. Cognitive mechanisms in the Nachlesen tabs cite their canonical homes (CAS Lernpsychologie 02-ki-und-lernen for offloading-vs-outsourcing; kompetenz-erwerben for expertise reversal). Pearl's intervention/observation distinction is named in the in-room Closing only as "Selbst-Tun vs. Zuschauen" with the Pearl mechanic explained one line in the Nachlesen tab.

### Test in Block 3

One pragmatic test question when participants insert their Spec into the running tool and observe the output: *Stimmt der Output mit dem überein, was deine echten Lernenden tun? Wenn nein, was fehlt im Spec?* Where the Spec is sharp the output is specific; where the Spec is vague the output is generic. This is a workshop-scale plausibility check, not a statistical test. The earlier Drei-Ausgänge-Heuristik (Pass / Fail soft / Fail hard) from the prior workshop iteration is documented in Block 3's Nachlesen tab as a historical reference; the slides for it remain in the deck as reference but are not shown live.

### Technical Stack

- **Anthropic Claude (Haiku/Sonnet)**: structured-output language model used by the running tool in Block 3
- **HuggingFace Spaces**: free deployment platform that hosts the Block 3 tool
- **Chat tools** (Microsoft Copilot, ChatGPT, Claude.ai, HuggingChat): the tools participants use during Block 2 to invoke the LLM-as-Novice and Lernende-Simulator roles, and that they can use after the workshop with their Spec
- **Pydantic**, **Marimo**, **Gradio**: used only in the legacy `hf-spaces/` deployments (`diagnostic-tool-shell-marimo/`, `diagnostic-tool-shell/`, `worked-example-weaver-app/`). Not part of the current workshop flow. The architecture explanation for participants who want to understand the Block 3 tool internally lives at `workshop/take-home/api-werkzeug-erklaert.qmd`.

### Seven Backup Scenarios

Located at `workshop/build/scenarios/`. **Translated to German** as of 2026-05-12. Earlier English versions are mirrored in `hf-spaces/diagnostic-tool-shell/scenarios.json` and `hf-spaces/diagnostic-tool-shell-marimo/scenarios.json` and are not regenerated when the German `.qmd` versions change:

1. Pflege: Warfarin und INR
2. Pädagogik: Eine Quizfrage kritisieren
3. Wirtschaft: Bäckerei-Preisanpassung
4. Sozialarbeit: Verpasste Termine
5. Engineering: Stale-Data-Bug
6. Statistik: Interpretation von $r = 0{,}3$
7. Mathematik: Das Substitutions-Muster erkennen

Each scenario provides three calibrated student responses, each tagged with a German failure-mode name (Aktive Fehlkonzeption, Lernferner Abruf, Schema-Lücke, Intrinsische Überlastung, Extrinsische Ablenkung). These serve as backup assignments for Block 2 (for participants without their own material) and as raw material for the Block 3 test (a known student answer to feed the system-prompted LLM). The earlier `load_signal` taxonomy from the diagnostic-tool-shell iteration is no longer used.

### Pedagogical Grounding

Layered on top of the intermediate workshop's CLT framing. The new design adds:

- **Computational vs. algorithmic levels** (Marr): used implicitly; not named in participant materials
- **Bayesian framing of belief revision**: priors, posteriors, conditioning variables; named as concepts (Posteriore, Aktualisierungsbedingungen) but not as a framework
- **ACT-R-style decomposition**: chunks and compiled productions as schemas + automatised patterns; named as concepts only
- **Pearl's intervention vs. observation**: named explicitly in participant materials. Mechanises the offloading-vs-outsourcing distinction
- **Daw & Fleming second-order metacognition**: the action-as-input claim is the workshop's strongest claim. The citation lives in instructor notes; the claim is stated in plain German for participants
- **Productive failure (Kapur)**: used implicitly in Block 3 (when participants observe a generic or off-target output, the diagnostic moment is a productive-failure moment) and in Block 2's Lernende-Simulator runs
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
