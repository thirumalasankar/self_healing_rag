import ollama

def generate_answer(query, docs):

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Use the following context to answer the question.
Answer the question based only on the context.

If the answer is not in the context say:
"I cannot find this information in the context provided." and do not attempt to answer the question.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]