from app.retriever import retrieve_docs
from app.generator import generate_answer
from app.evaluator import evaluate_answer
from app.logger import logger
from app.query_rewriter import rewrite_query


def rag_pipeline(query):

    query = rewrite_query(query)

    logger.info(f"Query received: {query}")

    max_attempts = 3
    attempt = 0

    docs, scores = retrieve_docs(query)

    logger.info(f"Retrieved docs: {len(docs)}")
    logger.info(f"Similarity scores: {scores}")

    # -------- Retrieval filtering ----------
    # detect if documents are irrelevant

    similarity_threshold = 0.8

    relevant_docs = []

    for doc, score in zip(docs, scores):

        if score < similarity_threshold:
            relevant_docs.append(doc)

    # if no relevant docs → stop pipeline
    if len(relevant_docs) == 0:

        logger.warning("No relevant documents found")

        return {
            "answer": "No relevant information found in the knowledge base.",
            "confidence": 0.0,
            "attempts": 0,
            "retrieved_docs": 0,
            "similarity_scores": [float(s) for s in scores],
        }

    docs = relevant_docs

    score = 0
    answer = ""

    while attempt < max_attempts:

        logger.info(f"Attempt number: {attempt + 1}")

        answer = generate_answer(query, docs)

        evaluation = evaluate_answer(answer, docs)

        score = evaluation["confidence"]

        logger.info(f"Evaluation score: {score}")

        if score >= 0.5:
            break

        docs, scores = retrieve_docs(query)

        attempt += 1

    return {
        "answer": answer,
        "confidence": float(score),
        "attempts": attempt,
        "retrieved_docs": len(docs),
        "similarity_scores": [float(s) for s in scores],
        "docs": [d.page_content for d in docs]
    }