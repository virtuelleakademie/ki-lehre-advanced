FROM python:3.11-slim

RUN useradd -m -u 1000 user
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml .
COPY src/ src/
RUN pip install --no-cache-dir -e .

COPY app.py .

USER user

EXPOSE 7860
CMD ["marimo", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]
