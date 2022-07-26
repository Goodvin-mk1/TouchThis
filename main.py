import asyncio

from schemas import *
from crud import *


async def start():
    await BotUserCRUD.add(bot_user=BotUserSchema(language_id=1))
    print(await BotUserCRUD.get_all())


# async def main():
#     loop = asyncio.get_running_loop()
#     task = loop.create_task(start())
#     await task


if __name__ == '__main__':
    asyncio.run(start())
