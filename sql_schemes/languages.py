from pydantic import BaseModel, Field


class LanguageScheme(BaseModel):
    language_code: str = Field(
        min_len=3,
        max_len=12
    )


class LanguageInDBScheme(LanguageScheme):
    id: int = Field(ge=1)
