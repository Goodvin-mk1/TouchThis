from pydantic import BaseModel, Field


class ProductScheme(BaseModel):
    category_id: int = Field(
        default=None,
        ge=1
    )
    price: float = Field(
        default=0,
        ge=0
    )
    total: float = Field(
        default=0,
        ge=0
    )
    is_published: bool = Field(
        default=False
    )
    name: str = Field(
        min_len=3,
        max_len=20
    )


class ProductInDBScheme(ProductScheme):
    id: int = Field(ge=1)
