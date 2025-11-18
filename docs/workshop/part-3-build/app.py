"""
Personalized Worked Example Generator
Demonstrates Cognitive Load Theory principles through AI-generated personalized examples.

Based on research:
- Sweller, J. (1988). Cognitive load during problem solving.
- NSW CESE (2017). Cognitive load theory: Research that teachers really need to understand.
"""

import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    from pydantic import BaseModel, Field
    from pydantic_ai import Agent
    from typing import Literal
    import os

    return mo, BaseModel, Field, Agent, Literal, os


@app.cell
def welcome_section(mo):
    mo.md("""
    # 🎓 Personalized Worked Example Generator

    **Learn concepts through examples tailored to YOUR interests!**

    ## Why This Works

    This tool demonstrates principles from **Cognitive Load Theory**:

    ### The Worked Example Effect
    > "Novice learners who are given worked examples to study perform better
    > than learners who are required to solve problems themselves."
    >
    > — NSW Centre for Education Statistics and Evaluation (2017)

    **Why?** Unguided problem-solving overloads working memory. Worked examples
    reduce cognitive load, freeing capacity for learning.

    ### The Personalization Effect

    Familiar contexts (your hobbies, interests, goals) are easier to process,
    further reducing cognitive load and improving learning.

    ---

    ## How It Works

    1. **Tell us about yourself** - interests, goals, background
    2. **Choose a concept** to learn in your domain
    3. **Get a custom example** woven into your context

    Let's get started! 👇
    """)
    return


@app.cell
def define_models(BaseModel, Field, Literal):
    """Define data models for learner profiles and worked examples"""

    class LearnerProfile(BaseModel):
        """Collect learner information for personalization"""

        name: str = Field(
            description="Learner's first name"
        )

        domain: Literal["programming", "health_sciences", "agronomy"] = Field(
            description="Learning domain"
        )

        specific_interest: str = Field(
            description="Specific interest within domain"
        )

        hobby_or_passion: str = Field(
            description="A hobby or passion they have"
        )

        goal: str = Field(
            description="What they want to achieve"
        )

        background_level: Literal["beginner", "intermediate", "advanced"] = Field(
            description="Their current level in the domain"
        )


    class PersonalizedWorkedExample(BaseModel):
        """A complete worked example tailored to the learner"""

        title: str = Field(
            description="Engaging title that incorporates learner's interest"
        )

        problem_statement: str = Field(
            description="Problem framed in learner's context (3-4 sentences)"
        )

        given_data: str = Field(
            description="Data presented in familiar context (can include code blocks or tables)"
        )

        step_by_step_solution: list[str] = Field(
            description="Clear steps with explanations. Include code or calculations."
        )

        final_answer: str = Field(
            description="The final answer with interpretation relevant to learner's context"
        )

        connection_to_goal: str = Field(
            description="How this example relates to their stated goal (2-3 sentences)"
        )

        practice_suggestion: str = Field(
            description="A similar problem they could try next, using their context"
        )

    return LearnerProfile, PersonalizedWorkedExample


@app.cell
def define_concepts():
    """Define concept library for each domain"""

    CONCEPTS = {
        "programming": [
            {
                "name": "For Loops",
                "abstract": "Iterate through a sequence of items",
                "difficulty": "beginner",
                "typical_use": "Processing lists, repeating actions multiple times"
            },
            {
                "name": "List Comprehensions",
                "abstract": "Create new lists using concise syntax",
                "difficulty": "intermediate",
                "typical_use": "Transform data, filter lists elegantly"
            },
            {
                "name": "Dictionary Methods",
                "abstract": "Access and manipulate key-value pairs",
                "difficulty": "beginner",
                "typical_use": "Store related data, perform fast lookups"
            },
            {
                "name": "Functions with Parameters",
                "abstract": "Create reusable code blocks that accept inputs",
                "difficulty": "beginner",
                "typical_use": "Organize code, avoid repetition"
            },
            {
                "name": "String Formatting",
                "abstract": "Create formatted text output using f-strings",
                "difficulty": "beginner",
                "typical_use": "Display data, create messages dynamically"
            }
        ],
        "health_sciences": [
            {
                "name": "Mean and Standard Deviation",
                "abstract": "Describe central tendency and variability in data",
                "difficulty": "beginner",
                "typical_use": "Summarize health measurements, describe populations"
            },
            {
                "name": "Correlation Analysis",
                "abstract": "Measure strength and direction of relationship between two variables",
                "difficulty": "intermediate",
                "typical_use": "Find relationships in health data, guide research"
            },
            {
                "name": "Linear Regression",
                "abstract": "Predict one variable from another using a straight-line relationship",
                "difficulty": "intermediate",
                "typical_use": "Predict outcomes, understand relationships, forecast trends"
            },
            {
                "name": "Independent T-Test",
                "abstract": "Compare means between two independent groups",
                "difficulty": "intermediate",
                "typical_use": "Test intervention effectiveness, compare treatments"
            },
            {
                "name": "Confidence Intervals",
                "abstract": "Estimate population parameters with uncertainty",
                "difficulty": "intermediate",
                "typical_use": "Interpret research findings, quantify precision"
            },
            {
                "name": "Effect Size (Cohen's d)",
                "abstract": "Measure practical significance of differences",
                "difficulty": "intermediate",
                "typical_use": "Interpret research impact beyond p-values"
            }
        ],
        "agronomy": [
            {
                "name": "Yield Prediction",
                "abstract": "Estimate crop output based on inputs using regression",
                "difficulty": "intermediate",
                "typical_use": "Plan harvest, allocate resources, financial projections"
            },
            {
                "name": "NPK Optimization",
                "abstract": "Calculate optimal fertilizer ratios for maximum benefit",
                "difficulty": "intermediate",
                "typical_use": "Maximize yield while minimizing cost and environmental impact"
            },
            {
                "name": "Growing Degree Days",
                "abstract": "Calculate heat accumulation for crop development",
                "difficulty": "beginner",
                "typical_use": "Predict crop stages, plan field operations"
            },
            {
                "name": "Water Use Efficiency",
                "abstract": "Calculate crop yield per unit of water used",
                "difficulty": "beginner",
                "typical_use": "Optimize irrigation, compare varieties"
            },
            {
                "name": "Cost-Benefit Analysis",
                "abstract": "Compare costs and returns of agricultural interventions",
                "difficulty": "intermediate",
                "typical_use": "Make informed decisions about inputs and practices"
            }
        ]
    }

    return CONCEPTS,


@app.cell
def create_agent(Agent, PersonalizedWorkedExample):
    """Create the AI agent for generating personalized examples"""

    example_generator = Agent(
        'openai:gpt-5.1',
        result_type=PersonalizedWorkedExample,
        system_prompt="""You are an expert educator who creates highly personalized
        worked examples that connect abstract concepts to learners' lived experiences.

        CRITICAL INSTRUCTIONS:
        1. Weave the learner's interests, hobbies, and goals naturally into the example
        2. Use their name throughout to increase personal connection
        3. Make data and scenarios feel authentic to their context
        4. Keep explanations clear but connect to what they care about
        5. The example should feel like it was written specifically for this person
        6. Match complexity to their level (beginner/intermediate/advanced)
        7. Make the connection to their goal explicit and motivating
        8. Use concrete numbers and realistic data
        9. For programming examples, include actual runnable code with comments
        10. For quantitative examples, show all calculations step by step

        STRUCTURE YOUR EXAMPLES:
        - Start with an engaging title that mentions their interest
        - Frame the problem in their context (use their name and interests)
        - Present data that feels real to their situation
        - Walk through steps clearly with explanations
        - For code: include comments explaining each part
        - For math: show each calculation explicitly
        - Connect the final answer to their goal
        - Suggest a related practice problem in their context

        AVOID:
        - Generic examples with personal details superficially added
        - Forced or artificial connections
        - Too much technical jargon for beginners
        - Abstract variable names (use meaningful names from their context)
        - Skipping steps in solutions

        Remember: This is a WORKED EXAMPLE - a complete solution for the learner
        to study, not a problem for them to solve.
        """
    )

    async def generate_personalized_example(
        profile: 'LearnerProfile',
        concept: dict
    ) -> PersonalizedWorkedExample:
        """Generate a personalized worked example"""

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
        specific context. The example should feel personal and relevant to their
        goal of "{profile.goal}".

        Make the problem realistic and the data believable for their situation.

        For programming: Include complete, runnable code with explanatory comments.
        For quantitative problems: Show every calculation step explicitly.

        This is a WORKED EXAMPLE - provide the complete solution for them to study.
        """

        result = await example_generator.run(prompt)
        return result.data

    return example_generator, generate_personalized_example


@app.cell
def profile_form_header(mo):
    """Header for profile form"""
    mo.md("---\n## 👤 Step 1: Tell Us About Yourself")
    return


@app.cell
def profile_inputs(mo):
    """Individual input widgets for profile"""

    name_input = mo.ui.text(
        label="Your first name:",
        placeholder="e.g., Maria",
        full_width=True
    )

    domain_input = mo.ui.dropdown(
        label="Choose your learning domain:",
        options={
            "Programming (Python)": "programming",
            "Health Sciences (Statistics)": "health_sciences",
            "Agronomy (Agricultural Science)": "agronomy"
        },
        value=None,
        full_width=True
    )

    interest_input = mo.ui.text(
        label="Your specific interest in this domain:",
        placeholder="e.g., web development, sports nutrition, coffee farming",
        full_width=True
    )

    hobby_input = mo.ui.text(
        label="A hobby or passion you have:",
        placeholder="e.g., photography, cycling, cooking",
        full_width=True
    )

    goal_input = mo.ui.text(
        label="What you want to achieve:",
        placeholder="e.g., build a portfolio site, improve performance, increase yield",
        full_width=True
    )

    level_input = mo.ui.dropdown(
        label="Your current level:",
        options=["beginner", "intermediate", "advanced"],
        value="beginner",
        full_width=True
    )

    return name_input, domain_input, interest_input, hobby_input, goal_input, level_input


@app.cell
def display_profile_form(mo, name_input, domain_input, interest_input, hobby_input, goal_input, level_input):
    """Display the profile form"""

    mo.vstack([
        name_input,
        domain_input,
        interest_input,
        hobby_input,
        goal_input,
        level_input
    ])

    return


@app.cell
def check_profile_complete(name_input, domain_input, interest_input, hobby_input, goal_input, level_input):
    """Check if profile is complete"""

    profile_complete = all([
        name_input.value,
        domain_input.value,
        interest_input.value,
        hobby_input.value,
        goal_input.value,
        level_input.value
    ])

    return profile_complete,


@app.cell
def create_profile(profile_complete, LearnerProfile, name_input, domain_input, interest_input, hobby_input, goal_input, level_input):
    """Create profile object if form is complete"""

    if profile_complete:
        learner_profile = LearnerProfile(
            name=name_input.value,
            domain=domain_input.value,
            specific_interest=interest_input.value,
            hobby_or_passion=hobby_input.value,
            goal=goal_input.value,
            background_level=level_input.value
        )
    else:
        learner_profile = None

    return learner_profile,


@app.cell
def show_profile_status(mo, profile_complete, learner_profile):
    """Show profile status"""

    if profile_complete:
        mo.callout(
            f"""
            ✅ **Profile Complete!**

            Great, {learner_profile.name}! Now choose a concept below.
            """,
            kind="success"
        )
    else:
        mo.callout(
            "📝 Please fill in all fields above to continue.",
            kind="info"
        )

    return


@app.cell
def concept_selection_header(mo, profile_complete):
    """Header for concept selection"""

    if profile_complete:
        mo.md("---\n## 📚 Step 2: Choose a Concept to Learn")

    return


@app.cell
def concept_selector_widget(mo, profile_complete, learner_profile, CONCEPTS):
    """Create concept selector based on chosen domain"""

    if profile_complete and learner_profile:
        available_concepts = CONCEPTS[learner_profile.domain]

        concept_selector = mo.ui.dropdown(
            label=f"Choose a concept in {learner_profile.domain.replace('_', ' ').title()}:",
            options={
                f"{c['name']} ({c['difficulty']})": c
                for c in available_concepts
            },
            value=None,
            full_width=True
        )

        mo.vstack([
            concept_selector,
            mo.callout(
                "👆 Select a concept from the dropdown above to continue.",
                kind="info"
            ) if not concept_selector.value else None
        ])
    else:
        concept_selector = None

    return concept_selector,


@app.cell
def generate_button_widget(mo, profile_complete, concept_selector):
    """Create generate button"""

    if profile_complete and concept_selector and concept_selector.value:
        generate_button = mo.ui.button(
            label="✨ Generate My Personalized Example",
            kind="success",
            full_width=True
        )

        mo.vstack([
            mo.md("---"),
            mo.md("## 🎯 Step 3: Generate Your Example"),
            generate_button
        ])
    else:
        generate_button = None

    return generate_button,


@app.cell
async def generate_and_display(mo, generate_button, learner_profile, concept_selector, generate_personalized_example):
    """Generate and display the personalized example"""

    if generate_button and generate_button.value and learner_profile and concept_selector.value:

        # Show loading state
        with mo.status.spinner(title="Creating your personalized example... This may take 30-60 seconds."):
            try:
                example = await generate_personalized_example(
                    profile=learner_profile,
                    concept=concept_selector.value
                )

                # Display the example
                display_content = mo.vstack([
                    mo.md("---"),
                    mo.md(f"# {example.title}"),
                    mo.md("## 📋 The Problem"),
                    mo.md(example.problem_statement),
                    mo.md("### Given Data"),
                    mo.md(example.given_data),
                    mo.md("---"),
                    mo.md("## 💡 Step-by-Step Solution"),
                    *[mo.md(f"**Step {i}:**\n\n{step}")
                      for i, step in enumerate(example.step_by_step_solution, 1)],
                    mo.md("---"),
                    mo.md("## ✅ Final Answer"),
                    mo.md(example.final_answer),
                    mo.md("---"),
                    mo.callout(
                        f"### 🎯 Why This Matters for You\n\n{example.connection_to_goal}",
                        kind="success"
                    ),
                    mo.md("---"),
                    mo.callout(
                        f"### 🚀 Try This Next\n\n{example.practice_suggestion}",
                        kind="info"
                    ),
                ])

                display_content

            except Exception as e:
                mo.callout(
                    f"❌ Error generating example: {str(e)}\n\nPlease check your OpenAI API key.",
                    kind="danger"
                )

    return


@app.cell
def footer(mo):
    """Display footer with information"""

    mo.md("""
    ---

    ## 📖 About This Tool

    ### Cognitive Load Theory Principles

    This tool demonstrates research-backed learning principles:

    **The Worked Example Effect** (Sweller, 1988; Cooper & Sweller, 1987)
    > "Novice learners who are given worked examples to study perform better on
    > subsequent tests than learners who are required to solve the equivalent
    > problems themselves."

    - **Why?** Unguided problem-solving overloads working memory
    - **Result:** Studying worked examples frees cognitive capacity for learning
    - **Evidence:** Effect size of 0.52 across multiple studies (Crissman, 2006)

    **The Personalization Effect** (Cordova & Lepper, 1996)
    > "Familiar contexts require less cognitive effort to process, reducing
    > extraneous cognitive load and improving learning outcomes."

    - **Why?** Known contexts don't require working memory to parse
    - **Result:** More capacity available for schema construction
    - **Benefit:** Increased motivation through personal relevance

    ### Built With

    - [Marimo](https://marimo.io) - Reactive Python notebooks
    - [PydanticAI](https://ai.pydantic.dev) - Type-safe AI agents
    - [OpenAI GPT-5.1](https://openai.com) - Language model
    - [Pydantic](https://pydantic.dev) - Data validation

    ### 🔧 Extend This Tool

    Ideas for enhancement:

    - Add more domains (economics, chemistry, history, literature)
    - Include images and diagrams in examples
    - Create sequences of scaffolded examples
    - Track learner progress over time
    - Export examples to PDF or flashcards
    - Add multilingual support
    - Integrate with learning management systems

    ### 📚 Research References

    - Cooper, G., & Sweller, J. (1987). Effects of schema acquisition and rule
      automation on mathematical problem-solving transfer. *Journal of Educational
      Psychology*, 79(4), 347-362.

    - Cordova, D. I., & Lepper, M. R. (1996). Intrinsic motivation and the process
      of learning: Beneficial effects of contextualization, personalization, and
      choice. *Journal of Educational Psychology*, 88(4), 715.

    - Crissman, J. (2006). *The design and utilization of effective worked examples:
      A meta-analysis* (Doctoral dissertation). University of Nebraska, Lincoln.

    - NSW Centre for Education Statistics and Evaluation (2017). *Cognitive load
      theory: Research that teachers really need to understand*.
      [Link](https://education.nsw.gov.au/about-us/education-data-and-research/cese/publications/literature-reviews/cognitive-load-theory)

    - Sweller, J. (1988). Cognitive load during problem solving: Effects on learning.
      *Cognitive Science*, 12(2), 257-285.

    ---

    **Created in the BFH Workshop:** Building Personalized Worked Example Generators with AI
    """)

    return


if __name__ == "__main__":
    app.run()
