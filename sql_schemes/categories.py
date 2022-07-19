from pydantic import BaseModel, Field


class CategoryScheme(BaseModel):
    parent_id: int = Field(
        default=None,
        ge=1
    )
    is_published: bool = Field(
        default=False
    )
    name: str = Field(
        min_len=3,
        max_len=20
    )


class CategoryInDBScheme(CategoryScheme):
    id: int = Field(ge=1)
