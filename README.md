```
Self-Healing Retrieval-Augmented Generation (RAG)

A production-style Self-Healing Retrieval-Augmented Generation (RAG) system built with:
Python, FastAPI, FAISS, SentenceTransformers, Phi-3 via Ollama, LangGraph, Streamlit UI, and Docker.

OVERVIEW
Large Language Models (LLMs) can hallucinate when answering questions outside their training data.
Retrieval-Augmented Generation (RAG) improves reliability by retrieving relevant documents from a
knowledge base and grounding LLM responses in real data.

WHY SELF-HEALING RAG?
Traditional RAG pipelines:
Query → Retrieval → Generation → Answer

Self-Healing RAG introduces an evaluation loop:
Query → Retrieval → Generation → Evaluate → Retry if confidence is low

KEY FEATURES
- Self-healing reliability loop
- Semantic retrieval with FAISS
- SentenceTransformer embeddings
- Query rewriting for better retrieval
- Similarity score filtering
- Observability logging
- FastAPI backend APIs
- Streamlit interactive UI
- Docker containerization

SYSTEM ARCHITECTURE

User Query
   ↓
FastAPI API
   ↓
Query Rewriter
   ↓
Retriever (FAISS)
   ↓
Context Builder
   ↓
Generator (Phi-3 via Ollama)
   ↓
Answer Evaluator
   ↓
High Confidence → Return Answer
Low Confidence → Self-Healing Loop

END-TO-END WORKFLOW

1. User Query
User asks a question via Streamlit UI or FastAPI.

2. Query Rewriting
Improves ambiguous queries for better retrieval.

3. Document Retrieval
Embeddings generated → FAISS similarity search → Top-k docs returned.

4. Context Construction
Retrieved documents combined into LLM prompt.

5. Answer Generation
Phi-3 LLM generates response grounded in context.

6. Response Evaluation
Evaluator produces confidence score.

7. Self-Healing Loop
If confidence is low:
- rewrite query
- retry retrieval
- regenerate answer

PROJECT STRUCTURE

self_healing_rag
├── app
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── generator.py
│   ├── evaluator.py
│   ├── query_rewriter.py
│   ├── agents.py
│   └── logger.py
├── scripts
│   ├── ingest.py
│   └── check_vector_db.py
├── ui
│   └── streamlit_app.py
├── vector_store
│   ├── index.faiss
│   └── index.pkl
├── Dockerfile
├── docker-compose.yml
├── requirements.txt

TECHNOLOGY STACK
Backend: FastAPI
LLM: Phi-3 (Ollama)
Vector Database: FAISS
Embeddings: SentenceTransformers
Agents: LangGraph
Frontend: Streamlit
Deployment: Docker
Language: Python

RUNNING LOCALLY

Install dependencies
pip install -r requirements.txt

Pull model
ollama pull phi3

Ingest documents
python scripts/ingest.py

Run API
uvicorn app.main:app --reload

Run UI
streamlit run ui/streamlit_app.py

DOCKER DEPLOYMENT

Build
docker compose build

Run
docker compose up

Access:
FastAPI → http://localhost:8000
Streamlit → http://localhost:8501

EXAMPLE API RESPONSE

{
 "answer": "...",
 "confidence": 0.74,
 "attempts": 1,
 "similarity_scores": [0.81,0.75,0.72],
 "retrieved_docs": 3
}

OBSERVABILITY
The system logs:
- similarity scores
- evaluation confidence
- retry attempts
- retrieved document count

FUTURE IMPROVEMENTS
- Hybrid search (BM25 + vector search)
- Cross-encoder reranking
- LangSmith evaluation dashboards
- Redis caching
- Kubernetes deployment
- CI/CD pipelines

AUTHOR
Thirumala Sankar Gurijala
https://github.com/thirumalasankar
```
