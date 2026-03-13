from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_db = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

# def retrieve_docs(query):

#     retriever = vector_db.as_retriever(
#         search_type="similarity",
#         search_kwargs={"k":3}
#     )

#     # docs = retriever.get_relevant_documents(query)
#     docs = retriever.invoke(query)
#     # return docs
#     filtered_docs = []

#     for d in docs:
#         #system avoids irrelevant context → fewer hallucinations.
#         if d.metadata.get("score", 0) > 0.3:
#             filtered_docs.append(d)

#     return filtered_docs  

def retrieve_docs(query):

    # return docs WITH similarity scores
    results = vector_db.similarity_search_with_score(query, k=3)

    docs = []
    scores = []

    for doc, score in results:
        docs.append(doc)
        scores.append(score)

    return docs, scores