from pydantic import BaseModel, Field


class BotUserSchema(BaseModel):
    is_blocked: bool = Field(default=False)
    balance: float = Field(default=0.00, ge=0)
    language_id: int = Field(ge=1)


class BotUserInDBSchema(BotUserSchema):
    id: int = Field(ge=1)
