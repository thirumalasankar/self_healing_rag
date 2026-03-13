from langgraph.graph import StateGraph
from app.retriever import retrieve_docs
from app.generator import generate_answer
from app.evaluator import evaluate_answer

class AgentState(dict):
    pass

def retrieve(state):

    docs = retrieve_docs(state["query"])

    state["docs"] = docs

    return state

def generate(state):

    answer = generate_answer(
        state["query"],
        state["docs"]
    )

    state["answer"] = answer

    return state

def evaluate(state):

    score = evaluate_answer(
        state["answer"],
        state["docs"]
    )

    state["score"] = score

    return state

builder = StateGraph(AgentState)

builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)
builder.add_node("evaluate", evaluate)

builder.set_entry_point("retrieve")

builder.add_edge("retrieve","generate")
builder.add_edge("generate","evaluate")

graph = builder.compile()