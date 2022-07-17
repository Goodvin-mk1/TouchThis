from pydantic import BaseModel, Field


class InvoiceScheme(BaseModel):
    bot_user_id: str = Field(
        min_length=1
    )
    date_create: int = Field(ge=1)
    total: int = Field(
        default=0
    )
    status_id: int = Field(ge=1)


class InvoiceInDBScheme(InvoiceScheme):
    id: str = Field(
        min_length=1
    )
