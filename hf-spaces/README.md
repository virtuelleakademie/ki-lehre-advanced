# HuggingFace Spaces Deployments

This directory contains two versions of the Worked Example Weaver app, ready for deployment to HuggingFace Spaces.

## 🧵 Two Versions Available

### 1. worked-example-weaver (Marimo)

**Interactive notebook-style interface**

- **Technology**: Marimo reactive notebooks
- **Best for**: Workshop participants, exploratory learning, educational settings
- **Interface**: Notebook-like cells with reactive updates
- **Deployment**: Docker-based HuggingFace Space

📁 [`worked-example-weaver/`](./worked-example-weaver/)

**Features:**
- Reactive Python notebook interface
- Git-friendly (pure Python files)
- No stale state issues
- Built-in UI components
- Production-ready

### 2. worked-example-weaver-app (Gradio)

**Polished web application**

- **Technology**: Gradio web framework
- **Best for**: End-users (teachers, students), production deployment
- **Interface**: Clean, traditional web form
- **Deployment**: Gradio SDK on HuggingFace Space

📁 [`worked-example-weaver-app/`](./worked-example-weaver-app/)

**Features:**
- User-friendly web interface
- Automatic form validation
- Dynamic concept selection
- Mobile-responsive
- Easy to customize

## 🚀 Quick Start

### Deploy Marimo Version

```bash
cd worked-example-weaver
# Follow DEPLOYMENT.md
```

**Use when:**
- Running workshops or teaching sessions
- Want notebook-style exploration
- Need reactive, interactive cells
- Building educational demos

### Deploy Gradio Version

```bash
cd worked-example-weaver-app
# Follow DEPLOYMENT.md
```

**Use when:**
- Creating a polished web app
- Serving end-users (teachers/students)
- Want traditional form interface
- Need easy customization

## 📋 What's Included

Each directory contains:

- ✅ `app.py` - Complete application code
- ✅ `requirements.txt` - Python dependencies
- ✅ `README.md` - HuggingFace Space README with metadata
- ✅ `DEPLOYMENT.md` - Step-by-step deployment guide
- ✅ `.env.example` - Environment variable template
- ✅ `Dockerfile` (Marimo only) - Docker configuration

## 🎯 What Both Apps Do

Generate personalized worked examples based on:

1. **Learner Profile**: Name, domain, interests, hobbies, goals, level
2. **Concept Selection**: Choose from 16 concepts across 3 domains
3. **AI Generation**: GPT-5.1 creates a personalized worked example

**Domains:**
- 🐍 Programming (Python)
- 🏥 Health Sciences (Statistics)
- 🌾 Agronomy (Agricultural Science)

## 🔑 Prerequisites

Both apps require:

1. **HuggingFace Account**: [Sign up](https://huggingface.co)
2. **OpenAI API Key**: [Get one](https://platform.openai.com/api-keys)

## 📚 Documentation

- **Workshop Materials**: [ki-lehre-advanced](https://virtuelleakademie.github.io/ki-lehre-advanced/)
- **Marimo Docs**: [marimo.io/docs](https://docs.marimo.io)
- **Gradio Docs**: [gradio.app/docs](https://gradio.app/docs)
- **PydanticAI Docs**: [ai.pydantic.dev](https://ai.pydantic.dev)

## 🧪 Local Testing

### Test Marimo App

```bash
cd worked-example-weaver
pip install -r requirements.txt
export OPENAI_API_KEY="sk-your-key"
marimo edit app.py
```

### Test Gradio App

```bash
cd worked-example-weaver-app
pip install -r requirements.txt
export OPENAI_API_KEY="sk-your-key"
python app.py
```

## 🎨 Customization

Both apps support:

- ✅ Changing the AI model (GPT-5.1 → GPT-4o, etc.)
- ✅ Adding new concepts to existing domains
- ✅ Adding entirely new domains
- ✅ Modifying the system prompt
- ✅ Adjusting the UI/UX

See each app's `DEPLOYMENT.md` for specific instructions.

## 💰 Cost Estimates

**HuggingFace Spaces:**
- Free tier: CPU basic (sufficient for most use)
- Paid tiers: $0.50-$3/hour for faster hardware

**OpenAI API (GPT-5.1):**
- ~$0.02-0.05 per example generated
- Set usage limits at [platform.openai.com](https://platform.openai.com)

## 📖 Research Foundation

Both apps implement evidence-based learning principles from Cognitive Load Theory:

- **Worked Example Effect** (Sweller, 1988)
- **Personalization Effect** (Cordova & Lepper, 1996)

See workshop materials for full research references.

## 🤝 Contributing

These apps were created for the "Building Personalized Worked Example Generators with AI" workshop at the Virtual Academy, Bern University of Applied Sciences.

**Instructor**: Dr. Andrew Ellis ([andrew.ellis@bfh.ch](mailto:andrew.ellis@bfh.ch))

## 📄 License

CC0 1.0 Universal - Public Domain

Both apps are freely available for educational use, modification, and redistribution.

---

**Choose your deployment:**
- [→ Deploy Marimo Version](./worked-example-weaver/DEPLOYMENT.md)
- [→ Deploy Gradio Version](./worked-example-weaver-app/DEPLOYMENT.md)
