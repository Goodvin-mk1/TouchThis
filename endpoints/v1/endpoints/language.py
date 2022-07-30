from fastapi import APIRouter, HTTPException

from schemas import LanguageSchema, LanguageInDBSchema
from crud import LanguageCRUD


language_router = APIRouter(
    prefix="/language",
    tags=["Language"]
)


@language_router.post("/add", status_code=201)
async def add_language(language: LanguageSchema):
    language = await LanguageCRUD.add(language=language)
    if language:
        return language.id
    raise HTTPException(status_code=409, detail="language is already exists")


@language_router.get("/get", response_model=LanguageInDBSchema)
async def get_language(language_id: int):
    language = await LanguageCRUD.get(language_id=language_id)
    if language:
        return language
    raise HTTPException(status_code=404, detail="language not found")


@language_router.get("/all", response_model=list[LanguageInDBSchema])
async def get_all_languages():
    languages = await LanguageCRUD.get_all()
    if languages:
        return languages
    raise HTTPException(status_code=404, detail="languages not found")


@language_router.put("/update", status_code=200)
async def update_language(language: LanguageInDBSchema):
    existing_language = await LanguageCRUD.get(language_id=language.id)
    if not existing_language:
        raise HTTPException(status_code=404, detail="language not found")
    await LanguageCRUD.update(language=language)
    return language


@language_router.delete("/del", status_code=204)
async def delete_language(language_id: int):
    language = await LanguageCRUD.get(language_id=language_id)
    if not language:
        raise HTTPException(status_code=404, detail="language not found")
    await LanguageCRUD.delete(language_id=language_id)
