# Workshop Redesign: Comprehensive Overview

## The Big Picture: What Problem Did We Solve?

You wanted to modernize your "KI in der Lehre: Advanced" workshop to:
1. **Focus on pedagogy over technology** - Build tools that genuinely help students learn, not just demonstrate API calls
2. **Use modern tools** - Replace Google Colab with marimo notebooks
3. **Base it on learning science** - Ground everything in "Make it Stick" cognitive principles
4. **Make it interactive** - Students should experiment, not just read

## The Solution: Marimo Islands + Quarto

I integrated two technologies:
- **Marimo**: Modern Python notebooks with reactive execution (cells auto-update when dependencies change)
- **Quarto**: Publishing system that creates beautiful educational websites

The **quarto-marimo extension** lets us embed interactive Python cells (called "marimo islands") directly into Quarto documents, so students can:
- Read explanatory text
- See code examples
- **Edit and run code in their browser** (no installation needed!)
- Get instant feedback from reactive execution

## What Was Actually Built

### 1. Module 0: Introduction & Setup (45 min content)

**Location**: `workshop/00-setup/index.qmd`

**What it teaches**:
- The pedagogical framework (Make it Stick principles)
- Why marimo is better than Jupyter/Colab
- How to set up OpenAI API
- First hands-on example: a Socratic tutor that asks questions instead of giving answers
- How to calculate API costs

**Interactive elements**:
```python
# Students can type questions and see the Socratic tutor respond
student_question = mo.ui.text_area(...)

# The tutor NEVER gives direct answers - it asks guiding questions
# This demonstrates the pedagogical principle of "productive struggle"
```

**Key innovation**: All text is in German, uses your custom callouts (like `:::{.callout-try}`), and cells are marked as either:
- `editor: false` (demo - students watch)
- `editor: true` (practice - students edit)

---

### 2. Module 1: Retrieval Practice Generator (60 min content)

**Location**: `workshop/01-retrieval-practice/index.qmd`

**What it teaches**:
- The science: Why active recall is more effective than re-reading
- How to build a tool that generates practice questions from learning materials
- Using Bloom's taxonomy for difficulty levels
- Structured output with Pydantic (JSON schema)
- Providing formative feedback

**The tool students build**:
```
Input: Learning material (text about a topic)
Configure: Difficulty level, number of questions, question type
Output: Questions with:
  - Sample answers
  - Common misconceptions
  - Key concepts tested
```

**Example interaction**:
1. Student pastes text about photosynthesis
2. Selects "understand" level from Bloom's taxonomy
3. AI generates 5 questions that require explanation (not just recall)
4. Each question includes what misconceptions to watch for
5. Student can try answering and get Socratic feedback

**Pedagogical principle**: The tool promotes **retrieval practice** (proven to improve retention) rather than recognition (like multiple choice).

---

### 3. Exercise 1: Build a Socratic Tutor (20 min hands-on)

**Location**: `exercises/exercise-01/`

**Files created**:
- `index.qmd` - Instructions and learning goals
- `socratic-tutor-starter.py` - Template with TODOs
- `socratic-tutor-solution.py` - Complete working version

**What students do**:
1. Choose a subject (Biology, Math, History, etc.)
2. Write a system prompt that enforces Socratic questioning
3. Build conversation interface with marimo UI elements
4. Implement multi-turn conversation with memory
5. Test with different scenarios

**Two ways to work**:
- **In browser**: Edit cells directly on the website
- **Locally**: Download the .py file and run `marimo edit socratic-tutor-starter.py`

**Learning goals**:
- System prompt design
- Conversation state management
- The Socratic method (questions > answers)
- Making AI tools pedagogically sound

---

### 4. Pedagogical Prompt Template Library

**Location**: `resources/prompt-templates/pedagogical-prompts.qmd`

**What it contains**: 14 evidence-based prompt templates for common teaching scenarios:

1. **Retrieval Practice Question Generator** - Active recall questions
2. **Spaced Repetition Scheduler** - When to review based on forgetting curve
3. **Socratic Guided Discovery** - Question-based tutoring
4. **Misconception Detector** - Identify and address wrong thinking
5. **Growth-Oriented Feedback** - Formative assessment
6. **Self-Assessment Facilitator** - Metacognition prompts
7. **Varied Practice Generator** - Transfer and application
8. **Real-World Connection Builder** - Relevance and motivation
9. **Learning Strategy Advisor** - Study skills coaching
10. **Progress Reflection Guide** - Metacognitive awareness
11. **Productive Failure Facilitator** - Learning from errors
12. **Difficulty Adjuster** - Zone of proximal development
13. **Multi-Path Explainer** - Multiple representations
14. **Authentic Assessment Creator** - Real-world tasks

Each template includes:
- **Purpose**: When to use it
- **Principles**: Which learning science it's based on
- **Template**: Copy-paste prompt structure
- **Example**: Concrete implementation
- **Cautions**: When NOT to use it

**Why this matters**: Instead of guessing how to prompt for education, you have research-backed templates.

---

## The Technical Integration: How Marimo + Quarto Work Together

### Before (Traditional Approach)
```
Jupyter Notebook (.ipynb)
↓
Render to static HTML
↓
Students can only READ
```

**Problems**:
- No interactivity after rendering
- JSON format (bad for git)
- Hidden state issues
- Can't experiment without local setup

### After (Marimo Islands Approach)
```
Marimo source (.py)
↓
Export to .qmd with islands
↓
Quarto renders to HTML with embedded WASM
↓
Students can READ and INTERACT in browser
```

**Benefits**:
- Reactive execution (changes propagate automatically)
- Interactive in browser (no installation)
- Git-friendly (Python source)
- Reproducible (no hidden state)

### The Workflow I Established

**For developing new content**:
```bash
# 1. Create marimo notebook
marimo edit workshop/new-module/notebook.py

# 2. Test interactivity - make sure UI elements work

# 3. Export to Quarto format
marimo export md workshop/new-module/notebook.py -o temp.qmd

# 4. Refine the .qmd:
#    - Add German explanatory text between code blocks
#    - Insert custom callouts (:::{.callout-reflect})
#    - Configure which cells students can edit (#| editor: true/false)
#    - Save as index.qmd

# 5. Preview in Quarto
quarto preview  # Live preview at localhost:8800

# 6. Render for deployment
quarto render  # Outputs to docs/ for GitHub Pages
```

**Key technical details**:
- Used `external-env: true` to leverage your existing `.venv` instead of creating isolated environments
- Configured cells with `#| echo: true` (show code) and `#| editor: true/false` (editable or not)
- Added `filters: - marimo-team/marimo` to front matter of each module

---

## Configuration Changes

### 1. Updated `_quarto.yml` (Site Navigation)

Added new sections to the sidebar:

```yaml
sidebar:
  - title: "Workshop"
    contents:
      - section: "Neue Module (Marimo-basiert)"
        contents:
          - workshop/00-setup/index.qmd
          - workshop/01-retrieval-practice/index.qmd
      - section: "Legacy Content (wird migriert)"
        contents:
          - [old content...]
```

This creates a clear visual separation between new (marimo-based) and old content.

### 2. Updated `pyproject.toml` (Dependencies)

Added:
```toml
dependencies = [
    "marimo[mcp]",
    "openai",
    "pydantic>=2.12.4",
    "python-dotenv>=1.2.1",
    "tiktoken>=0.8.0",  # For cost calculation
]
```

### 3. Updated `CLAUDE.md` (Developer Documentation)

Added detailed section on marimo workflow so future developers (or Claude instances) know:
- How to create new modules
- The two development workflows
- Cell configuration options
- File structure patterns
- Best practices

---

## Documentation Created

### 1. `docs/marimo-quarto-integration.md` - Integration Guide

**Comprehensive 500+ line guide covering**:
- How the extension works architecturally
- Two development workflows (marimo-first vs quarto-first)
- Cell configuration patterns
- Integration with custom callouts
- Project structure
- Common tasks (adding modules, converting Jupyter)
- Troubleshooting
- Best practices
- Migration plan

**Why this matters**: Anyone (including you in 6 months) can understand and extend the system.

### 2. Updated `CLAUDE.md`

Added:
- Pedagogical framework section
- Marimo workflow documentation
- New workshop structure
- References to pedagogical principles

### 3. Prompt Template Library

The 14 templates provide ready-to-use prompts for common educational scenarios, so you don't have to design them from scratch.

---

## Pedagogical Improvements

### Old Workshop Focus
- "Here's how to call the OpenAI API"
- "Here's how to use temperature and top_p"
- "Here's how to get JSON output"
- Technical skills ✅, Pedagogical value ❌

### New Workshop Focus
- "Here's how to build tools that promote active retrieval"
- "Here's how to implement Socratic questioning"
- "Here's why direct answers hurt learning"
- "Here's how to create desirable difficulties"
- Technical skills ✅, Pedagogical value ✅

### Alignment with "Make it Stick"

Every module explicitly connects to cognitive science:

**Module 0**: Introduces the framework
- Active retrieval over passive review
- Desirable difficulties
- Metacognition
- AI as scaffolding (not replacement)

**Module 1**: Implements retrieval practice
- Generation over recognition
- Varied practice
- Formative feedback
- Targeting misconceptions

**Exercise 1**: Practices Socratic method
- Questions over answers
- Productive struggle
- Building on prior knowledge
- Metacognitive awareness

---

## What Makes This Different: A Concrete Example

### Old Approach - "Exploring OpenAI Models"
```python
# Call the API
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is photosynthesis?"}]
)
print(response.choices[0].message.content)

# Output: "Photosynthesis is the process by which..."
```

**Student learns**: How to call the API ✓

**Problem**: This isn't pedagogically sound - direct answers don't promote learning!

### New Approach - "Retrieval Practice Generator"
```python
# Generate QUESTIONS that require active recall
system_prompt = """Generate retrieval practice questions.
- Focus on GENERATION not RECOGNITION
- Create desirable difficulties
- Identify common misconceptions
- Provide formative feedback"""

# Student configures difficulty (Bloom's taxonomy)
difficulty = mo.ui.radio({
    "recall": "Basic facts",
    "understand": "Explain concepts",
    "apply": "Use in new situations"
})

# Generates questions + sample answers + misconceptions
# Then provides Socratic feedback on student responses
```

**Student learns**:
- How to build pedagogically sound tools ✓
- Why this approach promotes learning ✓
- Cognitive science principles ✓
- Technical skills (structured output, prompting) ✓

---

## File Structure: Before & After

### Before
```
workshop/
├── setup-openai/          (QMD - basic setup)
├── setup-colab/           (QMD - Colab instructions)
├── exploring-openai-models/ (Jupyter - technical)
├── api-tricks/            (QMD - broken, German/English mix)
└── structured-output/     (Jupyter - JSON schemas)

exercises/
├── exercise-1/            (Basic API practice)
├── exercise-2/            (More API practice)
└── exercise-3/            (Structured output)
```

### After
```
workshop/
├── 00-setup/              ✨ NEW: Marimo intro + pedagogy
│   ├── marimo-intro.py   (Source)
│   └── index.qmd          (Published with islands)
│
├── 01-retrieval-practice/ ✨ NEW: Build learning tools
│   ├── retrieval-practice-generator.py
│   └── index.qmd
│
└── [legacy content...]    (Will migrate gradually)

exercises/
├── exercise-01/           ✨ NEW: Socratic tutor
│   ├── socratic-tutor-starter.py    (Template)
│   ├── socratic-tutor-solution.py   (Reference)
│   └── index.qmd          (Instructions)
│
└── [legacy exercises...]

resources/
└── prompt-templates/      ✨ NEW: 14 educational templates
    └── pedagogical-prompts.qmd

docs/
├── marimo-quarto-integration.md  ✨ NEW: Developer guide
└── workshop-redesign-overview.md ✨ NEW: This document
```

---

## How Students Experience This

### Module 0 (Setup)
1. Read about pedagogical principles
2. Learn why marimo > Jupyter
3. See a callout: "Try It!"
4. Type a question in a text box
5. Click button
6. Watch Socratic tutor respond (no direct answer!)
7. See cost calculation update reactively
8. Reflect on why this approach works

### Module 1 (Retrieval Practice)
1. Read about cognitive science of retrieval
2. Paste learning material into text area
3. Adjust sliders and dropdowns (difficulty, quantity)
4. Click "Generate Questions"
5. See questions with misconceptions and sample answers
6. Try answering a question
7. Get formative feedback (not just "right/wrong")
8. Reflect on design choices

### Exercise 1 (Socratic Tutor)
1. Read instructions
2. **Option A**: Edit cells directly in browser
3. **Option B**: Download .py and run locally
4. Fill in TODOs (system prompt, conversation logic)
5. Test with different scenarios
6. Check hints if stuck
7. Compare with solution
8. Experiment with variations

**Key**: Students can **interact** at every step, not just read.

---

## Technical Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│  Developer Workflow                              │
├─────────────────────────────────────────────────┤
│                                                  │
│  marimo edit module.py                          │
│       ↓                                          │
│  Test interactivity                             │
│       ↓                                          │
│  marimo export md → temp.qmd                    │
│       ↓                                          │
│  Refine: Add German text + callouts             │
│       ↓                                          │
│  Save as index.qmd                              │
│       ↓                                          │
│  quarto render                                  │
│       ↓                                          │
│  docs/module/index.html                         │
│                                                  │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  Student Experience (Browser)                    │
├─────────────────────────────────────────────────┤
│                                                  │
│  Open https://...github.io/module/              │
│       ↓                                          │
│  Read explanatory text                          │
│  See custom callouts                            │
│       ↓                                          │
│  Interact with marimo islands:                  │
│    - Edit code in browser                       │
│    - Move sliders                               │
│    - Type in text boxes                         │
│    - Click buttons                              │
│       ↓                                          │
│  Marimo WASM runtime:                           │
│    - Executes Python in browser                 │
│    - Reactive updates                           │
│    - Calls OpenAI API (with student's key)     │
│       ↓                                          │
│  See results immediately                        │
│  Get feedback                                   │
│  Experiment with variations                     │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## Why This Matters: Pedagogy Over Technology

### Traditional Coding Workshop
**Focus**: "Learn the syntax and API"
**Outcome**: Students can make API calls
**Problem**: They don't know WHEN or HOW to use it effectively for teaching

### This Workshop
**Focus**: "Learn to build tools that improve learning"
**Outcome**: Students understand:
- Why Socratic questioning works (cognitive science)
- When to use retrieval practice (evidence-based)
- How to create productive struggle (not frustration)
- How to give formative feedback (growth-oriented)

**Result**: They can transfer these skills to their own teaching contexts.

---

## Key Design Decisions Made

### 1. Marimo Islands over Standalone
**Why**: Keeps interactive code integrated with explanatory text and custom callouts. Students don't have to switch between files.

### 2. External Environment (`external-env: true`)
**Why**: Uses project `.venv` instead of creating isolated environments per notebook. Simpler dependency management.

### 3. Dual-Format Exercises
**Why**: Supports both in-browser work (no setup) and local development (full features). Different learning preferences.

### 4. German as Primary Language
**Why**: Consistency with target audience. Old workshop mixed German and English confusingly.

### 5. Strategic `editor: true/false`
**Why**: Demo cells (`editor: false`) show techniques. Practice cells (`editor: true`) let students experiment. Clear pedagogical intent.

### 6. Source + Published Files
**Why**: Keep `.py` files as source of truth (edit in marimo). Generate `.qmd` for publishing (add explanatory text). Separation of concerns.

### 7. Custom Callouts Integration
**Why**: 20+ pedagogical callouts (`try`, `reflect`, `caution`, etc.) scaffold learning. Marimo islands complement rather than replace them.

---

## Comparison Tables

### Content Focus

| Aspect | Old Workshop | New Workshop |
|--------|--------------|--------------|
| **Primary Focus** | API mechanics | Pedagogical tool building |
| **Example Task** | "Call the API with temperature=0.7" | "Build a tool that promotes retrieval practice" |
| **Learning Outcome** | Can use OpenAI API | Can design learning tools based on cognitive science |
| **Question Type** | "How do I set parameters?" | "Why does Socratic questioning work?" |
| **Student Role** | Execute API calls | Design pedagogical interventions |

### Technical Approach

| Aspect | Old Workshop | New Workshop |
|--------|--------------|--------------|
| **Platform** | Google Colab | Marimo (local + browser) |
| **Interactivity** | Static after render | Reactive, editable cells |
| **File Format** | Jupyter .ipynb (JSON) | Python .py files |
| **Version Control** | Difficult (JSON diffs) | Clean (Python diffs) |
| **Reproducibility** | Hidden state issues | Reactive execution (deterministic) |
| **Setup Required** | Google account | `.env` file with API key |
| **Deployment** | Upload to Colab | Static site (GitHub Pages) |

### Pedagogical Alignment

| Aspect | Old Workshop | New Workshop |
|--------|--------------|--------------|
| **Learning Theory** | Implicit | Explicit (Make it Stick) |
| **Active Learning** | Minimal | Central |
| **Retrieval Practice** | Not emphasized | Core module |
| **Metacognition** | Not addressed | Multiple prompts |
| **Formative Feedback** | Not modeled | Demonstrated and practiced |
| **Transfer** | Limited | Varied contexts and applications |
| **Desirable Difficulties** | Accidental | Intentionally designed |

---

## Summary: What You Now Have

### ✅ Foundation Built
1. **2 Complete Modules** with marimo islands (90-105 min content)
2. **1 Hands-on Exercise** with starter + solution (20 min)
3. **14 Pedagogical Prompt Templates** (reusable)
4. **3 Documentation Files** (integration guide, overview, updated CLAUDE.md)
5. **Working Integration** of marimo + Quarto + custom callouts
6. **Clear Migration Path** for legacy content

### ✅ Pedagogical Improvements
- Grounded in "Make it Stick" principles
- Focus on tools that promote learning
- Active over passive
- Questions over answers
- Productive struggle over easy answers
- Evidence-based practices throughout

### ✅ Technical Improvements
- Modern reactive notebooks (marimo)
- Interactive in browser (WASM)
- Git-friendly (Python source)
- Reproducible (no hidden state)
- Dual workflow (browser or local)
- Clean separation of source and published content

### 🎯 Ready for Next Steps
- Module 2: Metacognitive prompts (45 min)
- Module 3: Adaptive difficulty (45 min)
- Exercise 2: Multi-turn study assistant (30 min)
- Exercise 3: Adaptive practice system (40 min)
- Migrate legacy Jupyter notebooks
- Add capstone project
- Create workshop introduction page

---

## Testing the Workshop

### Quick Test
```bash
# Preview entire site
quarto preview

# Navigate to:
# - http://localhost:8800/workshop/00-setup/
# - http://localhost:8800/workshop/01-retrieval-practice/
# - http://localhost:8800/exercises/exercise-01/
```

### Detailed Test
```bash
# Test individual modules
quarto render workshop/00-setup/index.qmd
quarto render workshop/01-retrieval-practice/index.qmd

# Test marimo notebooks standalone
source .venv/bin/activate
marimo edit workshop/00-setup/marimo-intro.py
marimo edit workshop/01-retrieval-practice/retrieval-practice-generator.py
marimo edit exercises/exercise-01/socratic-tutor-starter.py
marimo edit exercises/exercise-01/socratic-tutor-solution.py
```

### Student Perspective Test
1. Open rendered HTML in browser
2. Try interacting with cells
3. Modify code in editable cells
4. Watch reactive updates
5. Test with your own API key
6. Follow exercise instructions

---

## Migration Strategy for Legacy Content

### High Priority (Core Content)
1. **exploring-openai-models** (Jupyter → Marimo)
   - Currently teaches parameter exploration
   - Needs: Convert to marimo, add pedagogical context
   - Estimated: 2-3 hours

2. **structured-output** (Jupyter → Marimo)
   - Currently teaches Pydantic schemas
   - Needs: Convert to marimo, integrate with retrieval practice
   - Estimated: 2-3 hours

### Medium Priority (Needs Fixes)
3. **api-tricks** (QMD)
   - Currently: Broken code, mixed languages
   - Needs: Fix syntax, translate, convert to marimo
   - Estimated: 2-3 hours

### Lower Priority (Optional)
4. **setup-openai** (QMD)
   - Consider: Merge into Module 0?
   - Or: Keep as standalone reference

5. **setup-colab** (QMD)
   - Consider: Remove (no longer using Colab)
   - Or: Archive as "alternative approach"

---

## The Bottom Line

**Before**: Technical workshop teaching API mechanics with Google Colab

**After**: Pedagogically-grounded workshop teaching educators how to build learning tools with evidence-based principles, using modern reactive notebooks that work in the browser

**Key Innovation**: Marimo islands let students interact with code directly on the website while you maintain clean Python source files, all integrated with your existing Quarto site and custom callouts.

**Impact**: Workshop participants will leave understanding not just HOW to use AI APIs, but WHEN and WHY to use them in ways that genuinely improve student learning.

---

*Last updated: November 13, 2025*
*Workshop version: 2.0 (Marimo-based redesign)*
