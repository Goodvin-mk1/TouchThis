from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import Category, create_async_session
from schemas.category import *


class CategoryCRUD:

    @staticmethod
    @create_async_session
    async def add(category: CategorySchema, session: AsyncSession = None
                  ) -> CategoryInDBSchema | None:

        category = Category(
            **category.dict()
        )
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> CategoryInDBSchema | None:
        category = await session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return CategoryInDBSchema(**category[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[CategoryInDBSchema]:
        categories = await session.execute(
            select(Category)
        )
        return [CategoryInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Category).where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(category: CategoryInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(Category).where(Category.id == category.id).values(
                **category.__dict__
            )
        )
        await session.commit()
