from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

#code to print the total number of vectors in the vector store
print("Total vectors:", db.index.ntotal)

#code to print the content of the first few documents in the vector store
docs = db.docstore._dict
for k,v in docs.items():
    print(v.page_content[:200])
