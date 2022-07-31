from datetime import datetime

from jose import JWTError, jwt

from core.config import CONFIG
from fastapi import Request

from crud import UserCRUD


class AuthHelper:

    @staticmethod
    async def validate_user(request: Request):
        access_token = request.headers.get("Authorization")
        if not access_token:
            return False
        try:
            data = jwt.decode(access_token, CONFIG.AUTH.SECRET_KEY, algorithms=[CONFIG.AUTH.ALGORITHM])
        except JWTError:
            return False
        username = data.get("sub")
        if not username:
            return False
        user = await UserCRUD.get_by_username(username=username)
        if not user:
            return False
        token_expire_date = data.get("exp")
        if not token_expire_date:
            return False
        token_expire_date = datetime.utcfromtimestamp(token_expire_date)
        if datetime.utcnow() < token_expire_date:
            return True
        else:
            return False
