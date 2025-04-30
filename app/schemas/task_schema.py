from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskIn(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    user_id: str

class TaskOut(TaskIn):
    id: str = Field(..., description="ID de la tarea en Firestore")

    class Config:
        orm_mode = True
        # Esto asegura que los datetime se conviertan a ISO strings
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }