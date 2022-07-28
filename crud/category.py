from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import Category, create_async_session, Product
from schemas.category import *
from schemas.product import ProductInDBSchema


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
    async def get_all(parent_id: int = None, session: AsyncSession = None) -> list[CategoryInDBSchema]:
        if parent_id:
            categories = await session.execute(
                select(Category)
                .order_by(Category.id)
                .where(Category.parent_id == parent_id)
            )
        else:
            categories = await session.execute(
                select(Category)
                .order_by(Category.id)
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

    @staticmethod
    @create_async_session
    async def get_products_by_category_id(
            category_id: int = None,
            session: AsyncSession = None
    ) -> list[tuple[CategoryInDBSchema, ProductInDBSchema]] | None:
        if category_id:
            response = await session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
                .where(Category.id == category_id)
            )
            return [
                (
                    CategoryInDBSchema(**res[0].__dict__),
                    ProductInDBSchema(**res[1].__dict__)
                ) for res in response
            ]

