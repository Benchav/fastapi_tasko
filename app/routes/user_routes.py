from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user_schema import UserIn, UserOut
from app.crud.user_crud import (
    create_user, get_all_users,
    get_user_by_id, update_user, delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def route_create_user(data: UserIn):
    return create_user(data)

@router.get("/", response_model=List[UserOut])
def route_get_users():
    return get_all_users()

@router.get("/{user_id}", response_model=UserOut)
def route_get_user(user_id: str):
    u = get_user_by_id(user_id)
    if not u:
        raise HTTPException(404, "Usuario no encontrado")
    return u

@router.put("/{user_id}", response_model=UserOut)
def route_update_user(user_id: str, data: UserIn):
    u = update_user(user_id, data)
    if not u:
        raise HTTPException(404, "Usuario no encontrado")
    return u

@router.delete("/{user_id}", status_code=204)
def route_delete_user(user_id: str):
    if not delete_user(user_id):
        raise HTTPException(404, "Usuario no encontrado")