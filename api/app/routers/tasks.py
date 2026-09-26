from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/status")
async def task_status():
    return {"status": "idle", "jobs": 0}
