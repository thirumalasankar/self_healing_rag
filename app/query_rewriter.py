import ollama

def rewrite_query(query):

    prompt = f"Rewrite this question to improve search retrieval: {query}"

    response = ollama.chat(
        model="phi3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]