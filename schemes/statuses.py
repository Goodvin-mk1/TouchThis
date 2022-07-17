from pydantic import BaseModel, Field


class StatusScheme(BaseModel):
    name: str = Field(
        min_len=3,
        max_len=20
    )


class StatusInDBScheme(StatusScheme):
    id: int = Field(ge=1)
