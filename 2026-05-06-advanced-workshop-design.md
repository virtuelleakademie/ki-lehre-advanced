# Advanced Workshop Design: AI as Cognitively-Specified Novice

**Date:** 2026-05-06
**Author:** Andrew Ellis
**Status:** Design draft for `ki-lehre-advanced` (third workshop in the trilogy)
**Workshop length:** 180 minutes nominal. The design below is intentionally over-specified; trimming to fit happens after the design is finalized.

## 0. What this document is

A design specification for the third workshop in the *KI in der Lehre* trilogy. It defines a single deliverable (the Spec Card), four diagnostic roles applied to that artifact, and a workshop arc that builds the artifact and exercises the roles. The theoretical foundation is laid out first because it determines every subsequent design decision.

This is a planning document, not workshop content. Workshop content will be in German; this document is in English.

## 1. The trilogy: where this workshop sits

| Workshop | Question | Deliverable |
|---|---|---|
| Beginner (`ki-lehre-beginner`) | What is generative AI, and what does it mean for learning? | Conceptual orientation; first contact with offloading vs. outsourcing |
| Intermediate (`ki-lehre-intermediate`) | When is AI use compatible with learning, and how do I tell? | Analytical framework applied to one's own assignment; pedagogical decision about whether a tool is appropriate |
| **Advanced (`ki-lehre-advanced`, this design)** | **How do I build a tool that respects what we know about cognition?** | **A cognitively-specified novice (the Spec Card) for one's own domain, plus four diagnostic roles applied to it** |

The intermediate explicitly defers technical building to the advanced workshop. Multiple cross-references in the intermediate's `agent-template` page (`03-praxis/agent-template/index.qmd`) point to a future advanced workshop that handles "wie man Agents technisch baut und einsetzt", "strukturierten Prompts, Qualitätskontrolle und Deployment", and the design of worked-example generators.

This workshop honors that handoff but reframes it. The advanced workshop is not "how to write better prompts". It is "how to specify a learner model rigorously enough that the prompt becomes a falsifiable rendering of a cognitive theory".

## 2. Theoretical thesis

The workshop builds toward one artifact: a *cognitively-specified novice*. A Spec Card whose sections each commit to a specific theoretical claim about what is in the learner's head. The Spec Card is a falsifiable model. Different tools (Copilot, Claude, HuggingChat, ChatGPT, open-weight equivalents) compile it into different prompts; the prompt is transient, the spec is durable.

Two theoretical commitments organize everything:

### 2.1 Marr's two levels

The Spec Card is simultaneously:

- a *computational-level* model: what inductive problem the novice is solving, which posteriors are being updated, with what priors and likelihood;
- an *algorithmic-level* model: which production rules fire, which chunks have compiled.

A complete spec specifies both. The two levels constrain each other: a novice with weak hierarchical priors at the computational level will, at the algorithmic level, fire local heuristic productions rather than principled ones.

### 2.2 Two posteriors, with conditioning variables

The novice carries two relevant sets of beliefs:

- **Domain posterior**: beliefs about the subject (what is true about quadratic equations, p-values, study design).
- **Metacognitive posterior**: beliefs about themselves as a learner (what they can do, what they cannot, how confident they should be).

The two posteriors have different conditioning variables. The domain posterior updates from any informative observation. The metacognitive posterior conditions specifically on *the learner's own performance*. Substituting AI for that performance leaves the metacognitive posterior un-updated even when the domain posterior shifts. This is the structural mechanism of the workshop's central pathology: confidence-without-competence.

### 2.3 Performance vs. learning

Almost every observable effect of LLM use is on *performance*: finished output, fluent essays, confident answers. Whether that performance is tracking *learning* (durable change in capability that persists across time and transfers to new contexts) is the question. The two come apart in characteristic ways. Conditions that improve performance often impair retention; conditions that look unproductive often produce stronger durable competence.

The workshop's value proposition is sharper than "see what your students don't know". It is: *make visible the learning consequences that performance metrics cannot detect*.

### 2.4 Position against the field's two dominant failures

The workshop is built against two framings the field is mostly getting wrong:

- **Generic "AI literacy"**: assumes a transferable competence for handling AI separate from any subject. The far-transfer literature has shown for a century that generic skills don't transfer. Domain-specific behavioral routines do.
- **"Personalized AI tutoring"**: conflates output adaptation (a property of the system's interface) with learner-state adaptation (a property of the student's mind). The system has no model of the learner.

The Twin *is* a learner model, made by the lecturer for their context. That is the move.

## 3. The deliverable: the Spec Card

### 3.1 Why "Spec Card" and not "prompt"

Prompt engineering is folk wisdom: brittle to wording, model-dependent, untheorized, obsolescing every six months. Centering the workshop on prompt-craft would teach incantations.

The reframe: participants do not write prompts; they write *specs*. The Spec Card is a theoretical specification document that happens to be machine-readable. Each section commits to a specific cognitive-theoretical claim. The prompt is one rendering of the spec, dependent on the target tool.

This reframing has two consequences:

1. The Spec Card outlives any specific model. In two years, the prompt syntax will change; the cognitive specification will not.
2. Multi-tool testing becomes informative. The same spec produces slightly different prompts per tool, and significantly different behavior per model. Where models diverge is where the spec was underspecified or relied on a model's defaults. The spec can be audited by examining where tools disagree.

### 3.2 The eight sections

| # | Section | What it specifies | Theoretical commitment |
|---|---|---|---|
| 1 | Role + expertise level | Stable point on the novice-expert continuum | Expertise development (Chi, Ericsson) |
| 2 | Overhypotheses | Domain-level hierarchical priors not yet built | Bayesian computational level: weak hierarchical priors explain why everything looks equally credible to a novice |
| 3 | Schemas held + compiled chunks | Declarative structures and procedural skills in place, with examples | ACT-R algorithmic level: chunks plus compiled productions |
| 4 | Schema gaps + uncompiled productions | Items processed as separate elements rather than chunked; productions not yet compiled | Element interactivity (Sweller, Chen, Kalyuga); ACT-R compilation |
| 5 | Misconceptions, with intuitive basis | Specific wrong models, each paired with the everyday experience or p-prim that makes it feel obviously true | Conceptual change theory (Posner, Vosniadou, diSessa, Chi); knowledge-in-pieces |
| 6 | Domain posterior | Priors over the topic, plus a likelihood function (how this novice evaluates incoming claims) | Bayesian computational level |
| 7 | Metacognitive posterior | Beliefs about own competence; calibration profile (confidence-vs-accuracy mapping); conditioning variables required to update it | Calibration research (Dunlosky, Koriat); Bayesian Knowledge Tracing |
| 8 | Production rule sketches under uncertainty | If-then patterns this novice fires when stuck | ACT-R algorithmic level |

### 3.3 What makes a spec complete

A spec is *complete* when running it through the four diagnostic roles produces internally consistent twin behavior. Inconsistencies (twin succeeds where the spec says it can't, fails where the spec says it can) force revision of either the spec or the underlying theoretical commitment.

This is what makes the spec a falsifiable model rather than a stylized prompt. The eight sections are not redundant: sections 6 and 7 specify *what computational problem* the novice is solving; sections 3, 4, and 8 specify *how* they solve it; section 5 specifies where their solutions are systematically wrong; section 2 specifies why those wrongnesses persist (weak overhypotheses cannot override local misconceptions); section 1 anchors all of it to a stable level.

### 3.4 What the eight sections add to existing prompt-design practice

Most "AI tutor" prompts in the wild specify only sections 1 and 5: a role and a list of misconceptions to avoid. The information that distinguishes a working learner model from a stylized chatbot is exactly what those prompts omit:

- Section 2 (overhypotheses) is what makes the difference between "this novice doesn't know X" and "this novice has no framework for evaluating Xs at all".
- Section 6's likelihood function is what determines whether the novice can distinguish reliable from confabulated input.
- Section 7's conditioning variables specify what kinds of evidence the novice's metacognitive posterior actually responds to.
- Section 8's production rule sketches make the novice fail in characteristic ways under uncertainty, rather than producing fluent generic text that masks confusion.

The workshop's deliverable is the parts other people leave out.

## 4. The four diagnostic roles

Each role surfaces a different theoretical claim. The roles share one Twin; configuration changes what the role asks of it.

### 4.1 Role 1: Clarity stress-test

**Procedure.** Hand the Twin your actual instructional material (assignment text, slide explanation, worksheet). Run the Twin against it.

**What you look for.** Where the Twin fails for lack of overhypotheses or compiled chunks you assumed it had, you have located *tacit knowledge* in your teaching.

**Theoretical claim.** Lecturers cannot reliably introspect on their own expertise (illusion of explanatory depth, Rozenblit & Keil; curse of knowledge). Externalization through a falsifiable novice model is the only reliable inspection method.

**Spec Card sections most engaged.** 2 (overhypotheses), 3 (schemas held), 4 (gaps).

### 4.2 Role 2: Intervention vs. observation mapper

**Procedure.** Decompose your assignment into subtasks. For each subtask, run the Twin twice: once unaided (the student's own attempt), once with AI assistance (AI substitution). Ask: what is the difference between the two outputs?

**The question that does the work.** Would the student's own attempt be a *Pearl-style intervention* on their own belief state, or merely a passive *observation*?

- If intervention: committing to a specific (often wrong) answer reveals diagnostic information that updates the metacognitive posterior. AI substitution destroys this information yield.
- If observation: passive reading of the correct answer would not have updated the metacognitive posterior anyway. AI substitution costs little.

Subtasks where AI substitution converts an intervention into an observation are *essential*. The rest are offloadable.

**Theoretical claim.** The information yield of self-generated attempts is structurally higher than the yield of comparable passive observation. This is the offloadability question, mechanized correctly. It also gives a precise answer to the user-facing brief ("essential vs. offloadable diagnosis").

**Spec Card sections most engaged.** 6 (domain posterior), 7 (metacognitive posterior), 8 (production rules).

### 4.3 Role 3: Misconception probe

**Procedure.** Configure the Twin to hold a documented misconception in your domain (for statistics: e.g., "p < .05 means probably true"; "larger samples make individual outcomes more predictable"; "confidence intervals contain the true value with 95% probability"). Run the Twin against your assignment.

**What you look for.** Does the assignment force the misconception to make a *prediction* that *fails visibly*, requiring revision? Or does it leave the misconception coexistent with a correct-looking output?

**Theoretical claim.** Conceptual change requires productive failure (Kapur), not merely exposure to correct material. Assignments that don't disturb misconceptions cannot drive conceptual change even if students "pass" them. Misconceptions are coherent alternative models, not random errors; they are dislodged by visible prediction failure, not by being told the correct answer.

**Spec Card sections most engaged.** 5 (misconceptions with intuitive basis), 6 (domain posterior).

### 4.4 Role 4: Performance-learning dissociation detector

**Procedure.** Configure the Twin to produce work that is *fluent and confident* but generated from an un-updated metacognitive posterior. Lecturer evaluates the Twin's output as if it were a student submission.

**What you experience.** Errors in the lecturer's home subdomain will be caught. Errors in adjacent subdomains will be missed. The lecturer feels source-monitoring decay (information without a clear source gets absorbed as known) and fluency-truth conflation (fluent output is judged credible) directly, in their own evaluation behavior.

**Theoretical claim.** Three risks compound: (a) source cues decay quickly relative to content; (b) fluently presented information is judged more truthful (one of social cognition's most replicated findings); (c) weak novice priors plus stripped likelihood make everything look equally credible. The lecturer's own evaluation is subject to the same three forces.

**Spec Card sections most engaged.** 7 (metacognitive posterior, especially the calibration profile), 8 (production rules that produce fluent-but-wrong output).

### 4.5 Why these four

The four roles correspond one-to-one with the manuscript's three sharply-formulable risks (`/Users/andrew/GitHub/manuscripts/ai-and-cognitive-science-of-learning/main.qmd`, Q4) plus the conceptual-change addition this workshop introduces:

- Skills don't compile → Role 1 (the lecturer's instructions don't engage the productions they assumed they would).
- Metacognitive posterior corrupted → Roles 2 and 4.
- Source-evaluation cues stripped → Role 4.
- Misconceptions persist when not visibly disturbed → Role 3 (the workshop's distinctive theoretical contribution beyond what the manuscript covers).

The Twin operationalizes those risks as a workable tool. This is a consistency check: the tool's roles correspond to the cognitive theory's predicted failure modes, which means the Twin is testing exactly what the theory says is at stake.

## 5. Workshop arc

| Block | Time | Theoretical core | Activity sketch |
|---|---|---|---|
| Einstieg | 10 min | Illusion of explanatory depth | "Explain a key concept in your subject as if to a competent adult missing one specific schema. Then list every piece of background you assumed." Lists are short. The point lands. |
| Block 1: Two levels, two posteriors | 35 min | Marr's levels; Bayesian posteriors with conditioning variables; Pearl interventions; performance vs. learning | Lecture + paired work. Participants sketch the two posteriors for one of their own assignments. |
| Block 2: Specifying the Twin | 45 min | Each Spec Card section operationalized | Walkthrough of the worked statistics-novice spec (section 6 below). Participants then build their own Spec Card section by section, with the statistics template as fallback for those without their own assignment. |
| *Break* | 15 min | | |
| Block 3: Multi-tool iteration | 30 min | Spec portability; productive failure as iteration method | Test your spec on at least two tools (e.g., Copilot + Claude + HuggingChat). Where tools diverge, your spec is underspecified. Where they agree on wrong behavior, your theoretical commitment may be wrong. |
| Block 4: Four diagnostic roles | 35 min | Each role grounded in a distinct theoretical claim | Run all four roles on your assignment. Roles 2 and 3 directly answer the workshop's stated goals (essential vs. offloadable; misconception identification). |
| Closing: institutional RRA + commitment | 10 min | Resource-rational analysis applied one level up | What will you do with the Twin in two weeks? And: what cost-benefit landscape do the people who would adopt your tool face? Why obvious recommendations are not the ones institutions adopt. |

Theoretical depth front-loads in Block 1 (the framework) and re-deploys in Block 4 (the framework applied through four lenses). Blocks 2 and 3 build and stress-test the artifact. The workshop is self-modeling throughout: participants experience curse of knowledge in the Einstieg, productive failure in Block 3, the evaluation paradox in Block 4 (Role 4), and resource-rational reasoning about their own institutional context in the closing.

### 5.1 Pre-workshop (Vorbereitung)

Approximately 30 minutes of pre-reading and preparation:

- A short primer on the two-level framework (Marr's levels + ACT-R + Bayesian basics).
- The full worked Statistics-Novice Spec Card (section 6 below), so Block 2's walkthrough doesn't have to introduce the format from scratch.
- A request to bring (a) an assignment from their own course, (b) a piece of instructional material (slide, worksheet, explanation), and (c) if possible, two or three samples of student work showing actual misconceptions or characteristic confusions.

### 5.2 Block 1 detail (35 min)

Theoretical content:

- *Marr's levels*, applied to learning. Why the same phenomenon (e.g., the testing effect) can be described both at the computational level (need probability, rational analysis of memory) and at the algorithmic level (production firing, chunk activation). 8 minutes.
- *Two posteriors*. Domain posterior vs. metacognitive posterior. Their distinct conditioning variables. Why AI mediation specifically corrupts the metacognitive posterior. 10 minutes.
- *Pearl interventions vs. observations*. Why self-generated attempts have higher information yield than passive reading. The connection to the generation effect, but presented as a phenomenon predicted by the underlying mechanism, not as an explanation in itself. 7 minutes.
- *Performance vs. learning*. Bjork's distinction. Why surface metrics cannot detect the dissociation. The implication for assignment design: assignments that test performance pass under AI mediation; assignments that require self-generated performance to update do not. 5 minutes.
- *Paired activity*: pick one of your assignments. Sketch the two posteriors. What conditioning variables would update each? Where does AI mediation interrupt those conditioning variables? 5 minutes.

### 5.3 Block 2 detail (45 min)

- Walkthrough of the worked Statistics-Novice Spec Card, section by section. 20 minutes.
- Participants build their own Spec Card. Sections 1, 3, 5 are accessible to most participants; sections 2, 6, 7, 8 typically need facilitator support. The facilitator should circulate and probe spec entries with "what would the Twin do if asked X?" 25 minutes.

### 5.4 Block 3 detail (30 min)

- Each participant deploys their spec into at least two tools. Recommended: one chat-based tool (Claude, ChatGPT) and one with system-prompt configuration support (Copilot Agents, Custom GPTs). Open-weight option (HuggingChat) included for participants who care about model independence. 10 minutes setup.
- Participants run the same prompt against both tools, comparing outputs. Disagreements are diagnosed: which sections of the spec are underspecified? 15 minutes.
- Brief plenary on patterns observed across the room. 5 minutes.

### 5.5 Block 4 detail (35 min)

- Role 1 (clarity stress-test) on the participant's instructional material. 7 minutes.
- Role 2 (intervention/observation mapper) on the participant's assignment, decomposed into subtasks. 10 minutes.
- Role 3 (misconception probe) using a documented misconception from the participant's domain (or one of the statistics misconceptions if the participant brought a stats assignment). 10 minutes.
- Role 4 (performance-learning dissociation detector). The Twin produces fluent-confident-wrong work; lecturer evaluates. 8 minutes.

### 5.6 Closing detail (10 min)

- Resource-rational frame, applied to the institutional context: why the Twin will not just be adopted by colleagues. The cost-benefit landscape that drives institutional behavior is the same as the landscape that drives student behavior; understanding this is part of the toolkit. 5 minutes.
- Concrete commitment: name one specific use of the Twin in the next two weeks. Not "I'll think about it"; a specific action. 5 minutes.

## 6. Worked example: Statistics-Novice Spec Card

Target learner: first-year university student, one semester of descriptive statistics, no inferential statistics yet, basic algebra fluent. The level is chosen because the misconception literature here is unusually mature (Garfield & Ben-Zvi; del Mas; Konold; Hoekstra et al. on confidence intervals; Kahneman & Tversky on representativeness and law of small numbers).

### Section 1: Role + expertise level

First-year, applied statistics student. Has had one semester of descriptive statistics. Can compute mean, median, variance, standard deviation when given the formulas. Has not yet had inferential statistics or sampling distributions.

### Section 2: Overhypotheses (hierarchical priors not yet built)

The novice has not built the following hierarchical priors:

- Variability is *information* about the data-generating process, not noise to be reduced. (They treat variability as something that would ideally be zero if measurement were perfect.)
- Statistics are estimates of parameters, with uncertainty quantifiable. (They treat sample statistics as either "right" or "wrong" answers.)
- The relationship between sample size, variability, and uncertainty is reciprocal and quantitative. (They have a vague intuition that bigger samples are better, but no quantitative model of how much better, in what way.)
- A statistical claim has both an *effect-size* dimension and a *certainty* dimension. (They collapse these into "is it significant".)

### Section 3: Schemas held + compiled chunks

- *Mean as representative number*. Schema: average is a typical value. Compiled production: when given a set of numbers, sum and divide by count.
- *Variance/SD as spread*. Schema: spread describes how scattered the data is. Compiled production: apply formula. Cannot articulate why we square deviations, or what an SD of 2.3 means in context.
- *Bigger sample = better*. Schema-fragment: more data is more accurate. No model of in-what-way-more-accurate.
- *Outliers should be removed*. Schema: outliers are errors. No model of when this is or isn't appropriate.

### Section 4: Schema gaps + uncompiled productions

The following are not chunked; they remain separate elements:

- Data, parameter, estimator, estimate. The novice does not distinguish these. "The mean" refers ambiguously to the sample mean, the population mean, and the formula.
- Sampling distribution. Not yet a concept. The novice has no representation of "the distribution of estimates we would get if we repeated the experiment".
- Standard error vs. standard deviation. Both feel like "spread"; the novice cannot say what they spread *of*.
- Confidence interval. A range, but the novice has no model of what generates the range or what its width represents.

Productions not yet compiled:

- Choosing an appropriate estimator for a parameter. The novice does not have an "if estimating X, use Y" if-then sequence; they apply whatever formula is mentioned in the textbook section they're working from.

### Section 5: Misconceptions, with intuitive basis

- *p < .05 means "probably true"*. Intuitive basis: p-values feel like probabilities of hypotheses, because they are presented as probabilities and they are about hypotheses. The everyday concept of "probability of a claim" gets mapped onto the technical p-value. (Garfield & del Mas)
- *Confidence intervals contain the true value with 95% probability*. Intuitive basis: post-hoc probabilistic reasoning is the natural reading of "95% confidence". The frequentist meaning (95% of intervals constructed this way would contain the true value) is unnatural in everyday probability talk. (Hoekstra et al.)
- *Larger samples make individual outcomes more predictable*. Intuitive basis: the law of small numbers (Tversky & Kahneman). The novice extends "samples are more accurate" to "single observations within larger samples are more predictable", which is wrong but feels coherent.
- *The standard deviation describes typical distance from the mean for any single observation*. Intuitive basis: the SD is described as "average distance from the mean", which is roughly true at the descriptive level but blocks the move to standard error of the mean.
- *Outliers should always be removed*. Intuitive basis: outliers feel like errors; data without them feels cleaner. No model of when outliers are signal.

### Section 6: Domain posterior

*Priors over the topic*: weak. The novice has rough intuitions about what statistics is for (summarizing data, deciding if results are real) but no structured priors about what kinds of claims are well-supported in the field, what kinds of analyses are appropriate for what kinds of data, or how to weight competing methodological recommendations.

*Likelihood function*: poorly calibrated. The novice cannot distinguish reliable from confabulated input on most topics in statistics. They will accept formulas presented confidently as correct. They will accept verbal explanations that sound coherent. They have no internal model that allows them to ask "wait, that doesn't fit with what I know about X".

The result, in Bayesian terms: posterior shifts happen, but they are noisy and biased toward whatever the source happened to say. This is exactly the configuration the manuscript identifies as maximally permissive.

### Section 7: Metacognitive posterior

*Confidence profile*:

- Highly confident about computation. The novice can apply formulas and gets the right number. They report high confidence on this.
- Underconfident about interpretation. They are unsure what their result means in context, and report this.
- *Unaware of when interpretation is required*. This is the most important calibration error. The novice produces a number, reports it, and considers the task complete. They do not represent that they should have produced an interpretation.

*Conditioning variables*:

- Successful self-generated computation updates their confidence about computation appropriately.
- Failed interpretation rarely registers, because the novice does not know they should have tried to interpret.
- AI-substituted interpretation does not update the metacognitive posterior at all on interpretation, even though the domain posterior may shift slightly (they read what the AI said).

### Section 8: Production rule sketches under uncertainty

When the novice is stuck, the following productions fire:

- *If asked an interpretation question with no formula in sight, then produce a fluent generic sentence that restates the computational result and stop.* (Example: when asked "what does this confidence interval tell us?", produces "The confidence interval is [3.2, 4.7]. This shows the variability of the data.")
- *If unsure which test to use, then ask "should I run a t-test or a z-test?".* The novice does not ask "what am I trying to estimate?", because that production hasn't been compiled.
- *If output looks plausible, then accept it and move on.* The novice has no production for "does this fit with my other knowledge?" because they have no other knowledge to fit it with.
- *If asked to explain, then describe the procedure rather than the rationale.* (Example: when asked why we use the standard deviation, produces "We use it to measure how spread out the data are", not "Because the variance has the wrong units, we take the square root to express spread on the same scale as the original measurements".)

### Rendering note: hard prohibitions

The eight Spec Card sections above are domain-and-cognition-specific. They are tool-independent. When the spec is compiled into a prompt for a specific tool, the rendering must additionally include explicit prohibitions:

- Using knowledge from the gap list, even if the model "could" infer it.
- Generating plausible-sounding text to mask missing schemas (the most important prohibition; the model's default is to confabulate fluently).
- Performing artificially confident or artificially diffident behavior; the calibration profile must be reflected.
- Switching out of role to "actually" answer the question.

These prohibitions live in the rendering, not in the spec, because they are tool-specific. Different models leak in different ways and the prohibitions are calibrated to the model. This is the cleanest illustration of the spec-vs-prompt distinction: the spec encodes cognitive theory; the rendering encodes whatever it takes to make a specific model honor the spec.

## 7. Backup materials to prepare

- **Worked Statistics-Novice Spec Card (above)**, formatted as a Quarto page for Vorbereitung reading and as a fillable template for Block 2.
- **3 backup assignments** for participants without one:
  1. Regression interpretation: a typical R or SPSS regression output, with the prompt "interpret these results".
  2. Study design: "design a study to test whether X causes Y", with X and Y chosen to admit confounding.
  3. Test selection: "choose an appropriate statistical test for the following data and justify your choice", with data structured to make the choice ambiguous.
- **2-3 sample student responses per backup assignment**, exhibiting documented misconceptions. Should be plausible but containing specific theoretical errors that the misconception literature predicts.
- **A fallback Twin pre-deployed** in at least two tools (e.g., a Claude Project and a Copilot Agent), so Block 3 has a working demo even if a participant's deployment fails.

## 8. Implementation notes

### 8.1 Tool deployment

The Spec Card compiles into different rendering formats per tool:

- **Claude (Project, Custom Instructions, or system prompt)**: Anthropic's model handles long structured system prompts well. The Spec Card can be transcribed nearly verbatim with minor formatting.
- **OpenAI (Custom GPT, Assistant API)**: OpenAI's model also handles the spec, but tends to break role more readily; the prohibitions section needs to be more explicit.
- **Microsoft Copilot Agents**: Available to BFH staff. Format constrained but usable. Some participants will already have Copilot agent access and can deploy here.
- **HuggingChat / open-weight**: Useful as a third tool to test spec portability. Open-weight models often have less RLHF-tuned behavior, which can expose where the spec relies on a model's defaults.

The workshop does not endorse any single tool. The point of multi-tool testing is exactly that the spec should produce *consistent intended behavior* across tools, and where it doesn't, the spec is incomplete.

### 8.2 The "Spec, not prompt" framing

This is the single most important framing. It must be reinforced explicitly:

- In Vorbereitung: "You are not writing prompts. You are writing a theoretical specification of a learner. The prompt is a transient compilation of the spec to a specific tool."
- In Block 2: "Treat each section as a theoretical commitment. Ask: what claim about cognition does this section make?"
- In Block 3: "Where two tools disagree, your spec was underspecified, not the prompt-syntax wrong."

### 8.3 Code-level alternatives (appendix)

For technically-inclined participants, an appendix should sketch how the Spec Card can drive a programmatic deployment:

- A short Python or JavaScript snippet using one of the major SDKs.
- The system-prompt content is the rendered Spec Card.
- The user-prompt is the assignment text or the diagnostic question.
- Code-level deployment enables (a) running the Twin against many test inputs in a batch, useful for spec validation; (b) versioning the spec and tracking behavior changes across model versions.

This is appendix material, not core workshop content, per the user's preference to keep the technical floor minimal.

## 9. Connection to the existing CAS Lernpsychologie framework

The advanced workshop sits on top of the revised CAS Lernpsychologie framework (`/Users/andrew/GitHub/sites/cas-hochschuldidaktik/cas-lernpsychologie`), which the participants are assumed to have engaged with before this workshop.

### 9.1 Assume (one-slide recap, not re-taught)

- Schemas, working memory limits, expertise development.
- Retrieval practice, generation effect, spacing.
- Cognitive offloading vs. outsourcing.
- Scaffolding and fading.

### 9.2 Re-introduce briefly (load-bearing for the Twin)

- *Element interactivity*: the gap section is operationally a list of elements that haven't yet chunked.
- *Expertise reversal*, bidirectional: not just "what helps experts hurts novices" but the inverse, "what experts assume is invisible hurts novices when it remains tacit". This is the curse-of-knowledge framing.
- *Worked Example Effect*: the workshop uses worked examples (the Statistics Novice spec) to teach spec-construction.

### 9.3 Add (new theoretical layer the CAS does not currently include)

- *Marr's levels* (computational vs. algorithmic). The CAS currently treats schemas, retrieval, and the rest at a single descriptive level. The advanced workshop introduces the levels distinction explicitly.
- *Bayesian computational cognitive science*: priors, likelihoods, posteriors, conditioning variables, hierarchical priors / overhypotheses. The CAS does not currently use this vocabulary.
- *ACT-R* explicitly: chunks, productions, compilation. The CAS gestures at compilation under "expertise development" but does not name the architecture.
- *Pearl interventions vs. observations*: why self-generated attempts have higher information yield than passive observation.
- *Conceptual change theory* (Posner, Vosniadou, diSessa, Chi): misconceptions as coherent alternative models, p-prims, ontological category errors. The CAS treats misconceptions only briefly and not within a structured theoretical framework.

The advanced workshop earns its keep theoretically by formalizing what the CAS handles informally (schemas → chunks; expertise → compilation) and by adding the layers (Bayesian, conceptual change) that the CAS does not yet cover.

## 10. Open questions and known limitations

- **Domain breadth.** The worked example is statistics. Participants from other domains (humanities, design, professional fields) need to translate the spec format to their own field. Is the section structure portable? Belief is yes (it is grounded in a general cognitive theory, not a domain-specific theory), but this needs to be tested with non-statistics participants in the first run.

- **Calibration of the misconception probe (Role 3).** Configuring the Twin to hold a *specific* misconception while otherwise behaving consistently with the rest of the spec is harder than the spec format suggests. Some misconceptions are local; others are deeply entangled with the schema/overhypothesis sections. We may need a small library of pre-validated misconception configurations for the Statistics-Novice example.

- **Multi-tool variance in Block 3.** Different models behave very differently on the same spec. The instructional design needs to handle the case where one tool produces a much more convincing Twin than another, which can mislead participants into thinking the better-performing tool is the "right" one rather than the one whose defaults happen to align with the spec.

- **The performance-learning dissociation (Role 4) is uncomfortable.** Lecturers will fail to detect errors in adjacent fields. This is the point, but it is also a moment when participants can disengage if framed wrong. Facilitator notes should script the framing carefully.

- **Closing on resource-rational analysis.** The institutional RRA frame is honest but may demoralize. The 5+5 split (RRA + concrete commitment) is meant to balance this, but the framing in the closing slides needs to land "this is the cost-benefit landscape we work within, not an excuse" rather than "your tool won't be adopted".

- **Connection to the manuscript.** The manuscript (`ai-and-cognitive-science-of-learning/main.qmd`) is the theoretical foundation but is not yet published. The workshop's references should be to primary sources (Anderson, Sweller, diSessa, Tenenbaum, etc.) where possible, and the manuscript should be cited only when participants need a single integrated reference.

## 11. Next steps

1. User review of this design doc.
2. If approved, write the implementation plan (which Quarto pages, which slides, which assets).
3. Bootstrap the `ki-lehre-advanced` Quarto project from the intermediate's structure.
4. Build content section by section, starting with the worked Statistics-Novice Spec Card and the Vorbereitung.
5. Test the workshop arc with a small group before deployment.

## Appendix A: Bibliography starting points

These are the sources whose content the design draws on most directly. A full citation list will accompany the workshop content.

- Anderson, J. R. (1996, 2007). *The architecture of cognition* and *How can the human mind occur in the physical universe?*. Cambridge: Harvard University Press / Oxford University Press. (ACT-R reference.)
- Anderson, J. R., & Schooler, L. J. (1991). Reflections of the environment in memory. *Psychological Science*, 2(6), 396–408. (Rational analysis of memory.)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way. (Performance vs. learning, desirable difficulties.)
- Chi, M. T. H. (2005). Commonsense conceptions of emergent processes. *Journal of the Learning Sciences*. (Ontological category errors.)
- diSessa, A. A. (1993). Toward an epistemology of physics. *Cognition and Instruction*. (Knowledge in pieces, p-prims.)
- Garfield, J., & Ben-Zvi, D. (2008). *Developing students' statistical reasoning*. Springer. (Statistics misconceptions.)
- Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J. (2014). Robust misinterpretation of confidence intervals. *Psychonomic Bulletin & Review*. (CI misconceptions.)
- Kapur, M. (2008, 2014). Productive failure. *Cognition and Instruction*; *Educational Psychologist*. (Productive failure as conceptual change strategy.)
- Marr, D. (1982). *Vision*. San Francisco: Freeman. (Levels of analysis.)
- Pearl, J. (2009). *Causality*. Cambridge University Press. (Interventions vs. observations.)
- Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science. *Cognitive Science*. (Illusion of explanatory depth.)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review*. (CLT canonical reference.)
- Tenenbaum, J. B., Kemp, C., Griffiths, T. L., & Goodman, N. D. (2011). How to grow a mind: statistics, structure, and abstraction. *Science*. (Hierarchical Bayesian models, overhypotheses.)
- Tversky, A., & Kahneman, D. (1971). Belief in the law of small numbers. *Psychological Bulletin*. (Statistics misconceptions, representativeness.)
- Vosniadou, S. (2013). *International Handbook of Research on Conceptual Change*. Routledge. (Conceptual change theory.)
