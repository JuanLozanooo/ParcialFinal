from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator

class FlightsBase(SQLModel):
    origen: str = Field(..., min_length=3, max_length=50)
    destino: str = Field(..., min_length=3, max_length=50)
    fecha: str = Field(..., min_length=3, max_length=50)

class Flights(FlightsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class FlightsCreate(FlightsBase):
    pass

class FlightsRead(FlightsBase):
    id: int

class FlightsUpdate(SQLModel):
    origen: Optional[str] = Field(None, min_length=3, max_length=50)
    destino: Optional[str] = Field(None, min_length=3, max_length=50)
    fecha: Optional[str] = Field(None, min_length=3, max_length=50)

    @validator('*', pre=True)
    def skip_blank_strings(cls, v):
        if v == "":
            return None
        return v

class FlightsResponse(SQLModel):
    id: int
    origen: str
    destino: str
    fecha: str

class DeletedPets(FlightsBase, table=True):
    __tablename__ = "deleted_flights"
    id: Optional[int] = Field(default=None, primary_key=True)
