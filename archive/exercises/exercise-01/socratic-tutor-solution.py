import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Exercise 1: Socratic Questioning Agent - SOLUTION

    This is a reference implementation showing one way to build a Socratic tutor.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import os
    from openai import OpenAI
    from dotenv import load_dotenv

    load_dotenv()

    # Initialize conversation history
    conversation_history = []
    return OpenAI, conversation_history, load_dotenv, mo, os


@app.cell
def _(mo, os):
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
            marimo edit socratic-tutor-solution.py
            ```
            """),
            kind="info"
        )

    mo.vstack([status_message, api_key_input]) if api_key_input else status_message
    return api_key_from_env, api_key_input, status_message


@app.cell
def _(OpenAI, api_key_from_env, api_key_input):
    # Create client with API key from either source
    api_key = api_key_from_env or (api_key_input.value if api_key_input else None)

    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = None

    return api_key, client


@app.cell
def _(mo):
    subject_area = mo.ui.dropdown(
        options={
            "biology": "Biology",
            "mathematics": "Mathematics",
            "history": "History",
            "physics": "Physics",
            "chemistry": "Chemistry",
            "literature": "Literature"
        },
        value="biology",
        label="Subject Area"
    )
    subject_area
    return (subject_area,)


@app.cell
def _(subject_area):
    # Well-designed system prompt
    system_prompt = f"""You are a Socratic tutor helping students learn {subject_area.value}.

    YOUR CORE PRINCIPLE: NEVER give direct answers. Guide students to discover answers themselves.

    YOUR TEACHING STRATEGIES:
    1. Ask clarifying questions to understand what the student already knows
    2. Break complex concepts into smaller, manageable questions
    3. Connect new ideas to prior knowledge
    4. Use analogies and examples from everyday life
    5. If they're stuck, provide hints through questions, not statements
    6. Celebrate good reasoning, even if the answer isn't perfect

    HOW TO HANDLE RESPONSES:
    - Right answer: Ask them to explain WHY to deepen understanding
    - Wrong answer: Don't say "wrong" - ask questions that reveal the misconception
    - Partial answer: Acknowledge what's correct, then guide toward completeness
    - Confused: Step back, find solid ground, build from there

    EXAMPLE EXCHANGE:
    Student: "What is photosynthesis?"
    YOU: "Great question! Let's think about this together. First, what do plants need to survive and grow? What have you noticed about where plants grow best?"

    Student: "They need water and sunlight?"
    YOU: "Exactly! Now, here's something interesting - animals eat food for energy, but plants don't eat. How do you think plants get energy from water and sunlight?"

    YOUR LANGUAGE:
    - Use encouraging, friendly tone
    - Ask 2-3 questions per response (not overwhelming)
    - Occasionally summarize their progress
    - Use "What do you think...?", "How might...?", "Why do you suppose...?"

    Remember: Struggle is part of learning. Don't rescue them too quickly."""
    return (system_prompt,)


@app.cell
def _(mo):
    student_input = mo.ui.text_area(
        label="Your Question or Response",
        placeholder="Type your question or answer here...",
        full_width=True,
        rows=3
    )
    student_input
    return (student_input,)


@app.cell
def _(mo):
    submit_button = mo.ui.button(
        label="💬 Send to Tutor",
        on_click=lambda: None
    )

    clear_button = mo.ui.button(
        label="🔄 Start New Conversation",
        on_click=lambda: None
    )

    mo.hstack([submit_button, clear_button])
    return clear_button, submit_button


@app.cell
def _(
    client,
    conversation_history,
    mo,
    student_input,
    submit_button,
    system_prompt,
):
    response_display = None

    if submit_button.value and student_input.value:
        if not client:
            response_display = mo.callout(
                mo.md("⚠️ **Please enter your OpenAI API key above to start the conversation.**"),
                kind="warn"
            )
        else:
            # Add student message to history
            conversation_history.append({
                "role": "user",
                "content": student_input.value
            })

            try:
                # Build messages for API call
                messages = [
                    {"role": "system", "content": system_prompt}
                ] + conversation_history

                # Call OpenAI API
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=300
                )

                # Extract tutor response
                tutor_response = response.choices[0].message.content

                # Add to conversation history
                conversation_history.append({
                    "role": "assistant",
                    "content": tutor_response
                })

                # Display latest response
                response_display = mo.callout(
                    mo.md(f"**Tutor**: {tutor_response}"),
                    kind="info"
                )

            except Exception as e:
                response_display = mo.callout(
                    mo.md(f"❌ Error: {str(e)}"),
                    kind="danger"
                )

    response_display
    return


@app.cell
def _(clear_button, conversation_history):
    # Handle clearing conversation
    if clear_button.value:
        conversation_history.clear()
    return


@app.cell
def _(conversation_history, mo):
    if conversation_history:
        history_md = "## Conversation History\n\n"

        for i, msg in enumerate(conversation_history):
            if msg["role"] == "user":
                history_md += f"""
    <div style="background-color: #e3f2fd; padding: 10px; border-radius: 5px; margin: 10px 0;">
    <strong>🧑‍🎓 Student:</strong><br>
    {msg['content']}
    </div>
    """
            else:  # assistant
                history_md += f"""
    <div style="background-color: #f3e5f5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    <strong>👨‍🏫 Tutor:</strong><br>
    {msg['content']}
    </div>
    """

        history_display = mo.Html(history_md)
    else:
        history_display = mo.md("*No conversation yet. Ask a question to start!*")

    history_display
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Key Implementation Details

    ### 1. System Prompt Design
    - Clear role definition
    - Specific strategies (not just "ask questions")
    - Example exchange to set the tone
    - Explicit handling of different response types

    ### 2. Conversation Management
    - Store full history (user + assistant messages)
    - Include history in each API call for context
    - Ability to clear/reset conversation

    ### 3. User Experience
    - Visual distinction between student and tutor
    - Clear action buttons
    - Conversation history visible

    ### 4. Error Handling
    - Try/except for API calls
    - User-friendly error messages

    ## Variations to Consider

    - **Adaptive Difficulty**: Adjust question complexity based on responses
    - **Concept Tracking**: Explicitly track which concepts have been covered
    - **Hint System**: Graduated hints if student is really stuck
    - **Progress Summary**: Periodic summaries of what's been learned
    - **Multi-modal**: Include diagrams or visual aids when helpful
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
