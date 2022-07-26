from pydantic import BaseModel, Field


class LanguageSchema(BaseModel):
    language_code: int = Field(default=None)


class LanguageInDBSchema(LanguageSchema):
    id: int = Field(ge=1)
