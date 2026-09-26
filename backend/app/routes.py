from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.llm import generate_response
from app.store import create_plan, create_task, list_tasks, update_task_status

router = APIRouter(prefix="/agent", tags=["agent"])


class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1)


class PlanRequest(BaseModel):
    goal: str = Field(..., min_length=1)
    context: str = Field(default="")


class TaskStatusUpdate(BaseModel):
    task_id: str
    status: str


@router.post("/chat")
async def chat(request: ChatRequest):
    reply = await generate_response(request.prompt)
    return {"reply": reply}


@router.post("/plan")
async def plan(request: PlanRequest):
    plan = create_plan(goal=request.goal, context=request.context)
    tasks = [
        {"id": item["id"], "title": item["title"], "status": item["status"]}
        for item in plan["tasks"]
    ]
    return {"plan": plan["summary"], "tasks": tasks}


@router.get("/tasks")
async def tasks():
    return {"tasks": list_tasks()}


@router.post("/tasks")
async def create_task_route(request: ChatRequest):
    task = create_task(request.prompt)
    return {"task": task}


@router.patch("/tasks/{task_id}/status")
async def update_status(task_id: str, update: TaskStatusUpdate):
    if update.task_id != task_id:
        raise HTTPException(status_code=400, detail="Task ID mismatch")
    return {"task": update_task_status(task_id, update.status)}
