from fastapi import APIRouter

router = APIRouter(prefix="/organization", tags=["organization"])


@router.get("/summary")
async def summary():
    return {
        "name": "Hermes Organization",
        "status": "active",
        "focus": ["planning", "execution", "tooling", "memory"],
        "agents": ["research", "ops", "code", "support"],
    }
