from fastapi import FastAPI
from app.rag_pipeline import rag_pipeline

app = FastAPI()

@app.post("/ask")

def ask(query:str):

    result = rag_pipeline(query)

    return result