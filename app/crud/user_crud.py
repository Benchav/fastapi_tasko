from typing import List, Optional
from app.schemas.user_schema import UserIn, UserOut
from app.core.firestore import usuarios_col

def create_user(data: UserIn) -> UserOut:
    doc_ref = usuarios_col.document()
    usuarios_col.document(doc_ref.id).set(data.dict())
    return UserOut(id=doc_ref.id, **data.dict())

def get_all_users() -> List[UserOut]:
    out = []
    for doc in usuarios_col.stream():
        d = doc.to_dict()
        out.append(UserOut(id=doc.id, **d))
    return out

def get_user_by_id(user_id: str) -> Optional[UserOut]:
    doc = usuarios_col.document(user_id).get()
    if not doc.exists:
        return None
    d = doc.to_dict()
    return UserOut(id=doc.id, **d)

def update_user(user_id: str, data: UserIn) -> Optional[UserOut]:
    doc_ref = usuarios_col.document(user_id)
    if not doc_ref.get().exists:
        return None
    doc_ref.update(data.dict())
    return UserOut(id=user_id, **data.dict())

def delete_user(user_id: str) -> bool:
    doc_ref = usuarios_col.document(user_id)
    if not doc_ref.get().exists:
        return False
    doc_ref.delete()
    return True