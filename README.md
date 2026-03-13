# 🚀 Self-Healing Retrieval-Augmented Generation (RAG)

A production-style **Self-Healing Retrieval-Augmented Generation (RAG)** system that improves the reliability of Large Language Models (LLMs) by evaluating generated responses and automatically retrying retrieval when answer confidence is low.

The system combines **vector search, LLM reasoning, and automated evaluation loops** to reduce hallucinations and improve response quality.

---

# 🧠 Overview

Large Language Models are powerful but often **hallucinate when answering questions outside their training data**.

**Retrieval-Augmented Generation (RAG)** solves this by retrieving relevant information from external documents and providing it as context to the LLM.

This project extends the traditional RAG pipeline by introducing a **Self-Healing loop**, where the system evaluates its own responses and retries retrieval when answer confidence is low.

This approach improves **accuracy, robustness, and reliability** of AI-powered question answering systems.

---

# 🔁 Self-Healing RAG Concept

Traditional RAG workflow:

Query → Retrieval → Generation → Answer

If retrieved documents are poor, the final answer will also be poor.

Self-Healing RAG introduces an evaluation loop:

Query → Retrieval → Generation → Evaluation → Retry Retrieval

If confidence is low:
- retrieval is retried
- new documents are fetched
- the answer is regenerated

---

# ✨ Features

- Self-healing answer evaluation loop
- Semantic search using FAISS vector database
- SentenceTransformer embeddings for contextual retrieval
- Query rewriting for improved document matching
- Similarity score filtering
- FastAPI backend for scalable APIs
- Streamlit UI for interactive querying
- Observability logging for debugging
- Docker support for easy deployment

---

# 🏗 System Architecture

User Query  
↓  
FastAPI API  
↓  
Query Rewriter  
↓  
Retriever (FAISS Vector Search)  
↓  
Context Builder  
↓  
Generator (Phi-3 via Ollama)  
↓  
Answer Evaluator  
↓  
High Confidence → Return Answer  
Low Confidence → Retry Retrieval  

---

# 🔄 End-to-End Workflow

### 1️⃣ User Query
User submits a query via **Streamlit UI or FastAPI API**.

### 2️⃣ Query Rewriting
Short or ambiguous queries are rewritten to improve retrieval.

### 3️⃣ Document Retrieval
The system generates embeddings and retrieves relevant document chunks using **FAISS vector similarity search**.

### 4️⃣ Context Construction
Retrieved documents are injected into the LLM prompt.

### 5️⃣ Answer Generation
The **Phi-3 model running via Ollama** generates a grounded response.

### 6️⃣ Response Evaluation
An evaluation module calculates a **confidence score**.

### 7️⃣ Self-Healing Retry
If confidence is below the threshold:
- retrieval is retried
- documents are refreshed
- answer is regenerated

---

# 📂 Project Structure

```
self_healing_rag
│
├── app
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── generator.py
│   ├── evaluator.py
│   ├── query_rewriter.py
│   └── logger.py
│
├── scripts
│   ├── ingest.py
│   └── check_vector_db.py
│
├── ui
│   └── streamlit_app.py
│
├── vector_store
│   ├── index.faiss
│   └── index.pkl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
```

---

# 🛠 Technology Stack

Backend : FastAPI  
LLM : Phi-3 (Ollama)  
Vector Database : FAISS  
Embeddings : SentenceTransformers  
Frontend : Streamlit  
Deployment : Docker  
Language : Python  

---

# ⚡ Running Locally

### Install dependencies

```
pip install -r requirements.txt
```

### Pull LLM model

```
ollama pull phi3
```

### Ingest documents

```
python scripts/ingest.py
```

### Start FastAPI server

```
uvicorn app.main:app --reload
```

API available at:

```
http://localhost:8000
```

### Run Streamlit UI

```
streamlit run ui/streamlit_app.py
```

UI available at:

```
http://localhost:8501
```

---

# 🐳 Docker Deployment

### Build containers

```
docker compose build
```

### Run containers

```
docker compose up
```

Services:

FastAPI API  
http://localhost:8000

Streamlit UI  
http://localhost:8501

---

# 📡 Example API Response

```
{
 "answer": "...",
 "confidence": 0.74,
 "attempts": 1,
 "similarity_scores": [0.81,0.75,0.72],
 "retrieved_docs": 3
}
```

---

# 📊 Observability

The system logs important runtime signals including:

- similarity scores
- evaluation confidence
- retry attempts
- retrieved document count

These metrics help monitor and debug the RAG pipeline.

---

# 🚀 Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Cross-Encoder Re-ranking
- Redis caching layer
- Kubernetes deployment
- CI/CD pipelines

---

# 👨‍💻 Author

**Thirumala Sankar Gurijala**

GitHub  
https://github.com/thirumalasankar
