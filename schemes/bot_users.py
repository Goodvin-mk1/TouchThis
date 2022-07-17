from pydantic import BaseModel, Field


class BotUserScheme(BaseModel):
    is_blocked: bool = Field(
        default=False
    )

    balance: float = Field(
        default=0
    )
    language_id: int = Field(ge=1)


class BotUserInDBScheme(BotUserScheme):
    id: str = Field(
        min_length=1
    )
