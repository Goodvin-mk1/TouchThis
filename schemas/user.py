from pydantic import BaseModel, Field


class UserRegisterSchema(BaseModel):
    username: str = Field(min_length=4, max_length=24)
    password: str = Field(default=None, min_length=12)


class UserSchema(BaseModel):
    username: str = Field(min_length=4, max_length=24)
    hashed_password: str = Field(default=None)


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
