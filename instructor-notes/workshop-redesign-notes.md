# Workshop Redesign Notes (Instructor Reference)

Audience: instructors and co-facilitators of the BFH "KI in der Lehre: Advanced" workshop. Internal-precise register (theory named); not rendered into the participant site.

## What this document is for

A single-page-ish briefing on the redesign rationale, the theory commitments behind it, and the moves a facilitator needs to make for the worked-example block to do what it is supposed to do. The participant-facing pages (`workshop/spec-sheet-template/`, `workshop/block-1-theorie-und-beispiel/worked-example-statistics.qmd`) are deliberately theory-light. This document holds what is being deliberately kept off the participant pages.

## The single goal

> Each lecturer leaves with an LLM-independent spec sheet for one subtask of one of their own assignments, validated against their own student experience (conjectured-vs-observed flagged on every item), and has translated that spec once into a working system prompt for an LLM tool of their choice.

Everything in the workshop's structure exists to deliver that goal. If a block does not produce or consolidate the spec sheet, it should be cut.

## What changed from the previous design

The previous design (six-section Spec Card + four diagnostic roles) was rendered and shipped, but cognitive-science reviews flagged three structural problems:

1. **Block 1 cognitive overload.** 35 minutes for Marr's levels + Bayesian framing + Pearl + Daw/Fleming + active inference, for participants with intermediate-CLT priors and not much else. Textbook intrinsic-load violation.
2. **Overstated central claim.** "AI substitution disables the metacognitive update" overreaches the second-order-metacognition literature. The defensible form is "AI substitution removes the action-contingent inputs to second-order metacognition." Sharper, falsifiable, doesn't pattern-match to "AI bad for thinking."
3. **Skill-development claim in 3 hours.** Cognitive task analysis is a domain skill that takes practitioners months to acquire. The honest claim is "experience the workflow once with worked-example scaffolding, take the prompts and worksheet home, repeat on Monday."

The redesign collapses to one transferable methodology, drops three of the four diagnostic roles (the surviving move, intervention/observation tagging, runs as a 5-minute closing reflection), grounds the KC typology in Koedinger's KLI tradition, and bakes a validation discipline (conjectured vs. observed) into the worksheet itself.

## Theory commitments

What is named in participant materials:

- **Pearl's intervention/observation distinction.** Named in the closing reflection; otherwise used as conceptual lens only. The participant register uses "Aktion-erforderlich" and "Beobachtung-zulässig."
- **Curse-of-knowledge.** Named in the Einstieg activator. The reactive-simulation prompt is its operational form in the workshop.
- **CLT.** Acknowledged once in Block 1 as substrate. Element interactivity and working-memory limits are reactivated as participants' prior knowledge. CLT does not carry the workshop.

What is *not* named in participant materials, but is the actual scaffolding:

- **Koedinger's KLI framework** (Koedinger, Corbett & Perfetti, 2012, *Cognitive Science* 36): the three-type KC typology participants use (Faktenwissen / Klassifikationswissen / Erklärungswissen, each labelled with its cognitive operation: Abrufen / Erkennen / Begründen) maps to KLI's *memory and fluency / induction and refinement / understanding and sense-making*. The acquisition signatures (retrieval practice / classification practice / self-explanation) are KLI's learning-event-to-KC-type matches. The Scheme-D parentheticals (operation) were chosen because the German "Begriffswissen" reading conflated definition-retrieval (Type 1) with category-recognition (Type 2); naming the operation forces the lecturer to specify what the student does with the knowledge. Cite KLI when needed; do not put it on the participants' page.
- **ACT-R / Anderson skill components.** The factual/conceptual/principled split also respects the declarative-procedural distinction. The reason "principled" is not collapsed into "procedural" is that principled KCs require self-explanation acquisition signatures, which is theoretically distinct from compiled-production formation.
- **Conceptual change theory** (Vosniadou, diSessa, Chi). The "coherent-intuitive misconception" type in section C of the spec sheet is grounded here. We distinguish surface misconceptions (wrong formula, miscoding) from coherent-intuitive ones (p-prims, ontological category errors); the latter is theoretically rich and pedagogically important. Participants get the distinction without the theory name.
- **Daw & Fleming's second-order metacognition with action-as-input.** The closing reflection's framing ("which subtasks generate the input the metacognitive computation needs?") inherits this. Softened to "removes the action-contingent inputs," not "disables." The *empirical anchor* for the softened claim is not Daw & Fleming (which is theoretical / mechanism-level) but Koedinger's **doer effect** (Koedinger, Kim, Jia, McLaughlin & Bier, 2015, *L@S*; Van Campenhout, Johnson & Olsen, 2022): doing-activity engagement predicts learning roughly six times more strongly than reading or video engagement, with causal-strength controls across hundreds of thousands of student-content interactions in OLI courses. When asked for evidence, lead with the doer effect; Daw & Fleming explains the mechanism but is not itself the warrant.
- **Proceduralised-skill compression in the typology.** The participant-facing *Faktenwissen* type compresses two cognitively distinct KC categories: declarative chunks (a fact one retrieves) and *proceduralised productions* (a skill one applies fluently, e.g., "calculate SD given a sample," "run through a clinical assessment in standard order"). The acquisition signature for proceduralised skills is *deliberate practice with feedback at production-rule grain*, not retrieval practice. For Statistics the collapse rarely bites, but in clinical (Pflege), engineering, computational, and procedural-workflow disciplines (Sozialarbeit assessment workflows) the collapse will produce mistyped Bausteine and consequent mismatched scaffolding. Facilitator move: in Block 2 with non-statistics participants, if a lecturer types a procedural-skill Baustein as Faktenwissen, ask them to describe the *exact step-by-step performance* the student must produce; that usually surfaces the proceduralised-skill nature and lets them re-type the Baustein or split it.
- **The author's own offloading-vs-outsourcing distinction** from the intermediate workshop. The intervention/observation tag operationalises this distinction. Lecturers who completed the intermediate workshop will recognise the move.

## The conjectured-vs-observed discipline

This is the workshop's most important methodological commitment. Every item in sections B, C, D of the spec sheet is flagged as either:

- **Vermutet (V):** LLM-proposed or lecturer-intuited, plausibility-checked. Not yet validated against real student work.
- **Beobachtet (B):** the lecturer has seen this in real student work; at least one concrete instance hangs on it.

Why this matters: the cognitive-science consultant's pressure-test convergent finding was that a workshop teaching LLM-assisted analysis without a built-in validation discipline launders intuition through fluent LLM output. Lecturers leave with confident-looking documents they did not actually validate. The V/B flag prevents this. Two implementation notes:

- The pruning protocol (the table at the end of the spec sheet) is the V/B flag's complement. It records items the LLM proposed but the lecturer rejected, with a one-line reason. A *full* spec sheet with an *empty* pruning protocol is a warning sign: the lecturer is rubber-stamping rather than engaging.
- In the worked example you walk through (Block 1), explicitly demonstrate at least two pruning moves with reasons aloud. Without seeing the pruning move modelled, lecturers will not do it on their own materials.

## Facilitator moves

### Block 1 walkthrough (the worked example)

This is the workshop's pedagogical hinge. The whole rest of the workshop assumes participants have seen the validation discipline in action.

Specific moves to make explicit:

- When you run prompt 1 (KC inventory) live, *deliberately get one or two LLM proposals that are wrong or off-target*. Either by using a slightly underspecified context, or by using an old chat to surface dated misconception lists. When the wrong proposal comes back, walk through your reasoning aloud: *"The LLM listed 'knows what r is' as factual. But for this assignment what students actually need is 'recognises that r is a measure of association, not a difference', which is conceptual. I'm correcting the type and rewriting the name."* That move is what participants need to see modelled.
- When you run prompt 3 (reactive simulation), pick a candidate "missing schema" that is *one of the two most central* to the subtask. Resist the temptation to pick something easy. The pedagogical point is that the reactive probe surfaces tacit knowledge in *your own* writing.
- When you run prompt 4 (productive simulation), preface the LLM output by predicting what kind of student answer it will produce. Then run it. The gap between your prediction and the LLM's actual output is the diagnostic signal, not the simulation itself.
- Throughout, keep the spec-sheet document visible on screen. Each LLM step writes into it. The participant takeaway should be: the spec sheet is the deliverable; the LLM exchanges are how you get there.

### Block 2 (participants build their own)

The single most important facilitator move in Block 2: when you walk past a participant who has filled in 6 KCs all marked V (vermutet), ask: *"Welcher dieser Bausteine ist dir bei Studierenden konkret begegnet?"* If the participant can name an instance, the item becomes B. If not, leave it as V but ask: *"Was würdest du als Erstes prüfen, um zu sehen, ob das stimmt?"* That question converts the spec sheet from a closed document into an open empirical instrument.

### Block 3 (rendering)

The most common confusion: participants try to put their entire spec sheet into the system prompt verbatim. This produces a system prompt that is too long for some tools and too generic in others. The facilitator move: when you see this, ask the participant: *"Welche zwei oder drei Bausteine sind für die Aufgabe wirklich tragend? Render zuerst nur die."* Iteration to fuller versions can happen at home.

### Closing

The intervention/observation reflection is short by design. The move that makes it land: ask participants to look at the *first* subtask of their assignment (whatever it is) and tag it. Then the *last* subtask. The contrast between the two tags is usually pedagogically informative for the lecturer themselves.

The student-facing AI-guidance reflection is also short. The format that works: *"Schreib einen Satz, der einer Studierenden sagt, wo sie für diese Aufgabe KI nutzen darf und wo nicht. Begründe nicht."* The constraint to one sentence forces commitment.

## Things to watch for

- **Lecturers who want to discuss "what AI is for in education."** This is not the workshop. Redirect to the artifact: *"Lass uns das an deiner konkreten Aufgabe ausprobieren; vielleicht wird die generelle Frage durch das Konkrete schärfer."*
- **Lecturers who want a longer theoretical introduction.** Block 1's 5-minute theory section is deliberately short. If a participant pushes, point them at this document and at `instructor-notes/spec-sheet-statistics-internal.md` for theory-rich versions of the same material.
- **Lecturers whose discipline is poorly represented in the LLM training data** (specialised crafts, niche professional skills, very local curricula). The hypothesis-generator step will produce thin output for them. The facilitator move: validate that this is real, not a personal failing, and emphasise that for these participants the productive move is to bring their own already-existing teaching observations as the B-flagged content. The LLM is then merely a sounding board.
- **Lecturers who try to "fix" the LLM by writing longer prompts.** Redirect: *"Geh zurück zu deinem Spec Sheet. Was steht da nicht, das das LLM eigentlich wissen müsste?"* Almost always the answer is a missing or vague item in B, C, or D.

## Why two LLM uses, with the simulator role doubled

The workshop names two operationally distinct LLM roles:

1. **Hypothesis generator** (drafts KC decomposition + misconception/prior-gap candidates). Addresses the blank-page problem. The LLM is good at this because it has read the relevant literatures.
2. **Learner simulator**, with two probes:
   - **Reactive probe** (LLM reads the lecturer's text as a learner missing X; reports confusion). This is the operational form of curse-of-knowledge stress-testing. It surfaces tacit knowledge in the lecturer's writing.
   - **Productive probe** (LLM produces a novice answer with X missing or with misconception Y). Tests whether the assignment discriminates the failure mode.

The reactive probe and the productive probe operate on different objects (the lecturer's material vs. the lecturer's KC list) and produce different deliverables (confusion-points to add to section D of the spec sheet vs. discrimination assessments to add to section C). They are pedagogically distinct moves; lecturers would benefit from learning both.

The reactive probe is also the methodological partner of the Einstieg's curse-of-knowledge activator. Without it, the Einstieg has no follow-up and the workshop's opening lands as a complaint about lecturer cognition without a remedy. With it, the Einstieg becomes the workshop's first concrete "and here's how you find your own blind spots" claim.

A third LLM role (configured agent, the rendered system prompt) is used in Block 3 but not framed as a separate "role" because the focus is on the spec/prompt distinction, not on accumulating LLM uses. Lecturers leave with two named moves they can apply elsewhere; the rendering is what they do with the spec.

## What the workshop deliberately does not do

To keep scope honest:

- Does not teach cognitive task analysis as a methodology. The workshop teaches a *workflow* that approximates lightweight CTA with LLM assistance. The honest framing is in the participant Vorbereitung primer.
- Does not teach prompt engineering. The system prompt is rendered mechanically from the spec; participants do not iterate on prompt phrasings beyond the basic template.
- Does not teach LLM tool selection. Three affordance types are demoed in 8 minutes (chat, structured, agentic). The intent is exposure, not skill-building.
- Does not address the student-facing question fully. A 5-minute closing reflection produces a single-sentence guidance per lecturer. The harder question (how to write assignment-level AI policies that scale across a course) is acknowledged but not solved.
- Does not name Daw & Fleming, ACT-R, KLI, or active inference in participant materials. The vocabulary policy is enforced.

## References (for facilitator deep-dive only)

- Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The Knowledge-Learning-Instruction framework: Bridging the science-practice chasm to enhance robust student learning. *Cognitive Science*, 36(5), 757-798.
- Koedinger, K. R., Booth, J. L., & Klahr, D. (2013). Instructional complexity and the science to constrain it. *Science*, 342(6161), 935-937.
- Pearl, J. (2009). *Causality: Models, reasoning, and inference* (2nd ed.). Cambridge University Press. (Chapter 1 on intervention vs. observation.)
- Daw, N. D., & Fleming, S. M. (relevant work on second-order metacognition and confidence; specifically the action-as-input arguments).
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review*, 31(2), 261-292. (For element interactivity as the substrate concept.)
- Vosniadou, S., & Skopeliti, I. (2014). Conceptual change from the framework theory side of the fence. *Science & Education*, 23(7), 1427-1445. (For the coherent-intuitive misconception type.)
- Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3), 379-424. (For the productive-failure framing, optionally available in closing.)
- Kirschner, P. A., & van Merriënboer, J. J. G. (2013). Do learners really know best? Urban legends in education. *Educational Psychologist*, 48(3), 169-183. (For the "skills in 3 hours" critique.)

The bibliography in `bibliography.bib` and `ai-for-research.bib` (Zotero-managed) holds the full citation set; do not edit those files directly.

## Companion documents

- `instructor-notes/spec-sheet-statistics-internal.md` — full theoretically-named version of the worked example walked through in Block 1.
- `instructor-notes/spec-card-statistics-internal.md` — the previous design's worked example, kept as historical reference.
- `2026-05-06-advanced-workshop-design.md`, `2026-05-06-spec-card-redesign.md`, `2026-05-07-redesign-comparison.md` — design history.
