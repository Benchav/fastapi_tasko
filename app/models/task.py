from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class TaskDoc:
    id: str
    title: str
    description: Optional[str]
    completed: bool
    user_id: str
    due_date: Optional[datetime]