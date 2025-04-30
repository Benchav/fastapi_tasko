from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.task_schema import TaskIn, TaskOut
from app.crud.task_crud import (
    create_task, get_all_tasks,
    get_task_by_id, update_task, delete_task,
    get_tasks_by_user
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut)
def route_create_task(data: TaskIn):
    return create_task(data)

@router.get("/", response_model=List[TaskOut])
def route_get_tasks():
    return get_all_tasks()

@router.get("/{task_id}", response_model=TaskOut)
def route_get_task(task_id: str):
    t = get_task_by_id(task_id)
    if not t:
        raise HTTPException(404, "Tarea no encontrada")
    return t

@router.put("/{task_id}", response_model=TaskOut)
def route_update_task(task_id: str, data: TaskIn):
    t = update_task(task_id, data)
    if not t:
        raise HTTPException(404, "Tarea no encontrada")
    return t

@router.delete("/{task_id}", status_code=204)
def route_delete_task(task_id: str):
    if not delete_task(task_id):
        raise HTTPException(404, "Tarea no encontrada")

@router.get("/user/{user_id}", response_model=List[TaskOut])
def route_tasks_by_user(user_id: str):
    return get_tasks_by_user(user_id)