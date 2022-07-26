from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from models import Status, create_async_session
from schemas.status import *


class StatusCRUD:

    @staticmethod
    @create_async_session
    async def add(status: StatusSchema, session: AsyncSession = None
                  ) -> StatusInDBSchema | None:

        status = Status(
            **status.dict()
        )
        session.add(status)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(status)
            return StatusInDBSchema(**status.__dict__)

    @staticmethod
    @create_async_session
    async def get(status_id: int, session: AsyncSession = None) -> StatusInDBSchema | None:
        status = await session.execute(
            select(Status).where(Status.id == status_id)
        )
        status = status.first()
        if status:
            return StatusInDBSchema(**status[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[StatusInDBSchema]:
        statuses = await session.execute(
            select(Status)
        )
        return [StatusInDBSchema(**status[0].__dict__) for status in statuses]

    @staticmethod
    @create_async_session
    async def delete(status_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Status).where(Status.id == status_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(status: StatusInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(Status).where(Status.id == status.id). values(
                **status.__dict__
            )
        )
        await session.commit()
