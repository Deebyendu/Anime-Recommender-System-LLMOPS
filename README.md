# 🎌 Anime Recommender System — LLMOps

> An intelligent, LLM-powered anime recommendation engine built with a production-grade LLMOps pipeline — featuring vector search, a Streamlit UI, Docker containerisation, and Kubernetes deployment.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Pipeline](#running-the-pipeline)
  - [Launching the App](#launching-the-app)
- [Docker](#docker)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Configuration](#configuration)

## Overview

The **Anime Recommender System** leverages Large Language Models (LLMs) combined with semantic vector search to deliver highly relevant anime recommendations based on natural language queries. Built with LLMOps best practices in mind, the project includes a structured ingestion pipeline, a persistent vector store (ChromaDB), and a clean Streamlit frontend — all packaged for Docker and orchestrated via Kubernetes.

Whether you type _"dark psychological thriller with a morally grey protagonist"_ or _"feel-good slice-of-life with great music"_, the system understands your intent and surfaces the most fitting titles.

---

## Architecture

```
User Query (Natural Language)
        │
        ▼
┌──────────────────┐      ┌────────────────────────┐
│  Streamlit App   │ ───► │  LLM Query Processor   │
│  (app/app.py)    │      │  (src/)                │
└──────────────────┘      └────────────┬───────────┘
                                       │ Embedding
                                       ▼
                          ┌────────────────────────┐
                          │  ChromaDB Vector Store │
                          │  (chroma_db/)          │
                          └────────────┬───────────┘
                                       │ Top-K Results
                                       ▼
                          ┌────────────────────────┐
                          │  Recommendation Output │
                          └────────────────────────┘
---

## Tech Stack

| Layer            | Technology                             |
| ---------------- | -------------------------------------- |
| Language         | Python 3.x                             |
| LLM / Embeddings | LLM API (configured via `config/`)     |
| Vector Store     | [ChromaDB](https://www.trychroma.com/) |
| Frontend         | [Streamlit](https://streamlit.io/)     |
| Package Manager  | .venv                                  |
| Containerisation | Docker                                 |
| Orchestration    | Kubernetes                             |

---

## Project Structure

```
Anime-Recommender-System-LLMOPS/
│
├── 📁 app/
│   └── app.py                    # Streamlit frontend application
│
├── 📁 chroma_db/                 # Persisted ChromaDB vector store (auto-generated)
│
├── 📁 config/
│   └── config.py                 # Centralised config — API keys, model & app settings
│
├── 📁 data/
│   ├── user_data/                # User interaction and session data
│   ├── anime_with_synopsis.csv   # Primary dataset with full synopses
│   └── updated_anime.csv         # Cleaned and enriched anime metadata
│
├── 📁 logs/                      # Runtime and pipeline logs
│
├── 📁 pipeline/
│   ├── build_pipeline.py         # Entry point — triggers full ingestion pipeline
│   └── pipeline.py               # Pipeline orchestration and step definitions
│
├── 📁 src/
│   ├── data_loader.py            # Data loading and preprocessing
│   ├── prompt_template.py        # LLM prompt engineering templates
│   ├── recommender.py            # Core recommendation and retrieval logic
│   └── vectore_store.py          # ChromaDB interface — embed, index & query
│
├── 📁 utils/
│   ├── custom_exception.py       # Custom exception classes
│   └── logger.py                 # Logging setup and configuration
│
├── .env                          # Environment variables (not committed to git)
├── .gitignore
├── .python-version               # Pinned Python version
├── Dockerfile                    # Container image definition
├── llmops-k8s.yaml               # Kubernetes deployment manifest
├── main.py                       # CLI entry point
├── pyproject.toml                # Project metadata and build configuration
├── requirements.txt              # Python dependencies
└── setup.py                      # Package setup
```

---
### Prerequisites

- Python ≥ 3.10 (see `.python-version`)
- Docker (for containerised runs)
- `kubectl` + a running Kubernetes cluster (for K8s deployment)
- An LLM API key (e.g. OpenAI / Gemini — configure in `config/`)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Deebyendu/Anime-Recommender-System-LLMOPS.git
cd Anime-Recommender-System-LLMOPS

# 2. Install the project in editable mode using uv
pip install -e .
```

### Running the Pipeline

Before launching the app, build the vector store by running the ingestion pipeline:

```bash
python pipeline/build_pipeline.py
```

This will:

1. Load anime data from the `data/` directory
2. Generate embeddings using the configured LLM/embedding model
3. Persist the resulting vectors to `chroma_db/`

### Launching the App

```bash
streamlit run app/app.py
```

The Streamlit UI will be available at `http://localhost:8501` by default.

---

## Docker

Build and run the application inside a Docker container:

```bash
# Build the image
docker build -t anime-recommender:latest .

# Run the container
docker run -p 8501:8501 anime-recommender:latest
```

The app will be accessible at `http://localhost:8501`.

---

## Kubernetes Deployment

A Kubernetes manifest is included for production-grade deployment:

```bash
# Apply the manifest to your cluster
kubectl apply -f llmops-k8s.yaml

# Check deployment status
kubectl get pods
kubectl get svc
```

Ensure your cluster has access to any required secrets (e.g. API keys) before deploying. Use Kubernetes Secrets or a secrets manager to inject credentials safely:

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=LLM_API_KEY=your_api_key_here
```

---

## Configuration

All settings are managed through `config/config.py` and the `.env` file:

| Variable       | Description                           | Where to Get                                                             |
| -------------- | ------------------------------------- | ------------------------------------------------------------------------ |
| `HF_TOKEN`     | Hugging Face API token for embeddings | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| `GROQ_API_KEY` | Groq API key for LLM inference        | [console.groq.com/keys](https://console.groq.com/keys)                   |

---

<p align="center">Made with ❤️ for anime fans and MLOps enthusiasts</p>
