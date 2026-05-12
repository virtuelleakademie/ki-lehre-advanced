---
title: Worked Example Weaver
emoji: 🧵
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
license: cc0-1.0
---

# 🧵 Worked Example Weaver

**Personalized Learning Through Cognitive Load Theory**

An AI-powered web application that generates personalized worked examples tailored to individual learners' interests, goals, and contexts. Built on research-backed principles from Cognitive Load Theory.

## What is this?

This tool demonstrates two key learning science principles:

### The Worked Example Effect
> "Novice learners who study worked examples perform better than learners who solve problems independently."
> — NSW Centre for Education Statistics and Evaluation (2017)

**Why?** Unguided problem-solving overloads working memory. Worked examples reduce cognitive load, freeing capacity for learning.

### The Personalization Effect

Familiar contexts (your hobbies, interests, goals) are easier to process, further reducing cognitive load and improving learning outcomes.

## Features

- 🎯 **Three Learning Domains**: Programming (Python), Health Sciences (Statistics), Agronomy
- 📚 **16 Total Concepts**: 5-6 concepts per domain with varying difficulty levels
- 🤖 **AI-Powered Personalization**: Uses OpenAI GPT-5.1 with structured outputs
- 🎨 **Clean Web Interface**: Built with Gradio for easy interaction

## How to Use

1. **Fill in your profile**
   - Name, domain, interests, hobbies, goals, skill level

2. **Select a concept**
   - Choose from domain-specific concepts based on your learning domain

3. **Generate your example**
   - Click the generate button and wait 30-60 seconds

4. **Study the worked example**
   - Examine the complete solution step-by-step
   - See how it connects to your personal goals

## Supported Domains

### 🐍 Programming (Python)
- For loops
- List comprehensions
- Dictionary methods
- Functions with parameters
- String formatting

**Example contexts**: Recipe websites, photography portfolios, gaming tools

### 🏥 Health Sciences (Statistics)
- Mean and standard deviation
- Correlation analysis
- Linear regression
- Independent t-tests
- Confidence intervals
- Effect size (Cohen's d)

**Example contexts**: Sports performance, nutrition tracking, patient outcomes

### 🌾 Agronomy (Agricultural Science)
- Yield prediction
- NPK optimization
- Growing degree days
- Water use efficiency
- Cost-benefit analysis

**Example contexts**: Family farms, specific crops, sustainable agriculture

## Technical Stack

- **[Gradio](https://gradio.app)**: Modern web interface for ML applications
- **[OpenAI GPT-5.1](https://platform.openai.com/docs/guides/latest-model)**: Latest language model with structured outputs
- **[Pydantic](https://pydantic.dev)**: Data validation using Python type hints

**Note**: This app uses GPT-5.1. If you encounter errors or don't have access yet, you can modify `app.py` line 169 to use `model="gpt-4o"` instead.

## Research Foundations

This tool implements evidence-based learning principles:

**Cooper, G., & Sweller, J. (1987)**. Effects of schema acquisition and rule automation on mathematical problem-solving transfer. *Journal of Educational Psychology*, 79(4), 347-362.

**Cordova, D. I., & Lepper, M. R. (1996)**. Intrinsic motivation and the process of learning: Beneficial effects of contextualization, personalization, and choice. *Journal of Educational Psychology*, 88(4), 715.

**NSW Centre for Education Statistics and Evaluation (2017)**. *Cognitive load theory: Research that teachers really need to understand*. [Link](https://education.nsw.gov.au/about-us/education-data-and-research/cese/publications/literature-reviews/cognitive-load-theory)

**Sweller, J. (1988)**. Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.

## Extend This Tool

Ideas for enhancement:

- Add more domains (economics, chemistry, history, literature)
- Include images and diagrams in examples
- Create sequences of scaffolded examples
- Track learner progress over time
- Export examples to PDF or flashcards
- Add multilingual support
- Integrate with learning management systems

## About

Created by the [Virtual Academy](https://virtuelleakademie.ch/) at Bern University of Applied Sciences as part of the workshop "Building Personalized Worked Example Generators with AI."

**Instructor**: [Dr. Andrew Ellis](mailto:andrew.ellis@bfh.ch), Cognitive Psychologist

**Workshop Materials**: [ki-lehre-advanced](https://virtuelleakademie.github.io/ki-lehre-advanced/)

## License

CC0 1.0 Universal - Public Domain

---

## Local Development

```bash
# Clone and install
git clone <repo>
cd worked-example-weaver-app
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY="sk-your-key-here"

# Run locally
python app.py
```
