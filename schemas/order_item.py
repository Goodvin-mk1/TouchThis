from pydantic import BaseModel, Field


class OrderItemSchema(BaseModel):
    order_id: int = Field(default=None, ge=1)
    product_id: int = Field(default=None, ge=1)
    total: float = Field(gt=0)


class OrderItemInDBSchema(OrderItemSchema):
    id: int = Field(ge=1)
