from fastapi import APIRouter
from app.llm import generate_response

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/chat")
async def chat(prompt: str):
    reply = await generate_response(prompt)
    return {"reply": reply}
