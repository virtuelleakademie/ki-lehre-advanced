import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import os
    from pydantic import BaseModel
    from pydantic_ai import Agent
    from typing import Literal
    return Agent, BaseModel, Literal, mo, os


@app.cell
def __(BaseModel, Literal):
    # DATA MODELS
    # These define the structure of our inputs and outputs

    class LearnerProfile(BaseModel):
        """Learner information we collect"""
        name: str
        domain: Literal["programming"]  # Only one domain in workshop version
        specific_interest: str
        hobby_or_passion: str
        goal: str
        background_level: Literal["beginner", "intermediate", "advanced"]

    class PersonalizedWorkedExample(BaseModel):
        """The structure of the example we generate"""
        title: str
        problem_statement: str
        given_data: str
        step_by_step_solution: list[str]
        final_answer: str
        connection_to_goal: str
        practice_suggestion: str

    return LearnerProfile, PersonalizedWorkedExample


@app.cell(hide_code=False)
def __():
    # CONCEPT LIBRARY
    # This is editable - you can add your own concepts here!

    CONCEPTS = {
        "programming": [
            {
                "name": "For Loops",
                "abstract": "Iterate through a sequence of items",
                "difficulty": "beginner",
                "typical_use": "Process lists, repeat actions with variations"
            },
            {
                "name": "Functions with Parameters",
                "abstract": "Reusable code blocks that accept inputs",
                "difficulty": "beginner",
                "typical_use": "Organise code, avoid repetition, create abstractions"
            },
            {
                "name": "String Formatting",
                "abstract": "Create formatted text using f-strings",
                "difficulty": "beginner",
                "typical_use": "Display data, create messages, build output strings"
            }
        ]
    }

    return (CONCEPTS,)


@app.cell(hide_code=False)
def __(Agent, PersonalizedWorkedExample, os):
    # AI AGENT CONFIGURATION
    # This is editable - you can customise the system prompt!

    system_prompt = """You are an expert educator who creates personalised worked examples.

CRITICAL INSTRUCTIONS:
- Weave the learner's interests NATURALLY into the problem context
- Use their name throughout the example
- Make the data/scenario realistic and relevant to their interest
- Connect explicitly to their stated goal
- Provide complete, step-by-step solutions
- Use clear explanations at each step

For Programming examples:
- Include detailed code comments
- Mention common pitfalls
- Show best practices
- Use modern Python syntax (f-strings, type hints)
"""

    # Create the AI agent with structured output
    example_generator = Agent(
        'openai:gpt-4o',  # Using GPT-4o for cost-effectiveness
        result_type=PersonalizedWorkedExample,
        system_prompt=system_prompt
    )

    return example_generator, system_prompt


@app.cell
def __(LearnerProfile, example_generator):
    # GENERATION FUNCTION
    async def generate_example(profile: LearnerProfile, concept: dict):
        """Generate a personalised worked example"""

        prompt = f"""Create a personalised worked example for:

LEARNER INFORMATION:
- Name: {profile.name}
- Domain: {profile.domain}
- Specific Interest: {profile.specific_interest}
- Hobby/Passion: {profile.hobby_or_passion}
- Goal: {profile.goal}
- Level: {profile.background_level}

CONCEPT TO TEACH:
- Name: {concept['name']}
- Description: {concept['abstract']}
- Difficulty: {concept['difficulty']}
- Typical Use: {concept['typical_use']}

Create a worked example that:
1. Uses a scenario from their interest/hobby
2. Teaches the concept through this familiar context
3. Explicitly connects to their goal
4. Provides complete step-by-step solutions
5. Feels natural, not forced"""

        result = await example_generator.run(prompt)
        return result.data

    return (generate_example,)


@app.cell
def __(mo):
    # USER INTERFACE HEADER
    mo.md("""
    # Personalised Worked Example Generator

    **Workshop Starter Template** - Simplified version for hands-on learning

    This application generates personalised worked examples based on learner interests.
    It demonstrates how AI can create educational content that reduces cognitive load
    through personalisation and the worked example effect.
    """)
    return


@app.cell
def __(mo):
    # LEARNER PROFILE INPUTS
    mo.md("## 1. Create a Learner Profile")
    return


@app.cell
def __(mo):
    # Input fields for learner information
    name_input = mo.ui.text(
        label="Learner Name",
        placeholder="e.g., Sarah"
    )

    domain_input = mo.ui.dropdown(
        options=["programming"],
        value="programming",
        label="Domain"
    )

    interest_input = mo.ui.text(
        label="Specific Interest",
        placeholder="e.g., Web development, Data analysis, Game design"
    )

    hobby_input = mo.ui.text(
        label="Hobby or Passion",
        placeholder="e.g., Baking, Photography, Running"
    )

    goal_input = mo.ui.text(
        label="Learning Goal",
        placeholder="e.g., Build a recipe sharing website"
    )

    level_input = mo.ui.dropdown(
        options=["beginner", "intermediate", "advanced"],
        value="beginner",
        label="Background Level"
    )

    # Display the form
    mo.vstack([
        name_input,
        domain_input,
        interest_input,
        hobby_input,
        goal_input,
        level_input
    ])
    return (
        domain_input,
        goal_input,
        hobby_input,
        interest_input,
        level_input,
        name_input,
    )


@app.cell
def __(CONCEPTS, mo):
    # CONCEPT SELECTION
    mo.md("## 2. Select a Concept to Learn")
    return


@app.cell
def __(CONCEPTS, mo):
    # Create dropdown with concepts
    programming_concepts = CONCEPTS["programming"]
    concept_options = {
        f"{c['name']} ({c['difficulty']})": c
        for c in programming_concepts
    }

    concept_selector = mo.ui.dropdown(
        options=concept_options,
        label="Choose a concept"
    )

    concept_selector
    return concept_options, concept_selector, programming_concepts


@app.cell
def __(mo):
    # GENERATE BUTTON
    mo.md("## 3. Generate Personalised Example")
    return


@app.cell
def __(mo):
    generate_button = mo.ui.run_button(label="Generate Example")
    mo.hstack([generate_button, mo.md("*Generation takes 30-60 seconds*")])
    return (generate_button,)


@app.cell
async def __(
    LearnerProfile,
    concept_selector,
    domain_input,
    generate_button,
    generate_example,
    goal_input,
    hobby_input,
    interest_input,
    level_input,
    mo,
    name_input,
):
    # GENERATION LOGIC
    generated_example = None

    if generate_button.value:
        # Check if all required fields are filled
        if not all([
            name_input.value,
            interest_input.value,
            hobby_input.value,
            goal_input.value,
            concept_selector.value
        ]):
            mo.md("**Please fill in all fields before generating.**")
        else:
            # Create learner profile
            profile = LearnerProfile(
                name=name_input.value,
                domain=domain_input.value,
                specific_interest=interest_input.value,
                hobby_or_passion=hobby_input.value,
                goal=goal_input.value,
                background_level=level_input.value
            )

            # Generate the example
            with mo.status.spinner(title="Generating personalised example..."):
                generated_example = await generate_example(
                    profile,
                    concept_selector.value
                )

    return generated_example, profile


@app.cell
def __(generated_example, mo):
    # DISPLAY RESULTS
    if generated_example:
        mo.md(f"""
        ## 4. Your Personalised Worked Example

        ### {generated_example.title}

        **Problem:**

        {generated_example.problem_statement}

        **Given Data:**

        {generated_example.given_data}

        **Step-by-Step Solution:**

        {chr(10).join([f"{i+1}. {step}" for i, step in enumerate(generated_example.step_by_step_solution)])}

        **Final Answer:**

        {generated_example.final_answer}

        **Connection to Your Goal:**

        {generated_example.connection_to_goal}

        **Practice Suggestion:**

        {generated_example.practice_suggestion}
        """)
    return


@app.cell
def __(mo):
    # FOOTER
    mo.md("""
    ---

    **About This Tool**

    This is the workshop starter template - a simplified version with 1 domain and 3 concepts.

    You can:
    - Add more concepts to the CONCEPTS dictionary (edit the cell above)
    - Customise the system prompt to control generation
    - Experiment with different learner profiles

    Built with [Marimo](https://marimo.io) + [PydanticAI](https://ai.pydantic.dev)

    Part of the *KI in der Lehre: Advanced* workshop by the Virtual Academy, BFH.
    """)
    return


if __name__ == "__main__":
    app.run()
