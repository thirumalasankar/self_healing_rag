from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_answer(answer, docs):

    doc_text = " ".join([d.page_content for d in docs])

    emb_answer = model.encode([answer])
    emb_docs = model.encode([doc_text])

    similarity = cosine_similarity(emb_answer, emb_docs)[0][0]

    confidence = float(similarity)

    evaluation = {
        "confidence": confidence,
        "context_used": len(docs)
    }

    return evaluation