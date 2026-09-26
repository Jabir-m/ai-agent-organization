import httpx
from app.config import OLLAMA_BASE_URL, OLLAMA_MODEL


async def generate_response(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=180.0) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.7, "top_p": 0.9},
            },
        )
        response.raise_for_status()
        payload = response.json()
        return payload.get("response", "")
