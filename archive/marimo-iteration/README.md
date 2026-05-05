# Archive: Marimo Iteration

This directory contains content from the **marimo + PydanticAI iteration** of the KI in der Lehre Advanced workshop, which was a planned design that was superseded by the **diagnose-then-respond / diagnostic-tool-shell** redesign before being delivered at scale.

The marimo iteration was internally consistent and well-spec'd, but it asked non-programmer participants to interact with ~370 LOC of Python notebook content across five labs in a 90-minute build block. Feedback on prior iterations of the broader workshop indicated that the cognitive load of code-as-medium was crowding out the pedagogical work. The redesign moved to a fixed-schema diagnostic shell so that every workshop activity engages CLT thinking rather than data-modelling thinking.

## What's here

- **`workshop-specification.md`** — the comprehensive design spec for the marimo iteration. Documents the five-lab structure, the multi-domain (programming, health sciences, agronomy) concept library, and the worked-example-generator pipeline.
- **`workshop-starter/`** — the marimo notebook participants were meant to modify. Includes the Dockerfile, requirements.txt, README, and `app.py` (the marimo app itself).

The git history of `workshop/build/index.qmd`, `workshop/theory/index.qmd`, and the other workshop content also reflects the marimo iteration prior to the redesign commit.

## Why kept

- These artifacts may resurface in a future **6-hour version** of the workshop where the second half adds custom-schema design and a deeper code-modification component for technically inclined participants.
- The Worked Example Weaver app at `hf-spaces/worked-example-weaver-app/` (still in the live tree, not archived) shares Pydantic and structured-output patterns with the workshop-starter and remains useful as an optional further-exploration link from the new workshop.
