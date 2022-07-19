from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Product, create_session
from schemas.product import *


class ProductCRUD:

    @staticmethod
    @create_session
    def add(product: ProductSchema, session: Session = None
            ) -> ProductInDBSchema | None:

        product = Product(
            **product.dict()
        )
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(product)
            return ProductInDBSchema(**product.__dict__)

    @staticmethod
    @create_session
    def get(product_id: int, session: Session = None) -> ProductInDBSchema | None:
        product = session.execute(
            select(Product).where(Product.id == product_id)
        )
        product = product.first()
        if product:
            return ProductInDBSchema(**product[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[ProductInDBSchema]:
        products = session.execute(
            select(Product)
        )
        return [ProductInDBSchema(**product[0].__dict__) for product in products]

    @staticmethod
    @create_session
    def delete(product_id: int, session: Session = None) -> None:
        session.execute(
            delete(Product).where(Product.id == product_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(product: ProductInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Product).where(Product.id == product.id). values(
                **product.__dict__
            )
        )
        session.commit()
