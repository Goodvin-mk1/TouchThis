from pydantic import BaseModel, Field


class OrderScheme(BaseModel):
    bot_user_id: str = Field(
        min_length=1
    )
    date_create: int = Field(ge=1)
    status_id: int = Field(ge=1)
    invoice_id: str = Field(
        min_length=1
    )


class OrderInDBScheme(OrderScheme):
    id: int = Field(ge=1)
