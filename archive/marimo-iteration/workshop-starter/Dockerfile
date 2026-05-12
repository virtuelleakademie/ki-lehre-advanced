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
