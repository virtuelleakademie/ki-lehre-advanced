import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        # Module 1: Retrieval Practice Generator

        ## The Science Behind Retrieval Practice

        **Retrieval practice** is one of the most powerful learning strategies. When students
        actively recall information from memory (rather than re-reading it), they:

        - Strengthen neural pathways
        - Identify knowledge gaps
        - Improve long-term retention
        - Develop metacognitive awareness

        ### Key Principles:

        1. **Retrieval > Recognition** - Asking students to generate answers is more
           effective than multiple choice
        2. **Difficulty Sweet Spot** - Questions should be challenging but achievable
        3. **Feedback Timing** - Delayed, informative feedback promotes deeper processing
        4. **Varied Practice** - Questions should cover concepts in different ways

        In this module, you'll build an AI tool that generates retrieval practice questions
        from learning materials.
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    import os
    from openai import OpenAI
    from dotenv import load_dotenv
    from pydantic import BaseModel, Field
    from typing import List
    import json

    load_dotenv()
    return BaseModel, Field, List, OpenAI, json, load_dotenv, mo, os


@app.cell
def __(mo, os):
    # Hybrid API key handling: works locally AND in browser
    api_key_from_env = os.getenv("OPENAI_API_KEY")

    if api_key_from_env:
        # Local mode: API key from .env file
        api_key_input = None
        status_message = mo.callout(
            mo.md("✅ **API Key loaded from environment** - You're ready to start!"),
            kind="success"
        )
    else:
        # Browser mode: Show input field
        api_key_input = mo.ui.text(
            label="OpenAI API Key",
            placeholder="sk-proj-...",
            kind="password",
            full_width=True
        )
        status_message = mo.callout(
            mo.md("""
            🌐 **Browser Mode**: Enter your OpenAI API key below

            Get your key from: https://platform.openai.com/api-keys

            *Note: For local use, create a `.env` file with:*
            ```
            OPENAI_API_KEY=your-key-here
            ```
            """),
            kind="info"
        )

    mo.vstack([status_message, api_key_input]) if api_key_input else status_message
    return api_key_from_env, api_key_input, status_message


@app.cell
def __(OpenAI, api_key_from_env, api_key_input):
    # Create client with API key from either source
    api_key = api_key_from_env or (api_key_input.value if api_key_input else None)

    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = None

    return api_key, client


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Step 1: Input Learning Material

        Paste the content you want to create retrieval practice questions for:
        """
    )
    return


@app.cell
def __(mo):
    learning_material = mo.ui.text_area(
        label="Learning Material",
        placeholder="""Example: Photosynthesis is the process by which plants convert light energy
into chemical energy. It occurs in chloroplasts and involves two main stages:
the light-dependent reactions and the Calvin cycle...""",
        value="""Photosynthesis is the process by which plants, algae, and some bacteria convert light energy (usually from the sun) into chemical energy stored in glucose. This process takes place primarily in the chloroplasts of plant cells.

The overall equation: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂

Photosynthesis occurs in two main stages:

1. Light-dependent reactions (occur in thylakoid membranes):
   - Chlorophyll absorbs light energy
   - Water molecules are split (photolysis)
   - Oxygen is released as a byproduct
   - ATP and NADPH are produced

2. Calvin Cycle (occurs in stroma):
   - Carbon dioxide is fixed
   - ATP and NADPH from light reactions are used
   - Glucose is synthesized

This process is crucial for life on Earth as it produces oxygen and serves as the base of most food chains.""",
        full_width=True,
        rows=10
    )
    learning_material
    return (learning_material,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Step 2: Configure Question Difficulty

        Adjust the cognitive demand of the questions:
        """
    )
    return


@app.cell
def __(mo):
    difficulty_level = mo.ui.radio(
        options={
            "recall": "Recall - Basic facts and terms",
            "understand": "Understand - Explain concepts in own words",
            "apply": "Apply - Use concepts in new situations",
            "analyze": "Analyze - Break down and examine relationships"
        },
        value="understand",
        label="Difficulty Level (Bloom's Taxonomy)"
    )

    num_questions = mo.ui.slider(
        start=3,
        stop=10,
        value=5,
        label="Number of Questions",
        show_value=True
    )

    mo.vstack([difficulty_level, num_questions])
    return difficulty_level, num_questions


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Step 3: Question Type

        Choose the type of retrieval practice:
        """
    )
    return


@app.cell
def __(mo):
    question_type = mo.ui.dropdown(
        options={
            "short_answer": "Short Answer - Brief free response",
            "explanation": "Explanation - Detailed conceptual explanation",
            "connection": "Connection - Relate concepts to prior knowledge",
            "application": "Application - Apply to real-world scenario"
        },
        value="short_answer",
        label="Question Type"
    )
    question_type
    return (question_type,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Generate Questions

        Click to generate retrieval practice questions based on your configuration:
        """
    )
    return


@app.cell
def __(mo):
    generate_button = mo.ui.button(
        label="🎯 Generate Retrieval Questions",
        on_click=lambda: None
    )
    generate_button
    return (generate_button,)


@app.cell
def __(BaseModel, Field, List):
    # Define structure for questions using Pydantic
    class RetrievalQuestion(BaseModel):
        """A single retrieval practice question"""
        question: str = Field(description="The question text")
        cognitive_level: str = Field(description="Bloom's taxonomy level")
        key_concepts: List[str] = Field(description="Key concepts being tested")
        sample_answer: str = Field(description="Example of a good answer")
        common_misconceptions: List[str] = Field(
            description="Common mistakes students make"
        )

    class QuestionSet(BaseModel):
        """A set of retrieval practice questions"""
        questions: List[RetrievalQuestion]
        overall_focus: str = Field(description="What this question set emphasizes")
    return QuestionSet, RetrievalQuestion


@app.cell
def __(
    QuestionSet,
    client,
    difficulty_level,
    generate_button,
    learning_material,
    mo,
    num_questions,
    question_type,
):
    questions_output = None

    if generate_button.value and learning_material.value:
        if not client:
            questions_output = mo.callout(
                mo.md("⚠️ **Please enter your OpenAI API key above to generate questions.**"),
                kind="warn"
            )
        else:
            # Create pedagogically-informed system prompt
            system_prompt = f"""You are an expert educator creating retrieval practice questions.

LEARNING MATERIAL:
{learning_material.value}

REQUIREMENTS:
- Generate {num_questions.value} questions at the "{difficulty_level.value}" level
- Question type: {question_type.value}
- Focus on RETRIEVAL (generating from memory) not RECOGNITION
- Questions should promote active thinking
- Avoid questions with obvious answers
- Identify common misconceptions to address

PEDAGOGICAL PRINCIPLES:
1. Desirable Difficulty - Make students think, but keep it achievable
2. Retrieval over Recognition - Ask for generation, not selection
3. Varied Practice - Approach concepts from different angles
4. Metacognition - Questions should reveal what students know/don't know

Generate questions that truly test understanding, not just memorization."""

            try:
                response = client.beta.chat.completions.parse(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": "Generate retrieval practice questions."}
                    ],
                    response_format=QuestionSet,
                    temperature=0.8
                )

                question_set = response.choices[0].message.parsed

                # Display questions in an organized way
                questions_md = f"""
## Generated Questions

**Focus**: {question_set.overall_focus}

**Level**: {difficulty_level.value.upper()}

---
"""

                for i, q in enumerate(question_set.questions, 1):
                    questions_md += f"""
### Question {i}

**{q.question}**

<details>
<summary>📚 Key Concepts Tested</summary>

{", ".join(q.key_concepts)}
</details>

<details>
<summary>✅ Sample Answer</summary>

{q.sample_answer}
</details>

<details>
<summary>⚠️ Common Misconceptions</summary>

{chr(10).join([f"- {m}" for m in q.common_misconceptions])}
</details>

---
"""

                questions_output = mo.accordion({
                    "View Generated Questions": mo.md(questions_md)
                })

            except Exception as e:
                questions_output = mo.callout(
                    mo.md(f"❌ Error generating questions: {str(e)}"),
                    kind="danger"
                )

    questions_output
    return question_set, questions_md, questions_output, response, system_prompt


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Understanding the Design Choices

        ### Why This Approach Works:

        1. **Structured Output** (Pydantic models)
           - Ensures consistent question format
           - Includes pedagogical metadata (misconceptions, key concepts)
           - Easy to integrate into learning management systems

        2. **Bloom's Taxonomy Levels**
           - Allows targeting specific cognitive skills
           - Higher levels promote deeper understanding
           - Matches questions to learning objectives

        3. **Sample Answers + Misconceptions**
           - Helps instructors evaluate student responses
           - Identifies gaps proactively
           - Supports formative feedback

        4. **Varied Question Types**
           - Different types test understanding in different ways
           - Prevents pattern recognition strategies
           - Supports transfer of learning

        ### Pedagogical Considerations:

        ⚠️ **When to Use vs. Not Use**:
        - ✅ **DO**: Use for formative assessment, practice, self-testing
        - ✅ **DO**: Provide to students AFTER they've attempted recall
        - ❌ **DON'T**: Use as the only assessment method
        - ❌ **DON'T**: Give questions before students engage with material
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Try It: Practice Round

        Now let's simulate a student using these questions. Pick one question and
        try answering it yourself:
        """
    )
    return


@app.cell
def __(mo):
    student_response = mo.ui.text_area(
        label="Your Answer",
        placeholder="Write your answer here...",
        full_width=True,
        rows=5
    )
    student_response
    return (student_response,)


@app.cell
def __(mo):
    evaluate_button = mo.ui.button(
        label="Get Feedback",
        on_click=lambda: None
    )
    evaluate_button
    return (evaluate_button,)


@app.cell
def __(client, evaluate_button, mo, student_response):
    feedback_output = None

    if evaluate_button.value and student_response.value:
        if not client:
            feedback_output = mo.callout(
                mo.md("⚠️ **Please enter your OpenAI API key above to get feedback.**"),
                kind="warn"
            )
        else:
            feedback_prompt = f"""You are providing formative feedback on a student's answer.

STUDENT'S ANSWER:
{student_response.value}

FEEDBACK GUIDELINES:
1. Start with what they got right (positive reinforcement)
2. Identify any misconceptions gently
3. Ask a guiding question to deepen understanding
4. Encourage them to elaborate or clarify
5. DO NOT just give the correct answer

Remember: The goal is to promote thinking, not to correct them directly."""

            try:
                feedback_response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": feedback_prompt},
                        {"role": "user", "content": "Provide feedback"}
                    ],
                    temperature=0.7,
                    max_tokens=250
                )

                feedback_output = mo.callout(
                    mo.md(f"""
**Feedback:**

{feedback_response.choices[0].message.content}

---

💡 **Notice**: The feedback doesn't just say "correct" or "wrong" - it promotes
deeper thinking and metacognition.
                    """),
                    kind="info"
                )

            except Exception as e:
                feedback_output = mo.callout(
                    mo.md(f"Error: {str(e)}"),
                    kind="danger"
                )

    feedback_output
    return feedback_output, feedback_prompt, feedback_response


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Reflection Questions

        Before moving to the next module, reflect on:

        1. How is this different from traditional multiple-choice questions?
        2. When would you use retrieval practice vs. other assessment methods?
        3. How could you integrate this into your teaching workflow?
        4. What challenges might students face with this approach?

        ---

        ## Next Steps

        You've learned to build a retrieval practice generator! In the next module,
        we'll explore **metacognitive prompts** - helping students reflect on their
        own learning process.

        ### Exercise 1: Customize This Tool

        Try adapting this tool for your own subject area:
        1. Change the learning material to content you teach
        2. Experiment with different difficulty levels
        3. Notice how question quality changes with different prompts
        4. Consider: What would make this more useful for YOUR students?
        """
    )
    return


if __name__ == "__main__":
    app.run()
