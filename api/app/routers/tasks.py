from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/status")
async def task_status():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("http://backend:8001/agent/tasks")
            response.raise_for_status()
            return response.json()
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))
