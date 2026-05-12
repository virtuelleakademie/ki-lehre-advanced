# KI in der Lehre: Advanced

## One-page overview

A 3-hour workshop in which lecturers build a Spec Sheet for one of their own teaching tasks, render it as a system prompt for a chat tool, and test it against a known student answer.

## What the workshop responds to

Using AI tools in teaching defaults, in practice, to whatever the tool happens to make easy. Lecturers write prompts that paraphrase what they would say in office hours, hand them to a chat tool, and discover that the result is fluent but pedagogically arbitrary: it builds the wrong representations, addresses the wrong misconceptions, or substitutes for the cognitive work the learner needs to do themselves. The problem is not prompt quality. The problem is that the cognitive content of the teaching task has not been articulated separately from the prompt.

## What the workshop proposes

Before touching a tool, the lecturer writes a Spec Sheet: a four-section, falsifiable decomposition of what the learner needs to construct in order to perform a single teaching task. The Spec Sheet is not a prompt. It is a structured-introspection scaffold for cognitive content, with two LLMs assisting (Hypothesengenerator and Lernende-Simulator) and a falsification procedure attached.

## Why this matters: AI as forcing function for cognitive task analysis

The motive that drives this design is not, in the first instance, defence against tool churn. It is that lecturers who teach a task for years rarely sit down to write out, at the resolution that matters, what is supposed to happen in the learner's head. Cognitive task analysis (Clark & Estes, 1996; Schraagen, Chipman & Shalin, 2000) has remained an expert-only technique partly because it has had no fast feedback loop: until recently, no tool existed that could externalise the lecturer's tacit model of the student and probe it in minutes. The Lernende-Simulator is that loop. The Hypothesengenerator accelerates the authoring. AI, in this design, is the forcing function and the microscope; the cognitive task analysis is the product. "Spec is durable, Prompt is rendering" is a by-product justification of that arrangement: the artifact happens to survive tool churn because it specifies content rather than tool behaviour.

## Central claim, narrowly stated

The Spec is the durable design artifact for the lecturer's reasoning about the task. The Prompt is its rendering for a specific tool. The two encode claims about different systems with different stability profiles: the Spec is about the learner's required cognitive architecture; the Prompt is about a specific LLM's quirks. Tool churn does not invalidate the Spec.

The Spec produces a KC-decomposition *hypothesis*, not a validated cognitive model. The lecturer leaves the workshop in a position to test that hypothesis against real student work and revise.

## What participants do

Total: 155 min contact + 15 min break = 170 min wall-clock; 10 min buffer to the 3-hour ceiling.

| Block | Time | What |
|---|---|---|
| Einstieg | 10 min | Cross-discipline-pair activator: write a paragraph about your own teaching task, read your partner's, write three sentences for them, mark what came back |
| Block 1 | 35 min | Three anchor slides (Das harte Problem / Expert Blind Spot / LLMs als strukturierte Novizen); live worked-example walkthrough at the Statistics multiple-regression task; Spec-Vorschau |
| Pause | 15 min | |
| Block 2 | 60 min | Build own Spec for one teaching task: Sektion 1 (Teilaufgabe) → 2 (Wissensbausteine) → 3 (Misconceptions); cross-discipline paired review |
| Block 3 | 35 min core (+10 min optional) | Demo of running tool with example Spec, insert own Spec and observe output, sharpen Spec, optional role-play, wrap |
| Closing | 15 min | Doktrin-Extension; Downstream-Uses-Gallery; persönliche Verpflichtung shared with partner; Take-Home pointer |

The Falsifikationsnotiz and Selbst-Tun-vs-Zuschauen tagging that used to live in the in-room Closing are now Take-Home homework (documented in `workshop/take-home/index.qmd`).

## The four moves the workshop makes

1. **Decomposition before rendering.** Cognitive content is named (knowledge-type, V/B status, failure-mode-per-Baustein) before any prompt is written.
2. **Falsification as discipline.** Each Spec entry is paired with a one-sentence prediction of how its absence would show up in student work. The Take-Home Falsifikationsnotiz operationalises what would falsify the decomposition.
3. **LLM as second opinion, not as authority.** Two operational roles: Hypothesengenerator (suggests Bausteine and misconceptions for the lecturer to accept or prune) and Lernende-Simulator (instantiates the Spec into a fluent confabulation the lecturer can probe).
4. **Per-Baustein action assignment.** As Take-Home homework, each Wissensbaustein is tagged Selbst-Tun-erforderlich or Zuschauen-reicht. The decision is per-component, not per-assignment, because the action-as-input claim has resolution only at component-grain.

## The three knowledge types

The typology compresses KLI's KC taxonomy into a teaching-pragmatic three-way split, with the type determining the learning mechanism that can build it.

- **Faktenwissen** (Memory-and-Fluency KCs): retrievable items. Built by retrieval practice. *Example:* "$r$ liegt zwischen $-1$ und $+1$".
- **Klassifikationswissen** (Induction-and-Refinement KCs over variable KCs): pattern recognition under feature uncertainty. Built by interleaved varied-example classification with contrast cases. *Example:* "erkennt eine Frage als Korrelations- vs. Mittelwertvergleich-Frage".
- **Erklärungswissen** (Understanding-and-Sense-Making KCs over compositional KCs): generative principles that license transfer. Built by self-explanation, worked examples with prompted explanation, productive failure. *Example:* "weiss, warum $r = 0.3$ in der Bildungsforschung bedeutsam und in der Physik vernachlässigbar ist".

## What participants leave with

- A three-section Spec Sheet for one of their own teaching tasks (with optional Take-Home Falsifikationsnotiz as Sektion 4)
- A test of that Spec against a running tool, with observations about where the Spec needs sharpening
- A concrete commitment for the next two weeks, shared with a cross-discipline partner
- Take-Home material: the running tool URL, an architecture explanation, four sketches for further tools, and the two optional homework assignments (Falsifikationsnotiz, Selbst-Tun-vs-Zuschauen-Tagging)

## What this is not

It is not a Cognitive Tutor authoring system. It is not a validated KC decomposition. It is not a prompt-engineering workshop. The Spec produces a hypothesis about cognitive content that the lecturer is now in a position to test, revise, and re-render across tools as the tool landscape changes.

## Cogsci anchors

- **Decomposition discipline:** Koedinger, Corbett, & Perfetti (2012), Knowledge-Learning-Instruction framework
- **Expert blind spot motivating V/B-discipline:** Nathan & Petrosino (2003); Koedinger & Nathan (2004)
- **Action-as-input motivating Selbst-Tun-tagging:** Koedinger, Kim, Jia, McLaughlin, & Bier (2015) doer effect; Van Campenhout, Johnson, & Olsen (2022); mechanism: Daw & Fleming (2018)
- **Misconception structure:** Vosniadou (1994), Chi (2008) for coherent wrong models; diSessa (1993) for fragmented intuitions
- **Cognitive load framing of Block 1 recap:** Sweller (1988); Kalyuga (expertise reversal)
