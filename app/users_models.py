from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator

class UsersBase(SQLModel):
    id_vuelo: int = Field(..., ge=0, le=1000000)
    nombre: str = Field(..., min_length=3, max_length=50)
    nombre_mascota: str = Field(..., min_length=3, max_length=50)

class Users(UsersBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UsersCreate(UsersBase):
    pass

class UsersRead(UsersBase):
    id: int

class UsersUpdate(SQLModel):
    id_vuelo: Optional[int] = Field(..., ge=0, le=1000000)
    nombre: Optional[str] = Field(None, min_length=3, max_length=50)
    nombre_mascota: Optional[str] = Field(None, min_length=3, max_length=50)

    @validator('*', pre=True)
    def skip_blank_strings(cls, v):
        if v == "":
            return None
        return v

class UsersResponse(SQLModel):
    id: int
    id_vuelo: int
    nombre: str
    nombre_mascota: str

class DeletedUsers(UsersBase, table=True):
    __tablename__ = "deleted_users"
    id: Optional[int] = Field(default=None, primary_key=True)