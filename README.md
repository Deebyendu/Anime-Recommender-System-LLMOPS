<div align="center">

# 🎌 Anime Recommender System

### An intelligent, LLM-powered anime recommendation engine built with production-grade LLMOps practices

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-F55036?style=for-the-badge)](https://groq.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-orange?style=for-the-badge)](https://www.trychroma.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

</div>

🌐 Live Demo
👉 http://docker-aws-anime-recommendation-1990735088.eu-north-1.elb.amazonaws.com/

---

## 📖 Overview

The **Anime Recommender System** uses Large Language Models (LLMs) combined with semantic vector search to deliver highly relevant anime recommendations from natural language queries. Simply describe what you're in the mood for — the system understands your intent and surfaces the most fitting titles.

> _"dark psychological thriller with a morally grey protagonist"_
> _"feel-good slice-of-life with great music"_

Built with **LLMOps best practices** — structured ingestion pipelines, persistent vector storage via ChromaDB, a clean Streamlit frontend, and full Docker + Kubernetes support for production deployments and deployed in AWS.

---

## ✨ Features

- 🔍 **Semantic Search** — understands natural language, not just keywords
- 🧠 **LLM-Powered** — leverages large language models for intelligent query processing
- 📦 **Vector Store** — fast similarity search with ChromaDB persistence
- 🎨 **Streamlit UI** — clean, interactive web interface
- 🐳 **Dockerised** — fully containerised for consistent environments
- ☸️ **Kubernetes Ready** — production deployment manifest included
- 📋 **Structured Logging** — centralised logging and custom exception handling

---

## 🛠️ Tech Stack

| Layer            | Technology                              |
| ---------------- | --------------------------------------- | --- |
| Language         | Python 3.10+                            |
| LLM Inference    | [Groq](https://groq.com/)               |
| Embeddings       | [Hugging Face](https://huggingface.co/) |
| Vector Store     | [ChromaDB](https://www.trychroma.com/)  |
| Frontend         | [Streamlit](https://streamlit.io/)      |
| Package Manager  | [.venv]                                 |     |
| Containerisation | Docker                                  |
| Orchestration    | Kubernetes                              |

---

## 🔍 How It Works

This project is built on a **RAG (Retrieval-Augmented Generation)** pipeline that combines semantic vector search with LLM-powered response generation. Here's the end-to-end flow:

**1. 📥 Data Ingestion (`data_loader.py`)**
The pipeline reads `anime_with_synopsis.csv` and `updated_anime.csv`, cleans the raw anime metadata, and prepares each title's synopsis as a structured document ready for embedding.

**2. 🧮 Embedding & Indexing (`vectore_store.py`)**
Each anime synopsis is passed through a **Hugging Face sentence-transformer model** to generate a dense semantic vector. These vectors are then indexed and persisted in **ChromaDB**, a local vector database — this only runs once via `build_pipeline.py`.

**3. 💬 Query Processing (`recommender.py`)**
When a user submits a natural language query (e.g. _"dark thriller with a twist ending"_), that query is embedded using the **same Hugging Face model**, producing a query vector.

**4. 🔎 Semantic Retrieval (`vectore_store.py`)**
The query vector is compared against all stored anime vectors in ChromaDB using **cosine similarity**. The top-K most semantically similar anime are retrieved as candidates.

**5. 🧠 LLM Response Generation (`prompt_template.py` + Groq)**
The retrieved anime candidates are injected into a carefully engineered prompt template, which is then sent to the **Groq LLM API** (ultra-fast inference). Groq synthesises a coherent, natural language recommendation response from the candidates.

**6. 🖥️ Display (`app/app.py`)**
The final recommendations are rendered in a clean **Streamlit** interface, where the user can refine their query and explore results interactively.

---

## 🏗️ Architecture

```
                        ┌─────────────────────────┐
                        │      Streamlit UI        │
                        │       (app/app.py)        │
                        └────────────┬────────────┘
                                     │ Natural Language Query
                                     ▼
                        ┌─────────────────────────┐
                        │    Recommender Engine    │
                        │    (src/recommender.py)  │
                        └────────────┬────────────┘
                                     │ Embed Query
                                     ▼
                        ┌─────────────────────────┐
                        │   ChromaDB Vector Store  │◄──── Build Pipeline
                        │       (chroma_db/)        │      (pipeline/)
                        └────────────┬────────────┘
                                     │ Top-K Similar Anime
                                     ▼
                        ┌─────────────────────────┐
                        │   LLM Response Builder   │
                        │ (src/prompt_template.py) │
                        └────────────┬────────────┘
                                     │
                                     ▼
                           Recommendations ✅
```

**Offline Build Pipeline:**

```
  anime_with_synopsis.csv
  updated_anime.csv
          │
          ▼
  data_loader.py  ──►  vectore_store.py  ──►  chroma_db/
  (clean & prep)        (embed & index)       (persisted)
```

---

## 🗂️ Project Structure

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
├── pyproject.toml                # Project metadata and build configuration
├── requirements.txt              # Python dependencies
└── setup.py                      # Package setup
```

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Version |
| ----------- | ------- |
| Python      | ≥ 3.10  |

| .venv
| Docker | Latest (optional) |
| kubectl | Latest (optional, for K8s) |

### 1. Clone the Repository

```bash
git clone https://github.com/Deebyendu/Anime-Recommender-System-LLMOPS.git
cd Anime-Recommender-System-LLMOPS
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
HF_TOKEN=your_huggingface_token_here
GROQ_API_KEY=your_groq_api_key_here
```

> **HF_TOKEN** — Get it from [Hugging Face Settings](https://huggingface.co/settings/tokens)
> **GROQ_API_KEY** — Get it from [Groq Console](https://console.groq.com/keys)

### 3. Install Dependencies

```bash
pip install -e .
```

### 4. Build the Vector Store

Run the ingestion pipeline to process the anime dataset and populate ChromaDB:

```bash
python pipeline/build_pipeline.py
```

This will:

- Load and preprocess anime data from `data/`
- Generate semantic embeddings using the configured model
- Persist the indexed vectors to `chroma_db/`

### 5. Launch the App

```bash
streamlit run app/app.py
```

Open your browser at **`http://localhost:8501`** and start exploring! 🎉

---

## 🐳 Docker

Build and run the entire application in a container:

```bash
# Build the image
docker build -t anime-recommender:latest .

# Run the container
docker run -p 8501:8501 --env-file .env anime-recommender:latest
```

The app will be available at `http://localhost:8501`.

---

## ☸️ Kubernetes Deployment

Deploy to a Kubernetes cluster using the provided manifest:

```bash
# Create a secret for sensitive credentials
kubectl create secret generic llmops-secrets \
  --from-literal=LLM_API_KEY=your_api_key_here

# Apply the deployment manifest
kubectl apply -f llmops-k8s.yaml

# Verify the deployment
kubectl get pods
kubectl get svc
```

---

## ⚙️ Configuration

All settings are managed through `config/config.py` and the `.env` file:

| Variable       | Description                           | Where to Get                                                             |
| -------------- | ------------------------------------- | ------------------------------------------------------------------------ |
| `HF_TOKEN`     | Hugging Face API token for embeddings | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| `GROQ_API_KEY` | Groq API key for LLM inference        | [console.groq.com/keys](https://console.groq.com/keys)                   |

Made with ❤️ for anime fans and MLOps enthusiasts

</div>
