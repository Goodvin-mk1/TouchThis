from pydantic import BaseModel, Field


class StatusSchema(BaseModel):
    name: str = Field(max_length=20,
                      min_length=1)


class StatusInDBSchema(StatusSchema):
    id: int = Field(ge=1)
