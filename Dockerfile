FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /requirements

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .

ENV STABLE_DIFFUSION_URL=ENABLED
ENV OPENAI_API_KEY=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

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]