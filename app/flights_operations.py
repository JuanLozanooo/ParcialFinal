from typing import List, Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.flights_models import *


class FlightsOperations:

    @staticmethod
    async def find_all_flights(session: AsyncSession) -> List[Flights]:
        result = await session.execute(select(Flights))
        return result.scalars().all()

    @staticmethod
    async def search_flights_by_origin(session: AsyncSession, origen: str) -> List[Flights]:
        result = await session.execute(
            select(Flights).where(Flights.origen.ilike(f"%{origen}%"))
        )
        return result.scalars().all()

    @staticmethod
    async def find_flights_by_destiny(session: AsyncSession, destino: str) -> List[Flights]:
        result = await session.execute(
            select(Flights).where(Flights.destino.ilike(f"%{destino}%"))
        )
        return result.scalars().all()

    @staticmethod
    async def find_flights_by_date(session: AsyncSession, fecha: str) -> List[Flights]:
        result = await session.execute(
            select(Flights).where(Flights.fecha.ilike(f"%{fecha}%"))
        )
        return result.scalars().all()
