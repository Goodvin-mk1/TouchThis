from pydantic import BaseModel, PostgresDsn


class DatabaseSchema(BaseModel):
    URL: PostgresDsn
    ASYNC_URL: PostgresDsn


class ConfigSchema(BaseModel):
    DATABASE: DatabaseSchema
