from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import httpx

router = APIRouter(prefix="/tasks", tags=["tasks"])


class PlanRequest(BaseModel):
    goal: str = Field(..., min_length=1)
    context: str = Field(default="")


@router.get("/status")
async def task_status():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("http://backend:8001/agent/tasks")
            response.raise_for_status()
            return response.json()
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))


@router.post("/plan")
async def generate_plan(payload: PlanRequest):
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(
                "http://backend:8001/agent/plan",
                json={"goal": payload.goal, "context": payload.context},
            )
            response.raise_for_status()
            return response.json()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Backend planning failed: {exc}")
