from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import aiofiles
from filters.chat_types import ChatTypeFilter
from keyboards.reply_keyboard import start_kb, start_kb_2


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Здравствуйте это виртуальный помощник. \n " "Я помогу вам сделать заказ =)",
        reply_markup=start_kb_2.as_markup(
            resize_keyboard=True, input_field_placeholder="Что вы хотели ?"
        ),
    )


@user_private_router.message(F.text.lower() == "каталог")
@user_private_router.message(Command("catalog"))
async def menu_cmd(message: types.Message):
    await message.answer("Каталог")


@user_private_router.message(F.text.lower() == "о нас")
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("Выводится информация о боте")


@user_private_router.message(
    (F.text.lower() == "Варианты оплаты") | (F.text.contains("оплат"))
)
@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    await message.answer("Варианты оплаты:")


@user_private_router.message(
    (F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки")
)
@user_private_router.message(Command("shiping"))
async def shiping_cmd(message: types.Message):
    await message.answer("Варианты доставки:")


@user_private_router.message(F.text.lower().contains("звон"))
@user_private_router.message(Command("feedback"))
async def feedback_cmd(message: types.Message):
    async with aiofiles.open("feedback_cal.txt", "a", encoding="utf-8") as file:
        await file.write(
            f"Перезвонить {message.date}-{message.from_user.id}-{message.from_user.first_name}-{message.from_user.last_name}-{message.from_user.username}\n"
        )
        await message.answer("Обратный звонок зарегистрировал")


# @user_private_router.message(F.text)
# async def final_check_text_fron_user(message: types.Message):
#     await message.answer("Я вас не понял повторите")
