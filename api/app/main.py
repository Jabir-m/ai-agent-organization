from fastapi import FastAPI
from app.routers.agents import router as agents_router
from app.routers.tasks import router as tasks_router
from app.routers.organization import router as organization_router
from app.routers.health import router as health_router

app = FastAPI(title="Agent API", version="0.1.0")

app.include_router(health_router)
app.include_router(agents_router)
app.include_router(tasks_router)
app.include_router(organization_router)


@app.get("/")
async def root():
    return {"service": "agent-api", "status": "running"}
