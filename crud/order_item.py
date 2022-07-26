from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from models import OrderItem, create_async_session
from schemas.order_item import *


class OrderItemCRUD:

    @staticmethod
    @create_async_session
    async def add(order_item: OrderItemSchema, session: AsyncSession = None
                  ) -> OrderItemInDBSchema | None:

        order_item = OrderItem(
            **order_item.dict()
        )
        session.add(order_item)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(order_item)
            return OrderItemInDBSchema(**order_item.__dict__)

    @staticmethod
    @create_async_session
    async def get(order_item_id: int, session: AsyncSession = None) -> OrderItemInDBSchema | None:
        order_item = await session.execute(
            select(OrderItem).where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return OrderItemInDBSchema(**order_item[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[OrderItemInDBSchema]:
        order_items = await session.execute(
            select(OrderItem)
        )
        return [OrderItemInDBSchema(**order_item[0].__dict__) for order_item in order_items]

    @staticmethod
    @create_async_session
    async def delete(order_item_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(OrderItem).where(OrderItem.id == order_item_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(order_item: OrderItemInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(OrderItem).where(OrderItem.id == order_item.id). values(
                **order_item.__dict__
            )
        )
        await session.commit()
