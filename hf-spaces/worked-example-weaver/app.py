# ruff: noqa
"""
Interactive Exploration: Cognitive Load Theory & AI-Generated Worked Examples
Five hands-on labs to understand how to design educational AI tools

Built for embedding in Quarto workshop materials
"""

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from openai import OpenAI
    from pydantic import BaseModel, Field
    from typing import Literal
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    return BaseModel, Field, OpenAI, mo, os


@app.cell
def _(mo):
    mo.md("""
    # 🧪 Interactive Exploration Lab
    ## Designing AI Tools Grounded in Cognitive Load Theory

    Welcome to the **interactive exploration**! This isn't a complete tool—it's a laboratory
    where you'll experiment with the key design decisions that make AI educational tools effective.

    ### What You'll Explore

    Through 5 hands-on labs, you'll discover:

    1. 🎨 **Prompt Design Lab** - How prompt engineering shapes learning
    2. ⚖️ **Personalization A/B Test** - Feel the cognitive load difference
    3. 🏗️ **Data Model Designer** - What makes examples "worked"
    4. 🎛️ **Parameter Playground** - Model settings and pedagogy
    5. 🔍 **CLT Analyzer** - Evaluate examples with a critical lens

    ### Why This Matters

    You could just use a tool. But **understanding the design principles** lets you:
    - Adapt tools to your specific domain
    - Critique and improve existing AI educational tools
    - Design new tools grounded in learning science

    **Ready to explore?** Let's start with the setup.
    """)
    return


@app.cell
def _(OpenAI, os):
    """Setup: Initialize OpenAI client"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return (client,)


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 🎨 Lab 1: Prompt Design Laboratory

    **Learning Question**: How does prompt engineering affect the quality of worked examples?

    ### The Experiment

    You'll see **two prompts** - a basic one and one grounded in CLT principles.
    Try editing them and see how the outputs change.

    **Key insight**: The prompt IS your pedagogical design encoded in language.
    """)
    return


@app.cell
def _(BaseModel, Field):
    """Simple data model for Lab 1"""

    class SimpleExample(BaseModel):
        """Minimal structure for prompt comparison"""
        problem: str = Field(description="The problem to solve")
        solution: str = Field(description="Step-by-step solution")
        explanation: str = Field(description="Why this approach works")
    return (SimpleExample,)


@app.cell
def _(mo):
    """Lab 1: Prompt inputs"""

    mo.md("### Try These Prompts")

    basic_prompt = mo.ui.text_area(
        label="Basic Prompt (no pedagogical grounding):",
        value="""Create an example problem about Python for loops and solve it step by step.""",
        full_width=True,
        rows=3
    )

    clt_prompt = mo.ui.text_area(
        label="CLT-Grounded Prompt (reduces cognitive load):",
        value="""Create a worked example about Python for loops.

    CRITICAL: This is a WORKED EXAMPLE for novice learners.
    - Problem: Clear, specific, uses familiar context (counting items)
    - Solution: Break into small steps, explain each step's purpose
    - Explanation: Connect to WHY this pattern works (not just WHAT it does)

    Keep cognitive load low: avoid technical jargon, use concrete examples.""",
        full_width=True,
        rows=8
    )

    mo.vstack([basic_prompt, clt_prompt])
    return basic_prompt, clt_prompt


@app.cell
def _(mo):
    """Lab 1: Generate button"""

    lab1_button = mo.ui.run_button(
        label="🔬 Generate Both Examples",
        kind="success",
    )

    mo.md(f"### Compare the Results\n\n{lab1_button}")
    return (lab1_button,)


@app.cell
def _(SimpleExample, basic_prompt, client, clt_prompt, lab1_button, mo):
    """Lab 1: Generate and compare both examples"""

    lab1_output = None

    if lab1_button.value and basic_prompt.value and clt_prompt.value:
        with mo.status.spinner(title="Generating both examples..."):
            basic_response = client.responses.parse(
                model="gpt-5.1",
                input=[{"role": "user", "content": basic_prompt.value}],
                text_format=SimpleExample
            )
            basic_example = basic_response.output_parsed

            clt_response = client.responses.parse(
                model="gpt-5.1",
                input=[{"role": "user", "content": clt_prompt.value}],
                text_format=SimpleExample
            )
            clt_example = clt_response.output_parsed

        lab1_output = mo.vstack([
            mo.md("### 📊 Basic Prompt Result"),
            mo.md(f"**Problem:** {basic_example.problem}"),
            mo.md(f"**Solution:** {basic_example.solution}"),
            mo.md(f"**Explanation:** {basic_example.explanation}"),
            mo.md("---"),
            mo.md("### 🎓 CLT-Grounded Prompt Result"),
            mo.md(f"**Problem:** {clt_example.problem}"),
            mo.md(f"**Solution:** {clt_example.solution}"),
            mo.md(f"**Explanation:** {clt_example.explanation}"),
            mo.callout(mo.md("""
            ### 💭 What Do You Notice?

            - Which problem is clearer and more specific?
            - Which solution breaks down steps better?
            - Which explanation helps you understand WHY, not just WHAT?

            **The prompt IS your pedagogical design!**
            """), kind="info")
        ])

    lab1_output


@app.cell
def _(mo):
    mo.md("""
    ---

    ## ⚖️ Lab 2: Personalization A/B Test

    **Learning Question**: Can you FEEL the difference in cognitive load?

    ### The Experiment

    You'll enter YOUR context (hobby, goal), then see the SAME concept taught:
    - **Generic**: Standard textbook style
    - **Personalized**: Using your context

    **Hypothesis**: The personalized version should feel more engaging and easier to process.
    """)
    return


@app.cell
def _(mo):
    """Lab 2: Context inputs"""

    mo.md("### Your Context")

    your_hobby = mo.ui.text(
        label="Your hobby or interest:",
        placeholder="e.g., photography, cooking, gaming",
        full_width=True
    )

    your_goal = mo.ui.text(
        label="What you want to achieve:",
        placeholder="e.g., build a recipe app, automate photo editing",
        full_width=True
    )

    mo.vstack([your_hobby, your_goal])
    return your_hobby, your_goal


@app.cell
def _(mo):
    """Lab 2: Generate button"""

    lab2_button = mo.ui.run_button(
        label="⚖️ Generate A/B Comparison",
        kind="success",
    )

    mo.md(f"{lab2_button}")
    return (lab2_button,)


@app.cell
def _(SimpleExample, client, lab2_button, mo, your_goal, your_hobby):
    """Lab 2: Generate A/B comparison"""

    lab2_output = None

    if lab2_button.value and your_hobby.value and your_goal.value:
        with mo.status.spinner(title="Generating generic and personalized examples..."):

            generic_prompt = "Create a worked example about Python dictionaries for beginners."
            generic_response = client.responses.parse(
                model="gpt-5.1",
                input=[{"role": "user", "content": generic_prompt}],
                text_format=SimpleExample
            )
            generic_example = generic_response.output_parsed

            personalized_prompt = f"""Create a worked example about Python dictionaries for beginners.

IMPORTANT: Personalize this example for someone who is interested in {your_hobby.value} and wants to {your_goal.value}.
Use familiar contexts and examples from their interest to make the concept more relatable and reduce cognitive load."""

            personalized_response = client.responses.parse(
                model="gpt-5.1",
                input=[{"role": "user", "content": personalized_prompt}],
                text_format=SimpleExample
            )
            personalized_example = personalized_response.output_parsed

        lab2_output = mo.vstack([
            mo.md("### 📖 Generic Example (Standard Textbook Style)"),
            mo.md(f"**Problem:** {generic_example.problem}"),
            mo.md(f"**Solution:** {generic_example.solution}"),
            mo.md(f"**Explanation:** {generic_example.explanation}"),
            mo.md("---"),
            mo.md(f"### ✨ Personalized Example (Your Context: {your_hobby.value})"),
            mo.md(f"**Problem:** {personalized_example.problem}"),
            mo.md(f"**Solution:** {personalized_example.solution}"),
            mo.md(f"**Explanation:** {personalized_example.explanation}"),
            mo.callout(mo.md("""
            ### 💭 How Did That Feel?

            - Which example was more engaging to read?
            - Which one felt easier to process mentally?
            - Could you visualize the personalized example more easily?

            **This is the personalization effect in action!** Familiar contexts reduce extraneous cognitive load.
            """), kind="success")
        ])

    lab2_output


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 🏗️ Lab 3: Data Model Designer

    **Learning Question**: What makes a worked example "worked"?

    ### The Experiment

    Design the data structure for a worked example. What fields do you need?
    Think about:
    - What cognitive load principle does each field support?
    - How does structure guide the AI's output?

    **Current Model** (you can modify this in your mind):
    ```python
    class WorkedExample:
        problem: str           # What they need to solve
        solution_steps: list   # Broken into chunks (why a list?)
        final_answer: str      # Clear conclusion
        key_insight: str       # Schema activation
    ```
    """)
    return


@app.cell
def _(mo):
    """Lab 3: Interactive field selector"""

    mo.md("### Which Fields Support Learning?")

    field_options = {
        "problem: str": "The problem statement",
        "solution_steps: list[str]": "Steps as a list (chunking!)",
        "solution: str": "Solution as one big block",
        "final_answer: str": "Explicit conclusion",
        "key_insight: str": "Why this approach works",
        "code_with_comments: str": "Annotated code",
        "common_mistakes: str": "What to avoid",
        "connection_to_real_world: str": "Practical relevance"
    }

    field_selector = mo.ui.multiselect(
        options=list(field_options.keys()),
        label="Select fields for YOUR ideal worked example:",
        value=["problem: str", "solution_steps: list[str]", "final_answer: str", "key_insight: str"]
    )

    field_selector
    return (field_selector,)


@app.cell
def _(field_selector, mo):
    """Lab 3: Display selection count"""
    mo.md(f"**You selected {len(field_selector.value)} fields**")
    return


@app.cell
def _(field_selector, mo):
    """Lab 3: Analysis"""

    if field_selector.value:
        mo.md(f"""
        ### Your Selected Structure

        ```python
        class WorkedExample:
            {chr(10).join(['    ' + f for f in field_selector.value])}
        ```

        ### 💭 Design Analysis

        **Key Questions:**
        - Did you choose `solution_steps: list[str]` or `solution: str`?
          - **List = chunking** (reduces cognitive load)
          - **String = one big block** (higher load for novices)

        - Did you include `key_insight`?
          - Helps with **schema activation** (connecting to prior knowledge)

        - Did you include `common_mistakes`?
          - **Desirable difficulty**: learning from contrasts

        **The design IS the pedagogy**. Each field choice implements a CLT principle.
        """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 🎛️ Lab 4: Parameter Playground

    **Learning Question**: How do model parameters affect pedagogical quality?

    ### The Experiment

    GPT-5.1 has parameters like `reasoning.effort`. Try different settings and see
    how they affect example quality.

    **Note**: This lab is conceptual---showing the parameters you COULD control.
    """)
    return


@app.cell
def _(mo):
    """Lab 4: Parameter sliders"""

    mo.md("### Adjust Parameters")

    reasoning_effort = mo.ui.dropdown(
        options=["none", "low", "medium", "high"],
        value="low",
        label="Reasoning Effort (how much thinking?)"
    )

    verbosity = mo.ui.dropdown(
        options=["low", "medium", "high"],
        value="medium",
        label="Verbosity (explanation detail)"
    )

    mo.vstack([reasoning_effort, verbosity])
    return reasoning_effort, verbosity


@app.cell
def _(mo, reasoning_effort, verbosity):
    """Lab 4: Display parameter info"""
    mo.callout(mo.md(f"""
    **Current Settings:**

    - Reasoning: {reasoning_effort.value}
    - Verbosity: {verbosity.value}

    **For novices**: Low reasoning (fast), medium-high verbosity (detailed explanations)

    **For experts**: Higher reasoning (better solutions), lower verbosity (concise)

    The "best" parameters depend on your learners!
    """), kind="info")
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 🔍 Lab 5: CLT Analyzer

    **Learning Question**: Can you evaluate examples using CLT principles?

    ### The Experiment

    Read an AI-generated example and evaluate it against CLT criteria.
    This develops your **critical lens** for educational AI.
    """)
    return


@app.cell
def _(mo):
    """Lab 5: Generate button"""

    mo.md("### Generate an Example to Analyze")

    lab5_button = mo.ui.run_button(
        label="🎲 Generate Random Example",
        kind="neutral",
    )

    lab5_button
    return (lab5_button,)


@app.cell
def _(SimpleExample, client, lab5_button, mo):
    """Lab 5: Generate and display example to analyze"""

    example_output = None

    if lab5_button.value:
        with mo.status.spinner(title="Generating example..."):
            response = client.responses.parse(
                model="gpt-5.1",
                input=[{"role": "user", "content": "Create a worked example about Python dictionaries for beginners."}],
                text_format=SimpleExample
            )
            analyze_example = response.output_parsed

        example_output = mo.vstack([
            mo.md("### Example to Analyze"),
            mo.md(f"**Problem:** {analyze_example.problem}"),
            mo.md(f"**Solution:** {analyze_example.solution}"),
            mo.md(f"**Explanation:** {analyze_example.explanation}"),
        ])

    example_output


@app.cell
def _(mo):
    """Lab 5: CLT evaluation checklist"""

    reduces_extraneous = mo.ui.checkbox(
        label="✅ Reduces extraneous cognitive load (no unnecessary complexity)"
    )

    manages_intrinsic = mo.ui.checkbox(
        label="✅ Manages intrinsic load (breaks problem into chunks)"
    )

    optimizes_germane = mo.ui.checkbox(
        label="✅ Optimizes germane load (helps build schemas/patterns)"
    )

    worked_not_problem = mo.ui.checkbox(
        label="✅ Is a WORKED example (shows complete solution, not a puzzle)"
    )

    clear_steps = mo.ui.checkbox(
        label="✅ Has clear step-by-step progression"
    )

    explains_why = mo.ui.checkbox(
        label="✅ Explains WHY, not just WHAT"
    )

    mo.vstack([
        reduces_extraneous,
        manages_intrinsic,
        optimizes_germane,
        worked_not_problem,
        clear_steps,
        explains_why
    ])
    return (
        clear_steps,
        explains_why,
        manages_intrinsic,
        optimizes_germane,
        reduces_extraneous,
        worked_not_problem,
    )


@app.cell
def _(
    clear_steps,
    explains_why,
    manages_intrinsic,
    mo,
    optimizes_germane,
    reduces_extraneous,
    worked_not_problem,
):
    """Lab 5: Scoring"""

    checklist_values = [
        reduces_extraneous.value,
        manages_intrinsic.value,
        optimizes_germane.value,
        worked_not_problem.value,
        clear_steps.value,
        explains_why.value
    ]

    score = sum(1 for v in checklist_values if v)

    score_output = None

    if score > 0:
        score_output = mo.callout(f"""
        ### Score: {score}/6

        {"🌟" * score}

        **Interpretation:**
        - 5-6: Excellent pedagogical design
        - 3-4: Good, but room for improvement
        - 1-2: Needs significant pedagogical revision
        - 0: Not yet evaluated

        **Key Skill**: You're developing a CLT-grounded critical lens for evaluating AI tools!
        """, kind="success" if score >= 5 else "info")

    score_output


@app.cell
def _(mo):
    mo.md("""
    ---

    ## 🎯 Conclusion: From Exploration to Creation

    ### What You Discovered

    Through these 5 labs, you explored:

    1. ✅ **Prompts encode pedagogy** - Design drives outputs
    2. ✅ **Personalization reduces load** - Context matters
    3. ✅ **Structure shapes learning** - Data models are pedagogical choices
    4. ✅ **Parameters affect quality** - Settings have learning implications
    5. ✅ **Critical evaluation is a skill** - You can assess AI tools with CLT

    ### What's Next?

    Now that you understand the **design principles**, you're ready to:

    **Option 1: Build Your Own Tool**
    - Use the simplified code from the workshop
    - Apply these design principles
    - Deploy to HuggingFace Spaces

    **Option 2: Use the Complete Tool**
    - [Try the full Worked Example Weaver](https://huggingface.co/spaces/virtuelleakademie/worked-example-weaver-app)
    - See all 5 principles integrated

    **Option 3: Adapt to Your Domain**
    - Take the template
    - Add your concepts
    - Customize for your learners

    ### The Big Idea

    AI tools for education should be **grounded in learning science**, not just technically impressive.

    You now have:
    - 🧠 The theoretical foundation (CLT)
    - 🔬 Hands-on experience (these labs)
    - 🛠️ The technical skills (simple OpenAI API)
    - 🎯 A critical lens (can evaluate tools)

    **Go build something that helps people learn!**

    ---

    *Created by the [Virtual Academy](https://virtuelleakademie.ch/), BFH*
    """)
    return


if __name__ == "__main__":
    app.run()
