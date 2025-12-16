from app.engine.graph import Node

from app.engine.tools import detect_smells, complexity_check

def extract_functions(state):
    state["functions"] = state["code"].count("def")
    return state

def check_complexity(state):
    state.update(complexity_check(state["code"]))
    return state

def detect_issues(state):
    state.update(detect_smells(state["code"]))
    return state

def suggest_improvements(state):
    score = 100 - (state["issues"] * 10 + state["complexity"])
    state["quality_score"] = score
    return state

def loop_condition(state):
    if state["quality_score"] < 70:
        return "detect_issues"
    return None


def build_workflow():
    nodes = {
        "extract": Node("extract", extract_functions),
        "complexity": Node("complexity", check_complexity),
        "detect_issues": Node("detect_issues", detect_issues),
        "suggest": Node("suggest", suggest_improvements),
    }

    edges = {
        "extract": "complexity",
        "complexity": "detect_issues",
        "detect_issues": "suggest",
        "suggest": loop_condition,
    }

    return nodes, edges, "extract"
