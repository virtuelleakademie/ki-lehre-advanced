# Workshop Redesign: From Worked-Example Generator to Diagnostic Tool

This document explains the redesign of the **KI in der Lehre: Advanced** workshop, the third in the BFH Virtuelle Akademie's three-workshop trilogy on AI in education.

## What changed

The previous design had participants build a multi-domain personalized worked-example generator using PydanticAI and a marimo notebook with five interactive labs over a 90-minute build block. The marimo iteration was internally consistent and well-spec'd, but a prior in-person iteration that asked participants to "develop something in Microsoft Copilot" after a prototype demo produced clear feedback: the workshop overall was too much material in too little time, and the open-ended Copilot exercise lacked structure.

The redesign narrows the workshop to **one specific pedagogical use case**: implementing CLT principles in a working diagnostic AI tool. Participants iterate a system prompt against a hosted Gradio shell whose output schema is fixed (it IS the cognitive-load-theory taxonomy). They never write code, never design data structures, and never deploy anything themselves.

## The decomposition

The redesign turns on one move: **separate the structure from the cues**.

- **Theory provides structure.** The five `load_signal` categories (`intrinsic_overload`, `extrinsic_distractor`, `germane_disengagement`, `schema_gap`, `active_misconception`) and five `intervention` categories are derived from CLT and schema-acquisition research. They are the same five whatever discipline you teach.
- **Practitioners provide cues.** What an `active_misconception` looks like in nursing differs from what it looks like in social work. Discipline expertise lives in the system prompt.

This decomposition is what makes the workshop tractable in 3 hours with non-programmer participants:

- Schema design is removed as a degree of freedom, eliminating bikeshedding on field types and JSON shapes
- All "developing" effort goes into pedagogical thinking (writing prompts grounded in CLT) rather than data modelling
- The workshop produces both a deployed tool and a portable prompt recipe usable in Microsoft Copilot, ChatGPT, or Claude

## Why a fixed schema (and not a schema designer)

An earlier draft of the redesign had participants design their own diagnosis and response schemas through a form-based UI. The reasoning was that schema design itself is pedagogical work: forcing precision about "what counts as a misconception in my discipline" surfaces decisions that are usually left implicit.

This was right but unstable in a 3-hour workshop. Schema design without structure pulls cognitive effort to data-modelling questions ("should severity be enum or scale 1-5?", "do I need a field for student-emotion?") that are *adjacent* to pedagogical thinking but not the thing we want participants to focus on.

The fix is to pre-load the structure with CLT itself. With a fixed schema whose categories are the CLT taxonomy, every classification decision the LLM makes is a CLT-grounded decision, and every prompt-iteration the participant makes is an act of teaching the model how a CLT category looks in their discipline. The structure becomes an aid to thinking, not a degree of freedom that distracts.

## What the workshop produces

Each participant leaves with three artifacts:

1. **A configured tool URL** — the shell with their system prompt encoded in URL state. They can return to it later or share it with colleagues.
2. **A portable prompt recipe** — an exported markdown block containing their prompt + the schema description + JSON-mode instructions, paste-able into any LLM interface they have institutional access to.
3. **A calibration record** — knowledge of which `load_signal` categories their prompt distinguishes reliably and which it does not, gathered from running their prompt against tagged scenario responses in Lab 4.

The vocabulary is the most durable artifact. The five categories and the diagnose-then-respond move are usable on Monday morning without any tool at all.

## Connection to the trilogy

- The **beginner** workshop introduces AI in education broadly.
- The **intermediate** workshop establishes cognitive load theory, the offloading-vs-outsourcing distinction, and a diagnostic vocabulary for analysing assignments. It ends explicitly pointing at the advanced workshop for the building step.
- This **advanced** workshop turns that diagnostic vocabulary into a working tool. The categories used here (extending classical CLT with `schema_gap` and `active_misconception`) are a slight extension of the intermediate workshop's framing.

## What was preserved

- The "this workshop IS a worked example" meta-framing carries over. The fixed schema is itself a worked example of how CLT decomposes diagnostic thinking.
- The 6 custom-callout types most useful for workshop pedagogy (`callout-individual`, `callout-pair`, `callout-group`, `callout-reflect`, `callout-pro-tip`, `callout-checkpoint`).
- The Worked Example Weaver app at `hf-spaces/worked-example-weaver-app/` stays deployed and is linked from the closing as optional further exploration.

## What was archived

- `archive/marimo-iteration/workshop-specification.md`: the previous design's comprehensive spec
- `archive/marimo-iteration/workshop-starter/`: the marimo notebook participants were meant to modify (Dockerfile, app.py, requirements.txt, README)
- The git history of `workshop/build/index.qmd`, `workshop/theory/index.qmd`, `workshop/index.qmd`, and the other workshop pages reflects the marimo iteration prior to the redesign commit

## Open work for the next iteration

These are deliberately deferred to keep the redesign focused, but worth flagging:

- **Calibration test** — the verification step where every scenario's three calibrated responses are run through the shell with the default system prompt to confirm the tool produces the tagged `load_signal` category at least 2 of 3 times. Required before workshop delivery.
- **Schema review with three colleagues** — confirm the wording of the five categories makes sense in disciplines outside the redesign authors' own. If a category is unclear, refine wording.
- **Walkthrough at full speed** — one BFH colleague (non-programmer) attempts Labs 1 to 4 in 80 minutes. Time each block and adjust the schedule if blocks consistently run long.
- **Slides** — the existing `slides/theory/index.html` was built for the worked-example-generator framing. They need to be either updated to anchor on the diagnostic taxonomy or replaced with the theory page rendered as a slide deck.
- **Comparative diagnostic mode** — a future shell version that runs a student response through two prompt variants side by side, showing how prompt phrasing changes the diagnosis.
- **A 6-hour version** that adds custom-schema design and a deeper code-modification component for technically inclined participants. The archived marimo content could resurface as the second half.
