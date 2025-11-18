import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        # Welcome to the Advanced AI in Teaching Workshop!

        This workshop will teach you how to build **pedagogically sound** AI tools
        that support student learning based on cognitive science principles.

        ## What Makes a Tool Pedagogically Sound?

        Based on "Make it Stick" and cognitive science research, effective AI learning
        tools should:

        1. **Promote Active Retrieval** - Encourage students to recall information rather
           than re-read it
        2. **Create Desirable Difficulties** - Introduce productive struggle that deepens
           understanding
        3. **Support Distributed Practice** - Space learning over time
        4. **Encourage Metacognition** - Help students reflect on their own learning
        5. **Facilitate Transfer** - Practice concepts in varied contexts

        **Key Principle**: AI should support cognitive work, NOT replace it. The best
        tools guide students through thinking rather than giving direct answers.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Why Marimo?

        We're using [marimo](https://marimo.io) instead of Jupyter/Colab because:

        - **Reactive** - Cells automatically update when dependencies change (no stale state!)
        - **Interactive** - Built-in UI elements (sliders, dropdowns, text inputs)
        - **Git-friendly** - Stored as Python files, easy to version control
        - **Reproducible** - No hidden state or execution order problems
        - **Local** - Runs on your machine (or can be deployed as web app)

        ## Quick Marimo Tips

        - Cells execute automatically when you change them
        - Use `mo.ui` for interactive elements
        - Variables are automatically tracked across cells
        - Code and markdown are both in cells
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    import os
    from openai import OpenAI
    from dotenv import load_dotenv
    import tiktoken

    # Load environment variables
    load_dotenv()
    return OpenAI, load_dotenv, mo, os, tiktoken


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Setting Up OpenAI API

        For this workshop, you'll need an OpenAI API key. Let's check if you have one configured:
        """
    )
    return


@app.cell
def __(mo, os):
    # Hybrid API key handling: works locally AND in browser
    api_key_from_env = os.getenv("OPENAI_API_KEY")

    if api_key_from_env:
        # Local mode: API key from .env file
        api_key_input = None
        status_message = mo.callout(
            mo.md("✅ **API Key loaded from environment** - You're ready to go!"),
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
        ## Your First AI Interaction

        Let's create a simple AI tool that demonstrates the **Socratic method** -
        asking guiding questions rather than giving direct answers.
        """
    )
    return


@app.cell
def __(mo):
    # Interactive input for student question
    student_question = mo.ui.text_area(
        label="Student asks:",
        placeholder="e.g., 'What is photosynthesis?'",
        full_width=True
    )
    student_question
    return (student_question,)


@app.cell
def __(client, mo, student_question):
    # Only run if there's a question
    response_output = None

    if student_question.value and client:
        # Socratic prompting system
        system_prompt = """You are a Socratic tutor. Instead of directly answering questions,
        you guide students to discover answers themselves by:

        1. Asking clarifying questions
        2. Breaking down complex problems into smaller parts
        3. Connecting to what they already know
        4. Encouraging them to think through the reasoning

        NEVER give the complete answer directly. Your goal is to facilitate their thinking process."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": student_question.value}
                ],
                temperature=0.7,
                max_tokens=200
            )

            response_output = mo.md(
                f"""
                **Tutor Response:**

                {response.choices[0].message.content}

                ---

                💡 **Notice**: The AI didn't give a direct answer - it asked guiding questions
                to promote active thinking!
                """
            )
        except Exception as e:
            response_output = mo.callout(
                mo.md(f"❌ Error: {str(e)}"),
                kind="danger"
            )

    response_output
    return client, response, response_output, system_prompt


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Understanding Costs

        It's important to be aware of API costs when building educational tools.
        Let's calculate the cost of that interaction:
        """
    )
    return


@app.cell
def __(mo, response, tiktoken):
    try:
        # Calculate tokens and cost
        encoding = tiktoken.encoding_for_model("gpt-4o-mini")

        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens

        # GPT-4o-mini pricing (as of 2025)
        # $0.150 per 1M input tokens, $0.600 per 1M output tokens
        input_cost = (prompt_tokens / 1_000_000) * 0.150
        output_cost = (completion_tokens / 1_000_000) * 0.600
        total_cost = input_cost + output_cost

        cost_display = mo.md(
            f"""
            **Token Usage:**
            - Input tokens: {prompt_tokens:,}
            - Output tokens: {completion_tokens:,}
            - Total tokens: {total_tokens:,}

            **Estimated Cost:**
            - Input cost: ${input_cost:.6f}
            - Output cost: ${output_cost:.6f}
            - **Total: ${total_cost:.6f}**

            For 1000 similar interactions: ~${total_cost * 1000:.2f}
            """
        )
    except:
        cost_display = mo.md("*Run a query above to see cost calculation*")

    cost_display
    return (
        completion_tokens,
        cost_display,
        encoding,
        input_cost,
        output_cost,
        prompt_tokens,
        total_cost,
        total_tokens,
    )


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Next Steps

        In the following modules, you'll learn to build:

        1. **Retrieval Practice Tools** - Generate questions that require active recall
        2. **Metacognitive Prompts** - Help students reflect on their learning process
        3. **Adaptive Difficulty** - Adjust challenge level based on student responses
        4. **Multi-turn Conversations** - Build on previous interactions with memory

        Each tool will be grounded in cognitive science principles to ensure it
        genuinely supports learning.

        ---

        ✨ **Ready?** Let's move on to Module 1: Building a Retrieval Practice Generator!
        """
    )
    return


if __name__ == "__main__":
    app.run()
