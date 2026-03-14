# 🎌 Anime Recommender System — LLMOps

> An intelligent, LLM-powered anime recommendation engine built with a production-grade LLMOps pipeline — featuring vector search, a Streamlit UI, Docker containerisation, and Kubernetes deployment.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Pipeline](#running-the-pipeline)
  - [Launching the App](#launching-the-app)
- [Docker](#docker)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Configuration](#configuration)
- [Contributing](#contributing)

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
```

**Pipeline (offline):**

```
Raw Anime Data (data/)
      │
      ▼
pipeline/build_pipeline.py
      │  ├─ Data Cleaning & Preprocessing
      │  ├─ Embedding Generation
      │  └─ ChromaDB Ingestion
      ▼
Persistent Vector Store (chroma_db/)
```

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
├── app/                    # Streamlit frontend application
├── chroma_db/              # Persistent ChromaDB vector store
├── config/                 # Configuration files (API keys, model settings)
├── data/                   # Raw and processed anime datasets
├── pipeline/               # Data ingestion & embedding pipeline
│   └── build_pipeline.py   # Entry point to build the vector store
├── src/                    # Core logic: retrieval, LLM interaction, ranking
├── utils/                  # Shared utility functions and helpers
├── main.py                 # Alternate entry point
├── Dockerfile              # Container image definition
├── llmops-k8s.yaml         # Kubernetes deployment manifest
├── pyproject.toml          # Project metadata and build config
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
└── .python-version         # Pinned Python version
```

---

## Getting Started

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
uv pip install -e .
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

All model settings, API keys, and environment-specific parameters live in the `config/` directory. Create a `.env` file or update the config files before running the pipeline or the app.

| Parameter            | Description                              |
| -------------------- | ---------------------------------------- |
| `LLM_API_KEY`        | API key for the LLM / embedding provider |
| `EMBEDDING_MODEL`    | Name of the embedding model to use       |
| `CHROMA_PERSIST_DIR` | Path to persist the ChromaDB database    |
| `TOP_K`              | Number of recommendations to return      |

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please make sure your code follows the existing style and that the pipeline runs cleanly before submitting.



<p align="center">Made with ❤️ for anime fans and MLOps enthusiasts</p>
