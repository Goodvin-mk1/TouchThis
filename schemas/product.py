from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    category_id: int = Field(ge=1)
    price: float = Field(gt=0)
    total: float = Field(gt=0)
    is_published: bool = Field(default=False)
    name: str = Field(max_length=20,
                      min_length=1)


class ProductInDBSchema(ProductSchema):
    id: int = Field(ge=1)
