from pydantic.v1 import BaseModel, EmailStr
from datetime import datetime


class CategoryRequest(BaseModel):
    name: str
    description: str


class CategoryResponse(CategoryRequest):
    id: int

    class Config:
        orm_mode = True


# # Provide only necessary field
# class CategoryResponse(BaseModel):
#     id: int
#     name: str
#     # description: str
#
#     class Config:
#         orm_mode = True


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime


    class Config:
        orm_mode = True

