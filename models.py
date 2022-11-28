from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID, uuid4

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    username: str
    phone: int
    email: EmailStr
    address: str


class UserUpdateRequest(BaseModel):
    username: Optional[str]
    phone: Optional[int]
    email: Optional[EmailStr]
    address: Optional[str]