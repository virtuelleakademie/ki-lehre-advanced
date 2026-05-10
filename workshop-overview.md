# KI in der Lehre: Advanced

## One-page overview

A 3-hour workshop in which lecturers build a Spec Sheet for one of their own teaching tasks, render it as a system prompt for a chat tool, and test it against a known student answer.

## What the workshop responds to

Using AI tools in teaching defaults, in practice, to whatever the tool happens to make easy. Lecturers write prompts that paraphrase what they would say in office hours, hand them to a chat tool, and discover that the result is fluent but pedagogically arbitrary: it builds the wrong representations, addresses the wrong misconceptions, or substitutes for the cognitive work the learner needs to do themselves. The problem is not prompt quality. The problem is that the cognitive content of the teaching task has not been articulated separately from the prompt.

## What the workshop proposes

Before touching a tool, the lecturer writes a Spec Sheet: a four-section, falsifiable decomposition of what the learner needs to construct in order to perform a single teaching task. The Spec Sheet is not a prompt. It is a structured-introspection scaffold for cognitive content, with two LLMs assisting (Hypothesengenerator and Lernende-Simulator) and a falsification procedure attached.

## Central claim, narrowly stated

The Spec is the durable design artifact for the lecturer's reasoning about the task. The Prompt is its rendering for a specific tool. The two encode claims about different systems with different stability profiles: the Spec is about the learner's required cognitive architecture; the Prompt is about a specific LLM's quirks. Tool churn does not invalidate the Spec.

The Spec produces a KC-decomposition *hypothesis*, not a validated cognitive model. The lecturer leaves the workshop in a position to test that hypothesis against real student work and revise.

## What participants do

Total: 150 min contact + 15 min break.

| Block | Time | What |
|---|---|---|
| Einstieg | 7 min | Curse-of-knowledge activator + LLM-mirror foreshadowing the Lernende-Simulator |
| Block 1 | 45 min | CLT-recap; three knowledge types; Spec / Prompt distinction; two LLM roles; live walked Statistics example; abbreviated tool-tour |
| Pause | 15 min | |
| Block 2 | 60 min | Build own Spec for one teaching task: Sektion A (Teilaufgabe) → B (Wissensbausteine, with V/B discipline) → C (Fehlkonzepte) → paired feedback |
| Block 3 | 25 min | Translate Spec into system prompt; test against a known student answer using pass / fail-soft / fail-hard |
| Closing | 13 min | Falsifikationsnotiz; Selbst-Tun-vs-Zuschauen tagging; one-sentence student-policy; concrete first commitment |

## The four moves the workshop makes

1. **Decomposition before rendering.** Cognitive content is named (knowledge-type, V/B status, failure-mode-per-Baustein) before any prompt is written.
2. **Falsification as discipline.** Each Spec entry is paired with a one-sentence prediction of how its absence would show up in student work. The Closing records what would falsify the decomposition.
3. **LLM as second opinion, not as authority.** Two operational roles: Hypothesengenerator (suggests Bausteine and misconceptions for the lecturer to accept or prune) and Lernende-Simulator (instantiates the Spec into a fluent confabulation the lecturer can probe).
4. **Per-Baustein action assignment.** In Closing, each Wissensbaustein is tagged Selbst-Tun-erforderlich or Zuschauen-reicht. The decision is per-component, not per-assignment, because the action-as-input claim has resolution only at component-grain.

## The three knowledge types

The typology compresses KLI's KC taxonomy into a teaching-pragmatic three-way split, with the type determining the learning mechanism that can build it.

- **Faktenwissen** (Memory-and-Fluency KCs): retrievable items. Built by retrieval practice. *Example:* "$r$ liegt zwischen $-1$ und $+1$".
- **Klassifikationswissen** (Induction-and-Refinement KCs over variable KCs): pattern recognition under feature uncertainty. Built by interleaved varied-example classification with contrast cases. *Example:* "erkennt eine Frage als Korrelations- vs. Mittelwertvergleich-Frage".
- **Erklärungswissen** (Understanding-and-Sense-Making KCs over compositional KCs): generative principles that license transfer. Built by self-explanation, worked examples with prompted explanation, productive failure. *Example:* "weiss, warum $r = 0.3$ in der Bildungsforschung bedeutsam und in der Physik vernachlässigbar ist".

## What participants leave with

- A four-section Spec Sheet for one of their own teaching tasks
- A system prompt that renders the Spec for a chat tool of their choice
- One pass / fail-soft / fail-hard test result against a real or backup student answer
- A one-sentence student-facing AI-use policy for that task
- A concrete first commitment for the next teaching iteration

## What this is not

It is not a Cognitive Tutor authoring system. It is not a validated KC decomposition. It is not a prompt-engineering workshop. The Spec produces a hypothesis about cognitive content that the lecturer is now in a position to test, revise, and re-render across tools as the tool landscape changes.

## Cogsci anchors

- **Decomposition discipline:** Koedinger, Corbett, & Perfetti (2012), Knowledge-Learning-Instruction framework
- **Expert blind spot motivating V/B-discipline:** Nathan & Petrosino (2003); Koedinger & Nathan (2004)
- **Action-as-input motivating Selbst-Tun-tagging:** Koedinger, Kim, Jia, McLaughlin, & Bier (2015) doer effect; Van Campenhout, Johnson, & Olsen (2022); mechanism: Daw & Fleming (2018)
- **Misconception structure:** Vosniadou (1994), Chi (2008) for coherent wrong models; diSessa (1993) for fragmented intuitions
- **Cognitive load framing of Block 1 recap:** Sweller (1988); Kalyuga (expertise reversal)
