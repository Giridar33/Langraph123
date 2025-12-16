from fastapi import FastAPI
from uuid import uuid4

from app.engine.graph import Graph

from app.engine.runner import GraphRunner
from app.workflows.code_review import build_workflow
from app.store import GRAPHS, RUNS
from app.models import GraphCreateResponse, GraphRunRequest, GraphRunResponse

app = FastAPI()

@app.post("/graph/create")
def create_graph():
    nodes, edges, start = build_workflow()
    graph_id = str(uuid4())
    GRAPHS[graph_id] = Graph(nodes, edges, start)
    return {"graph_id": graph_id}


@app.post("/graph/run")
def run_graph(graph_id: str, initial_state: dict):
    graph = GRAPHS[graph_id]
    runner = GraphRunner(graph)
    final_state, log = runner.run(initial_state)

    run_id = str(uuid4())
    RUNS[run_id] = final_state

    return {
        "run_id": run_id,
        "final_state": final_state,
        "log": log
    }


@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return RUNS[run_id]
