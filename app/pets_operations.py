from typing import List, Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.pets_models import *


class PetsOperations:

    @staticmethod
    async def find_all_pets(session: AsyncSession) -> List[Pets]:
        result = await session.execute(select(Pets))
        return result.scalars().all()

    @staticmethod
    async def create_pet(session: AsyncSession, data: dict) -> Pets:
        new_entry = Pets(**data)
        session.add(new_entry)
        await session.commit()
        await session.refresh(new_entry)
        return new_entry

    @staticmethod
    async def update_pet(session: AsyncSession, entry_id: int, update_data: dict) -> Optional[Pets]:
        """Modifica un registro existente, permitiendo cambios parciales o totales"""
        entry = await session.get(Pets, entry_id)
        if not entry:
            return None

        for key, value in update_data.items():
            if hasattr(entry, key):
                # Solo actualiza si el valor no es None ni una cadena vacía
                if value not in (None, ""):
                    setattr(entry, key, value)

        await session.commit()
        await session.refresh(entry)
        return entry

    @staticmethod
    async def kill_pet(session: AsyncSession, entry_id: int) -> Optional[Pets]:
        entry = await session.get(Pets, entry_id)
        if not entry:
            return None

        # Validar los datos antes de crear la copia
        try:
            deleted_entry = DeletedPets(**entry.dict())
        except ValueError as e:
            # Manejar errores de validación
            raise ValueError(f"Error al validar los datos para la tabla de eliminados: {e}")

        session.add(deleted_entry)
        await session.delete(entry)
        await session.commit()
        return entry