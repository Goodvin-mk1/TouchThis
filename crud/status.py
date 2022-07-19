from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Status, create_session
from schemas.status import *


class StatusCRUD:

    @staticmethod
    @create_session
    def add(status: StatusSchema, session: Session = None
            ) -> StatusInDBSchema | None:

        status = Status(
            **status.dict()
        )
        session.add(status)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(status)
            return StatusInDBSchema(**status.__dict__)

    @staticmethod
    @create_session
    def get(status_id: int, session: Session = None) -> StatusInDBSchema | None:
        status = session.execute(
            select(Status).where(Status.id == status_id)
        )
        status = status.first()
        if status:
            return StatusInDBSchema(**status[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[StatusInDBSchema]:
        statuses = session.execute(
            select(Status)
        )
        return [StatusInDBSchema(**status[0].__dict__) for status in statuses]

    @staticmethod
    @create_session
    def delete(status_id: int, session: Session = None) -> None:
        session.execute(
            delete(Status).where(Status.id == status_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(status: StatusInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Status).where(Status.id == status.id). values(
                **status.__dict__
            )
        )
        session.commit()
