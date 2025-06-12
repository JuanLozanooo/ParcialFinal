from typing import List, Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.users_models import *

class UsersOperations:

    @staticmethod
    async def find_all_users(session: AsyncSession) -> List[Users]:
        result = await session.execute(select(Users))
        return result.scalars().all()

    @staticmethod
    async def create_user(session: AsyncSession, data: dict) -> Users:
        new_entry = Users(**data)
        session.add(new_entry)
        await session.commit()
        await session.refresh(new_entry)
        return new_entry

    @staticmethod
    async def update_user(session: AsyncSession, entry_id: int, update_data: dict) -> Optional[Users]:
        """Modifica un registro existente, permitiendo cambios parciales o totales"""
        entry = await session.get(Users, entry_id)
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
    async def kill_user(session: AsyncSession, entry_id: int) -> Optional[Users]:
        entry = await session.get(Users, entry_id)
        if not entry:
            return None

        # Validar los datos antes de crear la copia
        try:
            deleted_entry = DeletedUsers(**entry.dict())
        except ValueError as e:
            # Manejar errores de validación
            raise ValueError(f"Error al validar los datos para la tabla de eliminados: {e}")

        session.add(deleted_entry)
        await session.delete(entry)
        await session.commit()
        return entry