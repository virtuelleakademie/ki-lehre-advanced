# Spec Sheet: Statistics Subtask (Internal-Precise Register)

Audience: workshop instructors and co-facilitators. Theoretical naming preserved so each section's commitments are auditable. The participant-facing version is at `workshop/block-1-theorie-und-beispiel/worked-example-statistics.qmd`.

## Subtask anchor

> A study reports a correlation of $r = 0.3$ between sleep duration the night before an exam and exam performance, based on a sample of 200 first-year students. Interpret this finding: what does it claim substantively, and how well-supported is the claim?

This subtask is chosen because:

- It exercises the magnitude-to-substantive translation, which is where principled (KLI: understanding-and-sense-making) KCs live.
- It admits at least one well-documented coherent misconception ($r$ vs. $r^2$ confusion) and one cohesive intuitive misconception (effect-size convention misapplication).
- The misconception literature in introductory statistics is mature (Garfield & Ben-Zvi; del Mas; Cohen 1988 for effect-size conventions; Hoekstra et al. on confidence-interval misinterpretation), making it tractable for the LLM-as-hypothesis-generator step.
- The subtask is short enough to demo in the 35-minute Block 1 walkthrough.

## Section A: subtask, course context, learning goal

The course context locates the learner: first-year, post-descriptive-stats, pre-inferential-stats. This anchor is necessary for granularity decisions in section B (KCs that depend on inferential statistics are out of scope; KCs that depend on descriptive statistics are assumed available).

The stated learning goal ("interpret the correlation in a substantive context") cleanly separates *computation* (already assessed in earlier subtasks) from *interpretation* (this subtask). The separation is what licenses many of the section B entries: we are testing only what this subtask is for.

## Section B: knowledge components by KLI type

Five KCs, mapped to the KLI typology.

### KC 1: $r \in [-1, +1]$

- **KLI type:** memory and fluency (Faktenwissen). A bounded-range fact that must be retrievable from memory to anchor magnitude judgements.
- **Anderson/ACT-R correlate:** a declarative chunk; cheap to acquire; the question is whether it's been consolidated enough to fire on cue when the student sees "$0.3$" in context.
- **Why it earns its place:** without it, the magnitude $0.3$ is unanchored; the student cannot calibrate "much" or "little" against the bounded scale.
- **Acquisition signature:** retrieval practice; the standard "ask the bounds without giving them" exercise.

### KC 2: $r$ measures linear association, not causation

- **KLI type:** induction and refinement (Klassifikationswissen). A boundary-condition concept that must be recognised across instances to discriminate appropriate from inappropriate inferences.
- **Anderson correlate:** declarative knowledge with classification productions ("when stem says X, do not infer Y"); acquired through multiple cases of correlation-without-causation and counter-examples.
- **Why it earns its place:** the subtask asks for interpretation; without this KC, the student slides into causal language ("more sleep leads to better performance") without flagging the inferential gap.
- **Acquisition signature:** multiple varied examples and non-examples; classification practice across instances. Self-explanation can substitute for some of the inductive work but not all of it.

### KC 3: effect-size magnitude is context-dependent

- **KLI type:** understanding and sense-making (Erklärungswissen). A principle whose application depends on understanding *why* domain context calibrates the magnitude.
- **Anderson correlate:** principled production rule whose firing condition includes "what discipline is this?" as a contextual variable; acquisition requires self-explanation of the rule plus contrastive cases (same $r$ in different domains).
- **Why it earns its place:** the subtask asks for substantive interpretation, not just numerical magnitude. Without this KC, the student either dismisses $r = 0.3$ as small (Cohen 1988 mechanically applied) or accepts it as "moderate" without questioning whether Cohen's conventions calibrate well in education research (where typical effects are substantially smaller than the social-psych contexts Cohen drew from).
- **Note:** marked V (vermutet) in the participant version because the lecturer's claim is a hypothesis about novice statistical reasoning; varies by population.

### KC 4: effect size and uncertainty are separate dimensions

- **KLI type:** understanding and sense-making (Erklärungswissen). The two-dimensional structure of statistical claims (effect + sampling uncertainty) is conceptually rich.
- **Anderson correlate:** principled understanding requiring multiple linked productions; sampling distributions provide the bridge but are not yet in the curriculum at this stage. Therefore acquisition is incomplete by design — this is a KC the assignment partially probes for and the curriculum partially supplies.
- **Why it earns its place:** the assignment names $n = 200$ explicitly. Without this KC, the student collapses size and certainty into a single judgement.
- **Pedagogical note:** this is the place where the absence of inferential statistics in the prerequisite makes itself felt. The assignment can probe whether the student notices the two dimensions; it cannot probe full mastery without the missing prerequisite.

### KC 5: $r^2$ is not $r$

- **KLI type:** memory and fluency, but with operational consequences (Faktenwissen). The fact $r^2 \neq r$ is simple; its consequences (variance-explained translation) are not.
- **Anderson correlate:** declarative chunk with a strong production rule attached ("when interpreting magnitude as 'percent explained', square first"); without the production, the chunk doesn't fire when needed.
- **Why it earns its place:** the most documented coherent misconception in this subtask space ($r$-as-percent) hinges on this KC's absence.
- **Acquisition signature:** retrieval practice plus worked examples that contrast $r$ and $r^2$ explicitly.

## Section C: misconceptions

Three misconceptions, with intuitive bases identified per Vosniadou/diSessa/Chi conceptual-change tradition.

### Misconception 1: $r = 0.3$ means 30% explained

- **Type:** coherent-intuitive (Vosniadou framework theory; intuitive ontology of "fraction" mapped onto correlation).
- **Intuitive basis:** the everyday concept of "X% of Y" maps onto any number between 0 and 1; the cognitive cost of distinguishing $r$ from $r^2$ is non-trivial because both numbers are "between zero and one and feel proportion-like."
- **Documentation in the literature:** widely reported in del Mas, Garfield, et al.; confused-r-with-r-squared is a textbook misconception in introductory statistics.
- **Discrimination by the assignment:** depends on whether the rubric explicitly distinguishes $r$ from $r^2$. If the rubric accepts "moderate effect" without checking the percent-explained translation, the misconception slips through.

### Misconception 2: large $n$ implies precise estimation

- **Type:** coherent-intuitive (Tversky & Kahneman, "law of small numbers"; the over-extension of "more is better" to "more is precise").
- **Intuitive basis:** the everyday intuition that "more data = more reliable" is roughly correct in many cases but mislocates the relationship as monotonically tight rather than reciprocal in a quantifiable way. Without the standard-error machinery (which is post-curriculum), the student has no quantitative model of uncertainty.
- **Documentation in the literature:** Tversky & Kahneman 1971; replicated in education-research contexts.
- **Discrimination by the assignment:** partial. The assignment names $n = 200$ but does not explicitly require uncertainty quantification, so a student holding this misconception can answer competently in surface terms. Marked V (vermutet) because we are conjecturing it applies to this novice population.

### Misconception 3: $r = 0.3$ is small, therefore practically negligible

- **Type:** surface (the mechanical application of Cohen's conventions without context calibration).
- **Intuitive basis:** less intuitive-driven than rule-driven; the student has memorised "Cohen says $0.3$ is medium" and applies it as a label rather than as an interpretive starting point.
- **Documentation in the literature:** the Cohen-conventions-misuse pattern is widely commented in methods reform literatures (Funder & Ozer 2019; Lakens 2013).
- **Discrimination by the assignment:** weak. A response that dismisses $r = 0.3$ as "small, therefore unimportant" is not factually wrong, just thin. Whether it counts as misconception depends on the rubric's depth requirement.

## Section D: prior-knowledge gaps

Three gaps, marked with curriculum-source notes.

### Gap 1: effect-size conventions are disciplinary, not universal

Curriculum source: Cohen's $0.1/0.3/0.5$ scheme is mentioned in the module but without disciplinary calibration discussion. The student carries the labels but not the qualifying caveat that education research effects are typically smaller than social-psych benchmarks Cohen drew from.

### Gap 2: "linear association" as a specific, not general, relationship

Curriculum source: should be in the correlation block of the current module. If this gap is widespread, it indicates the lecture didn't emphasise that $r$ misses non-linear relationships.

### Gap 3: sample $r$ vs. population $\rho$

Curriculum source: would be covered in the upcoming inferential statistics module. Knowable as a gap at this stage; the student treats $r = 0.3$ as the correlation rather than as an estimate.

## Section E: falsifiability note

The note specifies: if students who the lecturer would otherwise rate as competent correlation interpreters systematically fail this subtask, KC 3 is probably not what the assignment is testing. This is the workshop's characteristic move — converting a confident-looking decomposition into a falsifiable one by specifying *what would refute it*.

The pedagogical force: a spec sheet without a falsifiability note is, for our purposes, just a plausible document. The note makes it an empirical instrument with conditions for revision.

## Pruning protocol entries

Three documented LLM proposals rejected, with theoretical reasons:

1. **"Knows the concept of probability"** — granularity violation. KCs in the KLI tradition are operationalisable at the level where practice transfers; "concept of probability" is too abstract to drive acquisition or be falsified.
2. **"Knows that correlation does not imply causation, but is closer to causation in controlled studies"** — content error. The proposal smuggled a popular-science partial-truth that does not hold at first-year level and confuses the inferential gap. Pruned to keep the Spec Sheet honest about what is and isn't licensed.
3. **"Understands $p$-values and their interpretation"** — out-of-scope. The course context names inferential statistics as not yet covered; this KC is anachronistic.

The pruning entries are pedagogically the most important demonstration in Block 1. Walking through them aloud — with reasons stated — is what teaches participants the validation discipline.

## Reactive simulation analysis

The reactive simulation prompts the LLM to read the question stem as a learner missing KC 1 ($r$ bounded range). The expected output (and the example given in the participant page) reports confusion at:

- The unanchored magnitude of $0.3$.
- The inability to compare to "stronger" or "weaker" correlations without a scale.
- Indirect propagation into the $n = 200$ judgement (without scale anchoring, sample-size adequacy is also unclear).

The pedagogical surplus: the simulation surfaces an *assignment-design* issue (the assignment assumes the bounded range without restating it) that the lecturer might not have noticed. This is the curse-of-knowledge moment in operational form.

The instructor walking through this in Block 1 should explicitly note that the simulation's value is **not the simulated answer itself but the gap it reveals between what the assignment assumes and what it states**.

## Productive simulation analysis

The productive simulation prompts the LLM to produce an answer with Misconception 1 ($r = 0.3$ means 30% explained). The expected output is a fluent, internally-consistent answer that translates the correlation into a percent-explained claim and reasons forward consistently from there.

The two diagnostic features identified in the example output:

1. The direct numerical translation $r \to 30\%$.
2. The complementary "70% other factors" inference (which requires the variance-summing arithmetic that follows from $r$-as-proportion).

The instructor walking through this should explicitly note the meta-finding: a hurried lecturer who attends only to surface ("moderate effect, mentions sample size") will miss the misconception. The simulation thus tests both the *student's* understanding and the *grader's* attention.

## Connection to the workshop's softened metacognitive claim

Section E's falsifiability note plus the productive simulation together operationalise the softened form of the workshop's central claim: AI substitution removes the action-contingent inputs to second-order metacognition. The student who reads an AI-generated correct interpretation does not commit to an interpretation themselves; the second-order computation does not run on this episode.

This is *not* named in participant materials. It surfaces in the closing reflection ("which subtasks generate the input the metacognitive computation needs?") as the intervention/observation question. The lecturer who has built this spec sheet will realise that the interpretation subtask is intervention-required for the substantive-translation KC: the student must commit to an interpretation for the metacognitive update on "I can interpret correlations" to register.

## Audit trail to the workshop's pedagogical moves

| Workshop move | Spec sheet section it engages | Pedagogical purpose |
|---|---|---|
| Block 1 KC inventory walkthrough | Section B + pruning protocol | Models the validation discipline before participants attempt it |
| Block 1 reactive simulation | Section D + Block 4 closing | Surfaces tacit assumptions in assignment writing; operationalises curse of knowledge |
| Block 1 productive simulation | Section C + falsifiability | Tests assignment discrimination; demonstrates the grader-attention dimension |
| Block 2 own-spec construction | All sections | Independent practice with the validated workflow |
| Block 3 system-prompt rendering | Sections B, C, D map to prompt placeholders | Shows the spec/prompt distinction operationally |
| Closing intervention/observation reflection | Section B (per-KC tagging) | Applies Pearl's distinction to assignment subtasks; produces actionable AI-policy guidance |

## What this worked example deliberately does not do

- Does not attempt full coverage of the introductory-statistics misconception literature. Three misconceptions is enough for the demonstration; more would push the worked example past the 35-minute budget.
- Does not engage Bayesian statistical interpretation, despite the relevance. The audience is novice and the curriculum is frequentist; introducing a Bayesian framing here would be a category error in the participant context.
- Does not specify a complete rubric for grading the subtask. The spec sheet is for cognitive analysis, not for assessment design (though the analysis informs assessment).
- Does not propose a redesigned subtask. The spec sheet's purpose in Block 1 is to demonstrate the methodology, not to model assignment redesign. Some natural next-step suggestions appear in the participant page's "Konsequenzen für die Aufgabenbewertung" callouts but are not the deliverable.

## Companion documents

- `workshop/block-1-theorie-und-beispiel/worked-example-statistics.qmd` — participant-facing version (German, theory unnamed).
- `workshop/spec-sheet-template/index.qmd` — the empty worksheet participants fill in Block 2.
- `workshop/spec-sheet-template/prompt-scaffolds.md` — the five LLM prompts used to populate the worksheet.
- `workshop/spec-sheet-template/system-prompt-template.md` — the rendering template for Block 3.
- `instructor-notes/workshop-redesign-notes.md` — overall theoretical commitments and facilitator moves.
