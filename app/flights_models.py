from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator

class FlightsBase(SQLModel):
    origen: str = Field(..., min_length=3, max_length=50)
    destino: str = Field(..., min_length=3, max_length=50)
    fecha: str = Field(..., min_length=3, max_length=50)

class Flights(FlightsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class FlightsRead(FlightsBase):
    id: int

class FlightsResponse(SQLModel):
    id: int
    origen: str
    destino: str
    fecha: str

