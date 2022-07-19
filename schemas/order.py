from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import TIMESTAMP


class OrderSchema(BaseModel):
    bot_user_id: int = Field(default=None, ge=1)
    date_create: TIMESTAMP = Field(default=datetime.now())
    status_id: int = Field(default=None, ge=1)
    invoice_id: int = Field(default=None, ge=1)


class OrderInDBSchema(OrderSchema):
    id: int = Field(ge=1)
