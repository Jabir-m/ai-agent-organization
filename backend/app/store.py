from uuid import uuid4

_TASKS = {}
_PLANS = {}


def _break_goal_into_tasks(goal: str):
    segments = [
        "Clarify scope and success metrics",
        "Identify required inputs and dependencies",
        "Execute the implementation or workflow",
        "Review outcomes and summarize next steps",
    ]
    return [
        {"id": str(uuid4())[:8], "title": f"{goal}: {segment}", "status": "pending"}
        for segment in segments
    ]


def create_plan(goal: str, context: str = ""):
    tasks = _break_goal_into_tasks(goal)
    plan_id = str(uuid4())
    _PLANS[plan_id] = {"goal": goal, "context": context, "tasks": tasks}
    for task in tasks:
        _TASKS[task["id"]] = task
    return {
        "id": plan_id,
        "goal": goal,
        "summary": f"Plan created for: {goal}",
        "tasks": tasks,
    }


def create_task(title: str):
    task_id = str(uuid4())[:8]
    task = {"id": task_id, "title": title, "status": "pending"}
    _TASKS[task_id] = task
    return task


def list_tasks():
    return list(_TASKS.values())


def update_task_status(task_id: str, status: str):
    task = _TASKS.get(task_id)
    if not task:
        raise KeyError("Task not found")
    task["status"] = status
    return task
