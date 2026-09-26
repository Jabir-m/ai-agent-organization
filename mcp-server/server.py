from pydantic import BaseModel
import httpx
from fastapi import FastAPI

app = FastAPI(title="MCP Server", version="0.1.0")


class ToolRequest(BaseModel):
    prompt: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/tool/llm")
async def llm_tool(req: ToolRequest):
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            "http://ollama:11434/api/generate",
            json={
                "model": "llama3.1",
                "prompt": req.prompt,
                "stream": False,
            },
        )
        response.raise_for_status()
        data = response.json()
        return {"output": data.get("response", "")}
