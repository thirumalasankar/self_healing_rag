import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.title("Self-Healing RAG System")

query = st.text_input("Ask a question")

if st.button("Ask"):

    if query:
        try:
            response = requests.post(
                API_URL,
                params={"query": query}
            )

            result = response.json()

            st.subheader("Answer")

            st.write(result["answer"])

            st.subheader("Confidence Score")

            st.progress(result["confidence"])
            st.subheader("System Diagnostics")

            st.write("Confidence:", result["confidence"])

            st.write("Attempts:", result["attempts"])

            st.write("Retrieved Docs:", result["retrieved_docs"])
            st.subheader("Similarity Scores")

            st.subheader("Similarity Scores")

            st.write(result["similarity_scores"])
            st.subheader("Retrieved Context")

            for doc in result["docs"]:
                st.write(doc)
        
        except:
            st.error("FastAPI server is not running. Start it with: uvicorn app.main:app --reload")