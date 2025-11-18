# Deployment Guide: Worked Example Weaver App (Gradio)

This guide walks you through deploying the Gradio-based Worked Example Weaver to HuggingFace Spaces.

## Prerequisites

1. **HuggingFace Account**: Sign up at [huggingface.co](https://huggingface.co)
2. **OpenAI API Key**: Get one at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## Step 1: Create a New Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in the details:
   - **Space name**: `worked-example-weaver-app`
   - **License**: `cc0-1.0` (or your choice)
   - **Select SDK**: `Gradio`
   - **Space hardware**: `CPU basic` (free tier)
   - **Visibility**: `Public` (or Private)

3. Click **Create Space**

## Step 2: Upload Files

You can either use Git or the web interface to upload files.

### Option A: Using Git (Recommended)

```bash
# Clone your new Space
git clone https://huggingface.co/spaces/YOUR-USERNAME/worked-example-weaver-app
cd worked-example-weaver-app

# Copy files from this directory
cp /path/to/hf-spaces/worked-example-weaver-app/* .

# Add, commit, and push
git add .
git commit -m "Initial deployment of Worked Example Weaver App"
git push
```

### Option B: Using Web Interface

1. In your Space, click **Files** → **Add file** → **Upload files**
2. Upload these files:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Click **Commit changes to main**

## Step 3: Set Environment Variables

1. In your Space, go to **Settings**
2. Scroll down to **Repository secrets**
3. Click **New secret**
4. Add your OpenAI API key:
   - **Name**: `OPENAI_API_KEY`
   - **Value**: `sk-your-actual-key-here`
5. Click **Save**

## Step 4: Wait for Build

1. Go to the **App** tab of your Space
2. HuggingFace will automatically install dependencies and launch your app
3. This takes 2-5 minutes on first deployment
4. Watch the build logs to see progress

## Step 5: Test Your App

Once the app loads:

1. The Gradio interface should appear in the iframe
2. Fill in the learner profile form:
   - Your first name
   - Choose learning domain (this updates the concept dropdown)
   - Your specific interest
   - A hobby or passion
   - What you want to achieve
   - Your current level
3. Select a concept from the dropdown
4. Click "✨ Generate My Personalized Example"
5. Wait 30-60 seconds for the AI to generate your example

## Troubleshooting

### Build Fails

- Check the build logs in the **Logs** tab
- Ensure all required files are present (app.py, requirements.txt)
- Verify Python dependencies are compatible

### App Runs But Generation Fails

**"Please check your OpenAI API key" error:**
- Check that your `OPENAI_API_KEY` is set correctly in Settings → Repository secrets
- Verify the key is valid at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Make sure the key has sufficient credits

**"Please fill in all fields" warning:**
- Ensure ALL fields are filled before clicking generate
- Select a domain first (this populates the concept dropdown)
- Then select a concept from the dropdown

### Concept Dropdown is Empty

- Make sure you selected a learning domain first
- The concept dropdown updates automatically when you select a domain
- If it doesn't update, try refreshing the page

### Generation is Slow

- Free tier CPU can be slow for AI generation (30-60 seconds is normal)
- Consider upgrading to **CPU upgrade** or **T4 GPU** for faster generation
- Paid tiers available in Space Settings

## Customization

### Change the Model

In `app.py`, line 78:
```python
example_generator = Agent(
    'openai:gpt-5.1',  # Change to 'openai:gpt-4o' or other model
    result_type=PersonalizedWorkedExample,
    ...
)
```

### Add New Concepts

In `app.py`, around line 25, add to the `CONCEPTS` dictionary:

```python
"programming": [
    {
        "name": "Your New Concept",
        "abstract": "Brief description",
        "difficulty": "beginner",
        "typical_use": "When to use it"
    },
    # ... existing concepts
]
```

### Modify the System Prompt

In `app.py`, around line 80, edit the `system_prompt` parameter to change how the AI generates examples.

### Change Theme

In `app.py`, line 202:
```python
with gr.Blocks(title="Worked Example Weaver", theme=gr.themes.Soft()) as demo:
```

Try: `gr.themes.Default()`, `gr.themes.Monochrome()`, `gr.themes.Glass()`

### Add More Domains

1. Add domain to `CONCEPTS` dictionary
2. Update domain choices in the Gradio interface (line 217)
3. Update `update_concepts()` function to handle new domain

## Updating Your Space

After making changes:

```bash
git add .
git commit -m "Describe your changes"
git push
```

HuggingFace will automatically rebuild and redeploy.

## Cost Considerations

- **HuggingFace Space**: Free tier available (CPU basic)
- **OpenAI API**: Pay per use
  - GPT-5.1: ~$0.02-0.05 per example generated
  - GPT-4o: ~$0.01-0.02 per example generated
  - Set usage limits at [platform.openai.com](https://platform.openai.com)

## Sharing Your App

Once deployed, share your Space:

- **Direct link**: `https://huggingface.co/spaces/YOUR-USERNAME/worked-example-weaver-app`
- **Embed in website**: HuggingFace provides an iframe embed code
- **Share on social media**: Use the share button in your Space

## Additional Resources

- [HuggingFace Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Gradio Documentation](https://gradio.app/docs)
- [PydanticAI Documentation](https://ai.pydantic.dev)
- [Workshop Materials](https://virtuelleakademie.github.io/ki-lehre-advanced/)

## Example Spaces

- [Marimo version](https://huggingface.co/spaces/virtuelleakademie/worked-example-weaver) - Interactive notebook interface
- [Gradio version](https://huggingface.co/spaces/virtuelleakademie/worked-example-weaver-app) - This app!

## Support

Questions? Contact [andrew.ellis@bfh.ch](mailto:andrew.ellis@bfh.ch)
