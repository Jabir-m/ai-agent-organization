from fastapi import APIRouter
import httpx

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/status")
async def agent_status():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://backend:8001/health")
        return response.json()
