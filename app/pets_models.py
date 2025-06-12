from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator

class PetsBase(SQLModel):
    id_vuelo: int = Field(..., ge=10, le=100)
    nombre: str = Field(..., min_length=3, max_length=50)
    edad: int = Field(..., ge=10, le=100)
    raza: str = Field(..., min_length=3, max_length=50)

class Pets(PetsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class PetsCreate(PetsBase):
    pass

class PetsRead(PetsBase):
    id: int

class PetsUpdate(SQLModel):
    id_vuelo: Optional[int] = Field(..., ge=10, le=100)
    nombre: Optional[str] = Field(None, min_length=3, max_length=50)
    edad: Optional[int] = Field(..., ge=10, le=100)
    raza: Optional[str] = Field(None, min_length=3, max_length=50)

    @validator('*', pre=True)
    def skip_blank_strings(cls, v):
        if v == "":
            return None
        return v

class PetsResponse(SQLModel):
    id: int
    id_vuelo: int
    nombre: str
    edad: int
    raza: str

class DeletedPets(PetsBase, table=True):
    __tablename__ = "deleted_pets"
    id: Optional[int] = Field(default=None, primary_key=True)