from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserIn(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)

class UserOut(UserIn):
    id: str
