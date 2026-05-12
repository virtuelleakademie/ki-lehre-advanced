---
title: Worked Example Weaver
emoji: 🧵
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: cc0-1.0
---

# 🧵 Worked Example Weaver

**Personalized Learning Through Cognitive Load Theory**

An AI-powered tool that generates personalized worked examples tailored to individual learners' interests, goals, and contexts. Built on research-backed principles from Cognitive Load Theory.

## What is this?

This tool demonstrates two key learning science principles:

### The Worked Example Effect
> "Novice learners who study worked examples perform better than learners who solve problems independently."
> — NSW Centre for Education Statistics and Evaluation (2017)

**Why?** Unguided problem-solving overloads working memory. Worked examples reduce cognitive load, freeing capacity for learning.

### The Personalization Effect

Familiar contexts (your hobbies, interests, goals) are easier to process, further reducing cognitive load and improving learning outcomes.

## Features

- **Three Learning Domains**: Programming (Python), Health Sciences (Statistics), Agronomy
- **16 Total Concepts**: 5-6 concepts per domain with varying difficulty levels
- **AI-Powered Personalization**: Uses OpenAI GPT-5.1 with structured outputs
- **Interactive Interface**: Built with Marimo reactive notebooks

## How to Use

1. **Fill in your profile**: Name, domain, interests, hobbies, goals, skill level
2. **Select a concept**: Choose from domain-specific concepts
3. **Generate**: Get a personalized worked example woven into your context
4. **Study**: Examine the complete solution step-by-step

## Supported Domains

### Programming (Python)
- For loops, List comprehensions, Dictionary methods, Functions, String formatting

### Health Sciences (Statistics)
- Mean & SD, Correlation, Linear Regression, T-tests, Confidence Intervals, Effect Size

### Agronomy
- Yield prediction, NPK optimization, Growing degree days, Water use efficiency, Cost-benefit analysis

## Technical Stack

- **[Marimo](https://marimo.io)**: Reactive Python notebooks with built-in UI
- **[PydanticAI](https://ai.pydantic.dev)**: Type-safe AI agent framework
- **[OpenAI GPT-5.1](https://openai.com)**: Language model for generation
- **[Pydantic](https://pydantic.dev)**: Data validation

## Research Foundations

This tool implements evidence-based learning principles:

- **Cooper, G., & Sweller, J. (1987)**. Effects of schema acquisition and rule automation on mathematical problem-solving transfer. *Journal of Educational Psychology*, 79(4), 347-362.

- **NSW Centre for Education Statistics and Evaluation (2017)**. *Cognitive load theory: Research that teachers really need to understand*.

- **Sweller, J. (1988)**. Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.

## About

Created by the [Virtual Academy](https://virtuelleakademie.ch/) at Bern University of Applied Sciences as part of the workshop "Building Personalized Worked Example Generators with AI."

**Instructor**: [Dr. Andrew Ellis](mailto:andrew.ellis@bfh.ch), Cognitive Psychologist

## License

CC0 1.0 Universal - Public Domain
