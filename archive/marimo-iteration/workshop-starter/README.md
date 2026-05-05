---
title: Workshop Starter
emoji: 🎓
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
license: cc0-1.0
---

# Personalised Worked Example Generator - Workshop Starter

**Simplified version for hands-on learning**

This is the interactive application used in the *KI in der Lehre: Advanced* workshop. It demonstrates how to build AI-powered educational tools grounded in Cognitive Load Theory.

## What This Does

Generates personalised worked examples that:
- Collect learner profile information (name, interests, hobbies, goals)
- Create customised examples in familiar contexts
- Reduce cognitive load through personalisation
- Demonstrate the worked example effect

## Features

- **1 Domain**: Programming (Python)
- **3 Concepts**: For Loops, Functions with Parameters, String Formatting
- **Editable Cells**: Modify concepts and system prompts directly in the browser
- **Reactive UI**: Changes propagate automatically (Marimo reactivity)
- **Type-Safe AI**: Structured outputs guaranteed (PydanticAI)

## Technologies

- [Marimo](https://marimo.io) - Reactive Python notebooks
- [PydanticAI](https://ai.pydantic.dev) - Type-safe AI agent framework
- [Pydantic](https://pydantic.dev) - Data validation
- [OpenAI GPT-4o](https://openai.com) - Language model for generation

## Deployment to HuggingFace Spaces

### Prerequisites

1. HuggingFace account: [huggingface.co](https://huggingface.co)
2. OpenAI API key: [platform.openai.com](https://platform.openai.com)

### Steps

1. **Create New Space**
   - Go to huggingface.co/new-space
   - Choose Space name: `workshop-starter` (or your preference)
   - Select SDK: **Docker**
   - License: CC0 1.0 Universal

2. **Add Files**
   - Upload `app.py` (the marimo application)
   - Upload `requirements.txt` (Python dependencies)
   - Create `Dockerfile` (see below)
   - This README.md will be auto-displayed

3. **Configure Secrets**
   - Go to Space Settings → Variables and secrets
   - Add secret: `OPENAI_API_KEY` with your API key
   - This keeps your key secure

4. **Create Dockerfile**

Create a file called `Dockerfile` with this content:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the marimo app
COPY app.py .

# Expose port 7860 (HuggingFace Spaces default)
EXPOSE 7860

# Run marimo in headless mode
CMD ["marimo", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]
```

5. **Deploy**
   - Commit all files
   - HuggingFace will build and deploy automatically
   - Takes 2-3 minutes for first build

### Testing Locally

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENAI_API_KEY="sk-your-key-here"

# Run the app
marimo edit app.py
```

## Workshop Information

This is the simplified starter template from the workshop. The full demo application has:
- 3 domains (Programming, Health Sciences, Agronomy)
- 16 concepts total
- Deployed at: [huggingface.co/spaces/virtuelleakademie/worked-example-weaver](https://huggingface.co/spaces/virtuelleakademie/worked-example-weaver)

Workshop materials: [github.com/virtuelleakademie/ki-lehre-advanced](https://github.com/virtuelleakademie/ki-lehre-advanced)

## Customisation

### Adding New Concepts

Edit the `CONCEPTS` dictionary in the second code cell:

```python
{
    "name": "List Comprehensions",
    "abstract": "Create new lists using concise syntax",
    "difficulty": "intermediate",
    "typical_use": "Transform data, filter lists elegantly"
},
```

### Customising System Prompt

Edit the `system_prompt` variable in the third code cell to control how the AI generates examples.

### Adding New Domains

To add Health Sciences or Agronomy:
1. Extend the `LearnerProfile.domain` to include more options
2. Add domain concepts to `CONCEPTS` dictionary
3. Update concept selector to handle multiple domains

See the full demo application for complete multi-domain implementation.

## Cost Considerations

- Uses GPT-4o (cost-effective)
- Typical example costs £0.01-0.02
- Consider caching common examples
- OpenAI offers educational discounts

## Pedagogical Principles

This tool is grounded in Cognitive Load Theory:

**Worked Example Effect**: Studying complete solutions is more effective than unguided problem-solving for novices.

**Personalisation Effect**: Familiar contexts reduce extraneous cognitive load, improving learning outcomes.

## Licence

CC0 1.0 Universal - Public Domain

## Contact

Dr. Andrew Ellis
Virtual Academy, Bern University of Applied Sciences
andrew.ellis@bfh.ch

---

Built as part of the *KI in der Lehre: Advanced* workshop series.
