from fastapi import APIRouter
import httpx

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/status")
async def agent_status():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("http://backend:8001/health")
            response.raise_for_status()
            return response.json()
    except Exception:
        return {"status": "degraded", "service": "backend"}
