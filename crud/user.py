from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from models import User, create_async_session
from schemas.user import *


class UserCRUD:

    @staticmethod
    @create_async_session
    async def add(user: UserSchema, session: AsyncSession = None
                  ) -> bool:

        user = User(
            **user.dict()
        )
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_async_session
    async def get(user_id: int, session: AsyncSession = None) -> UserInDBSchema | None:
        user = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[UserInDBSchema]:
        users = await session.execute(
            select(User)
        )
        return [UserInDBSchema(**user[0].__dict__) for user in users]

    @staticmethod
    @create_async_session
    async def get_by_username(username: str, session: AsyncSession = None) -> UserInDBSchema | None:
        user = await session.execute(
            select(User)
            .where(User.username == username)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_async_session
    async def delete(user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User).where(User.id == user_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(user: UserInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(User).where(User.id == user.id). values(
                **user.__dict__
            )
        )
        await session.commit()
