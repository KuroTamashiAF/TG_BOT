from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import asyncio
import aiofiles
from idna import encode


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Здравствуйте это виртуальный помощник. \n " "Я помогу вам сделать заказ =)"
    )


@user_private_router.message(Command("catalog"))
async def menu_cmd(message: types.Message):
    await message.answer("Каталог")


@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("Выводится информация о боте")


@user_private_router.message(Command("feedback"))
async def feedback_cmd(message: types.Message):
    async with aiofiles.open("feedback_cal.txt", "a", encoding="utf-8") as file:
        await file.write(
            f"Перезвонить {message.date}-{message.from_user.first_name}-{message.from_user.last_name}-{message.from_user.username}\n"
        )


@user_private_router.message(F.text.lower() == "hello")
async def magic_0(message: types.Message):
    await message.answer("Да здравствуйте,  что вы хотели ? ")


@user_private_router.message(F.text)
async def magic(message: types.Message):
    await message.answer("Я вас не понял повторите")
