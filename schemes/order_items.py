from pydantic import BaseModel, Field


class OrderItemScheme(BaseModel):
    order_id: int = Field(ge=1)
    product_id: int = Field(ge=1)
    total: int = Field(
        default=0,
        ge=0
    )


class OrderItemInDBScheme(OrderItemScheme):
    id: int = Field(ge=1)
