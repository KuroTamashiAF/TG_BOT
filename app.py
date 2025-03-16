from aiogram import Bot, Dispatcher, types
import aiogram
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

import asyncio
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmd_list import private


ALOWED_UPDATES = ["message", "edited_message"]

bot = Bot(token=os.getenv("TG_TOKEN"))

dp = Dispatcher()
dp.include_routers(
    user_private_router,
)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES)


if __name__ == "__main__":
    asyncio.run(main())
