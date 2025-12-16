TOOLS = {}

def register_tool(name, fn):
    TOOLS[name] = fn

def get_tool(name):
    return TOOLS[name]

def detect_smells(code):
    return {"issues": len(code) % 5}

def complexity_check(code):
    return {"complexity": len(code.splitlines())}
