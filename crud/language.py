from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Language, create_session
from schemas.language import *


class LanguageCRUD:

    @staticmethod
    @create_session
    def add(language: LanguageSchema, session: Session = None
            ) -> LanguageInDBSchema | None:

        language = Language(
            **language.dict()
        )
        session.add(language)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(language)
            return LanguageInDBSchema(**language.__dict__)

    @staticmethod
    @create_session
    def get(language_id: int, session: Session = None) -> LanguageInDBSchema | None:
        language = session.execute(
            select(Language).where(Language.id == language_id)
        )
        language = language.first()
        if language:
            return LanguageInDBSchema(**language[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[LanguageInDBSchema]:
        languages = session.execute(
            select(Language)
        )
        return [LanguageInDBSchema(**language[0].__dict__) for language in languages]

    @staticmethod
    @create_session
    def delete(language_id: int, session: Session = None) -> None:
        session.execute(
            delete(Language).where(Language.id == language_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(language: LanguageInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Language).where(Language.id == language.id). values(
                **language.__dict__
            )
        )
        session.commit()
