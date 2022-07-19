from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Category, create_session
from schemas.category import *


class CategoryCRUD:

    @staticmethod
    @create_session
    def add(category: CategorySchema, session: Session = None
            ) -> CategoryInDBSchema | None:

        category = Category(
            **category.dict()
        )
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> CategoryInDBSchema | None:
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return CategoryInDBSchema(**category[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[CategoryInDBSchema]:
        categories = session.execute(
            select(Category)
        )
        return [CategoryInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category).where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(category: CategoryInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Category).where(Category.id == category.id). values(
                **category.__dict__
            )
        )
        session.commit()
