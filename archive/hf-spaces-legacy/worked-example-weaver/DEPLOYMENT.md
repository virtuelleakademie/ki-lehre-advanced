# Deployment Guide: Worked Example Weaver (Marimo)

This guide walks you through deploying the Marimo-based Worked Example Weaver to HuggingFace Spaces.

## Prerequisites

1. **HuggingFace Account**: Sign up at [huggingface.co](https://huggingface.co)
2. **OpenAI API Key**: Get one at [platform.openai.com](https://platform.openai.com/api-keys)

## Step 1: Create a New Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in the details:
   - **Space name**: `worked-example-weaver`
   - **License**: `cc0-1.0` (or your choice)
   - **Select SDK**: `Docker`
   - **Space hardware**: `CPU basic` (free tier)
   - **Visibility**: `Public` (or Private)

3. Click **Create Space**

## Step 2: Upload Files

You can either use Git or the web interface to upload files.

### Option A: Using Git (Recommended)

```bash
# Clone your new Space
git clone https://huggingface.co/spaces/YOUR-USERNAME/worked-example-weaver
cd worked-example-weaver

# Copy files from this directory
cp /path/to/hf-spaces/worked-example-weaver/* .

# Add, commit, and push
git add .
git commit -m "Initial deployment of Worked Example Weaver"
git push
```

### Option B: Using Web Interface

1. In your Space, click **Files** → **Add file** → **Upload files**
2. Upload these files:
   - `app.py`
   - `Dockerfile`
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
2. HuggingFace will automatically build your Docker container
3. This takes 5-10 minutes on first deployment
4. Watch the build logs to see progress

## Step 5: Test Your App

Once the build completes:

1. The app should automatically load in the iframe
2. Fill in the learner profile form
3. Select a concept
4. Click "Generate My Personalized Example"
5. Wait 30-60 seconds for the AI to generate your example

## Troubleshooting

### Build Fails

- Check the build logs in the **Logs** tab
- Ensure all files are present (app.py, Dockerfile, requirements.txt)
- Verify Python dependencies are correct

### App Runs But Generation Fails

- Check that your `OPENAI_API_KEY` is set correctly in Settings
- Verify the key is valid at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Check the logs for specific error messages

### App is Slow

- Free tier CPU can be slow for AI generation (30-60 seconds is normal)
- Consider upgrading to **CPU upgrade** or **T4 GPU** for faster generation
- Paid tiers available in Space Settings

### Can't See the Generate Button

- Make sure you filled in ALL profile fields (name, domain, interest, hobby, goal, level)
- Make sure you selected a concept from the dropdown
- The button only appears when profile is complete AND a concept is selected

## Customization

### Change the Model

In `app.py`, line 248:
```python
example_generator = Agent(
    'openai:gpt-5.1',  # Change to 'openai:gpt-4o' or other model
    result_type=PersonalizedWorkedExample,
    ...
)
```

### Add New Concepts

In `app.py`, around line 132, add to the `CONCEPTS` dictionary:
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

In `app.py`, around line 250, edit the `system_prompt` parameter to change how the AI generates examples.

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

## Additional Resources

- [HuggingFace Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Marimo Documentation](https://docs.marimo.io)
- [PydanticAI Documentation](https://ai.pydantic.dev)
- [Workshop Materials](https://virtuelleakademie.github.io/ki-lehre-advanced/)

## Support

Questions? Contact [andrew.ellis@bfh.ch](mailto:andrew.ellis@bfh.ch)
