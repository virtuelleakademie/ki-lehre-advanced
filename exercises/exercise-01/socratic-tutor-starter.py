import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        # Exercise 1: Build a Socratic Questioning Agent

        **Time**: 20 minutes

        ## Goal

        Build an AI tutor that uses the Socratic method to help students learn through
        guided questioning rather than direct answers.

        ## The Socratic Method

        Instead of telling students the answer, a Socratic tutor:
        1. Asks clarifying questions
        2. Breaks complex problems into smaller parts
        3. Connects to prior knowledge
        4. Guides students to discover answers themselves

        ## Your Task

        Complete the code below to create a Socratic tutor for your subject area.

        ### Requirements:
        - ✅ The agent should NEVER give direct answers
        - ✅ It should ask 2-3 guiding questions per response
        - ✅ It should adapt based on student responses
        - ✅ It should encourage the student to think through the problem

        ### Hints:
        <details>
        <summary>💡 Hint 1: System Prompt Design</summary>

        Your system prompt should:
        - Clearly state the role (Socratic tutor)
        - Define what NOT to do (no direct answers)
        - Give examples of good questions
        - Specify the subject area
        </details>

        <details>
        <summary>💡 Hint 2: Multi-turn Conversation</summary>

        You'll need to maintain conversation history to build on previous exchanges.
        Store messages in a list and include them all in each API call.
        </details>

        <details>
        <summary>💡 Hint 3: Subject-Specific Knowledge</summary>

        Consider what prior knowledge students typically have in your subject.
        The tutor should connect new concepts to what they already know.
        </details>
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    import os
    from openai import OpenAI
    from dotenv import load_dotenv

    load_dotenv()
    return OpenAI, load_dotenv, mo, os


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

            *Note: For local use with .env file, run:*
            ```bash
            marimo edit socratic-tutor-starter.py
            ```
            """),
            kind="info"
        )

    mo.vstack([status_message, api_key_input]) if api_key_input else status_message
    return api_key_from_env, api_key_input, status_message


@app.cell
def __(OpenAI, api_key_from_env, api_key_input):
    # TODO: Create client with API key from either source
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
        ## Step 1: Choose Your Subject

        What subject will your Socratic tutor teach?
        """
    )
    return


@app.cell
def __(mo):
    # TODO: Create a dropdown or text input for subject selection
    # Add subjects relevant to your teaching context

    subject_area = mo.ui.text(
        label="Subject Area",
        placeholder="e.g., Biology, Mathematics, History",
        value="Biology"
    )
    subject_area
    return (subject_area,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Step 2: Design Your System Prompt

        Create a system prompt that defines how your Socratic tutor should behave:
        """
    )
    return


@app.cell
def __(subject_area):
    # TODO: Complete this system prompt
    # Make it specific to your subject and pedagogical approach

    system_prompt = f"""You are a Socratic tutor helping students learn {subject_area.value}.

YOUR CORE PRINCIPLE: NEVER give direct answers.

INSTEAD, YOU SHOULD:
1. [TODO: Add your teaching strategies here]
2. [TODO: What kind of questions should you ask?]
3. [TODO: How should you handle wrong answers?]

EXAMPLE OF GOOD QUESTIONING:
[TODO: Add an example exchange]

Remember: Your goal is to make students THINK, not to make learning easy."""

    # Display the prompt (for development/debugging)
    # system_prompt
    return (system_prompt,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Step 3: Create the Conversation Interface

        Build an interface where students can ask questions and receive Socratic responses:
        """
    )
    return


@app.cell
def __(mo):
    # Initialize conversation history
    if not hasattr(mo, '_conversation_history'):
        conversation_history = []
    else:
        conversation_history = mo._conversation_history

    # TODO: Create a text input for student questions
    student_input = mo.ui.text_area(
        label="Your Question",
        placeholder="Ask your tutor a question...",
        full_width=True
    )

    student_input
    return conversation_history, student_input


@app.cell
def __(mo):
    # TODO: Create a submit button
    submit_button = mo.ui.button(
        label="Ask Tutor",
        on_click=lambda: None
    )
    submit_button
    return (submit_button,)


@app.cell
def __(client, conversation_history, mo, student_input, submit_button, system_prompt):
    # TODO: Implement the Socratic tutor logic
    response_display = None

    if submit_button.value and student_input.value:
        if not client:
            response_display = mo.callout(
                mo.md("❌ **No API key configured**. Please set up your OpenAI API key first."),
                kind="danger"
            )
        else:
            try:
                # TODO: Add the student's message to conversation history
                # conversation_history.append(...)

                # TODO: Build the messages list for the API
                # Include system prompt + all conversation history
                messages = [
                    {"role": "system", "content": system_prompt},
                    # TODO: Add conversation history here
                ]

                # TODO: Call the OpenAI API
                # response = client.chat.completions.create(...)

                # TODO: Extract the tutor's response
                # tutor_response = ...

                # TODO: Add tutor response to conversation history
                # conversation_history.append(...)

                # TODO: Display the response
                # response_display = mo.md(tutor_response)

                response_display = mo.callout(
                    mo.md("TODO: Implement the tutor response logic above"),
                    kind="warn"
                )

            except Exception as e:
                response_display = mo.callout(
                    mo.md(f"❌ Error: {str(e)}"),
                    kind="danger"
                )

    response_display
    return messages, response_display, tutor_response


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Step 4: Display Conversation History

        Show the full conversation so students can see the progression:
        """
    )
    return


@app.cell
def __(conversation_history, mo):
    # TODO: Display the conversation history in a readable format
    # Consider using different styling for student vs tutor messages

    if conversation_history:
        history_md = "## Conversation History\n\n"

        for msg in conversation_history:
            # TODO: Format each message nicely
            # Hint: Use different formatting for student vs tutor
            pass

        history_display = mo.md(history_md)
    else:
        history_display = mo.md("*No conversation yet. Ask a question to start!*")

    history_display
    return history_display, history_md, msg


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Testing Your Tutor

        Try these test scenarios:

        1. **Direct Question**: Ask "What is photosynthesis?"
           - Does it avoid giving a direct answer?
           - Does it ask guiding questions instead?

        2. **Follow-up**: Answer the tutor's question
           - Does it build on your response?
           - Does it guide you closer to understanding?

        3. **Wrong Answer**: Give an incorrect response
           - How does it handle misconceptions?
           - Is the feedback constructive?

        4. **Partial Understanding**: Show you understand part but not all
           - Does it recognize what you know?
           - Does it target the gaps?

        ## Reflection

        After testing, consider:
        - How is this different from a traditional Q&A chatbot?
        - When would this approach work well? When might it frustrate students?
        - How could you improve the prompting to make it more effective?
        - What subject-specific knowledge should the tutor have?

        ---

        ## Bonus Challenges

        If you finish early, try adding:

        1. **Difficulty Adjustment**: Detect if student is struggling and simplify questions
        2. **Encouragement**: Add positive reinforcement for good reasoning
        3. **Concept Tracking**: Track which concepts the student has grasped
        4. **Export Conversation**: Save the conversation for later review
        """
    )
    return


if __name__ == "__main__":
    app.run()
