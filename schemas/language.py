from pydantic import BaseModel, Field


class LanguageSchema(BaseModel):
    language_code: int = Field(default=None, min_length=2, max_length=2)


class LanguageInDBSchema(LanguageSchema):
    id: int = Field(ge=1)
