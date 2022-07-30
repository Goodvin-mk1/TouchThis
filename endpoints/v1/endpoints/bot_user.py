from fastapi import APIRouter, HTTPException

from schemas import BotUserSchema, BotUserInDBSchema
from crud import BotUserCRUD


bot_user_router = APIRouter(
    prefix="/bot_user",
    tags=["Bot User"]
)


@bot_user_router.post("/add", status_code=201)
async def add_bot_user(bot_user: BotUserSchema):
    bot_user = await BotUserCRUD.add(bot_user=bot_user)
    if bot_user:
        return bot_user.id
    raise HTTPException(status_code=409, detail="bot user is already exists")


@bot_user_router.get("/get", response_model=BotUserInDBSchema)
async def get_bot_user(bot_user_id: int):
    bot_user = await BotUserCRUD.get(bot_user_id=bot_user_id)
    if bot_user:
        return bot_user
    raise HTTPException(status_code=404, detail="bot user not found")


@bot_user_router.get("/all", response_model=list[BotUserInDBSchema])
async def get_all_bot_users():
    bot_users = await BotUserCRUD.get_all()
    if bot_users:
        return bot_users
    raise HTTPException(status_code=404, detail="bot users not found")


@bot_user_router.put("/update", status_code=200)
async def update_bot_user(bot_user: BotUserInDBSchema):
    existing_bot_user = await BotUserCRUD.get(bot_user_id=bot_user.id)
    if not existing_bot_user:
        raise HTTPException(status_code=404, detail="bot user not found")
    await BotUserCRUD.update(bot_user=bot_user)
    return bot_user


@bot_user_router.delete("/del", status_code=204)
async def delete_bot_user(bot_user_id: int):
    bot_user = await BotUserCRUD.get(bot_user_id=bot_user_id)
    if not bot_user:
        raise HTTPException(status_code=404, detail="bot user not found")
    await BotUserCRUD.delete(bot_user_id=bot_user_id)
