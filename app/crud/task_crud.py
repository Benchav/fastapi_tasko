from typing import List, Optional
from datetime import datetime
from app.schemas.task_schema import TaskIn, TaskOut
from app.core.firestore import tareas_col

def parse_due_date(d):
    raw = d.get("due_date")
    if isinstance(raw, datetime):
        return raw
    if isinstance(raw, str):
        try:
            return datetime.fromisoformat(raw)
        except ValueError:
            return None
    return None

def create_task(data: TaskIn) -> TaskOut:
    # creo el documento vacío
    doc_ref = tareas_col.document()
    # preparo el payload sin due_date
    payload = data.dict(exclude={"due_date"}, by_alias=False, exclude_none=True)
    # lo guardo
    tareas_col.document(doc_ref.id).set(payload)

    # ahora, si viene due_date, lo agrego como ISO string
    if data.due_date:
        tareas_col.document(doc_ref.id).update({
            "due_date": data.due_date.isoformat()
        })

    return TaskOut(id=doc_ref.id, **data.dict())


def get_all_tasks() -> List[TaskOut]:
    out = []
    for doc in tareas_col.stream():
        d = doc.to_dict()
        d["due_date"] = parse_due_date(d)
        out.append(TaskOut(id=doc.id, **d))
    return out

def get_task_by_id(task_id: str) -> Optional[TaskOut]:
    doc = tareas_col.document(task_id).get()
    if not doc.exists:
        return None
    d = doc.to_dict()
    d["due_date"] = parse_due_date(d)
    return TaskOut(id=doc.id, **d)

def update_task(task_id: str, data: TaskIn) -> Optional[TaskOut]:
    doc_ref = tareas_col.document(task_id)
    if not doc_ref.get().exists:
        return None
    payload = data.dict(exclude_none=True)
    if payload.get("due_date"):
        payload["due_date"] = payload["due_date"].isoformat()
    doc_ref.update(payload)
    d = doc_ref.get().to_dict()
    d["due_date"] = parse_due_date(d)
    return TaskOut(id=doc_ref.id, **d)

def delete_task(task_id: str) -> bool:
    doc_ref = tareas_col.document(task_id)
    if not doc_ref.get().exists:
        return False
    doc_ref.delete()
    return True

def get_tasks_by_user(user_id: str) -> List[TaskOut]:
    out = []
    for doc in tareas_col.where("user_id", "==", user_id).stream():
        d = doc.to_dict()
        d["due_date"] = parse_due_date(d)
        out.append(TaskOut(id=doc.id, **d))
    return out