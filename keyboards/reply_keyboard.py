from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог"),
            KeyboardButton(text="О нас"),
        ],
        [
            KeyboardButton(text="Варианты доставки"),
            KeyboardButton(text="Варианты оплаты"),
        ],
        [
            KeyboardButton(text="Заказать обратный звонок"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вы хотели ?",
)
del_kb = ReplyKeyboardRemove()


start_kb_2 = ReplyKeyboardBuilder()
start_kb_2.add(
    KeyboardButton(text="Каталог"),
    KeyboardButton(text="О нас"),
    KeyboardButton(text="Варианты доставки"),
    KeyboardButton(text="Варианты оплаты"),
    KeyboardButton(text="Заказать обратный звонок"),
)
start_kb_2.adjust(2, 1, 2,)
