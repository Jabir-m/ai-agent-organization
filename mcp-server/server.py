from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI(title="MCP Server", version="0.1.0")


class ToolRequest(BaseModel):
    tool: str
    args: dict = {}


TOOLS = {
    "llm": {"description": "Run a prompt through Ollama"},
    "task": {"description": "Check task state"},
    "organization": {"description": "Get organization summary"},
}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/tools")
async def list_tools():
    return {"tools": TOOLS}


@app.post("/tool/execute")
async def execute_tool(request: ToolRequest):
    if request.tool == "llm":
        prompt = request.args.get("prompt", "")
        async with httpx.AsyncClient(timeout=180.0) as client:
            response = await client.post(
                "http://ollama:11434/api/generate",
                json={"model": "llama3.1", "prompt": prompt, "stream": False},
            )
            response.raise_for_status()
            payload = response.json()
            return {"tool": request.tool, "output": payload.get("response", "")}

    if request.tool == "task":
        return {"tool": request.tool, "output": {"status": "pending", "tasks": 0}}

    if request.tool == "organization":
        return {
            "tool": request.tool,
            "output": {
                "name": "Hermes Organization",
                "status": "active",
                "focus": ["planning", "execution", "tooling", "memory"],
            },
        }

    return {"tool": request.tool, "output": "unknown tool"}
