from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Order, create_session
from schemas.order import *


class OrderCRUD:

    @staticmethod
    @create_session
    def add(order: OrderSchema, session: Session = None
            ) -> OrderInDBSchema | None:

        order = Order(
            **order.dict()
        )
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order)
            return OrderInDBSchema(**order.__dict__)

    @staticmethod
    @create_session
    def get(order_id: int, session: Session = None) -> OrderInDBSchema | None:
        order = session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return OrderInDBSchema(**order[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[OrderInDBSchema]:
        orders = session.execute(
            select(Order)
        )
        return [OrderInDBSchema(**order[0].__dict__) for order in orders]

    @staticmethod
    @create_session
    def delete(order_id: int, session: Session = None) -> None:
        session.execute(
            delete(Order).where(Order.id == order_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(order: OrderInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Order).where(Order.id == order.id). values(
                **order.__dict__
            )
        )
        session.commit()
