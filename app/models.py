from pydantic import BaseModel
from typing import Dict, Any, List, Optional


# -------- Graph Creation --------
class GraphCreateResponse(BaseModel):
    graph_id: str


# -------- Graph Run --------
class GraphRunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]


class GraphRunResponse(BaseModel):
    run_id: str
    final_state: Dict[str, Any]
    log: List[str]


# -------- State Query --------
class GraphStateResponse(BaseModel):
    state: Dict[str, Any]
