"""
Worked Example Weaver - Gradio App
Personalized worked examples based on Cognitive Load Theory

Built by the Virtual Academy at Bern University of Applied Sciences
"""

import gradio as gr
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from typing import Literal
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Data Models
class LearnerProfile(BaseModel):
    """Collect learner information for personalization"""
    name: str = Field(description="Learner's first name")
    domain: Literal["programming", "health_sciences", "agronomy"] = Field(description="Learning domain")
    specific_interest: str = Field(description="Specific interest within domain")
    hobby_or_passion: str = Field(description="A hobby or passion they have")
    goal: str = Field(description="What they want to achieve")
    background_level: Literal["beginner", "intermediate", "advanced"] = Field(description="Current level")


class PersonalizedWorkedExample(BaseModel):
    """A complete worked example tailored to the learner"""
    title: str = Field(description="Engaging title that incorporates learner's interest")
    problem_statement: str = Field(description="Problem framed in learner's context (3-4 sentences)")
    given_data: str = Field(description="Data presented in familiar context")
    step_by_step_solution: list[str] = Field(description="Clear steps with explanations")
    final_answer: str = Field(description="Final answer with interpretation")
    connection_to_goal: str = Field(description="How this relates to their goal (2-3 sentences)")
    practice_suggestion: str = Field(description="Similar problem they could try next")


# Concept Library
CONCEPTS = {
    "programming": [
        {"name": "For Loops", "abstract": "Iterate through a sequence of items", "difficulty": "beginner", "typical_use": "Processing lists, repeating actions"},
        {"name": "List Comprehensions", "abstract": "Create new lists using concise syntax", "difficulty": "intermediate", "typical_use": "Transform data, filter lists elegantly"},
        {"name": "Dictionary Methods", "abstract": "Access and manipulate key-value pairs", "difficulty": "beginner", "typical_use": "Store related data, perform fast lookups"},
        {"name": "Functions with Parameters", "abstract": "Create reusable code blocks that accept inputs", "difficulty": "beginner", "typical_use": "Organize code, avoid repetition"},
        {"name": "String Formatting", "abstract": "Create formatted text output using f-strings", "difficulty": "beginner", "typical_use": "Display data, create messages dynamically"},
    ],
    "health_sciences": [
        {"name": "Mean and Standard Deviation", "abstract": "Describe central tendency and variability in data", "difficulty": "beginner", "typical_use": "Summarize health measurements"},
        {"name": "Correlation Analysis", "abstract": "Measure strength and direction of relationship between two variables", "difficulty": "intermediate", "typical_use": "Find relationships in health data"},
        {"name": "Linear Regression", "abstract": "Predict one variable from another using a straight-line relationship", "difficulty": "intermediate", "typical_use": "Predict outcomes, understand relationships"},
        {"name": "Independent T-Test", "abstract": "Compare means between two independent groups", "difficulty": "intermediate", "typical_use": "Test intervention effectiveness"},
        {"name": "Confidence Intervals", "abstract": "Estimate population parameters with uncertainty", "difficulty": "intermediate", "typical_use": "Interpret research findings"},
        {"name": "Effect Size (Cohen's d)", "abstract": "Measure practical significance of differences", "difficulty": "intermediate", "typical_use": "Interpret research impact"},
    ],
    "agronomy": [
        {"name": "Yield Prediction", "abstract": "Estimate crop output based on inputs using regression", "difficulty": "intermediate", "typical_use": "Plan harvest, allocate resources"},
        {"name": "NPK Optimization", "abstract": "Calculate optimal fertilizer ratios for maximum benefit", "difficulty": "intermediate", "typical_use": "Maximize yield while minimizing cost"},
        {"name": "Growing Degree Days", "abstract": "Calculate heat accumulation for crop development", "difficulty": "beginner", "typical_use": "Predict crop stages, plan field operations"},
        {"name": "Water Use Efficiency", "abstract": "Calculate crop yield per unit of water used", "difficulty": "beginner", "typical_use": "Optimize irrigation, compare varieties"},
        {"name": "Cost-Benefit Analysis", "abstract": "Compare costs and returns of agricultural interventions", "difficulty": "intermediate", "typical_use": "Make informed decisions about inputs"},
    ]
}

# AI Agent
example_generator = Agent[PersonalizedWorkedExample](
    'openai:gpt-5.1',
    system_prompt="""You are an expert educator who creates highly personalized
    worked examples that connect abstract concepts to learners' lived experiences.

    CRITICAL INSTRUCTIONS:
    1. Weave the learner's interests, hobbies, and goals naturally into the example
    2. Use their name throughout to increase personal connection
    3. Make data and scenarios feel authentic to their context
    4. Keep explanations clear but connect to what they care about
    5. Match complexity to their level (beginner/intermediate/advanced)
    6. Make the connection to their goal explicit and motivating
    7. Use concrete numbers and realistic data
    8. For programming examples, include actual runnable code with comments
    9. For quantitative examples, show all calculations step by step

    STRUCTURE YOUR EXAMPLES:
    - Start with an engaging title that mentions their interest
    - Frame the problem in their context
    - Present data that feels real to their situation
    - Walk through steps clearly with explanations
    - Connect the final answer to their goal
    - Suggest a related practice problem

    Remember: This is a WORKED EXAMPLE - a complete solution for the learner
    to study, not a problem for them to solve.
    """
)


async def generate_example(
    name: str,
    domain: str,
    interest: str,
    hobby: str,
    goal: str,
    level: str,
    concept_name: str
) -> str:
    """Generate a personalized worked example"""

    # Validate inputs
    if not all([name, domain, interest, hobby, goal, level, concept_name]):
        return "⚠️ Please fill in all fields."

    # Create profile
    domain_key = domain.lower().replace(" ", "_").replace("(", "").replace(")", "").split()[0]
    if "programming" in domain.lower():
        domain_key = "programming"
    elif "health" in domain.lower():
        domain_key = "health_sciences"
    elif "agronomy" in domain.lower():
        domain_key = "agronomy"

    # Find concept
    concepts = CONCEPTS.get(domain_key, [])
    concept = None
    for c in concepts:
        if concept_name.startswith(c["name"]):
            concept = c
            break

    if not concept:
        return f"⚠️ Concept not found: {concept_name}"

    profile = LearnerProfile(
        name=name,
        domain=domain_key,
        specific_interest=interest,
        hobby_or_passion=hobby,
        goal=goal,
        background_level=level
    )

    # Generate example
    try:
        prompt = f"""
        Create a worked example for:

        LEARNER PROFILE:
        - Name: {profile.name}
        - Domain: {profile.domain}
        - Specific interest: {profile.specific_interest}
        - Hobby/passion: {profile.hobby_or_passion}
        - Goal: {profile.goal}
        - Level: {profile.background_level}

        CONCEPT TO TEACH:
        - Name: {concept['name']}
        - Abstract description: {concept['abstract']}
        - Difficulty: {concept['difficulty']}
        - Typical use: {concept['typical_use']}

        Create a worked example that teaches this concept using {profile.name}'s
        specific context. Make the problem realistic and the data believable.

        For programming: Include complete, runnable code with explanatory comments.
        For quantitative problems: Show every calculation step explicitly.
        """

        result = await example_generator.run(prompt)
        example = result.output

        # Format output
        output = f"""# {example.title}

## 📋 The Problem

{example.problem_statement}

### Given Data

{example.given_data}

---

## 💡 Step-by-Step Solution

"""
        for i, step in enumerate(example.step_by_step_solution, 1):
            output += f"**Step {i}:**\n\n{step}\n\n"

        output += f"""---

## ✅ Final Answer

{example.final_answer}

---

### 🎯 Why This Matters for You

{example.connection_to_goal}

---

### 🚀 Try This Next

{example.practice_suggestion}
"""

        return output

    except Exception as e:
        return f"❌ Error generating example: {str(e)}\n\nPlease check your OpenAI API key."


def update_concepts(domain: str):
    """Update concept dropdown based on selected domain"""
    domain_key = domain.lower().replace(" ", "_").replace("(", "").replace(")", "").split()[0]
    if "programming" in domain.lower():
        domain_key = "programming"
    elif "health" in domain.lower():
        domain_key = "health_sciences"
    elif "agronomy" in domain.lower():
        domain_key = "agronomy"

    concepts = CONCEPTS.get(domain_key, [])
    choices = [f"{c['name']} ({c['difficulty']})" for c in concepts]

    return gr.Dropdown(choices=choices, value=None, label="Choose a concept")


# Gradio Interface
with gr.Blocks(title="Worked Example Weaver", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🧵 Worked Example Weaver

    **Learn concepts through examples tailored to YOUR interests!**

    This tool demonstrates principles from **Cognitive Load Theory**:
    - **Worked Example Effect**: Studying complete solutions is more effective than struggling through problems
    - **Personalization Effect**: Familiar contexts reduce cognitive load and improve learning
    """)

    with gr.Row():
        with gr.Column():
            gr.Markdown("## 👤 Step 1: Tell Us About Yourself")

            name = gr.Textbox(label="Your first name", placeholder="e.g., Maria")
            domain = gr.Dropdown(
                choices=["Programming (Python)", "Health Sciences (Statistics)", "Agronomy (Agricultural Science)"],
                label="Choose your learning domain"
            )
            interest = gr.Textbox(label="Your specific interest in this domain", placeholder="e.g., web development, sports nutrition, coffee farming")
            hobby = gr.Textbox(label="A hobby or passion you have", placeholder="e.g., photography, cycling, cooking")
            goal = gr.Textbox(label="What you want to achieve", placeholder="e.g., build a portfolio site, improve performance, increase yield")
            level = gr.Dropdown(choices=["beginner", "intermediate", "advanced"], label="Your current level", value="beginner")

            gr.Markdown("## 📚 Step 2: Choose a Concept to Learn")
            concept = gr.Dropdown(label="Choose a concept", choices=[])

            domain.change(update_concepts, inputs=[domain], outputs=[concept])

            generate_btn = gr.Button("✨ Generate My Personalized Example", variant="primary", size="lg")

        with gr.Column():
            output = gr.Markdown(label="Your Personalized Worked Example")

    generate_btn.click(
        fn=lambda *args: asyncio.run(generate_example(*args)),
        inputs=[name, domain, interest, hobby, goal, level, concept],
        outputs=[output]
    )

    gr.Markdown("""
    ---

    ## 📖 About This Tool

    ### Research Foundations

    **The Worked Example Effect** (Sweller, 1988)
    > "Novice learners who study worked examples perform better on subsequent tests than learners who solve problems themselves."

    **The Personalization Effect** (Cordova & Lepper, 1996)
    > "Familiar contexts require less cognitive effort to process, reducing extraneous cognitive load."

    ### Built With
    - [PydanticAI](https://ai.pydantic.dev) - Type-safe AI agents
    - [OpenAI GPT-5.1](https://openai.com) - Language model
    - [Gradio](https://gradio.app) - Web interface

    ---

    **Created by the [Virtual Academy](https://virtuelleakademie.ch/) at Bern University of Applied Sciences**
    """)

if __name__ == "__main__":
    demo.launch()
