from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name: str = Field(max_length=20,
                      min_length=1,
                      unique_items=True)
    parent_id: int = Field(default=None, ge=1)
    is_published: bool = Field(default=False)


class CategoryInDBSchema(CategorySchema):
    id: int = Field(ge=1)
