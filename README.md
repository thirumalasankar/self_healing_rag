```
🚀 Self-Healing Retrieval-Augmented Generation (RAG)

A production-style **Self-Healing Retrieval-Augmented Generation (RAG) system** designed to improve
LLM reliability by evaluating generated responses and automatically retrying retrieval when answer confidence is low.

Built with:

🐍 Python  
⚡ FastAPI  
🧠 Phi-3 LLM via Ollama  
🔎 FAISS Vector Database  
📚 SentenceTransformers  
🖥 Streamlit UI  
🐳 Docker  

--------------------------------------------------

🧠 OVERVIEW

Large Language Models (LLMs) are powerful but can **hallucinate when answering questions outside their training data**.

Retrieval-Augmented Generation (RAG) reduces hallucinations by retrieving relevant knowledge from external documents and grounding responses in real context.

This project implements a **Self-Healing RAG architecture**, where the system evaluates its own answers and retries retrieval automatically when confidence is low.

--------------------------------------------------

🔁 WHY SELF-HEALING RAG?

Traditional RAG systems follow a single-pass workflow:

Query → Retrieval → Generation → Answer

However, if the retrieved documents are poor quality, the final answer will also be poor.

This project introduces a **self-healing evaluation loop**:

Query → Retrieval → Generation → Evaluation → Retry Retrieval

This improves answer quality and mimics reliability mechanisms used in production GenAI systems.

--------------------------------------------------

✨ KEY FEATURES

✔ Self-healing reliability loop using answer confidence scoring  
✔ Semantic document retrieval using FAISS vector database  
✔ SentenceTransformer embeddings for contextual search  
✔ Query rewriting to improve retrieval quality  
✔ Similarity score filtering to detect weak document matches  
✔ Observability logging for debugging and monitoring  
✔ FastAPI backend APIs for scalable inference  
✔ Streamlit interactive UI for real-time querying  
✔ Docker containerization for reproducible deployment  

--------------------------------------------------

🏗 SYSTEM ARCHITECTURE

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

--------------------------------------------------

🔄 END-TO-END WORKFLOW

1️⃣ User Query  
User submits a question via **Streamlit UI or FastAPI API**.

2️⃣ Query Rewriting  
Short or ambiguous queries are rewritten to improve document retrieval.

3️⃣ Document Retrieval  
Query embeddings are generated and FAISS performs vector similarity search to retrieve relevant document chunks.

4️⃣ Context Construction  
Retrieved documents are injected into the LLM prompt.

5️⃣ Answer Generation  
The **Phi-3 LLM running locally via Ollama** generates a grounded response.

6️⃣ Response Evaluation  
An evaluation module computes a **confidence score**.

7️⃣ Self-Healing Retry  
If confidence is low:
- retrieval is retried
- documents are refreshed
- answer is regenerated

--------------------------------------------------

📂 PROJECT STRUCTURE

self_healing_rag
├── app
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── generator.py
│   ├── evaluator.py
│   ├── query_rewriter.py
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

--------------------------------------------------

🛠 TECHNOLOGY STACK

Backend          : FastAPI  
LLM              : Phi-3 (Ollama)  
Vector Database  : FAISS  
Embeddings       : SentenceTransformers  
Frontend         : Streamlit  
Deployment       : Docker  
Language         : Python  

--------------------------------------------------

⚡ RUNNING LOCALLY

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

--------------------------------------------------

🐳 DOCKER DEPLOYMENT

Build containers

docker compose build

Run containers

docker compose up

Access services:

FastAPI API  
http://localhost:8000

Streamlit UI  
http://localhost:8501

--------------------------------------------------

📡 EXAMPLE API RESPONSE

{
 "answer": "...",
 "confidence": 0.74,
 "attempts": 1,
 "similarity_scores": [0.81,0.75,0.72],
 "retrieved_docs": 3
}

--------------------------------------------------

📊 OBSERVABILITY

The system logs key runtime signals:

• similarity scores  
• evaluation confidence  
• retry attempts  
• retrieved document count  

These metrics help monitor and debug RAG system performance.

--------------------------------------------------

🚀 FUTURE IMPROVEMENTS

• Hybrid Search (BM25 + Vector Search)  
• Cross-Encoder Re-ranking  
• Redis caching layer  
• Kubernetes deployment  
• CI/CD pipelines for automated deployment  

--------------------------------------------------

👨‍💻 AUTHOR

Thirumala Sankar Gurijala

GitHub  
https://github.com/thirumalasankar
```
